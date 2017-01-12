# Swap Bits

出处 Pairwise Swap

Swap the neighboring odd and even bits in a integer (bit position as 1,2,3,…32).

## Solution

我们首先根据题意重现我们需要做的操作：

1. 我们需要get奇数位比特，根据基本操作易得需要与形如1010…10的bit mask做位与。
2. get偶数位比特，根据基本操作易得需要与形如0101…01的bit mask做位与。
3. swap意味着将1)中得到的结果右移一位，与2)中得到的结果左移一位，然后做位或操作。

由此可见，对于需要进行比特操作的题目，对题目要求进行分步，然后选择合适的bit mask，最后与给定二进制数进行基本位操作都是解题的关键。

## Complexity

复杂度 O(1)

## Code

```java
int swapBits(int input) {
    return ((0xaaaaaaaa & input) >> 1) | ((0x55555555 & input) << 1);
}
```

