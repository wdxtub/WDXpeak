## Module 1.2

+ What are the differences between multicore and manycore processors?
    * Multicore: yoke of oxen. Each core optimized for executing a single thread.
    * Manycore: flock of chickens. Cores optimized for aggregate throughput, deemphasizing individual performance.
+ What is instruction level parallelism? What is SIMD?
    * ILP: Instructions in a sequence that can be computed at the same time.
    * ILP(wiki): a measure of how many of the operations in a computer program can be performed simultaneously
    * SIMD(wiki): computers with multiple processing elements that perform the same operation on multiple data points simultaneously. data level parallelism. 
+ What is simultaneous multithreading?
    * a technique for improving the overall efficiency of superscalar CPUs with hardware multithreading. SMT permits multiple independent threads of execution to better utilize the resources provided by modern processor architectures.
+ What are the three metrics for a memory hierarchy?
    * Capacity: Size, e.g. number of bytes of data
    * Latency: From start to finish, in units of time, e.g. CPU clock cycles
    * Throughput: Tasks accomplished per unit time, e.g. GB/s
+ What are the different system granularity?
    * Remote Procedure Call based Implementations
    * MPI-based Implementations
    * Pthread-based Implementations
    * Multicore Task Queue-based Implementations
    * Manycore Throughput Optimized Implementations

## Module 1.3

+ What is the different between concurrency and parallelism?
    * Concurrency: We expose concurrency in our application
    * Parallelism: We exploit parallelism in our platform
+ What are the four key elements of the human problem solving process?
    * Understand the current state
    * Observe the internal representation
    * Search among alternatives
    * Select from a set of choices
+ What are the characteristics of a current algorithm implementation?
    * Efficiency
    * Simplicity
    * Portablility
    * Scalability
+ What levels of concurrency can be exposed in the kmeans algorithm?
    * Expectation: N(independent) k(min reduction) D(sum reduction)
    * Maximization: D(independent) N(Histogram computation into k bins)
+ What levels of parallelism are available to be exploited?
    * Core level Parallelism
    * SIMD level parallelism
+ What mapping between concurrency and parallelism can be explored?
    * One level of concurrency could map to multiple levels of parallelism
    * SIMD & core-level parallelism across data-points
        - Update membership for each data point sequentially
        - Histogram computation

## Module 2.1

+ What are the exploitable levels of parallelism in a multicore processor?
    * SIMD-Level: using vectorizing compiler and hand-code intrinsics
    * SMT-Level: OS abstract it to core-level parallelism
    * Core-Level: Using threads to describe work done on different cores
+ What is SPMD? And how to use OpenMP to do SPMD?
    * OpenMP - Pthread-based Implementations(granularity)
    * SPMD(wiki): SPMD (single program, multiple data) is a technique employed to achieve parallelism; it is a subcategory of MIMD. Tasks are split up and run simultaneously on multiple processors with different input in order to obtain results faster.
    * OpenMP managed **Fork-Join** Parallelism to do SPMD
+ What is the difference between critical and atomic?
    * critical: 并行程序块，同时只能有一个线程能访问该并行程序块
    * atomic: 只适用于两种情况：自加减操作以及基本的操作符
    * critical 与 atomic 的区别在于，atomic 仅适用于两种基本类型操作，而且 atomic 所防护的仅为一句代码。critical 可以对某个并行程序块进行防护。
+ How to reduce synchronization cost and avoid false sharing?
    * Be aware of the cache line sizes for a platform
    * Avoid accessing the same cache line from different threads
+ What are the scheduling, reduction, data sharing, and synchronization options for OpenMP?
    * scheduling
        - static
        - dynamic
        - guided
    * data sharing
        - shared
        - private
        - firstprivate
        - lastprivate
    * synchronization
        - ordered
        - barrier
        - single
        - nowait

## !! Module 2.2

+ Why naive matrix-multiply does not achieve peak performance on the CPU?
    * Deep memory hierarchy
    * Pipeline, ILP
    * Free operations are not free
+ What are the different data layouts for matrices?
    * Column major
    * Row major
+ What is cache blocking? Why do we need it?
+ Is blocking sufficient? What more can we do?
    * Strength reduction
    * Function inlining
    * Loop unrolling
    * Common subexpression elimination
    * Load/Store elimination
    * Table lookups
    * Branch elimination

## Module 2.3

+ What is the roofline model? What are the metrics and axis used?
    * Roofline model: a pedagogical tool for program analysis and optimization
    * Metric of interest: DRAM bandwidth(GB/s)
    * y-axis: FLOPs; x-axis: AI
+ What is the difference between “flop’s per memory instruction” from “flop’s per DRAM byte”?
    * ?
+ Consider an image `Image[height][width]`. If one were to stride through the columns of values, what would be the effects? How would they be mapped to the roofline?
    * ?
+ How does one model incomplete SIMDization (e.g. half the flop’s can be SIMDized). insufficient ILP(some dependent flop’s), or an imbalance between FDMUL’s and FPADD’s on the roofline?
    * See the complete graph below
+ How would one model {branch mispredicts, TLB misses, or too many streams for the prefetchers} on the roofline.
    * See the complete graph below

![roofline](./_resources/qs1.jpg)

## Module 3.1

+ What’s the Difference between Multicore and Manycore?
    * Multicore: yoke of oxen. Each core optimized for executing a single thread.
    * Manycore: flock of chickens. Cores optimized for aggregate throughput, deemphasizing individual performance.
+ When does using a GPU make sense?
    * Application with a lot of concurrency (1000-way, fine-grained concurrency)
    * Some memory intensive applications (Aggregate memory bandwidth is higher)
    * Advantage diminishes when task granularity becomes too large to fit in shared memory
+ What is the memory hierarchy inversion? And why is it there?
    * Memory hierarchy inversion: more registers than shared memory
    * Single thread won't see inverse hierarchy
    * Inversion comes from parallelism
    * Registers scale with SIMD and multithreading (Shared memory/L1 cache don't have to)
+ What is the memory wall? How to get around it?
    * Memory wall: Increasing gap between Processor and DRAM performance
    * Many core Processors utilize application concurrency to hide memory latency (aka get around the memory wall)
+ Why warps?
    * Software abstract info hid an extra level of architecture complexity
    * A 128KB register file is a large memory (takes more than one cycle)
    * Hardware provide 160wide physical SIMD units, half-pump register files
    * To simplify the programming model
+ How do we deal with GPUs of different sizes?
    * CUDA provides an abstract infor concurrency to be fully exposed
    * HW/Runtime provides capability to schedule the computation
+ What are the implications of the thread block abstraction?
    * Computation is grouped into blocks of independent concurrently execrable work
    * Fully exposed the concurrency in the application
    * The HW/Runtime makes the decision to selectively sequentialize the execution as necessary
+ How do threads communicate with each other?
    * Shared Memory
    * Manycore processors provide memory local to each core
    * Computations in SIMD-lanes in the same core can communicate via memory read / write
+ What is the caveat in synchronizing threads in a thread block?
    * `__syncthreads()` 必须在每个线程中都能执行到，而不能有的有有的没有

## Module 3.2

+ What are the three ways to improve execution throughput?
    * Maximizing Memory Throughput
        - SoA vs AoS
        - Memory coalescing
        - Use of shared memory
        - Memory bank conflict
        - Padding
    * Maximizing Instruction Throughput
        - Branch divergence
        - Optimize instruction mix
    * Maximizing Scheduling Throughput
+ When to use SOA vs AOS?
    * Unfortunately, the SoA form is not ideal in all circumstances. For random or incoherent circumstances, gathers are used to access the data and the SoA form can result in extra unneeded data being read into cache, thus reducing performance. In this case, use of the AoS form instead will result in a smaller working set and improved performance. Generally, though, if the computation is to be vectorized, the SoA form is preferred.
+ What is memory coalescing? When to use it? Why is it important?
    * Memory coalescing: combine multiple memory accesses generated from multiple threads into a single physical transaction
    * Hardware Constraint: DRAM is accessed in 'segments' of 32B/64B/128B
+ What is shared memory? How to use it?
    * Manycore processors provide memory local to each core
    * `__share__`
+ What is memory bank conflict? How to work around it?
    * A bank conflict occurs if two or more threads access any bytes within different 32-bit words belonging to the same bank.
    * If each thread in a halfwarp accesses successive 32bit values there are no bank conflicts.
+ What is branch divergence?
    * threads of a warp diverge via a data-dependent conditional branch
+ How to optimize for instruction mix?
    * Compiler Assisted Loop Unrolling
    * #pragma unroll
+ What is occupancy? How to model/measure it?
    * Occupancy: Ability of a CUDA kernel to occupy concurrent contexts in a SM
    * CUDA Occupancy Calculator
    * `--ptxas-options=-v`
+ How to use the code profiler with CUDA?
    * CUDA Profiler Tutorial by Erik Reed

## Module 3.3

+ What are the important properties of a Map function?
    * Side-effect free: Only returning a value, no modifications of state with the rest of the application
    * Independent: Has an independent piece of work, where its input does not depend on another function
+ What are the important properties of a Reduce function?
    * Associativity: a+(b+c) == (a+b)+c
    * Allows elements to be reduced in prarallel in a 'tree'
+ What are the important properties of s Scan function?
    * return a ordered set
+ How to compact an array in a data-parallel way?
    * Map - create flags (1 keep, 0 remove)
    * Scan - compute index
    * Map - copy to new array
+ How to find unique elements in an array in a data-parallel way?
    * Sort
    * Map - create flags (1 keep, 0 remove)
    * Scan - compute index
    * Map - copy to new array

## Module 3.4

+ What are parallel software patterns?
+ What are the three goals the software patterns aim to achieve?
+ What is a software architecture?
+ How is it important for writing fast code?
+ What the the five categories of patterns in OPL?
+ What are the nine sections in an OPL pattern?
+ What are the areas of consideration for your Term Project?

## Module 4.1

+ Why Distributed Computing?
+ How common are failures in Large Scale Distributed Computing?
+ How are failures handled in HADOOP?
+ What is MapReduce?
+ When developing a MapReduce application what components and functions need to be defined?
+ How are data bottlenecks reduced in HDFS?
+ What are the advantages of Cloud Computing?
