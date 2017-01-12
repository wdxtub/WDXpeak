# Minimum Subarray for Sum

给定一个由 n 个整数组成的数组和一个正整数 s ，请找出该数组中满足其和 ≥ s 的最小长度子数组。如果无解，则返回 -1。

样例

    给定数组 [2,3,1,2,4,3] 和 s = 7, 子数组 [4,3] 是该条件下的最小长度子数组。

挑战

    如果你已经完成了O(n)时间复杂度的编程，请再试试 O(n log n)时间复杂度。
    
## Solution

我们需要定义两个指针left和right，分别记录子数组的左右的边界位置，然后我们让right向右移，直到子数组和大于等于给定值或者right达到数组末尾，此时我们更新最短距离，并且将left像右移一位，然后再sum中减去移去的值，然后重复上面的步骤，直到right到达末尾，且left到达临界位置，即要么到达边界，要么再往右移动，和就会小于给定值。

two pointers.当当前sum已经满足条件后，将start往后移至不满足条件的index为止，再更新结果。

## Complexity

复杂度O(n)。

## Code

```java
public class Solution {
    /**
     * @param nums: an array of integers
     * @param s: an integer
     * @return: an integer representing the minimum size of subarray
     */
    public int minimumSize(int[] nums, int s) {
        if (nums == null || nums.length == 0) {
            return -1;
        }
        int res = -1;
        int sum = 0;
        int start = 0;
        for (int end = 0; end < nums.length; end++) {
            sum += nums[end];
            if (sum >= s) {
                if (start == end) {
                    res = 1;
                    break;
                }
                while (start < end && sum - nums[start] >= s) {
                    sum -= nums[start];
                    start++;
                }
                res = res == -1 ? end - start + 1 : Math.min(res, end - start + 1);
            }
        }
        return res == -1 ? -1 : res;
    }
}

```

