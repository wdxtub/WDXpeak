# String Composition

出处

Given a newspaper and message as two strings, check if the message can be composed using letters in the newspaper.

## Solution

在什么情况下newspaper中出现的字符能够组成message？

首先，message中用到的字符必须出现在newspaper中。其次，message中任意字符出现的次数一定少于其在newspaper中出现的次数。一旦需要统计一个元素集中元素出现的次数，我们就应该想到哈希表。键是字符，值是字符在newspaper中出现的次数。那么，如果message中用到的字符没有出现在哈希表中，则构成失败；如果 message用到了某个哈希表中出现的字符，那我们可以将值减少，表示“消耗”了一个字符。如果最终某个值变成了负值，那么message中该字符出现的次数多于其在newspaper中出现的次数，构成失败。

## Complexity

假设message长度为m ，newspaper长度为n，我们的算法需要hash整条message和整个newspaper，故时间复杂度O(m+n)。假设字符集大小为c，则平均空间是O(c)

## Code

```java
boolean canCompose(String newspaper, String message){
	if (message == null) return true;
	if (newspaper == null) return false;
	
	HashMap<Character, Integer> alphabet = new HashMap<Character, Integer>();
	
	for (int i = 0; i < newspaper.length(); i++){
		if (alphabet.containsKey(newspaper.charAt(i)){
			alphabet.put(newspaper.charAt(i), alphabet.get(newspaper.charAt(i))+1);
		} else {
			alphabet.put(newspaper.charAt(i), 1);
		}
	}
	
	for (int i = 0; i < message.length(); i++){
		if (!alphabet.containsKey(message.charAt(i)){
			return false;
		} else {
			if (alphabet.get(message.charAt(i)) == 0){
				return false;
			} else {
				alphabet.put(message.charAt(i), alphabet.get(nespaper.charAt(i))-1);
			}
		}
	}
	return true;
}
```

