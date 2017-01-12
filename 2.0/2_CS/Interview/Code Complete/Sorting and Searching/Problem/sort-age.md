# Sort Age

出处

Sort a large number of people by their ages.

## Solution

人的寿命是有限的，即数据都处于[0,150]。在数据最大值已知的情况下，通常桶排序效率最高，为O(n)。对于本例，由于数据为十进制数，并且至多3位。故我们还可以考虑用基数排序，时间复杂度与桶排序近似。

## Complexity

同桶排序，O(n)。

## Code 

参考桶排序的实现

