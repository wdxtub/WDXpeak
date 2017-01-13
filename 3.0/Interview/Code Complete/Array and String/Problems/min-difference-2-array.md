# Min Difference 2 Array

给定两个整数数组（第一个是数组 A，第二个是数组 B），在数组 A 中取 A[i]，数组 B 中取 B[j]，A[i] 和 B[j]两者的差越小越好(|A[i] - B[j]|)。返回最小差。

样例

    给定数组 A = [3,4,6,7]， B = [2,3,8,9]，返回 0。

挑战

    时间复杂度 O(n log n)

## Solution

Given the hint of time complexity O(nlogn), we know that we should sort two arrays first, and then, use two pointers going through two arrays. To get the smallest difference, keep the  strategy of moving smaller pointer forward.

## Code

```java
public class Solution {
    /**
     * @param A, B: Two integer arrays.
     * @return: Their smallest difference.
     */
    public int smallestDifference(int[] A, int[] B) {
        Arrays.sort(A);
        Arrays.sort(B);

        int i = 0, j = 0;
        int min = Integer.MAX_VALUE;

        while (i < A.length && j < B.length) {
            min = Math.min(min, Math.abs(A[i] - B[j]));
            if (A[i] <= B[j]) {
                i++;
            } else {
                j++;
            }
        }
        return min;
    }
}
```

