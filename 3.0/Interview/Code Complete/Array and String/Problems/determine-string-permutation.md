# Determine String Permutation

出处

Given two strings, determine if they are permutations of each other.

## Solution

对于这道题目，我们需要找到两个字符串之间的共同点，即通过某种映射，使得所有置换得到相同的结果。 考虑到置换的特性：无论如何变化，每个字符出现的次数一定相同。一旦需要统计一个元素集中元素出现的次数，我们就应该想到哈希表。于是，对于每个字符串，我们通过统计每个字符出现的次数把string映射成一个哈希表，最后比较两个哈希表是否相同。事实上，这种所谓的映射，其本身也是一个哈希的过程 (只不过哈希的结果是一个哈希表)：我们可以根据哈希的结果判断一个字符串集合中有多少字符串属于同一个置换。针对这道题目，我们还可以利用一些小技巧提前进行快速判断：如果两个字符串的长度不同，那它们一定不是一个置换。

## Complexity

哈希表需要扫描整个字符串，每次插入操作时间复杂度O(1)，假设字符串的长度为n，则平均时间复杂度都是O(n)。最后比较两个hash是否相同，每个合法字符都有可能出现，假设字符集大小为m，则需要的时间复杂度是O(m)，故总的时间复杂度O(m+n)。空间上，平均空间是O(m)。

## Code

```java
boolean isPermutation(String s1, String s2){
	if (s1.length() != s2.length()){
		return false;
	}
	if (s1 == null || s2 == null){
		return false;
	}
	
	HashMap<Character, Integer> map1 = new HashMap<Character, Integer>();
	HashMap<Character, Integer> map2 = new HashMap<Character, Integer>();
	
	for (int i = 0; i < s1.length(); i++){
		if (map1.containsKey(s1.charAt(i)){
			map1.put(s1.charAt(i), map1.get(s1.charAt(i)) + 1);
		} else {
			map1.put(s1.charAt(i), map1.get(s1.charAt(i)) + 1);
		}
	}
	
	for (int i = 0; i < s2.length(); i++){
		if (map2.containsKey(s2.charAt(i)){
			map2.put(s2.charAt(i), map1.get(s2.charAt(i)) + 1);
		} else {
			map2.put(s2.charAt(i), 1);
		}
	}
	
	if(map1.size() != map2.size()){
		return false;
	}
	
	Iterator iter = map1.entrySet().iterator();
	while(iter.hasNext()){
		Map.Entry entry = (Map.Entry) iter.next();
		if ((Integer) entry.getValue() != map2.get((Character)entry.getKey())){
			return false;
		}
	}
	return true;
}
```


