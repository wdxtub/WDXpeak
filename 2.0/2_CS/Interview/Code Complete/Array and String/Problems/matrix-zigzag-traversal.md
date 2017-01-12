# Matrix ZigZag Traversal

给你一个包含 m x n 个元素的矩阵 (m 行, n 列), 求该矩阵的之字型遍历。

样例

对于如下矩阵：

    [
      [1, 2,  3,  4],
      [5, 6,  7,  8],
      [9,10, 11, 12]
    ]
    返回 [1, 2, 5, 9, 6, 3, 4, 7, 10, 11, 8, 12]

## Solution

注意越界问题

## Complexity

时间复杂度 O(n^2 )，空间复杂度 O(1)

## Code

```java
// java
public class Solution {
    /**
     * @param matrix: a matrix of integers
     * @return: an array of integers
     */ 
    public int[] printZMatrix(int[][] matrix) {
        if(matrix == null || matrix.length == 0 || matrix[0].length == 0) return null;
        int count = matrix.length * matrix[0].length;
        int[] array = new int[count];
        int r = 0, c = 0;
        array[0] = matrix[0][0];
        for (int i = 1; i < count; ) {
            //斜上走到顶
            while(i < count && r - 1 >= 0 && c + 1 < matrix[0].length) {
                array[i++] = matrix[--r][++c];
            }
            //横右走一步，不可横右走时竖下走一步
            if (i < count && c + 1 < matrix[0].length) {
                array[i++] = matrix[r][++c];
            } else if (i < count && r + 1 < matrix.length) {
                array[i++] = matrix[++r][c];
            }
            //斜下走到底
            while(i < count && r + 1 < matrix.length && c - 1 >= 0) {
                array[i++] = matrix[++r][--c];
            }
            //竖下走一步，不可竖下走时横右走一步
            if (i < count && r + 1 < matrix.length) {
                array[i++] = matrix[++r][c];
            } else if (i < count && c + 1 < matrix[0].length) {
                array[i++] = matrix[r][++c];
            }
        }
        return array;
    }
}
```



```python
# python
class Solution:
    # @param: a matrix of integers
    # @return: a list of integers
    def printZMatrix(self, matrix):
        i = 0
        j = 0
        m = len(matrix)
        n = len(matrix[0])
        ret = []

        up = True
        for _ in xrange(m*n):
            ret.append(matrix[i][j])
            if up:
                if i-1<0 or j+1>=n:
                    up = False
                    if j+1>=n:  # go down
                        i += 1
                    else:  # go right
                        j += 1
                else:
                    i -= 1
                    j += 1
            else:
                if i+1>=m or j-1<0:
                    up = True
                    if i+1>=m:
                        j += 1  # go right
                    else:
                        i += 1  # go up
                else:
                    i += 1
                    j -= 1

        return ret

```

