# Rank from Stream

Imagine you are reading in a stream of integers. Periodically, you wish to be able to look up the rank of a number x (the number of values less than or equal to x). Implement the data structures and algorithms to support these operations. That is, implement the method track(int x), which is called when each number of values less than or equal to x (not including x itself).

EXAMPLE

    Stream (in order of appearance): 5, 1, 4, 4, 5, 9, 7, 13, 3
    getRankOfNumber(1) = 0
    getRankOfNumber(3) = 1
    getRankOfNumber(4) = 3

## Solution

 Use a Binary Search Tree to finish the job
 
 	int getRank(Node node, int x){
 		if x is node.data, return node.leftSize()
 		if x is on left of node, return getRank(node.left, x)
 		if x is on right of node,
 		return node.leftSize()+ 1 + getRank(node.right, x)

## Code

```java
RankNode root = null;

void track(int number){
    if (root == null){
        root = new RankNode(number);
    } else {
        root.insert(number);
    }
}

int getRankOfNumber(int number){
    return root.getRank(number);
}

public class RankNode {
    public int left_size = 0;
    public RankNode left, right;
    public int data = 0;
    public RankNode(int d){
        data = d;
    }

    public void insert(int d){
        if (d < data){
            if (left != null) left.insert(d);
            else left = new RankNode(d);
            left_size++;
        }
        else {
            if (right != null) right.insert(d);
            else right = new RankNode(d);
        }
    }

    public int getRank(int d){
        if (d == data){
            return left_size;
        }
        else if (d < data){
            if (left == null) return -1;
            else return left.getRank(d);
        }
        else {
            int right_rank = right == null ? -1 : right.getRank(d);
            if (right_rank == -1) return -1;
            else return left_size + 1 + right_rank;
        }
    }
}
```

