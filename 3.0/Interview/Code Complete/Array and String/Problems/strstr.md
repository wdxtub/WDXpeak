# Implement strStr()

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

让你判断，needle是不是haystack的子串，是的话就返回这个子串

## Solution

简单粗暴的办法

```java
public class Solution {
    public int strStr(String haystack, String needle) {
        for (int i = 0; ; i++) {
            for (int j = 0; ; j++) {
                if (j == needle.length()) return i;
                if (i + j == haystack.length()) return -1;
                if (needle.charAt(j) != haystack.charAt(i + j)) break;
                
            } 
        }
    }
}
```

KMP 算法在面试的时候不大可能当场写对，所以考虑用 BM 算法 http://www-igm.univ-mlv.fr/~lecroq/string/node14.html#SECTION00140

```java
public class Solution {
    public int strStr(String haystack, String needle) {
        int hlen = haystack.length();
        int nlen = needle.length();
        int[] jump = new int[256];  // hashmap char-> index, assume ASCII
        for(int i=0; i<jump.length; i++) {
            jump[i]=-1;
        }
        for(int i=0; i<nlen; i++) {
            jump[needle.charAt(i)] = i; // index of last occurrence
        }
        int skip=0;
        for(int i=0; i<hlen-nlen+1; i+=skip) { // !!! not i<hlen 
            skip=0;
            for(int j=nlen-1; j>=0; j--) {
                if(haystack.charAt(i+j)!=needle.charAt(j)) {
                    skip =Math.max( 1, j-jump[haystack.charAt(i+j)] );    
                    // max is j+1, min is 1 (do not allow <0);
                    break;
                }
            }
            if(skip==0) return i;
        }
        return -1;
    }
}
```

