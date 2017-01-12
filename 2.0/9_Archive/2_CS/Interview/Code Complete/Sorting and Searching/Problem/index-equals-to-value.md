# Index Equals to Value

出处

Find i in a given array that arr[i] == i.

## Solution

本题最直观的想法是线性扫描整个数组，逐一检查元素值与下标是否相同。这样做的时间复杂度是O(n)，但是很明显的缺陷在于这种做法完全没有利用到数组是有序的特性。由于题目中出现了关键字“sorted”，结合“The Rules”中提到的规律：对于有序线性容器的搜索，二分查找或其变种基本上是解题的最佳方法，我们需要尝试设计一种类似于二分查找的算法。通常，我们可以尝试自己举个实例，便于发现普遍规律性：

Index | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 
:--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: 
Value | -7 | -2 | 0 | 3 | 7 | 9 | 10 | 12 | 13

在此例中，A[3] = 3。同时，不难发现一个规律：A[3]左侧的数据满足value < index，A[3]右侧的数据满足value > index。反而言之，如果当前数据满足value < index，则需要搜索的数据必然在其右侧，如“果当前数据满足value > index，则需要搜索的数据必然在其左侧。这样，实际上就可以利用二分查找：比较当前数据值和其下标，选择恰当的半边进行下一步搜索。

## Complexity

时间复杂度同二分查找，为O(logn)。

## Code

非递归方法

```java
int indexSearch(int[] arr){
	int len = arr.length;
	int low = 0;
	int high = len - 1;
	while (low =< high){
		int mid = (low + high) / 2;
		if (mid == arr[mid]){
			return mid;
		} else if (mid > arr[mid]){
			low = mid + 1;
		} else {
			high = mid - 1;			
		}
	}
	return -1;
}
```

递归方法

```java
int indexSearch(int[] arr, int low, int high){
	if (high > low)
		return -1;
	
	int mid = (low + high) / 2;
	if (mid == arr[mid]){
		return mid;
	} else if (mid < arr[mid]){
		return indexSearch(arr, low, mid - 1);
	} else {
		return indexSearch(arr, mid + 1, high);
	}
}
```

---

可能有重复的情况

```java
int magicIndex1(int[] array){
    for (int i = 0; i < array.length; i++){
        if (array[i] == i){
            return i;
        }
    }
    return -1;
}

int magicIndex2(int[] array){
    int start = 0;
    int end = array.length - 1;

    while (end > start){
        int mid = (start + end) / 2;
        if (array[mid] == mid){
            return mid;
        }
        else if (array[mid] > mid){
            end = mid - 1;
        }
        else {
            start = mid + 1;
        }
    }
    return -1;
}

// FOLLOW UP, Use the solution to help understanding
int magicFast3(int[] array){
    return magicFast3(array, 0, array.length - 1);
}

int magicFast3(int[] array, int start, int end){
    if (end < start)
        return -1;

    int midIndex = (start + end) / 2;
    int midValue = array[midIndex];
    if (midValue == midIndex){
        return midIndex;
    }

    // search left
    int leftIndex = Math.min(midIndex - 1, midValue);
    int left = magicFast3(array, start, leftIndex);
    if (left >= 0){
        return left;
    }

    // seach right
    int rightIndex = Math.max(midIndex + 1, midValue);
    int right = magicFast3(array, rightIndex, end);

    return right;
}
```


