# Paths with Sum II

You are given a binary tree in which each node contains an integer value (which might be positive or negative). Design an algorithm to count the number of paths that sum to a given value. The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes)

## Solution

暂时只想到暴力法

## Code 

```java
// Brute Force
int countPath(TreeNode root, int sum){
    if (root == null)
        return 0;

    int pathsRoot = countPathFromNode(root, sum, 0);

    int pathsLeft = countPath(root.left, sum);
    int pathsRight = countPath(root.right, sum);

    return pathsRoot + pathsLeft + pathsRight;
}

int countPathFromNode(TreeNode node, int sum, int curSum){
    if (node == null){
        return 0;
    }

    curSum += node.data;

    int totalPath = 0;
    if (curSum == sum){
        totalPath++;
    }

    totalPath += countPathFromNode(node.left, sum, curSum);
    totalPath += countPathFromNode(node.right, sum, curSum);

    return totalPath;
}
```

