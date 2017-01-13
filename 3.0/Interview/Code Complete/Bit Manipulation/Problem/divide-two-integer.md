# Divide Two Integers

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.

## Solution

Use << operator.

直观的方法是，用被除数逐个的减去除数，直到被除数小于0。这样做会超时。

那么如果每次不仅仅减去1个除数，计算速度就会增加，但是题目不能使用乘法，因此不能减去`k*除数`，我们可以对除数进行左移位操作，这样每次相当于减去2^k个除数，如何确定k呢，只要使 `(2^k)*除数 <=  当前被除数 <(2^(k+1))*除数`.

## Complexity

时间复杂度 O(logn)，空间复杂度 O(1)

## Code

```java
public class Solution {
    public int divide(int dividend, int divisor) {
        boolean flag = dividend < 0 ^ divisor < 0;
        long Dividend = Math.abs((long)dividend);
        long Divisor = Math.abs((long)divisor);
        long res = 0;
        while (Dividend >= Divisor) {
            long c = Divisor;
            for (int i = 0; (c << i) <= Dividend; ++i) {
                Dividend -= (c << i);
                res += (1 << i);
            }
        }
        if (flag == true) res = -res;
        if (res > Integer.MAX_VALUE) return Integer.MAX_VALUE;
        return (int)res;
    }
}
```

