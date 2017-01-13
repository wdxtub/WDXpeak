# House Robbery

假设你是一个专业的窃贼，准备沿着一条街打劫房屋。每个房子都存放着特定金额的钱。你面临的唯一约束条件是：相邻的房子装着相互联系的防盗系统，且 当相邻的两个房子同一天被打劫时，该系统会自动报警。

给定一个非负整数列表，表示每个房子中存放的钱， 算一算，如果今晚去打劫，你最多可以得到多少钱 在不触动报警装置的情况下。

样例

给定 [3, 8, 4], 返回 8.

挑战

O(n) 时间复杂度 且 O(1) 存储。

## Solution

dp[i] 表示到当前房屋可能打劫的最大值

用两个变量来代替 dp 中原来要有的数组

dp[i] = max(dp[i - 1], dp[i - 2] + num[i - 1])

## Complexity

O(n) 时间复杂度 且 O(1) 存储。

## Code

```java
public class Solution {
    /**
     * @param A: An array of non-negative integers.
     * return: The maximum amount of money you can rob tonight
     */
    public long houseRobber(int[] A) {
        int length = A.length;
        long even = 0, odd = 0;
        for(int i = 0; i < A.length; i++){
            if(i % 2 == 1){
                odd = Math.max(odd + A[i], even);
            } else {
                even = Math.max(even + A[i], odd);
            }
            
        }
        return Math.max(even, odd);
    }
}
```

