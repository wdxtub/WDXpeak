# Insertion Sort List

Sort a linked list using insertion sort.

## Solution

基本插入排序

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

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
    public ListNode insertionSortList(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode dummy = new ListNode(Integer.MIN_VALUE);
        dummy.next = head;
        ListNode cur = head.next;
        head.next = null;
        while (cur != null) {
            ListNode tmp = dummy;
            while (tmp.next != null && tmp.next.val <= cur.val) tmp = tmp.next;
            ListNode next = cur.next;
            cur.next = tmp.next;
            tmp.next = cur;
            cur = next;
        }
        return dummy.next;
    }
}
```

