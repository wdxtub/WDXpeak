# Maximal Rectangle

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.

## Solution & Complexity

1. dp. 
    + dp[i][j] records the number of consecutive '1' on the left and up of the element matrix[i][j].
    + For each element(i,j), calculate the area of rectangle including the element itself.
2. calculate 'Largest Rectangle in Histogram' for each row.
3. Time : O(n ^ 2), Space : O(n).

## Code 

```java
public class Solution {
    public int maximalRectangle_1(char[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return 0;
        int M = matrix.length, N = matrix[0].length;
        int[][][] dp = new int[M][N][2];
        int res = 0;
        for (int i = 0; i < M; ++i) {
            for (int j = 0; j < N; ++j) {
                if (matrix[i][j] == '0') continue;
                dp[i][j][0] = (j==0)?1:dp[i][j-1][0] + 1;
                dp[i][j][1] = (i==0)?1:dp[i-1][j][1] + 1;
                int minheight = dp[i][j][1];
                for (int k = j; k > j - dp[i][j][0]; --k) {
                    minheight = Math.min(minheight, dp[i][k][1]);
                    res = Math.max(res, minheight*(j-k+1));
                }
            }
        }
        return res;
    }
    
    public int cal(int[] dp) {
        int N = dp.length;
        Stack<Integer> stk = new Stack<Integer>();
        int i = 0, res = 0;
        while (i < N) {
            if (stk.empty() || dp[i] >= dp[stk.peek()]) {
                stk.push(i++);
                continue;
            }
            int idx = stk.pop();
            int width = stk.empty()?i:(i-stk.peek()-1);
            res = Math.max(res, width*dp[idx]);
        }
        return res;
    }
    public int maximalRectangle_2(char[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return 0;
        int M = matrix.length, N = matrix[0].length;
        int[] dp = new int[N+1];
        int res = 0;
        for (int i = 0; i < M; ++i) {
            for (int j = 0; j < N; ++j) {
                if (matrix[i][j] == '0') dp[j] = 0;
                else dp[j] = dp[j] + 1;
            }
            res = Math.max(res, cal(dp));
        }
        return res;
    }
    
    public int maximalRectangle(char[][] matrix) {
        if (matrix.length == 0 || matrix[0].length == 0) return 0;
        int M = matrix.length, N = matrix[0].length;
        int[] L = new int[N]; Arrays.fill(L,0);
        int[] R = new int[N]; Arrays.fill(R,N);
        int[] H = new int[N]; Arrays.fill(H,0);
        int res = 0;
        for (int i = 0; i < M; ++i) {
            int left = 0, right = N;
            for (int j = 0; j < N; ++j) {
                if (matrix[i][j] == '1') {
                    L[j] = Math.max(L[j], left);
                    H[j] = H[j] + 1;
                } else {
                    H[j] = 0; L[j] = 0; R[j] = N;
                    left = j + 1;
                }
            }
            for (int j = N - 1; j >= 0; --j) {
                if (matrix[i][j] == '1') {
                    R[j] = Math.min(R[j], right);
                    res = Math.max(res, (R[j]-L[j])*H[j]);
                } else {
                    right = j;
                }
            }
        }
        return res;
    }
}
```

