# Check Power of Two

Explain what the following code does: ((n & (n-1)) == 0)

## Solution

n = abcde1000
n - 1 = abcde0111

can only have one 1 in the binary form -> check power of 2

注意判断 n > 0

注意因为对时间复杂度有要求，所以必须利用位操作来进行判断。注意一些边界情况，例如是负数或者是0,1 之类的，需要分别处理。

2 的幂次表示在二进制中只有最高位是 1 其余都是零，所以利用 `n & n-1 == 0` 来进行检测  

## Complexity

时间复杂度 O(1) 空间复杂度 O(1)

## Code

```java
public class Solution {
    public boolean isPowerOfTwo(int n) {
        return  (n > 0) && (n & (n-1)) == 0;
    }
}
```

