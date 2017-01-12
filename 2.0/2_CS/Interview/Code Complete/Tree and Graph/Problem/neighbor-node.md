# Neighbor Node

出处

Find the immediate right neighbor of the given node, with parent links given, but without root node.

## Solution

直接的右邻居(immediate right neighbor)定义为：在给定节点右侧且与给定节点在同一层。由于给定了父指针，故可以利用父指针向上倒推。根据定义，如果当前节点是父节点的右孩子，我们继续倒推，直到当前节点是某个父节点的左孩子，并且该父节点存在右子树。这样，我们立即进入该子树，找到与给定节点处于相同层的最左节点即可。

## Complexity

倒推需要复杂度O(h)，下降进入子树寻找与给定节点处于相同层的最左节点也需要复杂度O(h)，故整体复杂度O(h)，h为树高。

## Code

```java
Node findDescendent(Node root, int level){
	if (root == null) return null;
	while (level > 0 && root != null) {
		if (root.left != null){
			root = root.left;
		} else if (root.right != null){
			root = root.right;
		} else {
			root = null;
		}
		level--;
	}
	return root;
}

Node rightNeighbor(Node node){
	if (node == null) return null;
	
	int level = 0;
	Node parent = node.parent;
	Node rtn = null;
	int flag = 0;
	while (parent != null){
		if (parent.left == node && parent.right != null){
			flag = 1;
		}
		level++;
		node = parent;
		parent = parent.parent;
		
		if (flag == 1){
			if (parent == null) {
				return null;
			} else {
				rtn = findDescendent(parent, level);
				if (rtn != null){
					return rtn;
				} else {
					flag = 0;
				}
			}
		}
	}
	return null;
}


```
 

