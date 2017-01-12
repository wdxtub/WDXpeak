# Max Difference 2 Subarray

最大子数组差

给定一个整数数组，找出两个不重叠的子数组A和B，使两个子数组和的差的绝对值|SUM(A) - SUM(B)|最大。

返回这个最大的差值。

样例

    给出数组[1, 2, -3, 1]，返回 6

注意

    子数组最少包含一个数

挑战

    时间复杂度为O(n)，空间复杂度为O(n)

## Solution

用到了max subarray的技巧，并且分别从左边和右边扫，对于每一个index， 更新res = Math.max(res, Math.max(maxFromRight[i] – minFromLeft[i-1], maxFromLeft[i] – maxFromRight[i-1]));

## Code

```java
public class Solution {
    /**
     * @param nums: A list of integers
     * @return: An integer indicate the value of maximum difference between two
     *          Subarrays
     */
    public int maxDiffSubArrays(ArrayList<Integer> nums) {
        if (nums == null || nums.size() == 0) {
            return 0;
        }
        int[] maxFromLeft = new int[nums.size()];
        int[] minFromLeft = new int[nums.size()];
        int min = nums.get(0);
        int max = min;
        int localmin = min;
        int localmax = max;
        maxFromLeft[0] = minFromLeft[0] = min;
        for (int i = 1; i < nums.size(); i++) {
            localmin = Math.min(nums.get(i), localmin+nums.get(i));
            localmax = Math.max(nums.get(i), localmax+nums.get(i));
            max = Math.max(max, localmax);
            min = Math.min(min, localmin);
            maxFromLeft[i] = max;
            minFromLeft[i] = min;
        }
        min = nums.get(nums.size() - 1);
        max = min;
        localmin = min;
        localmax = max;
        int res = Math.max(max - minFromLeft[nums.size()-2],
                           maxFromLeft[nums.size() - 2] - min);
        for (int i = nums.size() - 2; i > 0; i--) {
            localmin = Math.min(nums.get(i), localmin+nums.get(i));
            localmax = Math.max(nums.get(i), localmax+nums.get(i));
            max = Math.max(max, localmax);
            min = Math.min(min, localmin);
            res = Math.max(res, Math.max(max - minFromLeft[i-1],
                           maxFromLeft[i-1] - min));
        }
        return res;
    }
}
```

