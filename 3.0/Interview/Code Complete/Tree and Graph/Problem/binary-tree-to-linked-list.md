# Binary Tree to Linked List

出处

Covert a binary tree to linked lists. Each linked list is correspondent to all the nodes at the same level.

## Solution

本题相当于层次遍历，当遍历完一层时将构成的链表加入链表集合。本题的核心在于如何判断某层已经遍历完成。回顾层次遍历，我们将节点逐次放入优先队列，然后一次弹出，并将左右子节点放入队列。我们可以引入一个特别的哑节点，用来作为层与层之间的分隔符。每当发现当前节点是哑节点，则说明当前层已经遍历完毕，也意味着下一层的所有节点都已经进入队列。此时，立刻再推送一个哑节点入队，作为下一层的分隔符。

## Complextiy

算法需要层次遍历树，故时间复杂度O(n)。同时，需要额外的O(n)空间将树中的元素存储到链表。

## Code

```java
ArrayList<Node> treeToList(Node head){
	if (head == null) return null;
	ArrayList<Node> headList = new ArrayList<Node>();
	Queue<Node> queue = new Queue<Node>();
	
	queue.add(head);
	queue.add(null);
	
	ArrayList<Node> levelList = new ArrayList<Node>();
	while(!queue.isEmpty()){
		Node cur = queue.poll();
		if (cur != null){
			levelList.add(cur);
			if (cur.left != null){
				queue.add(cur.left);
			}
			if (cur.right != null){
				queue.add(cur.right);
			}
		} else {
			Node newhead = levelList.get(0);
			Node backup = newhead;
			for (int i = 1; i < levelList.length()-1; i++{
				newhead.next = levelList.get(i);
				newhead = newhead.next;
			}
			newhead.next = null;
			headList.add(backup);
			levelList.Clear();
		}
	}
	return headList;
}
```


