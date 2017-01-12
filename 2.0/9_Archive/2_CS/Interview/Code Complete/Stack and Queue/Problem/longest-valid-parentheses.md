# Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

## Solution & Complexity

O(n) - Use stack

## Code

```java
public class Solution {
    public int longestValidParentheses(String s) {
        Stack<Integer> stk = new Stack<Integer>();
        int res = 0, count = 0;
        for(int i = 0; i < s.length(); ++i) {
            if (s.charAt(i) == '(') {
                stk.push(count);
                count = 0;
            } else if (stk.empty() == false) {
                count += (1 + stk.pop());
                res = Math.max(res, count);
            } else {
                count = 0;
            }
        }
        return res * 2;
    }
}
```

