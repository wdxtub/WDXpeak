# Delete Middle Node

Implement an algorithm to delete a node in the middle of a singly linked list, given only access to that node.

 EXAMPLE

    Input: the node c from the linked list a->b->c->d->e
    Result: nothing is returned, but the new linked list looks like a->b->d->e

## Solution

快慢指针

## Complexity

时间复杂度 O(n), 空间复杂度 O(1)

## Code

```java
/**
 * Copy the value of the next node to the curNode and delete the next node.
 * This problem cannot be solved if the node to be deleted is the las node
 * in the linked list
 */
public static boolean deleteCurrentNode(Node curNode){
    if (curNode == null || curNode.next == null){
        return false;
    }
    curNode.data = curNode.next.data;
    curNode.next = curNode.next.next;
    return true;
}
```

