# Fibonacci

查找斐波纳契数列中第 N 个数。

所谓的斐波纳契数列是指：

+ 前2个数是 0 和 1 。
+ 第 i 个数是第 i-1 个数和第i-2 个数的和。

斐波纳契数列的前10个数字是：0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...

样例

    给定 1，返回 0
    给定 2，返回 1
    给定 10，返回 34
    
## Solution

动规思想，简化为 O(1)

## Complexity

时间复杂度 O(1)，空间复杂度 O(1)

## Code

```java
class Solution {
    /**
     * @param n: an integer
     * @return an integer f(n)
     */
    public int fibonacci(int n) {
        if(n <= 2) return n - 1;
        int pre = 0, cur = 1;
        for(int i = 3; i <= n; i++){
            int temp = cur;
            if(Integer.MAX_VALUE - pre < cur) return Integer.MAX_VALUE;
            cur = pre +cur;
            pre = temp;
        }
        return cur;
    }
}
```

