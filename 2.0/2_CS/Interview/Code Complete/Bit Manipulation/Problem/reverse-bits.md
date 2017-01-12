# Reverse Bits

Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

Follow up:

If this function is called many times, how would you optimize it?

Related problem: Reverse Integer

## Solution

```java
public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        for (int i = 0; i < 16; i++) {
            n = swapBit(n, i, 32-1-i);
        }
        
        return n;
    }
    
    public int swapBit(int n, int i, int j) {
        int a = (n >> i) & 1;
        int b = (n >> j) & 1;
        if (a != b) {
            n ^= 1 << i | 1 << j;
        }
        
        return n;
    }
}
```

