# Unique Binary Search Trees II

Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

For example,

Given n = 3, your program should return all 5 unique BST's shown below.

    1         3     3      2      1
     \       /     /      / \      \
      3     2     1      1   3      2
     /     /       \                 \
    2     1         2                 

## Solution

1. DFS directly. (from the Internet)
2. DP + DFS. (my solution)
    + Generate trees for 'n' from 1 to n. (DP)
    + When generate trees for n = i, get the left and right subtrees by copying tree structures of dp[1...i-1]. (copy tree uses DFS)

## Code

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public List<TreeNode> generateTrees(int n) {
        return generateTreesRe(1, n);
    }
    public List<TreeNode> generateTreesRe(int l, int r) {
        ArrayList<TreeNode> res = new ArrayList<TreeNode>();
        if (l > r) {
            res.add(null);
            return res;
        }
        for (int k = l; k <= r; ++k) {
            List<TreeNode> leftTrees = generateTreesRe(l, k-1);
            List<TreeNode> rightTrees = generateTreesRe(k+1, r);
            for (int i = 0; i < leftTrees.size(); i++) {
                for (int j = 0; j < rightTrees.size(); j++) {
                    TreeNode root = new TreeNode(k);
                    root.left = leftTrees.get(i);
                    root.right = rightTrees.get(j);
                    res.add(root);
                }
            }
        }
        return res;
    }
}
```

