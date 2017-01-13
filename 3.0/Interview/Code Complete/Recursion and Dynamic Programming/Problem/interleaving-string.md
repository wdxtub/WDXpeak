# Interleaving String

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

For example,

    Given:
    s1 = "aabcc",
    s2 = "dbbca",

    When s3 = "aadbbcbcac", return true.
    When s3 = "aadbbbaccc", return false.

## Solution

这是一道关于字符串操作的题目，要求是判断一个字符串能不能由两个字符串按照他们自己的顺序，每次挑取两个串中的一个字符来构造出来。

像这种判断能否按照某种规则来完成求是否或者某个量的题目，很容易会想到用动态规划来实现。

动态规划重点在于找到：维护量，递推式。维护量通过递推式递推，最后往往能得到想要的结果

先说说维护量，`res[i][j]`表示用`s1`的前`i`个字符和`s2`的前`j`个字符能不能按照规则表示出`s3`的前`i+j`个字符，如此最后结果就是`res[s1.length()][s2.length()]`，判断是否为真即可。接下来就是递推式了，假设知道`res[i][j]`之前的所有历史信息，我们怎么得到`res[i][j]`。可以看出，其实只有两种方式来递推，一种是选取`s1`的字符作为`s3`新加进来的字符，另一种是选`s2`的字符作为新进字符。而要看看能不能选取，就是判断`s1(s2)`的第`i(j)`个字符是否与`s3`的`i+j`个字符相等。如果可以选取并且对应的`res[i-1][j](res[i][j-1])`也为真，就说明`s3`的`i+j`个字符可以被表示。这两种情况只要有一种成立，就说明`res[i][j]`为真，是一个或的关系。所以递推式可以表示成

    res[i][j] = res[i-1][j] && s1.charAt(i-1)==s3.charAt(i+j-1) || 
                res[i][j-1] && s2.charAt(j-1)==s3.charAt(i+j-1)
 
## Complexity

dp. O(MN) time & space.

## Code

```java
public class Solution {
    public boolean isInterleave_1(String s1, String s2, String s3) {
        int l1 = s1.length(), l2 = s2.length(), l3 = s3.length();
        if (l1 == 0) return s2.compareTo(s3) == 0;
        if (l2 == 0) return s1.compareTo(s3) == 0;
        if (l1 + l2 != l3) return false;
        boolean[][] dp = new boolean[l1+1][l2+1];
        dp[0][0] = true;
        for (int i = 1; i <= l1; ++i) {
            dp[i][0] = dp[i-1][0] && (s1.charAt(i-1) == s3.charAt(i-1));
        }
        for (int j = 1; j <= l2; ++j) {
            dp[0][j] = dp[0][j-1] && (s2.charAt(j-1) == s3.charAt(j-1));
        }
        for (int i = 1; i <= l1; ++i) {
            for (int j = 1; j <= l2; ++j) {
                if (s1.charAt(i - 1) == s3.charAt(i+j-1)) dp[i][j] = dp[i-1][j];
                if (s2.charAt(j - 1) == s3.charAt(i+j-1)) dp[i][j] = dp[i][j] | dp[i][j-1];
            }
        }
        return dp[l1][l2];
    }
    
    public boolean isInterleave(String s1, String s2, String s3) {
        int l1 = s1.length(), l2 = s2.length(), l3 = s3.length();
        if (l1 == 0) return s2.compareTo(s3) == 0;
        if (l2 == 0) return s1.compareTo(s3) == 0;
        if (l1 + l2 != l3) return false;
        boolean[] dp = new boolean[l2+1];
        dp[0] = true;
        for (int j = 1; j <= l2; ++j) {
            dp[j] = dp[j-1] && (s2.charAt(j-1) == s3.charAt(j-1));
        }
        for (int i = 1; i <= l1; ++i) {
            dp[0] = dp[0] && (s1.charAt(i-1) == s3.charAt(i-1));
            for (int j = 1; j <= l2; ++j) {
                boolean before = dp[j]; dp[j] = false;
                if (s1.charAt(i - 1) == s3.charAt(i+j-1)) dp[j] = before;
                if (s2.charAt(j - 1) == s3.charAt(i+j-1)) dp[j] = dp[j] | dp[j-1];
            }
        }
        return dp[l2];
    }
} 
```

