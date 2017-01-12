# FCA Homework Problem Set

*Da Wang 2014.10.13*

##Chapter 1: Processor Design

**P1.3 Explain the differences between architecture, implementation, and realization. Explain how each of these relates to processor performance as expressed in Equation 1-1.**

Architecture specifies the interface between the hardware and the programmer and affects the number of instructions that need to be executed for a particular program or algorithm. Imple- mentation specifies the microarchitectural organization of the design, and determines the instruc- tion execution rate (measured in instructions per cycle) for that particular design. The realization actually maps the implementation to silicon, and determines the cycle time. The product of the three terms determines performance.

---

**P1.6 A program’s run time is determined by the product of instructions per program, cycles per instruction, and clock frequency. Assume the following instruction mix for a MIPS-like RISC instruction set: 15% stores, 25% loads, 15% branches, and 30% integer arithmetic, 5% integer shift, and 5% integer multiply. Given that stores require one cycle, load instructions require two cycles, branches require four cycles, integer ALU instructions require one cycle, and integer multiplies require ten cycles, compute the overall CPI.**

Type | Mix | Cost | CPI
:--: | :--:| :--: | :--:
store | 15% | 1 | 0.15
load | 25% | 2 | 0.5
branch | 15% | 4 | 0.6
integer | 30% | 1 | 0.3
shift | 5% | 1 | 0.05
multiply | 5% | 10 | 0.5
**Total** | 100% |  | **2.10**

---

**P1.7 Given the parameters of Problem 6, consider a strength-reducing optimization that converts multiplies by a compile-time constant into a sequence of shifts and adds. For this instruction mix, 50% of the multiplies can be converted to shift-add sequences with an average length of three instructions. Assuming a fixed frequency, compute the change in instructions per program, cycles per instruction, and overall program speedup.**

Type | Old Mix | New Mix | Cost | CPI
:--: | :--:| :--: | :--: | :--:
store | 15% | 15% | 1 | 0.15
load | 25% | 25% | 2 | 0.5
branch | 15% | 15% | 4 | 0.6
integer&shift | 35% | 42.5% | 1 | 0.425
multiply | 5% | 2.5% | 10 | 0.25
**Total** | 100% | 105% | | **1.925 / 105% = 1.83**

There are 5% more instructions per program, the CPI is reduced by 12.7% to 1.83, and overall speedup is 2.1/1.925 = 1.091 or 9.1%.

---

**P1.8 Recent processors like the Pentium 4 processors do not implement single-cycle shifts. Given the scenario of Problem 7, assume that s = 50% of the additional integer and shift instructions introduced by strength reduction are shifts, and shifts now take four cycles to execute. Recompute the cycles per instruction and overall program speedup. Is strength reduction still a good optimization?**

Type | Old Mix | New Mix | Cost | CPI
:--: | :--:| :--: | :--: | :--:
store | 15% | 15% | 1 | 0.15
load | 25% | 25% | 2 | 0.5
branch | 15% | 15% | 4 | 0.6
integer | 30% | 33.75% | 1 | 0.3375
shift | 5% | 8.75% | 4 | 0.35
multiply | 5% | 2.5% | 10 | 0.25
**Total** | 100% | 105% | | **2.1875 / 105% = 2.083**

Speedup is now a slowdown: 2.1/2.1875 = 0.96 or 4% slowdown, hence strength reduction is a bad idea.

---

**P1.9 Given the assumptions of Problem 8, solve for the break-even ratio s (percentage of additional instructions that are shifts). That is, find the value of s (if any) for which program performance is identical to the baseline case without strength reduction (Problem 6).**

	2.1 = 0.15+0.50+0.60+0.30+0.05x4+0.25 + (1-s)x0.075x1 + sx0.075x4 
	0.025 = 0.225s => s = 0.111 = 11.1%
	
**P1.11 Using Amdahl’s law,compute speedups for a program that is 85% vectorizable for a system with 4, 8, 16, and 32 processors. What would be a reasonable number of processors to build into a sys- tem for running such an application?**

	Sn,p = 1/[p/n + (1-p)]: p = 0.85; n=4, 8, 16:	S(4,0.85) = 2.76, S(8,0.85) = 3.90, S(16,0.85) = 4.92, S(32,0.85) = 5.52	Of these, the 4 processor system achieves the most parallel efficiency (2.76/4), hence that might be a reasonable number.
### Terms and Buzzwords
**Q: What is (Flynn's Bottleneck) ?**A: Instruction-level parallelism within a basic block is typically upper bounded by 2
**Q: What is (pipelining or deep pipelining) ?**A: It will significantly reduce the machine cycle time, but can increase the branch penalty.
**Q: What is (Amdahl’s Law) ?**A: Describes the speedup achievable when some fraction of the program execution is not parallelizable
**Q: What is (branch prediction) ?**A: A widely-used solution to Flynn’s bottleneck.
**Q: What is (execution time (time per program)) ?**A: The best way to describe a computer system’s performance.
**Q: What is (the instruction set architecture (ISA)) ?**A: This specifies the number of registers, available addressing modes, and instruction opcodes.
**Q: What is (the microarchitecture) ?**A: This determines a processor’s configuration and number of functional units.
**Q: What is (a superscalar processor) ?**A: This is a type of processor that attempts to execute more than one instruction at the same time.
**Q: What is (a superpipelined processor) ?**A: This is a type of processor where results of instructions are not available until two or more cycles after the instruction begins execution.
**Q: What is (VLIW or very long instruction word) ?**A: This is a type of processor that relies heavily on the compiler to statically schedule indepen- dent instructions.

## Chapter 2: Pipelined Processors

**P2.1 Equation 4(P43) -> P=1/(T/k+S), which relates the performance of an ideal pipeline to pipeline depth, looks very simi- lar to Amdahl’s law. Describe the relationship between the terms in these two equations, and develop an intuitive explanation for why the two equations are so similar.**The nonpipelined combinational delay T is comparable to the serial execution time under Amdahl’s law. Pipelining effectively parallelizes this delay over k pipe stages. However, just as there is a serial portion (1-p) under Amdahl’s law that cannot be parallelized, the latch overhead S cannot be parallelized. Hence the speedup equations look very similar.

---
**P2.15 The IBM study of pipelined processor performance assumed an instruction mix based on popular C programs in use in the 1980s. Since then, object-oriented languages like C++ and Java have become much more common. One of the effects of these languages is that object inheritance and polymorphism can be used to replace conditional branches with virtual function calls. Given the IBM instruction mix and CPI shown in the following table, perform the following transformations to reflect the use of C++/Java, and recompute the overall CPI and speedup or slowdown due to this change:**
**1.Replace 50% of taken conditional branches with a load instruction followed by a jump register instruction (the load and jump register implement a virtual function call).**
**2.Replace 25% of not-taken branches with a load instruction followed by a jump register instruction.**
Type | Old Mix | Latency | Old CPI | Cycles | New Mix | Instructions | Cycles | New CPI
:--: | :--:| :--: | :--: | :--: | :--:| :--: | :--: | :--:
Load | 25% | 2 | 0.5 | 500 | 30.5% | 305 | 610 | 0.58
Store | 15% | 1 | 0.15 | 150 | 15% | 150 | 150 | 0.14
Arithmetric | 30% | 300 | 0.3 | 300 | 30% | 300 | 300 | 0.28
Logical | 10% | 1 | 0.1 | 100 | 10% | 100 | 100 | 0.09 
Branch-T | 8% | 3 | 0.24 | 240 | 4% | 40 | 120 | 0.11
Branch-NT | 6% | 2 | 0.12 | 120 | 4.5% | 45 | 90 | 0.09
Jump | 5% | 2 | 0.1 | 100 | 5% | 50 | 100 | 0.09
Jump register | 1% | 3 | 0.03 | 30 | 6.5% | 65 | 195 | 0.18
Total | 100% | | 1.54 | 1540 | 105.5% | 1055 | 1665 | 1.58

	Increase in CPi: 1.58/1.54 = 1.024805	Increase in pathlenth = 1.055	Total slowdown(product of two) 1.08 or 8% slowdown
## Chapter 3: Memory and I/O System
**P3.1 Given the following benchmark code, and assuming a virtually-addressed fully-associative cache with infinite capacity and 64 byte blocks, compute the overall miss rate (number of misses divided by number of references). Assume that all variables except array locations reside in reg- isters, and that arrays A, B, and C are placed consecutively in memory.**
	double A[1024], B[1024], C[1024]; 
	for(int i=0;i<1000;i += 2) {		[i] = 35.0 * B[i] + C[i+1]; 
	}There are 3000 memory references (1000 each to A, B, C)
For each array, these span ceil(1000*8/64) = 128 blocks, hence there are 128 misses to each array, leading to 3x128 = 384 total misses. The total miss rate is 384/3000 = 12.8% misses per reference.

--- 
**P3.2 Given the example code in Problem 1, and assuming a virtually-addressed direct-mapped cache of capacity 8KB and 64 byte blocks, compute the overall miss rate (number of misses divided by number of references). Assume that all variables except array locations reside in registers, and that arrays A, B, and C are placed consecutively in memory.**
The first iteration accesses memory location &B[0], &C[1], and &A[0]. Unfortunately, since the arrays are consecutive in memory, these locations are exactly 8KB (1024 x 8B per double) apart. Hence, in a direct-mapped cache they conflict, and the access to C[1] will evict B[0], while the access to A[0] will evict C[1]. As a result, every reference will miss, leading to a 100% miss rate.

---

**P3.3 Given the example code in Problem 1, and assuming a virtually-addressed two-way set associa- tive cache of capacity 8KB and 64 byte blocks, compute the overall miss rate (number of misses divided by number of references). Assume that all variables except array locations reside in reg- isters, and that arrays A, B, and C are placed consecutively in memory.**

The first iteration accesses memory location &B[0], &C[1], and &A[0]. Unfortunately, since the arrays are consecutive in memory, these locations are exactly 8KB (1024 x 8B per double) apart. Hence, in a two-way set-associative cache they conflict, and the access to A[0] will evict B[0]. In the second iteration, the access to B[1] will evict C[1], and so on. However, since the access to C is offset by 1 double (8 bytes), in the seventh iteration it will access C[8], which does not conflict with B[7]. Hence, B[7] will hit, as will A[7]. In the eighth iteration, C[9] will also hit, but now B[8] and A[8] will again conflict, and no hits will result. Hence, there are three hits every eight iterations, leading to a total number of hits of floor(1000/8)*3 = 375 hits. The num- ber of misses is 3000-375 = 2625, for an overall miss rate of 87.5% misses per reference.

---

**P3.16 Assume a two-level cache hierarchy with a private level one instruction cache(L1I),aprivate level one data cache (L1D), and a shared level two data cache (L2). Given local miss rates for the 4% for L1I, 7.5% for L1D, and 35% for L2, compute the global miss rate for the L2 cache.**

L2 global miss rate = (0.35 L2 misses)/(L2 ref) x ((0.04 L2 ref)/Ifetch + (0.075 L2 ref) / D-ref) = 0.35x0.04 + 0.35x0.075 = 0.04025 = 4.025% L2 misses per global reference

---

**P3.17 Assuming 1 L1I access per instruction and 0.4 data accesses per instruction, compute the misses per instruction for the L1I, L1D, and L2 caches of Problem 16.**

L1 I misses per instruction = .04 miss/ref x 1 ref/instr = .04 miss/instL1 D misses per instruction = .075 miss/ref x 0.4 ref/instr = .03 miss/instr
L2 misses per instruction = .35 miss/ref x (.04 ref/inst + .03 ref/inst) = .35 x .07 = .0245 miss/inst

---
**P3.18 Given the miss rates of Problem 16, and assuming that accesses to the L1I and L1D caches take one cycle, accesses to the L2 take 12 cycles, accesses to main memory take 75 cycles, and a clock rate of 1GHz, compute the average memory reference latency for this cache hierarchy.**
Avg Ifetch mem lat = (1-0.04) x 1 + 0.04 x (1-0.35) x 12 + 0.04 x0.35 x 75 = 0.96 + 0.312 + 1.05 = 2.322 cycles
Avg data ref mem lat = (1-0.075) x 1 + 0.075 x (1-0.35) x 12 + 0.075 x 0.35 x 75 = 0.925 + 0.567 + 1.96875 = 3.46075 cycles
NOTE: to determine overall average memory latency, you must know the ratio of data and instruction references and take the weighted average of the two types of references. As in Prob- lem 17, assume 0.4 data references per instruction reference:Avg mem lat = (2.322 cycles / ifetch x (1 ifetch) / ref + 3.46075 cycles/dref x (0.4 dref/ref)) / 1.4 = 2.647 cycles

---
**P3.19 Assuming a perfect cache CPI(cycles per instruction)for a pipelined processor equal to 1.15 CPI, compute the MCPI and overall CPI for a pipelined processor with the memory hierarchy described in Problem 18 and the miss rates and access rates specified in Problem 16 and Problem 17.**
From solution to 18, miss rates per instruction are .04, .03, and .0245, 
hence: MCPI = .04 x 12 + .03 x 12 + .0245 x (75 - 12) = 2.3835
CPI = 1.15 + MCPI = 1.15 + 2.3835 + 3.5335

---
**P3.25 It is usually the case that a set-associative or fully-associative cache has a higher hit rate than a direct-mapped cache. However, this is not always true. To illustrate this, show a memory refer- ence trace for a program that has a higher hit rate with a 2-block direct-mapped cache than a fully-associative cache with 2 blocks.**
Assume A and B map to the same set but C maps to the other set:
A,B,C,A,B,C,A,B,C,... would always miss in the fully-associative cache, resulting in a 100% miss rate
However, in a direct-mapped cache only A and B would always miss, but C would remain resi- dent, resulting in a 67% miss rate.

---

**Example 1: Suppose we have a 32KB 2-way SA cache with 2 word blocks. Determine the size of the tag, index and offset fields if we're using a 32-bit architecture.**

- number of bits for offset: specify the correct byte within a block, depends on the size of block.
- number of bits for set index: specify the correct cache set, dpends on the number of sets
- number of bits for tag: remaining bits

Here is the calculation:
	
	cache contains 32 KB = 2^15 bytes
	each block contains 2^3 bytes(2 words), so 3 offset bits.
	a set has two blocks = 2^4 bytes
	the number of sets = 2^15 / 2^4 = 2^11, so 11 index bits.
	tag bits(the remaining) = 32 - 11 - 3 = 18 bits(left most)
	Total size = number of rows * size of each row 
		= number of rows * N * size of each block(the N-way SA)
	Total size = 2^11 rows * 2 * (64 bits + 18 bits + 1bits) 
		= 339968 bits = 42496 B > 32 KB
	(64 bits = 2 words, 18 bits -> tag, 1 bit -> valid bit) 

---

**Example 2: The system has the following properties:**

- The processor uses 32-bit physical addresses.
- Load/store instructions are performed in program order and each ties up all caches until it is complete.
- There is 2KB of L1 cache and 16KB of L2 cache.
- Both caches are physically indexed and tagged with a block size of 128 bytes
- Both caches are 4-way set associative and use the LRU replacement policy.
- The write policy in both caches is write-allocate, write-back.
- Dirty bits are used to allow silent replacement of clean blocks, so only dirty blocks are written back on replacement.
- A dirty block replaced from the L1 cache is sent to the L2 cache. If that block is still cached in the L2 cache, the L2 updates its version of the block, but does not update the block’s LRU counter in L2, and does not send the block to memory. If the block is not in L2, it is sent to main memory without putting it in L2.
- When there is an access that misses in both caches, the L2 cache is completely updated (including replacement, if any is needed) before forwarding the block to L1.
- Hits in the L1 cache do not go to the L2 cache and do not update the LRU in the L2 cache.
- Neither inclusion nor exclusion property is maintained.

**(a)For each cache, show how physical address FFF82754 is broken down into the offset, index and tag, showing the number of bits for each. Which set will this load go to in the L1 cache, and which in the L2 cache? How many tags will be checked to determine whether this address is a hit or a miss in the L1 cache?**

In both caches, the block has 128 bytes, so the lowermost 7 bits of the address are the offset.
In the L1 cache, there are 16 lines (2048/128), so there are 4 sets (16/4) => index has 2 bits. The 23 bits that remain (32-7-2) are the tag.
In the L2 cache, there are 128 lines (16K/128), so there are 32 sets (128/4) =>index is 5 bits. The 20 bits that remain are the tag.
Address FFF82754 is 1111 1111 1111 1000 0010 0111 0101 0100 in binary.
In the L1 cache, we have Tag: 11111111111110000010011, Index: 10, and Offset: 1010100, and the load goes to set 2 (offset is 10). Since the cache s 4-way SA, 4 tags are checked on each access.
In the L2 cache, we have Tag: 11111111111110000010, Index: 01110, and Offset: 1010100, and the load goes to set 14 (01110 is 14). This ache is also 4-way SA, so 4 tags are checked.

**(b) Cache size tells us the number of data bytes that the cache can hold. However,the cache also has some overhead state (tags, valid, LRU, and dirty bits). Compute the number of number of overhead bits in the L1 cache in this problem. What is the ratio of the number of overhead bits and the number of data bits in the cache? Keeping all other specified parameters the same (cache size, associativity, etc.), what would this ratio be if the cache block size was changed to 32?**

For each line of data, we keep a valid bit, a 23-bit tag (see part a), a dirty bit, and 2 bits of LRU. In total, we have 27 (1+23+1+2) overhead bits for 1024 its (128 bytes * 8) of data, so the ratio is 27/1024=0.026 (2.6%).
In the data block were 32 bytes in size, there would be only 5 index bits in the address, and there would be 64 lines in the cache, so there would be 16 (64/4) sets, so there would be 4 index bits in the address. The number of tag bits would be 32-5-4=23 (same as with 128-byte blocks). Now we have 27 overhead bits per 256 bits (32 bytes) of data, so the ration is 27/256=0.105 (10.5%).

---
**Example 3: A 2-way set associative write back cache with perfect LRU replacement requires 15 × 29 bits of storage to implement its tag store (including bits for valid, dirty and LRU). The cache is virtually indexed, physically tagged. The virtual address space is 1 MB, page size is 2 KB, cache block size is 8 bytes.** 
**(a) What is the size of the data store of the cache in bytes?**
8 KB. The cache is 2-way set associative. So, each set has 2 tags, each of size t, 2 valid bits, 2 dirty bits and 1 LRU bit (because a single bit is enough to implement perfect LRU for a 2-way set associative cache).
	Let i be the number of index bits.	Tag store size = 2^i × (2 × t + 2 + 2 + 1) = 15 × 29	Therefore,	2t = 10 ⇒ t = 5	i = 9Data store size = 2i ×(2×8) bytes = 29 ×(2×8) bytes = 8 KB.
**(b) How many bits of the virtual index come from the virtual page number?**

1 bit. Page size is 2 KB. Hence, the page offset is 11 bits (bits 10:0).The cache block offset is 3 bits (bits 2:0) and the virtual index is 9 bits (bits 11:3). Therefore, one bit of the virtual index (bit 11) comes from the virtual page number.
**(c) What is the physical address space of this memory system?**
64 KB. The page offset is 11 bits.The physical frame number, which is the same as the physical tag is 5 bits. Therefore, the physical address space is 2^(11+5) = 2^16 bytes = 64 KB.

---
**Example 4: Consider a system with 4-way set associative cache of 256 KB. The cache line size is 8 words (32 bits per word). The smallest addressable unit is a byte, and memory addresses are 64 bits long.**
**(a) Show the division of the bits in a memory address and how they are used to access the cache.**
We are given that the block size is 8 words (32 bytes). Therefore, the number of bytes required to specify the block offset is log232 = 5 bits. The number of sets is 256 KB / (32 * 4) = 2048 sets. Therefore, the index field would require 11 bits. The remaining 64 – 11 – 5 = 48 bits are used for the tag field.

**(b) What percentage of the cache memory is used for tag bits?**

For each cache line (block), we have 1 tag entry. The size of the cache line is 32 * 8 = 256 bits. Therefore, the percentage of cache memory used for tag bits is 48 / (48 + 256) = 15.8%.---**Example 5: For a 1024 KB L2 cache with 64-byte blocks and 8-way set associativity, how many way prediction table entries are needed?**

	The number of blocks in the L2 cache = 1024KB / 64B = 16K 
	The number of sets in the L2 cache = 16K / 8 = 2K	Thus, the number of way prediction table entries needed = 2K---**Example 6: For an 8 MB L2 cache with 128-byte blocks and 2-way set associativity, how many way prediction table entries are needed?**
	The number of blocks in the L2 cache = 8MB / 128B = 64K 
	The number of sets in the L2 cache = 64K / 2 = 32K	Thus, the number of way prediction table entries needed = 32K
---

**Example 7: Consider a system with the following processor components and policies:**

- A direct-mapped L1 data cache of size 4KB and block size of 16 bytes, indexed and tagged using physical addresses, and using a write-allocate, write-back policy
- A fully-associative data TLB with 4 entries and an LRU replacement policy
- Physical addresses of 32 bits, and virtual addresses of 40 bits
- Byte addressable memory
- Page size of 1MB

**Which bits of the virtual address are used to obtain a virtual to physical translation from the TLB? Explain exactly how these bits are used to make the translation, assuming there is a TLB hit.**

The virtual address is 40 bits long. Because the virtual page size is 1MB = 2^20 bytes, and memory is byte addressable, the virtual page offset is 20 bits. Thus, the first 40- 20=20 bits are used for address translation at the TLB. Since the TLB is fully associative, all of these bits are used for the tag; i.e., there are no index bits.
When a virtual address is presented for translation, the hardware first checks to see if the 20 bit tag is present in the TLB by comparing it to all other entries simultaneously. If a valid match is found (i.e., a TLB hit) and no protection violation occurs, the page frame number is read directly from the TLB.
**Which bits of the virtual or physical address are used as the tag, index, and block offset bits for accessing the L1 data cache? Explicitly specify which of these bits can be used directly from the virtual address without any translation.**
Since the cache is physically indexed and physically tagged, all of the bits from accessing the cache must come from the physical address. However, since the lowest 20 bits of the virtual address form the page offset and are therefore not translated, these 20 bits can be used directly from the virtual address. The remaining 12 bits (of the total of 32 bits in the physical address) must be used after translation.
Since the block size is 16 bytes = 2^4 bytes, and memory is byte addressable, the lowest 4 bits are used as block offset.
Since the cache is direct mapped, the number of sets is 4KB/16 bytes = 2^8. Therefore, 8 bits are needed for the index.
The remaining 32-8-4 = 20 bits are needed for the tag.
As mentioned above, the index and offset bits can be used before translation while the tag bits must await the translation for the 12 uppermost bits.
---
**Example 8:Consider a memory hierarchy with the following parameters. Main memory is interleaved on a word basis with four banks and a new bank access can be started every cycle. It takes 8 processor clock cycles to send an address from the cache to main memory; 50 cycles for memory to access a block; and an additional 25 cycles to send a word of data back from memory to the cache. The memory bus width is 1 word. There is a single level of data cache with a miss rate of 2% and a block size of 4 words. Assume 25% of all instructions are data loads and stores. Assume a perfect instruction cache; i.e., there are no instruction cache misses. If all data loads and stores hit in the cache, the CPI for the processor is 1.5.**
**A: Suppose the above memory hierarchy is used with a simple in-order processor and the cache blocks on all loads and stores until they complete. Compute the miss penalty and resulting CPI for such a system.**
	Miss penalty = 8 + 50 + 25*4 = 158 cycles. 
	CPI = 1.5 + (0.25* 0.02 * 158) = 2.29

**B: Suppose we now replace the processor with an out-of-order processor and the cache with a non-blocking cache that can have multiple load and store misses outstanding. Such a configuration can overlap some part of the miss penalty, resulting in a lower effective penalty as seen by the processor. Assume that this configuration effectively reduces the miss penalty (as seen by the processor) by 20%. What is the CPI of this new system and what is the speedup over the system in Part A?**

	Effective miss penalty = 0.80 * 158 = 126 cycles.	CPI = 1.5 + (0.25 * .02 * 126) = 2.13	Speedup over the system in part A is 2.29/2.13 = 1.08.

**C: Start with the system in Part A for this part. Suppose now we double the bus width and the width of each memory bank. That is, it now takes 50 cycles for memory to access the block as before, and the additional 20 cycles now send a double word of data back from memory to the cache. What is the miss penalty now? What is the CPI? Is this system faster or slower than that in Part B?**

	Miss penalty = 8 + 50 + 25*2 = 108 cycles. 
	CPI = 1.5 + (0.25 * .02 * 108) = 2.04.This system is slightly faster than that in part B.
**Example 9: Why don't we include the tags bits when measuring a cache's size?**

The tag bits(and the value bit) do not hold any cache data so they are not counted in the size of the cache.
## Chapter 4: Superscalar Organization
**P4.7 What is the most important advantage of a centralized reservation station over distributed reser- vation stations?**
Better utilization (which is always true for a shared resource).

---

**Example 1: In one or two sentences, explain the tradeoffs between adding an additional pipeline stage vs. adding a write port to the register file. What conditions might favor one or the other design?**

Increasing the ports in the register file increases its size quadratically. If the register file is the critical path in the pipeline, this will slow down the processor, and no matter what it increases area and power overheads. On the other hand, if applications commonly stall on the structural hazard due to many LDWAs, it may be worth it to add a write port to the register file. An additional stage can also complicate bypassing and stalling logic, although this is likely to be less expensive than expanding the register file. (The latency of the additional pipeline stage, ignoring stalls, is not a major concern.)
### Terms and Buzzwords
**Q: What is (the reorder buffer)?**
A: A mechanism that tracks out-of-order execution and maintains speculative machine state.
**Q: What is (pipelining or deep pipelining)?**
A: It will significantly reduce the machine cycle time, but can increase the branch penalty.
**Q: What is (a taken branch)?**
A: A mechanism that tracks out-of-order execution and maintains speculative machine state.
**Q: What is (dispatch)?**
A: The logical pipeline stage that assigns an instruction to the appropriate execution unit.
## Chpater 5: Superscalar Techniques
**P5.24 In one or two sentences compare and contrast Load Forwarding with Load Bypassing**
Load bypassing allows independent loads to bypass earlier stores before those stores are committed, but stalls dependent loads until the aliased store commits. Load forwarding will forward val- ues from the earlier uncommitted store by reading the value from the store queue and satisfying the load with that value.

---

**Example 1: Suppose we have a deeply pipelined processor for which we implement a branch-target buffer (BTB) for conditional branches. Assume that the misprediction penalty is always 4 cycles and the buffer miss penalty is always 3 cycles. Assume 85% prediction accuracy and 20% frequency of conditional branches. What should the hit rate in the branch target buffer be for this processor to be faster than a processor that has a fixed 2-cycle branch penalty? (assume that the two processors are equivalent in every other respect.) Assume a base CPI of 1 when there are no conditional branch stalls.**

CPI of processor with a fixed 2-cycle branch penalty:
	1 + (# of branches * branch penalty) = 1 + (.2 * 2) = 1.4
The CPI of the processor with the BTB has to be lower than 1.4 The branch penalty of this processor is
	Branch penalty = mispredict penalty + buffer miss penalty	= fraction of hits in the BTB * fraction mispredicted * mispredict penalty + fraction of misses in the BTB * buffer miss penalty
	= H * 0.15 * 4 + (1 – H) * 3 = 3 – 2.4H
	where H is the hit rate in the BTB
	Overall CPI = 1 + fraction of branches * branch penalty 
	= 1 + 0.2 * (3 – 2.4H) 

The Overall CPI above must be less than 1.4
	1 + 0.2 * (3 – 2.4H) < 1.4	H > 0.4167The hit rate must be greater 41.67%

---
**Example 2: Consider the following high level language code segment:**	int array[1000] = { /* random values */ };
	int sum1 = 0, sum2 = 0, sum3 = 0, sum4 = 0;
	for (i = 0; i < 1000; i++) // Branch 1: Loop Branch
	{
		if (i % 4 == 0) // Branch 2: If Condition 1
			sum1 += array[i]; // Taken Path
		else
			sum2 += array[i]; // Not-Taken Path
		
		if (i % 2 == 0) // Branch 3: If Condition 2
			sum3 += array[i]; // Taken Path
		else
			sum4 += array[i]; // Not-Taken Path
	}

**(a) What is the prediction accuracy for each of the three branches using a per-branch last-time predictor(assume that every per-branch counter starts at "not-taken")? Please show all of your work.**

BRANCH 1: 998=1000 = 99:8%: The branch is mispredicted the rst time it's executed.

BRANCH 2: 500=1000  100 = 50%:

BRANCH 3: 0%. The branch changes direction every time it is executed.

**(b) What is the prediction accuracy for each of the three branches when a per-branch 2-bit saturating counter-based predictor is used (assume that every per-branch counter starts at "strongly not-taken")? Please show all of your work.**

BRANCH 1: 997 / 1000 * 100 = 99:7%: The branch is mispredicted the first two times it's executed and the last time(when the loop exits)

BRANCH 2: 750 / 1000 * 100 = 75%. The branch repeats the pattern TNNNTNNN... The saturating counter moves between "strongly not-taken" and "weakly not-taken" (once out of every four predictions, after the branch is actually taken), and the prediction is always not-taken.

BRANCH 3: 500 / 1000 * 100 = 75%. The branch repeats the pattern TNTN... The saturating counter moves between "strongly not-taken" and "weakly not-taken" every prediction, and every prediction is not-taken, which is correct half the time.
**(c) What is the prediction accuracy for both Branch 2 and Branch 3, when the counter starts at (i) "weakly not-taken" and (ii) "weakly taken"?**

(i) "weakly not-taken"

BRANCH 2: 749 / 1000 * 100 = 74.9%

BRANCH 3: 0%. The predictor oscillates between "weakly not-taken" and "weakly taken".

(ii) "weakly taken"

BRANCH 2: 749 / 1000 * 100 = 74.9%. The branch's pattern is TNNNTNNN... The first four iteration, the predictor's counter starts at weakly taken, moves to strongly taken, then weakly taken, then weakly not-taken. It thus predicts TTTN. Starting for the next group of four branches, the counter is strongly not-taken, weakly not-taken, strongly not-taken, strongly not-taken, yielding NNNN predictions. Thus 249*3+2 = 749 correct predictions are made.

BRANCH 3: 500 / 1000 * 100 = 50%. The branch pattern is TNTN... The counter is at weakly-taken for the first branch, moves to strongly-taken, then weakly taken, etc. Thus the predictions are TTTT.. so the predictor is 50% accurate.

**(d) What is the prediction accuracy for each of the three branches when a two-level global branch predictor with a two-bit global history register and a separate pattern history table per branch, consisting of 2-bit saturating counters for every entry, is used? Assume that both bits of the global history register are initialized to "not-taken" and the 2-bit saturating counters in the pattern history tables are initialized to "strongly not-taken". When calculating prediction accuracy, ignore the rst 500 loop iterations.**

BRANCH 1: 499/500 × 100 = 99.8% The predictor has already entered a “strongly taken” state for all global histories for this branch after 500 loop iterations. It always predicts taken. Only the last loop iteration (for which the loop branch is not taken) results in a misprediction.BRANCH 2: 75%. Correlation between BRANCH 3 (of the previous loop iteration) and BRANCH 2 helps out here. The global branch history will include BRANCH 3’s last result, as well as the loop branch, which will always be taken. There is thus effectively a separate saturating counter for even loop iterations and odd loop iterations. When the last BRANCH 3 branch was not taken, BRANCH 2’s pattern is N T N T ... There are never two consecutive T’s in this subsequence so the saturating counter oscillates between strongly not-taken and weakly-not taken, resulting in all not-taken predictions and 50% accuracy. When the last BRANCH 3 branch was taken, BRANCH 2’s pattern is N N N N ... which will result in 100% accuracy. Hence the overall accuracy is 75%.BRANCH 3: 75%. Similar to the above, BRANCH 2’s branch history correlates with BRANCH 3’s, and BRANCH 3 effectively uses two saturating counters, conditional on IF BRANCH 2’s outcome. When BRANCH 2 is not taken, BRANCH 3’s pattern is N T N N T N N T N ... (these branches result from iterations 1, 2, 3, 5, 6, 7, 9, 10, 11, ...). The predictor will oscillate between weakly and strongly not-taken, but will always predict N. When BRANCH 2 is taken, BRANCH 3 is also always taken, so the predictor will have 100% accuracy in this case. Altogether, only 1 out of every 4 iterations is mispredicted, so overall accuracy is 75%.
## Chpater 9: Advanced Instruction Flow Techniques
**P9.1 Profiling a program has indicated that a particular branch is taken 53% of the time. How effective are the following at predicting this branch and why? (a)Always-taken static prediction. (b)Bimodal/Smith predictor. (c)Local-history predictor. (d)Eager execution. State your assumptions.**
(a) For this branch, an always taken static prediction will always result in a 47% misprediction rate. This is not much better than random guessing.
(b) A bimodal predictor will provide very accurate predictions, assuming that the 53% taken branches are clustered separately from the 47% not-taken branches. For example, if the first 53% of all branches are taken, then the bimodal counters will quickly saturate and provide the correct prediction for this portion of the program. When the dominant direction of the branch switches, then the counter will mispredict a few times and then learn to predict not-taken. Overall, if the branch exhibits the same outcome many times in a row, the bimodal predictor will perform well. The less often the branch direction changes, the fewer mispredictions the bimodal predictor will make.
(c) The branch outcomes must repeat in a relatively short pattern for the local history predictor to learn and predict well. If the pattern is too complicated or too long to be captured by the local history register, then the local history predictor will not be able to learn the entire pattern, which will result in mispredictions. On the other hand, if the pattern is short enough, than a local history predictor can achieve a 100% prediction rate after the initial period that it takes to learn the pattern. The branch pattern may change part way through the program, and there will be a period where the local history predictor will make many more mispredictions as it tries to learn the new pattern. This is analogous to the bimodal predictor making mispredictions when the dominant branch direction changes. If the patterns do not change very often, then the local history predictor will make fewer mispredictions. If the 53% taken branches do not repeat in any discernable pattern, than the local history predictor will not be effective.(d) Eager execution is not effective at predicting branches because it is not a branch predictor! Rather, it is a means for dealing with hard to predict branches. For branches that are seemingly “random”, eager execution may provide a performance benefit since no matter which path is the correct one, some work on the correct path will always be done by the time the processor has resolved the actual branch direction. The flip-side of this is that the processor is also guaranteed to execute instructions on the wrong-path thus wasting power and execution resources. If the branch is very predictable, eager execution may actually slow down execution because the correct path instructions must now compete with the wrong path instructions for processor resources (e.g. functional units, register read ports, etc.).
---**P9.2 Assume that a branch has the following sequence of taken(T) and not-taken(N) outcomes: TTTNNTTTNNTTTNN. What is the prediction accuracy for a 2-bit counter(Smith predictor) for this sequence assuming an initial state of strongly taken?**
Counter State | Prediction | Actual Outcome | Correct? | Next State
:--: | :--:| :--: | :--: | :--:
ST | T | T | 1 | ST
ST | T | T | 1 | ST
ST | T | T | 1 | ST
ST | T | N | 0 | WT
WT | T | N | 0 | WN
WN | N | T | 0 | WT
WT | T | T | 1 | ST
ST | T | T | 1 | ST
ST | T | N | 0 | WT
WT | T | N | 0 | WN
WN | N | T | 0 | WT
WT | T | T | 1 | ST
ST | T | T | 1 | ST
ST | T | N | 0 | WT
WT | T | N | 0 | WN

This table shows the progression of the counter state, the counter’s predictions, the actual outcomes, whether the prediction was correct, and the transition to the next state. The column labeled “Actual Outcome” lists the original branch outcome sequence. For this sequence, there were 7 correct predictions out of 15 predictions overall for a 46.67% prediction rate (53.33% misprediction rate).

---

**P9.3 What is the minimum local history lenght needed to achieve perfect branch prediction for the branch outcome sequence used in Problem 9.2? Draw the corresponding PHT and fill in each entry wiht one or T(predict taken), N(predict not-taken), or X(doesn't matter).**

Even though the branch outcome pattern from Problem 2 repeats every five branches, a branch history register of only the last three outcomes is needed. This PHT is illustrated below:

PHT Index | Corresponding Prediction
:--: | :--:
000(NNN) | X
001(NNT) | T
010(NTN) | X
011(NTT) | T
100(TNN) | T
101(TNT) | X
110(TTN) | N
111(TTT) | N

For example, whenever the previous three branch outcomes were NTT, the following outcome is always T. Therefore the PHT stores a T in the entry for 011 (NTT). While this table only uses T’s and N’s, a real predictor would use two-bit saturating counters and so each T-prediction in the example PHT above would really have a counter in either the WT or ST state.

If a history register of length 5 was used, then the PHT would have 32 entries, where only five of the entries were in use.

---

**P9.4 Suppose that most of the branches in a program only need a 6-bit global history predictor to be accurately predicted. What are the advantages and disadvantages to using a longer history length?**

Using a larger history register than necessary may increase the training time of the predictor. If a particular branch has an outcome that is always the opposite of the sixth previous branch, then the PHT must learn the patterns 1xxxxx0 and 0xxxxx1 (where x is either 0 or 1). Since there are six bits to the pattern, it may take 26 = 64 PHT entries to store the entire mapping. It takes time just to observe all of the patterns, and then it may require observing each pattern more than once to learn the corresponding prediction. Adding additional unnecessary history bits increases the number of patterns, and thus the training time. This in turn may lead to more mispredictions.
For a traditional Two-Level global history predictor, increasing the history length means decreasing the number of branch address bits used in the PHT index. This may lead to an increase in aliasing between unrelated branches. For a gshare predictor, these effects are not as pronounced and the disadvantages of a longer history register are mostly limited to what has already been discussed.
The problem states that most of the branches only require six bits of history, which implies that there are some that require more. Whether or not it is a good idea to increase the history register length to help these other branches depends on how much the additional training time hurts the prediction rates of the other branches that do not require as much history, and it depends on how much performance is being lost to the branches that do require longer histories.
What makes choosing an appropriate history length difficult is that different programs exhibit different behaviors. A history length of four may be sufficient for one application, but another may require twelve. Choosing a history length of twelve may cause the first program to suffer from increased predictor training times. Choosing a history length of four may result in a high misprediction rate for the second program due to insufficient prediction context.---**P9.5 Conflict aliasing occurs in conventional caches when two addresses map to the same line of the cache. Adding tags and associativity is on of the common ways to reduce the miss rate of caches in the presence of conflict aliasing. What are the advantages and disadvantages of adding set associativity to a branch prediction data structure (e.g., PHT)?**
The main tradeoff is one between capacity and conflict aliasing. Adding bits for tags (the tags may be partial tags, similar to partial resolution for BTBs) decreases conflict aliasing, but this comes at the cost of additional bits. These bits could have alternatively been used to increase the number of entries in the branch prediction table (e.g. larger PHT), which in turn decreases interference due to insufficient capacity. For example, instead of adding a 6-bit tag to a 2-bit counter, one could instead implement an untagged table that is four times larger than the original (i.e. each 6-bit tag could instead be used to implement three separate 2-bit counters). For larger hardware budgets, further adding capacity has diminishing returns, and so adding associativity is likely to be more beneficial. At smaller hardware budgets, the amount of capacity aliasing is likely to be the predominant cause for interference, and so using the bits to increase the table size instead is likely to be the better choice.---
**P9.8 Most proposed hybrid predictors involve the combination of a global-history predictor with a local-history predictor. Explain the benefits, if any, of combining two global-history predictors(possibly of different types like Bi-Mode and gskewed, for example) in a hybrid configuration. If there is no advantage to a global-global hybrid, explain why.**
Intuitively, combining a global-history and local-history predictor may seem to make more sense because some branches may need one type of history to predict, while others may need the other type. Combining two predictors that use the same type of history may seem to be completely useless since it does not appear that the second predictor makes use of any new information. On the other hand, two global history predictors (even if they have the exact same history length) that use different prediction algorithms (e.g. Bi-Mode vs. gskewed) will result in different interference patterns in their respective PHTs. There may be cases where branch aliasing in a gskewed predictor causes a misprediction, but since the hashing function for a Bi-Mode predictor is different, there may not be any interference, and this results in a correct prediction. Using two global- history predictors in this situation may result in a decrease in interference-based mispredictions.