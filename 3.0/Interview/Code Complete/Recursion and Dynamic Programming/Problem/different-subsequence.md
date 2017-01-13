# Different Subsequence

给出字符串S和字符串T，计算S的不同的子序列中T出现的个数。

子序列字符串是原始字符串通过删除一些(或零个)产生的一个新的字符串，并且对剩下的字符的相对位置没有影响。(比如，“ACE”是“ABCDE”的子序列字符串,而“AEC”不是)。

样例

    给出S = "rabbbit", T = "rabbit"
    返回 3

## Solution

递归解法，首先，从个字符串S的尾部开始扫描，找到第一个和T最后一个字符相同的位置k，那么有下面两种匹配：

1. T的最后一个字符和S[k]匹配，
2. T的最后一个字符不和S[k]匹配。a相当于子问题:从S[0...lens-2]中删除几个字符得到T[0...lent-2]，b相当于子问题：从S[0...lens-2]中删除几个字符得到T[0...lent-1]。那么总的删除方法等于a、b两种情况的删除方法的和。递归解法代码如下，但是通过大数据会超时：

动态规划，设dp[i][j]是从字符串S[0...i]中删除几个字符得到字符串T[0...j]的不同的删除方法种类，有上面递归的分析可知，动态规划方程如下

+ 如果`S[i] = T[j], dp[i][j] = dp[i-1][j-1]+dp[i-1][j]`
+ 如果`S[i]` 不等于 `T[j]`, `dp[i][j] = dp[i-1][j]`

初始条件：当T为空字符串时，从任意的S删除几个字符得到T的方法为1

Consider s=”EEACC” and t=”EAC”. num[i][j] means how many distinct sequence for T[0..i-1] in S[0..j-1]

Two cases for each num[i][j]:

num[i][j] inherits from num[i][j-1]. This means overlooking s[j], t[0..i] at least keeps the number of distinct sequences in s[0..j-1]. This case finds all sequences of t[0..i] in s[o..j] without s[j].

if t[i]==s[j], this means t[i] could be mapped to s[j], we cannot overlook s[j].  We look at the number of t[0..i-1] in s[0..j-1], and add it to the result. This case finds all sequences of t[0..i] in s[o..j] with s[j].

## Complexity

时间复杂度 O(n^2 ) 空间复杂度 O(n)

## Code

解法一

```java
public class Solution {
    public int numDistinct(String S, String T) {
        int M = S.length();
        int N = T.length();
        int[] dp = new int[N+1];
        Arrays.fill(dp, 0);
        dp[0] = 1;
        for (int i = 1; i <= M; ++i) {
            for (int j = N; j >=1; --j) {
                dp[j] = dp[j] + (S.charAt(i-1) == T.charAt(j-1) ? dp[j-1] : 0);
            }
        }
        return dp[N];
    }
}
```

解法二

```java
public class Solution {
    /**
     * @param S, T: Two string.
     * @return: Count the number of distinct subsequences
     */
    public int numDistinct(String s, String t) {
        if (s==null || t==null || (s.length()==0 && t.length()!=0)) return 0;
        if (t.length()==0) return 1;
        int[] pre = new int[s.length()+1];
        Arrays.fill(pre,1);
        for (int i=1; i<=t.length(); i++){
            int[] cur = new int[s.length()+1];
            cur[0] = 0;
            for (int j=1; j<=s.length(); j++){
                if (s.charAt(j-1)==t.charAt(i-1)){
                    cur[j]+=pre[j-1];
                }
                cur[j] += cur[j-1];
            }
            System.arraycopy(cur, 0, pre, 0, cur.length);
        }
        return pre[s.length()];
    }
}

```

