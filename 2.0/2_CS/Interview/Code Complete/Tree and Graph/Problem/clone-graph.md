# Clone Graph

# Clone Graph

Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:

Nodes are labeled uniquely.

We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.

As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes, and therefore contains three parts as separated by #.

1. First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
2. Second node is labeled as 1. Connect node 1 to node 2.
3. Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.

Visually, the graph looks like the following:

        1
       / \
      /   \
     0 --- 2
          / \
          \_/

## Solution

1. DFS. 
2. BFS.

使用BFS来解决此问题。用一个Queue来记录遍历的节点，遍历原图，并且把复制过的节点与原节点放在MAP中防止重复访问。

图的遍历有两种方式，BFS和DFS

这里使用BFS来解本题，BFS需要使用queue来保存neighbors

但这里有个问题，在clone一个节点时我们需要clone它的neighbors，而邻居节点有的已经存在，有的未存在，如何进行区分？

这里我们使用Map来进行区分，Map的key值为原来的node，value为新clone的node，当发现一个node未在map中时说明这个node还未被clone，

将它clone后放入queue中处理neighbors。

使用Map的主要意义在于充当BFS中Visited数组，它也可以去环问题，例如A--B有条边，当处理完A的邻居node，然后处理B节点邻居node时发现A已经处理过了

处理就结束，不会出现死循环。

queue中放置的节点都是未处理neighbors的节点。

## Complexity

时间复杂度 O(n)，空间复杂度 O(n)

## Code

```java
public UndirectedGraphNode cloneGraph_1(UndirectedGraphNode node) {
        HashMap<UndirectedGraphNode, UndirectedGraphNode> map = new HashMap<UndirectedGraphNode, UndirectedGraphNode>();
        return cloneGraphRe(node, map);
    }
    
    public UndirectedGraphNode cloneGraphRe(UndirectedGraphNode node, HashMap<UndirectedGraphNode, UndirectedGraphNode> map) {
        if (node == null) return null;
        if (map.containsKey(node) == true) {
            return map.get(node);
        }
        UndirectedGraphNode newnode = new UndirectedGraphNode(node.label);
        map.put(node, newnode);
        for (UndirectedGraphNode cur : node.neighbors) {
            newnode.neighbors.add(cloneGraphRe(cur, map));
        }
        return newnode;
    }
    
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        HashMap<UndirectedGraphNode, UndirectedGraphNode> map = new HashMap<UndirectedGraphNode, UndirectedGraphNode>();
        Queue<UndirectedGraphNode> queue = new LinkedList<UndirectedGraphNode>();
        if (node == null) return null;
        queue.offer(node);
        map.put(node, new UndirectedGraphNode(node.label));
        while (queue.isEmpty() == false) {
            UndirectedGraphNode cur = queue.poll();
            for (UndirectedGraphNode neighbor : cur.neighbors) {
                if (map.containsKey(neighbor) == false) {
                    UndirectedGraphNode newnode = new UndirectedGraphNode(neighbor.label);
                    map.put(neighbor, newnode);
                    queue.offer(neighbor);
                }
                map.get(cur).neighbors.add(map.get(neighbor));
            }
        }
        return map.get(node);
    }
```

