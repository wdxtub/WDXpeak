# Min Adjustment Cost

最小调整代价

给一个整数数组，调整每个数的大小，使得相邻的两个数的差小于一个给定的整数target，调整每个数的代价为调整前后的差的绝对值，求调整代价之和最小是多少。

样例

    对于数组[1, 4, 2, 3]和target=1，最小的调整方案是调整为[2, 3, 2, 3]，调整代价之和是2。返回2。

注意

    你可以假设数组中每个整数都是正整数，且小于等于100。

## Solution

这道题要看出是背包问题，不容易，跟FB一面 paint house很像，比那个难一点

定义res[i][j] 表示前 i个number with 最后一个number是j，这样的minimum adjusting cost

如果第i-1个数是j, 那么第i-2个数只能在[lowerRange, UpperRange]之间，lowerRange=Math.max(0, j-target), upperRange=Math.min(99, j+target),

这样的话，transfer function可以写成：

    for (int p=lowerRange; p<= upperRange; p++) {
    　　res[i][j] = Math.min(res[i][j], res[i-1][p] + Math.abs(j-A.get(i-1)));
    }

## Code

```java
public class Solution {
    /**
     * @param A: An integer array.
     * @param target: An integer.
     */
    public int MinAdjustmentCost(ArrayList<Integer> A, int target) {
        int[][] res = new int[A.size()+1][100];
        for (int j=0; j<=99; j++) {
            res[0][j] = 0;
        }
        for (int i=1; i<=A.size(); i++) {
            for (int j=0; j<=99; j++) {
                res[i][j] = Integer.MAX_VALUE;
                int lowerRange = Math.max(0, j-target);
                int upperRange = Math.min(99, j+target);
                for (int p=lowerRange; p<=upperRange; p++) {
                    res[i][j] = Math.min(res[i][j], res[i-1][p]+Math.abs(j-A.get(i-1)));
                }
            }
        }
        int result = Integer.MAX_VALUE;
        for (int j=0; j<=99; j++) {
            result = Math.min(result, res[A.size()][j]);
        }
        return result;
    }
}

```

