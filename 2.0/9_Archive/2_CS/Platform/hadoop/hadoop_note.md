# Hadoop 原理学习

Hadoop 是 Apache 下的一个项目，由 HDFS、MapReduce、HBase、Hive 和 ZooKeeper 等成员组成。其中，HDFS 和 MapReduce 是两个最基础最重要的成员。

HDFS 是 Google GFS 的开源版本，一个高度容错的分布式文件系统，它能够提供高吞吐量的数据访问，适合存储海量(PB 级)的大文件(通常超过64M)，其原理如下图所示：

![hdfs](./_resources/hadoop1.jpg)

采用 Master/Slave 结构。NameNode 维护集群内的元数据，对外提供创建、打开、删除和重命名文件或目录的功能。DataNode 存储数据，并提负责处理数据的读写请求。DataNode 定期向 NameNode 上报心跳，NameNode 通过响应心跳来控制 DataNode。

Hadoop MapReduce的实现也采用了Master/Slave 结构。Master 叫做 JobTracker，而 Slave 叫做TaskTracker。用户提交的计算叫做 Job，每一个 Job 会被划分成若干个 Tasks。JobTracker 负责 Job 和 Tasks 的调度，而 TaskTracker 负责执行 Tasks。

## Shuffle 和 Sort 分析

MapReduce 框架的核心步骤主要分两部分：Map 和 Reduce。当你向 MapReduce 框架提交一个计算作业时，它会首先把计算作业拆分成若干个 Map 任务，然后分配到不同的节点上去执行，每一个 Map 任务处理输入数据中的一部分，当 Map 任务完成后，它会生成一些中间文件，这些中间文件将会作为 Reduce 任务的输入数据。Reduce 任务的主要目标就是把前面若干个 Map 的输出汇总到一起并输出。从高层抽象来看，MapReduce 的数据流图如下图所示：

![data flow](./_resources/hadoop2.jpg)

在本文中，Shuffle 是指从 Map 产生输出开始，包括系统执行排序以及传送 Map 输出到 Reducer 作为输入的过程。在这里我们将去探究 Shuffle 是如何工作的，因为对基础的理解有助于对 MapReduce 程序进行调优。

首先从 Map 端开始分析，当 Map 开始产生输出的时候，他并不是简单的把数据写到磁盘，因为频繁的操作会导致性能严重下降，他的处理更加复杂，数据首先是写到内存中的一个缓冲区，并作一些预排序，以提升效率，如图：

![shuffle and sort](./_resources/hadoop3.jpg)

每个 Map 任务都有一个用来写入输出数据的循环内存缓冲区，这个缓冲区默认大小是 100M，可以通过 `io.sort.mb` 属性来设置具体的大小，当缓冲区中的数据量达到一个特定的阀值 `(io.sort.mb * io.sort.spill.percent，其中io.sort.spill.percent 默认是0.80)`时，系统将会启动一个后台线程把缓冲区中的内容 spill 到磁盘。在 spill 过程中，Map 的输出将会继续写入到缓冲区，但如果缓冲区已经满了，Map 就会被阻塞直到 spill 完成。spill 线程在把缓冲区的数据写到磁盘前，会对他进行一个二次排序，首先根据数据所属的 partition 排序，然后每个 partition 中再按 Key 排序。输出包括一个索引文件和数据文件，如果设定了Combiner，将在排序输出的基础上进行。Combiner 就是一个 Mini Reducer，它在执行 Map 任务的节点本身运行，先对 Map 的输出作一次简单的 Reduce，使得 Map 的输出更紧凑，更少的数据会被写入磁盘和传送到 Reducer。Spill 文件保存在由 `mapred.local.dir` 指定的目录中，Map 任务结束后删除。

每当内存中的数据达到 spill 阀值的时候，都会产生一个新的 spill 文件，所以在 Map 任务写完他的最后一个输出记录的时候，可能会有多个 spill 文件，在 Map 任务完成前，所有的 spill 文件将会被归并排序为一个索引文件和数据文件。如下图所示。这是一个多路归并过程，最大归并路数由 `io.sort.factor` 控制(默认是10)。如果设定了 Combiner，并且 spill 文件的数量至少是 3（由`min.num.spills.for.combine` 属性控制），那么 Combiner 将在输出文件被写入磁盘前运行以压缩数据。

![map output](./_resources/hadoop4.jpg)

对写入到磁盘的数据进行压缩（这种压缩同 Combiner 的压缩不一样）通常是一个很好的方法，因为这样做使得数据写入磁盘的速度更快，节省磁盘空间，并减少需要传送到 Reducer 的数据量。默认输出是不被压缩的，但可以很简单的设置 `mapred.compress.map.output` 为 `true` 启用该功能。压缩所使用的库由 `mapred.map.output.compression.codec` 来设定

当 spill 文件归并完毕后，Map 将删除所有的临时 spill 文件，并告知 TaskTracker 任务已完成。Reducers 通过 HTTP 来获取对应的数据。用来传输 partitions 数据的工作线程个数由 `tasktracker.http.threads` 控制，这个设定是针对每一个 TaskTracker 的，并不是单个 Map，默认值为 40，在运行大作业的大集群上可以增大以提升数据传输速率。

现在让我们转到 Shuffle 的 Reduce 部分。Map 的输出文件放置在运行 Map 任务的 TaskTracker 的本地磁盘上（注意：Map 输出总是写到本地磁盘，但是 Reduce 输出不是，一般是写到 HDFS），它是运行 Reduce 任务的 TaskTracker 所需要的输入数据。Reduce 任务的输入数据分布在集群内的多个 Map 任务的输出中，Map 任务可能会在不同的时间内完成，只要有其中一个 Map 任务完成，Reduce 任务就开始拷贝他的输出。这个阶段称为拷贝阶段，Reduce 任务拥有多个拷贝线程，可以并行的获取 Map 输出。可以通过设定 `mapred.reduce.parallel.copies` 来改变线程数。

Reduce 是怎么知道从哪些 TaskTrackers 中获取 Map 的输出呢？当 Map 任务完成之后，会通知他们的父 TaskTracker，告知状态更新，然后 TaskTracker 再转告 JobTracker，这些通知信息是通过心跳通信机制传输的，因此针对以一个特定的作业，jobtracker 知道 Map 输出与 tasktrackers 的映射关系。Reducer 中有一个线程会间歇的向 JobTracker 询问 Map 输出的地址，直到把所有的数据都取到。在 Reducer 取走了 Map 输出之后，TaskTracker 不会立即删除这些数据，因为 Reducer 可能会失败，他们会在整个作业完成之后，JobTracker 告知他们要删除的时候才去删除。

如果 Map 输出足够小，他们会被拷贝到 Reduce TaskTracker 的内存中（缓冲区的大小由 `mapred.job.shuffle.input.buffer.percnet` 控制），或者达到了 Map 输出的阀值的大小(由 `mapred.inmem.merge.threshold` 控制)，缓冲区中的数据将会被归并然后 spill 到磁盘。

拷贝来的数据叠加在磁盘上，有一个后台线程会将它们归并为更大的排序文件，这样做节省了后期归并的时间。对于经过压缩的 Map 输出，系统会自动把它们解压到内存方便对其执行归并。

当所有的 Map 输出都被拷贝后，Reduce 任务进入排序阶段（更恰当的说应该是归并阶段，因为排序在 Map 端就已经完成），这个阶段会对所有的 Map 输出进行归并排序，这个工作会重复多次才能完成。

假设这里有 50 个 Map 输出（可能有保存在内存中的），并且归并因子是 10（由 `io.sort.factor` 控制，就像 Map 端的 merge 一样），那最终需要 5 次归并。每次归并会把 10 个文件归并为一个，最终生成 5 个中间文件。在这一步之后，系统不再把 5 个中间文件归并成一个，而是排序后直接“喂”给 Reduce 函数，省去向磁盘写数据这一步。最终归并的数据可以是混合数据，既有内存上的也有磁盘上的。由于归并的目的是归并最少的文件数目，使得在最后一次归并时总文件个数达到归并因子的数目，所以每次操作所涉及的文件个数在实际中会更微妙些。譬如，如果有 40 个文件，并不是每次都归并 10 个最终得到 4 个文件，相反第一次只归并 4 个文件，然后再实现三次归并，每次 10 个，最终得到 4 个归并好的文件和 6 个未归并的文件。要注意，这种做法并没有改变归并的次数，只是最小化写入磁盘的数据优化措施，因为最后一次归并的数据总是直接送到 Reduce 函数那里。在Reduce 阶段，Reduce 函数会作用在排序输出的每一个 key 上。这个阶段的输出被直接写到输出文件系统，一般是 HDFS。在 HDFS 中，因为 TaskTracker 节点也运行着一个 DataNode 进程，所以第一个块备份会直接写到本地磁盘。到此，MapReduce 的 Shuffle 和 Sort 分析完毕。

## 工作原理

+ Client: 作业提交发起者。
+ JobTracker: 初始化作业，分配作业，与 TaskTracker 通信，协调整个作业。
+ TaskTracker: 保持 JobTracker 通信，在分配的数据片段上执行 MapReduce 任务。

提交作业

+ 在作业提交之前，需要对作业进行配置
+ 程序代码，主要是自己书写的 MapReduce 程序。
+ 输入输出路径
+ 其他配置，如输出压缩等。
+ 配置完成后，通过 JobClinet 来提交

作业的初始化

+ 客户端提交完成后，JobTracker 会将作业加入队列，然后进行调度，默认的调度方法是 FIFO 调试方式。

任务的分配

+ TaskTracker 和 JobTracker 之间的通信与任务的分配是通过心跳机制完成的。
+ TaskTracker 会主动向 JobTracker 询问是否有作业要做，如果自己可以做，那么就会申请到作业任务，这个任务可以是 Map 也可能是 Reduce 任务。

任务的执行

+ 申请到任务后，TaskTracker 会做如下事情：
    + 拷贝代码到本地
    + 拷贝任务的信息到本地
    + 启动JVM运行任务

状态与任务的更新

+ 任务在运行过程中，首先会将自己的状态汇报给 TaskTracker，然后由 TaskTracker 汇总告知 JobTracker。
+ 任务进度是通过计数器来实现的。

作业的完成

+ JobTracker 是在接受到最后一个任务运行完成后，才会将任务标志为成功。
+ 此时会做删除中间结果等善后处理工作。

## 错误处理

任务失败

+ MapReduce 在设计之出，就假象任务会失败，所以做了很多工作，来保证容错。
+ 一种情况: 子任务失败
+ 另一种情况: 子任务的 JVM 突然退出
+ 任务的挂起

TaskTracker 失败

+ TaskTracker 崩溃后会停止向 Jobtracker 发送心跳信息。
+ Jobtracker 会将该 TaskTracker 从等待的任务池中移除。并将该 TaskTracker 上的任务，移动到其他地方去重新运行。
+ TaskTracker 可以被 JobTracker 放入到黑名单，即使它没有失败。

JobTracker失败

+ 单点故障，Hadoop 新的0.23版本解决了这个问题。

## 作业调度

+ FIFO: Hadoop 中默认的调度器，它先按照作业的优先级高低，再按照到达时间的先后选 择被执行的作业
+ 公平调度器: 为任务分配资源的方法，其目的是随着时间的推移，让提交的作业获取等量的集 群共享资源，让用户公平地共享集群。具体做法是：当集群上只有一个任务在运行 时，它将使用整个集群，当有其他作业提交时，系统会将 TaskTracker 节点空间的时 间片分配给这些新的作业，并保证每个任务都得到大概等量的CPU时间。
+ 容量调度器: 支持多个队列，每个队列可配置一定的资源量，每个队列采用 FIFO 调度策略，为了防止同一个用户的作业独占队列中的资源，该调度器会对同一用户提交的作业所占资源量进行限定。调度时，首先按以下策略选择一个合适队列：计算每个队列中正在运行的任务数与其应该分得的计算资源之间的比值，选择一个该比值最小的队列；然后按以下策略选择该队列中一个作业：按照作业优先级和提交时间顺序选择 ，同时考虑用户资源量限制和内存限制。但是不可剥夺式

## Shuffle & Sort

Mapreduce 的 map 结束后，把数据重新组织，作为 reduce 阶段的输入，该过程称之为 shuffle -- 洗牌。而数据在 Map 与 Reduce 端都会做排序。

Map

+ Map 的输出是由 collector 控制的
+ 我们从 collect 函数入手

Reduce

+ reduce 的 Shuffle 过程，分成三个阶段：复制 Map 输出、排序合并、reduce 处理。
+ 主要代码在 reduce的 run 函数

Shuffle优化

+ 首先 Hadoop 的 Shuffle 在某些情况并不是最优的，例如，如果需要对2集合合并，那么其实排序操作时不需要的。
+ 我们可以通过调整参数来优化 Shuffle
+ Map端: io.sort.mb
+ Reduce端: mapred.job.reduce.input.buffer.percent

## 任务的执行时的一些特有的概念

推测式执行

+ 每一道作业的任务都有运行时间，而由于机器的异构性，可能会会造成某些任务会比所有任务的平均运行时间要慢很多。
+ 这时 MapReduce 会尝试在其他机器上重启慢的任务。为了是任务快速运行完成。
+ 该属性默认是启用的。

JVM重用

+ 启动 JVM 是一个比较耗时的工作，所以在 MapReduce 中有 JVM 重用的机制。
+ 条件是统一个作业的任务。
+ 可以通过 `mapred.job.reuse.jvm.num.tasks`定义重用次数，如果属性是 -1 那么为无限制。

跳过坏记录

+ 数据的一些记录不符合规范，处理时抛出异常，MapReduce 可以讲次记录标为坏记录。重启任务时会跳过该记录。
+ 默认情况下该属性是关闭的。

任务执行环境

+ Hadoop 为 Map 与 Reduce 任务提供运行环境。
+ 如：Map 可以知道自己的处理的文件
+ 问题：多个任务可能会同时写一个文件
+ 解决办法：将输出写到任务的临时文件夹。目录为：{mapred.out. put.dir}/temp/${mapred.task.id}


## 流程分析

Map端：

1. 每个输入分片会让一个 map 任务来处理，默认情况下，以 HDFS 的一个块的大小（默认为 64M）为一个分片，当然我们也可以设置块的大小。map 输出的结果会暂且放在一个环形内存缓冲区中（该缓冲区的大小默认为 100M，由 `io.sort.mb` 属性控制），当该缓冲区快要溢出时（默认为缓冲区大小的80%，由 `io.sort.spill.percent` 属性控制），会在本地文件系统中创建一个溢出文件，将该缓冲区中的数据写入这个文件。
2. 在写入磁盘之前，线程首先根据 reduce 任务的数目将数据划分为相同数目的分区，也就是一个 reduce 任务对应一个分区的数据。这样做是为了避免有些 reduce 任务分配到大量数据，而有些 reduce 任务却分到很少数据，甚至没有分到数据的尴尬局面。其实分区就是对数据进行 hash 的过程。然后对每个分区中的数据进行排序，如果此时设置了 Combiner，将排序后的结果进行 Combiner 操作，这样做的目的是让尽可能少的数据写入到磁盘。
3. 当 map 任务输出最后一个记录时，可能会有很多的溢出文件，这时需要将这些文件合并。合并的过程中会不断地进行排序和 combiner 操作，目的有两个：1.尽量减少每次写入磁盘的数据量；2.尽量减少下一复制阶段网络传输的数据量。最后合并成了一个已分区且已排序的文件。为了减少网络传输的数据量，这里可以将数据压缩，只要将 `mapred.compress.map.out` 设置为 true 就可以了。
4. 将分区中的数据拷贝给相对应的 reduce 任务。有人可能会问：分区中的数据怎么知道它对应的 reduce 是哪个呢？其实 map 任务一直和其父 TaskTracker 保持联系，而 TaskTracker 又一直和 JobTracker 保持心跳。所以 JobTracker 中保存了整个集群中的宏观信息。只要 reduce 任务向 JobTracker 获取对应的 map 输出位置就ok了哦。

到这里，map 端就分析完了。那到底什么是 Shuffle 呢？Shuffle 的中文意思是“洗牌”，如果我们这样看：一个 map 产生的数据，结果通过 hash 过程分区却分配给了不同的 reduce 任务，是不是一个对数据洗牌的过程呢？呵呵。

Reduce端：

1. Reduce 会接收到不同 map 任务传来的数据，并且每个 map 传来的数据都是有序的。如果 reduce 端接受的数据量相当小，则直接存储在内存中（缓冲区大小由 `mapred.job.shuffle.input.buffer.percent` 属性控制，表示用作此用途的堆空间的百分比），如果数据量超过了该缓冲区大小的一定比例（由 `mapred.job.shuffle.merge.percent` 决定），则对数据合并后溢写到磁盘中。
2. 随着溢写文件的增多，后台线程会将它们合并成一个更大的有序的文件，这样做是为了给后面的合并节省时间。其实不管在 map 端还是 reduce 端，MapReduce 都是反复地执行排序，合并操作，现在终于明白了有些人为什么会说：排序是 hadoop 的灵魂。
3. 合并的过程中会产生许多的中间文件（写入磁盘了），但 MapReduce 会让写入磁盘的数据尽可能地少，并且最后一次合并的结果并没有写入磁盘，而是直接输入到 reduce 函数。
