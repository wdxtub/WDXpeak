# Zigzag Level Order Traversal

出处

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:

Given binary tree {3,9,20,#,#,15,7},

        3
       / \
      9  20
        /  \
       15   7
   
return its zigzag level order traversal as:

    [
      [3],
      [20,9],
      [15,7]
    ]

## Solution

1. Queue + reverse.
2. Two stacks.

## Complexity

时间复杂度 O(n)，空间复杂度 O(n)

## Code

```java
public class Solution {
    public List<List<Integer>> zigzagLevelOrder_1(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if (root == null) return res;
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);
        q.offer(null);
        List<Integer> level = new ArrayList<Integer>();
        int depth = 0;
        while(true) {
            TreeNode node = q.poll();
            if (node != null) {
                level.add(node.val);
                if(node.left!=null) q.offer(node.left);
                if(node.right!=null) q.offer(node.right);
            } else {
                if (depth % 2 == 1) Collections.reverse(level);
                res.add(level);
                depth++;
                level = new ArrayList<Integer>();
                if(q.isEmpty()==true) break;
                q.offer(null);
            }
        }
        return res;   
    }
    public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if (root == null) return res;
        Stack<TreeNode> cur = new Stack<TreeNode>();
        Stack<TreeNode> last = new Stack<TreeNode>();
        boolean left2right = true;
        last.push(root);
        List<Integer> level = new ArrayList<Integer>();
        while (last.empty() == false) {
            TreeNode node = last.pop(); 
            if (node != null) {
                level.add(node.val);
                if (left2right) {
                    if(node.left!=null) cur.push(node.left);
                    if(node.right!=null) cur.push(node.right);
                } else {
                    if(node.right!=null) cur.push(node.right);
                    if(node.left!=null) cur.push(node.left);
                }
            }
            if (last.empty() == true) {
                if (level.size() != 0)
                    res.add(level);
                level = new ArrayList<Integer>();
                Stack<TreeNode> temp = last;
                last = cur;
                cur = temp;
                left2right = !left2right;
            }
        }
        return res;
    }
}
```

