# Binary Tree Right Side View

出处

Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

For example:

Given the following binary tree,

       1            <---
     /   \
    2     3         <---
     \     \
      5     4       <---
  
You should return [1, 3, 4].

## Solution

每一层只取最后加入数组的那一个元素

## Complexity

时间复杂度 O(n)，空间复杂度 O(n)

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
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> result = new ArrayList<Integer>();
        List<TreeNode> curr = new ArrayList<TreeNode>();
        if (root == null) {
            return result;
        }
        
        curr.add(root);
        while (curr.isEmpty() == false) {
            List<TreeNode> next = new ArrayList<TreeNode>();
            for (int i = 0; i < curr.size(); i++) {
                if (i == curr.size() - 1) {
                    result.add(curr.get(i).val);
                }
                
                if (curr.get(i).left != null) {
                    next.add(curr.get(i).left);
                }
                
                if (curr.get(i).right != null) {
                    next.add(curr.get(i).right);
                }
            }
            
            curr.clear();
            curr = next;
        }
        
        return result;
    }
}
```

