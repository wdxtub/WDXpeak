## TODO

optimize: omp/matrix_mul.cpp

+ 只修改 matrix_multiplication 函数
+ at least 5X speedup
+ cache blocking
+ omp parallel
+ omp for
+ omp atomic
+ omp reduction
+ Intrinsics Programming
+ report runtime

make cppunit 的时候会出问题，在./configure 那句里加上LDFLAGS="-ldl"可以解决问题

## 上传

    scp /Users/dawang/Desktop/matrix_mul.cpp dawang@ghc52.ghc.andrew.cmu.edu:645/fastcode/matrix_mul/omp/

## 运行 matrix mul

    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/cppunit/lib
    ./matrix_mul -i ../matrix_mul_02.dat

## 提交

    git commit -a -m “description"
    git push origin master

对于按块相乘而言，当块大小是16的时候，子矩阵一行的大小是：16*4B=64B恰好是我的机器的L1 data cache 的块大小，因为miss一次所取到cache的数据全部立即被用到，因而这时候矩阵相乘cache的使用效率是最高的，miss的次数也是最少的，所以此时运行时间相对于块更大或更小而言是最少的；但是对于块更小而言，一次取来的数据当时不会立即用到，从而之后再用到的时候可能已经被剔除了cache；而当块更大的时候，一次每计算一行都需要造成多次cache的miss，这样，由于cache总大小有限，就会造成计算结果在cache 和内存间的频频移动，所以miss次数也是很大的，而且随着子矩阵的变大，而miss次数也会变大，从而导致了cache 块更大或更小运行时间都会明显增加。

    ******Sequential*****
    Test Case 1 0.0078125 milliseconds
    Test Case 2 0.013916 milliseconds
    Test Case 3 0.400879 milliseconds
    Test Case 4 0.458984 milliseconds
    Test Case 5 3621 milliseconds

    ******OMP*****
    Test Case 1 0.354004 milliseconds
    Test Case 2 0.0251465 milliseconds
    Test Case 3 0.0349121 milliseconds
    Test Case 4 0.0388184 milliseconds
    Test Case 5 60.4109 milliseconds

> 8 10 32 33 100

8为 size 的时候，结果比2 3 4时效果差很多，可能是因为不足 cache line size 的缘故

cache_alignment 64 -> 16 block

## 运行 kmeans

    ./omp_main -i ../data/kmeans01.dat -n 3 -o -a

### cmu 服务器上运行

    ./omp_main -i ../../data/kmeans04.dat -n 3 -o -a

### 上传

    scp /Users/dawang/Desktop/fastcode/kmeans/omp_kmeans.c dawang@ghc52.ghc.andrew.cmu.edu:645/fastcode/kmeans/


## Kmeans 代码相关

    -a perform atomic OpenMP pragma
    -o output timing results
    -d enable debug mode

+ 输入 N 个数据，每个里面有 M 个坐标，根据用户指定的 K 个聚类来操作。结果保存在两个数组中
+ `size[K][N]` 表示 K 个聚类的中心坐标
+ `membership[N]` 存着每个数据对应分配的聚类 id

### 函数与变量

+ euclid_dist_2 计算两个坐标的 euclid 距离
+ find_nearest_cluster 判断一个点离哪个聚类中心最近
+ numCoords 一个坐标有多少维
+ numClusters 有多少个聚类
+ `**clusters` 聚类中心的坐标 `[numClusters][numCoords]`
+ `*object` 每个点的坐标 `[numCoords]`
+ omp_kmeans 返回聚类中心
+ numObjs 数据的个数
+ `**objects` 数据集的各个坐标 `[numObjs][numCoords]`
+ `*membership` 每个数据所属的聚类编号 `[numObjs]`
+ `*newClusterSIze` 新的聚类中每一类的 object 数量 `[numClusters]`
+ delta 改变聚类中心的 object 的数量
+ `**newClusters` 新的聚类中心的坐标 `[numClusters][numCoords]`
+ nthreads 线程数量
+ `**local_newClusterSize` 本地的新聚类中每一类的数量 `[nthreads][numClusters]`
+ `***local_newClusters` 本地的新聚类中各个坐标 `[nthreads][numClusters][numCoords]`
+ if(!is_perform_atomic) 里都是初始化，没有数据操作，主要在 do while 里完成
