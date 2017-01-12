# String Comparison

出处

比较两个字符串A和B，确定A中是否包含B中所有的字符。字符串A和B中的字符都是 大写字母

样例

    给出 A = "ABCD" B = "ACD"，返回 true
    给出 A = "ABCD" B = "AABC"， 返回 false

注意

    在 A 中出现的 B 字符串里的字符不需要连续或者有序。

## Solution

用一个数组标记每个字母出现的次数，注意这里 lintcode 里的测试用例很坑，字符串是带有 `""`符号的，需要在一开始处理一下

## Complexity

时间复杂度 O(n)，空间复杂度 O(n)

## Code 

```python
class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        # write your code here
        cnt = [0] * 26
        A = A[1:-1]
        B = B[1:-1]
        for c in A:
            cnt[ord(c)-ord('A')] += 1
        for c in B:
            cnt[ord(c)-ord('A')] -= 1
            if cnt[ord(c)-ord('A')] < 0:
                return False
        return True

```

