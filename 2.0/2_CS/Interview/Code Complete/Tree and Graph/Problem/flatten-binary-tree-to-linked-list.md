# Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.

For example,
Given

         1
        / \
       2   5
      / \   \
     3   4   6
     
The flattened tree should look like:

    1
     \
      2
       \
        3
         \
          4
           \
            5
             \
              6

Hints:
If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.

## Solution

Recursion. Return the last element of the flattened sub-tree.

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
public class Solution {
    public void flatten(TreeNode root) {
        flatten_3(root);
    }
    
    public void flatten_1(TreeNode root) {
        if (root == null) return;
        flatten_1(root.left);
        flatten_1(root.right);
        if (root.left == null) return;
        TreeNode node = root.left;
        while (node.right != null) node = node.right;
        node.right = root.right;
        root.right = root.left;
        root.left = null;
    }
    
    public void flatten_2(TreeNode root) {
        if (root == null) return;
        Stack<TreeNode> stk = new Stack<TreeNode>();
        stk.push(root);
        while (stk.empty() == false) {
            TreeNode cur = stk.pop();
            if (cur.right != null) stk.push(cur.right);
            if (cur.left != null) stk.push(cur.left);
            cur.left = null;
            cur.right = stk.empty() == true ? null : stk.peek();
        }
    }
    
    public TreeNode flattenRe3(TreeNode root, TreeNode tail) {
        if (root == null) return tail;
        root.right = flattenRe3(root.left, flattenRe3(root.right, tail));
        root.left = null;
        return root;
    }
    public void flatten_3(TreeNode root) {
        if (root == null) return;
        flattenRe3(root, null);
    }
}
```

