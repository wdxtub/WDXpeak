# Remove Duplicates from Unsorted List

Write code to remove duplicates from an unsorted linked list

FOLLOW UP

    How would you solve this problem if a temporary buffer is not allowed?

## Solution

根据题意进行删除即可

## Complexity

时间复杂度 O(n)，空间复杂度 O(n)

## Code

```java
public static Node removeDups(Node head){
    HashSet<Integer> intSet = new HashSet<Integer>();
    Node cur = head;
    Node previous = null;
    while (cur != null){
        if (intSet.contains(cur.data)){
            previous.next = cur.next;
        }
        else{
            intSet.add(cur.data);
            previous = cur;
        }
        cur = cur.next;
    }
    return head;
}

/**
 * Iterate with two pointer: one iterates through the linked list, and the
 * other checks all subsequent nodes for duplicates
 */
public static Node removeDupsNoExtraSpace(Node head){
    Node cur = head;
    while (cur != null){
        Node pointer = cur;
        while (pointer.next != null){
            if (pointer.next.data == cur.data){
                pointer.next = pointer.next.next;
            }
            else {
                pointer = pointer.next;
            }
        }
        cur = cur.next;
    }

    return head;
}
```

