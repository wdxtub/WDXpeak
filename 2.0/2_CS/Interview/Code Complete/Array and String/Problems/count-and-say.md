# Count and Say

出处

报数指的是，按照其中的整数的顺序进行报数，然后得到下一个数。如下所示：

1, 11, 21, 1211, 111221, ...

+ 1 读作 "one 1" -> 11.
+ 11 读作 "two 1s" -> 21.
+ 21 读作 "one 2, then one 1" -> 1211.

给定一个整数 n, 返回 第 n 个顺序。

样例

    给定 n = 5, 返回 "111221".

注意

    整数的顺序将表示为一个字符串。

## Solution

按照规则进行递推即可

## Complexity

时间复杂度 O(n^2 )，空间复杂度 O(1)

## Code

```java
public class Solution {
    public String countAndSay(int n) {
        StringBuffer s = new StringBuffer("1");
        StringBuffer res = new StringBuffer();
        while((--n) != 0){
            res.setLength(0);
            int size = s.length();
            int cnt = 1;
            char cur = s.charAt(0);
            for(int i=1;i<size;i++){
                if(s.charAt(i)!=cur){
                    res.append(cnt);
                    res.append(cur);
                    cur = s.charAt(i);
                    cnt = 1;
                }else ++cnt;
            }
            res.append(cnt);
            res.append(cur);
            StringBuffer tmp = s;
            s = res;
            res = tmp;
        }
        return s.toString();
    }
}
```


