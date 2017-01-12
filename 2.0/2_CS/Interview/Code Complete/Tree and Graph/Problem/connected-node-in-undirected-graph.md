# Connected Nodes in Undirected Graph

请找出无向图中相连要素的个数。

图中的每个节点包含其邻居的 1 个标签和 1 个列表。（一个无向图的相连节点（或节点）是一个子图，其中任意两个顶点通过路径相连，且不与超级图中的其它顶点相连。）

样例

    给定图:
    A------B  C
     \     |  |
      \    |  |
       \   |  |
        \  |  |
          D   E
    返回 {A,B,D}, {C,E}。其中有 2 个相连的元素，即{A,B,D}, {C,E}

## Solution

How do we check for a connected graph (any two nodes are connected)?

Maybe check for each node: each node represents a lead to a subgraph, then check if this subgraph is valid.

1. In real case, need to ask the intervier: can we assume the given nodes are valid, so that we only need to check for success case? That means, we assume for example a linear list A-B-C does not exist.
2. Then, we can use a 'set' to mark: we've checked this node.
3. Use a queue for BFS
4. Use a arraylist to save the results.
5. Key point: when the queue is empty(), that means one set of connected component is ready to go
6. Iterate through nodes, when it's not empty.

More Notes:Have to do Collections.sort()....somehow it want me to sort the results?

Note2: Get rid of a node from nodes, whenever add it to component ... don't forget this.

Note3: Well, there is a chance that compoents are added, queue is cleaned, but nodes are empty as well.. that means, need to catch the last case of 'remaining component' and add it to rst.

## Code

BFS

```java
/**
 * Definition for Undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     ArrayList<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */
public class Solution {
    /**
     * @param nodes a array of Undirected graph node
     * @return a connected set of a Undirected graph
     */
    public List<List<Integer>> connectedSet(ArrayList<UndirectedGraphNode> nodes) {
        List<List<Integer>> rst = new ArrayList<>();
        if (nodes == null || nodes.size() == 0) {
            return rst;
        }
        //Init:
        Set<UndirectedGraphNode> checked = new HashSet();
        Queue<UndirectedGraphNode> queue = new LinkedList();
        ArrayList<Integer> component = new ArrayList<Integer>();

        queue.offer(nodes.get(0));

        while (!nodes.isEmpty()) {
            if (queue.isEmpty()) {
                Collections.sort(component);
                rst.add(component);
                queue.offer(nodes.get(0));
                component = new ArrayList<Integer>();
            } else {
                UndirectedGraphNode curr = queue.poll();
                if (!checked.contains(curr)) {
                    checked.add(curr);
                    component.add(curr.label);
                    nodes.remove(curr);
                    for (UndirectedGraphNode node : curr.neighbors) {
                            queue.add(node);
                    }
                }
            }
        }
        if (!component.isEmpty()) {
            rst.add(component);
        }
        return rst;
    }
}

```

DFS

```java
/**
 * Definition for Undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     ArrayList<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */
public class Solution {
    /**
     * @param nodes a array of Undirected graph node
     * @return a connected set of a Undirected graph
     */
    public List<List<Integer>> connectedSet(ArrayList<UndirectedGraphNode> nodes) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> path = new ArrayList<Integer>();
        Set<UndirectedGraphNode> visited = new HashSet<UndirectedGraphNode>();
        for(UndirectedGraphNode node : nodes){
            if(!visited.contains(node)){
                dfs(node, visited, path);
                Collections.sort(path);
                result.add(new ArrayList<Integer>(path));
                path.clear();
            }
        }
        return result;

    }

    public void dfs(UndirectedGraphNode node, Set<UndirectedGraphNode> visited, List<Integer> path){
        visited.add(node);
        path.add(node.label);
        for(UndirectedGraphNode n : node.neighbors){
            if(!visited.contains(n)){
                dfs(n, visited, path);
            }
        }
    }
}

```

