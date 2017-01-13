# Package Problem

出处

在n个物品中挑选若干物品装入背包，最多能装多满？假设背包的大小为m，每个物品的大小为A[i]

样例

    如果有4个物品[2, 3, 5, 7]
    如果背包的大小为11，可以选择[2, 3, 5]装入背包，最多可以装满10的空间。
    如果背包的大小为12，可以选择[2, 3, 7]装入背包，最多可以装满12的空间。
    函数需要返回最多能装满的空间大小。

注意

    你不可以将物品进行切割。


## Solution

The problem does not care how many items you can put in the backpack, it cares how you can choose the proper combination of items to fully fill the backpack.

We create a boolean array full[n + 1][m + 1], with full[i][j] indicating whether items in A[0] … A[i] could fulfill the backpack with size j.

## Complexity

时间复杂度 O(n^2 )，空间复杂度 O(n)

## Code

```java
public class Solution {
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A: Given n items with size A[i]
     * @return: The maximum size
     */
    public int backPack(int m, int[] A) {
        if (A == null || A.length == 0) {
            return 0;
        }
        boolean full[] = new boolean[m + 1];
        boolean lastFull[] = new boolean[m + 1];
        full[0] = true;
        for (int i = 0; i < A.length; i++) {
            System.arraycopy(full, 0, lastFull, 0, m + 1);
            for (int size = 1; size <= m; size++) {
                if (size >= A[i] && lastFull[size - A[i]]) {
                    full[size] = true;
                } else {
                    full[size] = lastFull[size];
                }
            }
        }
        for (int size = m; size >= 1; size--) {
            if (full[size]) {
                return size;
            }
        }
        return 0;
    }
}

```

