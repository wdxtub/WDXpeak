# Queue of Stack

出处

Implement the following operations of a queue using stacks.

+ push(x) -- Push element x to the back of queue.
+ pop() -- Removes the element from in front of queue.
+ peek() -- Get the front element.
+ empty() -- Return whether the queue is empty.

Notes:

+ You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
+ Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
+ You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).

## Solution

这是一道比较常见的题目。 栈的输出顺序是LIFO，queue的输出顺序是FIFO，考虑到如果想利用栈实现特定顺序的读取操作，往往可以借助两个栈互相“倾倒”来实现特定顺序：当一个栈中的元素倾倒到另一个栈中，则原栈最后出栈的元素最先出栈，相当于实现了FIFO。

## Complexity

出栈由于多了倾倒的过程，故时间复杂度降为O(n)。空间复杂度不变，因为并没有重复存储元素。

## Code

```java
class MyQueue {
    Stack<Integer> temp = new Stack<Integer>();
    Stack<Integer> value = new Stack<Integer>();
 
    // Push element x to the back of queue.
    public void push(int x) {
        if(value.isEmpty()){
            value.push(x);
        }else{
            while(!value.isEmpty()){
                temp.push(value.pop());
            }
 
            value.push(x);
 
            while(!temp.isEmpty()){
                value.push(temp.pop());
            }    
        }
    }
 
    // Removes the element from in front of queue.
    public void pop() {
        value.pop();
    }
 
    // Get the front element.
    public int peek() {
        return value.peek();
    }
 
    // Return whether the queue is empty.
    public boolean empty() {
        return value.isEmpty();
    }
}
```

