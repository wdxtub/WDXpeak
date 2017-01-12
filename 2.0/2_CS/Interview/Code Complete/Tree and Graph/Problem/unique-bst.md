# Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

    1         3     3      2      1
     \       /     /      / \      \
      3     2     1      1   3      2
     /     /       \                 \
    2     1         2                 3
    
## Solution

dp

## Code

```java
public class Solution {
    public int numTrees_1(int n) {
        int[] dp = new int[n+1];
        dp[0] = 1;
        for (int i = 1; i <= n; ++i)
            for (int j = 0; j < i; j++)
                dp[i] += dp[j] * dp[i-j-1];
        return dp[n];
    }
    public int numTrees(int n) {
        if (n < 0) return 0;
        int[] dp = new int[n+1];
        dp[0] = 1; dp[1] = 1;
        for(int i = 2;i <= n; ++i){
            dp[i] = dp[i-1] * (4 * i - 2)/(i + 1);
        }
        return dp[n];
    }
}
```

