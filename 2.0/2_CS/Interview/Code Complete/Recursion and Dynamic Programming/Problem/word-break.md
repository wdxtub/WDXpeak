# Word Break

出处

Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

For example, given

s = "leetcode",

dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

## Solution

这个问题属于在所有组合中，寻求一个特解以满足一定的条件。对于这样的判定性问题，它具有很强的聚合性，可以用DP。

DP的关键在于寻找递推关系：考虑string的前n个字符，那么对于第i个字符(i [0, n))，如果[0,i)可以由一个或多个单词组成(前驱节点，可以直接读取DP table中计算过的结果)，并且[i, n)是一个单词(这一段我们不能去借助局部解，因为目前为止，我们只有[0,1), [0,2) … [0, n-1)的结果，需要利用字典判断)，那么，[0, n)的结果就是true。

## Complexity

遍历到每个位置的时候还需要检查以当前位置为起始的词是不是在字典中，故时间复杂度为 O(n^2 )，空间复杂度为 O(n)

## Code 

```java
boolean wordBreak(String str, HashSet<String> dict){
	boolean[] dp = new boolean[str.length() + 1];
	dp[0] = true;
	for (int i = 1; i <= str.length(); i++){
		dp[i] = false;
	}
	for (int end = 0; end < str.length(); end++){
		for (int begin = 0; begin < str.length(); begin++){
			if (dp[begin] && dict.contains(str.substring(begin, end-begin+1){
				dp[end+1] = true;
				break;
			}
		}
	}
	return dp[str.lengt()];
}
```


