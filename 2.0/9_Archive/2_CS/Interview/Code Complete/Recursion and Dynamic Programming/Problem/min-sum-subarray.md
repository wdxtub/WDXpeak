# Min Sum Subarray

给定一个整数数组，找到一个具有最小和的子数组。返回其最小和。

样例

    给出数组[1, -1, -2, 1]，返回 -3

注意

    子数组最少包含一个数字

## 题解

Greedy.

1. Initialize sum = 0, `min_sum = MAX_INT`
2. for each num n, sum + n, check sum with min_sum
3. if sum > 0, no need to keep it, reset sum to 0.

Time complexity = O(n)

```java
public class Solution {
    /**
     * @param nums: a list of integers
     * @return: A integer indicate the sum of minimum subarray
     */
    public int minSubArray(ArrayList<Integer> nums) {
        int len = nums.size();
        if (len==0) return 0;

        int curMin = nums.get(0);
        int minRes = nums.get(0);

        for (int i=1;i<len;i++){
            curMin = Math.min(nums.get(i),curMin+nums.get(i));
            minRes = Math.min(curMin,minRes);
        }
        return minRes;
    }
}


```

