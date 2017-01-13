# Remove Duplicates from Sorted List

Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,

Given 1->1->2, return 1->2.

Given 1->1->2->3->3, return 1->2->3.

## Solution

1. Delete duplicates directly.
2. Copy value first (like Remove Duplicates from Array) and then delete the remaining elements.

## Code

```java
public class Solution {
    public ListNode deleteDuplicates_1(ListNode head) {
        if(head == null || head.next == null) return head;
        ListNode pre = head, cur = head.next;
        while(cur != null) {
            if(pre.val == cur.val) {
                pre.next = cur.next;
            } else {
                pre = pre.next;
            }
            cur = cur.next;
        }
        return head;
    }
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null || head.next == null) return head;
        ListNode pre = head, cur = head.next;
        while(cur != null) {
            if (pre.val != cur.val) {
                pre.next.val = cur.val;
                pre = pre.next;
            }
            cur = cur.next;
        }
        pre.next = null;
        return head;
    }
}
```

