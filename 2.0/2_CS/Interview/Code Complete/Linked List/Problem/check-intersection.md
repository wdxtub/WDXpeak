# Check Intersection

Given two singly linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth node of the first linked list is the exact same node(by reference) as the jth node of the second linked list, then they are intersecting.

## Solution

1. Run through each linked list to get the lengths and tails
2. Compare the tails. If they are different(by reference, not by value), return immediately. There is no intersection.
3. Set two pointers to the start of each linked list
4. On the longer linked list, advance its pointer by the difference in lengths
5. Now, traverse on each linked list until the pointers are the same

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
public static Node findIntersection(Node head1, Node head2){
    if (head1 == null)
        return null;
    if (head2 == null)
        return null;

    int size1 = 1;
    int size2 = 1;

    Node tail1 = null;
    Node tail2 = null;

    tail1 = head1;
    while (tail1.next != null){
        size1++;
        tail1 = tail1.next;
    }
    tail2 = head2;
    while (tail2.next != null){
        size2++;
        tail2 = tail2.next;
    }

    if (tail1 != tail2){
        return null;
    }

    Node longer = size1 < size2 ? head2 : head1;
    Node shorter = size1 < size2 ? head1 : head2;

    for (int i = 0; i < Math.abs(size1 - size2); i++){
        longer = longer.next;
    }

    while (shorter != longer){
        shorter = shorter.next;
        longer = longer.next;
    }

    return longer;
}
```


