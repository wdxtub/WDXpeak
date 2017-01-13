# Search Rotated Array

出处

An array is sorted without duplicates. However, someone mysteriously shifted all the elements in this array (e.g. 1,2,3,4,5 -> 5,1,2,3,4). Implement a function to find an element in such array (return -1 if no such element).

## Solution

如果是在完全有序的数组中进行搜索，最优的解法无疑是二分查找。本题中，平移操作后的数组不再是完全有序了，因此我们不能直接应用二分查找。回顾二分查找算法：二分查找将容器等分为两部分，再根据中间节点与待搜索数据的相对大小关系，进一步搜索其中某一部分。算法本质在于，通过数据之间的相互比较，每次我们只需要搜索容器的某一半边。事实上，对于本题而言，既然数据具备局部有序的特性，如果通过适当的条件判断，每次能够减半搜索范围，那么我们同样可以达到二分查找的效果。关键问题在于：如何通“过数据之间的相互比较，确定需要检索的那一半数据？

首先，我们可以通过一个实例观察平移后的数组有什么特性：假设数组0,1,2,3,4,5,6,7,8,9,10通过平移变为7,8,9,10,0,1,2,3,4,5,6，要求搜索4。根据二分查找的算法，我们将4与容器的中间元素进行比较，由此确定需要继续搜索的半边。本例中，中间元素为1，即将数组切割为7,8,9,10,0,1与1,2,3,4,5,6。不难发现，每次切割都保证至少有一半数组是完全有序的，并且，我们可以通过比较切割后两半数组各自的头尾数据大小，确定哪一半是完全有序的。

现在，我们进一步考虑如何减半搜索范围。由于至少有一半数组是有序的(并且我们知道数据的范围)，那么可能有两种情况：

1. 待搜索元素落在有序的那一半(即大于最左元素且小于最右元素)。
2. 待搜索元素不在有序的那一半。

对于情况1，我们只需要搜索那半边即可。对于情况2，我们只需搜索另一半边即可。这样，无论出现哪种情况，我们都可以减半搜索范围。

总结一下我们的算法：

1. 通过中间元素将数组划分为两个半边
2. 通过比较切割后两半数组各自的头尾数据大小，确定哪一半是完全有序的
3. 判断待搜索元素落在哪个半边，减半搜索范围

## Complexity

由于我们每次能够减半搜索范围，故时间复杂度与二分查找相同，为O(logn)。

## Code

```java
int searchInRotatedArray(int[] arr, int target){
	int len = arr.length;
	return helper(arr, 0, len-1, target);
}

int helper(int[] arr, int low, int high, int target){
	if (low > high) return -1;

	int mid = high - (high - low) / 2;
	if (arr[mid] == target)
		return mid;
	
	
	if (arr[low] <= arr[mid]){
		// left part is sorted
		if (target >= arr[low] && target <= arr[mid]){
			return helper(arr, low, mid-1, target);
		} else {
			return helper(arr, mid+1, high, target);
		}
	} else {
		// right part is sorted
		if (target >= arr[mid] && target <= arr[high]){
			return helper(arr, mid+1, high, target);
		} else {
			return helper(arr, low, mid-1, target);
		}
	}
}

```

