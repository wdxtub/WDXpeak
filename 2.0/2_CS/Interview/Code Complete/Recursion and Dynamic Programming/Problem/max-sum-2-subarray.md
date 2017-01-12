# Max Sum 2 Subarray

给定一个整数数组，找出两个不重叠子数组使得它们的和最大。

每个子数组的数字在数组中的位置应该是连续的。

返回最大的和。

样例

    给出数组[1, 3, -1, 2, -1, 2]，这两个子数组分别为[1, 3]和[2, -1, 2]或者[1, 3, -1, 2]和[2]，它们的最大和都是7

注意

    子数组最少包含一个数

挑战

    要求时间复杂度为O(n)

## Solution

类似max subarray I的解法，区别是我们这里扫两遍，从左边向右边的时候算出globalmax，从右边向左边的时候算出localMax，然后找两边加起来的最大值。首先我们定义两个变量，localMax[i]为以i结尾的subarray中最大的值，globalMax[i]定义为[0, i]范围中最大的subarray(subarray不一定需要以i结尾)。递推表达式是：

+ localMax[i] = max(localMax[i - 1] + A[i], A[i]);
+ globalMax[i] = max(globalMax[i - 1], localMax[i]);

从右边向左边的时候维护localMax[i]，这时的localMax[i]指的是以i开头的最大的subarray

+ localMax[i] = max(localMax[i + 1] + A[i], A[i]);

扫两遍，时间复杂度O(n)，空间复杂度O(n)，从右边向左边扫的时候不需要开辟一个新的数组，并且计算最后最大值可以在第二次循环的时候一起做了

## Code

```java
public class Solution {
    /**
     * @param nums: A list of integers
     * @return: An integer denotes the sum of max two non-overlapping subarrays
     */
    public int maxTwoSubArrays(ArrayList<Integer> nums) {
        if (nums == null)
            return 0;
        int len = nums.size(), currSum = 0;
        int[] left = new int[len];
        for (int i = 0; i < len - 1; i++) {
            int sum = currSum + nums.get(i);
            if (i == 0)
                left[i + 1] = sum;
            else
                left[i + 1] = sum > left[i]? sum: left[i];
            currSum = sum <= 0? 0: sum;
        }
        currSum = 0;
        int max = Integer.MIN_VALUE;
        for (int i = len - 1; i > 0; i--) {
            int sum = currSum + nums.get(i);
            if (sum + left[i] > max)
                max = sum + left[i];
            currSum = sum <= 0? 0: sum;
        }
        return max;
    }
}
```

