# Middle of List

出处

Given a linked list, write a function to return the middle point of that list.

## Solution

对于寻找链表的某个特定位置的问题，不妨用两个指针变量runner与chaser (ListNode*runner = head, *chaser = head)，以不同的速度遍历该链表，以找到目标位置。在验证算法正确性时，可以用几个简单的小测试用例 (例如长度为4和5的链表)。注意，通常需要分别选取链表长度为奇数和偶数的测试用例以验证算法在一般情况下的正确性。

由于题目涉及在链表中寻找特定位置，我们用两个指针变量以不同的速度遍历该链表。其中，runner以两倍速前进，chaser 一倍速。这样，当runner到达尾节点时，chaser即为所求解。在实际实现的时候，还需要注意链表的越界问题。

## Complexity

只要遍历一次，时间复杂度 O(n)

## Code

```java
Node middleList(Node head){
	if (head == null) return null;
	
	Node quick = head;
	Node slow = head;
	
	while(head.next != null && head.next.next != null){
		quick = quick.next.next;
		slow = slow.next;
	}
	
	return slow;
}
```


