# Max Stack

出处

Design a stack with push(), pop() and max() in O(1) time.

## Solution

在push的时候记录当前的最大值十分显然，只需要在插入当前值的时候比较是否比现在的最大值大，如果是，更新最大值即可。问题在于如何恰当处理pop的情况：直观想法是，当需要出栈的元素是当前最大值，则需要“回溯”到前一个最大值。考虑到栈具有LIFO的特性，那么与之匹配地，最大值追踪方式也需要具有相同特性：不妨用另一个栈追踪最大值。注意一个细节，当最大值重复入栈时，我们的“最大值栈”也需要重复记录该值。否则，在弹出第一个重复最大值的时候，我们就可能在最大值栈中丢失相应的信息。

## Complexity

时间复杂度符合题目要求为O(1)。空间复杂度最坏情况附加的栈中需要存储每个元素，故额外使用O(n)空间。

## Code 

```java
class MaxStack{
	private Stack<Integer> valueStack;
	private Stack<Integer> maxStack;
	
	public void push(int value){
		valueStack.push(value);
		if (maxStack.isEmpty() || value > maxStack.top()){
			maxStack.push(value);
		}
	}
	
	public void pop(){
		int value = valueStack.top();
		valueStack.pop();
		if (value == maxStack.top()){
			maxStack.pop();
		}
	}
	
	public int max(){
		return maxStack.top();
	}
}
```


