# Palindrome Number

Determine whether an integer is a palindrome. Do this without extra space.

Some hints:

Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.

## Solution

1. Count the number of digits first (traverse once) then check the digits from both sides to center.
2. Reverse the number, then check to see if x == reverse(x).
3. Recursion (interesting but a little hard to understand). -> See C++.

除以 10 是去掉最低位

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
public class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) return false;
        int d = 1;
        while (x / d >= 10) d *= 10;
        while (d > 1) {
            if (x % 10 != x / d) return false;
            x = (x % d) / 10;
            d /= 100;
        }
        return true;
    }
}
```

