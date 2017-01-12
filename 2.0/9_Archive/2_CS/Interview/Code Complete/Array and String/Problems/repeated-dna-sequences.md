# Repeated DNA Sequences

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

For example,

Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:

["AAAAACCCCC", "CCCCCAAAAA"].

## Solution

```java
public class Solution {
    public List<String> findRepeatedDnaSequences(String s) {
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        HashMap<Character,Integer> mole = new HashMap<Character,Integer>();
        mole.put('A',0); mole.put('C',1); mole.put('G',2); mole.put('T',3);
        List<String> res = new ArrayList<String>();
        if (s.length() < 11) return res;
        int x = 0, i = 0, mask = (1<<20) - 1;
        for (; i < 10; ++i) {
            x = (x << 2) | mole.get(s.charAt(i));
        }
        map.put(x, 1);
        for (; i < s.length(); ++i) {
            x = (x<<2)|mole.get(s.charAt(i));
            x = x & mask;
            if (map.containsKey(x)) {
                if (map.get(x) == 1) {
                    res.add(convert2Str(x));
                    map.put(x,-1);
                }
            } else {
                map.put(x,1);
            }
        }
        return res;
    }
    public String convert2Str(int x) {
        String res = new String();
        for (int i = 0; i < 10; ++i) {
            int k = x & 3;
            if (k == 0) res = 'A' + res;
            if (k == 1) res = 'C' + res;
            if (k == 2) res = 'G' + res;
            if (k == 3) res = 'T' + res;
            x = x >> 2;
        }
        return res;
    }
}
```

