# Index of Permuation

给出一个不含重复数字的排列，求这些数字的所有排列按字典序排序后该排列的编号。其中，编号从1开始。

样例

    例如，排列[1,2,4]是第1个排列。

## Solution

以序列1, 2, 4为例，其不同的排列共有 3!=6 种，以排列[2, 4, 1]为例，若将1置于排列的第一位，后面的排列则有 2!=2 种。将2置于排列的第一位，由于[2, 4, 1]的第二位4在1, 2, 4中为第3大数，故第二位可置1或者2，那么相应的排列共有 2 * 1! = 2种，最后一位1为最小的数，故比其小的排列为0。综上，可参考我们常用的十进制和二进制的转换，对于[2, 4, 1], 可总结出其排列的index为2! * (2 - 1) + 1! * (3 - 1) + 0! * (1 - 1) + 1.

以上分析看似正确无误，实则有个关键的漏洞，在排定第一个数2后，第二位数只可为1或者4，而无法为2, 故在计算最终的 index 时需要动态计算某个数的相对大小。按照从低位到高位进行计算，我们可通过两重循环得出到某个索引处值的相对大小。

## Complexity

时间复杂度 O(n)，空间复杂度 O(1）

## Code

```java
public class Solution {
    /**
     * @param A an integer array
     * @return a long integer
     */
    public long permutationIndex(int[] A) {
        if (A == null || A.length == 0) return 0;

        long index = 1;
        long factor = 1;
        for (int i = A.length - 1; i >= 0; i--) {
            int rank = 0;
            for (int j = i + 1; j < A.length; j++) {
                if (A[i] > A[j]) rank++;
            }
            index += rank * factor;
            factor *= (A.length - i);
        }

        return index;
    }
}

```

