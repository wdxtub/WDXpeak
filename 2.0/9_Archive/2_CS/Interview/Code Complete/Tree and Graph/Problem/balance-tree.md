# Balance Tree

出处

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

## Solution

回顾二叉树是否平衡的定义：一颗二叉树是平衡的，当且仅当左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。同时，注意特例，空树是一棵平衡二叉树。子树平衡是全局问题的一部分，因此可以通过子问题的结果来推断全局的结果：判断高度差的绝对值不超过1，以及递归左右子树都为平衡二叉树。

计算高度的子函数我们也可以用递归来实现。首先，考虑递归的出口：当node为空的时候，高度应该为0。其次，如果node不为空，那么这棵树的高度应该为左右子树中的高度较高者加1。

## Complexity

对于这个实现，isBalanced函数对于每个节点只运行一次。然而，level函数会进行很多重复的计算：每次进入isBalanced函数，调用level会遍历一遍所有子节点。原因在于level函数没有记忆性，当输入为同一个节点时，level函数会再次进行完整的计算。

一种改进方式是，可以考虑利用动态编程的思想，将TreeNode指针作为键，高度作为值，一旦发现节点已经被计算过，直接返回结果，这样，level函数对每个节点只计算一次。另一种更为巧妙的方法是，isBalanced返回当前节点的高度，用-1表示树不平衡。 将计算结果自底向上地传递，并且确保每个节点只被计算一次，复杂度O(n)。

## Code

有重复计算的方法

```java
int level(Node root){
	if (root == null) return 0;
	return Math.max(level(root.left), level(root.right)) + 1
}

boolean isBalanced(Node root){
	if (root == null) return true;
	int delta = abs(level(root.left) - level(root.right));
	return delta < 2 && isBalanced(root.left) && isBalaned(root.right);
}
```

无重复计算的方法，返回当前节点的高度

```java
int curHeight(Node root){
	if (root == null) 
		return 0;
		
	int left = curHeight(root.left);
	if (left == -1){
		return -1;
	}
	
	int right = curHeight(root.right);
	if (right == -1){
		return -1;
	}
	
	if (abs(left - right) > 1){
		return -1;
	}
	
	return Math.max(left, right) + 1;
}

bool isBalance(Node root){
	if (curHeight(root) == -1){
		return false;
	}
	return true;
}
```

