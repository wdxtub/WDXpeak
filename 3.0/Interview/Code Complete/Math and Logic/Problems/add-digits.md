# Add Digits

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

Follow up:

Could you do it without any loop/recursion in O(1) runtime?

Hint:

1. A naive implementation of the above process is trivial. Could you come up with other methods?
2. What are all the possible results?
3. How do they occur, periodically or randomly?
4. You may find this Wikipedia article useful.

## Solution

观察发现 out = (in - 1) % 9 + 1

## Complexity

时间复杂度 O(1)，空间复杂度 O(1) 

## Code 

```java
public class Solution {
    public int addDigits(int num) {
        if (num == 0)
            return 0;
        return (num - 1) % 9 + 1;
    }
}
```

