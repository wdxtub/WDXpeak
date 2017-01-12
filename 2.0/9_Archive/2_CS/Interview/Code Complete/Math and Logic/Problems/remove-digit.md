# Remove Digit

给出一个字符串 A, 表示一个 n 位正整数, 删除其中 k 位数字, 使得剩余的数字仍然按照原来的顺序排列产生一个新的正整数。

找到删除 k 个数字之后的最小正整数。

N <= 240, k <= N

样例

    给出一个字符串代表的正整数 A 和一个整数 k, 其中 A = 178542, k = 4
    返回一个字符串 "12"

## Solution & Complexity

这道题跟Leetcode里面的那道Next Permutation很像，那个题要找比一个数大的下一个数，于是从这个数的右边开始，找第一个递减的位置所在。这道题也是类似，只不过从这个数的左边开始，找第一个递减的位置所在。那道题是想要改动的影响最小，所以从右边开始扫描。这道题是想要改动的影响最大，所以从左边开始扫描。

这道题，删掉一个数，相当于用这个数后面的数代替这个数。所以后面这个数一定要比当前小才行。所以找的是第一个递减的位置，把大的那个数删了。

这样做一次就是找到了：删除哪一个数，使得剩下的数最小。对剩下的数再做k次，就可以找到删除哪k个数，使得剩下的数最小。这其实是一个Greedy算法，因为这样每做一次，得到的都是当前最优的结果。

看起来需要O(Nk)时间复杂度，但其实用一个Stack，再记录pop了几次，O(2N)就好了

## Code

```java
public class Solution {
    /**
     *@param A: A positive integer which has N digits, A is a string.
     *@param k: Remove k digits.
     *@return: A string
     */
    public String DeleteDigits(String A, int k) {
        Stack<Integer> st = new Stack<Integer>();
        int popCount = 0;
        StringBuffer res = new StringBuffer();
        for (int i=0; i<A.length(); i++) {
            int num = (int)(A.charAt(i) - '0');
            if (st.isEmpty()) st.push(num);
            else if (num >= st.peek()) {
                st.push(num);
            }
            else {
                if (popCount < k) {
                    st.pop();
                    i--;
                    popCount++;
                }
                else {
                    st.push(num);
                }
            }
        }
        while (popCount < k) {
            st.pop();
            popCount++;
        }
        while (!st.isEmpty()) {
            res.insert(0, st.pop());
        }
        while (res.length() > 1 && res.charAt(0) == '0') {
            res.deleteCharAt(0);
        }
        return res.toString();
    }
}

```

