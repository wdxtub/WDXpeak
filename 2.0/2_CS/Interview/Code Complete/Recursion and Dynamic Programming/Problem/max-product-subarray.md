# Max Product Subarray

出处

求出一个序列中乘积最大的连续子序列（至少包含一个数）。

比如, 序列 [2,3,-2,4] 中乘积最大的子序列为 [2,3] ，其乘积为6。

## Solution

用两个变量分别记录乘积的最大值和乘积的最小值.用一个变量记录当前值是否为负数.然后遍历array中的每个数,并累乘起来,更新乘积的最大值和乘积的最小值.

+ 取累乘的数值和当前的数值中大的,存为乘积的最大值
+ 取累乘的数值和当前的数值中小的,存为乘积的最小值

因为:如果当前的数值较大,则前面的都可以抛弃不要,从当前的地方开始继续累乘可能会出现最大值; 如果累乘值较大,则后面可能会继续增大.同理,如果当前值最小,则如果出现一个负数,可能反而会出现最大值.

所以要同时记录最大和最小值!

## Complexity

时间复杂度 O(n)，空间复杂度 O(n)

## Code

```java
public class Solution {
    /**
     * @param nums: an array of integers
     * @return: an integer
     */
    public int maxProduct(int[] nums) {
        int[] max = new int[nums.length];
        int[] min = new int[nums.length];

        min[0] = max[0] = nums[0];
        int result = nums[0];
        for (int i = 1; i < nums.length; i++) {
            min[i] = max[i] = nums[i];
            if (nums[i] > 0) {
                max[i] = Math.max(max[i], max[i - 1] * nums[i]);
                min[i] = Math.min(min[i], min[i - 1] * nums[i]);
            } else if (nums[i] < 0) {
                max[i] = Math.max(max[i], min[i - 1] * nums[i]);
                min[i] = Math.min(min[i], max[i - 1] * nums[i]);
            }

            result = Math.max(result, max[i]);
        }

        return result;
    }
}

```

