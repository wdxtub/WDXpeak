# Boggle Game - Word Search

出处

Solve a boggle game(http://en.wikipedia.org/wiki/Boggle), with a dictionary given as unordered_set.

## Solution

1)	猜词游戏(boggle game)实际上就是寻找有限路径，判断路径能否组成单词。从matrix的每一个slot出发进行回溯，直到超过matrix的边缘，或者当前slot已经被访问过(环路可能)，或者路径超过了最长单词的长度，就三种invalid条件。胜利条件是当前的路径组成一个词典中的单词，但胜利条件之后应当继续回溯(统一地，对任何回溯问题，在处理上胜利条件之后都应该继续回溯，只不过很多时候胜利节点就是末节点，因此回溯下去也会因为invalid条件返回而已)。

2)	考虑对这个问题剪枝，可以将dictionary改写成prefix tree，这样才每一步查询时，可以根据当前路径序列是否是一个有效的prefix，增加一个invalid的条件，大幅提高搜索的效率。Prefix tree的DFS，可以与问题的回溯同步进行，“可以与问题的回溯同步进行，matrix单条搜索路径中的节点，对应prefix tree单条搜索路径中的节点。

利用回溯的另一种情景是：就算是处理收敛结构问题，如果无论从哪一端出发，都避免不了“(部分)当前节点的解依赖后驱节点”(也就是说，当前节点，如果不能获知后驱节点，就无法得到有意义的解)的情况，那么可以也用回溯解决。

## Complexity

## Code
 
```java
public class Solution {
    /**
     * @param board: A list of lists of character
     * @param word: A string
     * @return: A boolean
     */
    public boolean exist(char[][] board, String word) {
        if (board==null || board.length==0) return false;
        boolean visited[][] = new boolean[board.length][board[0].length];
        for (int i=0; i < board.length; i++){
            for (int j=0; j < board[0].length; j++){
                if (search(word, 0, board, i, j, visited)) {
                    return true;
                }
            }
        }
        return false;
    }

    public boolean search(String word, int index, char[][] board, int i, int j, boolean[][] visited){
        if (i<0 || j<0 || i==board.length || j==board[0].length || visited[i][j]==true) return false;
        visited[i][j] = true;
        boolean result = false;
        if (board[i][j]==word.charAt(index)){
            if (index == word.length()-1) return true;
            //save the result here instead of just return the result, as we need to unset the visited matrix before return
            result = search(word, index+1, board, i-1, j, visited) ||
                            search(word, index+1, board, i+1, j, visited) ||
                            search(word, index+1, board, i, j-1, visited) ||
                            search(word, index+1, board, i, j+1, visited);
        }
        visited[i][j] = false;
        return result;
    }
}
```

