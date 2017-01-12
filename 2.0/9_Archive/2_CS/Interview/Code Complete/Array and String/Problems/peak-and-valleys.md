# Peaks and Valleys

In an array of integers, a "peak" is an element which is greater than or equal or equal to the adjacent integers and a "valley" is an element which is less than or equal to the adjacent integers. For example, in the array {5, 8, 6, 2, 3, 4, 6}, {8, 6} are peaks and {5, 2} are valleys. Given an array of integers, sort the array into an alternating sequence of peaks and valleys.

EXAMPLE

    Input:  {5, 3, 1, 2, 3}
    Output: {5, 1, 3, 2, 3}
    
## Solution

比较三个数，然后进行交换即可

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)
    
## Solution

```java
/**
 * Optimal Solution
 *
 * No need to sort in the first place
 */
void sortValleyPeak2(int[] array){
    for (int i = 1; i < array.length; i+= 2){
        int biggestIndex = maxIndex(array, i-1, i, i+1);
        if (i != biggestIndex){
            swap(array, i, biggestIndex);
        }
    }
}

int maxIndex(int[] array, int a, int b, int c){
    int len = array.length;
    int aValue = a >= 0 && a < len ? array[a] : Integer.MIN_VALUE;
    int bValue = b >= 0 && b < len ? array[b] : Integer.MIN_VALUE;
    int cValue = c >= 0 && c < len ? array[c] : Integer.MIN_VALUE;

    int max = Math.max(aValue, Math.max(bValue, cValue));
    if (aValue == max) return a;
    else if (bValue == max) return b;
    else return c;
}
```

