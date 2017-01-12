# 3 Sum Closest

出处

Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

## Solution

Similar to 3Sum, taking O(n^2) time complexity.

固定一个，指针左右动

## Complexity

时间复杂度 O(n^2 )，空间复杂度 O(1)

## Code

```java
public class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int N = nums.length;
        if (N < 3) return 0;
        int res = nums[0] + nums[1] + nums[2];
        Arrays.sort(nums);
        for (int i = 0; i < N-2; ++i)
        {
            int l = i + 1, r = N - 1;
            while (l < r)
            {
                int threesum = nums[i] + nums[l] + nums[r];
                if (threesum == target) return target;
                else if (threesum < target) ++l;
                else --r;
                if (Math.abs(threesum - target) < Math.abs(res - target))
                    res = threesum;
            }
        }
        return res;
    }
}


