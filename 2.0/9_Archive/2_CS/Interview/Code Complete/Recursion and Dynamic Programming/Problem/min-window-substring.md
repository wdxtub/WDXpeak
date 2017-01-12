# Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,

    S = "ADOBECODEBANC"
    T = "ABC"

Minimum window is "BANC".

Note:

If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

## Solution & Complexity

1. Use two pointers: start and end. First, move 'end'. After finding all the needed characters, move 'start'. O(n)
2. Use array as hashtable.

## Code

```java
public class Solution {
    public String minWindow(String S, String T) {
        int N = S.length(), M = T.length();
        if (N < M) return new String("");
        int[] need = new int[256];
        int[] find = new int[256];
        for (int i = 0; i < M; ++i)
            need[T.charAt(i)]++;

        int count = 0, resStart = -1, resEnd = N;
        for (int start = 0, end = 0; end < N; ++end)
        {
            if (need[S.charAt(end)] == 0)
                continue;
            if (find[S.charAt(end)] < need[S.charAt(end)])
                count++;
            find[S.charAt(end)]++;
            if (count != M) continue;
            // move 'start'
            for (; start < end; ++start) {
                if (need[S.charAt(start)] == 0) continue;
                if (find[S.charAt(start)] <= need[S.charAt(start)]) break;
                find[S.charAt(start)]--;
            }
            // update result
            if (end - start < resEnd - resStart) {
                resStart = start;
                resEnd = end;
            }
        }
        return (resStart == -1) ? new String("") : S.substring(resStart, resEnd + 1); 
    }
}
```

