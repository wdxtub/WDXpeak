# Coin Game

有 n 个硬币排成一条线。两个参赛者轮流从右边依次拿走 1 或 2 个硬币，直到没有硬币为止。拿到最后一枚硬币的人获胜。

请判定 第一个玩家 是输还是赢？

样例

    n = 1, 返回 true.
    n = 2, 返回 true.
    n = 3, 返回 false.
    n = 4, 返回 true.
    n = 5, 返回 true.

挑战

    O(1) 时间复杂度且O(1) 存储。

## Solution

递推一下即可找到规律，除了被三整除的数会输之外，其他都不会输

## Code

```java
public class Solution {
    /**
     * @param n: an integer
     * @return: a boolean which equals to true if the first player will win
     */
    public boolean firstWillWin(int n) {
        if (n % 3 == 0){
            return false;
        }
        else {
            return true;
        }
    }
}

```

