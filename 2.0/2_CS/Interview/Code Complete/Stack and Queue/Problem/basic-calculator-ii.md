# Basic Calculator II

出处

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

You may assume that the given expression is always valid.

Some examples:

    "3+2*2" = 7
    " 3/2 " = 1
    " 3+5 / 2 " = 5

Note: Do not use the eval built-in library function.

## Solution

思路就是两个stack，一个存数字一个存符号。如果遇到数字直接存到数字stack；如果遇到符号，有几种情况：

1.当前符号比上一个符号优先级高，比如* 高于+，那么直接进栈
2.当前符号低于上一个，那么就要把所有已经在stack里面优先于当前符号的全算完，再推进当前符号
3.当前符号是“（”，直接push
4.当前符号是“）”，就要把所有“（”以前的符号全部算完

另一个思路： pass两遍, 第一遍, 先解决乘除, 第二遍, 做加减.

## Complexity

时间复杂度 O(n)，空间复杂度 O(n)

## Code

```java
public class Solution {
    public int calculate(String s) {
        if(s==null || s.length()==0) return 0;  
          
        LinkedList<Integer> list = new LinkedList<Integer>();  
          
        for(int i=0; i<s.length(); i++) {  
            char c = s.charAt(i);  
            if(Character.isDigit(c)) {  
                int cur = c-'0';  
                while(i+1<s.length() && Character.isDigit(s.charAt(i+1))) {  
                    cur = cur * 10 + s.charAt(i+1) - '0';  
                    ++i;  
                }  
                if(!list.isEmpty() && (list.peek() == 2 || list.peek()==3)) {  
                    int op = list.pop();  
                    int opl = list.pop();  
                    int res = 0;  
                    if(op==2) res = opl * cur;  
                    else res = opl / cur;  
                    list.push(res);  
                } else {  
                    list.push(cur);  
                }                 
            } else if(c==' ') continue;  
            else {  
                switch (c) {  
                    case '+': list.push(0);  
                    break;  
                    case '-': list.push(1);  
                    break;  
                    case '*': list.push(2);  
                    break;  
                    case '/': list.push(3);  
                    break;  
                    default: return -1;  
                }  
            }  
        }  
          
        if(list.isEmpty()) return 0;  
        Collections.reverse(list);  
          
        int res = list.poll();  
          
        while(!list.isEmpty()) {  
            int op = list.poll();  
            int opr = list.poll();  
            if(op==0) res += opr;  
            else res -= opr;  
        }  
        return res;  
    }
}
```

