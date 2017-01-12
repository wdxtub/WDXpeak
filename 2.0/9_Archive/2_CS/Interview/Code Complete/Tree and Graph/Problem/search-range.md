# Search Range

给定两个值 k1 和 k2（k1 < k2）和一个二叉查找树的根节点。找到树中所有值在 k1 到 k2 范围内的节点。即打印所有x (k1 <= x <= k2) 其中 x 是二叉查找树的中的节点值。返回所有升序的节点值。

样例

    如果有 k1 = 10 和 k2 = 22, 你的程序应该返回 [12, 20, 22].
    
        20
       /  \
      8   22
     / \
    4   12

## Solution

正常回溯一波二分即可

## Complexity

时间复杂度 O(logn)，空间复杂度 O(h)

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
     * @param root: The root of the binary search tree.
     * @param k1 and k2: range k1 to k2.
     * @return: Return all keys that k1<=key<=k2 in ascending order.
     */
    public ArrayList<Integer> searchRange(TreeNode root, int k1, int k2) {
        ArrayList<Integer> res = searchRangeRecur(root,k1,k2);
        return res;
    }

    public ArrayList<Integer> searchRangeRecur(TreeNode cur, int k1, int k2){
        ArrayList<Integer> res = new ArrayList<Integer>();
        if (cur==null) return res;
        if (k1>k2) return res;

        ArrayList<Integer> left = searchRangeRecur(cur.left,k1,Math.min(cur.val-1,k2));
        ArrayList<Integer> right = searchRangeRecur(cur.right,Math.max(cur.val+1,k1),k2);

        res.addAll(left);
        if (cur.val>=k1 && cur.val<=k2) res.add(cur.val);
        res.addAll(right);

        return res;
    }
}
```

