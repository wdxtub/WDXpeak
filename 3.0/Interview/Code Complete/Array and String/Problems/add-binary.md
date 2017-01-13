# Add Binary

出处

Given two binary strings, return their sum (also a binary string).

For example,

    a = "11"
    b = "1"
    Return "100".

## Solution

'1'-'0' = 1.

## Complexity

时间复杂度 O(n)，空间复杂度 O(1);

## Code

```java
public class Solution {
    public String addBinary(String a, String b) {
        StringBuffer res = new StringBuffer();
        int N = a.length(), M = b.length();
        int i = N - 1, j = M - 1;
        int carry = 0;
        while (i>=0 || j>=0) {
            int sum = carry;
            if (i >= 0) sum += a.charAt(i--) - '0';
            if (j >= 0) sum += b.charAt(j--) - '0';
            carry = sum / 2;
            res.insert(0,String.valueOf(sum % 2));
        }
        if (carry == 1) res.insert(0,'1');
        return res.toString();
    }
}
```

