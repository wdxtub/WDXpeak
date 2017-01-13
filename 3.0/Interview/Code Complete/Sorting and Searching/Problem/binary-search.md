# Binary Search

给定一个排序的整数数组（升序）和一个要查找的整数 `target`，用`O(logn)`的时间查找到`target`第一次出现的下标（从0开始），如果`target`不存在于数组中，返回`-1`。

## Solution

标准的二分，注意如果找到之后，需要顺着往前再找相同的，以确定第一个出现的下标

## Complexity

时间复杂度 O(logn)，空间复杂度 O(n)

## Code

```python
class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        # write your code here
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] == target:
                while nums[mid] == target:
                    mid = mid - 1
                return mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
```

