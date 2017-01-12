# Node Path Sum

出处

Get all the paths (from any node to any other node with deeper level) in a binary tree, whose sum would be equal to given value.

## Solution

经过前两道题目的分析，本题的大体思路应该已经比较容易想到了：用path记录当前走过的路径，用result记录所有符合条件的path，利用DFS进行左子树和右子树的探索。本题的特别之处在于，所求的path并不一定需要从root开始，即之前的题目都是知道固定的起始点，寻找终点，而本题起始点不定。进一步考虑path中存放的路径，该路径是由root到当前节点经过的所有节点，且当前节点一定是path的终点。那么，不妨换一个角度思考：以当前节点为终点，是否存在一个起始节点，使得路径上的节点数字和为给定值。这样，“对于每个path数组，应该从数组尾(当前节点，即终点)，反向搜索，寻求起始节点。一旦找到，则将该段path加入answer。

## Complexity

对于处于第i层的节点，从终点往根节点反向搜索需要的复杂度为i。对于二叉树，第i层有 2^i 个节点，故复杂度为 `i*2^i`。对于深度为d的二叉树，整体复杂度为：
`1*2^1+2*2^2+…+d*2^d = 2(d - 1)*2^d + 2`
又`d = logn`，故整体时间复杂度`O(nlogn)`。

## Code

```java
ArrayList<ArrayList<Integer>> nodePathSum(Node root, int sum){
	ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
	ArrayList<Integer> path = new ArrayList<Integer>();
	
	nodePathSumHelper(root, path, result, sum);
	return result;
}

void nodePathSumHelper(Node root, ArrayList<Integer> path, ArrayList<ArrayList<Integer>> result, int sum){
	if (root == null) return;
	
	path.add(root.value);
	int tmpsum = sum;
	ArrayList<Integer> partialPath = new ArrayList<Integer>()
	for (int i = path.length() - 1; i >=0; i--){
		partialPath.add(path.get(i));
		tmpsum -= path.get(i);
		if (tmpsum == 0){
			result.add(partialPath);
		}
	}
	nodePathSumHelper(root.left, path, result, sum-root.value);
	nodePathSumHelper(root.right, path, result, sum-root.value);
	path.remove(path.length() - 1);
}

```

