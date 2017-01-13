# Flip Bits

出处

Write a function to determine the number of bits you would need to flip to convert integer A to integer B.

EXAMPLE

    Input: 29(11101), 15(01111)
    Output: 2

## Solution

通常情况下，当需要比较某比特位是否相同时，需要用位异或。如果A和B中某位比特不相同，则位异或得1。所以，题目等价为 A异或B，所得得结果里有几位是1。统计有几位是1可以通过反复Get lowest bit和右移1位(除2)实现。另一个常用技巧是n &= (n-1) 相当于clear最低的一位1。事实上，可以用一个哈希表在O(1)时间内得到一个整数中有多少个比特为1，具体见“工具箱”。

## Complexity

假设整型有n位，则复杂度O(n)。

## Code

```java
int bitCount(int a, int b){
	int c = a ^ b;
	int count = 0;
	while (c > 0){
		c = c & (c-1);
		count++;
	}
	return count;
}
```

