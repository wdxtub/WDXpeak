# Reverse List

出处

Reverse the linked list and return the new head.

样例

    给出一个链表1->2->3->null，这个翻转后的链表为3->2->1->null

挑战

    在原地一次翻转完成

## Solution

循环遍历链表, 每次只处理当前指针的next 变量，由此实现链表的逆转。

在纸上画清晰即可，注意需要用一个临时变量保存节点，最多同时需要三个节点的信息

## Complexity

时间复杂度 O(n)

## Code

```java
Node reverseList(Node head){
	if (head == null) return null;
	
	Node prev = null;
	Node next = null;
	
	while (head.next != null){
		next = head.next
		head.next = prev;
		
		prev = head;
		head = next;
	}
	return head;
}
```


