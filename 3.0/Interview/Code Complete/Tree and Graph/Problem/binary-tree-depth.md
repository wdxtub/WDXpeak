# Binary Tree Depth

出处

Compute the depth of a binary tree.

## Solution

回顾树的高度定义：从根节点到某个节点的路径长度称为该节点的层数(level)，根节点为第0层，非根节点的层数是其父节点的层数加1。树的高度定义为该树中层数最大的叶节点的层数加1。判断树的高度符合D&C的 条件：对于某个节点，其高度为左子树和右子树高度的较大者加1，即原问题依赖于两个子问题。对于递归的实现，出口为传入节点为空，此时应该返回高度0。

## Complexity

该算法遍历树的所有节点，故复杂度O(n)。

## Code

```java
int depthBT(Node root){
	if (root == null) return 0;
	return Math.max(depthBT(root.left), depthBT(root.right))+1;
}
```


