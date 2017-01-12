# Find Minimum in Rotated Sorted Array

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

## Solution

根据中间与两边的大小来判断最小值在哪里

## Complexity

时间复杂度 O(logn)，空间复杂度 O(1)

## Code 

```java
public class Solution {
    public int findMin(int[] num) {
        if (num.length == 0) return 0;
        int left = 0, right = num.length -1;
        while (left < right && num[left] > num[right]) {
            int mid = left + (right - left) / 2;
            if (num[mid] > num[right]) left = mid + 1;
            else right = mid;
        }
        return num[left];
    }
}
```

如果有重复

```java
public class Solution {
    public int findMin(int[] num) {
        if (num.length == 0) return 0;
        int left = 0, right = num.length -1;
        while (left < right && num[left] >= num[right]) {
            int mid = left + (right - left) / 2;
            if (num[mid] > num[right]) left = mid + 1;
            else if (num[mid] < num[right]) right = mid;
            else left++;
        }
        return num[left];
    }
}
```


