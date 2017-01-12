# ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   N
    A P L S I I G
    Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

    string convert(string text, int nRows);

convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

## Solution

找规律题目

```java
public class Solution {
    public String convert(String s, int numRows) {
        int n = s.length();
        if (n <= 1 || numRows <= 1) return s;
        StringBuffer res = new StringBuffer();
        for (int i = 0; i < numRows; ++i) {
            for (int j = 0; j + i < n; j += 2*numRows - 2) {
                res.append(s.charAt(j+i));
                if (i == 0 || i == numRows - 1) continue;
                if (j + 2*numRows - 2 - i < n) 
                    res.append(s.charAt(j + 2*numRows - 2 - i));
            }
        }
        return res.toString();
    }
}
```

