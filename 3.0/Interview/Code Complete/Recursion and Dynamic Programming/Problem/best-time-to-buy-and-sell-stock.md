# Best Time to Buy and Sell Stock

出处

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

## Solution

For each element, calculate the max difference with the former elements.

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
public class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        if (n <= 1) return 0;
        int res = 0, minVal = prices[0];
        for (int i = 1; i < n; ++i) {
            res = Math.max(res, prices[i] - minVal);
            minVal = Math.min(minVal, prices[i]);
        }
        return res;
    }
}
```

