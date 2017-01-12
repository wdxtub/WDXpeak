# String Compression

Implement a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string. You can assum the string has only uppercase and lowercase letters(a-z)

## Solution

```java
/**
 * check the length of the new string in the first place and then build
 * the new string with stringBuilder(if needed)
 */
public static String compressString(String str){
    StringBuilder compressed = new StringBuilder(str.length());
    int count = 0;

    for (int i = 0; i < str.length(); i++){
        count++;
        if (i+1 == str.length() || str.charAt(i) != str.charAt(i+1)){
            compressed.append(str.charAt(i));
            compressed.append(count);
            count = 0;
        }
    }

    if (compressed.toString().length() >= str.length()){
        return str;
    }

    return compressed.toString();
}

public static int countLength(String str){
    int compressedLength = 0;
    int countConsecutive = 0;
    for (int i = 0; i < str.length(); i++){
        countConsecutive++;
        if (i + 1 == str.length() || str.charAt(i) != str.charAt(i+1)){
            compressedLength += 1
                    + String.valueOf(countConsecutive).length();
            countConsecutive = 0;
        }
    }

    return compressedLength;
}
```

