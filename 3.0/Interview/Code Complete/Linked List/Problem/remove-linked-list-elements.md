# Remove Linked List Elements

Remove all elements from a linked list of integers that have value val.

Example

    Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
    Return: 1 --> 2 --> 3 --> 4 --> 5

## Solution

根据题意删除即可

## Comlexity

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
    public ListNode removeElements(ListNode head, int val) {
        ListNode dummy = new ListNode(0);
        ListNode backup = dummy;
        while (head != null){
            if (head.next != null){
                if (head.val != val){
                    dummy.next = head;
                    dummy = dummy.next;
                    head = head.next;
                }
                else {
                    head = head.next;
                }
            }
            else {
                if (head.val != val){
                    dummy.next = head;
                    dummy = dummy.next;
                    head = head.next;
                }
                else {
                    dummy.next = null;
                    head = head.next;
                }
            }
        }
        return backup.next;
    }
}
```

