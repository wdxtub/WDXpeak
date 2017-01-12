# Stacks and Queues

## 解题策略

+ 考虑到栈具有LIFO的特性，那么与之匹配地，最大值追踪方式也需要具有相同特性：不妨用另一个栈追踪最大值。
+ 遍历子树的过程是一个自上而下结构：从顶层出发，逐渐向下扩散。所以考虑递归或者栈。
+ 从最基本的情况出发，根据题意推倒整个计算流程。这样做的好处是：1) 确保自己正确地理解了题目 2) 从简单的情况出发，找找解题思路。该方法特别适用于递归，动态编程等题目类型。
+ 由于栈具有LIFO的特性，如需实现任何特定顺序的读取操作，往往可以借助两个栈互相“倾倒”来实现特定顺序。事实上，在很多情况下，栈并不是实现这种读取顺序的最佳数据结构。但作为面试问题，往往面试官会很明确的说明用栈实现。此时，我们就应该立刻想到利用另一个栈作为辅助。
+ 有一类问题有这样的特性：当前节点的解依赖后驱节点。也就是说，对于某个当前节点，如果不能获知后驱节点，就无法得到有意义的解。这类问题可以通过栈(或等同于栈的若干个临时变量)解决：先将当前节点入栈，然后看其后继节点的值，直到其依赖的所有节点都完备时，再从栈中弹出该节点求解。某些时候，甚至需要反复这个过程：将当前节点的计算结果再次入栈，直到其依赖的后继节点完备。
+ 所谓的自上而下(Top-Down)结构，从逻辑理解的角度来看，实际上就是一种树形结构，从顶层出发，逐渐向下扩散，例如二叉树的遍历问题。 在实际运算的时候，我们先解决子问题，再利用子问题的结果解决当前问题。从算法角度而言，就是利用递归。用递归解决自上而下结构的问题，详见第7章。
+ 由于栈的LIFO特性，可以利用栈数据结构消除递归。递归通常用函数调用自身实现，在调用的时候系统会分配额外的空间，并且需要用栈指针记录函数返回的位置，故额外开销(overhead)比较大。但在实际工作或面试中，往往用栈或者用递归的区别不大，按照自己擅长的方式做就可以。在使用栈的时候， 每个子问题应当被看成是同样类型的对象(object)，将该对象按照自上而下“的方向入栈。然后通过while循环，调用栈的pop()函数弹出栈顶元素并访问，直至栈清空。这样，后入栈的子问题会优先被弹出，相当于实现了递归。

## 栈

栈(stack)是一种数据结构，可以实现后进先出(Last in first out, LIFO)。通常情况下，我们可以用栈作为辅助，实现深度优先算法(Depth first search, DFS)，或者将递归转为while循环。在本书第4章中，可以看到这样的实例。

事实上，递归本身就是相当于把函数本身一层一层地加到操作系统的内存栈上，所以利用栈数据结构去实现递归也是非常自然的：入栈操作相当于递归调用自身，出栈操作相当于递归返回。入栈操作的对象相当于需要被解决的问题，出栈对象相当于已经解决的子问题，通过共享的状态变量或返回值把子问题的结果传递出来。

最基本的栈至少包括入栈(push)和出栈(pop)，前者将一个元素放入栈内，后者将最后放入栈的元素弹出。

## 队列

与栈对称，队列(Queue)帮助实现先进先出(First in first out, FIFO)，我们可以用Queue作为辅助，实现广度优先算法(Breadth first search, BFS)。在第5章可以看到这样的实例。队列还可以作为buffer，构建一个生产者－消费者模型：生产者把新的元素加到队尾，消费者从队头读取元素。在有两个线程同时读取同一个队列时，需要考虑同步(synchronization)，具体问题在第11章中讨论。

事实上，栈 与队列可以视作封装好的链表，只是限制了访问和插入的自由。因此适用栈或队列的情境，也可以考虑使用更为强大的链表。

## 工具箱

### 栈

栈在C++标准模版库(Standard Template Library, STL)中实现，使用时需要include<stack>。 简要介绍如下常见函数，更多信息请参考[这里](http://www.cplusplus.com/reference/stack/stack/)：

```
// Returns whether the stack is empty: i.e. whether its size is zero.
bool empty() const;    

// Inserts a new element at the top of the stack. The content of this new element is initialized to a copy of val.
void push (const value_type& val);    

Example:
stack<int> myStack;
myStack.push(10);    // stack has one element, the value of which is 10
```

注意：如果放入一个类的实例(instance)，会调用复制构造函数(copy constructor)

```
// Removes the element on top of the stack, effectively reducing its size by one.
void pop();    

Example:
stack<int> myStack;
myStack.push(10);
myStack.push(20);    // stack now has two elements, the value of which is 20, 10
myStack.pop();    // stack now has one element, the value of which is 10

// Returns a reference to the top element in the stack
value_type& top();    

Example:
stack<int> myStack;
myStack.push(10);
myStack.push(20);
int value = myStack.top();    // value equals to 20
```

### 队列

队列在C++标准模版库(Standard Template Library, STL)中实现，使用时需要include<queue>。 简要介绍如下常见函数，更多信息请参考[这里](http://www.cplusplus.com/reference/queue/queue/)：

```
// Returns whether the queue is empty
bool empty() const;    

 // Inserts a new element at the end of the queue. The content of this new element is initialized to val.
void push (const value_type& val);   

Example:
queue<int> myQueue;
myQueue.push(10);    // queue has one element, the value of which is 10
```

注意：如果放入一个类的实例(instance)，会调用复制构造函数(copy constructor)

```
// Removes the oldest element in the queue, effectively reducing its size by one.
void pop();    

Example:
queue<int> myQueue;
myQueue.push(10);
myQueue.push(20);
int value = myQueue.front();    // value equals to 10

// Returns a reference to the oldest element in the queue.
value_type& front();    

Example:
queue<int> myQueue;
myQueue.push(10);
myQueue.push(20);    // queue now has two elements, the value of which is 10, 20
myQueue.pop();     // queue now has one element, the value of which is 20
```

