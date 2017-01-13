# Social Network

How would you design the data structures for a very large social network like Facebook or LinkedIn? Describe how you would design an algorithm to show the shortest path between two people (e.g., Me -> Bob -> Susan -> Jason -> You)

## Solution

construct a graph by treating each person as a node and letting an edge between two nodes indicate that the two users are friends.

BFS search -> bidirectional breadth-first-search

Suppose every person has k friends, and node S and node D have a friend C in common.

+ Traditional bfs from S to D: go through `k+k*k` nodes
+ Bidirectional bfs: go through 2k nodes

Generalizing this to a path of length q

+ BFS: O(q^k)
+ Bidirectional BFS: O(q^(k/2) + q^(k/2))

### Handle the Millions of User

data in different machines, use hashtable or other mechanism to index them and search them for the same time.

Optimization:

+ Reduce machine jumps
+ Smart division of people and machines(related data should be put together)
+ Instead of marking VISITED, we use a hashtable to record the nodes we have already visited

