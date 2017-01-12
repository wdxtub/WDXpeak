# Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.

## Solution

计算 5 出现的次数即可

## Code

```java
public class Solution {
    public int trailingZeroes_1(int n) {
        int res = 0;
        while (n != 0) {
            res += n / 5;
            n = n / 5;
        }
        return res;
    }
    public int trailingZeroes_2(int n) {
        if (n == 0) return 0;
        return n / 5 + trailingZeroes_2(n / 5);
    }
}
```

