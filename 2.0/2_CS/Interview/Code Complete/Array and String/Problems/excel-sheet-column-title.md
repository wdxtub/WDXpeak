# Excel Sheet Column Title

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 

## Solution

根据题意进行转化即可

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code 

```java
public class Solution {
    public String convertToTitle(int n) {
        StringBuffer sb = new StringBuffer();
        while (n > 0) {
            sb.insert(0,(char)((n - 1)%26 + 'A'));
            n  = (n - 1) / 26;
        }
        return sb.toString();
    }
}
```

