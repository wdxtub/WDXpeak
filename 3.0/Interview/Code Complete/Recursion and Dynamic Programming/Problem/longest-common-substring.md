# Longest Common Substring

给出两个字符串，找到最长公共子串，并返回其长度。

样例

    给出A=“ABCD”，B=“CBCE”，返回 2

注意

    子串的字符应该连续的出现在原字符串中，这与子序列有所不同。

## Solution

求最长公共子串，注意「子串」和「子序列」的区别！简单考虑可以使用两根指针索引分别指向两个字符串的当前遍历位置，若遇到相等的字符时则同时向后移动一位

## Code

```cpp
class Solution {
public:
    /**
     * @param A, B: Two string.
     * @return: the length of the longest common substring.
     */
    int longestCommonSubstring(string &A, string &B) {
        // write your code here
        if (A.empty() || B.empty()){
            return 0;
        }

        int lcs = 0, tlcs = 0;
        for (int i = 0; i < A.size(); i++){
            for (int j = 0; j < B.size(); j++){
                tlcs = 0;
                while ((i + tlcs < A.size()) && (j + tlcs < B.size()) && (A[i + tlcs] == B[j + tlcs])){
                    tlcs++;
                }
                if (tlcs > lcs){
                    lcs = tlcs;
                }
            }
        }
        return lcs;
    }
};

```

