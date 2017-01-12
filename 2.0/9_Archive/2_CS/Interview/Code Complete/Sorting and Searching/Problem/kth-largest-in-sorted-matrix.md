# Kth Largest in Sorted Matrix

在一个排序矩阵中找从小到大的第 k 个整数。

排序矩阵的定义为：每一行递增，每一列也递增。

样例

    给出 k = 4 和一个排序矩阵：
    [
      [1 ,5 ,7],
      [3 ,7 ,8],
      [4 ,8 ,9],
    ]
    返回 5。

挑战

    使用O(k log n)的方法，n为矩阵的宽度和高度中的最大值。

## Solution

用优先队列，也就是最小堆

时间复杂度 O(logn)，空间复杂度 O(n)

## Code

```java
public class Solution {
    /**
     * @param matrix: a matrix of integers
     * @param k: an integer
     * @return: the kth smallest number in the matrix
     */
    public int kthSmallest(final int[][] matrix, int k) {
        int m = matrix.length, n = matrix[0].length;
        boolean[][] visited = new boolean[m][n];

        PriorityQueue<int[]> queue = new PriorityQueue<int[]>(k, new Comparator<int[]>(){
            public int compare(int[] a, int[]b){
                return matrix[a[0]][a[1]] - matrix[b[0]][b[1]];
            }
        });
        queue.add(new int[]{0,0});
        visited[0][0] = true;
        while(k > 1){
            int[] res = queue.poll();
            k--;
            int x = res[0];
            int y = res[1];
            if(x+1 < m && visited[x+1][y] == false){
                queue.add(new int[]{x+1, y});
                visited[x+1][y] = true;
            }

            if(y+1 < n && visited[x][y+1] == false){
                queue.add(new int[]{x, y+1});
                visited[x][y+1] = true;
            }
        }
        int[] res = queue.poll();
        return matrix[res[0]][res[1]];
    }
}

```

