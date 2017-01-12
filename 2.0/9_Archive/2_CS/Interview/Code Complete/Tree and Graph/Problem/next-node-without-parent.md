# Next Node without Parent

出处

In-order traverse a binary search tree without parent links, find the next node to visit given a specific node.

## Solution

对于该节点有右子树的情况，由于我们不需要利用父节点信息倒推，故搜索过程与上题一致：中序后继节点就是右子树中最左的节点。在其他情况下，我们需要从根部开始搜索。对于根节点，我们应该如何判断继续搜索左子树还是右子树？对于BST，中序遍历的后继节点就是值比当前节点大的所有节点中最小的那个。因此，一旦根节点大于当前节点，我们存储当前节点，并且往数值减小的方向搜索(左子树)；一旦根节点小于当前节点，我们继续往数值增大的方向搜索(右子树)。这样，当算法执行完成，我们存储的最后一个节点一定恰好大于给定节点，即是给定节点的中序遍历后继。

## Complexity

算法复杂度同上题：平均情况下，复杂度为O(h)，h为树的高度。

## Code

```java
Node nextNode(Node node, Node root){
	if (node == null) return null;
	if (head == null) return null;
	
	if (node.right != null){
		return leftMostChild(node.right);
	} else {
		Node next = null;
		while (root != null){
			if (root.value > node.value){
				next = root;
				root = root.left;
			} else {
				root = root.right;
			}
		}
	}
	return next;
}

Node leftMostChild(Node node){
	if (node == null) return null;
	while (node.left != null){
		node = node.left;
	}
	return node;
}
```

