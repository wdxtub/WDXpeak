# Package Problem II

出处

给出n个物品的体积 A[i] 和其价值 V[i]，将他们装入一个大小为m的背包，最多能装入的总价值有多大？

样例

    对于物品体积[2, 3, 5, 7]和对应的价值[1, 5, 2, 4], 假设背包大小为10的话，最大能够装入的价值为9。

注意

    A[i], V[i], n, m均为整数。你不能将物品进行切分。你所挑选的物品总体积需要小于等于给定的m。

## Solution

这道题还是跟Backpack有大不一样之处

用子问题定义状态：即f[i][v]表示前 i 件物品恰放入一个容量为 j 的背包可以获得的最大价值。则其状态转移方程便是：

f[i][j] = max{f[i-1][j], j>=A[i-1]? f[i-1][j-A[i-1]]+V[i-1] : 0}

## Complexity

时间复杂度 O(n^2 )，空间复杂度 O(n^2 )

## Code

```java
public class Solution {
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A & V: Given n items with size A[i] and value V[i]
     * @return: The maximum value
     */
    public int backPackII(int m, int[] A, int V[]) {
        int[][] res = new int[A.length+1][m+1];
        res[0][0] = 0;
        for (int i=1; i<=A.length; i++) {
            for (int j=0; j<=m; j++) {
                if (j - A[i-1] < 0)
                    res[i][j] = res[i-1][j];
                if (j - A[i-1] >= 0) {
                    res[i][j] = Math.max(res[i-1][j], res[i-1][j-A[i-1]]+V[i-1]);
                }
            }
        }

        return res[A.length][m];
    }
}

```


