# Number of Islande

出处

给一个01矩阵，求不同的岛屿的个数。

0代表海，1代表岛，如果两个1相邻，那么这两个1属于同一个岛。我们只考虑上下左右为相邻。

## Solution

Use DFS to find the number of connected components of the graph. One full DFS traversal of a node yields a connected component, which could be viewed as an island containing adjacent nodes (by left,right,up and down). Then we could traverse other isolated node excluded from this connected component, in the same manner.

## Complexity

时间复杂度 O(n)，空间复杂度 O(n)

## Code

其实可以不用 visit 访问过的设为 0 即可

```java
public class Solution {
    private void detectIsland(char[][] grid, int i, int j) {
		if (grid[i][j] == '1') {
			grid[i][j] = '0';
			if (i > 0) {
					detectIsland(grid, i-1, j);
			}
			if (i < grid.length-1) {
				detectIsland(grid, i+1, j);
			}
			if (j < grid[0].length-1) {
				detectIsland(grid, i, j+1);
			}
			if (j > 0) {
				detectIsland(grid, i, j-1);
			}
		} else {
			return;
		}
	}
	
    public int numIslands(char[][] grid) {
    	if (grid==null || grid.length==0 || grid[0].length==0) {
    		return 0;
    	}
        int numberOfIslands = 0;
        for (int i = 0;i != grid.length;i++) {
        	for (int j = 0;j != grid[0].length;j++) {
        		if (grid[i][j] == '1') {
        			numberOfIslands++;
        			detectIsland(grid, i, j);
        		}
        	}
        }
        return numberOfIslands;
    }
}
```


---

```java
public class Solution {
    /**
     * @param grid a boolean 2D matrix
     * @return an integer
     */
    public int numIslands(boolean[][] grid) {
        if(grid == null || grid.length == 0) {
            return 0;
        }

        final int N = grid.length;
        final int M = grid[0].length;
        final boolean visited[][] = new boolean[N][M];
        int count = 0;

        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {

                if(grid[i][j] && !visited[i][j]) {
                    dfs(grid, i, j, visited);
                    count++;
                }
            }
        }
        return count;
    }

    private void dfs(boolean[][] grid, int i, int j, boolean[][] visited) {
        if(i < 0 || i >= grid.length || j < 0 || j >= grid[0].length) {
            return;
        } else if (visited[i][j] || !grid[i][j] ) {
            return;
        }

        visited[i][j] = true;
        dfs(grid, i - 1, j, visited);
        dfs(grid, i + 1, j, visited);
        dfs(grid, i, j - 1, visited);
        dfs(grid, i, j + 1, visited);
    }
}

```

