# Pascal's Triangle

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,

Return

    [
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
    ]

## Solution

根据题意进行累加

## Complexity

时间复杂度 O(n^2 )，空间复杂度 O(n^2 )

## Code

```java
public class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if (numRows < 1) return res;
        List<Integer> temp = new ArrayList<Integer>();
        temp.add(1);
        res.add(temp);
        for (int i = 1; i < numRows; ++i) {
            List<Integer> t = new ArrayList<Integer>();
            t.add(1); 
            for (int j = 1; j < i; ++j) {
                t.add(res.get(i-1).get(j-1) + res.get(i-1).get(j));
            }
            t.add(1);
            res.add(t);
        }
        return res;
    }
}
```

