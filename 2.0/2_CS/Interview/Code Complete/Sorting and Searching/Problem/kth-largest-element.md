# Kth Largest Element

在数组中找到第k大的元素

样例

    给出数组[9,3,2,4,8]，第三大的元素是4
    给出数组 [1,2,3,4,5]，第一大的元素是5，第二大的元素是4，第三大的元素是3，以此类推

注意

    你可以交换数组中的元素的位置

挑战

    要求时间复杂度为O(n），空间复杂度为O(1）

## Solution

Quickselect uses the same overall approach as quicksort, choosing one element as a pivot and partitioning the data in two based on the pivot, accordingly as less than or greater than the pivot. However, instead of recursing into both sides, as in quicksort, quickselect only recurses into one side – the side with the element it is searching for. This reduces the average complexity from O(n log n) (in quicksort) to O(n) (in quickselect).

下面这个code几个注意的地方：

1. 第8行 `Kth largest element = len-K+1` th smallest element

2. 第24行，l、r在相遇之后，l 所处的位置就是第一个大于等于pivot元素所在位置，把它跟pivot交换，pivot就放在了它应该在的位置

## Complexity

时间复杂度为O(n），空间复杂度为O(1）

1. sort O(nlogn)
2. quickselect O(n)

## Code

```java
class Solution {
    //param k : description of k
    //param numbers : array of numbers
    //return: description of return
    public int kthLargestElement(int k, ArrayList<Integer> numbers) {
        if (k > numbers.size())
            return 0;
        return helper(numbers.size()-k+1, numbers, 0, numbers.size()-1);
    }

    public int helper(int k, ArrayList<Integer> numbers, int start, int end) {
        int l=start, r=end;
        int pivot = end;
        while (true) {
            while (numbers.get(l)<numbers.get(pivot) && l<r) {
                l++;
            }
            while (numbers.get(r)>=numbers.get(pivot) && l<r) {
                r--;
            }
            if (l == r) break;
            swap(numbers, l, r);
        }
        swap(numbers, l, end);  // l here is the first one which is bigger than pivot, swap it with the pivot
        if (l+1 == k) return numbers.get(l);
        else if (l+1 < k) return helper(k, numbers, l+1, end);
        else return helper(k, numbers, start, l-1);
    }

    public void swap(ArrayList<Integer> numbers, int l, int r) {
        int temp = numbers.get(l);
        numbers.set(l, numbers.get(r).intValue());
        numbers.set(r, temp);
    }
};
```

