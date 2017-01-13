# Next Node in BST

出处Inorder Successor in BST

In Binary Tree, Inorder successor of a node is the next node in Inorder traversal of the Binary Tree. Inorder Successor is NULL for the last node in Inoorder traversal.

In Binary Search Tree, Inorder Successor of an input node can also be defined as the node with the smallest key greater than the key of input node. So, it is sometimes important to find next node in sorted order.

## Solution

If p has a right subtree, then get its successor from there. Otherwise do a regular search from root to p but remember the node of the last left-turn and return that. Same solution as everyone, I guess, just written a bit shorter. 

## Complexity

Runtime O(h), where h is the height of the tree.

## Code

Iterative Successor

```java
public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
    if (p.right != null) {
        p = p.right;
        while (p.left != null)
            p = p.left;
        return p;
    }
    TreeNode candidate = null;
    while (root != p)
        root = (p.val > root.val) ? root.right : (candidate = root).left;
    return candidate;
}
```


Recursive Successor

```java
public TreeNode successor(TreeNode root, TreeNode p) {
  if (root == null)
    return null;

  if (root.val <= p.val) {
    return successor(root.right, p);
  } else {
    TreeNode left = successor(root.left, p);
    return (left != null) ? left : root;
  }
}
```

Recursive predecessor

```java
public TreeNode predecessor(TreeNode root, TreeNode p) {
  if (root == null)
    return null;

  if (root.val >= p.val) {
    return predecessor(root.left, p);
  } else {
    TreeNode right = predecessor(root.right, p);
    return (right != null) ? right : root;
  }
}
```

