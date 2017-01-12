# Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

For example,

    Given numerator = 1, denominator = 2, return "0.5".
    Given numerator = 2, denominator = 1, return "2".
    Given numerator = 2, denominator = 3, return "0.(6)".
    
## Solution

        0.16
      ------
    6 ) 1.00
        0 
        1 0       <-- Remainder=1, mark 1 as seen at position=0.
        - 6 
          40      <-- Remainder=4, mark 4 as seen at position=1.
        - 36 
           4      <-- Remainder=4 was seen before at position=1, so the fractional part which is 16 starts repeating at position=1 => 1(6).
           
The key insight here is to notice that once the remainder starts repeating, so does the divided result.

You will need a hash table that maps from the remainder to its position of the fractional part. Once you found a repeating remainder, you may enclose the reoccurring fractional part with parentheses by consulting the position from the table.

The remainder could be zero while doing the division. That means there is no repeating fractional part and you should stop right away.

## Code

```java
public class Solution {
    public String fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) return new String("0");
        boolean flag = (numerator < 0)^(denominator < 0);
        long Numerator = Math.abs((long)numerator);
        long Denominator = Math.abs((long)denominator);
        StringBuffer res = new StringBuffer();
        if (flag == true) res.append('-');
        res.append(String.valueOf((Numerator / Denominator)));
        Numerator = Numerator % Denominator;
        if (Numerator == 0) return res.toString();
        res.append('.');
        HashMap<Long, Integer> map = new HashMap<Long, Integer>();
        for (int i = res.length(); Numerator != 0; ++i) {
            if (map.get(Numerator) != null) break;
            map.put(Numerator, i);
            Numerator *= 10;
            res.append(String.valueOf((Numerator / Denominator)));
            Numerator %= Denominator;
        }
        
        if (Numerator == 0) return res.toString();
        res.insert(map.get(Numerator),"(");
        res.append(')');
        return res.toString();
    }
}
```

