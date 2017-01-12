# Evaluate Reverse Polish Notation

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:

    ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
    ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

## Solution

利用栈就可以完美解决，每次弹出两个，如果有需要压回去一个

## Complexity

时间复杂度 O(n)，空间复杂度 O(n)

## Code 

```java
public class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stk = new Stack<Integer>();
        for (int i = 0; i < tokens.length; ++i) {
            if ((tokens[i].compareTo("+") != 0) && (tokens[i].compareTo("-") != 0) 
                    && (tokens[i].compareTo("*") != 0) && (tokens[i].compareTo("/") != 0)) {
                stk.push(Integer.parseInt(tokens[i]));
            } else {
                int op2 = stk.pop();
                int op1 = stk.pop();
                int res = 0;
                if(tokens[i].compareTo("+") == 0)
                    res = op1 + op2;
                else if(tokens[i].compareTo("-") == 0)
                    res = op1 - op2;
                else if(tokens[i].compareTo("*") == 0)
                    res = op1 * op2;
                else if(tokens[i].compareTo("/") == 0)
                    res = op1 / op2;
                stk.push(res);
            }
        }
        return stk.pop();
    }
}
```

