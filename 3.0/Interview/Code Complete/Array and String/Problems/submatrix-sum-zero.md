# Submatrix Sum Zero

给定一个整数矩阵，请找出一个子矩阵，使得其数字之和等于0.输出答案时，请返回左上数字和右下数字的坐标。

样例

    给定矩阵
    [
      [1 ,5 ,7],
      [3 ,7 ,-8],
      [4 ,-8 ,9],
    ]
    返回 [(1,1), (2,2)]

挑战

    O(n^3 ) 时间复杂度。

## Solution

If the matrix is Nx1, we can solve it easily like sum of contiguous subsequense. If it's Nx2, we just need to repeat the same process 3 times --  the first column, the second column and sum of the two columns as an Nx1 array. That's applicable to any cases.

## Complexity

时间复杂度 O(n^3 )，空间复杂度 O(n)

## Code

```java
public class Solution {
    /**
     * @param matrix an integer matrix
     * @return the coordinate of the left-up and right-down number
     */
    public int[][] submatrixSum(int[][] matrix) {
        int[][] res = new int[2][2];
        int m = matrix.length;
        if(m==0) return res;
        int n = matrix[0].length;
        
        
        for(int i=0;i<n;i++){
            int[] sum = new int[m];
            for(int j=i;j<n;j++){
                for(int k=0;k<m;k++)
                    sum[k]+=matrix[k][j]; //traverse every possible combination of indices of each column
                   
                int lastSum=0;
                HashMap<Integer,Integer> map = new HashMap<>();
                map.put(0,-1);
               
                for(int v=0;v<m;v++){
                    lastSum+=sum[v];
                    if(map.containsKey(lastSum)){
                        res[0][0]=map.get(lastSum)+1;
                        res[0][1]=i;
                        res[1][0]=v;
                        res[1][1]=j;
                        return res;
                    }
                    map.put(lastSum,v);
                }
             }
        }
        return res;
    }
}


```

