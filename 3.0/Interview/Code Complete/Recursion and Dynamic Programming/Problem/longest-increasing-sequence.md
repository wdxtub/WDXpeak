# Longest Increasing Sequence

出处

Find the longest increasing subsequence in an integer array. E.g, for array {1, 3, 2, 4}, return 3.

## Solution

用DP Table来记录以当前节点为末节点的序列的最大长度，其数值取决于当前节点之前的所有节点：如果当前节点对应的数组数值大于之前的某个节点，那么可以将当前节点对应的数组数值append在该节点的最长序列之后。最终，我们在DP table中将当前节点的结果更新为所有可能解的最大值。递推关系如下:

maxLength(i) = max{ maxLength(k), k = 0~i-1 and array[i] > array[k] } + 1;

另外，如果需要输出最长序列，那么无非就是对于每个节点额外记录一个index，该index是以当前节点为末节点的最长序列中，前驱元素在数组中的下标。

## Complexity

两层循环，时间复杂度 O(n^2 )，空间复杂度 O(n)

## Code  

```java
int lis(int[] arr){
	int len = arr.length;
	int[] dp = new int[len];
	dp[0] = 1;
	int maxLength = 0;
	for (int i = 1; i < dp.length; i++){
		for (int j = 0; j < i; j++){
			if (arr[i] > arr[j] && dp[j] + 1 > dp[i]){
				dp[i] = dp[j]+1;
			} else {
				dp[i] = 1;
			}
		}
	}
	for (int i = 0; i < dp.length; i++){
		if (dp[i] > maxLength){
			maxLength = dp[i];
		}
	}
	return maxLength;
}
```

## 分析与解法

### 解法一 转换为最长公共子序列问题

比如原数组为

    A{5， 6， 7， 1， 2， 8}，

当我们对这个数组进行排序后，排序后的数组为：

    A'{1， 2， 5， 6， 7， 8}。

然后想求数组`A`的最长递增子序列，其实就是求数组`A`与它的排序数组`A'`的最长公共子序列，原因是原数组`A`的子序列顺序保持不变，而且排序后`A'`本身就是递增的，这样，就保证了两序列的最长公共子序列的递增特性。

如此，若想求数组A的最长递增子序列，其实就是求数组A与它的排序数组A‘的最长公共子序列。

### 解法二 动态规划

想到这个问题不能改变元素各自的相对顺序，所以我们不能排序，在不能排序的情况下，我们考虑下是否能用动态规划解决。

定义`dp[i]`为以`ai`为末尾的最长递增子序列的长度，故以`ai`结尾的递增子序列

+ 要么是只包含`ai`的子序列
+ 要么是在满足`j<i`并且`aj<ai`的以`ai`为结尾的递增子序列末尾，追加上`ai`后得到的子序列

如此，便可建立递推关系，在O(N^2)时间内解决这个问题。参考代码如下：

```cpp
int n;
int a[n];

int dp[n];

void lis()
{
    int res = 0;
    int i;
    for (i = 0; i < n; i++)
    {
        dp[i] = (dp[i] > dp[i + 1] )? dp[i]:dp[i + 1];
    }
    res = (res > dp[i])?res:dp[i];
    printf("%d\n,res");
}
```


