# Longest Word in Dictionary

给一个词典，找出其中所有最长的单词。

样例

    在词典
    {
      "dog",
      "google",
      "facebook",
      "internationalization",
      "blabla"
    }
    中, 最长的单词集合为 ["internationalization"]
    
    在词典
    {
      "like",
      "love",
      "hate",
      "yes"
    }
    中，最长的单词集合为 ["like", "love", "hate"]

挑战

    遍历两次的办法很容易想到，如果只遍历一次你有没有什么好办法？

## Solution

具体计算的时候，保持一个计数和一个当前计数的单词数组，就可以一次搞定

## Code

```python
class Solution:
    # @param dictionary: a list of strings
    # @return: a list of strings
    def longestWords(self, dictionary):
        # write your code here
        ret = []
        for word in dictionary:
            if not ret or len(word) > len(ret[0]):
                ret = [word]

            elif len(word) == len(ret[0]):
                ret.append(word)

        return ret

```

