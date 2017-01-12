# Heapify

给出一个整数数组，堆化操作就是把它变成一个最小堆数组。

对于堆数组A，A[0]是堆的根，并对于每个A[i]，A [i * 2 + 1]是A[i]的左儿子并且A[i * 2 + 2]是A[i]的右儿子。

样例

    给出 [3,2,1,4,5]，返回[1,2,3,4,5] 或者任何一个合法的堆数组

挑战

    O(n)的时间复杂度完成堆化

说明

什么是堆？

+ 堆是一种数据结构，它通常有三种方法：push， pop 和 top。其中，“push”添加新的元素进入堆，“pop”删除堆中最小/最大元素，“top”返回堆中最小/最大元素。

什么是堆化？

+ 把一个无序整数数组变成一个堆数组。如果是最小堆，每个元素A[i]，我们将得到A[i * 2 + 1] >= A[i]和A[i  * 2 + 2] >= A[i]

如果有很多种堆化的结果？

+ 返回其中任何一个。

## Solution

Heapify的基本思路就是：Given an array of N values, a heap containing those values can be built by simply “sifting” each internal node down to its proper location：

1. start with the last internal node
2. swap the current internal node with its smaller child, if necessary
3. then follow the swapped node down
4. continue until all internal nodes are done

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)


## Code 

```java
public class Solution {
    /**
     * @param A: Given an integer array
     * @return: void
     */
    public void heapify(int[] A) {
        int start = A.length/2;
        for (int i=start;i>=0;i--)
            shiftDown(i, A);
    }

    private void shiftDown(int ind, int[] A){
        int size = A.length;
        int left = ind*2+1;
        int right = ind*2+2;
        while (left<size || right<size){
            int leftVal = (left<size) ? A[left] : Integer.MAX_VALUE;
            int rightVal = (right<size) ? A[right] : Integer.MAX_VALUE;
            int next = (leftVal<=rightVal) ? left : right;
            if (A[ind]<A[next]) break;
            else {
                swap(A, ind,next);
                ind = next;
                left = ind*2+1;
                right = ind*2+2;
            }
        }
    }

    private void swap(int[] A, int x, int y){
        int temp = A[x];
        A[x] = A[y];
        A[y] = temp;
    }
}

``` 

