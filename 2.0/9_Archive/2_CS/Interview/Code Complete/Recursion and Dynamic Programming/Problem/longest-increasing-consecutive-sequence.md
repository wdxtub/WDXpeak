# Longest Increasing Consecutive Sequence

给定一个整数数组（下标从 0 到 n-1， n 表示整个数组的规模），请找出该数组中的最长上升连续子序列。（最长上升连续子序列可以定义为从右到左或从左到右的序列。）

样例

    给定 [5, 4, 2, 1, 3], 其最长上升连续子序列（LICS）为 [5, 4, 2, 1], 返回 4.
    给定 [5, 1, 2, 3, 4], 其最长上升连续子序列（LICS）为 [1, 2, 3, 4], 返回 4.

## Solution

题目只要返回最大长度，注意此题中的连续递增指的是双向的，即可递增也可递减。简单点考虑可分两种情况，一种递增，另一种递减，跟踪最大递增长度，最后返回即可。也可以在一个 for 循环中搞定，只不过需要增加一布尔变量判断之前是递增还是递减。

## Code

```java
public class Solution {
    /**
     * @param A an array of Integer
     * @return  an integer
     */
    public int longestIncreasingContinuousSubsequence(int[] A) {
        if (A == null || A.length == 0) return 0;

        int start = 0, licsMax = 1;
        boolean ascending = false;
        for (int i = 1; i < A.length; i++) {
            // ascending order
            if (A[i - 1] < A[i]) {
                if (!ascending) {
                    ascending = true;
                    start = i - 1;
                }
            } else if (A[i - 1] > A[i]) {
            // descending order
                if (ascending) {
                    ascending = false;
                    start = i - 1;
                }
            } else {
                start = i - 1;
            }
            licsMax = Math.max(licsMax, i - start + 1);
        }

        return licsMax;
    }
}

```

