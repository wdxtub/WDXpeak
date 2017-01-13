# Sorted Two Sorted Array II

合并两个排序的整数数组A和B变成一个新的数组。

样例

    给出A = [1, 2, 3, empty, empty] B = [4,5]
    合并之后A将变成[1,2,3,4,5]

注意

    你可以假设A具有足够的空间（A数组的大小大于或等于m+n）去添加B中的元素。

## Solution

在上题的基础上加入了in-place的限制。将上题的新数组视为length相对较大的数组即可，仍然从数组末尾进行归并，取出较大的元素。

## Complexity

时间复杂度 O(n)，空间复杂度 O(n)

## Code

```python
class Solution:
    """
    @param A: sorted integer array A which has m elements,
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        # resize nums1 to required size
        A += [0] * (n + m - len(A))
        index = m + n
        while m > 0 and n > 0:
            if A[m - 1] > B[n - 1]:
                index -= 1
                m -= 1
                A[index] = A[m]
            else:
                index -= 1
                n -= 1
                A[index] = B[n]

        while n > 0:
            index -= 1
            n -= 1
            A[index] = B[n]
```

