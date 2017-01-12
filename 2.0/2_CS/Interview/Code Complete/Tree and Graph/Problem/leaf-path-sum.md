# Leaf Path Sum

出处

Get all the paths (always starts from the root and ends at leaf) in a binary tree, whose sum would be equal to given value.

## Solution

本题的处理办法基本与 path-sum.md 完全一致，唯一的区别在于现在要求一定是root-to-leaf paths，故当path和为给定值的时候还需要判断当前节点是否是叶节点。

## Complexity

时间、空间复杂度均为O(n)。

## Code

```java
ArrayList<ArrayList<Integer>> leafPathSum(Node root, int sum){
	ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
	ArrayList<Integer> path = new ArrayList<Integer>();
	
	leafPathSumHelper(root, path, result, sum);
	return result;
}

void leafPathSumHelper(Node root, ArrayList<Integer> path, ArrayList<ArrayList<Integer>> result, int sum){
	if (root == null) return;
	
	path.add(root.value);
	if (root.left == null && root.right == null && root.value == sum){
		ArrayList<Integer> tp = new ArrayList<Integer>(path);
		result.add(tp);
	}
	leafPathSumHelper(root.left, path, result, sum - root.value);
	leafPathSumHelper(root.right, path, result, sum - root.value);
	path.remove(path.length()-1);
}

```

