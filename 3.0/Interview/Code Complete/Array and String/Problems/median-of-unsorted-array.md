# Median of Unsorted Array

给定一个未排序的整数数组，找到其中位数。

中位数是排序后数组的中间值，如果数组的个数是偶数个，则返回排序后数组的第N/2个数。

样例

    给出数组[4, 5, 1, 2, 3]， 返回 3
    给出数组[7, 9, 4, 5]，返回 5

挑战

    时间复杂度为O(n)

## Solution

这一题比较简单，就是判断一个奇偶性，然后排序即可，注意下标是从零开始的

## Code

```python
class Solution:
    """
    @param nums: A list of integers.
    @return: An integer denotes the middle number of the array.
    """
    def median(self, nums):
        # write your code here
        l = len(nums)
        nums.sort()

        if l % 2 == 0:
            return nums[l / 2 - 1]
        else:
            return nums[l / 2]
```

