# Unique Path

出处

How many paths are there for a robot to go from (0,0) to (x,y), supposing it can only move down and move right.

## Solution

这是一个具有收敛性的数量问题，需要在x轴和y轴两个维度上使用二维DP。

递推关系：Paths(i, j) = Paths(i+1, j) + Paths(i, j+1); i和j分别表示起点的横纵坐标。DP table可以是一个二维数组，这样的解答在实际面试中已经足够好。但事实上，根据上述DP table的优化理论，我们至少可以选取一个维度来化简，因为我们只关心紧接的那一行/列的结果，而不在乎之前的行/列的结果，我们可以将新的结果叠加上去，这样可以仅用一个array作为DP table，详见解答。

## Complexity

时间复杂度 O(n^2 )，空间复杂度 O(n^2 )，可以优化到 O(n)

## Code

二维数组解法

```java
int uniquePaths(int m, int n) {
	int[][] ways = new int[m][n];
	for (int i = 0; i < m; i++){
		ways[i][0] = 1;
	}
	for (int i = 0; i < n; i++){
		ways[0][i] = 1;
	}
	for (int i = 1; i < m; i++){
		for (int j = 1; j < n; j++){
			ways[i][j] = ways[i-1][j] + ways[i][j-1];
		}
	}
	return ways[m-1][n-1];
}
```

一维数组解法

```java
int uniquePaths(int m, int n) {
	int[] ways = new int[n];
	for (int i = 0; i < n; i++){
		ways[i] = 1;
	}
	for (int i = 1; i < m; i++){
		for (int j = 1; j < n; j++){
			ways[j] = ways[j-1] + ways[j];
		}
	}
	return ways[n-1];
}
```


