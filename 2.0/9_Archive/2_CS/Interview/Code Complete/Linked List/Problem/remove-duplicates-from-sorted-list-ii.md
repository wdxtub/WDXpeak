# Remove Duplicates from Sorted List II

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,

Given 1->2->3->3->4->4->5, return 1->2->5.

Given 1->1->1->2->3, return 2->3

## Solution

1. Iterative
2. Recursive

## Code

```java
public class Solution {
    public ListNode deleteDuplicates_1(ListNode head) {
        ListNode dummy = new ListNode(-1);
        ListNode cur = dummy;
        while (head != null) {
            if (head.next != null && head.val == head.next.val) {
                while (head.next != null && head.val == head.next.val)
                    head = head.next;
            } else {
                cur.next = head;
                cur = cur.next;
            }
            head = head.next;
        }
        cur.next = null;
        return dummy.next;
    }
    
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) return null;
        if (head.next == null || head.val != head.next.val){
            head.next = deleteDuplicates(head.next);
            return head;
        }
        while (head.next != null && head.val == head.next.val)
            head = head.next;
        return deleteDuplicates(head.next);
    }
}
```

