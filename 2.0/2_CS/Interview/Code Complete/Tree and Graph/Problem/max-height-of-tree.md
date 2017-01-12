# Height of Binary Tree

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的距离。

样例

    给出一棵如下的二叉树:
      1
     / \
    2   3
       / \
      4   5
    这个二叉树的最大深度为3.

## 题解

这里先整一个递归的，就是逐层遍历，深度优先

## Complexity

时间复杂度 O(n),空间复杂度 O(h)

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
    def maxDepth(self, root):
        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        if left < right:
            return right + 1
        else:
            return left + 1

```

