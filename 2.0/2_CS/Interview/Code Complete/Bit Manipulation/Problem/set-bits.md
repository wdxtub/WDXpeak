# Set Bits

出处 Insertion

Given N and M, 32bit integers, how to set i to j bits (bit position as 1,2,3,…32) of N as the value of bits in M.

For example, N = 00000000000000000000000001111011,

M = 00000000001000000011000000011000, i = 10, j = 20, then the result should be:

00000000001000000011000001111011

## Solution

我们首先根据题意重现我们需要做的操作：

1. 我们需要从M中get第i到第j个比特 
2. 我们需要clear N中第i到第j个比特 
3. 我们需要set N中第i到第j个比特。

对于1)，根据基本操作，get bit需要&1，所以与M进行操作的bit mask在第i到第j位应当为1，其他位为0。对于2)， 根据基本操作，clear bit需要&0，所以与N进行操作的位掩码在第i到第j位应当为0，其他位为1。注意，这个位掩码刚好是前一项操作位掩码的位反运算。对于3)，我们只需要将1)，2)的操作结果进行位或即可。构造所需位掩码的过程如前所述，对~0进行基本操作和加减法即可。

题意简单来讲就是使用 M 代替 N 中的第i位到第j位。很显然，我们需要借用掩码操作。大致步骤如下：

1. 得到第i位到第j位的比特位为0，而其他位均为1的掩码mask。
2. 使用mask与 N 进行按位与，清零 N 的第i位到第j位。
3. 对 M 右移i位，将 M 放到 N 中指定的位置。
4. 返回 N | M 按位或的结果。

获得掩码mask的过程可参考 CTCI 书中的方法，先获得掩码(1111...000...111)的左边部分，然后获得掩码的右半部分，最后左右按位或即为最终结果。

在给定测试数据[-521,0,31,31]时出现了 WA, 也就意味着目前这段程序是存在 bug 的，此时m = 0, i = 31, j = 31，仔细瞅瞅到底是哪几行代码有问题？本地调试后发现问题出在left那一行，left移位后仍然为ones, 这是为什么呢？在j为31时j + 1为32，也就是说此时对left位移的操作已经超出了此时int的最大位宽！

使用~0获得全1比特位，在j == 31时做特殊处理，即不必求left。求掩码的右侧1时使用了(1 << i) - 1, 题中有保证第i位到第j位足以容纳 M, 故不必做溢出处理。

## Complexity

复杂度 O(1)

## Code

```java
final int BITS_COUNT = 32;
int setBits(int m, int n, int i, int j){
	int max = ~0;
	int mask = (max << BITS_COUNT - i) | (max >> j);
	return (m & mask) | (n & ~mask)
}
```

