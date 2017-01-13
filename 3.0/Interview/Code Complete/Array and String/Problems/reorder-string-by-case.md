# Reorder String by Case

给定一个只包含字母的字符串，按照先小写字母后大写字母的顺序进行排序。

样例

    给出"abAcD"，一个可能的答案为"acbAD"

注意

    小写字母或者大写字母他们之间不一定要保持在原始字符串中的相对位置。

挑战

    在原地扫描一遍完成

## Solution

和快排的方法类似，找到两个要交换的元素，分别交换即可

## Code

```java
public class Solution {
    /**
     *@param chars: The letter array you should sort by Case
     *@return: void
     */
    public void sortLetters(char[] chars) {
        int len = chars.length;
        if (len <= 1) return;

        int p1 = 0, p2 = len-1;
        while (p1<len && chars[p1]>='a' && chars[p1]<='z') p1++;
        while (p2>=0 && chars[p2]>='A' && chars[p2]<='Z') p2--;
        while (p1<p2){
            //swap p1 and p2.
            char temp = chars[p1];
            chars[p1] = chars[p2];
            chars[p2] = temp;
            //find next swap positions.
            while (p1<len && chars[p1]>='a' && chars[p1]<='z') p1++;
            while (p2>=0 && chars[p2]>='A' && chars[p2]<='Z') p2--;
        }
    }
}
```

