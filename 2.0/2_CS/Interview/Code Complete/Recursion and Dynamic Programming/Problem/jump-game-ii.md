# Jump Game II

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:

Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

## Solution

Jump to the position where we can jump farthest (index + A[index]) next time.

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
public class Solution {
    public int jump(int[] A) {
        int n = A.length;
        int last = 0, cur = 0, res = 0;
        for (int i = 0; i < n; ++i) {
            if (i > last) {
                res++;
                last = cur;
                if (cur >= n - 1) return res;
            }
            cur = Math.max(cur, i + A[i]);
        }
        return res;
    }
}
```

