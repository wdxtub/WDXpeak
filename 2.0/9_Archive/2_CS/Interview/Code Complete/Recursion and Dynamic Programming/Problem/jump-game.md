# Jump Game

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:

A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

## Solution

try every reachable index.

## Complexity

时间复杂度 O(n)空间复杂度 O(1)

## Code

```java
public class Solution {
    public boolean canJump(int[] A) {
        int pos = 0, n = A.length;
        for (int i = 0; i < n; ++i) {
            if (pos >= i) {
                pos = Math.max(pos, i + A[i]);
            }
        }
        return pos >= n - 1;
    }
}
```

