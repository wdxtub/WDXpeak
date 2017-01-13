# Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

## Solution

Pay attention when moving the 'start' pointer forward.

## Complexity

时间复杂度 O(n)，空间复杂度 O(n)

## Code

```
public class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s == null || s.length() < 1) return 0;
        int len = s.length();
        int maxCount = 0;
        int curStart = -1;
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        for (int i = 0; i < len ;i++){
            if (map.containsKey(s.charAt(i))){
                curStart = Math.max(curStart,map.get(s.charAt(i)));
            }
            map.put(s.charAt(i),i);
            maxCount = Math.max(maxCount, i-curStart);
        }
        
        return maxCount;
    }
}
```

---

Reference

```java
public class Solution {
    public int lengthOfLongestSubstring(String s) {
        boolean[] hash = new boolean[256];
        Arrays.fill(hash,false);
        int n = s.length();
        if (n <= 1) return n;
        int start = 0, end = 0, res = 0;
        while (end < n && start + res < n) {
            if (hash[s.charAt(end)] == false) {
                hash[s.charAt(end++)] = true;
            } else {
                hash[s.charAt(start++)] = false;
            }
            res = Math.max(res, end - start);
        }
        return res;
    }
}
```

