# Single Element III

给出2*n + 2个的数字，除其中两个数字之外其他每个数字均出现两次，找到这两个数字。

样例

    给出 [1,2,2,3,4,4,5,3]，返回 1和5

挑战

    O(n)时间复杂度，O(1)的额外空间复杂度

## Solution

与以上两题不同的是，这道题有两个数只出现一次。基本的思路还是利用位运算，除去出现次数为2次的数。

如果对所有元素进行异或操作，最后剩余的结果是出现次数为1次的两个数的异或结果，此时无法直接得到这两个数具体的值。但是，因为这两个数一定是不同的，所以最终异或的值至少有一个位为1。我们可以找出异或结果中第一个值为1的位，然后根据该位的值是否为1，将数组中的每一个数，分成两个部分。这样每个部分，就可以采用Sing number I中的方法得到只出现一次的数。

利用bitwise XOR的特点，n个数（0或1），如果1的个数为奇数，则n个数bitwise XOR结果为1，否则为0

先将所有的数异或，得到的将是x和y以后之后的值n。 找到这个数n的为1的某一位（为了方便就取最右边为1的一位， n & ~(n-1)，再将这一位为1的数异或，其余的数异或，得到的就是x和y的值。

## Complexity

时间复杂度 O(n)，空间复杂度 O(n)

## Code

```java
public class Solution {
    /**
     * @param A : An integer array
     * @return : Two integers
     */
    public List<Integer> singleNumberIII(int[] A) {
        ArrayList<Integer> res = new ArrayList<Integer>();
        res.add(0);
        res.add(0);
        int n = 0;
        for (int elem : A) {
            n ^= elem;
        }
        n = n & (~(n-1));
        for (int elem : A) {
            if ((elem & n) != 0) {
                res.set(0, res.get(0)^elem);
            }
            else res.set(1, res.get(1)^elem);
        }
        return res;
    }
}

```

