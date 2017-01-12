## Basic Info

CUDA machine: ssh dawang@ghc44.ghc.andrew.cmu.edu (32-46)

Setting up the CUDA enviroment:
+ The developer driver provides a set of interfaces for the operating system to talk to the GPU subsystem.
+ The CUDA toolkit provides a compiler, a debugger, a performance profiler, and a set of optimized CUDA libraries.
+ The CUDA SDK provides an infrastructure and examples to help users quickly get start on using the CUDA infrastructure.

Samples -> NVIDIA_CUDA-6.5_Samples

Run CUDA Visual Profiler

    ssh -X dawang@ghc32.ghc.andrew.cmu.edu
    computeprof &

Optimize matrix_mul.cu & cuda_kmeans.cu

## Project 2 grade guideline

### Matrix Multiplication

1. Should success all test cases (7 cases)
2. Should achieving at least 150 Gflops for 1024 case on GTX670 (GHC28)
3. Please add new test case 1024 at the end of matrix_mul_02.dat (your will have 7 cases: 5, 8, 10, 32, 33, 1000, 1024 in different lines)

### K-means clustering

1. Should success all test cases.
2. Sum of all test cases should be achieving at least 1.5X speed up compared to initial cuda code on GTX670 (GHC28)

We’ll announce initial processing time shortly.

We’ll use GHC28 for grading.

Please do not use this machine at least between PDT 00:00am 3:00am and 12:00p.m. (noon) – 3:00 p.m.

We plan to update the motion chart as many as we can (at least once).

## Matmul

现在的代码只实现了2次幂矩阵大小的乘积，我们要做的是

1. 优化到 150GFLOPS
2. 支持各种矩阵大小

运行 matrix mul

    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/cppunit/lib
    ./matrix_mul -i ../matrix_mul_02.dat

提交

    git commit -a -m “description"
    git push origin master

初始代码的问题在于，一个 block 有线程限制，最多只有1024个，那么对于 33*33的矩阵，线程数目就会超过限制，而我们这里只开了一个 grid，所以会有问题。

目前的代码还需要优化，估计可以到200G，去掉判断语句。


上传

    scp /Users/dawang/Desktop/matrix_mul.cu dawang@ghc32.ghc.andrew.cmu.edu:645/fastcode/matrix_mul/cuda/

写一些测试脚本和上传脚本

## Kmeans

目前的程序会在test 3和4中 fail，弄清楚为什么(hint: compute delta kernel function)，要做的是

1. 更新代码跑通所有测试
2. 1.5x speedup


## GHC server GPU status

                GPU1              GPU2
    ghc25   Quadro NVS 295  
    ghc26   Quadro FX 580   GeForce GTX 480
    ghc27   Quadro NVS 295  GeForce GTX 480
    ghc28   Quadro NVS 295  GeForce GTX 670
    ghc29   N/A N/A
    ghc30   Quadro NVS 295  GeForce GTX 650
    ghc31   Quadro NVS 295  GeForce GTX 480
    ghc32   Quadro NVS 295  GeForce GTX 670
    ghc33   Quadro NVS 295  GeForce GTX 670
    ghc34   Quadro NVS 295  GeForce GTX 670
    ghc35   Quadro NVS 295  GeForce GTX 670
    ghc36   Quadro NVS 295  GeForce GTX 670
    ghc37   Quadro NVS 295  GeForce GTX 670
    ghc38   Quadro NVS 295  GeForce GTX 680
    ghc39   Quadro NVS 295  GeForce GTX 670
    ghc40   Quadro NVS 295  GeForce GTX 670
    ghc41   GeForce GTX 780
    ghc42   Quadro NVS 295  GeForce GTX 680
    ghc43   Quadro NVS 295  GeForce GTX 670
    ghc44        N/A             N/A
    ghc45   Quadro NVS 295  GeForce GTX 480
    ghc46   Quadro NVS 295  GeForce GTX 480

    GeForce GTX 670 will be used for grading.
    But, you can use any GPUs (GeForece series) for development.

## Q&A

> Q1. Is CUDA core the smallest unit in GPU?

Is CUDA core the smallest unit in GPU? -> Yes

> Q2. There will be at most one thread running on a CUDA core, right?

There will be at most one thread running on a CUDA core, right? -> Yes, at most one thread at a time. (context switching is available, so we can assign more threads than number of cuda cores)

> Q3. For a streaming multiprocessor, can it have more than one block running on it?

For a streaming multiprocessor, can it have more than one block running on it? -> Multiple thread blocks can be assigned to a streaming multiprocessor. Streaming multiprocessor runs a thread block at a time and switching to other thread blocks (context switching)

> Nvidia Visual Profiler solution (Confirmed)

    Step0: ssh -X
    Step1: cp /usr/local/cuda-6.5/libnvvp/nvvp.ini ~/
    Step2: Add following line in ~/nvvp.ini
        -Dorg.eclipse.swt.internal.gtk.cairoGraphics=false
    Step3: Launch visual profiler using following command
    nvvp --launcher.ini ~/nvvp.ini

I've tested this method, and It works well.

Workaround:  Running visual profiler on your local machine while collecting performance statistic from the remote server (GHC)

    Step 1. Running visual profiler on your local machine (I believe that you can install cuda-toolkit without CUDA-capable GPU)
    Step 2. Create session.
    ------ In "Create New Session Window" ------
    Step 3. Select "Manage" in beside connection slot. (It will open "New Remote Connection" window)
    ----- In "New Remote Connection Window" ----
    Step 3a. Add Host name: ghc##.ghc.andrew.cmu.edu
    Step 3b. Add User name: <YourAndrewID> and click finish.
    ---------------------------------------------------------------

    Step 4a. Setting Executable properties.
    ------ In "Create New Session Window" ------
    Toolkit:  
    Click "Connect" (right bottom) and connect to remote GHC server
    Click "Detect" or browser to /usr/local/cuda-6.5/bin
    Click "Finish"
    Executable:
    Click "Browse" and find your executable (i.e. .../kmeans/cuda_main)
    Working directory:
    Click "Browse" and set your working directory  (i.e. .../kmenas)
    Arguments:
    Set required arguments
    -----------------------------------------------------------
