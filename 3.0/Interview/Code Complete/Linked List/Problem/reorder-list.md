# Reorder List

给定一个单链表L： L0→L1→…→Ln-1→Ln,

重新排列后为：L0→Ln→L1→Ln-1→L2→Ln-2→…

必须在不改变节点值的情况下进行原地操作

样例

    给出链表1->2->3->4->null，重新排列后为1->4->2->3->null。

## Solution

先利用快慢指针找到中间，然后把后一半翻转过来，然后两个链表合并即可。

## Code

```java
/**
 * Definition for ListNode.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int val) {
 *         this.val = val;
 *         this.next = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param head: The head of linked list.
     * @return: void
     */
    public void reorderList(ListNode head) {
        if(head == null || head.next == null || head.next.next == null) return;
        ListNode slow = head, fast = head;

        while(fast.next != null && fast.next.next != null){
            fast = fast.next.next;
            slow = slow.next;
        }
        fast = slow.next;
        slow.next = null;
        // reverse
        ListNode pre = null;
        while(fast != null){
            ListNode temp = fast.next;
            fast.next = pre;
            pre = fast;
            fast = temp;
        }

        while(head != null && pre != null){
            ListNode temp = head.next;
            head.next = pre;
            pre = pre.next;
            head.next.next = temp;
            head = temp;
        }
    }
}


```

