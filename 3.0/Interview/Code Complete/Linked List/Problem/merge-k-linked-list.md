# Merge K Linked List

出处

Merge k sorted linked lists to be one sorted list.

## Solution

可以将k个sorted list想象成k个有序数据流，互相竞争插入到结果序列， 因此可以考虑使用一个最小值堆维护动态数据：将每个队头的元素加入一个堆，然后从堆中依次弹出最小数据。如果数据属于第i个list，则该list补充一个元素到堆。重复上述过程直到所有元素排序完成。事实上，该算法就是外排序算法的一个具体实现，区别仅仅在于这里略去了文件的读写操作。

## Complexity

时间上，我们需要维护一个大小为k的最小值堆，每次维护复杂度O(logk)，由于一共有n个数据，每个数据都会加入最小值堆，故总体时间复杂度O(nlogk)。由于每个list至少有一个数据，故n一定大于等于k。相比于完全无序的n个数据排序(所需时间O(nlogn))，我们的算法将复杂度降至O(nlogk)。原因在于数据是部分有序的。事实上，在通常面试中，如果数据已经部分有序，我们理应能够实现时间复杂度优于O(nlogn)的算法。

空间上，我们需要大小为k的最小值堆。同时，在不允许破坏原有链表的情况下，我们需要额外O(n)的空间构建新链表，故总体空间复杂度O(n+k)。如果可以直接修改原有数据的next指针，则总体空间复杂度即为O(k)。至于是否能够破坏原始数据，需要与面试官进行沟通。

## Code 

```java
//  Definition for singly-linked list.
class ListNode {
	int val;
	ListNode next;
 
	ListNode(int x) {
		val = x;
		next = null;
	}
}
 
public class Solution {
	public ListNode mergeKLists(ArrayList<ListNode> lists) {
		if (lists.size() == 0)
			return null;
 
		//PriorityQueue is a sorted queue
		PriorityQueue<ListNode> q = new PriorityQueue<ListNode>(lists.size(),
				new Comparator<ListNode>() {
					public int compare(ListNode a, ListNode b) {
						if (a.val > b.val)
							return 1;
						else if(a.val == b.val)
							return 0;
						else 
							return -1;
					}
				});
 
		//add first node of each list to the queue
		for (ListNode list : lists) {
			if (list != null)
				q.add(list);
		}
 
		ListNode head = new ListNode(0);
		ListNode p = head; // serve as a pointer/cursor
 
		while (q.size() > 0) {
			ListNode temp = q.poll();
			//poll() retrieves and removes the head of the queue - q. 
			p.next = temp;
 
			//keep adding next element of each list
			if (temp.next != null)
				q.add(temp.next);
 
			p = p.next;
		}
 
		return head.next;
	}
}
```

