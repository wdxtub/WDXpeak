# Recover Binary Search Tree

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Note:

A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

## Solution & Complexity

1. recursive solution. O(n) space. get inorder list first.
2. recursive solution. O(n) space. with only auxiliary two pointers.
3. Use a stack. Iteration.
4. Morris inorder traversal. O(1) space. with only auxiliary two pointers.

## Code

```java
public class Solution {
    public void recoverTree_1(TreeNode root) {
        if (root == null) return;
        ArrayList<TreeNode> res = new ArrayList<TreeNode>();
        inorderTraversal(root, res);
        TreeNode first = null, second = null;
        for (int i = 1; i < res.size(); ++i) {
            if (res.get(i).val > res.get(i-1).val)
                continue;
            if (first == null) first = res.get(i-1);
            second = res.get(i);
        }
        if (first == null) return;
        int tmp = first.val;
        first.val = second.val;
        second.val = tmp;
    }
    public void inorderTraversal(TreeNode root, ArrayList<TreeNode> res) {
        if (root == null) return;
        inorderTraversal(root.left, res);
        res.add(root);
        inorderTraversal(root.right, res);
    }
    
    
    public void recoverTree_2(TreeNode root) {
        if (root == null) return;
        TreeNode[] res = new TreeNode[3];// 0->pre, 1->first, 2->second
        recoverRe2(root, res);
        int tmp = res[1].val;
        res[1].val = res[2].val;
        res[2].val = tmp;
    }
    public void recoverRe2(TreeNode root, TreeNode[] res) {
        if (root == null) return;
        recoverRe2(root.left, res);
        if (res[0] != null && res[0].val > root.val) {
            if (res[1] == null) res[1] = res[0];
            res[2] = root;
        }
        res[0] = root;
        recoverRe2(root.right, res);
    }
    
    public void recoverTree_3(TreeNode root) {
        if (root == null) return;
        Stack<TreeNode> stk = new Stack<TreeNode>();
        TreeNode cur = root, pre = null, first = null, second = null;
        while (stk.isEmpty() == false || cur != null) {
            if (cur != null) {
                stk.push(cur);
                cur = cur.left;
            } else {
                cur = stk.pop();
                if (pre != null && pre.val > cur.val) {
                    if (first == null) first = pre;
                    second = cur;
                }
                pre = cur;
                cur = cur.right;
            }
        }
        if (first == null) return;
        int tmp = first.val;
        first.val = second.val;
        second.val = tmp;
    }

    public void recoverTree_4(TreeNode root) {
        if (root == null) return;
        TreeNode cur = root, pre = null, first = null, second = null;
        while (cur != null) {
            if (cur.left == null) {
                if (pre != null && pre.val > cur.val) {
                    if (first == null) first = pre;
                    second = cur;
                }
                pre = cur;
                cur = cur.right;
            } else {
                TreeNode node = cur.left;
                while (node.right != null && node.right != cur)
                    node = node.right;
                if (node.right != null) {
                    if (pre != null && pre.val > cur.val) {
                        if (first == null) first = pre;
                        second = cur;
                    }
                    pre = cur;
                    node.right = null;
                    cur = cur.right;
                } else {
                    node.right = cur;
                    cur = cur.left;
                }
            }
        }
        if (first == null) return;
        int tmp = first.val;
        first.val = second.val;
        second.val = tmp;
    }
}
```

