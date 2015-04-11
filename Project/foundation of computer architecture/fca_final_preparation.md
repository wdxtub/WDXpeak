
#FCA Final Preparation

## Topics from Slides

- Multithreading Processors ( Lec 12, Shen Chapter 11)
- Multicore Processors ( Lec 13, Note 21-22)
- **Multicore Cache Coherence** ( Lec 14, IMPORTANT!!)
- Multicore Parallel Programming ( Lec 15, Note 25-26, Parallel Chapter 5 & 7)
- SIMD and GPU ( Lec 16, Note 26-27) Virtual Machine ( Lec 17, Note 27-28)
- **Performance and Power Iron Laws** ( Lec 18, Note 29-30)
- **Power Reduction and Energy Efficiency** ( Lec 19, Note 31, EPI)
- Cluster Computing System, Cloud and MObile Computing, Mobile Computing ( Last 3 Slides 20-22)

## Important Concepts

### Binary Translation

Advantages:

+ Innovation
	+ To allow processor innovation not tied to particular instruction sets
	+ Using BT to provide backwards compatibility
+ Performance
	+ To enable new means to improve processor performance
	+ Using BT to provide backwards compatibility
+ Power
	+ To enable simpler and lower power processors
	+ Using BT to provide backwards compatibility


Conclusion:

+ Binary Translation based processors can work well, no longer a theory
+ Special purpose hardware support is needed, co-designed with software
+ Software translation can be done poorly or well, special care is needed to keep translation overhead low
+ Many opportunities for clever hardware/software co-design tradeoffs
+ This is a technological approach still in its infancy

### Thread-Level Parallelism

+ Instruction-level parallelism
	+ Reaps performance by finding independent work in a single thread
+ Thread-level parallelism
	+ Reaps performance by finding independent work across multiple threads

### Process vs Thread

+ Process: an instance of a program executing in a system
	+ OS supports concurrent execution of multiple processes
	+ Each process has its own address space, set of register, and PC
	+ Two different processes can partially share their address spaces to communicate
+ Thread: an independent control stream within a process
	+ A process can have one or more threads
	+ Private state: PC, registers(int, FP), stack, thread-local storage
	+ Shared state: heap, address space (VM structures)
+ A parallel program is one process but multiple threads

### Multithreaded Processors

+ Motivation: HW underutilized on stalls
	+ Memory accesses (misses)
	+ Data & control hazards
	+ Synchronization & I/O
+ Instead of reducing stalls, switch to running new thread for a while
	+ Latency tolerance (vs avoidance)
	+ Improves throughput & HW utilization
	+ Does not improve single thread latency
+ Need hardware support for fast context-switching

Three Approaches (Benefits & DrawBacks)

1. Coarse-grain multithreading
	+ Switch contexts on long-latency events (e.g. cache misses)
	+ Need a handful of contexts(2-4) for most benefit
	+ **Benefits**
		+ Simple, improved throughput (~30%), low cost
		+ Thread priorities mostly avoid single-thread slowdown
	+ **Drawback**
		+ Nondeterministic, conflicts in shared caches
	+ Hardware context switch takes only a few cycles
		+ Flush the pipeline (not necessary)
		+ Choose the next ready thread as the currently active one
		+ Start fetching instructions from this thread
	+ Four potential states: {Ready / Not-ready} x {using HW context, swapped out}
2. Fine-grain multithreading
	+ Switch contexts at fixed fine-grain interval (e.g. every cycle)
	+ Need enough thread contexts to cover stalls ( Tera MTA - 128 contexts)
	+ **Benefits**
		+ Conceptually simple, high throughput, deterministic behavior
	+ **Drawback**
		+ Very poor single-thread performance
3. Simultaneous multithreading (SMT)
	+ Multiple concurrent active threads (no notion of thread switching)
	+ Need a handful of contexts for most benefit (2-8)
	+ **Benefits**
		+ Natural fit for OOO superscalar, improve throughput, low incremental cost
	+ **Drawbacks**
		+ Additional complexity over OOO superscaler, cache, conflicts

![Multithreaded/Multicore Processors Comparison](_resources/p1.jpg)

### Shared memory multiprocessors

+ A system with multiple CPUs "sharing" the same main memroy is called **multiprocessor**
+ In a multiprocessor system all processes on the various CPUs share a unique logical address space, which is mapped on a physical memory that can be distributed among the processors.
+ Each process can read and write a data item simply using load and store operations, and process communications is through shared memory
+ It is the hardware that makes all CPUs access and use the same main memory
+ On the contrary, in systems with no shared memory, each CPU must have its own copy of the operating system, and processes can only communicate through the message passing

### MESI protocol

One of the most common **write-back** cache coherency protocol, used in modern processors

+ Invalid: the cache entry does not contain valid data
+ Shared: Multiple caches can hold the bolck, RAM is updated
+ Exclusize: No other caches holds the block,  RAM is updated
+ Modified: The block is valid. RAM holds an old copy of the block, no other copies exist

Procedure:

+ At system startup, all cache entries are flagged I: Invalid
+ The first time a block is read into the cache the CPU 1, it is flagged E: Exclusive, because the cache is the exclusive owner of the block.
+ Subsequent reads of the data item from the same CPU will hit in the cache and will not involve the bus
+ If CPU 2 reads the same block, the snooper in CPU 1 detects the read and signals over the bus that CPU 1 holds a copy of the same buffer. Bother entries in the caches are flagged S: Shared.
+ Subsequent reads in the block from CPU 1 or CPU 2 will hit in the appropriate cache, with no access to the BUS.
+ If CPU 2 modifies a block flagged S, it sends over the bus an invalidate signal, so that other CPUs can invalidate their copy. The block is flagged M: Modified, and it is not written to RAM( if the block is flagged E, no signal is sent to other caches, since there are no other copies of block in other caches)
+ What happens if CPU 3 tries to read the same block? The snooper in CPU 2 detects this, and holding the unique valid copy of block, it sends a wait signal to CPU 3, meanwhile updating the stale memory with the valid block.
+ Once memory has been updated, CPU 3 can fetch the required block, and the two copies of the block are flagged S, shared, in both caches
+ If CPU 2 modifies the block again, in its cache, it will send again an invalidate signal over the bus, and all other copies (such as that in CPU 3) will be flagged I: Invalid. Block in CPU 2 is flagged again M: modified.

