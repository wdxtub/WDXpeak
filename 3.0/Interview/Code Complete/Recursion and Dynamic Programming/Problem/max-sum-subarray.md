# Maximum Subarray

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],

the contiguous subarray [4,−1,2,1] has the largest sum = 6.

## Solution

dp

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
public class Solution {
    public int maxSubArray_1(int[] A) {
        if (A.length == 0) return 0;
        int minVal = Math.min(A[0],0), res = A[0], sum = A[0];
        for (int i = 1; i < A.length; ++i) {
            sum += A[i];
            res = Math.max(res, sum - minVal);
            minVal = Math.min(minVal, sum);
        }
        return res;
    }
    
    public int maxSubArray_2(int[] A) {
        if (A.length == 0) return 0;
        int dp = A[0], res = A[0];
        for (int i = 1; i < A.length; ++i) {
            dp = Math.max(A[i], dp + A[i]);
            res = Math.max(res, dp);
        }
        return res;
    }
}
```

