# Sorted Array to Binary Search Tree

出处

给一个排序数组（从小到大），将其转换为一棵高度最小的排序二叉树。

样例

    给出数组 [1,2,3,4,5,6,7], 返回
         4
       /   \
      2     6
     / \    / \
    1   3  5   7

挑战

    可能有多个答案，返回任意一个即可

## Solution

将数据结构分成左右两部分，分别构造两个二叉树，再用中间数与这两个局部解合并得到当前的全局解。因为数组已经排序好，因此这个二叉树一定满足BST的条件(左边的任何数一定小于中间数小于右边的任何数)，在选择分界点的时候选择中点，那么也就能满足平衡条件。

要达到「平衡二叉搜索树」这个条件，我们首先应从「平衡二叉搜索树」的特性入手。简单起见，我们先考虑下特殊的满二叉搜索树，满二叉搜索树的一个重要特征就是各根节点的 key 不小于左子树的 key ，而小于右子树的所有 key；另一个则是左右子树数目均相等，那么我们只要能将所给升序序列分成一大一小的左右两半部分即可满足题目要求。又由于此题所给的链表结构中仅有左右子树的链接而无指向根节点的链接，故我们只能从中间的根节点进行分析逐层往下递推直至取完数组中所有 key, 数组中间的索引自然就成为了根节点。由于 OJ 上方法入口参数仅有升序序列，方便起见我们可以另写一私有方法，加入start和end两个参数，至此递归模型初步建立。

## Complexity

算法遍历整个数组，故时间复杂度O(n)，需要额外O(n)空间存储树的节点。

## Code

```java
Node arrayToBst(int[] arr){
	if (arr.length == 0) return null;
	if (arr.length == 1) {
		Node head = new Node(arr[0]);
		return head;
	}
	
	return helper(arr, 0, arr.length-1);
}

Node helper(int[] arr, int low, int high){
	if (low > high){
		return null;
	}
	if (low == high){
		Node head = new Node(arr[low]);
		return head;
	}
	
	int mid = (low+high)/2;
	Node left = helper(arr, low, mid - 1);
	Node right = helper(arr, mid + 1, high);
	Node head = new Node(arr[mid]);
	head.left = left;
	head.right = right;
	return head;
}

```


