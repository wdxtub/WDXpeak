# Longest Common Subsequence

出处

Please write a function to calculate the Longest Common Subsequence (LCS) given two strings.

LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.

LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.

## Solution

同时遍历两个序列，考虑以当前两个节点为末节点的序列的common subsequence长度。如果其对应的字符相等，那么可以使得LCS长度+1，即append当前字符；否则，保留较优的结果。递推关系如下：

Length(i,j) = (str1[i-1] == str2[j-1]) ? Length(i-1, j-1) + 1 ： Max { Length(i,j-1), Length(i-1,j) }

当char i != char j, D[i ][j - 1], D[i - 1][j] 里取一个大的（因为最后一个不相同，所以有可能s1的最后一个字符会出现在s2的前部分里，反之亦然。

## Complexity

循环遍历两次，时间复杂度 O(n^2 ) 空间复杂度 O(n^2 )

## Code

```java
int lcs(String a, String b){
	int lena = a.length();
	int lenb = b.length();
	
	if (lena == 0 || lenb == 0){
		return 0;
	}
	
	int[][] dp = new int[lena+1][lenb+1];
	for (int i = 0; i <= lena; i++){
		for (int j = 0; j <= lenb; j++{
			if (i == 0 || j == 0){
				dp[i][j] = 0;
			} else if (a.charAt(i-1) == b.charAt(j-1){
				dp[i][j] = dp[i-1][j-1] + 1;
			} else {
				dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
			}
		}
	}
	return dp[lena][lenb];
}

```
 

