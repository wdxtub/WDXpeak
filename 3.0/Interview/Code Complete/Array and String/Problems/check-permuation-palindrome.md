# Palindrome Permutation

Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

EXAMPLE

    Input:  Tact Coa
    Output: True (permutations: "taco cat", "atco cta", etc.)

DETAIL:

    check if it is ANSI or Unicode
    
## Solution

第一次遍历统计每个单词的个数

第二次遍历看看奇数个的个数是不是大于1

## Complexity

时间复杂度 O(n)，空间复杂度 O(n)

## Code

```java
/**
 * It is also possible to finish the whole process within one pass, but as
 * it is not always a optimal solution. I skip it here. What's more, bit
 * vector can be used here too, but again, it is the same strategy and
 * increase the opportunity of writing wrong code(bit operations are always
 * easy to become a mess and hard to understand
 */
public static boolean isPalindromePermutation(String str){
    String newStr = str.toLowerCase();
    int[] alphabet = new int[256];
    int oddCount = 0;
    // 1 - pass
    for (int i = 0; i < newStr.length(); i++){
        if (newStr.charAt(i) != ' ') {
            alphabet[newStr.charAt(i)]++;
        }
    }
    // 2 - pass
    for (int i = 0; i < alphabet.length; i++){
        if (alphabet[i] != 0){
            if (alphabet[i] % 2 != 0){
                oddCount++;
            }
        }
    }
    if (oddCount > 1){
        return false;
    }

    return true;
}
```

