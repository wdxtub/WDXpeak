# Find Anagram

出处

给出一个字符串数组S，找到其中所有的乱序字符串(Anagram)。如果一个字符串是乱序字符串，那么他存在一个字母集合相同，但顺序不同的字符串也在S中。

样例

    对于字符串数组 ["lint","intl","inlt","code"]
    返回 ["lint","inlt","intl"]

注意

    所有的字符串都只包含小写字母

## Solution

在题 Two Strings Are Anagrams 中曾介绍过使用排序和 hashmap 两种方法判断变位词。这里我们将这两种方法同时引入！只不过此时的 hashmap 的 key 为字符串，value 为该字符串在 vector 中出现的次数。两次遍历字符串数组，第一次遍历求得排序后的字符串数量，第二次遍历将排序后相同的字符串取出放入最终结果中。

## Complexity

时间复杂度 O(n)，空间复杂度 O(n)

## Code

```java
public class Solution {
    /**
     * @param strs: A list of strings
     * @return: A list of strings
     */
    public List<String> anagrams(String[] strs) {
        List<String> ret = new ArrayList<String>();

        if (strs == null) {
            return ret;
        }

        HashMap<String, List<String>> map = new HashMap<String, List<String>>();

        int len = strs.length;
        for (int i = 0; i < len; i++) {
            String s = strs[i];

            // Sort the string.
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String strSort = new String(chars);

            // Create a ArrayList for the sorted string.
            if (!map.containsKey(strSort)) {
                map.put(strSort, new ArrayList<String>());
            }

            // Add a new string to the list of the hashmap.
            map.get(strSort).add(s);
        }

        // go through the map and add all the strings into the result.
        for (Map.Entry<String, List<String>> entry: map.entrySet()) {
            List<String> list = entry.getValue();

            // skip the entries which only have one string.
            if (list.size() == 1) {
                continue;
            }

            // add the strings into the list.
            ret.addAll(list);
        }

        return ret;
    }
}

```

