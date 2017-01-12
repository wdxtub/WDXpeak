# Merge Two Lists

出处

Given two sorted linked lists, write a function to merge these two lists, and return a new list which is sorted.

## Solution

遇到同时处理两个链表的问题，循环的条件一般可以用 while( list1 && list2 )，当循环跳出后，再处理剩下非空的链表。这相当于：边界情况特殊处理，常规情况常规处理。

这是一个典型的需要同时处理两个链表的问题，可以先处理常规情况(两个链表都有剩下节点)，再处理边界情况(其中一个链表已经遍历完毕)。在处理常规情况的时候，我们将当前两个链表中较小的那个节点放入新的链表。

## Complexity

时间复杂度 O(n)

## Code

```java
Node mergeList(Node head1, Node head2){
	if (head1 == null && head2 == null) return false;
	if (head1 == null) return head2;
	if (head2 == null) return head1;
	
	Node dummy = new Node(-1);
	Node backup = dummy;
	while(head1 != null && head2 != null){
		if (head1.value < head2.value){
			dummy.next = head1;
			head1 = head1.next;
		} else {
			dummy.next = head2;
			head2 = head2.next;
		}
		dummy = dummy.next;
	}
	
	if (head1 != null){
		dummy.next = head1;
	} else {
		dummy.next = head2;
	}
	return backup.next;
}
```


