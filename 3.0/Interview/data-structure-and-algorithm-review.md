# 数据结构及算法复习

<!-- MarkdownTOC -->

- Linked List 链表
    - 反转链表
    - 删除某个节点
    - Dummy Node
    - 快慢指针
- Binary Tree 二叉树
    - 树的遍历
    - 递归法遍历
    - 非递归遍历
    - 分治法 Divide & Conquer
- Binary Search Tree 二叉查找树
- 基础排序算法
    - Bubble Sort 冒泡排序
    - Selection Sort 选择排序
    - Insertion Sort 插入排序
    - Shell Sort 希尔排序
    - Merge Sort 归并排序
    - Quick Sort 快速排序
    - Heap Sort 堆排序
    - 指标对比
    - Bucket Sort 桶排序
    - Counting Sort 计数排序
- Basics Miscellaneous
    - XOR 异或
    - 移位操作
- String 字符串
- 有用的网址

<!-- /MarkdownTOC -->

## Linked List 链表

+ **两种存储方式**
    + 顺序存储结构：随机读取，访问时是 O(1)
    + 链式存储结构：插入和删除 O(1)，访问时最坏是 O(n)
+ 分类（根据指针域）
    + 单向链表
    + 双向链表
    + 循环链表

### 反转链表

+ 访问某个节点 `curt.next` 时，要检验 `curt` 是否为 `null`
+ 要把反转后的最后一个节点（即第一个节点）指向 `null`

### 删除某个节点

+ 由于需要知道前继节点的信息，而前继节点可能会导致表头产生变化，所以需要一些技巧 `Dummy Node`
+ 链表指针的鲁棒性
    + 访问某个节点 `curt.next` 时，要检验 `curt` 是否为 `null`
    + 全部操作结束后，判断是否有环；若有，则置其中一端为 `null`

### Dummy Node

+ 是一个虚拟节点 `dummy.next = head`
+ 针对单向链表没有前向指针的问题，保证链表的 `head` 不会在删除操作中丢失
+ 也可以用来进行 `head` 节点（但比较少见）
+ 当链表的 `head` 可能有变化时，使用 dummy node 可以简化代码，最后返回 `dummy.next` 即可

### 快慢指针

+ 快慢指的是指针向前移动的步长，一般来说，快指针每次移动 2，慢指针每次移动 1
+ 主要有两个应用
    + **快速找出未知长度单链表的中间节点**
        + 设置两个指针 `*fast` 和 `*slow` 都指向头节点
        + `*fast` 移动速度是 `*slow` 的两倍
        + `*fast` 指向末尾节点时，`*slow` 正好就在中间
    + **判断单链表是否有环**
        + 设置两个指针 `*fast` 和 `*slow` 都指向头节点
        + `*fast` 移动速度是 `*slow` 的两倍
        + 如果 `*fast == null` 说明该单链表不是循环链表
        + 如果 `*fast == *slow` 说明该链表是循环链表
+ 其他应用
    + **找倒数第 N 个节点**
        + 设置两个指针 `*fast` 和 `*slow` 都指向头节点
        + `*fast` 先移动 N 步，然后两个指针一起前进
        + `*fast` 到达末尾时，`*slow` 即为倒数第 N 个节点


## Binary Tree 二叉树

二叉树是每个节点最多有两个子树的树结构，子树有左右之分，二叉树常被用于实现二叉查找树和二叉堆。

二叉树的第i层至多有 `2^(i-1)` 个结点；深度为k的二叉树至多有 `2^k - 1` 个结点；对任何一棵二叉树T，如果其终端结点数为 n0, 度为2的结点数为 n2, 则 `n0 = n2 + 1`

一棵深度为 k, 且有 `2^(k−1)` 个节点称之为满二叉树；深度为 k，有 n 个节点的二叉树，当且仅当其每一个节点都与深度为 k 的满二叉树中，序号为 1 至 n 的节点对应时，称之为完全二叉树。完全二叉树中重在节点标号对应

### 树的遍历

+ 三个主要步骤
    + 对当前节点进行操作
    + 遍历左边子节点
    + 遍历右边子节点

顺序不同形成了不同的遍历方式，通常用递归的方式进行理解和实现

**深度优先**

先访问子节点，再访问父节点，根据顺序不同有三种方式

1. 前序 pre-order: 先根后左再右
2. 中序 in-order: 先左后根再右
3. 后序 post-order: 先左后右再根

**广度优先**

先访问根节点，沿着树的宽度遍历子节点，直到所有节点均被访问为止

### 递归法遍历

前序中序后序

### 非递归遍历

前序中序后序 + 广度

### 分治法 Divide & Conquer

经典题目

1. 二分搜素
2. 大整数乘法
3. Strassen 矩阵乘法
4. 棋盘覆盖
5. 归并排序
6. 快速排序
7. 循环赛日程表
8. 汉诺塔

## Binary Search Tree 二叉查找树

一颗二叉查找树(BST)是一颗二叉树，其中每个节点都含有一个可进行比较的键及相应的值，且每个节点的键都大于等于左子树中的任意节点的键，而小于右子树中的任意节点的键。

使用中序遍历可得到有序数组，这是二叉查找树的又一个重要特征。

二叉查找树使用的每个节点含有两个链接，它是将链表插入的灵活性和有序数组查找的高效性结合起来的高效符号表实现。

二叉树中每个节点只能有一个父节点(根节点无父节点)，只有左右两个链接，分别为左子节点和右子节点。

## 基础排序算法

稳定性：如果排序后文件中拥有相同键的项的相对位置不变，这种排序方式是稳定的。

常见算法根据是否需要比较可以这样分类

+ Comparison Sorting
    + Bubble Sort
    + Selection Sort
    + Insertion Sort
    + Shell Sort
    + Merge Sort
    + Quick Sort
    + Heap Sort
+ Bucket Sort
+ Counting Sort
+ Radix Sort

### Bubble Sort 冒泡排序

冒泡排序的原理非常简单，它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。

步骤：

1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2. 对第0个到第n-1个数据做同样的工作。这时，最大的数就“浮”到了数组最后的位置上。
3. 针对所有的元素重复以上的步骤，除了最后一个。
4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

```python
def bubble_sort(arry):
    n = len(arry)                   #获得数组的长度
    for i in range(n):
        for j in range(1,n-i):
            if  arry[j-1] > arry[j] :       #如果前者比后者大
                arry[j-1],arry[j] = arry[j],arry[j-1]      #则交换两者
    return arry
```

针对上述代码还有两种优化方案。

优化1：某一趟遍历如果没有数据交换，则说明已经排好序了，因此不用再进行迭代了。用一个标记记录这个状态即可。

```python
#优化1：某一趟遍历如果没有数据交换，则说明已经排好序了，因此不用再进行迭代了。
#用一个标记记录这个状态即可。
def bubble_sort2(ary):
    n = len(ary)
    for i in range(n):
        flag = 1                    #标记
        for j in range(1,n-i):
            if  ary[j-1] > ary[j] :
                ary[j-1],ary[j] = ary[j],ary[j-1]
                flag = 0
        if flag :                   #全排好序了，直接跳出
            break
    return ary
```

优化2：记录某次遍历时最后发生数据交换的位置，这个位置之后的数据显然已经有序，不用再排序了。因此通过记录最后发生数据交换的位置就可以确定下次循环的范围了。

```python
#优化2：记录某次遍历时最后发生数据交换的位置，这个位置之后的数据显然已经有序了。
# 因此通过记录最后发生数据交换的位置就可以确定下次循环的范围了。
def bubble_sort3(ary):
    n = len(ary)
    k = n                           #k为循环的范围，初始值n
    for i in range(n):
        flag = 1
        for j in range(1,k):        #只遍历到最后交换的位置即可
            if  ary[j-1] > ary[j] :
                ary[j-1],ary[j] = ary[j],ary[j-1]
                k = j               #记录最后交换的位置
                flag = 0
        if flag :
            break
    return ary
```

### Selection Sort 选择排序

选择排序无疑是最简单直观的排序。它的工作原理如下。

步骤：

1. 在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
2. 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
3. 以此类推，直到所有元素均排序完毕。

```python
def select_sort(ary):
    n = len(ary)
    for i in range(0,n):
        min = i                             #最小元素下标标记
        for j in range(i+1,n):
            if ary[j] < ary[min] :
                min = j                     #找到最小值的下标
        ary[min],ary[i] = ary[i],ary[min]   #交换两者
    return ary
```

### Insertion Sort 插入排序

插入排序的工作原理是，对于每个未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

步骤：

1. 从第一个元素开始，该元素可以认为已经被排序
2. 取出下一个元素，在已经排序的元素序列中从后向前扫描
3. 如果被扫描的元素（已排序）大于新元素，将该元素后移一位
4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
5. 将新元素插入到该位置后
6. 重复步骤2~5

```python
def insert_sort(ary):
    n = len(ary)
    for i in range(1,n):
        if ary[i] < ary[i-1]:
            temp = ary[i]
            index = i           #待插入的下标
            for j in range(i-1,-1,-1):  #从i-1 循环到 0 (包括0)
                if ary[j] > temp :
                    ary[j+1] = ary[j]
                    index = j   #记录待插入下标
                else :
                    break
            ary[index] = temp
    return ary
```

### Shell Sort 希尔排序

希尔排序，也称递减增量排序算法，实质是分组插入排序。由 Donald Shell 于1959年提出。希尔排序是非稳定排序算法。

希尔排序的基本思想是：将数组列在一个表中并对列分别进行插入排序，重复这过程，不过每次用更长的列（步长更长了，列数更少了）来进行。最后整个表就只有一列了。将数组转换至表是为了更好地理解这算法，算法本身还是使用数组进行排序。

例如，假设有这样一组数`[ 13 14 94 33 82 25 59 94 65 23 45 27 73 25 39 10 ]`，如果我们以步长为5开始进行排序，我们可以通过将这列表放在有5列的表中来更好地描述算法，这样他们就应该看起来是这样：

    13 14 94 33 82
    25 59 94 65 23
    45 27 73 25 39
    10

然后我们对每列进行排序：

    10 14 73 25 23
    13 27 94 33 39
    25 59 94 65 82
    45

将上述四行数字，依序接在一起时我们得到：`[ 10 14 73 25 23 13 27 94 33 39 25 59 94 65 82 45 ]`。这时10已经移至正确位置了，然后再以3为步长进行排序：

    10 14 73
    25 23 13
    27 94 33
    39 25 59
    94 65 82
    45

排序之后变为：

    10 14 13
    25 23 33
    27 25 59
    39 65 73
    45 94 82
    94

最后以1步长进行排序（此时就是简单的插入排序了）。

```python
def shell_sort(ary):
    n = len(ary)
    gap = round(n/2)       #初始步长 , 用round四舍五入取整
    while gap > 0 :
        for i in range(gap,n):        #每一列进行插入排序 , 从gap 到 n-1
            temp = ary[i]
            j = i
            while ( j >= gap and ary[j-gap] > temp ):    #插入排序
                ary[j] = ary[j-gap]
                j = j - gap
            ary[j] = temp
        gap = round(gap/2)                     #重新设置步长
    return ary
```

上面源码的步长的选择是从n/2开始，每次再减半，直至为0。步长的选择直接决定了希尔排序的复杂度

### Merge Sort 归并排序

归并排序是采用分治法的一个非常典型的应用。归并排序的思想就是先递归分解数组，再合并数组。

先考虑合并两个有序数组，基本思路是比较两个数组的最前面的数，谁小就先取谁，取了后相应的指针就往后移一位。然后再比较，直至一个数组为空，最后把另一个数组的剩余部分复制过来即可。

再考虑递归分解，基本思路是将数组分解成left和right，如果这两个数组内部数据是有序的，那么就可以用上面合并数组的方法将这两个数组合并排序。如何让这两个数组内部是有序的？可以再二分，直至分解出的小组只含有一个元素时为止，此时认为该小组内部已有序。然后合并排序相邻二个小组即可。

```python
def merge_sort(ary):
    if len(ary) <= 1 : return ary
    num = int(len(ary)/2)       #二分分解
    left = merge_sort(ary[:num])
    right = merge_sort(ary[num:])
    return merge(left,right)    #合并数组

def merge(left,right):
    '''合并操作，
    将两个有序数组left[]和right[]合并成一个大的有序数组'''
    l,r = 0,0           #left与right数组的下标指针
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result
```

### Quick Sort 快速排序

快速排序通常明显比同为Ο(n log n)的其他算法更快，因此常被采用，而且快排采用了分治法的思想，所以在很多笔试面试中能经常看到快排的影子。可见掌握快排的重要性。

步骤：

1. 从数列中挑出一个元素作为基准数。
2. 分区过程，将比基准数大的放到右边，小于或等于它的数都放到左边。
3. 再对左右区间递归执行第二步，直至各区间只有一个数。

```python
def quick_sort(ary):
    return qsort(ary,0,len(ary)-1)

def qsort(ary,left,right):
    #快排函数，ary为待排序数组，left为待排序的左边界，right为右边界
    if left >= right : return ary
    key = ary[left]     #取最左边的为基准数
    lp = left           #左指针
    rp = right          #右指针
    while lp < rp :
        while ary[rp] >= key and lp < rp :
            rp -= 1
        while ary[lp] <= key and lp < rp :
            lp += 1
        ary[lp],ary[rp] = ary[rp],ary[lp]
    ary[left],ary[lp] = ary[lp],ary[left]
    qsort(ary,left,lp-1)
    qsort(ary,rp+1,right)
    return ary
```

### Heap Sort 堆排序

堆排序在 top K 问题中使用比较频繁。堆排序是采用二叉堆的数据结构来实现的，虽然实质上还是一维数组。二叉堆是一个近似完全二叉树 。

**二叉堆具有以下性质：**

1. 父节点的键值总是大于或等于（小于或等于）任何一个子节点的键值。
2. 每个节点的左右子树都是一个二叉堆（都是最大堆或最小堆）。

**步骤：**

1. 构造最大堆（`Build_Max_Heap`）：若数组下标范围为0~n，考虑到单独一个元素是大根堆，则从下标n/2开始的元素均为大根堆。于是只要从n/2-1开始，向前依次构造大根堆，这样就能保证，构造到某个节点时，它的左右子树都已经是大根堆。
2. 堆排序（HeapSort）：由于堆是用数组模拟的。得到一个大根堆后，数组内部并不是有序的。因此需要将堆化数组有序化。思想是移除根节点，并做最大堆调整的递归运算。第一次将heap[0]与heap[n-1]交换，再对heap[0...n-2]做最大堆调整。第二次将heap[0]与heap[n-2]交换，再对heap[0...n-3]做最大堆调整。重复该操作直至heap[0]和heap[1]交换。由于每次都是将最大的数并入到后面的有序区间，故操作完后整个数组就是有序的了。
4. 最大堆调整（`Max_Heapify`）：该方法是提供给上述两个过程调用的。目的是将堆的末端子节点作调整，使得子节点永远小于父节点。

```python
def heap_sort(ary) :
    n = len(ary)
    first = int(n/2-1)       #最后一个非叶子节点
    for start in range(first,-1,-1) :     #构造大根堆
        max_heapify(ary,start,n-1)
    for end in range(n-1,0,-1):           #堆排，将大根堆转换成有序数组
        ary[end],ary[0] = ary[0],ary[end]
        max_heapify(ary,0,end-1)
    return ary

#最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
#start为当前需要调整最大堆的位置，end为调整边界
def max_heapify(ary,start,end):
    root = start
    while True :
        child = root*2 +1               #调整节点的子节点
        if child > end : break
        if child+1 <= end and ary[child] < ary[child+1] :
            child = child+1             #取较大的子节点
        if ary[root] < ary[child] :     #较大的子节点成为父节点
            ary[root],ary[child] = ary[child],ary[root]     #交换
            root = child
        else :
            break

```

### 指标对比

排序方法 | 平均情况 | 最好情况 | 最坏情况 | 辅助空间 | 稳定性
:---: | :---: | :---: | :---: | :---: | :---:
冒泡排序 | O(n2) | O(n) | O(n2) | O(1) | 稳定
选择排序 | O(n2) | O(n2) | O(n2) | O(1) | 不稳定
插入排序 | O(n2) | O(n) | O(n2) | O(1) | 稳定
希尔排序 | O(nlogn)~O(n2)| O(n1.3) | O(n2) | O(1) | 不稳定
堆排序 | O(nlogn) | O(nlogn) | O(nlogn) | O(1) | 不稳定
归并排序 | O(nlogn) | O(nlogn) | O(nlogn) | O(n) | 稳定
快速排序 | O(nlogn) | O(nlogn) | O(n2) | O(logn)~O(n) | 不稳定

### Bucket Sort 桶排序

桶排序和归并排序有那么点点类似，也使用了归并的思想。大致步骤如下：

1. 设置一个定量的数组当作空桶。
2. Divide - 从待排序数组中取出元素，将元素按照一定的规则塞进对应的桶子去。
3. 对每个非空桶进行排序，通常可在塞元素入桶时进行插入排序。
4. Conquer - 从非空桶把元素再放回原来的数组中。”

### Counting Sort 计数排序

计数排序，顾名思义，就是对待排序数组按元素进行计数。使用前提是需要先知道待排序数组的元素范围，将这些一定范围的元素置于新数组中，新数组的大小为待排序数组中最大元素与最小元素的差值。

维基上总结的四个步骤如下：

1. 定新数组大小——找出待排序的数组中最大和最小的元素
2. 统计次数——统计数组中每个值为i的元素出现的次数，存入新数组C的第i项
3. 对统计次数逐个累加——对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）
4. 反向填充目标数组——将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1
5. 其中反向填充主要是为了避免重复元素落入新数组的同一索引处。

## Basics Miscellaneous

### XOR 异或

> 异或：相同为0，不同为1。也可用「不进位加法」来理解。

异或操作的一些特点：

    x ^ 0 = x
    x ^ 1s = ~x // 1s = ~0
    x ^ (~x) = 1s
    x ^ x = 0 // interesting and important!
    a ^ b = c => a ^ c = b, b ^ c = a // swap
    a ^ b ^ c = a ^ (b ^ c) = (a ^ b) ^ c // associative

### 移位操作

移位操作可近似为乘以/除以2的幂。0b0010 * 0b0110等价于0b0110 << 2. 下面是一些常见的移位组合操作。

1. 将x最右边的n位清零 `x & (~0 << n)`
2. 获取x的第n位值(0或者1) `x & (1 << n)`
3. 获取x的第n位的幂值 `(x >> n) & 1`
4. 仅将第n位置为1 `x | (1 << n)`
5. 仅将第n位置为0 `x & (~(1 << n))`
6. 将x最高位至第n位(含)清零 `x & ((1 << n) - 1)`
7. 将第n位至第0位(含)清零 `x & (~((1 << (n + 1)) - 1))`
8. 仅更新第n位，写入值为v; v为1则更新为1，否则为0 `mask = ~(1 << n); x = (x & mask) | (v << i)`

## String 字符串

常见的做法是从尾部开始编辑，从后往前你想操作。因为尾部往往有足够的空间，可以直接修改而不用担心字符串前面的数据。



## 有用的网址

+ [VisuAlgo](http://visualgo.net): 数据结构和算法可视化
