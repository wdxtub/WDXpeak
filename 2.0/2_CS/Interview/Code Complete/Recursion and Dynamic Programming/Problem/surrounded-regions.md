# Surrounded Regions

Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,

    X X X X
    X O O X
    X X O X
    X O X X

After running your function, the board should be:

    X X X X
    X X X X
    X X X X
    X O X X

## Solution

Traverse from the border to the inside and mark all the 'O's that are not surrounded by 'X' as 'V' (visited).

转换一下思路，真的需要开辟一个map在存储访问信息吗？其实这个可以省掉的，既然已经知道连通区域必须至少一个元素是在四边，那么一开始直接从四边开始扫描就好了，所以无法connect到得元素都是应该被清除的。所以，算法如下：

1. 从四条边上的O元素开始BFS，所有相连的O都赋个新值，比如‘Y’
2. 扫描整个数组，所有现存的O元素全部置为X，所有Y元素置为O

BFS (queue).

## Code

```java
public class Solution {
    public void solve(char[][] board) {
        if (board.length == 0 || board[0].length == 0) return;
        int M = board.length, N = board[0].length;
        for (int i = 0; i < M; ++i) {
            for (int j = 0; j < N; ++j) {
                if (i == 0 || j == 0 || i == M - 1 || j == N -1) {
                    bfs(board, i, j);
                }
            }
        }
        for (int i = 0; i < M; ++i)
            for (int j = 0; j < N; ++j)
                board[i][j] = (board[i][j] == 'V') ? 'O' : 'X';
    }
    public void bfs(char[][] board, int row, int col) {
        if (board[row][col] != 'O') return;
        int M = board.length, N = board[0].length;
        Queue<Integer> q = new LinkedList<Integer>();
        q.offer(row); q.offer(col);
        while (q.isEmpty() == false) {
            int i = q.poll(); int j = q.poll();
            if (i < 0 || i == M || j < 0 || j == N) continue;
            if (board[i][j] != 'O') continue;// important to recheck!
            board[i][j] = 'V';
            q.offer(i-1); q.offer(j);
            q.offer(i+1); q.offer(j);
            q.offer(i); q.offer(j-1);
            q.offer(i); q.offer(j+1);
        }
    }
}
```

