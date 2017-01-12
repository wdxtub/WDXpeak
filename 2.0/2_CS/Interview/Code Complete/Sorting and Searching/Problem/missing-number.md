# Missing Number

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

For example,

Given nums = [0, 1, 3] return 2.

Note:

Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

## Solution

Math formular

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
public class Solution {
    public int missingNumber(int[] nums) {
        int len = nums.length;
        int total = len*(len+1)/2;
        for (int i = 0; i < len; i++){
            total -= nums[i];
        }
        return total;
    }
}
```

