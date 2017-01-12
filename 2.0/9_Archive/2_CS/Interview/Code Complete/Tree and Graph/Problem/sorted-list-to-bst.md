# Convert Sorted List to Binary Search Tree

Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

给出一个所有元素以升序排序的单链表，将它转换成一棵高度平衡的二分查找树

## Solution

1. Recursion. In-order. O(n)
2. Recursion . Pre-order.
3. pre-order.

## Complexity

见上

## Code

```java
public class Solution {
    public ListNode iter;
    public TreeNode sortedListToBST_1(ListNode head) {
        iter = head;
        int len = 0;
        while (head != null) {
            ++len;
            head = head.next;
        }
        return sortedListToBSTRe1(len);
    }
    public TreeNode sortedListToBSTRe1(int len) {
        if (len == 0) return null;
        int mid = len / 2;
        TreeNode left = sortedListToBSTRe1(mid);
        TreeNode root = new TreeNode(iter.val);
        root.left = left;
        iter = iter.next;
        root.right = sortedListToBSTRe1(len - 1 - mid);
        return root;
    }
    
    
    public TreeNode sortedListToBST_2(ListNode head) {
        return sortedListToBSTRe2(head, null);
    }
    public TreeNode sortedListToBSTRe2(ListNode start, ListNode end) {
        if(start == end) return null;
        ListNode pre = null;
        ListNode slow = start;
        ListNode fast = start;
        while (fast!=end&&fast.next!=end) {
            fast = fast.next.next;
            slow = slow.next;
        }
        TreeNode node = new TreeNode(slow.val);
        node.left = sortedListToBSTRe2(start, slow);
        node.right = sortedListToBSTRe2(slow.next,end);
        return node;
    }
    
    
    public TreeNode sortedListToBST_3(ListNode head) {
        if (head == null) return null;
        if (head.next==null) return new TreeNode(head.val);
        ListNode slow = head;
        ListNode fast = head;
        ListNode pre = null;
        while(fast.next!=null && fast.next.next!=null) {
            pre = slow;
            slow = slow.next;
            fast =fast.next.next;
        }
        fast = slow.next;
        TreeNode node = new TreeNode(slow.val);
        if(pre!=null) {
            pre.next = null;
            node.left = sortedListToBST_3(head);
        }
        node.right = sortedListToBST_3(fast);
        return node;
    }
}
```

