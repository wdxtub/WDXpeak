# Check Cycle

给定一个链表，判断它是否有环。

样例

    给出 -21->10->4->5, tail connects to node index 1，返回 true

挑战

    不要使用额外的空间

## Solution

快慢指针

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

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
     * @param head: The first node of linked list.
     * @return: True if it has a cycle, or false
     */
    public boolean hasCycle(ListNode head) {
        if(head == null)
            return false;
        ListNode fast = head;
        ListNode slow = head;
        while(fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if(slow == fast)
                return true;
        }
        return false;
    }
}
```


