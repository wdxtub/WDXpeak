# Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

        1
       / \
      2   2
     / \ / \
    3  4 4  3

But the following is not:

        1
       / \
      2   2
       \   \
       3    3

Note:

Bonus points if you could solve it both recursively and iteratively.

## Solution

Recursive solution

## Code

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public boolean isSymmetric(TreeNode root) {
        if (root == null) return true;
        return solve (root.left, root.right);
    }
    
    public boolean solve(TreeNode t1, TreeNode t2) {
        if (t1 == null && t2 == null) return true;
        if (t1 == null && t2 != null || t1 != null && t2 == null || t1.val != t2.val) return false;
        return solve(t1.left, t2.right) && solve(t1.right, t2.left);
    }
}
```

