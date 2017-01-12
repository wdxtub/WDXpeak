# Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

## Solution

1. HashMap
2. uses constant extra space.
3. Recursive. (Stack)-->StackOverflow in Java.
4. Iterative. 

## Complexity

时间复杂度 O(n)，空间复杂度 O(n)

## Code

```java
public class Solution {
    public RandomListNode copyRandomList_1(RandomListNode head) {
        if (head == null) return null;
        HashMap<RandomListNode, RandomListNode> map = new HashMap<RandomListNode, RandomListNode>();
        RandomListNode dummy = new RandomListNode(-1);
        RandomListNode curNew = dummy, cur = head;
        while (cur != null) {
            if (map.containsKey(cur) == false) {
                map.put(cur, new RandomListNode(cur.label));
            }
            if (cur.random != null && map.containsKey(cur.random) == false) {
                map.put(cur.random, new RandomListNode(cur.random.label));
            }
            curNew.next = map.get(cur);
            curNew.next.random = map.get(cur.random);
            curNew = curNew.next;
            cur = cur.next;
        }
        return dummy.next;
    }
    
    
    public RandomListNode copyRandomList_2(RandomListNode head) {
        if (head == null) return null;
        RandomListNode cur = head;
        while (cur != null) {
            RandomListNode newnode = new RandomListNode(cur.label);
            newnode.next = cur.next;
            cur.next = newnode;
            cur = cur.next.next;
        }
        cur = head;
        while (cur != null) {
            if (cur.random != null) {
                cur.next.random = cur.random.next;
            }
            cur = cur.next.next;
        }
        RandomListNode dummy = new RandomListNode(-1);
        RandomListNode curNew = dummy;
        cur = head;
        while (cur != null) {
            curNew.next = cur.next;
            curNew = curNew.next;
            cur.next = cur.next.next;
            cur = cur.next;
        }
        return dummy.next;
    }
    
    
    public RandomListNode copyRandomList_3(RandomListNode head) {/*StackOverflowError*/
        if (head == null) return null;
        HashMap<RandomListNode, RandomListNode> map = new HashMap<RandomListNode, RandomListNode>();
        return copy(head, map);
    }
    public RandomListNode copy(RandomListNode root, HashMap<RandomListNode, RandomListNode> map) {
        if (root == null) return null;
        if (map.containsKey(root) == true) {
            return map.get(root);
        }
        RandomListNode newnode = new RandomListNode(root.label);
        map.put(root, newnode);
        newnode.next = copy(root.next, map);
        newnode.random = copy(root.random, map);
        return newnode;
    }
    
    
    public RandomListNode copyRandomList_4(RandomListNode head) {
        if (head == null) return null;
        HashMap<RandomListNode, RandomListNode> map = new HashMap<RandomListNode, RandomListNode>();
        Queue<RandomListNode> queue = new LinkedList<RandomListNode>();
        queue.offer(head);
        map.put(head, new RandomListNode(head.label));
        while (queue.isEmpty() == false) {
            RandomListNode cur = queue.poll();
            if (cur.next != null && map.containsKey(cur.next) == false) {
                RandomListNode newnode = new RandomListNode(cur.next.label);
                map.put(cur.next, newnode);
                queue.offer(cur.next);
            }
            map.get(cur).next = map.get(cur.next);
            if (cur.random != null && map.containsKey(cur.random) == false) {
                RandomListNode newnode = new RandomListNode(cur.random.label);
                map.put(cur.random, newnode);
                queue.offer(cur.random);
            }
            map.get(cur).random = map.get(cur.random);
        }
        return map.get(head);
    }
}
```

