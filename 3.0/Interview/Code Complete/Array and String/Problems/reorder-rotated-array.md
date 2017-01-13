# Reorder Rotated Array

给定一个旋转排序数组，在原地恢复其排序。

样例

    [4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]

挑战

    使用O(1)的额外空间和O(n)时间复杂度

说明

    什么是旋转数组？
    比如，原始数组为[1,2,3,4], 则其旋转数组可以是[1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]

## Solution

首先找到分割点，随后分三步调用翻转函数。

## Complexity

时间复杂度 O(n)，哦那感觉复杂度 O(1)

## Code

```python
class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                self.recover(nums, 0, i)
                self.recover(nums, i+1, len(nums)-1)
                self.recover(nums, 0, len(nums) -1)
        return

    def recover(self, nums, start, end):
        i, j = start, end
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i = i + 1
            j = j - 1
        return nums
```

