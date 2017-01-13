# Wildcard Matching

Implement wildcard pattern matching with support for '?' and '*'.

    '?' Matches any single character.
    '*' Matches any sequence of characters (including the empty sequence).
    
    The matching should cover the entire input string (not partial).
    
    The function prototype should be:
    bool isMatch(const char *s, const char *p)
    
    Some examples:
    isMatch("aa","a") → false
    isMatch("aa","aa") → true
    isMatch("aaa","aa") → false
    isMatch("aa", "*") → true
    isMatch("aa", "a*") → true
    isMatch("ab", "?*") → true
    isMatch("aab", "c*a*b") → false

## Solution

if s[i]  == p[j] || p[j] == '?', ++i and ++j.

ii, jj, record the positon of '*' in s and p, ++j and go on.

if not match, go back to star, i = ++ii;

## Code

```java
public class Solution {
    public boolean isMatch(String s, String p) {
        int ii = -1, jj = -1, i = 0, j = 0;
        while (i < s.length()) {
            if (j < p.length() && p.charAt(j) == '*') {
                while (j < p.length() && p.charAt(j) == '*') ++j;
                if (j == p.length()) return true;
                ii = i;
                jj = j;
            }
            if (j < p.length() && (p.charAt(j) == '?' || p.charAt(j) == s.charAt(i))) {
                ++i; ++j;
            } else {
                if (ii == -1) return false;
                ++ii;
                i = ii;
                j = jj;
            }
        }
        while (j < p.length() && p.charAt(j) == '*') ++j;
        return i == s.length() && j == p.length();
    }
}
```

