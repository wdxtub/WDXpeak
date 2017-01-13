# Remove Duplicates from Sorted Array II

Follow up for "Remove Duplicates":

What if duplicates are allowed at most twice?

For example,

Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.

## Solution

按照题意即可

## Code

```java
public class Solution {
    public int removeDuplicates(int[] A) {
        int N = A.length;
        if (N <= 2) return N;
        int idx = 2;
        for (int i = 2; i < N; ++i) {
            if (A[i] != A[idx-2])
                A[idx++] = A[i];
        }
        return idx;
    }
}
```

