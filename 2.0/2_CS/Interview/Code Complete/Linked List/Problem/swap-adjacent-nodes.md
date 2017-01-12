# Swap Adjacent Node

出处

Given a linked list, swap every two adjacent nodes and return its head

## Solution

如果需要交换两个节点的位置，则对这两个节点的前驱节点，它们的next指针会受到影响；这两个节点本身的next指针，也会受到影响。但是，如下过程总是可以实现交换：

1. 先交换两个前驱节点的next指针的值；
2. 再交换这两个节点的next指针的值。

无论这两个节点的相对位置和绝对位置如何，以上的处理方式总是成立。

## Complexity

时间复杂度 O(n)

## Code

```java
Node swapNodes(Node head){
	if (head == null) return null;
	
	Node dummy = new Node(-1);
	Node backup = dummy;
	while (head != null && head.next != null){
		Node next = head.next;
		dummy.next = next;
		head.next = next.next;
		next.next = head;
		dummy = head;
		head = head.next;
	}
	
	return backup.next;
}
```


