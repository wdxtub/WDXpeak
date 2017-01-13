# Reverse Binary Tree

样例

      1         1
     / \       / \
    2   3  => 3   2
       /       \
      4         4

挑战

    递归固然可行，能否写个非递归的？

## Solution

基本翻转即可

## Complexity

时间复杂度 O(n)，空间复杂度 非递归O(1) 递归O(h) 

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
    public TreeNode invertTree(TreeNode root) {
        if(root!=null){
            helper(root);
        }
     
        return root;    
    }
     
    public void helper(TreeNode p){
     
        TreeNode temp = p.left;
        p.left = p.right;
        p.right = temp;
     
        if(p.left!=null)
            helper(p.left);
     
        if(p.right!=null)
            helper(p.right);
    }
    
    public TreeNode invertTree_2(TreeNode root) {
        LinkedList<TreeNode> queue = new LinkedList<TreeNode>();
     
        if(root!=null){
            queue.add(root);
        }
     
        while(!queue.isEmpty()){
            TreeNode p = queue.poll();
            if(p.left!=null)
                queue.add(p.left);
            if(p.right!=null)
                queue.add(p.right);
     
            TreeNode temp = p.left;
            p.left = p.right;
            p.right = temp;
        }
     
        return root;    
    }
}
```

---

递归版本

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def invertBinaryTree(self, root):
        if root is None:
            return None
        if root.left:
            self.invertBinaryTree(root.left)
        if root.right:
            self.invertBinaryTree(root.right)
        root.left, root.right = root.right, root.left
        return root

```

非递归版本

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def invertBinaryTree(self, root):
        if root is None:
            return None
        queue = [root]
        while queue:
            front = queue.pop(0)
            if front.left:
                queue.append(front.left)
            if front.right:
                queue.append(front.right)
            front.left, front.right = front.right, front.left
        return root

```

