# Implement Stack using Queues

mplement the following operations of a stack using queues.

+ push(x) -- Push element x onto stack.
+ pop() -- Removes the element on top of the stack.
+ top() -- Get the top element.
+ empty() -- Return whether the stack is empty.

Notes:

+ You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
+ Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
+ You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

## Solution

这道题让我们用队列来实现栈，队列和栈作为两种很重要的数据结构，它们最显著的区别就是，队列是先进先出，而栈是先进后出。题目要求中又给定了限制条件只能用queue的最基本的操作，像back()这样的操作是禁止使用的。那么怎么样才能让先进先出的特性模拟出先进后出呢，这里就需要另外一个队列来辅助操作，我们总共需要两个队列，其中一个队列用来放最后加进来的数，模拟栈顶元素。剩下所有的数都按顺序放入另一个队列中。当push操作时，将新数字先加入模拟栈顶元素的队列中，如果此时队列中有数字，则将原本有的数字放入另一个队中，让新数字在这队中，用来模拟栈顶元素。当top操作时，如果模拟栈顶的队中有数字则直接返回，如果没有则到另一个队列中通过平移数字取出最后一个数字加入模拟栈顶的队列中。当pop操作时，先执行下top()操作，保证模拟栈顶的队列中有数字，然后再将该数字移除即可。当empty操作时，当两个队列都为空时，栈为空。

```java
class MyStack {
    LinkedList<Integer> queue1 = new LinkedList<Integer>();
    LinkedList<Integer> queue2 = new LinkedList<Integer>();
 
    // Push element x onto stack.
    public void push(int x) {
        if(empty()){
            queue1.offer(x);
        }else{
            if(queue1.size()>0){
                queue2.offer(x);
                int size = queue1.size();
                while(size>0){
                    queue2.offer(queue1.poll());
                    size--;
                }
            }else if(queue2.size()>0){
                queue1.offer(x);
                int size = queue2.size();
                while(size>0){
                    queue1.offer(queue2.poll());
                    size--;
                }
            }
        }
    }
 
    // Removes the element on top of the stack.
    public void pop() {
        if(queue1.size()>0){
            queue1.poll();
        }else if(queue2.size()>0){
            queue2.poll();
        }
    }
 
    // Get the top element.
    public int top() {
       if(queue1.size()>0){
            return queue1.peek();
        }else if(queue2.size()>0){
            return queue2.peek();
        }
        return 0;
    }
 
    // Return whether the stack is empty.
    public boolean empty() {
        return queue1.isEmpty() & queue2.isEmpty();
    }
}
```

