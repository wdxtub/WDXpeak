# Basic Calculator

出处

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

You may assume that the given expression is always valid.

Some examples:

    "1 + 1" = 2
    " 2-1 + 2 " = 3
    "(1+(4+5+2)-3)+(6+8)" = 23

Note: Do not use the eval built-in library function.

## Solution

This problem can be solved by using a stack. We keep pushing element to the stack, when ')" is met, calculate the expression up to the first "(".

## Complexity

时间复杂度 O(n)，空间复杂度 O(n)

## Code

```java
public class Solution {
    public int calculate(String s) {
        s = s.replaceAll(" ", "");
 
    	Stack<String> stack = new Stack<String>();
    	char[] arr = s.toCharArray();
     
    	StringBuilder sb = new StringBuilder();
    	for (int i = 0; i < arr.length; i++) {
    		if (arr[i] == ' ')
    			continue;
     
    		if (arr[i] >= '0' && arr[i] <= '9') {
    			sb.append(arr[i]);
     
    			if (i == arr.length - 1) {
    				stack.push(sb.toString());
    			}
    		} else {
    			if (sb.length() > 0) {
    				stack.push(sb.toString());
    				sb = new StringBuilder();
    			}
     
    			if (arr[i] != ')') {
    				stack.push(new String(new char[] { arr[i] }));
    			} else {
    				// when meet ')', pop and calculate
    				ArrayList<String> t = new ArrayList<String>();
    				while (!stack.isEmpty()) {
    					String top = stack.pop();
    					if (top.equals("(")) {
    						break;
    					} else {
    						t.add(0, top);
    					}
    				}
     
    				int temp = 0;
    				if (t.size() == 1) {
    					temp = Integer.valueOf(t.get(0));
    				} else {
    					for (int j = t.size() - 1; j > 0; j = j - 2) {
    						if (t.get(j - 1).equals("-")) {
    							temp += 0 - Integer.valueOf(t.get(j));
    						} else {
    							temp += Integer.valueOf(t.get(j));
    						}
    					}
    					temp += Integer.valueOf(t.get(0));
    				}
    				stack.push(String.valueOf(temp));
    			}
    		}
    	}
     
    	ArrayList<String> t = new ArrayList<String>();
    	while (!stack.isEmpty()) {
    		String elem = stack.pop();
    		t.add(0, elem);
    	}
     
    	int temp = 0;
    	for (int i = t.size() - 1; i > 0; i = i - 2) {
    		if (t.get(i - 1).equals("-")) {
    			temp += 0 - Integer.valueOf(t.get(i));
    		} else {
    			temp += Integer.valueOf(t.get(i));
    		}
    	}
    	temp += Integer.valueOf(t.get(0));
     
    	return temp;
    }
}
```

