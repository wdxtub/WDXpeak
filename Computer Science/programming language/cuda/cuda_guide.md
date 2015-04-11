## CUDA架构

在 CUDA 的架构下,一个程序分为两个部份:host 端和 device 端。Host 端是指在 CPU 上执行 的部份,而 device 端则是在显示芯片上执行的部份。Device 端的程序又称为 "kernel(核心)"。 通常 host 端程序会将数据准备好后,复制到显卡的内存中,再由显示芯片执行 device 端程序,完 成后再由 host 端程序将结果从显卡的内存中取回。

在 CUDA 架构下,显示芯片执行时的最小单位是 thread(线程)。数个 thread 可以组成一个 block(块)。一个 block 中的 thread 能存取同一块共享的内存,而且可以快速进行同步的动作。

每一个 block 所能包含的 thread 数目是有限的。不过,执行相同程序的 block,可以组成 grid(格子)。不同 block 中的 thread 无法存取同一个共享的内存,因此无法直接互通或进行同步。因此, 不同 block 中的 thread 能合作的程度是比较低的。不过,利用这个模式,可以让程序不用担心显示芯片实际上能同时执行的 thread 数目限制。例如,一个具有很少量执行单元的显示芯片,可能会 把各个 block 中的 thread 顺序执行,而非同时执行。不同的 grid 则可以执行不同的程序(即 kernel)。

每个 thread 都有自己的一份 register 和 local memory 的空间。同一个 block 中的每个 thread 则有共享的一份 share memory。此外,所有的 thread(包括不同 block 的 thread)都共享一份 global memory、constant memory、和 texture memory。不同的 grid 则有各自的 global memory、 constant memory 和 texture memory。

## 执行模式

由于显示芯片大量并行计算的特性,它处理一些问题的方式,和一般 CPU 是不同的。主要的特点包括:

1. 内存存取 latency 的问题:CPU 通常使用 cache 来减少存取主内存的次数,以避免内存 latency 影响到执行效率。显示芯片则多半没有 cache(或很小),而利用并行化执行的方式来隐藏内存的 latency(即,当第一个 thread 需要等待内存读取结果时,则开始执行第二 个 thread,依此类推)。
2. 分支指令的问题:CPU 通常利用分支预测等方式来减少分支指令造成的 pipeline bubble。显示芯片则多半使用类似处理内存 latency 的方式。不过,通常显示芯片处理分支的效率会比较差

最适合利用 CUDA 处理的问题,是可以大量并行化的问题,才能有效隐藏内存的 latency, 并有效利用显示芯片上的大量执行单元。使用 CUDA 时,同时有上千个 thread 在执行是很正常的。 因此,如果不能大量并行化的问题,使用 CUDA 就没办法达到最好的效率了。

## 基本概念

+ streaming processor, sp: 最基本的处理单元，最后具体的指令和任务都是在 sp 上处理的。GPU 进行并行计算，也就是很多个 sp 同时做处理
+ streaming multiprocessor, sm: 多个 sp 加上存储资源组成一个 sm
+ warp: GPU 执行程序时的调度单位，目前 CUDA 的 warp 大小为32，同在一个 warp 的线程，以不同数据资源执行相同的指令。
+ thread, block, grid: 利用 CUDA 进行编程时，一个 grid 分为多个 block，一个 block 分为多个 thread (From a programmer’s perspective)

### Some Restrictions First

+ All threads in a grid execute the same kernel function
+ A grid is organized as a 2D array of blocks(gridDim.X and gridDim.y)
+ Each block is organized as 3D array of threads(blockDim.x, blockDim.y, and blockDim.z)
+ Once a kernel is launched, its dimensions cannot change.
+ All blocks in a grid have the same dimension
+ The total size of a block is limited to 512 threads(? I’m not sure?)
+ Once assigned to an SM, the block must execute in its entirey by the SM.
+ Thread ID is unique within a block
+ Using block ID and thread ID we can make unique ID for each thread per kernel
+ Threads assigned to execution resources on a block-by-block basis
+ CUDA runtime automatically reduces number of blocks assigned to each SM
+ until resource usage is under limit.

### SM -Streaming multi-processors with multiple processing cores

+ Each SM contains 32 processing cores
+ Execute in a Single Instruction Multiple Thread (SIMT) fashion
+ Up to 16 SMs on a card cor a maximum of 512 compute cores

### Warps

+ Once a block is assigned to an SM, it is divided into units called warps.
+ Thread IDs within a warp are consecutive and increasing
+ Warp 0 starts with Thread ID 0
+ Warp is unit of thread scheduling in SMs
+ Partitioning is always the same
+ DO NOT rely on any ordering between warps
+ Each warp is executed in a SIMD fashion (all threads within a warp must execute the same instruction at any given time)
+ Problem: branch divergence

### Latency Tolerance

+ When an instruction executed by the threads in a warp must wait for the result of a previously initiated long-latency operation, the warp is not selected for execution -> lantency hiding
+ Priority mechanism used to schedule ready warps
+ Scheduling does not introduce idle time -> zero-overhead thread scheduling
+ Scheduling is used for telerating long-latency operations, such as:
+ piplined floating-point arithmetic
+ branch instructions

The only safe way to synchronize threads in different blocks is to terminate the kernel and start a new kernel for the acitivities after the synchronization point.

## 代码相关

+ 通过 cudaGetDeviceProperties 函数可以取得许多数据，除了装置支持的 CUDA 版本之外, 还有装置的名称、内存的大小、最大的 thread 数目、执行单元的频率等等
+ 需要包含头文件`<cuda_runtime.h>`
+ 编译直接可以`nvcc xxx.cu`
+ nvcc 是 CUDA 的 compile 工具,它会将 .cu 檔拆解出在 GPU 上执行的部份,及在 host 上执 行的部份,并呼叫适当的程序进行 compile 动作。在 GPU 执行的部份会透过 NVIDIA 提供的 compiler 编译成中介码,而 host 执行的部份则会透过系统上的 C++ compiler 编译(在 Windows 上使用 Visual C++ 而在 Linux 上使用 gcc)
+ cudaMalloc 和 cudaMemcpy 的用法和一般的 malloc 及 memcpy 类似,不过 cudaMemcpy 则多出一个参数,指示复制内存的方向。从主内存复制到显卡内存,所以使用 cudaMemcpyHostToDevice。如果是从显卡内存到主内存,则使用 cudaMemcpyDeviceToHost。
+ 在 CUDA 中，在函数前面加上 `__global__` 表示这个函数是要在显示芯片上执行的。
+ 在显卡上执行的程序有一些限制，例如它不能有返回值
+ 让 CUDA 执行函数的语法
    + `function<<<# block, # thread, shared memory size>>>(para....)`
+ 在 CUDA 中,一般的数据复制到的显卡内存的部份,称为 global memory。这些内存是没有 cache 的,而且,存取 global memory 所需要的时间(即 latency)是非常长的,通常是数百个 cycles。由于我们的程序只有一 个 thread,所以每次它读取 global memory 的内容,就要等到实际读取到数据、累加到 sum 之后, 才能进行下一步。
+ 由于 global memory 并没有 cache,所以要避开巨大的 latency 的方法,就是要利用大量的 threads。假设现在有大量的 threads 在同时执行,那么当一个 thread 读取内存,开始等待结果的 时候,GPU 就可以立刻切换到下一个 thread,并读取下一个内存位置。因此,理想上当 thread 的 数目够多的时候,就可以完全把 global memory 的巨大 latency 隐藏起来了。
+ 显卡上的内存是 DRAM,因此最有效率的存取方式,是以连续的方式存取。前面的程序,虽然看起 来是连续存取内存位置(每个 thread 对一块连续的数字计算平方和),但是我们要考虑到实际上 thread 的执行方式。前面提过,当一个 thread 在等待内存的数据时,GPU 会切换到下一个 thread。 也就是说,实际上执行的顺序是类似 thread0 -> thread1 -> thread2。因此,在同一个 thread 中连续存取内存,在实际执行时反而不是连续了。要让实际执行结果是连续 的存取,我们应该要让 thread 0 读取第一个数字,thread 1 读取第二个数字...依此类推。
+ 在 CUDA 中,thread 是可以分组的,也就是 block。一个 block 中的 thread,具有一个共享的 shared memory,也可以进行同步工作。不同 block 之间的 thread 则不行。在我们的程序中,其 实不太需要进行 thread 的同步动作,因此我们可以使用多个 block 来进一步增加 thread 的数目
+ 利用 `__shared__` 声明的变量表示这是 shared memory,是一个 block 中每个 thread 都共享的 内存。它会使用在 GPU 上的内存,所以存取的速度相当快,不需要担心 latency 的问题。
+ `__syncthreads()`` 是一个 CUDA 的内部函数,表示 block 中所有的 thread 都要同步到这个点,才能继续执行。

## 经验技巧

+ 利用 `threadIdx.x` 来分 thread 执行，考虑好邻接性。
￼
