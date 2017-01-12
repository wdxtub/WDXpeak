# Sort Stack

出处

How to sort a stack in ascending order (i.e. pop in ascending order) with another stack?

## Solution

本题明确要求利用两个栈实现一种特定的输出顺序。由于栈限制了输出的顺序，所以要调整栈内部的元素顺序比较困难。但从另一个角度想，我们也许可以在入栈的时候就控制插入的位置，使得栈内的元素都是有序的，即只要保证新栈的元素一定是有序的即可。同时，考虑到栈具有LIFO的输出性质，将一个栈中的元素倾倒到另一个栈，在倾倒回来，元素之间保持原有顺序。

于是我们可以构建如下算法：假设有Stack A和Stack B，Stack A中的元素没有顺序。我们需要把Stack A中的数据有序地加入到Stack B中。每当我们从Stack A中取出一个元素，当该元素不符合Stack B的当前排列顺序时，我们倾倒Stack B的元素，直到该元素可以按顺序入栈。然后，我们恢复之前倾倒的元素。根据栈“将一个栈中的元素倾倒到另一个栈，在倾倒回来，元素之间保持原有顺序”的性质，特别地，我们可以将Stack A看成性质中的“另一个栈”。

## Complexity

由于调整一个元素的顺序可能要求将之前的n个元素来回倾倒，故时间复杂度O(n^2)

## Code

```java
Stack<Integer> sortStack(Stack<Integer> input){
	Stack<Integer> output = new Stack<Integer>();
	while (!input.isEmpty()){
		int value = input.top();
		input.pop();
		while (!output.isEmpty() && output.top() < value){
			input.push(output.top());
			output.pop();
		}
		output.push(value)
	}
	return output;
}
```

