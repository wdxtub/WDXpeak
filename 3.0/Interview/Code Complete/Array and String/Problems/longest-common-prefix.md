# Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

## Solution

正常查找即可

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
public class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) return new String("");
        for(int i = 0;i < strs[0].length(); ++i){
            for(int j = 1;j < strs.length; ++j){
                if(i >= strs[j].length() || 
                    strs[j].charAt(i) != strs[0].charAt(i)) 
                    return strs[0].substring(0,i);
            }
        }
        return strs[0];
    }
}
```

