# Unique Character

出处：

Determine if all characters of a string are unique.

## Solution

这道题的关键在于“unique”。一般来说，一旦出现“unique”，就落入使用哈希表或者bitset来判断元素出现与否的范畴。进一步地，考虑如何建立键-值对：如果运用哈希表，我们可以直接用字符作为键，出现的次数作为值。特别地，由于“unique”只需要判断哈希表中是否已经存在当前键，所以我们可以通过insert函数的返回值作出相应的判断。

如果运用bitset，我们需要建立字符到整数下标的映射关系。通常，字符都是255个ASCII编码之一，所以可以利用ASCII 索引作为其整数下标的映射：a对应97，b对应98等等。此时，通常可以与面试官进行沟通，作出字符串中仅含有a-z，A-Z的合理假设，这样可以缩小bitset的空间需求。

## Complexity

哈希表和bitset做法都需要扫描整个字符串，每次插入操作时间复杂度O(1)，假设字符串长度为n，则平均时间复杂度都是O(n)。空间上，每个合法字符都有可能出现，假设字符集大小为m，则平均空间是O(m)。哈希表的数据结构需要占用更多空间，所以bit-set是更合理的数据结构。

## Code

```java
boolean isUnique(String str){
	HashSet<Character> set = new HashSet<Character>();
	for (int i = 0; i < str.length(); i++){
		if(set.contains(str.charAt(i)){
			return false;
		}
		set.add(str.charAt(i));
	}
	return true;
}
```



