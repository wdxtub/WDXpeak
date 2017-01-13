# One Away

There are three types of edits that can be performed on strings: insert a character, remove a character, or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away

EXAMPLE

    pale, ple -> true
    pales, pale -> true
    pale, bale -> true
    pale, bake -> false
    
## Solution

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
public static boolean isOneWay(String str1, String str2){
    if (str1.length() - str2.length() > 1 ||
            str2.length() - str1.length() > 1){
        return false;
    }

    String s1 = null;
    if (str1.length() < str2.length()){
        s1 = str1;
    }
    else{
        s1 = str2;
    }

    String s2 = null;
    if (str1.length() < str2.length()){
        s2 = str2;
    }
    else{
        s2 = str1;
    }

    int i1 = 0;
    int i2 = 0;
    boolean isdif = false;
    while (i2 < s2.length() && i1 < s1.length()){
        if (s1.charAt(i1) != s2.charAt(i1)){
            if (isdif) return false;
            isdif = true;

            if (s1.length() == s2.length()){
                i1++;
            }
        }
        else{
            i1++;
        }
        i2++;
    }
    return true;
}
```

