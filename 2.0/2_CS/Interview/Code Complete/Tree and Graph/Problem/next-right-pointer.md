# Populating Next Right Pointers in Each Node

Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
    
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

+ You may only use constant extra space.
+ You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).

For example,

Given the following perfect binary tree,

         1
       /  \
      2    3
     / \  / \
    4  5  6  7

After calling your function, the tree should look like:

         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \  / \
    4->5->6->7 -> NULL

## Solution

1. iterative way with CONSTANT extra space.
2. iterative way + queue.
3. recursive solution.

也可以根据层次遍历来进行修改

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
/**
 * Definition for binary tree with next pointer.
 * public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void connect(TreeLinkNode root) {
        if (root == null) return;
        TreeLinkNode dummy = new TreeLinkNode(-1);
        TreeLinkNode pre = dummy;
        TreeLinkNode cur = root;
        while (cur != null) {
            if (cur.left != null) {
                pre.next = cur.left;
                pre = pre.next;
            }
            if (cur.right != null) {
                pre.next = cur.right;
                pre = pre.next;
            }
            cur = cur.next;
        }
        connect(dummy.next);
    }
}
```

