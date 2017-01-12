# Different BST II

出处

给出n，生成所有由1...n为节点组成的不同的二叉查找树

样例

    给出n = 3，生成所有5种不同形态的二叉查找树：
    1         3     3       2    1
     \       /     /       / \    \
      3     2     1       1   3    2
     /     /       \                \
    2     1         2                3

## Solution

使用递归来做。

1. 先定义递归的参数为左边界、右边界，即1到n.
2. 考虑从left, 到right 这n个数字中选取一个作为根，余下的使用递归来构造左右子树。
3. 当无解时，应该返回一个null树，这样构造树的时候，我们会比较方便，不会出现左边解为空，或是右边解为空的情况。
4. 如果说左子树有n种组合，右子树有m种组合，那最终的组合数就是n*m. 把这所有的组合组装起来即可

## Complexity

这个不是很确定

时间复杂度 O(n^2 ) 空间复杂度 O(n)

## Code

```java
/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @paramn n: An integer
     * @return: A list of root
     */
    public List<TreeNode> generateTrees(int n) {
        return dfs(1, n);
    }

    public List<TreeNode> dfs(int left, int right) {
        List<TreeNode> ret = new ArrayList<TreeNode>();

        // The base case;
        if (left > right) {
            ret.add(null);
            return ret;
        }

        for (int i = left; i <= right; i++) {
            List<TreeNode> lTree = dfs(left, i - 1);
            List<TreeNode> rTree = dfs(i + 1, right);
            for (TreeNode nodeL: lTree) {
                for (TreeNode nodeR: rTree) {
                    TreeNode root = new TreeNode(i);
                    root.left = nodeL;
                    root.right = nodeR;
                    ret.add(root);
                }
            }
        }

        return ret;
    }
}

```

