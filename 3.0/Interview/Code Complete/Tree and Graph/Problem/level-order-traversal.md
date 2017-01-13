# Level Order Traversal

出处

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:

Given binary tree {3,9,20,#,#,15,7},

        3
       / \
      9  20
        /  \
       15   7
   
return its level order traversal as:

    [
      [3],
      [9,20],
      [15,7]
    ]

## Solution

1. Use queue. In order to seperate the levels, use 'NULL' as the end indicator of one level.
2. DFS.

## Complexity

时间复杂度 O(n)，空间复杂度 O(n)

## Code

```java
public class Solution {
    public List<List<Integer>> levelOrder_1(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if (root == null) return res;
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);
        q.offer(null);
        List<Integer> level = new ArrayList<Integer>();
        
        while(true) {
            TreeNode node = q.poll();
            if (node != null) {
                level.add(node.val);
                if(node.left!=null) q.offer(node.left);
                if(node.right!=null) q.offer(node.right);
            } else {
                res.add(level);
                level = new ArrayList<Integer>();
                if(q.isEmpty()==true) break;
                q.offer(null);
            }
        }
        return res;
    }
    
    public List<List<Integer>> levelOrder_2(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if (root == null) return res;
        levelOrderRe(root, 0, res);
        return res;
    }
    public void levelOrderRe(TreeNode root, int level, List<List<Integer>> res) {
        if(root == null) return;
        if(level == res.size()) res.add(new ArrayList<Integer>());
        res.get(level).add(root.val);
        levelOrderRe(root.left, level+1, res);
        levelOrderRe(root.right,level+1, res);
    }
}
```

