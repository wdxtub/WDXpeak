# Happy Number

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 0^2 = 1
    
## Solution

按照规律算即可，如果出现循环就证明不可能

## Complexity

时间复杂度 O(n^2 )，空间复杂度 O(n)

## Code

```java
public class Solution {
    int trans(int n){
        int s = 0;
        do{
            int t = n % 10;
            s += t * t;
            n /= 10;
        } while(n > 0);
        return s;
    }

    public boolean isHappy(int n) {
        Set<Integer> s = new HashSet<>();
        for(;;) {
            n = trans(n);
            if(n == 1) return true;
            if(s.contains(n)) return false;
            s.add(n);
        }
    }
}
```

