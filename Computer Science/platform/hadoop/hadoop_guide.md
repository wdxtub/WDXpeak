# Hadoop Guide

## 概述

Hadoop Map/Reduce是一个使用简易的软件框架，基于它写出来的应用程序能够运行在由上千个商用机器组成的大型集群上，并以一种可靠容错的方式并行处理上T级别的数据集。

一个Map/Reduce 作业（job） 通常会把输入的数据集切分为若干独立的数据块，由 map任务（task）以完全并行的方式处理它们。框架会对map的输出先进行排序， 然后把结果输入给reduce任务。通常作业的输入和输出都会被存储在文件系统中。 整个框架负责任务的调度和监控，以及重新执行已经失败的任务。

通常，Map/Reduce框架和分布式文件系统是运行在一组相同的节点上的，也就是说，计算节点和存储节点通常在一起。这种配置允许框架在那些已经存好数据的节点上高效地调度任务，这可以使整个集群的网络带宽被非常高效地利用。

Map/Reduce框架由一个单独的master JobTracker 和每个集群节点一个slave TaskTracker共同组成。master负责调度构成一个作业的所有任务，这些任务分布在不同的slave上，master监控它们的执行，重新执行已经失败的任务。而slave仅负责执行由master指派的任务。

应用程序至少应该指明输入/输出的位置（路径），并通过实现合适的接口或抽象类提供map和reduce函数。再加上其他作业的参数，就构成了作业配置（job configuration）。然后，Hadoop的 job client提交作业（jar包/可执行程序等）和配置信息给JobTracker，后者负责分发这些软件和配置信息给slave、调度任务并监控它们的执行，同时提供状态和诊断信息给job-client。

虽然Hadoop框架是用JavaTM实现的，但Map/Reduce应用程序则不一定要用 Java来写 。

## 输入与输出

Map/Reduce框架运转在`<key, value>` 键值对上，也就是说， 框架把作业的输入看为是一组`<key, value>` 键值对，同样也产出一组 `<key, value>` 键值对做为作业的输出，这两组键值对的类型可能不同。

框架需要对key和value的类(classes)进行序列化操作， 因此，这些类需要实现 Writable接口。 另外，为了方便框架执行排序操作，key类必须实现 WritableComparable接口。

一个Map/Reduce 作业的输入和输出类型如下所示：

    (input) <k1, v1> -> map -> <k2, v2> -> combine -> <k2, v2> -> reduce -> <k3, v3> (output)


## 核心功能描述

应用程序通常会通过提供map和reduce来实现 Mapper和Reducer接口，它们组成作业的核心。

### Mapper

Mapper将输入键值对(key/value pair)映射到一组中间格式的键值对集合。

Map是一类将输入记录集转换为中间格式记录集的独立任务。 这种转换的中间格式记录集不需要与输入记录集的类型一致。一个给定的输入键值对可以映射成0个或多个输出键值对。

Hadoop Map/Reduce框架为每一个InputSplit产生一个map任务，而每个InputSplit是由该作业的InputFormat产生的。

概括地说，对Mapper的实现者需要重写 JobConfigurable.configure(JobConf)方法，这个方法需要传递一个JobConf参数，目的是完成Mapper的初始化工作。然后，框架为这个任务的InputSplit中每个键值对调用一次 map(WritableComparable, Writable, OutputCollector, Reporter)操作。应用程序可以通过重写Closeable.close()方法来执行相应的清理工作。

输出键值对不需要与输入键值对的类型一致。一个给定的输入键值对可以映射成0个或多个输出键值对。通过调用 OutputCollector.collect(WritableComparable,Writable)可以收集输出的键值对。

应用程序可以使用Reporter报告进度，设定应用级别的状态消息，更新Counters（计数器），或者仅是表明自己运行正常。

框架随后会把与一个特定key关联的所有中间过程的值（value）分成组，然后把它们传给Reducer以产出最终的结果。用户可以通过 JobConf.setOutputKeyComparatorClass(Class)来指定具体负责分组的 Comparator。

Mapper的输出被排序后，就被划分给每个Reducer。分块的总数目和一个作业的reduce任务的数目是一样的。用户可以通过实现自定义的 Partitioner来控制哪个key被分配给哪个 Reducer。

用户可选择通过 JobConf.setCombinerClass(Class)指定一个combiner，它负责对中间过程的输出进行本地的聚集，这会有助于降低从Mapper到 Reducer数据传输量。

这些被排好序的中间过程的输出结果保存的格式是(key-len, key, value-len, value)，应用程序可以通过JobConf控制对这些中间结果是否进行压缩以及怎么压缩，使用哪种 CompressionCodec。

### 需要多少个Map？

Map的数目通常是由输入数据的大小决定的，一般就是所有输入文件的总块（block）数。

Map正常的并行规模大致是每个节点（node）大约10到100个map，对于CPU 消耗较小的map任务可以设到300个左右。由于每个任务初始化需要一定的时间，因此，比较合理的情况是map执行的时间至少超过1分钟。

这样，如果你输入10TB的数据，每个块（block）的大小是128MB，你将需要大约82,000个map来完成任务，除非使用 setNumMapTasks(int)（注意：这里仅仅是对框架进行了一个提示(hint)，实际决定因素见这里）将这个数值设置得更高。

### Reducer

Reducer将与一个key关联的一组中间数值集归约（reduce）为一个更小的数值集。

用户可以通过 JobConf.setNumReduceTasks(int)设定一个作业中reduce任务的数目。

概括地说，对Reducer的实现者需要重写 JobConfigurable.configure(JobConf)方法，这个方法需要传递一个JobConf参数，目的是完成Reducer的初始化工作。然后，框架为成组的输入数据中的每个`<key, (list of values)>`对调用一次 reduce(WritableComparable, Iterator, OutputCollector, Reporter)方法。之后，应用程序可以通过重写Closeable.close()来执行相应的清理工作。

Reducer有3个主要阶段：shuffle、sort和reduce。

#### Shuffle

Reducer的输入就是Mapper已经排好序的输出。在这个阶段，框架通过HTTP为每个Reducer获得所有Mapper输出中与之相关的分块。

#### Sort

这个阶段，框架将按照key的值对Reducer的输入进行分组 （因为不同mapper的输出中可能会有相同的key）。

Shuffle和Sort两个阶段是同时进行的；map的输出也是一边被取回一边被合并的。

#### Secondary Sort

如果需要中间过程对key的分组规则和reduce前对key的分组规则不同，那么可以通过 JobConf.setOutputValueGroupingComparator(Class)来指定一个Comparator。再加上 JobConf.setOutputKeyComparatorClass(Class)可用于控制中间过程的key如何被分组，所以结合两者可以实现按值的二次排序。

#### Reduce

在这个阶段，框架为已分组的输入数据中的每个 `<key, (list of values)>`对调用一次 reduce(WritableComparable, Iterator, OutputCollector, Reporter)方法。

Reduce任务的输出通常是通过调用 OutputCollector.collect(WritableComparable, Writable)写入 文件系统的。

应用程序可以使用Reporter报告进度，设定应用程序级别的状态消息，更新Counters（计数器），或者仅是表明自己运行正常。

Reducer的输出是没有排序的。

### 需要多少个Reduce？

Reduce的数目建议是0.95或1.75乘以 `<no. of nodes> * mapred.tasktracker.reduce.tasks.maximum`。

用0.95，所有reduce可以在maps一完成时就立刻启动，开始传输map的输出结果。用1.75，速度快的节点可以在完成第一轮reduce任务后，可以开始第二轮，这样可以得到比较好的负载均衡的效果。

增加reduce的数目会增加整个框架的开销，但可以改善负载均衡，降低由于执行失败带来的负面影响。

上述比例因子比整体数目稍小一些是为了给框架中的推测性任务（speculative-tasks） 或失败的任务预留一些reduce的资源。

### 无Reducer

如果没有归约要进行，那么设置reduce任务的数目为零是合法的。

这种情况下，map任务的输出会直接被写入由 setOutputPath(Path)指定的输出路径。框架在把它们写入FileSystem之前没有对它们进行排序。

### Partitioner

Partitioner用于划分键值空间（key space）。

Partitioner负责控制map输出结果key的分割。Key（或者一个key子集）被用于产生分区，通常使用的是Hash函数。分区的数目与一个作业的reduce任务的数目是一样的。因此，它控制将中间过程的key（也就是这条记录）应该发送给m个reduce任务中的哪一个来进行reduce操作。

HashPartitioner是默认的 Partitioner。

### Reporter

Reporter是用于Map/Reduce应用程序报告进度，设定应用级别的状态消息， 更新Counters（计数器）的机制。

Mapper和Reducer的实现可以利用Reporter 来报告进度，或者仅是表明自己运行正常。在那种应用程序需要花很长时间处理个别键值对的场景中，这种机制是很关键的，因为框架可能会以为这个任务超时了，从而将它强行杀死。另一个避免这种情况发生的方式是，将配置参数mapred.task.timeout设置为一个足够高的值（或者干脆设置为零，则没有超时限制了）。

应用程序可以用Reporter来更新Counter（计数器）。

### OutputCollector

OutputCollector是一个Map/Reduce框架提供的用于收集 Mapper或Reducer输出数据的通用机制 （包括中间输出结果和作业的输出结果）。

Hadoop Map/Reduce框架附带了一个包含许多实用型的mapper、reducer和partitioner 的类库。

## 作业配置

JobConf代表一个Map/Reduce作业的配置。

JobConf是用户向Hadoop框架描述一个Map/Reduce作业如何执行的主要接口。框架会按照JobConf描述的信息忠实地去尝试完成这个作业，然而：

+ 一些参数可能会被管理者标记为 final，这意味它们不能被更改。
+ 一些作业的参数可以被直截了当地进行设置（例如： setNumReduceTasks(int)），而另一些参数则与框架或者作业的其他参数之间微妙地相互影响，并且设置起来比较复杂（例如： setNumMapTasks(int)）。

通常，JobConf会指明Mapper、Combiner(如果有的话)、 Partitioner、Reducer、InputFormat和 OutputFormat的具体实现。JobConf还能指定一组输入文件 (setInputPaths(JobConf, Path...) /addInputPath(JobConf, Path)) 和(setInputPaths(JobConf, String) /addInputPaths(JobConf, String)) 以及输出文件应该写在哪儿 (setOutputPath(Path))。

JobConf可选择地对作业设置一些高级选项，例如：设置Comparator； 放到DistributedCache上的文件；中间结果或者作业输出结果是否需要压缩以及怎么压缩； 利用用户提供的脚本(setMapDebugScript(String)/setReduceDebugScript(String)) 进行调试；作业是否允许预防性（speculative）任务的执行 (setMapSpeculativeExecution(boolean))/(setReduceSpeculativeExecution(boolean)) ；每个任务最大的尝试次数 (setMaxMapAttempts(int)/setMaxReduceAttempts(int)) ；一个作业能容忍的任务失败的百分比 (setMaxMapTaskFailuresPercent(int)/setMaxReduceTaskFailuresPercent(int)) ；等等。

当然，用户能使用 set(String, String)/get(String, String) 来设置或者取得应用程序需要的任意参数。然而，DistributedCache的使用是面向大规模只读数据的。

## 任务的执行和环境

TaskTracker是在一个单独的jvm上以子进程的形式执行 Mapper/Reducer任务（Task）的。

子任务会继承父TaskTracker的环境。用户可以通过JobConf中的 mapred.child.java.opts配置参数来设定子jvm上的附加选项，例如： 通过-Djava.library.path=<> 将一个非标准路径设为运行时的链接用以搜索共享库，等等。如果mapred.child.java.opts包含一个符号@taskid@， 它会被替换成map/reduce的taskid的值。

下面是一个包含多个参数和替换的例子，其中包括：记录jvm GC日志； JVM JMX代理程序以无密码的方式启动，这样它就能连接到jconsole上，从而可以查看子进程的内存和线程，得到线程的dump；还把子jvm的最大堆尺寸设置为512MB， 并为子jvm的java.library.path添加了一个附加路径。

    <property> 
      <name>mapred.child.java.opts</name> 
      <value> 
         -Xmx512M -Djava.library.path=/home/mycompany/lib -verbose:gc -Xloggc:/tmp/@taskid@.gc 
         -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false 
      </value> 
    </property>

用户或管理员也可以使用mapred.child.ulimit设定运行的子任务的最大虚拟内存。mapred.child.ulimit的值以（KB)为单位，并且必须大于或等于-Xmx参数传给JavaVM的值，否则VM会无法启动。

注意：mapred.child.java.opts只用于设置task tracker启动的子任务。为守护进程设置内存选项请查看 cluster_setup.html
