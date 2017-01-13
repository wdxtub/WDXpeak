# Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

For example,

Given height = [2,1,5,6,2,3],

return 10.

## Solution

1. Only calucate area when reaching local maximum value.
2. Keep a non-descending stack. O(n). if the vector height is not allowed to be changed.

## Complexity

时间复杂度 O(n)，空间复杂度 O(n) 或 O(1)

## Code

```java
public class Solution {
    public int largestRectangleArea_1(int[] height) {
        int res = 0;
        for (int i = 0; i < height.length; ++i) {
            if ((i < height.length - 1) && (height[i] <= height[i+1])) {
                continue;
            }
            int minheight = height[i];
            for (int j = i; j >= 0; --j) {
                minheight = Math.min(minheight, height[j]);
                res = Math.max(res, (i-j+1)*minheight);
            }
        }
        return res;
    }
    
    public int largestRectangleArea(int[] height) {
        int res = 0;
        Stack<Integer> stk = new Stack<Integer>();
        int i = 0;
        while (i < height.length) {
            if (stk.isEmpty() == true || (height[i] >= height[stk.peek()])) {
                stk.push(i++);
            } else {
                int idx = stk.pop();
                int width = stk.isEmpty() ? i : (i - stk.peek() - 1);
                res = Math.max(res, width*height[idx]);
            }
        }
        while (stk.isEmpty() == false) {
            int idx = stk.pop();
            int width = stk.isEmpty() ? height.length : (height.length - stk.peek() - 1);
            res = Math.max(res, width*height[idx]);
        }
        return res;
    }
}
```

