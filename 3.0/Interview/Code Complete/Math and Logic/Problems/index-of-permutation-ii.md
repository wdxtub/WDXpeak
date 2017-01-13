# Index of Permutation II

给出一个可能包含重复数字的排列，求这些数字的所有排列按字典序排序后该排列在其中的编号。编号从1开始。

样例

    给出排列[1, 4, 2, 2]，其编号为3。

## Solution

这里需要考虑重复元素，有无重复元素最大的区别在于原来的1!, 2!, 3!...等需要除以重复元素个数的阶乘，颇有点高中排列组合题的味道。记录重复元素个数同样需要动态更新，引入哈希表这个万能的工具较为方便。

## Complexity

时间复杂度 O(n^2 )，空间复杂度 O(n)
## Code

```java
public class Solution {
    /**
     * @param A an integer array
     * @return a long integer
     */
    public long permutationIndexII(int[] A) {
        if (A == null || A.length == 0) return 0;

        long index = 1;
        long factor = 1;
        for (int i = A.length - 1; i >= 0; i--) {
            HashMap<Integer, Integer> hash = new HashMap<Integer, Integer>();
            hash.put(A[i], 1);
            int rank = 0;
            for (int j = i + 1; j < A.length; j++) {
                if (hash.containsKey(A[j])) {
                    hash.put(A[j], hash.get(A[j]) + 1);
                } else {
                    hash.put(A[j], 1);
                }

                if (A[i] > A[j]) {
                    rank++;
                }
            }
            index += rank * factor / dupPerm(hash);
            factor *= (A.length - i);
        }

        return index;
    }

    private long dupPerm(HashMap<Integer, Integer> hash) {
        if (hash == null || hash.isEmpty()) return 1;

        long dup = 1;
        for (int val : hash.values()) {
            dup *= fact(val);
        }

        return dup;
    }

    private long fact(int num) {
        long val = 1;
        for (int i = 1; i <= num; i++) {
            val *= i;
        }

        return val;
    }
}

```

