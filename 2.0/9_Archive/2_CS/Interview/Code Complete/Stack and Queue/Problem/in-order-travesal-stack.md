# In Order Travesal with Stack

出处

Given a binary tree, implement the In-Order Traversal using a stack

## Solution

中序遍历(In-Order Traversal)的规则是：1) 先遍历左子树 2) 访问当前节点 3) 遍历右子树。我们先逻辑上重现整个遍历过程，对于某个上层节点，先向左下降到下一层，解决子问题，回到当前节点，向右下降到下一层。很显然，遍历子树的过程是一个自上而下结构：从顶层出发，逐渐向下扩散。实际计算时，我们先解决子问题(遍历左子树)，再利用子问题的结果解决当前问题(访问当前节点，转向右子树)。如果用栈作为辅助结构消除递归，由于子问题是遍历左子树，所以我们将左孩子以自上而下的顺序放入栈，每次弹出时，都意味着子问题已经解决好了，需要解决当前问题，即访问当前节点，再转向右子树。

## Complexity

该算法不重复地扫描所有节点，故时间复杂度O(n)。

## Code

```java
void inordertraversal(Node root){
	if (root == null) return;
	Stack<Node> stack = new Stack<Node>();
	while( !stack.isEmpty() || root != null){
		if (root != null){
			stack.push(root);
			root = root.left;
		} else {
			Node cur = stack.top();
			stack.pop();
			visit(cur);
			root = root.right;
		}
	}
}
```

