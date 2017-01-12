# Reversely List Traverse

出处

Traverse the linked list reversely.

## Solution

倒序访问问题本身，我们利用递归处理。

## Complexity

时间复杂度 O(n)，空间则是利用系统的堆栈进行

## Code

```java
void reverseTraverse(Node head){
	if (head == null)
		return;
	reverseTraverse(head.next);
	visit(head);
}
```


