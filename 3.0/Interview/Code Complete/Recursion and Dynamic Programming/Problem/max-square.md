# Max Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

样例

    For example, given the following matrix:

    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0

    Return 4.

## Solution

动态规划（Dynamic Programming）

状态转移方程：

    dp[x][y] = min(dp[x - 1][y - 1], dp[x][y - 1], dp[x - 1][y]) + 1

上式中，`dp[x][y]`表示以坐标(x, y)为右下角元素的全1正方形矩阵的最大长度（宽度）

## Complexity

时间复杂度 O(n^2 )，空间复杂度 O(n^2 )

## Code 

```java
public class Solution {
    /**
     * @param matrix: a matrix of 0 and 1
     * @return: an integer
     */
    public int maxSquare(int[][] matrix) {
        // write your code here
        if (matrix == null || matrix.length == 0) {
            return 0;
        }

        int[][] dp = new int[matrix.length][matrix[0].length];
        int max = 0;

        for (int i = 0; i < matrix.length; i++) {
            dp[i][0] = matrix[i][0] == 1 ? 1 : 0;
            max = Math.max(max, dp[i][0]);
        }

        for (int j = 0; j < matrix[0].length; j++) {
            dp[0][j] = matrix[0][j] == 1 ? 1 : 0;
            max = Math.max(max, dp[0][j]);
        }


        for (int i = 1; i < matrix.length; i++) {
            for (int j = 1; j < matrix[0].length; j++) {
                dp[i][j] = matrix[i][j] == 1 ?
                Math.min(Math.min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1 : 0;
                max = Math.max(max, dp[i][j]);
            }
        }

        return (int)Math.pow(max, 2);
    }
}

```

