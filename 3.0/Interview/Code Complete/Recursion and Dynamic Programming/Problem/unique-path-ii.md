# Unique Path II

出处

现在考虑网格中有障碍物，那样将会有多少条不同的路径？

网格中的障碍和空位置分别用1和0来表示。

样例


    如下所示在3x3的网格中有一个障碍物：
    [
    [0,0,0],
    [0,1,0],
    [0,0,0]
    ]
    一共有2条不同的路径从左上角到右下角。

注意

    m和n均不超过100

## Solution

这里需要注意的是处理有障碍物时的情况，即直接表示为零，然后按照同样的方式进行累加。而因为要从第一个元素进行处理，所以需要注意如果还是用 `result[j] = result[j] + result[j-1]` 在 `j==0` 时会出现 `result[-1]` 的情况，就不符合题目意思了，所以在边界需要特别处理一下

## Complexity

时间复杂度 O(n)，空间复杂度 O(n)

## Code

```python
class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        result = [1] * n
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                for j in range(i, n):
                    result[j] = 0

        for i in range(1, m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    result[j] = 0
                elif j != 0:
                    result[j] = result[j] + result[j-1]

        return result[-1]
```

