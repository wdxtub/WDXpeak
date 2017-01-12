# Peeking Iterator

Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

Here is an example. Assume that the iterator is initialized to the beginning of the list: [1, 2, 3].

Call next() gets you 1, the first element in the list.

Now you call peek() and it returns 2, the next element. Calling next() after that still return 2.

You call next() the final time and it returns 3, the last element. Calling hasNext() after that should return false.

Hint:

1. Think of "looking ahead". You want to cache the next element.
2. Is one variable sufficient? Why or why not?
3. Test your design with call order of peek() before next() vs next() before peek().
4. For a clean implementation, check out Google's guava library source code.

## Solution

本题目考察设计模式中的装饰器模式（Decorator Pattern）

参阅维基百科Decorator Pattern词条：https://en.wikipedia.org/wiki/Decorator_pattern

In object-oriented programming, the decorator pattern (also known as Wrapper, an alternative naming shared with the Adapter pattern) is a design pattern that allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class. The decorator pattern is often useful for adhering to the Single Responsibility Principle, as it allows functionality to be divided between classes with unique areas of concern.

引入两个额外的变量nextElement和peekFlag

nextElement标识peek操作预先获取的下一个元素，peekFlag记录当前是否已经执行过peek操作

若已知所有元素非空，不使用peekFlag变量也可，参考：https://leetcode.com/discuss/59327/my-java-solution

关于进一步思考，使用Java的泛型可以适用于所有的类型。

```java
// Java Iterator interface reference:
// https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html
class PeekingIterator implements Iterator<Integer> {

    private Iterator<Integer> iterator;
    private boolean peekFlag = false;
    private Integer nextElement = null;
    public PeekingIterator(Iterator<Integer> iterator) {
        // initialize any member here.
        this.iterator = iterator;
    }

    // Returns the next element in the iteration without advancing the iterator.
    public Integer peek() {
        if (!peekFlag) {
            nextElement = iterator.next();
            peekFlag = true;
        }
        return nextElement;
    }

    // hasNext() and next() should behave the same as in the Iterator interface.
    // Override them if needed.
    @Override
    public Integer next() {
        if (!peekFlag) {
            return iterator.next();
        }
        peekFlag = false;
        Integer result = nextElement;
        nextElement = null;
        return result;
    }

    @Override
    public boolean hasNext() {
        return peekFlag || iterator.hasNext();
    }

}
```

