# Reverse Sentence

给定一个字符串，逐个翻转字符串中的每个单词。

样例

    给出s = "the sky is blue"，返回"blue is sky the"

说明

+ 单词的构成：无空格字母构成一个单词
+ 输入字符串是否包括前导或者尾随空格？可以包括，但是反转后的字符不能包括
+ 如何处理两个单词间的多个空格？在反转字符串中间空格减少到只含一个

## Solution

1. 由第一个提问可知：题中只有空格字符和非空格字符之分，因此空格字符应为其一关键突破口。
2. 由第二个提问可知：输入的前导空格或者尾随空格在反转后应去掉。
3. 由第三个提问可知：两个单词间的多个空格字符应合并为一个或删除掉。

首先找到各个单词(以空格隔开)，根据题目要求，单词应从后往前依次放入。正向取出比较麻烦，因此可尝试采用逆向思维——先将输入字符串数组中的单词从后往前逆序取出，取出单词后即翻转并append至新字符串数组。在append之前加入空格即可。

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```python
class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        # write your code here
        res = ""    # result string
        word = ""   # single word string
        for ch in s:
            if (ch!=' '):
                word+=ch
            if (ch==' '):
                if (len(word)!=0):
                    if (res!=""):   # add space between words
                        res = ' ' + res
                    res = word + res
                    word = ""

        if (len(word)!=0):  #handle the final word
            if (res!=""):
                res = ' ' + res
            res = word + res

        return res

```

