# Midterm Preparation

In Class 50 minutes, 100 points

Four Parts:

1. Short questions
2. OpenMP - code interpretation
3. CUDA - code interpretation
4. SIMD - code interpretation

## Short questions

> Describe a general problem in which OpenMP can't be applied, and why.

在循环中如果下一次循环的计算依赖于当次循环的结果，则无法利用 OpenMP。因为在 OpenMP 中多个线程同时执行循环，迭代的顺序是不确定的，只有数据不相关时，才可以使用。

> Race conditions and false sharing are common problems in OpenMP code. 
>   
> 1. Write a small code snippet that demonstrates false sharing
>   
> 2. Write a samll code snippet that demonstrates a race condition


1) 只需要不同的线程轮流访问邻接的数据即可

    int a[10] = {0,1,2,3,4,5,6,7,8,9};
    #pragma omp parallel for
    for (int i = 0; i < 10; ++i){
        a[i]++;
    }

2) 只需要不同的线程访问同一个数据即可

    int a = 0;
    #pragma omp parallel for
    for (int i = 0; i < 10; ++i){
        a++;
    }

> I would like to improve the throughput of a CUDA kernel. What are the three areas I could look at to improve execution throughput? What tools could I use for measuring the performance?

Three areas: memory, instruction and scheduling.

Tools: CUDA Visual Profiler / CUDA Occupancy Calculator

## Code Interpretation Questions

First part

+ a) VECTOR_N x ELEMENT_N = 1024 x 256 = 262,144
    * `scalarProd<<<VECTOR_N, ELEMENT_N>>>(d_C, d_A, d_B, ELEMENT_N)`
+ b) 32
    * fix size of 32
+ c) ELEMENT_N = 256

Second part

__global__ function parameters are passed to the device:

+ via shared memory and are limited to 256 bytes on devices of compute capability 1.x,

+ via constant memory and are limited to 4 KB on devices of compute capability 2.0.

+ a) loads: 2(21 x 2) stores: 1(line 30)
+ b) for each thread block: 256+256+(128+64+32+16+8+4+2+1)x3
    * 1 from line 21, need to times the number of threads
    * 1 from line 30, need to times the number of threads
    * other from `for loop`
+ c) 5 iterations have branch divergance. Branch Divergance only appears in one warp which has two instruction paths. So for the size of 128, 64, 32, every thread in one warp has same path, thus no branch divergance. But for the size of 16, 8, 4, 2, 1, the threads in one warp have two different paths.
+ d) Line 30 stores an identical value to global memory 256 times to the same addres, which causes massive performance losses in the memory system performance. The simple solution is to add a conditional so that only thread 0 will do so. We can eliminate 1024*255 stores to the global memory.
