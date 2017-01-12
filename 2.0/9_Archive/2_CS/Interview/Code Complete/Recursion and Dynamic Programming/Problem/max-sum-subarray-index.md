# Max Sum Subarray Index

给定一个整数数组，请找出一个连续子数组，使得该子数组的和最大。输出答案时，请分别返回第一个数字和最后一个数字的值。（如果两个相同的答案，请返回其中任意一个）

样例

    给定 [-3, 1, 3, -3, 4], 返回[1,4].

## Solution

和最大子数组类似，只是这个要记录下标，最大子数组是求和

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
public class Solution {
    /**
     * @param A an integer array
     * @return  A list of integers includes the index of the first number and the index of the last number
     */
    public ArrayList<Integer> continuousSubarraySum(int[] A) {
        ArrayList<Integer> res = new ArrayList<Integer>();
        if (A == null || A.length == 0) {
            return res;
        }
        int sum = A[0];
        int max = sum;
        int start = 0, end = 0;
        res.add(0);
        res.add(0);
        for (int i = 1; i < A.length; i++) {
            if (sum > max) {
                res.set(0, start);
                res.set(1, i-1);
                max = sum;
            }
            if (sum < 0) {
                sum = 0;
                start = i;
                end = i;
            }
            sum += A[i];
        }
        if (sum > max) {
            res.set(0, start);
            res.set(1, A.length-1);
        }
        return res;
    }
}

```

