# All Path

出处

Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

       1
     /   \
    2     3
     \
      5
  
All root-to-leaf paths are:

["1->2->5", "1->3"]

## Solution

dfs

## Complexity

暂时还不会算

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
    List<String> res = new ArrayList<String>();
    
    public List<String> binaryTreePaths(TreeNode root) {
        if(root != null) findPaths(root,String.valueOf(root.val));
        return res;
    }
    
    private void findPaths(TreeNode n, String path){
        if(n.left == null && n.right == null) res.add(path);
        if(n.left != null) findPaths(n.left, path+"->"+n.left.val);
        if(n.right != null) findPaths(n.right, path+"->"+n.right.val);
    }
}
``` 

