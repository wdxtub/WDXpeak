# Route Between Nodes

Given a directed graph, design an algorithm to find out whether there is a route between two nodes

## Solution

通常的图算法

## Code

```java
enum State {Unvisited, Visited, Visiting;}

boolean search(Graph g, Node start, Node end){
    if (start == end)
        return true;
    Stack<Node> curStep = new Stack<Node>();

    for (Node u : g.getNodes()){
        u.state = State.Unvisited;
    }

    start.state = State.Visiting;
    curStep.push(start);

    while (!curStep.isEmpty()){
        Node u = curStep.pop();
        if (u != null){
            for (Node v : u.getAdjacent()){
                if (v.state == State.Univisted){
                    if (v == end){
                        return true;
                    }
                    else{
                        v.state = State.Visiting;
                        q.push(v);
                    }
                }
            }
        }
        u.state = State.Visited;
    }
    return false;
}
```

