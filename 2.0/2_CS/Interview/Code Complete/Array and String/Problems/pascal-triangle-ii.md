# Pascal's Triangle II

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,

Return [1,3,3,1].

Note:

Could you optimize your algorithm to use only O(k) extra space?

## Solution

from back to forth...

## Complexity

时间复杂度 O(n^2 )，空间复杂度 O(n)

## Code

```java
public class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> res = new ArrayList<Integer>();
        res.add(1);
        for (int i = 1; i <= rowIndex; ++i) {
            for (int j = i - 1; j >= 1; --j) {
                res.set(j,res.get(j) + res.get(j-1));
            }
            res.add(1);
        }
        return res;
    }
}
```

