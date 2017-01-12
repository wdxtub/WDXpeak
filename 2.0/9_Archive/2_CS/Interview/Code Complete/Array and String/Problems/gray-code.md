# Gray Code

格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个二进制的差异。

给定一个非负整数 n ，表示该代码中所有二进制的总数，请找出其格雷编码顺序。一个格雷编码顺序必须以 0 开始，并覆盖所有的 2n 个整数。

样例

    给定 n = 2， 返回 [0,1,3,2]。其格雷编码顺序为：
    00 - 0
    01 - 1
    11 - 3
    10 - 2

注意

    对于给定的 n，其格雷编码顺序并不唯一。
    根据以上定义， [0,2,3,1] 也是一个有效的格雷编码顺序。

挑战

    O(2n) 时间复杂度。

## Solution

n 位的格雷码可由 n-1位的格雷码递推，在最高位前顺序加0，逆序加1即可。实际实现时我们可以省掉在最高位加0的过程，因为其在数值上和前 n-1位格雷码相同。另外一点则是初始化的处理，图中为从1开始，但若从0开始可进一步简化程序。而且根据 格雷码 的定义，n=0时确实应该返回0.

加 0 的那一部分已经在前一组格雷码中出现，故只需将前一组格雷码镜像后在最高位加 1 即可。第二重 for 循环中需要注意的是currGray.size() - 1并不是常量，只能用于给 j 初始化。本应该使用 2^n 和上一组格雷码相加，这里考虑到最高位为1的特殊性，使用位运算模拟加法更好。

## Complexity

时间复杂度 O(nlogn)，空间复杂度 O(1)

## Code

```java
public class Solution {
    /**
     * @param n a number
     * @return Gray code
     */
    public ArrayList<Integer> grayCode(int n) {
        if (n < 0) return null;

        ArrayList<Integer> currGray = new ArrayList<Integer>();
        currGray.add(0);

        for (int i = 0; i < n; i++) {
            int msb = 1 << i;
            // backward - symmetry
            for (int j = currGray.size() - 1; j >= 0; j--) {
                currGray.add(msb | currGray.get(j));
            }
        }
        return currGray;
    }
}

```

Refer to http://en.wikipedia.org/wiki/Gray_code.

```java
public class Solution {
    public List<Integer> grayCode(int n) {
        ArrayList<Integer> res = new ArrayList<Integer>();
        for (int i = 0; i < 1 << n; ++i)
            res.add((int)((i >> 1) ^ i));
        return res; 
    }
}
```

