# Roman to Integer

给定一个罗马数字，将其转换成整数。

返回的结果要求在1到3999的范围内。

样例

    IV -> 4
    XII -> 12
    XXI -> 21
    XCIX -> 99

## Solution

正常进行转换，注意罗马数字的用法即可

## Complexity

时间复杂度 O(n)，空间复杂度 O(n)

## Code

```java
public class Solution {
    /**
     * @param s Roman representation
     * @return an integer
     */
    public int romanToInt(String s) {
         if (s == null) {
            return 0;
        }

        // bug 1: forget new.
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);

        int len = s.length();
        int num = 0;
        for (int i = len - 1; i >= 0; i--) {
            int cur = map.get(s.charAt(i));
            if (i < len - 1 && cur < map.get(s.charAt(i + 1))) {
                num -= cur;
            } else {
                num += cur;
            }
        }

        return num;
    }
}

```

