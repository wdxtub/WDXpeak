# Min Triangle Path Sum

给定一个数字三角形，找到从顶部到底部的最小路径和。每一步可以移动到下面一行的相邻数字上。

样例

    比如，给出下列数字三角形：
    [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
    从顶到底部的最小路径和为11 ( 2 + 3 + 5 + 1 = 11)。

注意

    如果你只用额外空间复杂度O(n)的条件下完成可以获得加分，其中n是数字三角形的总行数。

## Solution

It’s an easy question. Instead of normal DP transition function, this one is so-called bottom-up approach.

其实就是包括所有情况的累加，逐层分析就可以明白，其中 `m[0]` 指的是最左边元素的和，`m[j]` 是最右边元素的和，中间的通过比较选最小值

## Code

```java
public class Solution {
    /**
     * @param triangle: a list of lists of integers.
     * @return: An integer, minimum path sum.
     */
    public int minimumTotal(ArrayList<ArrayList<Integer>> triangle) {
        int len = triangle.size();
        if (len == 0) return 0;
        int[] m = new int[len];
        m[0] = triangle.get(0).get(0);
        for (int i = 1; i < len; i ++) {
            ArrayList<Integer> cur = triangle.get(i);
            for (int j = i; j >= 0; j --) {
                if (j == i) m[j] = m[j-1] + cur.get(j);
                else if (j == 0) m[j] = m[0] + cur.get(0);
                else m[j] = Math.min(m[j-1], m[j]) + cur.get(j);
            }
        }
        int min = Integer.MAX_VALUE;
        for (Integer k: m)
            min = Math.min(min, k);
        return min;
    }
}
```

