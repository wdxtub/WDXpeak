# Word Break II

Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given

    s = "catsanddog",
    dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

## Solution

check before constructing the sentences.

## Code

```java
public class Solution {
    public List<String> wordBreak(String s, Set<String> dict) {
        List<String> res = new ArrayList<String>();
        int n = s.length();
        boolean[] canBreak = new boolean[n+1];
        canBreak[n] = true;
        for (int i = n - 1; i >= 0; --i) {
            for (int j = i; j < n; ++j) {
                if (dict.contains(s.substring(i,j+1)) && canBreak[j+1]) {
                    canBreak[i] = true;
                    break;
                }
            }
        }
        if (canBreak[0] == false) return res;
        wordBreakRe(s, dict, "", 0, res);
        return res;
    }
    public void wordBreakRe(String s, Set<String> dict, String path, int start, List<String> res) {
        if (start == s.length()) {
            res.add(path);
            return;
        }
        if (path.length() != 0) path = path + " ";
        for (int i = start; i < s.length(); ++i) {
            String word = s.substring(start, i + 1);
            if (dict.contains(word) == false) continue;
            wordBreakRe(s, dict, path + word, i + 1, res);
        }
    }
}
```

