# Rotate Image

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:

Could you do this in-place?

## Solution

Method 1

```
123   ->  147   ->   741    (preferable)
456       258        852
789       369        963
```
 
Method 2

Rotate one-fourth of the image clockwise.

## Complexity

时间复杂度 O(n^2 )，空间复杂度 O(1)

## Code

```java
public class Solution {
    public void rotate_1(int[][] matrix) {
        int n = matrix.length;
        if (n <= 1) return;
        for(int i=0;i<n;i++){
            for(int j=0;j<i;j++){
                int tmp = matrix[i][j];
                matrix[i][j]=matrix[j][i];
                matrix[j][i]=tmp;
            }
        }
        
        for(int i=0;i<n;i++){
            for(int j=0;j<n/2;j++){
                int tmp = matrix[i][j];
                matrix[i][j]=matrix[i][n-1-j];
                matrix[i][n-1-j] = tmp;
            }
        }
    }
    public void rotate_2(int[][] matrix) {
        int n = matrix.length;
        if (n <= 1) return;
        int level = 0;
        while (level < n / 2) {
            for (int i = level; i < n - 1 - level; ++i) {
                int tmp = matrix[i][level];
                matrix[i][level] = matrix[n - 1 - level][i];
                matrix[n - 1 - level][i] = matrix[n - 1 - i][n - 1 - level];
                matrix[n - 1 - i][n - 1 - level] = matrix[level][n - 1 - i];
                matrix[level][n - 1 - i] = tmp;
            }
            ++level;
        }
    }
}
```

---

```java
public static void rotate(int[][] mat, int n){
    for (int layer = 0; layer < n/2; layer++){
        int first = layer;
        int last = n - 1 - layer;
        for (int i = first; i < last; i++){
            int offset = i - first;
            // save top
            int top = matrix[first][i];
            // left -> top
            matrix[first][i] = matrix[last-offset][first];
            // bottom -> left
            matrix[last-offset][first] = matrix[last][last-offset];
            // right -> bottom
            matrix[last][last-offset] = matrix[i][last];
            // top -> right
            matrix[i][last] = top;
        }
    }
}

public static void rotateinv(int[][] mat, int n){
    for (int layer = 0; layer < n/2; layer++){
        int first = layer;
        int last = n - 1 - layer;
        for (int i = first; i < last; i++){
            int offset = i - first;
            // save top
            int top = matrix1[first][i];
            // right -> top
            matrix1[first][i] = matrix1[i][last];
            // bottom -> right
            matrix1[i][last] = matrix1[last][last-offset];
            // left -> bottom
            matrix1[last][last-offset] = matrix1[last - offset][first];
            // top -> right
            matrix1[last-offset][first] = top;
        }
    }
}
```

