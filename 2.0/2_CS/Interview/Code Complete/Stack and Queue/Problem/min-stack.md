# Min Stack

实现一个带有取最小值min方法的栈，min方法将返回当前栈中的最小值。

你实现的栈将支持push，pop 和 min 操作，所有操作要求都在O(1)时间内完成。

样例

    如下操作：push(1)，pop()，push(2)，push(3)，min()， push(1)，min() 返回 1，2，1

注意

    如果堆栈中没有数字则不能进行min方法的调用

## Solution

维护另一个 stack 即可

## Complexity

均为 O(1)

## Code 

```java
public class Solution {
    private Stack<Integer> stack;
    private Stack<Integer> minStack;
    public Solution() {
        stack = new Stack<Integer>();
        minStack = new Stack<Integer>();
    }

    public void push(int number) {
        stack.push(number);
        if (minStack.isEmpty()) {
            minStack.push(number);
        } else {
            minStack.push(Math.min(number, minStack.peek()));
        }
    }

    public int pop() {
        minStack.pop();
        return stack.pop();
    }

    public int min() {
        return minStack.peek();
    }
}
```

