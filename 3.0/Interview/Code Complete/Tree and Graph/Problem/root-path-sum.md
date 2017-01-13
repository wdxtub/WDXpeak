# Root Path Sum

出处

Get all the paths (always starts from the root) in a binary tree, whose sum would be equal to given value.

## Solution

正如上文的叙述，寻找满足条件的路径，用path记录当前走过的路径，用result记录所有符合条件的path，用DFS进行探索。 对于递归函数，传入的节点相当于当前子树的根：当传入节点为空时，说明我们走完了当前的path，直接返回，即达到递归函数的出口。由于根节点必须要出现在path中，所以我们先将当前节点push到path中去。此时，如果当前节点的数值等于sum，说明找到了一个可行解，故把该递归状态下的path加入到answer中。进一步，我们需要调用函数自身解决左子树和右子树的子问题。由于当前节点已经加入path，那么自然传递给子问题的sum变为sum – root->val，根的左右孩子成为了子问题的根。

## Complexity

时间上，上述解法遍历每个节点，故时间复杂度O(n)。空间上，如果path以引用的方式传入，则额外空间为O(n)；如果path以值的方式传入，则在递归函数的底层会有 2^h 个path拷贝，h为树的高度。故复杂度为O(2^h *n)。

## Code

 ```java
 ArrayList<ArrayList<Integer>> pathSum(Node root, int sum){
 	ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
 	ArrayList<Integer> path = new ArrayList<Integer>();
 	pathSumHelper(root, path, result, sum);
 	return result;
 }
 
 void pathSumHelper(Node root, ArrayList<Integer> path, ArrayList<ArrayList<Integer>> result, int sum){
 	if (root == null) return;
 	
 	path.add(root.value);
 	if (root.value == sum){
 		ArrayList<Integer> tp = new ArrayList<Integer>(path);
 		result.add(tp);
 	}
 	pathSumHelper(root.left, path, result, sum - root.value);
 	pathSumHelper(root.right, path, result, sum - root.value);
 	path.remove(path.length()-1);
 }
 ```

