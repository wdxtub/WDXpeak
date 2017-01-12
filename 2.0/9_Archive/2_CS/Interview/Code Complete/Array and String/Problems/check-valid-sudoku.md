# Check Valid Sudoku

请判定一个数独是否有效。

该数独可能只填充了部分数字，其中缺少的数字用 . 表示。

注意

    一个合法的数独（仅部分填充）并不一定是可解的。我们仅需使填充的空格有效即可。

说明 什么是数独？

+ [英文版](http://sudoku.com.au/TheRules.aspx)
+ [中文版](http://baike.baidu.com/subview/961/10842669.htm)

## Solution

按照题意进行检测即可

## Complexity

时间复杂度 O(n^2 )，空间复杂度 O(n)

## Code

```java
class Solution {
    /**
      * @param board: the board
        @return: wether the Sudoku is valid
      */
    public boolean isValidSudoku(char[][] board) {
        if(board == null || board.length == 0 || board[0].length == 0) return false;

        int m = 9, n = 9;
        // check row
        boolean[] visited = new boolean[9];
        for(int i = 0; i < m; i++){
            Arrays.fill(visited, false);
            for(int j = 0; j < n; j++){
                if(!precess(visited, board[i][j])) return false;
            }
        }

        for(int i = 0; i < n; i++){
            Arrays.fill(visited, false);
            for(int j = 0; j < m; j++){
                if(!precess(visited, board[j][i])) return false;
            }
        }

        for(int i = 0; i < m; i+=3){

          for(int j = 0; j < n; j+=3){
              Arrays.fill(visited, false);
              for(int k = 0; k < 9; k++){
                  if(!precess(visited, board[i+k/3][j+k%3])) return false;
              }

            }
        }
        return true;

    }

    private boolean precess(boolean[] visited, char c){
        if(c == '.') return true;
        int num = c - '0';
        if(num > 9 || num < 1 || visited[num-1]) return false;
        visited[num-1] = true;
        return true;
    }
};

```

