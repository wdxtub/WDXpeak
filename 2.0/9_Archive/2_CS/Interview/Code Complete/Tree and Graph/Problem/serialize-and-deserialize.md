# Serialize and Deserialize

设计一个算法，并编写代码来序列化和反序列化二叉树。将树写入一个文件被称为“序列化”，读取文件后重建同样的二叉树被称为“反序列化”。

如何反序列化或序列化二叉树是没有限制的，你只需要确保可以将二叉树序列化为一个字符串，并且可以将字符串反序列化为原来的树结构。

样例

    给出一个测试数据样例， 二叉树{3,9,20,#,#,15,7}，表示如下的树结构：
      3
     / \
    9  20
      /  \
     15   7
    我们的数据是进行BFS遍历得到的。当你测试结果wrong answer时，你可以作为输入调试你的代码。
    你可以采用其他的方法进行序列化和反序列化。

## Solution

Serialize

+ 注意这个是Lintcode的Serialize, 和Leetcode的区别在于他使用的是BFS. 而后者则是使用的pre-order DFS.
+ null object 和 null的区别.
+ flag的设计: 要有初始值, 在进入循环的时候update, 对于每一个节点再次update. 那么当这一层结束后就是有效的flag.

De-serialize

+ 还是使用BFS解决. 和Pre-order的de-serialize一样, 和各自的Serialize有一个一一对应的关系.
+ 第一次写的时候出现idx超出array size的问题. 这是为什么呢? 因为我在判断token[idx]的时候居然判断了4次. 因为每一次判断都要idx++. 然后我把4个if并成2个if…else就OK了.
+ 注意这个时候的while loop判断不是parents queue是否为空, 而是判断token[] array走完没有. 我一开始这里搞错了, 居然去判断string走完没有. 注意string就是char Array. 例如{3, 9, 20, #, #, 15, 7}, 这个string的length是21. 而token[]则是7.
+ 还有注意这里update parents queue的时候要注意. 这里的做法是对于”#”, 则不加入null到queue. 不然queue的size()就不对了. 因为这里不用traverse null node.

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
class Solution {
    /**
     * This method will be invoked first, you should design your own algorithm
     * to serialize a binary tree which denote by a root node to a string which
     * can be easily deserialized by your own "deserialize" method later.
     */
    public String serialize(TreeNode root) {
        StringBuffer buffer = new StringBuffer();
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        if(root != null){
             queue.offer(root);
             buffer.append(root.val);
        }

        while(!queue.isEmpty()){
            int size = queue.size();

            for(int i = 0; i < size; i++){
                TreeNode node = queue.poll();

                if(node.left == null){
                    buffer.append(",#");
                } else {
                    buffer.append(","+node.left.val);
                    queue.offer(node.left);
                }

                if(node.right == null){
                    buffer.append(",#");
                } else {
                    buffer.append(","+node.right.val);
                    queue.offer(node.right);
                }
            }
        }
        return buffer.toString();
    }

    /**
     * This method will be invoked second, the argument data is what exactly
     * you serialized at method "serialize", that means the data is not given by
     * system, it's given by your own serialize method. So the format of data is
     * designed by yourself, and deserialize it here as you serialize it in
     * "serialize" method.
     */
    public TreeNode deserialize(String data) {
        if(data == null || data.length() == 0) return null;
        Queue<TreeNode> queue = new LinkedList<TreeNode>();

        String[] arr = data.split(",");
        TreeNode root = new TreeNode(Integer.parseInt(arr[0]));
        queue.offer(root);
        for(int i = 1; i < arr.length; i++){
            TreeNode left = null, right = null;
            if(!arr[i].equals("#")){
                left = new TreeNode(Integer.parseInt(arr[i]));
            }
            if(++i < data.length() && !arr[i].equals("#")){
                right = new TreeNode(Integer.parseInt(arr[i]));
            }
            TreeNode parent = queue.poll();
            parent.left = left;
            parent.right = right;
            if(left != null)
                queue.offer(left);
            if(right != null)
                queue.offer(right);
        }
        return root;
    }
}
```

