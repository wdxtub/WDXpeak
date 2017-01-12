# Stack of Box

出处

Given a set of boxes, each one has a square bottom and height of 1. Please write a function to return the tallest stack of these boxes. The constraint is that a box can be put on top only when its square bottom is restrictively smaller.

## Solution

放置在当前盒子上的盒子序列是否满足条件，与当前盒子下面已经放好的盒子(前驱条件)无关，只与将要放在当前盒子上的盒子序列有关(后驱节点)，并且在计算后驱条件时，以每个盒子为底的最长序列必然会被反复计算。因此可以将盒子作为Memorization的key，以满足条件的最长序列作为Memorization的value。

## Complexity

以每个盒子为底都需要遍历一次，时间复杂度 O(n^2 )，空间复杂度 O(n)

## Code

```java
ArrayList<Box> stackBox(Box boxes[], Box Bottom, HashMap<Box, ArrayList<Box> stackCache){
	int len = boxes.length;
	if (len == 0) return null;
	
	ArrayList<Box> max_stack;
	int max_height = 0;
	ArrayList<Box> new_stack;
	
	if (stackCache.contains(bottom)){
		return stackCache.get(bottom);
	} else {
		for (int i = 0; i < len; i++){
			if (boxes[i].canBeAbove(bottom)){
				// solve subproblem
				new_stack = stackBox(boxes, boxes[i], stackCache);
			}
			if (new_stack.size() > max_height){
				max_height = new_stack.length();
				max_stack = new_stack;
			}		
		}
	}
	max_stack.insert(0, bottom);
	stackCache.put(bottom, max_stack);
	return max_stack;
}
```


