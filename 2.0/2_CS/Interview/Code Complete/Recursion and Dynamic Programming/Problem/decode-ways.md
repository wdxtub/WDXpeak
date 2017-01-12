# Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:

    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26

Given an encoded message containing digits, determine the total number of ways to decode it.

For example,

Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2

## Solution

dp. 类似于 fibonacci 数列，但是有更多的限制条件

## Complexity

Time : O(n); Space : O(1).

## Code

```java
public class Solution {
    public int numDecodings(String s) {
        if (s.length() == 0 || s.charAt(0) == '0') return 0;
        int N = s.length();
        int f0 = 1, f1 = 1;
        for (int i = 1; i < N; ++i) {
            if (s.charAt(i) == '0') f1 = 0;
            int num = s.charAt(i) - '0' + (s.charAt(i-1) - '0') * 10;
            if (num < 10 || num > 26) {
                f0 = 0;
            }
            int tmp = f1;
            f1 = f1 + f0;
            f0 = tmp;
        }
        return f1;
    }
}
``` 

