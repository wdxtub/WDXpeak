# Valid Binary Search Tree

出处

Check if a binary tree is a Binary Search Tree (BST), you may assume there is no element having same value.

## Solution

首先考虑BST的定义：对于二分查找树的任意节点，该节点存储的数值一定比左子树的所有节点的值大比右子树的所有节点的值小。并且中序遍历能够获得从小到大排列的有序数组。

根据BST的中序遍历特性，非常直观的想法是：可以通过中序遍历将这棵二叉树线性化，然后遍历数据，考察数组是否有序。然而，这样的方法并不是最优的，原因在于我们至少遍历整棵树，而不是一旦发现该树不是BST立刻返回结果。此外，遍历完成后还需要再遍历一遍额外的数组空间以判断是否有序，故该方法整体额外开销较大。

事实上，问题的定义符合采用D&C的条件：子树是BST的是原问题的一部分；对于递归调用的函数而言，节点代表的树与子节点代表的树是同样的结构。考虑到对于BST的判断，我们需要左子树均小于当前节点，右子树均大于当前节点，故可以将当前节点作为最小或最大值传入。为了函数接口的统一，一个小技巧是：可以同时传入最小／最大值，并且将初始值设为`INT_MIN`，`INT_MAX`，这样，其左子树所有节点的值必须在 `INT_MIN`及根节点的值之间，其右子树所有节点的值必须在根节点的值以及`INT_MAX`之间。“从递归的角度看，不难得出递归方式是：判断`root->value > min && root->value < max` (root->value为`INT_MIN`或`INT_MAX`的情况需要特殊处理)，以及递归左右子树都为BST。同时，注意特例，空树是一棵BST，该特例可以最为递归的出口。

## Complexity

根据解题分析的描述，算法需要遍历所有节点，故时间复杂度为O(n)。

## Code

```java
boolean helper(Node root, int min, int max){
	if (root == null) return true;
	if ((root.value < max || root.value == Integer.MAX_INT && root.right == null) && (root.value > min || root.value == Integer.MIN_INT && root.left == null) && helper(root.left, min, root.value) && helper(root.right, root.value, max))){
		return true;
	}
	return false;
}

boolean isValidBST(Node root){
	return helper(root, Integer.MIN_INT, Integer.MAX_INT);
}
```


