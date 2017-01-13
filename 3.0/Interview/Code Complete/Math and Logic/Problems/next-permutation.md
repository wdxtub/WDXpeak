# Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1
    
## Solution

Take A = {1,3,2} as an example:

1. Traverse from back to forth, find the turning point, that is A[i] = 3.
2. Sort from the turning point to the end (A[i] to A[end]), so {3,2} becomes {2,3}.
3. If i equals to 0, finish! Else, goto 4.
4. Let j = i, search from A[j] to A[end] to find the first elem which is larger than A[i-1], '2' here.
5. Swap the elem A[j] with A[i-1].

Finally, the next permutation is {2,1,3}.

关于字典序的理解：

a[0], a[1]...a[n-1] 的下一个排列是字典序比它大的最小的一个。

找到尽可能大的 m，b[0] = a[0], b[1] = a[1]....b[m-1] = a[m-1]，而 b[m] > a[m], b[m+1...n-1] 是按照升序(不减序)排列的.

+ 目前的排列是：`(A)a[x](B)`
+ 下一个排列是：`(A)a[y](B')`
    + A 是相同的，A 尽可能长
    + a[y] > a[x]
    + B' 几乎是 B 里面的数排好顺序的结果
+ 如何确定 x？
    + 一个位置只要右边有数比它大就是候选的 x
    + a[x] 是最后一个这样的数(最右边)
        + a[x] 右边的数，每个数的右边(后缀)没有比它大的
        + 所以 a[x] 右边的数是按照降序(不升序) 排列的


算法(二找、一交换、一翻转)

+ 找到最后一个严格升序的首位 (a[i] < a[i+1])，定义为 x
    + （A）= a[0...x-1] (B) = a[x+1...n-1]
+ 找到 y > x, a[y] > a[x],且 a[y] 最小(从右往前左找的第一个)
    + 一定存在，因为 x+1 就是一个候选
    + a[x] 后面的数都是降序，所以从后往前找到第一个大于 a[x] 的位置就是 y
+ 交换 a[x], a[y]
+ 对(x+1) 位后进行逆转
    + 交换后 a[x+1...n-1] 仍然是降序(不升)
    + 逆转等于排序

### Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
public class Solution {
    public void nextPermutation(int[] num) {
        int last = num.length - 1;
        int i = last;
        while (i >0 && num[i - 1] >= num [i]) --i;
        if (i == 0) {
            for (int l = 0, r = last; l < r; ++l, --r) {
                int tmp = num[l];
                num[l] = num[r];
                num[r] = tmp;
            }
            return;
        }
        for (int j = last; j >= i; --j) {
            if (num[j] > num[i-1]) {
                int tmp = num[j];
                num[j] = num[i-1];
                num[i-1] = tmp;
                for (int l = i, r = last; l < r; ++l, --r) {
                    int t = num[l];
                    num[l] = num[r];
                    num[r] = t;
                }
                return;
            }
        }
    }
}
```

