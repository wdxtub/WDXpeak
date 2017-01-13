# Remove Element

Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

## Solution

Use two pointers.

## Code

```java
public class Solution {
    public int removeElement(int[] nums, int val) {
        int N = nums.length;
        int idx = 0;
        for (int i = 0; i < N; ++i) {
            if (nums[i] != val) {
                nums[idx++] = nums[i];
            }
        }
        return idx;
    }
}
```

