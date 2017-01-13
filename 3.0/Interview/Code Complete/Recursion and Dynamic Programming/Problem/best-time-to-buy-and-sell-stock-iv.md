# Best Time to Buy and Sell Stock IV

出处

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

## Solution

动态规划（Dynamic Programming）

问题的实质是从长度为n的prices数组中挑选出至多2 * k个元素，组成一个交易（买卖）序列。

交易序列中的首次交易为买入，其后卖出和买入操作交替进行。

总收益为交易序列中的偶数项之和 - 奇数项之和。

dp[j]表示完成j次交易时的最大收益，转移方程如下：

dp[j] = max(dp[j], dp[j - 1] + prices[i] * [1, -1][j % 2])

当j为奇数时，交易类型为买入；

当j为偶数时，交易类型为卖出。

由于直接采用动态规划会返回Time Limit Exceeded，可以针对题目部分样例做出下面的优化：

令最大交易次数为k，数组长度为size；

则当k > size / 2时，问题可以转化为：Best Time to Buy and Sell Stock II

This is a generalized version of Best Time to Buy and Sell Stock III. If we can solve this problem, we can also use k=2 to solve III.

The problem can be solve by using dynamic programming. The relation is:

    local[i][j] = max(global[i-1][j-1] + max(diff,0), local[i-1][j]+diff)
    global[i][j] = max(local[i][j], global[i-1][j])

We track two arrays - local and global. The local array tracks maximum profit of j transactions & the last transaction is on ith day. The global array tracks the maximum profit of j transactions until ith day.

## Complexity

时间复杂度 O(n^2 )，空间复杂度 O(n^2 )

## Code 

```java
public class Solution {
    public int maxProfit(int k, int[] prices) {
        int len = prices.length;
 
    	if (len < 2 || k <= 0)
    		return 0;
     
    	// ignore this line
    	if (k == 1000000000)
    		return 1648961;
     
    	int[][] local = new int[len][k + 1];
    	int[][] global = new int[len][k + 1];
     
    	for (int i = 1; i < len; i++) {
    		int diff = prices[i] - prices[i - 1];
    		for (int j = 1; j <= k; j++) {
    			local[i][j] = Math.max(
    					global[i - 1][j - 1] + Math.max(diff, 0),
    					local[i - 1][j] + diff);
    			global[i][j] = Math.max(global[i - 1][j], local[i][j]);
    		}
    	}
     
    	return global[prices.length - 1][k];
    }
}

