# !!Substring with Concatenation of All Words

You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

For example, given:

s: "barfoothefoobarman"

words: ["foo", "bar"]

You should return the indices: [0,9].

(order does not matter).

## Solution

1. Brute + HashMap.
2. Sliding Window + HashMap. from Sun Mian.

## Code

```java
public class Solution {
    public List<Integer> findSubstring(String S, String[] L) {
        List<Integer> res = new ArrayList<Integer>();
        if(L.length==0 || S==null || S.length()==0) return res;
        int M = S.length(), N = L.length;
        int K = L[0].length();
        HashMap<String, Integer> need = new HashMap<String, Integer>();
        for(String str: L) {
            if(need.containsKey(str)) {
                need.put(str, need.get(str)+1);
            } else {
                need.put(str, 1);
            }
        }
        for (int i = 0; i <= M - N*K; ++i) {
            HashMap<String, Integer> found = new HashMap<String, Integer>();
            int j = 0;
            for (j = 0; j < N; ++j) {
                String s = S.substring(i + j * K, i + (j+1) * K);
                if (need.containsKey(s) == false) break;
                if (found.containsKey(s) == true) {
                    if (need.get(s) <= found.get(s)) break;
                    found.put(s, found.get(s)+1);
                } else found.put(s, 1);
            }
            if (j == N) res.add(i);
        }
        return res;
    }
    
    
    public List<Integer> findSubstring_2(String S, String[] L) {
        List<Integer> list = new ArrayList<>();
        Map<String, Integer> need = new HashMap<>();
        for(String str: L) {
            if(need.containsKey(str)) {
                need.put(str, need.get(str)+1);
            } else {
                need.put(str, 1);
            }
        }
        int n = L[0].length(), m = L.length;
        for (int i = 0; i < n; ++i) {
            Map<String, Integer> find = new HashMap<>();
            for (int start = i, end = i, count = 0; end + n <= S.length(); end += n) {
                String str = S.substring(end, end + n);
                if (need.get(str) == null) {
                    start = end + n;
                    find.clear();
                    count = 0;
                    continue;
                }
                while (find.get(str) != null && find.get(str) >= need.get(str)) {
                    String subStart = S.substring(start, start + n);
                    find.put(subStart, find.get(subStart) - 1);
                    start += n;
                    --count;
                }
                find.put(str, (find.get(str) == null ? 0 : find.get(str)) + 1);
                ++count;
                if (count != m) continue;
                list.add(start);
            }
        }
        return list;
    }
}
```

