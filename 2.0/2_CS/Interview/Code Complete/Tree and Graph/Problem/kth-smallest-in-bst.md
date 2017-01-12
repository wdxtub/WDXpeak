# Kth Smallest Element in a BST

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 

You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:

What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

## Solution

We can inorder traverse the tree and get the kth smallest element. Time is O(n).

## Complexity

时间复杂度 O(n)，空间复杂度 O(h)

## Code

如果BST节点TreeNode的属性可以扩展，则再添加一个属性leftCnt，记录左子树的节点个数

记当前节点为node

当node不为空时循环：

若k == node.leftCnt + 1：则返回node

否则，若k > node.leftCnt：则令k -= node.leftCnt + 1，令node = node.right

否则，node = node.left

上述算法时间复杂度为O(BST的高度)

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
    public int kthSmallest(TreeNode root, int k) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
 
        TreeNode p = root;
        int result = 0;
     
        while(!stack.isEmpty() || p!=null){
            if(p!=null){
                stack.push(p);
                p = p.left;
            }else{
                TreeNode t = stack.pop();
                k--;
                if(k==0)
                    result = t.val;
                p = t.right;
            }
        }
     
        return result;
    }
}
```



