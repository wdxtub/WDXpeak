# Next Number

Given a positive integer, print the next smallest and the next largest number that have the same number of 1 bits in their binary representation



## Solution

**Get Next**

 1. Flip rightmost non-trailing zero
 2. Clear bits to the right of p
 3. add in c1 - 1 ones

**Get Previous**

1. trailing ones, and trailing zeros to the left of trailing ones
2. Flip the right most one-trailing one to a zero.
3. clear all bits to the right of bit p
4. Insert c1 + 1 ones immediately to the right of position p

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
/**
 * @param n
 * @return
 */
int getNext(int n){
    int temp = n;
    int zeros = 0;
    int ones = 0;

    while(((temp & 1) == 0) && (temp != 0)){
        zeros++;
        temp = temp >> 1;
    }

    while((temp & 1) == 1){
        ones++;
        temp = temp >> 1;
    }

    if (zeros + ones == 31 || zeros + ones == 0){
        return -1;
    }

    int rightmost = zeros + ones;

    n = n | (1 << rightmost);
    n = n & ~((1 << rightmost) - 1);
    n = n | (1 << (ones - 1)) - 1;

    return n;
}

/**
 * @param n
 * @return
 */
int getPrev(int n){
    int temp = n;
    int zeros = 0;
    int ones = 0;

    while((temp & 1) == 1){
        ones++;
        temp = temp >> 1;
    }

    while(((temp & 1) == 0) && (temp != 0)){
        zeros++;
        temp = temp >> 1;
    }

    if (zeros + ones == 31 || zeros + ones == 0){
        return -1;
    }

    int rightmost = zeros + ones;

    n = n & ~(1 << (rightmost + 1) - 1);
    int mask = ((1 << (ones + 1)) - 1) << (zeros - 1);
    n = n | mask;
    return n;
}
```

