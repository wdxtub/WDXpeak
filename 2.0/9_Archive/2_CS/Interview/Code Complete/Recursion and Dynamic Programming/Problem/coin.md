# Coin

出处

Given a value N, this N means we need to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change?

## Solution

本问题以及其他类似描述的Coin Change问题，都属于典型的分布在二维整数空间上的计数问题，用DP。

重要的是理解如下递推关系：

对于第j种coin，无非是选择和不选择使用两种可能(i是目标钱数，j是当前coin的下标)

ways(i, j) = ways(i-s(j), j) + ways(i, j-1);  i~[0,N], j~[1,m]

注意到在j这个维度上，只在意紧邻的上一步的结果，而不在意过去几步的结果，最后仍然是求和，因此上一步的局部解也只是当前解求和过程当中的一部分，完全可以覆盖，仅用一个变量表示，因此DP table可以简化为i方向一维空间。

## Complexity

两层循环，时间复杂度 O(mn)，空间复杂度 O(n)

## Code

```python
stepstr = input()
steps = stepstr.split()
test = int(input())

table = [[0 for x in range(len(steps))] for x in range(int(1E5+1))]
# Fill the enteries for 0 value case (n = 0)
for i in range(len(steps)):
    table[0][i] = 1

last = 1
for t in range(0,test):
    target = int(input())
 
    # Fill rest of the table enteries in bottom up manner
    for i in range(last, target+1):
        for j in range(len(steps)):
            # Count of solutions including S[j]
            x = table[i - int(steps[j])][j] if i-int(steps[j]) >= 0 else 0
 
            # Count of solutions excluding S[j]
            y = table[i][j-1] if j >= 1 else 0
 
            # total count
            table[i][j] = x + y
            table[i][j] %= 1E9+7;
    if (target > last):
        last = target
    print(int(table[target][len(steps)-1]))
 
```


```java
int minNum(int[] S, int n) {
	int[] dp = new int[n+1];
	for (int i = 0; i < n+1; i++){
		dp[i] = Integer.MAX_INT;
	}
	dp[0] = 0;
	for (int i = 1; i <= n; i++){
		for (int j = 0; j < m; j++){
			if (i >= s[j] && dp[i] > dp[i-s[j]]){
				dp[i] = dp[i-s[j]] + 1;
			}
		}
	}
	return dp[n];
}
```

# Coin

Given an infinite number of quarters(25 cents), dimes(10 cents), nickels(5 cents), and pennies(1 cent), write code to calculate the number of ways of representing n cents.

## Solution

```java
// Use the solution from the book to help understanding
public static int makeChange(int amount, int[] cents, int index){
    if (index == cents.length - 1)
        return 1;
    int coin = cents[index];
    int ways = 0;
    for (int i = 0; i * coin <= amount; i++){
        int rest = amount - i * coin;
        ways += makeChange(rest, cents, index+1);
    }
    return ways;
}

public static int makeChange(int n){
    int[] cents = {25, 10, 5, 1};
    return makeChange(n, cents, 0);
}       
``` 

