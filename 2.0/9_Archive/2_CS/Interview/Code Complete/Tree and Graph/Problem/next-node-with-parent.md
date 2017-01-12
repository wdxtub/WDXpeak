# Next Node

出处

In-order traverse a binary tree with parent links, find the next node to visit given a specific node.

## Solution

根据中序遍历的性质，我们可以分几种情况来考虑目标节点与给定节点的关系：1，如果该节点有右子树，那么，中序后继节点就是右子树中最左的节点。2，如果没有右子树，那么考虑该节点与其父节点的关系：如果它是父节点的左孩子，那么，父节点就是它的后继。3，如果它是父节点的右孩子，那么我们可以向上倒推，直到某个节点(或者不存在这样的节点，返回空指针)是其父节点的左孩子。

## Complexity

最坏情况下，考虑一棵树只有右孩子，而输入恰好是最右节点。在这个情况下，我们需要向上倒推遍历所有节点，此时复杂度O(n)。平均情况下，复杂度为O(h)，h为树的高度。

## Code

```java
Node nextNode(Node node){
	if (node == null) return null;
	if (node.right != null) {
		return leftMostChild(node.right);
	} else {
		Node parent = node.parent;
		while (node == parent.right || parent == null){
			node = parent;
			parent = parent.parent;
		}
		return parent;
	}
}

Node leftMostChild(Node node){
	if (node == null){
		return null;
	}
	
	while( node.left != null){
		node = node.left;
	}
	return node;
}
```


