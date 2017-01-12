# Single Element

Given an array of integers, every element appears twice except for one. Please write a function to find that single one.

## Solution

当遇到某些题目需要统计一个元素集中元素出现的次数，应该直觉反应使用哈希表，key是元素，value是出现的次数。扫描整个数组建立哈希表，再次扫描table看哪个元素出现了一次。这样做的时间复杂度O(n+n)。

事实上，能在面试中给出这样的解答已经足够好，而且这种解法具有普适性，应该首先想到。对于这道特殊的题目，能不能做的更好？我们考虑两个数如果相等，二进制表示有什么特点？很明显，当然是二进制表示每位比特都相等。能否通过某种二进制操作把两个相同整数变成常数？答案是异或：相同整数异或得0。如何把这个性质利用到本题？如果我们异或所有得元素，则出现两次的数都相互抵消，最后留下的就是单独的那个。

## Complexity

扫描数组一次，复杂度O(n)。

## Code

```java
int singleElement(int[] arr){
	int ans = 0;
	for (int i = 0; i < arr.length; i++){
		ans ^= arr[i];
	}
	return ans;
}
```

