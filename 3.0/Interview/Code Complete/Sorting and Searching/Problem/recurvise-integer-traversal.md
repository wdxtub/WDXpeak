# Recursive Integer Traversal

用递归的方法找到从1到最大的N位整数。

样例

    给出 N = 1, 返回[1,2,3,4,5,6,7,8,9].
    给出 N = 2, 返回[1,2,3,4,5,6,7,8,9,10,11,...,99].

注意

    用下面这种方式去递归其实很容易：
    recursion(i) {
        if i > largest number:
            return
        results.add(i)
        recursion(i + 1)
    }
    但是这种方式会耗费很多的递归空间，导致堆栈溢出。你能够用其他的方式来递归使得递归的深度最多只有 N 层么？

挑战

    用递归完成，而非循环的方式。

## Solution

注意整体思路的理解

## Code

```java
public class Solution {
    /**
     * @param n: An integer.
     * return : An array storing 1 to the largest number with n digits.
     */
    public List<Integer> numbersByRecursion(int n) {
        List<Integer> res = new ArrayList<Integer>();
        if (n >= 0) {
            sub(n, res);
        }
        return res;
    }

    private int sub(int n, List<Integer> res) {
        if (n == 0) {
            return 1;
        }
        int base = sub(n - 1, res);
        int size = res.size();
        for (int i = 1; i <= 9; i++) {
            int curBase = i * base;
            res.add(curBase);
            for (int j = 0; j < size; j++) {
                res.add(curBase + res.get(j));
            }
        }
        return base * 10;
    }
}

```

