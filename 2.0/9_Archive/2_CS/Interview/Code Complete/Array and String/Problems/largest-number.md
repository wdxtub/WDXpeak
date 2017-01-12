# Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.

## Solution

按照字典序来排序

## Complexity

时间复杂度 O(nlogn)，空间复杂度 O(n)

## Code

```java
public class Solution {
    public String largestNumber_1(int[] num) {
        int size = num.length;
        if (size <= 0) return new String();
        if (size == 1) return String.valueOf(num[0]);
        Comparator<Integer> comp =  new Comparator<Integer>(){  
            public int compare(Integer a,  Integer b) { 
                    String aa = ""+a+b;
                    String bb = ""+b+a;
                    return bb.compareTo(aa);
            }  
        };
        Integer[] in = new Integer[size];
        for (int i = 0; i < size; ++i)
            in[i] = Integer.valueOf(num[i]);
        Arrays.sort(in, comp);
        StringBuffer res = new StringBuffer();
        int i = 0;
        while ((i < in.length - 1) && (in[i] == 0)) ++i;
        while (i < in.length) res.append(in[i++]);
        return res.toString();
    }
    
    
    public String largestNumber_2(int[] num) {
        int size = num.length;
        if (size <= 0) return new String();
        String[] in = new String[size];
        for (int i = 0; i < size; ++i)
            in[i] = String.valueOf(num[i]);
        return foo(in);
    }
    public String foo(String[] in) {
        if (in.length == 0) return new String();
        if (in.length == 1) return in[0];
        StringBuffer res = new StringBuffer();
        Comparator<String> comp =  new Comparator<String>(){  
            public int compare(String a,  String b) { 
                    String aa = a+b;
                    String bb = b+a;
                    return bb.compareTo(aa);
            }  
        };
        Arrays.sort(in, comp);
        int i = 0;
        while ((i < in.length - 1) && (in[i].compareTo("0") == 0)) ++i;
        while (i < in.length) res.append(in[i++]);
        return res.toString();
    }
}
```

