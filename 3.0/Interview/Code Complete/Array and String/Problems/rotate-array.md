# Rotate Array

Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to [5,6,7,1,2,3,4].

Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.

Hint:

Could you do it in-place with O(1) extra space?

Related problem: Reverse Words in a String II

## Solution

Can we do this in O(1) space and in O(n) time? The following solution does.

Assuming we are given {1,2,3,4,5,6} and order 2. The basic idea is:

1. Divide the array two parts: 1,2,3,4 and 5, 6
2. Rotate first part: 4,3,2,1,5,6
3. Rotate second part: 4,3,2,1,6,5
4. Rotate the whole array: 5,6,1,2,3,4

## Code

```java
public class Solution {
    public void rotate(int[] nums, int k) {
        int len = nums.length;
        k %= len;
        reverse(nums, 0, len-1);
        reverse(nums, 0, k-1);
        reverse(nums, k, len-1);
    }
    
    public void reverse(int[] nums, int l, int r) {
        while (l <= r) {
            int temp = nums[l];
            nums[l] = nums[r];
            nums[r] = temp;
            l++;
            r--;
        }
    }
}
```

