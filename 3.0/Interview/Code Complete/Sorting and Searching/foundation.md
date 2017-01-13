# Sorting and Searching

# Bubble Sort 冒泡排序

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

# Selection Sort 选择排序

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

# Insertion Sort 插入排序

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

# Shell Sort 希尔排序

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

# Merge Sort 归并排序

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

# Quick Sort 快速排序

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

# Heap Sort 堆排序

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

# 指标对比

排序方法 | 平均情况 | 最好情况 | 最坏情况 | 辅助空间 | 稳定性
:---: | :---: | :---: | :---: | :---: | :---:
冒泡排序 | O(n2) | O(n) | O(n2) | O(1) | 稳定
选择排序 | O(n2) | O(n2) | O(n2) | O(1) | 不稳定
插入排序 | O(n2) | O(n) | O(n2) | O(1) | 稳定
希尔排序 | O(nlogn)~O(n2)| O(n1.3) | O(n2) | O(1) | 不稳定
堆排序 | O(nlogn) | O(nlogn) | O(nlogn) | O(1) | 不稳定
归并排序 | O(nlogn) | O(nlogn) | O(nlogn) | O(n) | 稳定
快速排序 | O(nlogn) | O(nlogn) | O(n2) | O(logn)~O(n) | 不稳定

# Bucket Sort 桶排序

桶排序和归并排序有那么点点类似，也使用了归并的思想。大致步骤如下：

1. 设置一个定量的数组当作空桶。
2. Divide - 从待排序数组中取出元素，将元素按照一定的规则塞进对应的桶子去。
3. 对每个非空桶进行排序，通常可在塞元素入桶时进行插入排序。
4. Conquer - 从非空桶把元素再放回原来的数组中。”

# Counting Sort 计数排序

计数排序，顾名思义，就是对待排序数组按元素进行计数。使用前提是需要先知道待排序数组的元素范围，将这些一定范围的元素置于新数组中，新数组的大小为待排序数组中最大元素与最小元素的差值。

维基上总结的四个步骤如下：

1. 定新数组大小——找出待排序的数组中最大和最小的元素
2. 统计次数——统计数组中每个值为i的元素出现的次数，存入新数组C的第i项
3. 对统计次数逐个累加——对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）
4. 反向填充目标数组——将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1
5. 其中反向填充主要是为了避免重复元素落入新数组的同一索引处。

# Merge Sort

Merge sort divides then array in half, sorts each of those halves, and then merges them back together. Each of those halves has the same sorting algorithm applied to it. Eventually, you are merging just two single-element arrays. It is the “merge” part that does all the heavy lifting.

The merge method operates by copying all the elements from the target array segment into a helper array, keeping track of where the start of the left and right halves should be (`helperLeft` and `helperRight`).

	void mergesort(int[] array){
	    int[] helper = new int[array.length];
	    mergesort(array, helper, 0, array.length - 1)
	}

	void merge(int[] array, int[] helper, int low, int middle, int high){
	    for (int i = low; i <= high; i++){
	        helper[i] = array[i];
	    }

	    int helperLeft = low;
	    int helperRight = middle + 1;
	    int current = low;

	    while (helperLeft <= middle && helperRight <= high){
	        if (helper[helperLeft] <= helper[helperRight]){
	            array[current] = helper[helperLeft];
	            helperLefting;
	        }
	        else {
	            array[current] = helper[helperRight];
	            helperRight++;
	        }
	        current++;
	    }

	    int remaining = middle - helperLeft;
	    for (int i = 0; i <= remaining; i++){
	        array[current + i] = helper[helperLeft + i];
	    }
	}

You may notice that only the remaining elements from the left half of the helper array are copied into the target array. Why not the right half? The right half doesn't need to be copied because it's already there.

# Quick Sort

In quick sort, we pick a random element and partition the array, such that all numbers that are less than the partitioning element come before all elements that are greater than it. The partitioning can be performed efficiently through a series of swaps.

	void quickSort(int arr[], int left, int right){
	    int index = partition(arr, left, right);
	    if (left < index - 1){
	        quickSort(arr, left, index - 1);
	    }
	    if (index < right){
	        quickSort(arr, index, right);
	    }
	}

	int partition(int arr[], int left, int right){
	    int pivot = arr[(left + right) / 2];
	    while (left <= right){
	        while (arr[left] < pivot) left++;
	        while (arr[right] > pivot) right--;

	        // Swap elements, and move left and right indices
	        if (left <= right){
	            swap(arr, left, right);
	            left++;
	            right--;
	        }
	    }
	    return left;
	}

# Radix Sort

Takes advantage of the fact that integers have finite number of bits. In radix sort, we iterate through each digit of the number, grouping numbers by each digits.

# Binary Search

注意加一和减一的问题

	int binarySearch(int[] a, int x){
	    int low = 0;
	    int high = a.length - 1;
	    int mid;

	    while (low <= high){
	        mid = (low + high) / 2;
	        if (a[mid] < x){
	            low = mid + 1;
	        }
	        else if (a[mid] > x){
	            high = mid - 1;
	        }
	        else {
	            return mid;
	        }
	    }
	    return -1;
	}

	int binarySearchRecursive(int[] a, int x, int low, int high){
	    if (low > high) return -1;

	    int mid = (low + high) / 2;
	    if (a[mid] < x){
	        return binarySearchRecursive(a, x, mid + 1, high);
	    }
	    else if (a[mid] > x){
	        return binarySearchRecursive(a, x, low, mid - 1);
	    }
	    else{
	        return mid;
	    }
	}

## 解题策略

### 动态数据结构的维护

维护动态数据(data stream)的最大值、最小值或中位数，可以考虑使用堆。如果是动态数据求最大的k个元素，因为元素总数量不确定，不能使用quick select，这种情况下也应该用堆解决。

如果需要一个动态插入/删除的有序数据结构，那么可以使用二叉搜索树，因为它天生就是一个动态的有序数组，并且支持检索。

### 对于有序／部分有序容器的搜索

用二分查找(binary search)。

### 数据范围有限、离散

数据范围有限、离散(或存在大量重复数据，即密集数据)的排序问题，一般可以使用桶排序。对于有限位数的数据(如string, `vector<int>`, int)，可以利用基数排序进行数值序或词典序排序。

### Scalability & Memory Limits 问题

对这类问题一般采用Divide & Conquer策略，即对问题进行预处理，将问题的输入进行分割、归类(sorting)，放入相应的桶(单机上的某一块Chunk，或者分布式系统中的一台单机)，再对每个桶进行后期处理，最后合并结果。

整个过程中应该用到哈希函数: 对于Memory Limits问题，一般可以直接利用哈希函数建立对象到索引的直接映射；对Scalability问题，一般可以用哈希表来记录对象与存储该对象的机器之间的映射，在该机器上进一步做映射以获得索引。

## 常见的内排序算法

所谓的内排序是指所有的数据已经读入内存，在内存中进行排序的算法。排序过程中不需要对磁盘进行读写。同时，内排序也一般假定所有用到的辅助空间也可以直接存在于内存中。与之对应地，另一类排序称作外排序，即内存中无法保存全部数据，需要进行磁盘访问，每次读入部分数据到内存进行排序。

### Merge Sort

合并排序(Merge Sort)是一种典型的排序算法，应用“分而治之(divide and conquer)”的算法思路：将线性数据结构(如array、vector或list )分为两个部分，对两部分分别进行排序，排序完成后，再将各自排序好的两个部分合并还原成一个有序结构。由于合并排序不依赖于随机读写，因此具有很强的普适性，适用于链表等数据结构。算法的时间复杂度O(nlogn)，如果是处理数组需要额外O(n)空间，处理链表只需要O(1)空间。算法实现如下：

```
void merge_sort( int array[], int helper[], int left, int right){
    if( left >= right )
        return;

    // divide and conquer: array will be divided into left part and right part
    // both parts will be sorted by the calling merge_sort
    int mid = right - (right - left) / 2;
    merge_sort( array, helper, left, mid );
    merge_sort( array, helper, mid + 1, right);

    // now we merge two parts into one
    int helperLeft = left;
    int helperLeft = left;
    int helperRight = mid + 1;
    int curr = left;
    for(int i = left; i <= right; i++)
        helper[i] = array[i];
    while( helperLeft <= mid && helperRight <= right ){
        if( helper[helperLeft] <= helper[helperRight] )
            array[curr++] = helper[helperLeft++];
        else
            array[curr++] = helper[helperRight++];
    }

    // left part has some large elements remaining. Put them into the right side
    while( helperLeft <= mid )
        array[curr++] = helper[helperLeft++];
}
```

当递归调用merge_sort返回时，array的左右两部分已经分别由子函数排序完成，我们利用helper数组暂存array中的数值，再利用两个while循环完成合并。helper数组的左右半边就是两个排序完的队列，第一个while循环相当于比较队列头，将较小的元素取出放入array，最后使得array的左半边由小到大排序完成。第二个while循环负责扫尾，把helper左半边剩余元素复制入array中。注意，此时我们不需要对helper右半边做类似操作，因为即使右半边有剩余元素，它们也已经处于array中恰当的位置。

关于合并排序更多理论方面的讨论，请见“工具箱”。

### Quick Sort (快速排序)

快速排序(Quick Sor)是最为常用的排序算法，C++自带的排序算法的实现就是快速排序。该算法以其高效性，简洁性，被评为20世纪十大算法之一(虽然合并排序与堆排序的时间复杂度量级相同，但一般还是比快速排序慢常数倍)。快速排序的算法核心与合并排序类似，也采用“分而治之”的想法：随机选定一个元素作为轴值，利用该轴值将数组分为左右两部分，左边元素都比轴值小，右边元素都比轴值大，但它们不是完全排序的。在此基础上，分别对左右两部分分别递归调用快速排序，使得左右部分完全排序。算法的平均时间复杂度是O(nlogn)，在最坏情况下为O(n^2)，额外空间复杂度O(logn)。算法实现如下：

```
int partition( int array[], int left, int right ) {
    int pivot = array[right];
    while( left != right ){
        while( array[left] < pivot && left < right)
            left++;
        if (left < right) {
            swap( array[left], array[right--]);
        }
        while( array[right] > pivot && left < right)
            right--;
        if( left < right )
            swap( array[left++], array[right]);
    }
    //array[left] = pivot;
    return left;
}
void qSort( int array[], int left, int right ){
    if( left >=right )
        return;
    int index = partition( array, left, right);
    qSort(array, left, index - 1);
    qSort(array, index + 1, right);
}
```

partition函数先选定数组right下标所指的元素作为轴值，用pivot变量存储该元素值。然后，右移left，即从左向右扫描数组，直到发现某个元素大于轴值或者扫描完成。如果某个元素大于轴值，则将该元素与轴值交换。该操作特性在于：保证交换后轴值左侧的元素都比轴值小。再次，左移right，即从右向左扫描数组，直到发现某个元素小于轴值或者扫描完成。如果某个元素小于轴值，则将该元素与轴值交换。该操作特性在于：保证交换后轴值右侧的元素都比轴值大。重复上述过程直到left和right相遇，最终相遇的位置即为轴值所在位置。由于上述操作的特性，最终轴值左侧的元素都比轴值小，轴值右侧的元素都比轴值大。

关于快速排序的更多理论讨论请见“工具箱”。C++标准模版库提供函数sort，实现快速排序的功能: sort( iterator first, iterator last, Compare comp ); // can aslo be pointers here

### Heap Sort(堆排序)

堆排序(Heap Sort)利用了我们在Chapter 4 Trees and Graphs中提到的堆作为逻辑存储结构，将输入array变成一个最大值堆。然后，我们反复进行堆的弹出操作。回顾之前所述的弹出过程：将堆顶元素与堆末元素交换，堆的大小减一，向下移动新的堆顶以维护堆的性质。事实上，该操作等价于每次将剩余的最大元素移动到数组的最右边，重复这样的操作最终就能获得由小到大排序的数组。初次建堆的时间复杂度O(n)，删除堆顶元素并维护堆的性质需要O(logn)，这样的操作一共进行n次，故最终时间复杂度O(nlogn)。我们不需要利用额外空间，故空间复杂度O(1)。具体实现如下：

```
void heapSort(int array[], int size)  { 
    Heapify(array, size);
    for (int i = 0; i < size - 1; i++)
       popHeap(array);
}
```

Heapify和popHeap的实现参考Chapter 4 Trees and Graphs 。

### Bucket Sort (桶排序) 和 Radix Sort (基数排序)

桶排序(Bucket Sort) 和基数排序(Radix Sort)不需要进行数据之间的两两比较，但是需要事先知道数组的一些具体情况。特别地，桶排序适用于知道待排序数组大小范围的情况。其特性在于将数据根据其大小，放入合适的“桶(容器)”中，再依次从桶中取出，形成有序序列。具体实现如下：

```
void BucketSort(int array[], int n, int max)
{
    // array of length n，all records in the range of [0,max)
    int tempArray[n];
    int i;
    for (i = 0; i < n; i++)
        tempArray[i] = array[i];

    int count[max];    // buckets
    memset(count, 0, max * sizeof(int));

    for (i = 0; i < n; i++) // put elements into the buckets
        count[array[i]]++;
    for (i = 1; i < max; i++)
        count[i] = count[i-1] + count [i];  // count[i] saves the starting index (in array) of value i+1

    // for value tempArray[i], the last index should be count[tempArray[i]]-1
    for (i = n-1; i >= 0; i--)
        array[--count[tempArray[i]]] = tempArray[i];
}
```

该实现总的时间代价O(max+n)，适用于max相对n较小的情况。空间复杂度也为O(max+n)，用以记录原始数组和桶计数。

桶排序只适合max很小的情况，如果数据范围很大，可以将一个记录的值即排序码拆分为多个部分来进行比较，即使用基数排序。基数排序相当于将数据看作一个个有限进制数，按照由高位到低位(适用于字典序)，或者由低位到高位(适用于数值序)进行排序。排序具体过程如下：对于每一位，利用桶排序进行分类，在维持相对顺序的前提下进行下一步排序，直到遍历所有位。该算法复杂度为O(k*n)，k为位数(或者字符串长度)。直观上，基数排序进行了k次桶排序。具体实现如下：

```
void RadixSort(int Array[], int n, int digits, int radix)
{
    // n is the length of the array
    // digits is the number of digits
    int  *TempArray = new int[n];
    int *count = new int[radix]; // radix buckets
    int i, j, k;
    int Radix = 1; // radix modulo, used to get the ith digit of Array[j]
    // for ith digit
    for (i = 1; i <= digits; i++)  {
        for (j = 0; j < radix; j++)
            count[j] = 0;            // initialize counter
        for (j = 0; j < n; j++) {
            // put elements into buckets
            k = (Array[j] / Radix) % radix;  // get a digit
            count[k]++;
        }
        
        for (j = 1; j < radix; j++) {
            // count elements in the buckets
            count[j] = count[j-1] + count[j];
        }

        // bucket sort
        for (j = n-1; j >= 0; j--)  {
            k = (Array[j] / Radix ) % radix;
            count[k]--;
            TempArray[count[k]] = Array[j];
        }
        for (j = 0; j < n; j++) {
            // copy data back to array
            Array[j] = TempArray[j];
        }
        Radix *= radix;      // get the next digit
    }
}
```

与其他排序方式相比，桶排序和基数排序不需要交换或比较，它更像是通过逐级的分类来把元素排序好。

## 常见的外排序算法

外排序算法的核心思路在于把文件分块读到内存，在内存中对每块文件依次进行排序，最后合并排序后的各块数据，依次按顺序写回文件。相比于内排序，外排序需要进行多次磁盘读写，因此执行效率往往低于内排序，时间主要花费于磁盘读写上。我们给出外排序的算法步骤如下：

假设文件需要分成k块读入，需要从小到大进行排序

1. 依次读入每个文件块，在内存中对当前文件块进行排序(应用恰当的内排序算法)。此时，每块文件相当于一个由小到大排列的有序队列
2. 在内存中建立一个最小值堆，读入每块文件的队列头
3. 弹出堆顶元素，如果元素来自第i块，则从第i块文件中补充一个元素到最小值堆。弹出的元素暂存至临时数组
4. 当临时数组存满时，将数组写至磁盘，并清空数组内容。
5. 重复过程3)，4)，直至所有文件块读取完毕

## 快速选择算法 (quick selection algorithm)

快速选择算法能够在平均O(n)时间内从一个无序数组中返回第k大的元素。算法实际上利用了快速排序的思想，将数组依照一个轴值分割成两个部分，左边元素都比轴值小，右边元素都比轴值大。由于轴值下标已知，则可以判断所求元素落在数组的哪一部分，并在那一部分继续进行上述操作，直至找到该元素。与快排不同，由于快速选择算法只在乎所求元素所在的那一部分，所以时间复杂度是O(n)。关于算法复杂度的理论分析请见“工具箱”给出的参考资料。我们给出算法实现如下：

```
int partition( int array[], int left, int right ) {
    int pivot = array[right];
    while( left != right ){
        while( array[left] < pivot && left < right)
            left++;
            left++;
        if (left < right) {
            swap( array[left], array[right--]);
        }
        while( array[right] > pivot && left < right)
            right--;
        if( left < right )
            swap( array[left++], array[right]);
    }
    return left;
}

int quick_select(int array[], int left, int right, int k)
{
    if ( left >= right )
        return array[left];
    int index = partition(array, left, right);
    int size = index - left + 1;
    if ( size == k )
        return array[left + k - 1]; // the pivot is the kth largest element
    else if ( size > k )
        return quick_select(array, left, index - 1, k);
    else
        return quick_select(array, index + 1, right , k - size);
}
```

> Get the k largest elements in an array with O(n) expected time, they don’t need to be sorted.

解题分析：实际上和quick select的应用场景是一致的，先找到第k大的元素，再将数组重新整理，找出比第k大的元素小的所有元素。

> There are n points on a 2D plan, find the k points that are closest to origin ( x= 0, y= 0).

解题分析：在这里已知点的数量，因此k个点到原点的距离构成size确定的静态数组，应该对这个数组使用快速选择算法。

## 二分查找 (Binary search)

对于已排序的有序线性容器而言(比如数组，vector)，二分查找(Binary search)几乎总是最优的搜索方案。二分查找将容器等分为两部分，再根据中间节点与待搜索数据的相对大小关系，进一步搜索其中某一部分。二分查找的算法复杂度为O(logn)，算法复杂度的具体分析请见“工具箱”给出的参考资料。算法实现如下：

```
int binarySearch(int *array, int left, int right, int value) {
    if (left > right) {
        // value not found
        return -1;
    }

    int mid = right - (right - left) / 2;
    if (array[mid] == value) {
        return mid;
    } else if (array[mid] < value) {
        return binarySearch(array, mid + 1, right, value);
    } else {
        return binarySearch(array, left, mid - 1, value);
    }
}
```

对于局部有序的数据，也可以根据其局部有序的特性，尽可能地利用逼近、剪枝，使用二分查找的变种进行搜索。


