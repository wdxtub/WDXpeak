# Start of Circle

出处

## Solution

寻找某个特定位置，用runner和chaser。这里的技巧是，如果runner以两倍速度前进，chaser以一倍速前进，在有环的情况下，runner与chaser一定能在某点相遇。相遇后，再让chaser从头节点出发再次追赶runner，此时两者都以一倍速前进，可以证明，第二次相遇的节点即为环的开始位置。

## Complexity

时间复杂度 O(n)

## Code

```java
Node startCircle(Node head){
	if (head == null) return null;
	
	Node quick = head;
	Node slow = head;
	Node backup = head;
	
	while (quick != null && quick.next != null){
		quick = quick.next.next;
		slow = slow.next;
		if (slow == quick)
			break;
	}
	
	if (quick == null || quick.next == null){
		return null;
	}
	
	slow = backup;
	while (slow != quick){
		slow = slow.next;
		quick = quick.next;
	}
	return slow;
}
``` 

