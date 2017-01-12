# Container with Most Water

出处

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container.

## Solution

From both sides to the center.

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
public class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int res = 0;
        while (left < right) {
            res = Math.max(res, 
                    Math.min(height[left],height[right]) * (right - left));
            if (height[left] > height[right]) --right;
            else ++left;
        }
        return res;
    }
}
```

