# Best Time to Buy and Sell Stock II

出处

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

## Solution

1. At the beginning of the ascending order: buy.
2. At the ending of the ascending order: sell.

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code 

```java
public class Solution {
    public int maxProfit(int[] prices) {
        int res = 0;
        for (int i = 1; i < prices.length; ++i) {
            res += Math.max(0, prices[i] - prices[i-1]);
        }
        return res;
    }
}
```

