# Build Order

出处

You are given a list of projects and a list of projects and a list of dependencies (which is a list of pairs of projects, where the first project is dependent on the second project). All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to be built. If there is no valid build order, return an error.

EXAMPLE

    Input:    
    projects: a, b, c, d, e, f
    dependencies: (d, a), (b, f), (d, b), (a, f), (c, d)
    
    Output:
    f, e, a, b, d, c

## Solution

见 CC

## Complexity

## Code

```java
Project[] findBuildOrder(String[] projects, String[][] dependencies){
    Graph graph = buildGraph(projects, dependencies);
    return orderProjects(graph.GetNodes());
}

Graph buildGraph(String projects, String[][] dependencies){
    Graph graph = new Graph();
    for (String project: projects){
        graph.createNode(project);
    }
    for (String[] dependency: dependencies){
        String first = dependency[0];
        String second = dependency[1];
        graph.addEdge(first, second);
    }
    return graph;
}

Project[] orderProjects(ArrayList<Project> projects){
    Project[] order = new Project[projects.size()];

    int endOfList = addNonDependent(order, projects, 0);
    int toBeProcessed = 0;
    while (toBeProcessed < order.length){
        Project current = order[toBeProcessed];

        if (current == null){
            return null;
        }

        ArrayList<Project> children = current.getChildren();
        for (Project child: children){
            child.decrementDependencies();
        }

        endOfList = addNonDependent(order, children, endOfList);
        toBeProcessed++;
    }
    return order;
}

int addNonDependent(Project[] order, ArrayList<Project> projects, int offset){
    for (Project project: projects){
        if (project.getNumberDependencies() == 0){
            order[offset] = project;
            offset++;
        }
    }
    return offset;
}

class Graph {
    private ArrayList<Project> nodes = new ArrayList<Project>();
    private HashMap<String, Project> map = new HashMap<String, Project>();

    public Project getOrCreateNode(String name){
        if (!map.containsKey(name)){
            Project node = new Project(name);
            nodes.add(note);
            map.put(name, node);
        }
        return map.get(name);
    }

    public void addEdge(String startName, String endName){
        Project start = getOrCreateNode(startName);
        Project end = getOrCreateNode(endName);
        start.addNeighbor(end);
    }

    public ArrayList<Project> getNodes(){ return nodes;}
}

class Project{
    private ArrayList<Project> children = new ArrayList<Project>();
    private HashMap<String, Project> map = new HashMap<String, Project>();
    private String name;
    private int dependencies = 0;

    public Project(String n) { name = n;}

    public void addNeighbor(Project node){
        if (!map.containsKey(node.getName())){
            children.add(node);
            node.incrementDependencies();
        }
    }

    public void incrementDependencies(){ dependencies++;}
    public void decrementDependencies(){ dependencies--;}

    public String getName() { return name;}
    public ArrayList<Project> getChildren() {return children;}
    public int getNumberDependencies() { return dependencies;}
}
```

