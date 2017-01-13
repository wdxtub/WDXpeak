# N-Queens II

Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.

## Solution

1. Recursion.
2. Recursion + bit version. (fast) The idea is from http://www.matrix67.com/blog/archives/266 (in chinese).
3. Iteration. 

## Complexity

回溯总共n步，每次供选择的方向为n。经过剪枝之后，可以认为复杂度小于n!。

## Code

```java
public class Solution {
    public int totalNQueens(int n) {
        return totalNQueens_3(n);
    }
    public int totalNQueens_1(int n) {
        int[] board = new int[n];
        Arrays.fill(board,-1);
        int[] res = new int[1];
        totalNQueensRe(n, 0, board, res);
        return res[0];
    }
    public void totalNQueensRe(int n, int row, int[] board, int[] res) {
        if (n == row) {
            res[0]++;
            return;
        }
        for (int i = 0; i < n; ++i) {
            if (isValid(board, row, i)) {
                board[row] = i;
                totalNQueensRe(n, row + 1, board, res);
                board[row] = -1;
            }
        }
    }
    public boolean isValid(int[] board, int row, int col) {
        for (int i = 0; i < row; ++i) {
            if (board[i] == col || row - i == Math.abs(col - board[i]))
                return false;
        }
        return true;
    }
    public int totalNQueens_2(int n) {
        int[] res = new int[1];
        totalNQueensRe2(n, 0, 0, 0, res);
        return res[0];
    }
    public void totalNQueensRe2(int n, int row, int ld, int rd, int[] res) {
        if (row == (1<<n) -1 ) {
            res[0]++;
            return;
        }
        int avail = ~(row | ld | rd);
        for (int i = n - 1; i >= 0; --i) {
            int pos = 1<<i;
            if ((int)(avail&pos) != 0) {
                totalNQueensRe2(n, row | pos, (ld|pos) << 1, (rd|pos) >>1, res);
            }
        }
    }
    public int totalNQueens_3(int n) {
        int[] a = new int[n];
        Arrays.fill(a,-1);
        int res = 0;
        int row = 0;
        while (row >= 0) {
            if (row == n) {
                res++; row--;
            }
            int i = a[row] == -1 ? 0 : a[row] + 1;
            for ( ; i < n; ++i) {
                if (isValid(a, row, i)) {
                    a[row] = i;
                    row++;
                    break;
                }
            }
            if (i == n) {
                a[row] = -1;
                row--;
            }
        }
        return res;
    }
}
```

