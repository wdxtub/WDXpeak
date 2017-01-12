# Search Range

出处

Given a sorted array of integers with duplicates. Implement a function to get the start and end position of a given value.

## Solution

对于完全排序数组的搜索问题，首先应该想到二分查找：我们可以通过二分查找找到相应的元素。其次，题目要求返回该元素的起始和终止位置。那么，我们可以基于二分查找返回的结果，向左向右依次做线性扩展，即查看下一个元素是否依然符合条件。这样做可以得到正确的结果，但是在最坏情况下，该算法复杂度为O(n)。例如，数组为1,1,1,1,1，给定的元素也为1。那么，在我们做线性扩展的时候，我们会遍历数组中的每一个元素。

如何效率更高地找到元素的起始和终止位置？考虑到数组是完全排序的，即被目标值分割的左右半边仍然分别有序，满足局部有序的特征，于是我们可以进一步继续做二分查找：即对左右两个区间分别继续搜索目标元素，在这个过程中，更新目标值出现的最左位置和最右位置。这样，我们可以以O(logn)的复杂度快速获得起始和终止位置。

## Complexity

始终在做二分查找，没有线性查找，因此平均时间复杂度是O(logn)。

## Code

```java
int[] searchRange(int[] arr, int target){
	int len = arr.length;
	int[] range = new int[]{-1, -1};
	helper(arr, 0, len-1, target, range);
	return range;
}

void helper(int[] arr, int low, int high, int target, int[] range){
	if (low > high) return;
	int mid = high - (high - low) / 2;
	
	if (arr[mid] == target){
		if (mid < range[0] || range[0] == -1){
			range[0] = mid;
		}
		if (mid > range[1]){
			range[1] = mid;
		}
		helper(arr, low, mid-1, target, range);
		helper(arr, mid+1, high, target, range);
	} else if (arr[mid] < target) {
		helper(arr, mid+1, high, target, range);
	} else {
		helper(arr, low, mid-1, target, range);
	}
}

```


