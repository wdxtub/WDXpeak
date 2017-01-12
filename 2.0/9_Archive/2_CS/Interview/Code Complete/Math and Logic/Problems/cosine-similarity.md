# Cosine Similarity

出处

Cosine similarity is a measure of similarity between two vectors of an inner product space that measures the cosine of the angle between them. The cosine of 0° is 1, and it is less than 1 for any other angle.

Given two vectors A and B with the same size, calculate the cosine similarity.

Return 2.0000 if cosine similarity is invalid (for example A = [0] and B = [0]).

样例

    Given A = [1, 2, 3], B = [2, 3 ,4].
    Return 0.9926.
    Given A = [0], B = [0].
    Return 2.0000

## Solution

依照题意计算即可

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
class Solution {
    /**
     * @param A: An integer array.
     * @param B: An integer array.
     * @return: Cosine similarity.
     */
    public double cosineSimilarity(int[] A, int[] B) {
        if ( A.length != B.length){
            return 2.0000;
        }

        double up = 0.0;
        double down1 = 0.0;
        double down2 = 0.0;

        for (int i = 0; i < A.length; i++){
            up += A[i] * B[i];
            down1 += A[i] * A[i];
            down2 += B[i] * B[i];
        }

        if (down1 == 0 || down2 == 0){
            return 2.0000;
        }

        return up / (Math.sqrt(down1*down2));
    }
}
```

