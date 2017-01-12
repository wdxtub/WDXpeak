# Partition Linked List

Write code to partition a linked list around a value x, such athat all nodes less than x come befor all nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the elements less than x (see below)

EXAMPLE

    Input:  3->5->8->5->10->2->1 [partition = 5]
    Output: 3->1->2->10->5->5->8

## Solution

用 dummy node 即可

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
public static Node partitionStable(Node head, int x){
    Node minStart = null;
    Node minEnd = null;
    Node maxStart = null;
    Node maxEnd = null;

    while (head != null){
        Node next = head.next;
        head.next = null;
        if (head.data < x){
            if (minStart == null){
                minStart = head;
                minEnd = minStart;
            }
            else{
                minEnd.next = head;
                minEnd = head;
            }
        }
        else{
            if(maxStart == null){
                maxStart = head;
                maxEnd = maxStart;
            }
            else{
                maxEnd.next = head;
                maxEnd = head;
            }
        }
        head = next;
    }

    if (minStart == null){
        return maxStart;
    }

    minEnd.next = maxStart;
    return minStart;
}

public static Node partitionUnstable(Node head, int x){
    Node start = head;
    Node end = head;

    while (head != null){
        Node next = head.next;
        if (head.data < x){
            head.next = start;
            start = head;
        }
        else{
            end.next = head;
            end = head;
        }
        head = next;
    }
    end.next = null;

    return start;
}
```

