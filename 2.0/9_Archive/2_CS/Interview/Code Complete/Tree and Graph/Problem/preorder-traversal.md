# Preorder Traversal

出处

Given a binary tree, return the preorder traversal of its nodes' values.

For example:

Given binary tree {1,#,2,3},

       1
        \
         2
        /
       3
   
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?

## Solution

1. Iterative way (stack).   Time: O(n), Space: O(n).
2. Recursive solution.      Time: O(n), Space: O(n).
3. Threaded tree (Morris).  Time: O(n), Space: O(n/1). 

## Complexity

见上

## Code

```java
/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public List<Integer> preorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        if(root == null) return res;
        res.add(root.val);
        List<Integer> left = preorderTraversal(root.left);
        List<Integer> right = preorderTraversal(root.right);
        res.addAll(left);
        res.addAll(right);
        return res;
    }
    
    public void preorderTraversalRe(TreeNode root, List<Integer> res) {
        if (root == null) return;
        res.add(root.val);
        preorderTraversalRe(root.left, res);
        preorderTraversalRe(root.right, res);
    }
    
    public List<Integer> preorderTraversal_2(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        if(root == null) return res;
        preorderTraversalRe(root, res);
        return res;
    }
    
    public List<Integer> preorderTraversal_3(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        if(root == null) return res;
        Stack<TreeNode> stk = new Stack<TreeNode>();
        stk.push(root);
        while (stk.isEmpty() == false) {
            TreeNode cur = stk.pop();
            res.add(cur.val);
            if (cur.right != null) stk.push(cur.right);
            if (cur.left != null) stk.push(cur.left);
        }
        return res;
    }
    
    
    public List<Integer> preorderTraversal_4(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        if(root == null) return res;
        Stack<TreeNode> stk = new Stack<TreeNode>();
        TreeNode cur = root;
        while (stk.isEmpty() == false || cur != null) {
            if (cur != null) {
                stk.push(cur);
                res.add(cur.val);
                cur = cur.left;
            } else {
                cur = stk.pop();
                cur = cur.right;
            }
        }
        return res;
    }
    
    
    public List<Integer> preorderTraversal_5(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        if(root == null) return res;
        TreeNode cur = root;
        while (cur) {
            if (cur.left == null) {
                res.add(cur.val);
                cur = cur.right;
            } else {
                TreeNode node = cur.left;
                while (node.right != null && node.right != cur)
                    node = node.right;
                if (node == null) {
                    node.right = cur;
                    res.add(cur.val);
                    cur = cur.left;
                } else {
                    node.right = null;
                    cur = cur.right;
                }
            }
        }
        return res;
    }
}
```

