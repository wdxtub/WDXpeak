# Divide Number

将两个整数相除，要求不使用乘法、除法和 mod 运算符。

如果溢出，返回 2147483647 。

样例

    给定被除数 = 100 ，除数 = 9，返回 11。

## Solution

不断用减法即可

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
public class Solution {
    /**
     * @param dividend the dividend
     * @param divisor the divisor
     * @return the result
     */
    public int divide(int dividend, int divisor) {
        if (divisor == 0) {
             return dividend >= 0? Integer.MAX_VALUE : Integer.MIN_VALUE;
        }

        if (dividend == 0) {
            return 0;
        }

        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }

        boolean isNegative = (dividend < 0 && divisor > 0) ||
                             (dividend > 0 && divisor < 0);

        long a = Math.abs((long)dividend);
        long b = Math.abs((long)divisor);
        int result = 0;
        while(a >= b){
            a -= b;
            result++;
        }
        return isNegative? -result: result;
    }
}
```

