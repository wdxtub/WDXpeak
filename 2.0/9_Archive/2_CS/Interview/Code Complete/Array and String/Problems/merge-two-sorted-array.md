# Merge Two Sorted Array

合并两个排序的整数数组A和B变成一个新的数组。

样例

    给出A=[1,2,3,4]，B=[2,4,5,6]，返回 [1,2,2,3,4,4,5,6]

挑战

    你能否优化你的算法，如果其中一个数组很大而另一个数组很小？

## Solution

自尾部向首部逐个比较两个数组内的元素，取较大的置于新数组尾部元素中。用 python 的话可以非常简单粗暴，直接正着弄就行，注意数组长度的差异可能导致的越界。

如果一个特别大一个特别小，就要考虑二分来进行插入了

## Complexity

时间复杂度 O(n)，空间复杂度 O(n)

## Coding

```python
# python
class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        ai = 0
        bi = 0
        c = []
        for i in range(len(A)+len(B)):
            if ai < len(A) and bi < len(B):
                if A[ai] < B[bi]:
                    c.append(A[ai])
                    ai = ai + 1
                else:
                    c.append(B[bi])
                    bi = bi + 1
            elif ai < len(A) and bi >= len(B):
                c.append(A[ai])
                ai = ai + 1
            elif ai >= len(A) and bi < len(B):
                c.append(B[bi])
                bi = bi + 1
        return c
```

```java
// java
class Solution {
    /**
     * @param A: sorted integer array A which has m elements, 
     *           but size of A is m+n
     * @param B: sorted integer array B which has n elements
     * @return: void
     */
    public void mergeSortedArray(int[] A, int m, int[] B, int n) {
        int i = m-1, j = n-1, index = m + n - 1;
        while (i >= 0 && j >= 0) {
            if (A[i] > B[j]) {
                A[index--] = A[i--];
            } else {
                A[index--] = B[j--];
            }
        }
        while (i >= 0) {
            A[index--] = A[i--];
        }
        while (j >= 0) {
            A[index--] = B[j--];
        }
    }
}
```


