# Kth to Last

出处

Find the kth to last element of a singly linked list. For example, if given a list 1->2->3->4, and k equals to 2, the function should return element 2.

## Solution

由于题目涉及在链表中寻找特定位置，我们用两个指针变量遍历该list。只是在本例中，runner与chaser以相同倍速前进，但runner提前k步出发。

## Complexity

只要遍历一次，时间复杂度 O(n)

## Code

```java
Node kthtolast(Node head, int k){
	if (head == null) return null;
	if (k < 0) return null;
	
	Node quick = head;
	Node slow = head;
		
	for (int i = 0; i < k; i++){
		if (quick.next != null)
			quick = quick.next
	}
	
	while (quick != null){
		slow = slow.next;
		quick = quick.next;
	}
	
	return slow;
}
```


