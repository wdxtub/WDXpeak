# Check Permutation 

出处

Given two strings, write a method to decide if one is a permutation of the other.

Detail: if white space is significant

## Solution

可以排序或者用 hashtable 来做

## Complexity

排序的时间复杂度是 O(nlogn)，空间复杂度 O(1)，hashtable 时间复杂度 O(n)，空间复杂度 O(n)

## Code

```java
public static boolean isPermutationHashTable(String str1, String str2){
    // check special case first
    if (str1 == null && str2 != null || str1 != null && str2 == null){
        return false;
    }
    if (str1.length() != str2.length()){
        return false;
    }

    int[] alphabet = new int[256];
    for (int i = 0; i < str1.length(); i++){
        alphabet[str1.charAt(i)]++;
    }

    for (int i = 0; i < str2.length(); i++){
        alphabet[str2.charAt(i)]--;
        if (alphabet[str2.charAt(i)] < 0){
            return false;
        }
    }
    return true;
}

public static boolean isPermutationSort(String str1, String str2){
    // check special case first
    if (str1 == null && str2 != null || str1 != null && str2 == null){
        return false;
    }
    if (str1.length() != str2.length()){
        return false;
    }

    char[] str1char = str1.toCharArray();
    char[] str2char = str2.toCharArray();
    Arrays.sort(str1char);
    Arrays.sort(str2char);

    for (int i = 0; i < str1char.length; i++){
        if (str1char[i] != str2char[i]){
            return false;
        }
    }
    return true;
}
```

