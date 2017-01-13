# Find Peak Element

A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

Note:

Your solution should be in logarithmic complexity.

## Solution

由时间复杂度的暗示可知应使用二分搜索。

首先分析若使用传统的二分搜索，若A[mid] > A[mid - 1] && A[mid] < A[mid + 1]，则找到一个peak为A[mid]；若A[mid - 1] > A[mid]，则A[mid]左侧必定存在一个peak，可用反证法证明：若左侧不存在peak，则A[mid]左侧元素必满足A[0] > A[1] > ... > A[mid -1] > A[mid]，与已知A[0] < A[1]矛盾，证毕。同理可得若A[mid + 1] > A[mid]，则A[mid]右侧必定存在一个peak。如此迭代即可得解。

## Complexity

时间复杂度 O(logn)，空间复杂度 O(1)

## Code

```java
public class Solution {
    public int findPeakElement(int[] num) {
        int left = 0, right = num.length - 1, mid = -1;
        while (left <= right) {
            mid = (left + right) /2;
            if ((mid == 0 || num[mid-1] <= num[mid]) && (mid == num.length - 1 || num[mid] >= num[mid+1]))
                return mid;
            if (mid > 0 && num[mid-1] > num[mid]) {
                right = mid - 1;
            } else if (num[mid+1] > num[mid]) {
                left = mid + 1;
            }
        }
        return mid;
    }
}
```

