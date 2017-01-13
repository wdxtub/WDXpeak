# Is Subtree

出处

T1 and T2 are two very large binary trees, with T1 much bigger than T2. Create an algorithm to determine if T2 is a subtree of T1.

A tree T2 is a subtree of T1 if there exists a node n in T1 such that the subtree of n is identical to T2. That is, if you cut off the tree at node n, the two trees would be identical.

## Solution

根据题意，比较容易想到的是我们需要实现一个matchTree辅助函数，用以判断根节点为root1和root2的两棵树是否完全相等。判断两棵树相等的定义符合采用D&C的条件：原问题的答案取决于左子树右子树都相等这两个子问题 。对于递归的实现，出口为root1 == NULL && root2 == NULL，递归函数需要判断当前节点是否相等，左子树是否相等和右子树是否相等。

其次，考虑在什么情况下我们需要调用matchTree：当Tree1的当前节点与Tree2的根节点相等时，我们有兴趣调用matchTree判断以Tree1当前节点为根的子树是否与Tree2相等。那么如果不相等怎么办？我们同样可以利用递归的思想，“将当前节点的左子树或右子树是否包含Tree2作为子问题，通过递归调用自身获得结果。

## Complexity

假设Tree1有M个节点，Tree2有N个节点。最坏情况下，对于Tree1的每个节点，都需要调用matchTree函数，并且matchTree在基本遍历完Tree2后才能返回结果。此时，时间复杂度为O(MN)。

## Code

```java
boolean isSubtree(Node tree1, Node tree2){
	if (tree2 == null){
		return true;
	}
	if (tree1 == null){
		return false;
	}
	
	if (tree1.value == tree2.value){
		if (matchTree(tree1, tree2){
			return true;
		}
	}
	
	return (isSubtree(tree1.left, tree2) || isSubtree(tree1.right, tree2));
}

boolean matchTree(Node tree1, Node tree2){
	if (tree1 == null && tree2 == null){
		return true;
	}
	if (tree1 == null || tree2 == null){
		return false;
	}
	if (tree1.value != tree2.value){
		return false;
	}
	return matchTree(tree1.left, tree2.left) && matchTree(tree1.right, tree2.right);
}

```


