# K Sum II

给定 n 个不同的正整数，整数 k（1<= k <= n）以及一个目标数字。　　　　

在这 n 个数里面找出 K 个数，使得这 K 个数的和等于目标数字，你需要找出所有满足要求的方案。

样例

    给出[1,2,3,4]，k=2， target=5，返回 [[1,4],[2,3]]

## Solution

同Combination Sum II

## Complexity

时间复杂度 O(2^n )

## Code

```java
public class Solution {
    /**
     * @param A: an integer array.
     * @param k: a positive integer (k <= length(A))
     * @param target: a integer
     * @return a list of lists of integer
     */
    public ArrayList<ArrayList<Integer>> kSumII(int A[], int k, int target) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> path = new ArrayList<Integer>();
        helper(res, path, A, k, target, 0);
        return res;
    }

    public void helper(ArrayList<ArrayList<Integer>> res, ArrayList<Integer> path, int[] A, int k, int remain, int index) {
        if (path.size() == k) {
            if (remain == 0) {
                res.add(new ArrayList<Integer>(path));
            }
            return;
        }
        for (int i=index; i<A.length; i++) {
            path.add(A[i]);
            helper(res, path, A, k, remain-A[i], i+1);
            path.remove(path.size()-1);
        }
    }
}


```

