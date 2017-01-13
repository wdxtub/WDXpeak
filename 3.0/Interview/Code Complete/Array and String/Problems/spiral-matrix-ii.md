# Spiral Matrix II

Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,

Given n = 3,

You should return the following matrix:

    [
     [ 1, 2, 3 ],
     [ 8, 9, 4 ],
     [ 7, 6, 5 ]
    ]
    
## Solution

要仔细

## Code

```java
public class Solution {
    public int[][] generateMatrix(int n) {
        if (n <= 0) return new int[0][0];
        int[][] res = new int[n][n];
        int m = n, row = 0, col = -1, num = 0;
        while (true) {
            for (int i = 0; i < m; ++i) res[row][++col] = ++num;
            if (--n == 0) break;
            for (int i = 0; i < n; ++i) res[++row][col] = ++num;
            if (--m == 0) break;
            for (int i = 0; i < m; ++i) res[row][--col] = ++num;
            if (--n == 0) break;
            for (int i = 0; i < n; ++i) res[--row][col] = ++num;
            if (--m == 0) break;
        }
        return res;
    }
}
```

