# Set Matrix Zero

给定一个m×n矩阵，如果一个元素是0，则将其所在行和列全部元素变成0。

需要在原地完成。

样例

    给出一个矩阵[[1,2],[0,3]]，返回[[0,2],[0,0]]

挑战

    你是否使用了额外的空间？
    一个直接的解决方案是使用O(MN)的额外空间，但这并不是一个好的方案。
    一个简单的改进方案是使用O(M + N)的额外空间，但这仍然不是最好的解决方案。
    你能想出一个常数空间的解决方案吗？

## Solution

1. 设置两个布尔型标示符flag_row,flag_col用来保存第0行和第0列是否需要置0,初始值false
2. 遍历第0行，如果遇到0，则将flag_row=true
3. 同上遍历第0列，如果遇到0，则将flag_col=true
4. 遍历剩下的元素即i从1开始，j从一开始，如果遇到某个元素【i,j】为0，则将matrix[i][0]=0,matrix[0][j]=0
5. 遍历第0行，遇到matrix[0][j]=0则设置此列上的所有元素为0
6. 遍历第0列，遇到matrix[i][0]=0则设置此行上的所有元素为0
7. 判断flag_row是否为true，是的话设置第0行元素均为0
8. 判断flag_col是否为true，是的话设置第0列元素均为0
9. 至此，题目完成

## Complexity

时间复杂度 O(n^2 )，空间复杂度 O(n)

## Code

```java
public class Solution {
    /**
     * @param matrix: A list of lists of integers
     * @return: Void
     */
    public void setZeroes(int[][] matrix) {
        int row = matrix.length;
        if (row == 0) {
            return;
        }
        int col = matrix[0].length;

        int rowIndex = 0;
        int colIndex = 0;
        boolean stop = false;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == 0) {
                    rowIndex = i;
                    colIndex = j;
                    stop = true;
                    break;
                }
            }
            if (stop) {
                break;
            }
        }

        if (!stop) {
            return;
        }

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (i == rowIndex || j == colIndex) {
                    continue;
                }

                if (matrix[i][j] == 0) {
                    matrix[rowIndex][j] = 0;
                    matrix[i][colIndex] = 0;
                }
            }
        }

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (i == rowIndex || j == colIndex) {
                    continue;
                }
                if (matrix[rowIndex][j] == 0 || matrix[i][colIndex] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }

        for (int i = 0; i < row; i++) {
            matrix[i][colIndex] = 0;
        }
        for (int j = 0; j < col; j++) {
            matrix[rowIndex][j] = 0;
        }
    }
}

```

