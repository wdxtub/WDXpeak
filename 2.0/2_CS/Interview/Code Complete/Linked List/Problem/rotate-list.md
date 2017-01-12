# Rotate List

出处

Given a list, rotate the list to the right by k places, where k is non-negative. e.g: 1->2->3->4->5, k = 2; after rotation: 4->5->1->2->3

## Solution

假设链表长度为len，新的链表的尾节点是原链表中第 len-k 个节点。则我们的runner指针需要前进len – k – 1 次，到达的位置即为新链表中的尾节点。同时，下一个节点即为新链表的头结点。

## Complexity

时间复杂度 O(n)

## Code

```java
Node rotateList(Node head, int k){
	if (head == null) return null;
	
	// get the length of the list;
	Node tmp = head;
	int length = 1;
	while (tmp.next != null){
		length++;
		tmp = tmp.next;
	}
	
	// move the pointer to len - k%len -1 
	k = k % length;
	if (k == 0) 
		return head;
	
	// link the tail to the head
	tmp.next = head;
	
	for(int i = 0; i < length - k - 1; i++){
		cur = cur.next;
	}
	
	head = cur.next;
	cur.next = null;
	
	return head;
}
```

