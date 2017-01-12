# OpenMP 入门指南

For CMU 18-645 How to write fast code 2015 Spring

Learn openmp in an hour!  [主要来源](http://blog.csdn.net/donhao)

## 简介

这门课作为 ECE 中少有的跟计算机科学相关的课，自然是必上不可。不过无论是 OpenMP 还是 CUDA，对于平时极少接触并行编程的我来说，都是十分吃力的，第一次作业的 OpenMP 编程已经让意识到了个中的差别，当然，在单个核心的计算速度基本达到极致的现在，掌握并行编程可以算是程序员的基本素养，而 OpenMP 其实是一个非常好的开始，简单，易懂，见效飞快。所以我们的旅程，就从这里开始吧。

## Hello OpenMP

OpenMP是一种面向共享内存以及分布式共享内存的多处理器多线程并行编程语言。一段简单的代码如下：

	#include <omp.h>
	#include <iostream>
	using namespace std;

	int main(){
	    #pragma omp parallel for 
	    for (int i = 0; i < 10; ++i)
	    {
	        cout << i;
	    }
	    cout << endl;
	    return 0;
	}

通过#pragma omp预处理指示符指定要采用OpenMP

通过#pragma omp parallel for来指定下方的for循环采用多线程执行，此时编译器会根据CPU的个数来创建线程数，对于双核系统，编译器会默认创建两个线程执行并行区域的代码。

这段程序的输入如下（省略前面的终端信息）
	
	dawang$ ./a.out
	3680479152
	dawang$ ./a.out
	8603971425
	dawang$ ./a.out
	3086419752
	dawang$ ./a.out
	6038714925
	
### 常用的库函数

函数原型 / 功能

	返回当前可用的处理器个数
	int omp_get_num_procs(void) 
	
	返回当前并行区域中的活动线程个数，如果在并行区域外部调用，返回1
	int omp_get_num_threads(void)
	
	返回当前的线程号（个人感觉这里为omp_get_thread_ID好一些）
	int omp_get_thread_num(void) 
	
	设置进入并行区域时，将要创建的线程个数
	int omp_set_num_threads(void)
	
下面的这个例子演示了四个库函数

	#include <iostream>
	#include <omp.h>
	using namespace std;

	int main(){
	    cout << "CPU number: " << omp_get_num_procs() << endl;

	    cout << "Parallel area 1: " << endl;
	
	    #pragma omp parallel //下面大括号内部为并行区域
	    {
	        cout << "Num of threads is: " << omp_get_num_threads();
	        cout << "; This thread ID is " << omp_get_thread_num() << endl;
	    }
	
	    cout << "Parallel area 2:" << endl;
	    omp_set_num_threads(4); // 设置为并行区域创建4个线程
	    #pragma omp parallel //下面大括号内部为并行区域
	    {
	        cout << "Num of threads is: " << omp_get_num_threads();
	        cout << "; This thread ID is " << omp_get_thread_num() << endl;
	    }
	
	    return 0;
	}
	
大家可以自己运行一次看看自己的输出

## 数据相关性

在循环并行化时，由于多个线程同时执行循环，迭代的顺序是不确定的。如果是数据不相关的，则可以采用基本的#pragma omp parallel for预处理器指示符。

如果语句S2与语句S1相关，那么必然存在以下两种情况之一：

1. 语句S1在一次迭代中访问存储单元L，而S2在随后的一次迭代中访问统一存储单元，称之为循环迭代相关（Loop-Carried Dependence）；
2. S1和S2在同一循环迭代中访问统一存储单元L，但S1的执行在S2之前，称之为非循环迭代相关（Loop-Independent Dependence）。

### for 循环并行化的声明形式

	#include <iostream>
	#include <omp.h>
	using namespace std;
	
	int main(){
	    // for 循环并行化声明形式1
	    #pragma omp parallel
	    {
	        #pragma omp for
	        for (int i = 0; i < 10; ++i){
	            cout << i << endl;
	        }
	    }

	    // for 循环并行化声明形式2
	    #pragma omp parallel for
	    for (int j = 0; j < 10; ++j){
	        cout << j << endl;
	    }
	    return 0;
	}
	
上边代码的两种声明形式是一样的，很显然第二种声明形式更为简洁紧凑。但是第一种声明形式有一个好处，即可以在并行区域内、for循环以外写其他并行代码。

### for 循环并行化的约束条件

尽管OpenMP可以方便地对for循环进行并行化，但并不是所有的for循环都可以进行并行化。以下几种情况不能进行并行化：

1. for循环中的循环变量必须是有符号整形。例如，for (unsigned int i = 0; i < 10; ++i){}会编译不通过；
2. for循环中比较操作符必须是<, <=, >, >=。例如for (int i = 0; i != 10; ++i){}会编译不通过；
3. for循环中的第三个表达式，必须是整数的加减，并且加减的值必须是一个循环不变量。例如for (int i = 0; i != 10; i = i + 1){}会编译不通过；感觉只能++i; i++; --i; 或i--；
4. 如果for循环中的比较操作为<或<=，那么循环变量只能增加；反之亦然。例如for (int i = 0; i != 10; --i)会编译不通过；
5. 循环必须是单入口、单出口，也就是说循环内部不允许能够达到循环以外的跳转语句，exit除外。异常的处理也必须在循环体内处理。例如：若循环体内的break或goto会跳转到循环体外，那么会编译不通过。

### 基本 for 循环并行化举例

	#include <iostream>
	#include <omp.h>

	int main(){
	    int a[10] = {1};
	    int b[10] = {2};
	    int c[10] = {0};
	
	    #pragma omp parallel
	    {
	        #pragma omp for
	        for (int i = 0; i < 10; ++i){
	            // c[i] 只跟 a[i] 和 b[i] 有关
	            c[i] = a[i] + b[i];
	        }
	    }
	
	    return 0;
	}
	
### 嵌套 for 循环并行化举例

	#include <omp.h>
	
	int main(){
	    int a[10][5] = {1};
	    int b[10][5] = {2};
	    int c[10][5] = {3};
	
	    #pragma omp parallel
	    {
	        #pragma omp for
	        for (int i = 0; i < 10; ++i){
	            for (int j = 0; j < 5; ++j){
	                // c[i][j] 只跟 a[i][j] 和 b[i][j] 有关
	                c[i][j] = a[i][j] + b[i][j];
	            }
	        }
	    }
	
	    return 0;
	}
	
对于双核 CPU 来说，编译器会让第一个cpu完成：

	for (int i = 0; i < 5; ++i){
        for (int j = 0; j < 5; ++j){
            // c[i][j] 只跟 a[i][j] 和 b[i][j] 有关
            c[i][j] = a[i][j] + b[i][j];
        }
    }

会让第二个 cpu 完成：

	for (int i = 5; i < 10; ++i){
        for (int j = 0; j < 5; ++j){
            // c[i][j] 只跟 a[i][j] 和 b[i][j] 有关
            c[i][j] = a[i][j] + b[i][j];
        }
    }
    
## 数据的共享与私有化

在并行区域中，若多个线程共同访问同一存储单元，并且至少会有一个线程更新数据单元中的内容时，会发送数据竞争。本节的数据共享与私有化对数据竞争做一个初步的探讨，后续会在同步、互斥相关章节中进行进一步描述。

除了以下三种情况外，并行区域中的所有变量都是共享的：

1. 并行区域中定义的变量
2. 多个线程用来完成循环的循环变量
3. private、firstprivate、lastprivate或reduction字句修饰的变量

例如：

	#include <iostream>
	#include <omp.h>
	using namespace std;
	
	int main(){
	    int share_a = 0; // 共享变量
	    int share_to_private_b = 1; // 通过 private 子句修饰该变量之后在并行区域内变为私有变量
	
	    #pragma omp parallel
	    {
	        int private_c = 2;
	        
	        #pragma omp for private(share_to_private_b)
	        for (int i = 0; i < 10; ++i) //该循环变量是私有的，若为两个线程，则一个线程执行0~4，另一个执行5~9
	            cout << i << endl;
	
	    }
	
	    return 0;
	}
	
声明方法 / 功能

	并行区域中变量val是私有的，即每个线程拥有该变量的一个拷贝
	private(val1, val2, ...)
	
	与private不同的是，每个线程在开始的时候都会对该变量进行一次初始化。
	first_private(val1, val2, ...)      

	与private不同的是，并发执行的最后一次循环的私有变量将会拷贝到val
	last_private(val1, val2, ...)      

	声明val是共享的
	shared(val1, val2, ...)              

如果使用private，无论该变量在并行区域外是否初始化，在进入并行区域后，该变量均不会初始化。

## Reduction 的用法

直接上例子

	#include <iostream>
	#include <stdio.h>
	#include <omp.h>
	using namespace std;
	
	int main(){
	    int sum = 0;
	    cout << "Before: " << sum << endl;
	
	    #pragma omp parallel for reduction(+:sum)
	    for (int i = 0; i < 10; ++i){
	        sum = sum + i;
	        printf("%d\n", sum);
	    }
	
	    cout << "After: " << sum << endl;
	    
	    return 0;
	}
	
其中sum是共享的，采用reduction之后，每个线程根据reduction（+: sum）的声明算出自己的sum，然后再将每个线程的sum加起来。

reduction声明可以看作：

1. 保证了对sum的原则操作
2. 多个线程的执行结果通过reduction中声明的操作符进行计算，以加法操作符为例：

假设sum的初始值为10，reduction（+: sum）声明的并行区域中每个线程的sum初始值为0（规定），并行处理结束之后，会将sum的初始化值10以及每个线程所计算的sum值相加。

我们在上边已经了解了reduction的声明形式，其具体如下：

reduction (operator: var1, val2, ...)

其中operator以及约定变量的初始值如下：

	运算符            数据类型            默认初始值
	  +              整数、浮点             0	
	  -              整数、浮点             0	
	  *              整数、浮点             1	
	  &                整数             所有位均为1	
	  |                整数                0
	  ^                整数                0	
	  &&               整数                1	
	  ||               整数                0
	  
## 线程同步之 atomic

在OpenMP中，线程同步机制包括互斥锁同步机制和事件同步机制。互斥锁同步的概念类似于Windows中的临界区（CriticalSection）以及Windows和Linux中的Mutex，以及VxWorks中的SemTake何SemGive（初始化时信号量为满），即对某一块代码操作进行保护，以保证同时只能有一个线程执行该段代码。

### atomic（原子）操作语法

	#pragma omp atomic
	x< + or * or - or * or / or & or | or << or >> >=expr
	(例如x <<= 1; or x *=2;)
	
或

	#pragma omp atomic
	x++ //or x--, --x, ++x
	
可以看到atomic的操作仅适用于两种情况：

1. 自加减操作
2. x<上述列出的操作符>=expr

例如

	#include <iostream>
	#include <omp.h>
	using namespace std;
	
	int main(){
	    int sum = 0;
	    cout << "Before: " << sum << endl;
	
	    #pragma omp parallel for
	    for (int i = 0; i < 20000; ++i){
	        #pragma omp atomic
	        sum++;
	    }
	    cout << "Atomic-After: " << sum << endl;
	
	    sum = 0;
	    #pragma omp parallel for
	    for (int i = 0; i < 20000; ++i){
	        sum++;
	    }
	    cout << "None-atomic-After: " << sum << endl;
	    return 0;
	}
	
输出20000。如果将#pragma omp atomic声明去掉，则输出值不确定。

## 线程同步之 critical

这里的临界区与Windows下的CriticalSection类似。
临界区声明方法

	#pragma omp critical [(name)] //[]表示名字可选
	{
	//并行程序块，同时只能有一个线程能访问该并行程序块
	}
	
例如

	#include <iostream>
	#include <omp.h>
	using namespace std;
	
	int main(){
	    int sum = 0;
	    cout << "Before: " << sum << endl;
	
	    #pragma omp parallel for
	    for (int i = 0; i < 100; ++i){
	        #pragma omp critical(a)
	        {
	            sum = sum + i;
	            sum = sum + i * 2;
	        }
	    }
	
	    cout << "After: " << sum << endl;
	
	    return 0;
	}
	
critical 与 atomic 的区别在于，atomic 仅适用于上一节规定的两种类型操作，而且 atomic 所防护的仅为一句代码。critical 可以对某个并行程序块进行防护。

For a simple increment to a shared variable, atomic and critical are semantically equivalent, but atomic allows the compiler more opportunities for optimisation (using hardware instructions, for example). 

In other cases, there are differences. If incrementing array elements (e.g. a[i]++ ), atomic allows different threads to update different elements of the array concurrently whereas critical does not. If there is a more complicated expression on the RHS (e.g. a+=foo() ) then the evaluation of foo() is protected from concurrent execution with critical but not with atomic. 

Using a critical section is a legitimate way of implementing atomics inside the compiler/runtime, but most current OpenMP compilers do a better job than this. 

## 线程同步之事件同步机制

互斥锁同步包括atomic、critical、mutex函数，其机制与普通多线程同步的机制类似。而事件同步则通过nowait、sections、single、master等预处理器指示符声明来完成。

### 隐式栅障

barrier为隐式栅障，即并行区域中所有线程执行完毕之后，主线程才继续执行。

### nowait 用来取消栅障

其用法如下：

	#pragma omp for nowait //不能用#pragma omp parallel for nowait
	或
	#pragma omp single nowait
	
例如

	#include <stdio.h>
	#include <omp.h>
	
	int main(){
	    #pragma omp parallel
	    {
	        #pragma omp for nowait
	        for (int i = 0; i < 1000; ++i){
	            printf("%d+\n", i);
	        }
	
	        #pragma omp for
	        for (int j = 0; j < 10; ++j){
	            printf("%d-\n", j);
	        }
	    }
	    return 0;
	}

第一个 for 循环的两个线程中的一个执行完之后，继续往下执行，因此同时打印出了第一个循环的 + 和第一个循环的 - 。

可以看到，第二个 for 循环的两个线程都执行完之后，才开始同时执行第三个 for 循环，并没有交叉。也就是说，通过 #pragma omp for 声明的 for 循环结束时有一个默认的栅障。

### 显式同步栅障 #pragma omp barrier

	#include <stdio.h>
	#include <omp.h>
	
	int main(){
	    #pragma omp parallel
	    {
	        for (int i = 0; i < 100; ++i){
	        printf("%d+\n", i);
	        }
	        #pragma omp barrier
	        for (int j = 0; j < 10; ++j){
	            printf("%d-\n", j);
	        }
	    }    
	}
	
两个线程(具体数目不同 CPU 不同)执行了第一个for循环，当两个线程同时执行完第一个for循环之后，在barrier处进行了同步，然后执行后边的for循环。

### master 通过#pragma omp mater来声明对应的并行程序块只由主线程完成。

	#include <stdio.h>
	#include <omp.h>
	
	int main(){
	    #pragma omp parallel
	    {
	        #pragma omp master
	        {
	            for (int j = 0; j < 10; ++j){
	                printf("%d-\n", j);
	            }
	        }
	
	        printf("This will be shown two or more times\n");
	    }
	    return 0;
	}
	
进入 parallel 声明的并行区域之后，创建了两个(或更多)线程，主线程执行了 for 循环，而另一个线程没有执行 for 循环，而直接进入了 for 循环之后的打印语句，然后执行 for 循环的线程随后还会再执行一次后边的打印语句。

### section 用来指定不同的线程执行不同的部分

通过一个示例说明其使用方法：

	#include <stdio.h>
	#include <omp.h>
	
	int main(){
	    #pragma omp parallel sections // 声明该区域分为若干个 section, section 之间的运行顺序为并行的关系
	    {
	        #pragma omp section // 第一个 section, 由某个线程单独完成
	        for (int i = 0; i < 5; ++i){
	            printf("%d+\n", i);
	        }
	
	        #pragma omp section // 另一个 section, 由某个线程单独完成
	        for (int j = 0; j < 5; ++j){
	            printf("%d-\n", j);
	        }
	    }
	    return 0;
	}
	
因为并行区域中有两个线程，所以两个section同时执行。

## 线程的调度优化

通过前边的介绍，知道了并行区域，默认情况下会自动生成与CPU个数相等的线程，然后并行执行并行区域中的代码，对于并行区域中的for循环，有特殊的声明方式，这样不同的线程可以分别运行for循环变量的不同部分。通过锁同步（atomic、critical、mutex函数）或事件同步（nowait、signal、section、master）来实现并行区域的同步控制。

具体的调度策略均由底层完成，本节介绍几种可以在上层对for循环进行控制的调度策略。

determines which iterations are executed by each thread

+ STATIC
	+ The iteration space is broken in chunks of approximately size N/(num of threads). Then these chunks are assigned to the threads in a Round-Robin fashion.	
+ STATIC, CHUNK
	+ The iteration space is broken in chunks of size N. Then these chunks are assigned to the threads in a Round-Robin fashion.
+ Characteristics of static schedules
	+ Low overhead
	+ Good locality (usually)
	+ Can have load imbalance problems
+ DYNAMIC[,chunk]
	+ Threads dynamically grab chunks of N iterations until all iterations have been executed. If no chunk is specified, N = 1
+ GUIDED[,chunk]
	+ Variant of dynamic. The size of the chunks deceases as the threads grab iterations, but it is at least of size N. If no chunk is specified, N = 1.
+ Characteristics of static schedules
	+ Higher overhead
	+ Not very good locality (usually)
	+ Can solve imbalance problems
+ AUTO
	+ The implementation is allowed to do whatever it wishes. (Do not expect much of it as of now)
+ RUNTIME
	+ The decision is delayed until the program is run through the sched-nvar ICV. It can be set with:
	+ The OMP_SCHEDULE environment variable
	+ The omp_set_schedule() API call
	
能看到这里，如果都跑过一遍的话，应该也就差不多了。上课过程中有啥想法再追加吧。我要去改代码了再见。
