# Group Anagrams List

Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

    [
      ["ate", "eat","tea"],
      ["nat","tan"],
      ["bat"]
    ]

Note:

For the return value, each inner list's elements must follow the lexicographic order.
All inputs will be in lower-case.

## Solution

Anagrams指几个string有相同的字符，但不同的字符顺序。所以一个有效的检查方法是：当两个string排序以后相同，则它们是anagrams。可以使用一个hash table，string s的key是它自己排序后的string，这样anagrams会有相同的key。用一个`vector<int>`来记录相同key的string在input `vector<string>`中的index。最后扫描一遍hash table，当有两个或以上string有相同的key时，将它们输出到结果。


## Complexity

时间复杂度 O(n)，空间复杂度 O(n)

## Code

```java
public class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> rst = new ArrayList<List<String>>();
        HashMap<String, List<String>> map = new HashMap<String, List<String>>();
        Arrays.sort(strs);

        for(int i = 0; i < strs.length; i++) {
            char[] strChar = strs[i].toCharArray();
            Arrays.sort(strChar);
            String str = new String(strChar);
            if(map.containsKey(str)) {
                map.get(str).add(strs[i]);
            }
            else {
                List<String> list = new ArrayList<String>();
                list.add(strs[i]);
                map.put(str, list);
            }
        }

        for(List<String> val : map.values()) {
            rst.add(val);
        }

        return rst;
    }
    
    String sortChars(String s){
        char[] content = sortChars.toCharArray();
        Arrays.sort(content);
        return new String(content);
    }
}
```

