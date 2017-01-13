# Integer to English Words

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2^31 - 1.

For example,

    123 -> "One Hundred Twenty Three"
    12345 -> "Twelve Thousand Three Hundred Forty Five"
    1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Hint:

1. Did you see a pattern in dividing the number into chunk of words? For example, 123 and 123000.
2. Group the number by thousands (3 digits). You can write a helper function that takes a number less than 1000 and convert just that chunk to words.
3. There are many edge cases. What are some good test cases? Does your code work with input such as 0? Or 1000010? (middle chunk is zero and should not be printed out)

## Solution

题目中给足了提示，首先告诉我们要3个一组的进行处理，而且题目中限定了输入数字范围为0到231 - 1之间，最高只能到billion位，3个一组也只需处理四组即可，那么我们需要些一个处理三个一组数字的函数，我们需要把1到19的英文单词都列出来，放到一个数组里，还要把20,30，... 到90的英文单词列出来放到另一个数组里，然后我们需要用写技巧，比如一个三位数n，百位数表示为n/100，后两位数一起表示为n%100，十位数表示为n%100/10，个位数表示为n%10，然后我们看后两位数是否小于20，小于的话直接从数组中取出单词，如果大于等于20的话，则分别将十位和个位数字的单词从两个数组中取出来。然后再来处理百位上的数字，还要记得加上Hundred。主函数中调用四次这个帮助函数，然后中间要插入"Thousand", "Million", "Billion"到对应的位置，最后check一下末尾是否有空格，把空格都删掉，返回的时候检查下输入是否为0，是的话要返回'Zero'。

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
public class Solution {
    public String numberToWords(int num) {
        String[] bigs = new String[]{" Thousand", " Million", " Billion"};
        StringBuilder sb = new StringBuilder();
        int i = 0;
        sb.append(convertToWords(num % 1000));
        num /= 1000;
        while (num > 0) {
            if (num % 1000 != 0) {
                sb.insert(0, convertToWords(num % 1000) + bigs[i]);
            }
            i++;
            num /= 1000;
        }
        return sb.length() == 0 ? "Zero" : sb.toString().trim();
    }
     
    public String convertToWords(int num) {
        String[] digit = {"", " One", " Two", " Three", " Four", " Five",
                " Six", " Seven", " Eight", " Nine"};
        String[] tenDigit = {" Ten", " Eleven", " Twelve", " Thirteen", " Fourteen", " Fifteen",
                " Sixteen", " Seventeen", " Eighteen", " Nineteen"};
        String[] tenMutipleDigit = {"", "", " Twenty", " Thirty", " Forty", " Fifty",
                " Sixty", " Seventy", " Eighty", " Ninety"};
        StringBuilder sb = new StringBuilder();
        if (num >= 100) {
            sb.append(digit[num / 100]).append(" Hundred");
            num %= 100;
        }
        if (num > 9 && num < 20) {
            sb.append(tenDigit[num - 10]);
        } else {
            if (num >= 20) {
                sb.append(tenMutipleDigit[num / 10]);
                num %= 10;
            }
            sb.append(digit[num]);
        }
        return sb.toString();
    }
}
```

