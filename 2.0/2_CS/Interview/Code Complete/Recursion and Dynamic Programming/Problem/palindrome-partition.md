# Palindrom Partition

出处 leetcode 131, 132

Given a string s, we can partition s such that every segment is a palindrome (e.g, ‘abba’ is a palindrome, ‘a’ is a palindrome, ‘ab’ is not). Please write a function to return the minimum cuts needed for a palindrome parti“tioning, given string s.

## Solution

凡是求最优解的，一般都是走DP的路线。这一题也不例外。首先求dp函数，

定义函数 D[i,n] = 区间[i,n]之间最小的cut数，n为字符串长度

	a b a b b b a b b a b a
	        i             n

如果现在求[i,n]之间的最优解？应该是多少？简单看一看，至少有下面一个解


	a   b   a   b   b   b   a   b   b   a   b   a
	                i               j  j+1      n

此时  D[i,n] = min(D[i, j] + D[j+1,n])  i<=j <n。这是个二维的函数，实际写代码时维护比较麻烦。所以要转换成一维DP。如果每次，从i往右扫描，每找到一个回文就算一次DP的话，就可以转换为
D[i] = 区间[i,n]之间最小的cut数，n为字符串长度， 则,

D[i] = min(1+D[j+1] )    i<=j <n

判断字串是不是回文(palindrome)，实际上也是一个递归问题，递推关系是：

isPalindrome( i , j ) = (value(i) == value(j)) AND ( isPalindrome(i+1, j-1) OR j – i <= 1 ) ， i和j分别表示substring的首坐标和尾坐标。

注意i的前驱坐标是i+1，j的前驱坐标是j-1， 所以在具体处理时，前者是倒序遍历，后者是顺序遍历，其实也是利用了自底向上，自底向上的处理方向总是与直观理解的方向相反，这样可以确保每次都能调用已经计算过的结果。

再来考虑cut的问题，因为首坐标的遍历顺序是倒序，因此可以将minCut(i)定义为：将原字符串最末字符到第i个字符视为子串，依题意处理这个字串需要的最少cut 数量。所谓的“最少”，同样是一个DP问题，递归式如下(请深刻理解该递归式，所有DP相关的最大／最小问题都可以总结为类似的递归式)：
minCut(i) = min(minCut[j+1]+1, minCut[i])，for i <= j < n, and substring(i , j) is palindrome。

直观上说，如果substring(i , j)是回文，那么一种分割方式就是将i到j视为一个子串，j+1到字符串末尾按照minCut(j+1)的方式分割。这样，minCut(i)需要在minCut(j+1)的基础上再分割一次(substring(i , j))。最终，最外层的最小值符号确保保存minCut(i)是所有这些分割中最优的一个。

注意对于最小值，可以初始化一个显然的最坏的解，在这里就是每一个字符都需要分割的情况。

## Complexity

时间复杂度 O(n^2 )，空间复杂度 O(n^2 )

## Code 

```java
int palindromePartition(String str){
	boolean[][] flag = new boolean[str.length()][str.length()];
	int[] dp = new int[str.length() + 1];
	for (int i = 0; i < dp.length; i++){
		dp[i] = dp.length - i - 1;
	}
	
	for (int i = str.length() - 1; i >= 0; i--){
		for (int j = i; j < str.length(); j++){
			if ((str.charAt(i) == str.charAt(j) && ((j-i < 2) || flag[i+1][j-1])){
				flag[i][j] = true;
				dp[i] = Math.min(dp[j+1]+1, dp[i]);
			}
		} 
	}
	return dp[0];
}
```




