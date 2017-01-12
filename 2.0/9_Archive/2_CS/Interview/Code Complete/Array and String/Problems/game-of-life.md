# Game of Life

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies, as if by over-population..
4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state.

Follow up: 

1. Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
2. In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

## Solution

最简单的方法是再建一个矩阵保存，不过当inplace解时，如果我们直接根据每个点周围的存活数量来修改当前值，由于矩阵是顺序遍历的，这样会影响到下一个点的计算。如何在修改值的同时又保证下一个点的计算不会被影响呢？实际上我们只要将值稍作编码就行了，因为题目给出的是一个int矩阵，大有空间可以利用。这里我们假设对于某个点，值的含义为

0 : 上一轮是0，这一轮过后还是0
1 : 上一轮是1，这一轮过后还是1
2 : 上一轮是1，这一轮过后变为0
3 : 上一轮是0，这一轮过后变为1
这样，对于一个节点来说，如果它周边的点是1或者2，就说明那个点上一轮是活的。最后，在遍历一遍数组，把我们编码再解回去，即0和2都变回0，1和3都变回1，就行了。

注意

注意编码方式，1和3都是这一轮过后为1，这样就可以用一个模2操作来直接解码了
我实现的时候并没有预先建立一个对应周围8个点的数组，因为实际复杂度是一样，多加几个数组反而程序可读性下降


## Complexity

时间复杂度 O(n^2 )，空间复杂度 O(1)

## Code

```java
public class Solution {
    public void gameOfLife(int[][] board) {
        int m = board.length, n = board[0].length;
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                int lives = 0;
                // 判断上边
                if(i > 0){
                    lives += board[i - 1][j] == 1 || board[i - 1][j] == 2 ? 1 : 0;
                }
                // 判断左边
                if(j > 0){
                    lives += board[i][j - 1] == 1 || board[i][j - 1] == 2 ? 1 : 0;
                }
                // 判断下边
                if(i < m - 1){
                    lives += board[i + 1][j] == 1 || board[i + 1][j] == 2 ? 1 : 0;
                }
                // 判断右边
                if(j < n - 1){
                    lives += board[i][j + 1] == 1 || board[i][j + 1] == 2 ? 1 : 0;
                }
                // 判断左上角
                if(i > 0 && j > 0){
                    lives += board[i - 1][j - 1] == 1 || board[i - 1][j - 1] == 2 ? 1 : 0;
                }
                //判断右下角
                if(i < m - 1 && j < n - 1){
                    lives += board[i + 1][j + 1] == 1 || board[i + 1][j + 1] == 2 ? 1 : 0;
                }
                // 判断右上角
                if(i > 0 && j < n - 1){
                    lives += board[i - 1][j + 1] == 1 || board[i - 1][j + 1] == 2 ? 1 : 0;
                }
                // 判断左下角
                if(i < m - 1 && j > 0){
                    lives += board[i + 1][j - 1] == 1 || board[i + 1][j - 1] == 2 ? 1 : 0;
                }
                // 根据周边存活数量更新当前点，结果是0和1的情况不用更新
                if(board[i][j] == 0 && lives == 3){
                    board[i][j] = 3;
                } else if(board[i][j] == 1){
                    if(lives < 2 || lives > 3) board[i][j] = 2;
                }
            }
        }
        // 解码
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                board[i][j] = board[i][j] % 2;
            }
        }
    }
}
```

