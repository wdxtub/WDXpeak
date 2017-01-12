# Inorder Traversal

出处

Given a binary tree, return the inorder traversal of its nodes' values.

For example:

Given binary tree {1,#,2,3},

       1
        \
         2
        /
       3
       
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?

## Solution

1. Recursive solution.      Time: O(n), Space: O(n).
2. Iterative way (stack).   Time: O(n), Space: O(n).
3. Threaded tree (Morris).  Time: O(n), Space: O(1).

## Complexity

见上

## Code

```java
public class Solution {
    public List<Integer> inorderTraversal_1(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        if (root == null) return res;
        inorder(root, res);
        return res;
    }
    public void inorder(TreeNode root, List<Integer> res) {
        if (root == null) return;
        inorder(root.left, res);
        res.add(root.val);
        inorder(root.right, res);
    }
    
    
    public List<Integer> inorderTraversal_2(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        Stack<TreeNode> stk = new Stack<TreeNode>();
        TreeNode cur = root;
        while (stk.isEmpty() == false || cur != null) {
            if (cur != null) {
                stk.push(cur);
                cur = cur.left;
            } else {
                cur = stk.pop();
                res.add(cur.val);
                cur = cur.right;
            }
        }
        return res;
    }
    
    
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        TreeNode cur = root;
        while (cur != null) {
            if (cur.left == null) {
                res.add(cur.val);
                cur = cur.right;
            } else {
                TreeNode node = cur.left;
                while (node.right != null && node.right != cur)
                    node  = node.right;
                if (node.right == null) {
                    node.right = cur;
                    cur = cur.left;
                } else {
                    res.add(cur.val);
                    node.right = null;
                    cur = cur.right;
                }
            }
        }
        return res;
    }
}

```

