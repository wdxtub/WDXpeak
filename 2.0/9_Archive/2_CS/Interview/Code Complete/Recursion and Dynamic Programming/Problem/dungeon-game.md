# Dungeon Game

The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.


Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

    -2(K)  -3	 3
    -5    -10	 1
    10	 30	 -5 (P)

Notes:

+ The knight's health has no upper bound.
+ Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

## Solution

Fortunately, this problem can be solved through a table-filling Dynamic Programming technique, similar to other "grid walking" problems:

To begin with, we should maintain a 2D array D of the same size as the dungeon, where D[i][j] represents the minimum health that guarantees the survival of the knight for the rest of his quest BEFORE entering room(i, j). Obviously D[0][0] is the final answer we are after. Hence, for this problem, we need to fill the table from the bottom right corner to left top.

Then, let us decide what the health should be at least when leaving room (i, j). There are only two paths to choose from at this point: (i+1, j) and (i, j+1). Of course we will choose the room that has the smaller D value, or in other words, the knight can finish the rest of his journey with a smaller initial health. Therefore we have:

  min_HP_on_exit = min(D[i+1][j], D[i][j+1])
  
Now D[i][j] can be computed from dungeon[i][j] and min_HP_on_exit based on one of the following situations:

If dungeon[i][j] == 0, then nothing happens in this room; the knight can leave the room with the same health he enters the room with, i.e. D[i][j] = min_HP_on_exit.

If dungeon[i][j] < 0, then the knight must have a health greater than min_HP_on_exit before entering (i, j) in order to compensate for the health lost in this room. The minimum amount of compensation is "-dungeon[i][j]", so we have D[i][j] = min_HP_on_exit - dungeon[i][j].

If dungeon[i][j] > 0, then the knight could enter (i, j) with a health as little as min_HP_on_exit - dungeon[i][j], since he could gain "dungeon[i][j]" health in this room. However, the value of min_HP_on_exit - dungeon[i][j] might drop to 0 or below in this situation. When this happens, we must clip the value to 1 in order to make sure D[i][j] stays positive: D[i][j] = max(min_HP_on_exit - dungeon[i][j], 1).

Notice that the equation for dungeon[i][j] > 0 actually covers the other two situations. We can thus describe all three situations with one common equation, i.e.:

D[i][j] = max(min_HP_on_exit - dungeon[i][j], 1)

for any value of dungeon[i][j].

Take D[0][0] and we are good to go. Also, like many other "table-filling" problems, the 2D array D can be replaced with a 1D "rolling" array here.

## Code

```java
public class Solution {
    public int calculateMinimumHP(int[][] dungeon) {
        int M = dungeon.length;
        if (M == 0) return 0;
        int N = dungeon[0].length;
        int[][] dp = new int[M][N];
        dp[M-1][N-1] = 1 - Math.min(0, dungeon[M-1][N-1]);
        for (int i = M - 2; i >= 0; --i) {
            if (dp[i+1][N-1] - dungeon[i][N-1] <= 0) dp[i][N-1] = 1;
            else dp[i][N-1] = dp[i+1][N-1] - dungeon[i][N-1]; 
        }
        for (int j = N - 2; j >= 0; --j) {
            if (dp[M-1][j+1] - dungeon[M-1][j] <= 0) dp[M-1][j] = 1;
            else dp[M-1][j] = dp[M-1][j+1] - dungeon[M-1][j];
        }
        for (int i = M - 2; i >= 0; --i) {
            for (int j = N - 2; j >= 0; --j) {
                int val = Math.min(dp[i+1][j], dp[i][j+1]);
                if (dungeon[i][j] >= val) dp[i][j] = 1;
                else dp[i][j] = val - dungeon[i][j];
            }
        }
        return Math.max(1,dp[0][0]); 
    }
}
```

