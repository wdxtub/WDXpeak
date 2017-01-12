# Bitwise AND of Numbers Range

出处

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

For example, given the range [5, 7], you should return 4.

## Solution

我连题目都看不懂

## Complexity

## Code

```java
public class Solution {
    static final int SIZE = Integer.SIZE;

    static final long[] POW = new long[SIZE + 1];

    static {
        for(int i = 0; i < SIZE; i++){
            POW[i] = (long)Math.pow(2, i);
        }        
    }
    
    public int rangeBitwiseAnd(int m, int n) {

        for(int i = SIZE; i > 0; i--){
            if(POW[i - 1] <= m && m < POW[i]){
                if(POW[i - 1] <= n && n < POW[i]){
                    long p = POW[i - 1];
                    return (int)p | rangeBitwiseAnd((int)(m & (p - 1)), (int)(n & (p - 1)));
                }
            }
        }

        return 0;
    }
}
```

