# Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.

## 方法一

一个自然数可能是:

+ 一个平方数 if and only if each prime factor occurs to an even power in the number’s prime factorization.
+ 两个平方数之和 if and only if each prime factor that’s 3 modulo 4 occurs to an even power in the number’s prime factorization.
+ 三个平方数之和 if and only if it’s not of the form 4a(8b+7) with integers a and b.
+ 四个平方数之和. Period. No condition. You never need more than four.

```java
public class Solution {
    public int numSquares(int n) {
        int m = n;
        while (m % 4 == 0)
            m /= 4;
        if (m % 8 == 7)
            return 4;
        for (int a = 0; a * a < (n / 2 + 1); a++) {
            int b = (int) Math.sqrt(n - a * a);
            if (a * a + b * b == n) {
                return 1 + ((a == 0) ? 0 : 1);
            }
        }
        return 3;
    }
}
```

## 方法二

According to the How to solve DP problems during Interview, it satisfied both conditions:

+ Minimum
+ Cannot sort / swap

Which means it can be solve by Dynamic Programming, and belongs to the One Sequence

DP Function: dp[x + y * y] = min(dp[x + y * y], dp[x] + 1)

Time Complexity: O(n * sqrt n)

我们建立一个长度为n+1的一维dp数组，将第一个值初始化为0，其余值都初始化为INT_MAX, i从0循环到n，j从1循环到`i+j*j <= n`的位置，然后每次更新`dp[i+j*j]`的值，动态更新dp数组，其中dp[i]表示正整数i最少能由多个完全平方数组成，那么我们求n，就是返回dp[n]即可，

```java
public class Solution {
    public int numSquares(int n) {
        int[] dp = new int[n + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;
        for (int i = 0; i <= n; i++) {
            for (int j = 1; i + j * j <= n; j++) {
                dp[i + j * j] = Math.min(dp[i] + 1, dp[i + j * j]);
            }
        }
        return dp[n];
    }
}
```

