# Topological Sort

给定一个有向图，图节点的拓扑排序被定义为：

+ 对于每条有向边A--> B，则A必须排在B之前　　
+ 拓扑排序的第一个节点可以是任何在图中没有其他节点指向它的节点　　

找到给定图的任一拓扑排序

挑战

    能否分别用BFS和DFS完成？

## Solution

A basica method is recording the pre nodes of every node, then find out a node without pre node in each iteration and delete this node from unvisited set.

DFS: use a recursive method, randomly pick up an unmakred node, before adding it into result list, recursively visite all its neighbors and add its neighbors into list first. In this way, we guarantee that all the nodes belong to some node's post nodes will be added to the result list first.

Thoughts:

1. For each node in the graph, construct a map with node as key, and number of parent nodes as value
2. Looping through left nodes and see if its indegree is 0: if so, remove the node from graph and add it to result; also its neighbors indegree--

A problem while implementing #2 is ConcurrentModificatoinException that I tried to remove the node from map while looping through it. A work around is looping through remaining nodes from graph and remove it from graph directly. Entries in map are never removed.

## Code

```java
/**
 * Definition for Directed graph.
 * class DirectedGraphNode {
 *     int label;
 *     ArrayList<DirectedGraphNode> neighbors;
 *     DirectedGraphNode(int x) { label = x; neighbors = new ArrayList<DirectedGraphNode>(); }
 * };
 */
public class Solution {
    /**
     * @param graph: A list of Directed graph node
     * @return: Any topological order for the given graph.
     */
    public ArrayList<DirectedGraphNode> topSort(ArrayList<DirectedGraphNode> graph) {
        ArrayList<DirectedGraphNode> res = new ArrayList<DirectedGraphNode>();
        if (graph.size()==0) return res;

        //Construct hash map.
        Map<DirectedGraphNode, Set<DirectedGraphNode>> map = new HashMap<DirectedGraphNode, Set<DirectedGraphNode>>();
        for (DirectedGraphNode node: graph){
            Set<DirectedGraphNode> set = new HashSet<DirectedGraphNode>();
            map.put(node,set);
        }
        for (DirectedGraphNode node : graph)
            for (DirectedGraphNode temp: node.neighbors)
                map.get(temp).add(node);

        //Construct topological order sequence.
        int len = graph.size();
        while (graph.size()>0) {
            int index = 0;
            while (index<graph.size()){
                DirectedGraphNode node = graph.get(index);
                if (map.get(node).size()==0){
                    graph.remove(node);
                    res.add(node);
                    for (DirectedGraphNode temp: graph)
                        if (map.get(temp).contains(node))
                            map.get(temp).remove(node);
                } else index++;
            }
        }
        return res;
    }
}

```

