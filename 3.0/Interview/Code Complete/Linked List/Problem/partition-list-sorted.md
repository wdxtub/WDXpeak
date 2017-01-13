# Partitiom List Sorted

出处

Given a linked list and a value x, write a function to reorder this list such that all nodes less than x come before the nodes greater than or equal to x.

给定一个单链表和数值x，划分链表使得所有小于x的节点排在大于等于x的节点之前。

你应该保留两部分内链表节点原有的相对顺序。

样例

    给定链表 1->4->3->2->5->2->null，并且 x=3
    返回 1->2->2->4->3->5->null

## Solution

将链表分成两部分，但这两部分的头节点连是不是NULL都不确定。当涉及对头节点的操作，我们不妨考虑创建哑节点。这样做的好处是：我们总是可以创建两个哑节点，用dummy->next作为真正头节点的引用， 然后在此基础上append，这样就不用处理头节点是否为空的边界条件了。

## Complexity

实际上只需要遍历链表一次，所以复杂度是 O(n)

## Code

```java
Node reorderList(Node head, int x){
	if (head == null) return null;

	Node small = new Node(-1);
	Node sback = small;
	Node large = new Node(-1);
	Node lback = large;
	
	while (head != null){
		Node next = head.next;
		head.next = null;
		if (head.value < x){
			small.next = head;
			small = small.next;
		} else {
			large.next = head;
			large = large.next;
		}
		head = next;
	}
	small.next = lback.next;
	
	return sback.next;
}
```

