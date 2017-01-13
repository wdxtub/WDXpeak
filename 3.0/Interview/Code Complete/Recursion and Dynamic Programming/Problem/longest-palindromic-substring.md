# Longest Palindromic Substring

Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

## Solution & Complexity

1. Time O(n^2), Space O(n^2)
2. Time O(n^2), Space O(n)
3. Time O(n^2), Space O(1) (actually much more efficient than 1 & 2) 两头扩张
4. Time O(n), Space O(n) (Manacher's Algorithm)
5. Time O(n), Smaller Space than solution 4. (Manacher's Algorithm)

## Code

```java
public class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.length() <= 1) return s;
        int len = s.length();
        int index = 0, maxlen = 0;
        for (int i = 0; i < len; i++){
            for (int j = 0; j < 2; j++){
                boolean isP = true;
                for (int k = 0; i - k >= 0 && i + j + k < len && isP; k++){
                    isP = (s.charAt(i-k) == s.charAt(i+j+k));
                    if (isP && j+1+k*2 > maxlen) {
                        maxlen = j+1+k*2;
                        index = i-k;
                    }
                }
            }
        }
        return s.substring(index, index+maxlen);
    }
}
```

---

Reference

```java
public class Solution {
    public String longestPalindrome_1(String s) {
        int n = s.length();
        boolean[][] dp = new boolean[n][n];
        int idx = 0, maxLen = 0;
        for (int k = 0; k < n; ++k) {
            for (int i = 0; i + k < n; ++i) {
                if (k == 0 || k == 1) 
                    dp[i][i+k] = (s.charAt(i) == s.charAt(i+k));
                else 
                    dp[i][i+k] = 
                    (s.charAt(i) == s.charAt(i+k)) ? dp[i+1][i+k-1] : false;
                if (dp[i][i+k] == true && (k+1) > maxLen) {
                    idx = i; maxLen = k + 1;
                }
            }
        }
        return s.substring(idx, idx + maxLen);
    }
    
    public String longestPalindrome_2(String s) {
        int n = s.length();
        boolean[][] dp = new boolean[2][n];
        int idx = 0, maxLen = 0;
        int cur = 1, last = 0;
        for (int i = 0; i < n; ++i) {
            cur = cur + last - (last = cur);
            for (int j = i; j >=0; --j) {
                if (j == i || j == i - 1)
                    dp[cur][j] = (s.charAt(i) == s.charAt(j));
                else 
                    dp[cur][j] = (s.charAt(i) == s.charAt(j)) && dp[last][j + 1];
                if (dp[cur][j] && (i - j + 1) > maxLen) {
                    idx = j; maxLen = i - j + 1;
                }
            }
        }
        return s.substring(idx, idx + maxLen);
    }
    
    public String longestPalindrome_3(String s) {
        int n = s.length();
        int idx = 0, maxLen = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j <= 1; ++j) {
                boolean isP = true;
                for (int k = 0; i - k >= 0 && i + j + k < n && isP; ++k) {
                    isP = (s.charAt(i - k) == s.charAt(i + j + k));
                    if (isP && (j + 1 + k*2) > maxLen) {
                        idx = i - k; maxLen = j + 1 + k*2;
                    }
                }
            }
        }
        return s.substring(idx, idx + maxLen);
    }
    
    public String longestPalindrome_4(String s) {
        int n = s.length();
        int idx = 0, maxLen = 0;
        StringBuffer sb = new StringBuffer();
        sb.append('^');
        for (int i = 0; i < n; ++i) {
            sb.append('#');
            sb.append(s.charAt(i));
        }
        sb.append("#$");
        n = 2 * n + 3;
        int mx = 0, id = 0;
        int[] p = new int[n];
        Arrays.fill(p,0);
        for (int i = 1; i < n - 1; ++i) {
            p[i] = (mx > i) ? Math.min(p[2 * id - i], mx - i) : 0;
            while (sb.charAt(i + 1 + p[i]) == sb.charAt(i - 1 - p[i])) ++p[i];
            if (i + p[i] > mx) {
                id = i; mx = i + p[i];
            }
            if (p[i] > maxLen) {
                idx = i; maxLen = p[i];
            }
        }
        idx = (idx - maxLen - 1) / 2;
        return s.substring(idx, idx + maxLen);
    }
    
    public String longestPalindrome_5(String s) {
        int n = s.length();
        int idx = 0, maxLen = 0;
        int mx = 0, id = 0;
        int[] p = new int[2*n+1];
        Arrays.fill(p,0);
        for (int i = 0; i < 2*n+1; ++i) {
            p[i] = (mx > i) ? Math.min(p[2*id-i], mx - i) : 0;
            int left = i - 1 - p[i],  right = i + 1 + p[i];
            while (left>=0 && right <= 2*n) {
                if (left % 2 == 0 || s.charAt(left/2) == s.charAt(right/2)) {
                    ++p[i];
                } else break;
                --left;
                ++right;
            }
            if (i + p[i] > mx) {
                id = i; mx = i + p[i];
            }
            if (p[i] > maxLen) {
                idx = i; maxLen = p[i];
            }
        }
        idx = (idx - maxLen) / 2;
        return s.substring(idx, idx + maxLen);
    }
}
```



