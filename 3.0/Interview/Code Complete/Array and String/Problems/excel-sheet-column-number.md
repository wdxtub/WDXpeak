# Excel Sheet Column Number

Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 

## Solution

根据题意转换即可

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
public class Solution {
    public int titleToNumber(String s) {
        int res = 0;
        if (s.length() == 0) return 0;
        for (int i = 0; i < s.length(); ++i) {
            res = res * 26 + s.charAt(i) - 'A' + 1;
        }
        return res;
    }
}
```

