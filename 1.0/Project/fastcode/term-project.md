# Term Project

## Timeline

Email to 18645@sv.cmu.edu by 22:00(PST)

+ Abstract: March 31th (1 page)
    * what you propose to do for this project
    * Baseline performance, expected outcome
    * submit early!
+ Draft Project Report: April 16th (5-10 pages)
    * Project overview including preliminary results
+ Final Project Report: April 23th (5-10 pages)
    * Final graded report: 5-10 pages

## Report

Apply skills learned in this course to a problem that is important to you

+ Technical report describing your work (5-10 pages)
    * 0.5 page: Overview of the problem you tackled. Why this problem?
    * 0.5 - 1 page: Literature survey, related work. What have others done?
    * 1 - 2 pages: Detailed description of techniques. What did you do?
    * 1.5 - 3 pages: Analysis of results What are the results? What do they mean?
    * 0.5 - 1 page: Conclusion. What is the take home message?
+ Size of report should reflect size of team
+ Report could be basis for a conference submission


## Class

+ location_tool: Read data
+ location: Class
+ pso_algo: algorithm
+ reference_point: tool


## Detailed description of techniques. What did you do?

Besides the method using CUDA, it is also possible to optimize the performance using OpenMP. CUDA can make better usage of the manycore computing power and OpenMP can boost the performance on multicore. Using both techniques can make the computation and test procedure faster in different ways. As we have many test cases, OpenMP can test them concurrently and CUDA can make each test case faster.

In this part we'll focus on the usage of OpenMP.

Though OpenMP may not be as efficient as the CUDA version on each test case, it can still boost the performance with little modification of the code as well as the data structure. This is also the advantage of OpenMP. It may have some strict limitation, but it can still be regarded to be a powerful and easy-to-use technique.

The development of a new algorithm consists of two parts: computing and testing. Not only should we put our concentration on computing, testing is also important. The procedure of our pso algorithm has these two parts, so what we want is to make them both faster.

However, simply adding several openmp statement can not meet our needs as most of the time it can not make full use of the powerful cores of our CPUs.

First we redesign our variables used in the algorithm so that less shared spaces are used as well as the sync issue. This is one of the most common techniques in the practice of OpenMP. For those statement that visits one of the elements of an array, we use a temporary variable to eliminate the false sharing. Also, the reduction operation is very useful.

    double sum = 0, norm_a = 0, norm_b = 0;
    #pragma omp parallel for reduction(+:sum, norm_a, norm_b)
    for (int i = 0; i < (int)a.size(); i++) {
        sum += a[i] * b[i];
        norm_a += a[i] * a[i];
        norm_b += b[i] * b[i];
    }

Loop unrolling is also one of the useful techniques that can reduce the amounts of instructions passed to the CPU. For those loops with limited circulating times, we replace the for statement with the complete statements. These methods increases the length of code but reduces the working load for CPU.

    //origin
    for(....){ statement section A } // 4 times

    //after unrolling
    statement section A;
    statement section A;
    statement section A;
    statement section A;

However, we can't use OpenMP on all for statements as in the pso algorithm, the n+1 step needs the result of the n step, we have to add barriers to make sure that the computations are performed in the correct order.

So what we can do is to change our data structure so as to keep the correct order and reduce unnecessary operations. For pso algorithm, KD-tree is a good choice. However the implementation of KD-tree is difficult to suit the OpenMP. After tesing we have to give up combing KD-tree with OpenMP(But we use is on the CUDA version).

Then we make those variables owned by each thread private because they do not have to communicate with other threads. It is better to make them `private` instead of `shared`.

    #pragma omp parallel for private(x, y, i, temp_p)
    for (i = 0; i < particle_num; i++) {
        x = rand() % rangeX;
        y = rand() % rangeY;
        temp_p = find_nearest_neighbour(database, x, y);
        particles_x[i] = temp_p.first;
        particles_y[i] = temp_p.second;
    }

OpenMP is focusing on multi-platform shared memory multiprocessing programming. Using fork-join model, some STL containers don't work well in multithreading environment. That is to say, they are not thread-safe. So we modify our code in order to use the basic data structure such as array and struct. Actually, the random-access container(vector) works fine with OpenMP. But the set/map container is difficult to use correctly in OpenMP, even with the help of the latest version of OpenMP, only limited operations on these contains are available. We make most of the data structure friendly to OpenMP to accelerate the computation.

## Analysis of results What are the results? What do they mean?

We test our code both on local machine and cmu ghc machine. Unlike CUDA, the number of cores really matters in OpenMP. Let's see the results first.

Method | Time(second) | Error | Speedup
:---: | :---: | :---: | :---:
Origin | 216.7 | 1.71381 | x
Local Machine 1(OpenMP) | 51.365 | 2.22721 | 4.22x
Server(OpenMP)1 | 5.62625 | 2.62159 | 38.56x
Server(OpenMP)2 | 15.12063 | 1.57904 | 14.33x
Server(OpenMP)3 | 15.21625 | 1.16756 | 14.25x

Local Machine | CPU | Memory
:---: | :---: | :---:
1 | 2.4 GHz Intel Core i5 | 2G
2 | x | x

There are 500 test cases in our testing. And for each test case there are 64 particles and 20 times iteration.

We can see from the table that the more powerful the CPU is, the better performance we can get. The multicore processor we are optimizing for has sixteen cores. OpenMP targeted on optimizing toward multicore as the openmp technique make the code run in parallel.

The different optimizing methods have different effects. For running test cases concurrency, the more thread there are, the less time it consumed. For example, it takes about over 200s to finish the testing without OpenMP but only 5s on our server. Our server has 16x cores(16 cores) than mine thus the speedup is almost the same.

One of the interesting fact is that the server got the speedup more than 32x(each core can maintain 2 threads) than the origin sequential version. Where does this 6x speedup come from?

They come from the techniques we used to optimizing the pso algorithm itself, including code reordering, loop unrolling, branch eliminating, SIMD and avoiding capacity/conflict/compulsory misses.

However, as pso algorithm has its own limitation, most more powerful techniques can not be applied on it (the iteration process has to be in order). For each iteration, the amount of computation is not as much as matrix multiplication or kmeans. We try our best to get this 6x speedup using simple data structure and OpenMP.

After testing with different configs, we can see that the increasing number of particles and iterations brings about lots of computation. Doubling the number of particles has the same effect on performance as doubling the number of iterations.

But the good news is, the increases of performance is almost linear in testing. As it is, we can save lots of time using more powerful CPUs without worry about the sync issue. It can promote the efficiency on developing new algorithms.


## Conclusion. What is the take home message?

+ We have to make a choice between time and space, flexibility and speed.
+ Finding the opportunities of concurrency is the most difficult task in writing fast code.
+ The improvement on data structure may be better than any other optimizing methods.
+ However, sometimes the manycore/multicore optimization cannot be used on complex but efficient algorithm, so we have to choose between them according to the situation.
+ Though you can make code run faster without knowing the meaning behind the code, if you really want to push things to the limit, you should know how the code works and optimize the whole procedure.
+ Most of the optimizations contribute little to the performance, some of them even make things worse. We should test them with great caution to get the best result.
