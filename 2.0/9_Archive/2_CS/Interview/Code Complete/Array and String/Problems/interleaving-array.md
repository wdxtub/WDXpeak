# Interleaving Array

给出一个含有正整数和负整数的数组，重新排列成一个正负数交错的数组。

样例

    给出数组[-1, -2, -3, 4, 5, 6]，重新排序之后，变成[-1, 5, -2, 4, -3, 6]或者其他任何满足要求的答案

注意

    不需要保持正整数或者负整数原来的顺序。

挑战

    原地完成，没有额外的空间

## Solution

这道题没有给出正数、负数谁多谁少，所以需要先统计数量，数量多的要包着数量少的，然后数组尾部全是数量多的数

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
class Solution {
    /**
     * @param A: An integer array.
     * @return: void
     */
    public void rerange(int[] A) {
        int posNum = 0, negNum = 0;
        for (int elem : A) {
            if (elem < 0) {
                negNum++;
            }
            else {
                posNum++;
            }
        }
        int posInd = 1, negInd = 0;
        if (posNum > negNum) {
            negInd = 1;
            posInd = 0;
        }
        while (posInd<A.length && negInd<A.length) {
            while (posInd < A.length && A[posInd] > 0) {
                posInd += 2;
            }
            while (negInd < A.length && A[negInd] < 0) {
                negInd += 2;
            }
            if (posInd<A.length && negInd<A.length) {
                swap(A, posInd, negInd);
            }
        }
        return ;
   }

   public void swap(int[] A, int l, int r) {
       int temp = A[l];
       A[l] = A[r];
       A[r] = temp;
   }
}
``` 

