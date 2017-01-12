# Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,

	Given "egg", "add", return true.
	Given "foo", "bar", return false.
	Given "paper", "title", return true.

Note:

You may assume both s and t have the same length.

## Solution

对应映射一次，看看是否满足

## Complexity

时间复杂度 O(n)，空间复杂度 O(n)

## Code

```java
public class Solution {
    boolean isIsomorphic(char[] S, char[] T) {
        char[] MAP = new char[256];
        for(int i = 0; i < S.length; i++) {
            if(MAP[(int)S[i]] == 0) {
                // not mapped
                MAP[(int)S[i]] = T[i];
            } else {
                if ( MAP[(int)S[i]] != T[i]) {
                    return false;
                }
            }
        }

        return true;
    }

    public boolean isIsomorphic(String s, String t) {

        char[] S = s.toCharArray();
        char[] T = t.toCharArray();

        if(S.length != T.length) return false;

        return isIsomorphic(S, T) && isIsomorphic(T, S);
    }
}
```

