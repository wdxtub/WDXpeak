# Continuous Subarray Sum

出处

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

## Solution

只观察以当前节点为末节点可能的最大sum，并记录一个global sum。对于当前节点，需要判断加入对应数组元素能否使得sum变大。递推公式如下

sum[i] = max(sum[i-1] + A[i], A[i])

因为需要连续的子数组，故计算当前的最大sum，只在乎前一次计算的结果，因此用一个变量每次覆盖即可 (正如我们之前关于简化DP空间的描述)。

## Complexity

遍历一次，时间复杂度 O(n)，空间复杂度可以优化至 O(1)

## Code 

```java
int largestSum(int[] arr){
	int len = arr.length;
	if (len == 0) return 0;
	int maxSum = arr[0];
	int sum = arr[0];
	for (int i = 1; i < len; i++){
		sum = Math.max(sum + arr[i], arr[i]);
		if (sum > maxSum){
			maxSum = sum;
		}
	}
	return maxSum;
}
```


