# Stack of Plates

Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore, in real life, we would likely start a new stack when the previous stack exceeds ome threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks and should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack.

FOLLOW UP

    Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.
    
## Solution

```java
class SetOfStacks{
    ArrayList<Stack> stacks = new ArrayList<Stack>();
    public int capacity;

    public SetOfStacks(int capacity){
        this.capacity = capacity;
    }

    public Stack getLastStack(){
        if (stacks.size() == 0){
            return null;
        }
        return stacks.get(stacks.size() - 1);
    }

    public void push(int v){
        Stack last = getLastStack();
        if (last != null && !last.isFull()){
            last.push(v);
        }
        else {
            Stack stack = new Stack(capacity);
            stack.push(v);
            stacks.add(stack);
        }
    }

    public int pop(){
        Stack last = getLastStack();
        if (last == null) throw new EmptyStackException();
        int v = last.pop();
        if (last.size == 0) stacks.remove(stacks.size() - 1);
        return v;
    }

    public boolean isEmpty(){
        Stack last = getLastStack();
        return last == null || last.isEmpty();
    }

    public int popAt(int index){
        return leftShift(index, true);
    }

    public int leftShift(int index, boolean removeTop){
        Stack stack  = stacks.get(index);
        int removed_item;
        if (removeTop) removed_item = stack.pop();
        else removed_item = stack.removeBottom();
        if (stack.isEmpty()){
            stacks.remove(index);
        }
        else if (stacks.size() > index + 1){
            int v = leftShift(index + 1, false);
            stack.push(v);
        }
        return removed_item;
    }
}

class Stack{
    private int capacity;
    public Node top, bottom;
    public int size = 0;

    public Stack(int capacity){
        this.capacity = capacity;
    }

    public boolean isFull(){
        return capacity == size;
    }

    public void join(Node above, Node below){
        if (below != null) below.above = above;
        if (above != null) above.below = below;
    }

    public boolean push(int v){}

    public int pop(){}

    public boolean isEmpty(){}

    public int removeBottom(){}
}
```

