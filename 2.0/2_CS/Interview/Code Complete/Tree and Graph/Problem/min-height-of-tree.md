# Min Height of Binary Tree

给定一个二叉树，找出其最小深度。

二叉树的最小深度为根节点到最近叶子节点的距离。

样例

    给出一棵如下的二叉树:
       1
     /   \
    2     3
        /   \
       4     5
    这个二叉树的最小深度为 2

## Solution

找到没有左右节点的节点就停手，然后返回当时的深度即可，也属于深度优先搜索

## Complexity

时间复杂度 O(n)，空间复杂度 O(h)

## Code

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def minDepth(self, root):
        if root is None:
            return 0

        return self.getMin(root)

    def getMin(self, node):
        if node is None:
            return 99999

        if node.left is None and node.right is None:
            return 1

        return min(self.getMin(node.left), self.getMin(node.right)) + 1

```

