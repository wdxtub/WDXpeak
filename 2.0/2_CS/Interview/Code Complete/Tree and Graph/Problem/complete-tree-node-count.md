# Complete Tree Node Count

出处

Given a complete binary tree, count the number of nodes.

Definition of a complete binary tree from Wikipedia:

In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

## Solution

Steps to solve this problem:

1. get the height of left-most part
2. get the height of right-most part
3. when they are equal, the # of nodes = 2^h -1
4. when they are not equal, recursively get # of nodes from left&right sub-trees

## Complexity

时间复杂度 O(h)，空间复杂度 O(1)

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
    public int countNodes(TreeNode root) {
        if(root==null)
        return 0;
 
        int left = getLeftHeight(root)+1;    
        int right = getRightHeight(root)+1;
     
        if(left==right){
            return (2<<(left-1))-1;
        }else{
            return countNodes(root.left)+countNodes(root.right)+1;
        }
    }
     
    public int getLeftHeight(TreeNode n){
        if(n==null) return 0;
     
        int height=0;
        while(n.left!=null){
            height++;
            n = n.left;
        }
        return height;
    }
     
    public int getRightHeight(TreeNode n){
        if(n==null) return 0;
     
        int height=0;
        while(n.right!=null){
            height++;
            n = n.right;
        }
        return height;
    }
}
``` 

