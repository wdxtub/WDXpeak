# Scramble String

Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

        great
       /    \
      gr    eat
     / \    /  \
    g   r  e   at
               / \
              a   t

To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

        rgeat
       /    \
      rg    eat
     / \    /  \
    r   g  e   at
               / \
              a   t

We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

        rgtae
       /    \
      rg    tae
     / \    /  \
    r   g  ta  e
           / \
          t   a

We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

## Solution

1. Recursion + pruning.
2. 3-dimensional dp.
    + `dp[k][i][j] == true` means string s1(start from i, length k) is a scrambled string of string s2(start from j, length k).

## Code

```java
public class Solution {
    public boolean isScramble_1(String s1, String s2) {
        if (s1.compareTo(s2) == 0) return true;
        if (s1.length() != s2.length()) return false;
        return isScrambleRe(s1, s2);
    }
    public boolean isScrambleRe(String s1, String s2) {
        if (hasSameLetters(s1, s2) == false) return false;
        int len = s1.length();
        if (len == 0 || len == 1) return true;
        for (int i = 1; i < len; ++i) {
            if (isScrambleRe(s1.substring(0,i), s2.substring(0,i)) 
                && isScrambleRe(s1.substring(i), s2.substring(i)) 
                || isScrambleRe(s1.substring(0,i), s2.substring(len-i)) 
                && isScrambleRe(s1.substring(i), s2.substring(0,len-i))) {
                    return true;
                }
        }
        return false;
    }
    public boolean hasSameLetters(String s1, String s2) {
        if (s1.compareTo(s2) == 0) return true;
        if (s1.length() != s2.length()) return false;
        int[] count = new int[256];
        for (int i = 0; i < s1.length(); ++i) count[(int)s1.charAt(i)]++;
        for (int i = 0; i < s2.length(); ++i) count[(int)s2.charAt(i)]--;
        for (int i = 0; i < 256; ++i)
            if (count[i] != 0) return false;
        return true;
    }
    
    
    public boolean isScramble(String s1, String s2) {
        if (s1.compareTo(s2) == 0) return true;
        if (s1.length() != s2.length()) return false;
        int N = s1.length();
        boolean[][][] dp = new boolean[N+1][N][N];
        for (int k = 1; k <= N; ++k) {
            for (int i = 0; i <= N - k; ++i) {
                for (int j = 0; j <= N - k; ++j) {
                    dp[k][i][j] = false;
                    if (k == 1) dp[1][i][j] = (s1.charAt(i) == s2.charAt(j));
                    for (int p = 1; p < k && !dp[k][i][j]; ++p) {
                        if (dp[p][i][j] && dp[k-p][i+p][j+p] || dp[p][i][j+k-p] && dp[k-p][i+p][j])
                            dp[k][i][j] = true;
                    }
                }
            }
        }
        return dp[N][0][0];
    }
}
```

