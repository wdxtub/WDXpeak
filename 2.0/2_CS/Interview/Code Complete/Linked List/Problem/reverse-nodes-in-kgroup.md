# Reverse Nodes in k-Group

Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

## Solution

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if (k <= 1) return head;
        int T = GetLength(head) / k;
        ListNode dummy = new ListNode(0), cur = head, ins = dummy; 
        dummy.next = head;
        while ((T--) != 0) {
            for (int i = 0; i < k - 1; ++i) {
                ListNode move = cur.next;
                cur.next = move.next;
                move.next = ins.next;
                ins.next = move;
            }
            ins = cur;
            cur = cur.next;
        }
        return dummy.next;
    }
    
    public int GetLength(ListNode head) {
        int length = 0;
        while (head != null) {
            head = head.next;
            length++;
        }
        return length;
    }
}
```

