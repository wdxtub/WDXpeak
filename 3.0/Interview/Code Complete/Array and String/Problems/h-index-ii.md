# H-Index II

Follow up for H-Index: What if the citations array is sorted in ascending order? Could you optimize your algorithm?

Hint:

Expected runtime complexity is in O(log n) and the input is sorted.

## Solution

二分法（Binary Search）

```java
public class Solution {
    public int hIndex(int[] citations) {
        int len = citations.length;
        int low = 0;
        int high = len - 1;
        while (low <= high){
            int mid = (low + high) / 2;
            if (len - mid > citations[mid])
                low = mid + 1;
            else
                high = mid - 1;
        }
        return len - low;
    }
}
```

