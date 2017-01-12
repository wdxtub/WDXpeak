# Add One

给定一个非负数，表示一个数字数组，在该数的基础上+1，返回一个新的数组。

该数字按照大小进行排列，最大的数在列表的最前面。

样例

    给定 [1,2,3] 表示 123, 返回 [1,2,4].
    给定 [9,9,9] 表示 999, 返回 [1,0,0,0].

## Solution

先翻转，然后逐个加，最后再翻转，注意最后的进位

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
public class Solution {
    public int[] plusOne(int[] digits) {
        if (digits.length == 0) return digits;
        int carry = 1;
        for (int i = digits.length - 1; i >= 0; --i) {
            digits[i] += carry;
            carry = digits[i] / 10;
            digits[i] = digits[i] % 10;
        }
        if (carry == 0) return digits;
        int[] res = new int[digits.length + 1];
        res[0] = carry;
        System.arraycopy(digits, 0, res, 1, digits.length);
        return res;
    }
}
```

---

```python
class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        # Write your code here
        l = len(digits)
        addit = 1
        digits.reverse()
        ans = []
        for i in range(l):
            if digits[i] + addit == 10:
                ans.append(0)
                addit = 1
            else:
                ans.append(digits[i] + addit)
                addit = 0
        if addit == 1:
            ans.append(1)
        ans.reverse()
        return ans

```

