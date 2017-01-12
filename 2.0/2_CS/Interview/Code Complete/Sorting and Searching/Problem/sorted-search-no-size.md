# Sorted Search, No Size

You are given an array-like data structure Listy which lacks a size method. It does, however, have an elementAt(i) method that returns the element at index i in O(1) time. If i is beyond the bounds of the data structure, it returns -1. (For this reason, the data structure only supports positive integers.) Given a Listy which contains sorted, positive integers, find the index at which an element x occurs. If x occurs multiple times, you may return any index.

## Solution

```java
/**
 * 每次放大一倍找到长度，然后二分
 */
int search(Listy list, int value){
    int index = 1;
    while (list.elementAt(index) != -1 && list.elementAt(index) < value){
        index *= 2;
    }
    return binarySearch(list, value, index / 2, index);
}

int binarySearch(Listy list, int value, int low, int high){
    int mid;

    while (low <= high){
        mid = (low + high) / 2;
        int middle = list.elementAt(mid);
        if (middle  > value || middle == -1){
            high = mid - 1;
        }
        else if (middle < value ){
            low = mid + 1;
        }
        else {
            return mid;
        }
    }
    return -1;
}
```

