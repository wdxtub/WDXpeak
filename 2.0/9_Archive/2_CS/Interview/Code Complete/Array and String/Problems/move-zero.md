# Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:

1. You must do this in-place without making a copy of the array.
2. Minimize the total number of operations.

## Solution

维护两个 index，一个遍历，一个用来交换值

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
public class Solution {
    public void moveZeroes(int[] nums) {
        int i = -1, j = 0;
        while (j < nums.length) {
            if (nums[j] != 0) {
                swap(++i, j, nums);
            }
            j++;
        }
    }
    
    public void swap(int i, int j, int[] nums) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
```

