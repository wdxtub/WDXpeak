# Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",

Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

## Solution

整体的思路是一维DP。DP[i]表示长度为i的prefix：s[0: i-1]的min cut数量。
DP[i] = min (DP[j] + 1) ，对所有 0<=j<i，且s[j: i-1]为palindrome。
和I同样的技巧，用DP先计算存储一个palindrome判断矩阵isPal[i][j]，便于后面一维DP计算中能迅速判断s[j: i-1]是否为palindrome。

## Complexity

时间复杂度 O(n^2 )，空间复杂度 O(n^2 )

## Code

```java
public class Solution {
    public int minCut(String s) {
        int n = s.length();
        int[] dp = new int[n+1];
        dp[n] = -1;
        boolean[][] isP = new boolean[n][n];
        for (int i = n - 1; i >= 0; --i) {
            dp[i] = n - 1 - i;
            for (int j = i; j < n; ++j) {
                if (s.charAt(i) == s.charAt(j) && (j < i + 2 || isP[i+1][j-1])) isP[i][j] = true;
                if (isP[i][j] == true) {
                    dp[i] = Math.min(dp[i], 1 + dp[j+1]);
                }
            }
        }
        return dp[0];
    }
}
```

