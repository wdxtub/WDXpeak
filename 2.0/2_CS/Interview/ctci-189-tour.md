# Cracking the Code Interview 6th Edition

<!-- MarkdownTOC -->

- 任务列表
	- --------------------
- 1.Big O
	- 例题
	- --------------------
- 2.Arrays and Strings
	- Hash Tables
	- --------------------
- 3.Linked List
	- The "Runner" Technique
	- --------------------
- 4.Stacks and Queues
	- --------------------
- 5.Trees and Graphs
	- Binary Tree Traversal
	- Binary Heaps (Min-Heaps and Max-Heaps)
	- Tries(Prefix Trees)
	- Graphs
	- Graph Search
	- --------------------
- 6.Sorting and Searching
	- Merge Sort
	- Quick Sort
	- Radix Sort
	- Binary Search
	- --------------------
- 7.Bit Manipulation
	- Get Bit
	- Set Bit
	- Clear Bit
	- Update Bit
	- --------------------
- 8.Math and Logic Puzzles
	- Prime Numbers
		- Divisibility
		- Check for Primality
	- Probability
	- Start Talking
	- --------------------
- 9.Recursion and Dynamic Programming
	- Recursive vs. Iterative Solutions
	- Dynamic Programming & Memorization
	- --------------------
- 10.Object-Oriented Design
	- Design Patterns
		- Singleton Class
		- Factory Method
	- --------------------
- 11.System Design and Scalability
	- Key Concepts
	- Considerations
	- --------------------
- 12.Testing
	- --------------------
- 13.C++
	- --------------------
- 14.Java
	- Questions
	- --------------------
- Behavioral Questions
	- Interview Preparation Grid
		- 细致准备重点项目
	- 常见面试问题
	- 问面试官的问题
		- Genuine Questions
		- Insightful Questions
		- Passion Questions
	- 回答问题技巧
		- Nugget First
		- S.A.R. (Situation, Action, Result)
	- --------------------
- 算法题解答技巧
	- Core Data Sturctures, Algorithms, and Concepts
	- A Problem-Solving Flow
		- 1.Listen
		- 2.Example
		- 3.Brute Force
		- 4.Optimize
		- 5.Walk Through
		- 6.Implement
		- 7.Test
	- --------------------
- 表现技巧
	- --------------------
- 基本面试流程
	- --------------------
- 部分公司准备
	- Microsoft
	- Amazon
	- Google
	- Apple
	- Facebook
	- Palantir

<!-- /MarkdownTOC -->


## 任务列表

+ Behavioral Questions 的准备，每天一点点

题目分类分布

1. Arrays and Strings: 9 (1.7, 1.9)
2. Linked List: 8 (2.8)
3. Stacks and Queues: 6
4. **Trees and Graphs**: 12 (4.4 4.5 4.6 4.9 4.11 4.12)
5. Bit Manipulation: 8
6. Math and Logic Puzzles: 10
7. Object-Oriented Design: 10
8. **Recursion and Dynamic Programming**: 14
9. System Design and Scalability: 8
10. **Sorting and Searching**: 11 (10.7)
11. Testing: 6
12. C and C++: 11
13. Java: 8
14. Database: 7
15. Threads and Locks: 7
16. Moderate: 26
17. Hard: 26

### --------------------

## 1.Big O

需要了解如何分析 Time Complexity 以及 Space Complexity.

+ 了解递归情况下的复杂度分析
	+ 根据递推公式模拟几步，然后找到规律进行分析
	+ When you have a recursive function that makes multiple calls, the runtime will often look like O(branches^depth)
+ Big O just describes the rate of increase.
+ Drop the Constants
+ Drop the Non-Dominant Terms
	+ `O(X!)` \> `O(2^x)` \> `O(x^2)` \> `O(x log x)` \> `O(x)` \> `O(log x)`
+ do this, then, when done, do that -\> add the runtime
+ do this for each time you do that -\> multiply the runtime
+ Log N Runtime 来自于二分查找或者诸如二叉树等结构

### 例题

> Suppose we had an algorithm that took in an array of strings, sorted each string, and then sorted the full array. What would the runtime be?

+ Let `s` be the length of the longest string
+ Let `a` be the length of the array

The runtime can be get as followed:

+ Sorting each string is `O(s log s)`
+ We have to do this fro every string, `O(a*s log s)`
+ Now we have to sort all the strings. Need to campare the strings. Each string comparison takes `O(s)` time. There are `O(a log a)` comparisons, therefore this will take `O(a*s log a)` time
+ Add up these two parts, you get `O(a*s(log a + log s))`

> The following simple code sums the values of all the nodes in a balanced binary search tree. What is its runtime?

	int sum(Node node){
	    if (node == null){
	        return 0;
	    }
	    return sum(node.left) + node.value + sum(node.right);
	}

*有树结构并不意味着 runtime 中一定会有 log*

The runtime will be linear in terms of the number of nodes. If there are N nodes, then the runtime is O(N)

> What is the time complexity of this function?

	boolean isPrime(int n){
	    for (int x = 2; x * x <= n; x++){
	        if (n % x == 0){
	            return false;
	        }
	    }
	    return true;
	}

The for loop will start when `x = 2` and end when `x * x = n`, aka √n. So it runs in O(√n) time.

> This code prints all permutations of a string. What is its time complexity?

	void permuation(String str){
	    permutation(str, "");
	}

	void permutation(String str, String prefix){
	    if (str.length() == 0){
	        System.out.println(prefix);
	    }
	    else {
	        for (int i = 0; i < str.length(); i++){
	            String rem = str.substring(0,i) + str.substring(i+1);
	            permutation(rem, prefix + str.charAt(i));
	        }
	    }
	}

可以有两种不同的思路: What It Means 和 What It Does.

**What It Means**

因为是求排列，如果一个字符串有`n`个字符，那么所有的可能为`n*(n-1)*...*2*1` -\> `O(n!)`

**What It Does**

设一共有`n`个字符，第一次循环，有`n`次递归调用，第二次有`n-1`次，到最后一共有`n*(n-1)*...*2*1` -\> `O(n!)`

> The following code computes the Nth Fibonacci number

	int fib(int n){
	    if (n <= 0) return 0;
	    else if (n == 1) return 1;
	    return fib(n-1) + fib(n-2);
	}

There are 2 branches per call, and we go as deep as N, there fore the runtime is O(2^N)

**Generally speaking, when you see an algorithm with multiple recursive calls, you're looking at exponential runtime**

> The following code prints all Fibonacci numbers from 0 to n. What is its time complexity?

	void allFib(int n){
	    for (int i = 0; i < n; i++){
	        System.out.println(i + ": " + fib(i));
	    }
	}

	int fib(int n){
	    if (n <= 0) return 0;
	    else if (n == 1) return 1;
	    return fib(n-1) + fib(n-2);
	}

这题的特点是，循环中的递归次数因为`i`的值的不同是不同的。例如：

	fib(1) -> 2^1 steps
	fib(2) -> 2^2 steps
	fib(3) -> 2^3 steps
	fib(4) -> 2^4 steps
	...
	fib(n) -> 2^n steps

所以把这些加起来的总和为：`2^1 + 2^2 + 2^3 +...+ 2^n = 2^(n+1)` -\> O(2^n)

> The following code performs integer idvision. What is its runtime (assume a and b are both positive)?

	int div(int a, int b){
	    int count = 0;
	    int sum = b;
	    while (sum <= a){
	        sum += b;
	        count++;
	    }
	    return count;
	}

O(a/b). The variable count will eventually equal 1/b. The while loop iterates count times. Therefore, it iterates a/b times.

### --------------------

## 2.Arrays and Strings

### Hash Tables

A hash table is ad data structure that maps keys to values for highly efficient lookup.

If the number of collisions is very high, the worst case runtime is O(N), where N is the number of keys. However, we generally assume a good implementation that keeps collisions to a minimum, in which case the **lookup time is O(1)**.

可以用一个数组，数组的每个元素是一个链表来实现。

### --------------------

## 3.Linked List

When you're discussing a linked list in an interview, you must understand whether it is a singly linked list or a doubly linked list.

### The "Runner" Technique

The "runner"(or second pointer) technique is used in many linked list problems. The runner technique means that you iterate through the linked list with two pointers simultaneously, with one ahead. The "fast" node might be ahead by a fixed amount, or it might be hopping multiple nodes for each one node that "slow" node iterates through.

### --------------------

## 4.Stacks and Queues

+ Stack - LIFO
+ Queue - FIFO

Both can be implemented by linked list

### --------------------

## 5.Trees and Graphs

Tree and graph questions are rife with ambiguous details and incorrect assumptions. Be sure to watch out for the following issues and seek clarification when necessary

+ Trees vs. Binary Trees
+ Binary Tree vs. Binary Search Tree
	+ all left descendants \<= n \< all right descendants
	+ the definition of a binary search tree can vary slightly with respect to quality. Under some definitions, the tree cannot have duplicate values. In others, the duplicate values will be on the right or can be on either side. All are valid definitions, but you should clarify this with your interviewer.
+ Balanced vs. Unbalanced
+ Complete Binary Trees
	+ A complete binary tree is a binary tree in which every level of the tree is fully filled, except for perhaps the last level. To the extent that the last level is filled, it is filled left to right.
+ Full Binary Trees
	+ A full binary tree is a binary tree in which every node has either zero or two children. That is, no nodes have only one child.
+ Perfect Binary Trees
	+ A perfect binary tree is one that is both full and complete. All leaf nodes will be at the same level, and this level has the maximum number of nodes.

### Binary Tree Traversal

**In-Order Traversal**

left, current, right

	void inOrderTraversal(TreeNode node){
	    if (node != null){
	        inOrderTraversal(node.left);
	        visit(node);
	        inOrderTraversal(node.right);
	    }
	}

**Pre-Order Traversal**

current, left, right

	void preOrderTraversal(TreeNode node){
	    if (node != null){
	        visit(node);
	        preOrderTraversal(node.left);
	        preOrderTraversal(node.right);
	    }
	}

**Post-Order Traversal**

left, right, current

	void postOrderTraversal(TreeNode node){
	    if (node != null){
	        postOrderTraversal(node.left);
	        postOrderTraversal(node.right);
	        visit(node);
	    }
	}

### Binary Heaps (Min-Heaps and Max-Heaps)

A min-heap is a complete binary tree (that is, totally filled other than the right most elements on the last level) where each node is smaller than its children. The root, therefore, is the minimum element in the tree.

### Tries(Prefix Trees)

A trie is a variant of an n-ary tree in which characters are stored at each node. Each path down the tree may represent a word.

The \* nodes are often used to indicate complete words.

Very commonly, a trie is used to store the entire (English) language for quick prefix lookups. While a hash table can quickly look up whether a string is a valid word, it cannot tell us if a string is a prefix of any valid words.

### Graphs

+ Graphs can be either directed or undirected. While directed edges are like a one-way street, undirected edges are like a two-way street.
+ The graph might consist of multiple isolated subgraphs. If there is a path between every every pair of vertices, it is called a "connected graph"
+ The graph can also have cycles. An "acyclic graph" is one without cycles

**Adjacency List**

Most common way to represent a graph. Every vertex stores a list of adjacent vertices. In an undirected graph, an edge like (a,b) would be stored twice

	class Graph{
	    public Node[] nodes;
	}

	class Node {
	    public String name;
	    public Node[] children;
	}

**Adjacency Matrices**

an NxN boolean matrix (where N is the number of nodes), where a true value at `matrix[i][j]` indicates an edge from node i to node j.

### Graph Search

DFS & BFS

**DFS Depth-First Search**

Note that pre-order and other forms of tree traversal are a form of DFS. The key difference is that when implementing this algorithm for a graph, we must check if the node has been visited. If we don't, we risk getting stuck in an infinite loop

	void search(Node root){
	    if (root == null) return;
	    visit(root);
	    root.visited = true;
	    for each (Node n in root.adjacent){
	        if (n.visited == false){
	            search(n);
	        }
	    }
	}

**BFS Breadth-First Search**

BFS uses a queue. In BFS, node `a` visits each of `a's` neighbors before visiting any of their neighbors. An iterative solution involving a queue usually works best.

	void search(Node root){
	    Queue queue = new Queue();
	    root.marked = true;
	    queue.enqueue(root);

	    while (!queue.isEmpty()){
	        Node r = queue.dequeue();
	        visit(r);
	        foreach(Node n in r.adjacent){
	            if (n.marked == false){
	                n.marked = true;
	                queue.enqueue(n);
	            }
	        }
	    }
	}

If you are asked to implement BFS, the key thing to remember is the use of the queue. The rest of the algorithm flows from this fact.

**Bidirectional Search**

Bidirectional search is used to find the shortest path between a source and destination node. It operates by essentially running two simultaneous breadth-first searches, on from each node. When their searches collide, we have found a path.

### --------------------

## 6.Sorting and Searching

+ Bubble Sort | Runtime: O(n^2) | Memory: O(1)
+ Selection Sort | Runtime: O(n^2) | Memory: O(1)
+ Merge Sort | Runtime: O(n log(n)) | Memory: Depends
+ Quick Sort | Runtime: O(n log(n)) O(n^2) - worst case | Memory: O(log(n))
+ Radix Sort | Runtime: O(kn)

### Merge Sort

Merge sort divides then array in half, sorts each of those halves, and then merges them back together. Each of those halves has the same sorting algorithm applied to it. Eventually, you are merging just two single-element arrays. It is the “merge” part that does all the heavy lifting.

The merge method operates by copying all the elements from the target array segment into a helper array, keeping track of where the start of the left and right halves should be (`helperLeft` and `helperRight`).

	void mergesort(int[] array){
	    int[] helper = new int[array.length];
	    mergesort(array, helper, 0, array.length - 1)
	}

	void merge(int[] array, int[] helper, int low, int middle, int high){
	    for (int i = low; i <= high; i++){
	        helper[i] = array[i];
	    }

	    int helperLeft = low;
	    int helperRight = middle + 1;
	    int current = low;

	    while (helperLeft <= middle && helperRight <= high){
	        if (helper[helperLeft] <= helper[helperRight]){
	            array[current] = helper[helperLeft];
	            helperLefting;
	        }
	        else {
	            array[current] = helper[helperRight];
	            helperRight++;
	        }
	        current++;
	    }

	    int remaining = middle - helperLeft;
	    for (int i = 0; i <= remaining; i++){
	        array[current + i] = helper[helperLeft + i];
	    }
	}

You may notice that only the remaining elements from the left half of the helper array are copied into the target array. Why not the right half? The right half doesn't need to be copied because it's already there.

### Quick Sort

In quick sort, we pick a random element and partition the array, such that all numbers that are less than the partitioning element come before all elements that are greater than it. The partitioning can be performed efficiently through a series of swaps.

	void quickSort(int arr[], int left, int right){
	    int index = partition(arr, left, right);
	    if (left < index - 1){
	        quickSort(arr, left, index - 1);
	    }
	    if (index < right){
	        quickSort(arr, index, right);
	    }
	}

	int partition(int arr[], int left, int right){
	    int pivot = arr[(left + right) / 2];
	    while (left <= right){
	        while (arr[left] < pivot) left++;
	        while (arr[right] > pivot) right--;

	        // Swap elements, and move left and right indices
	        if (left <= right){
	            swap(arr, left, right);
	            left++;
	            right--;
	        }
	    }
	    return left;
	}

### Radix Sort

Takes advantage of the fact that integers have finite number of bits. In radix sort, we iterate through each digit of the number, grouping numbers by each digits.

### Binary Search

注意加一和减一的问题

	int binarySearch(int[] a, int x){
	    int low = 0;
	    int high = a.length - 1;
	    int mid;

	    while (low <= high){
	        mid = (low + high) / 2;
	        if (a[mid] < x){
	            low = mid + 1;
	        }
	        else if (a[mid] > x){
	            high = mid - 1;
	        }
	        else {
	            return mid;
	        }
	    }
	    return -1;
	}

	int binarySearchRecursive(int[] a, int x, int low, int high){
	    if (low > high) return -1;

	    int mid = (low + high) / 2;
	    if (a[mid] < x){
	        return binarySearchRecursive(a, x, mid + 1, high);
	    }
	    else if (a[mid] > x){
	        return binarySearchRecursive(a, x, low, mid - 1);
	    }
	    else{
	        return mid;
	    }
	}

### --------------------

## 7.Bit Manipulation

+ Two's Complement - 负数可以看作是最高位的 1 为负，其他位为正，相加得到最后的值
	+ 例如 -1 = (1111) 最高位的 1 表示 -8， 剩下三位等于 7，相加后等于 -1
+ logical right shift - put a `0` in the most significant bit - `>>>`
+ arithmetic right shift - put a `1` in the most significant bit - `>>`

### Get Bit

Shifts 1 over by `i` bits, creating a value that looks like `00010000`. AND operation

	boolean getBit(int num, int i){
		return ((num & (1 << i)) != 0);
	}

### Set Bit

Shifts 1 over by `i` bits, creating a value like `00010000`. OR operation

	int setBit(int num, int i){
		return num | (1 << i);
	}

### Clear Bit

Create a number like `11101111` by creating the reverse of it (`00010000`). AND operation.

	int clearBit(int num, int i){
		int mask = ~(1 << i);
		return num & mask;
	}

To clear all bits from the most significant bit through `i` (inclusive), we create a mask with a `1` at the ith bit(1 << i). Then we subtract 1 from it, giving us a sequence of 0s followed by i 1s. AND operation.

	int clearBitsMSBthroughI(int num, int i){
		int mask = (1 << i) - 1;
		return num & mask;
	}

To clear bits from i through 0 (inclusive), we take a sequence of 1s (which is -1) and shift it over by 31 - i bits.

	int clearBitsIthrough0(int num, int i){
		int mask = ~(-1 >>> (31 - i));
		return num & mask;
	}

### Update Bit

Set the ith bit to a value `v`

	int updateBit(int num, int i, boolean bitIs1){
		int value = bitIs1 ? 1 : 0;
		int mask = ~(1 << i);
		return (num & mask) | (value << i);
	}

### --------------------

## 8.Math and Logic Puzzles

### Prime Numbers

Every positive integer can be decomposed into a product of primes

#### Divisibility

Let x = 2^(j0) * 3^(j1) * 5 ^(j2) * .....

Let y = 2^(k0) * 3^(k1) * 5 ^(k2) * .....

If mod(y, x) == 0, for all i, ji < ki

gcd(x,y) = 2^min(j0,k0) * 3^min(j1,k1) * 5^min(j2,k2) * ...

lcm(x,y) = 2^max(j0,k0) * 3^max(j1,k1) * 5^max(j2,k2) * ...

gcd * lcm = xy

#### Check for Primality

	boolean prime(int n){
		if (n < 2){
			return false;
		}
		int sqrt = (int) Math.sqrt(n);
		for (int = 2; i <= sqrt; i++){
			if (n % i == 0) return false;
		}
		return true;
	}

### Probability

P(A and B) = P(B given A) P(A)

P(A or B) = P(A) + P(B) - P(A and B)

### Start Talking

Don't panic when you get a brainteaser. Like algorithm questions, interviewers want to see how you tackle a problem; they don't expect you to immediately know the anser. Start talking, and show the interviewer how you approach a problem.

### --------------------

## 9.Recursion and Dynamic Programming

+ Recursive solutions, by definition, are built off of solutions to subproblems.
+ The bottom-upa approach is ofent the most intuitive. Start with simple case.
+ The top-down approach can be more complex since it's less concrete. We think about how we can divide the problem for case N into subproblems.
+ Half-and-Half Approach -> Binary Search

### Recursive vs. Iterative Solutions

+ Recursive algorithms can be very space inefficient.
+ Each recursive call adds a new layer to the stack, which means that if your algorithm recurses to a depth of n, it uses at lest O(n) memory.
+ **All** recursive algorithms can be implemented iteratively, although sometimes the code to do so is much more complex.

### Dynamic Programming & Memorization

+ Taking a recursive algorithm and finding the overlapping subproblems.
+ Cache those results for future recursive calls.

一个例子: Fibonacci Numbers

Recursive

	int fibonacci(int i){
		if (i == 0) return 0;
		if (i == 1) return 1;
		return fibonacci(i-1) + fibonacci(i-2);
	}

Cache the results of fibonacci(i) between calls

	int fibonacci(int n){
		return fibonacci(n, new int[n+1]);
	}

	int fibonacci(int i, int[] memo){
		if (i == 0 || i == 1) return i;

		if (memo[i] == 0){
			memo[i] = fibonacci(i-1, memo) + fibonacci(i-2, memo);
		}
		return memo[i];
	}

Bottom-Up Dynamic Programming

	int fibonacci(int n){
		if (n == 0) return 0;
		else if (n == 1) return 1;

		int[] memo = new int[n];
		memo[0] = 0;
		memo[1] = 1;
		for (int i = 2; i < n; i++){
			memo[i] = memo[i-1] + memo[i-2];
		}
		return memo[n-1] + memo[n-2];
	}

Just store afew variables

	int fibonacci(int n){
		if (n == 0) return 0;
		int a = 0;
		int b = 1;
		for (int i = 2; i < n; i++){
			int c = a + b;
			a = b;
			b = c;
		}
		return a + b;
	}

---

### --------------------

## 10.Object-Oriented Design

1. Step1: Handle Ambiguity
	+ make assumptions & ask clarifying questions
	+ **who** is going to use it and **how** they are going to use it
	+ who, what, where, when, how, why
2. Define the core objects
	Suppose we are designing for a restaurant. Our core objects might be things like `Table`, `Guest`, `Party`, `Order`, `Meal`, `Employee`, `Server`, and `Host`.
3. Analyze Relationships
4. Investigate Actions

### Design Patterns

Singleton and Factory Method design patterns are widely used in intervies.

#### Singleton Class

Ensures that a class has only on instance and ensures access to the instance through the application. It can be useful in cases where you have a "global" object with exactly one instance.

```java
public class Restaurant{
	private static Restaurant _instance = null;
	protected Restaurant() {...}
	public static Restaurant getInstance(){
		if (_instance == null){
			_instance = new Restaurant();
		}
		return _instance;
	}
}
```

#### Factory Method

Offers an interface for creating an instance of a class, with its subclasses deciding which class to instantiate.

```java
public class CardGame {
	public static CardGame createCardGame(GameType type){
		if (type == GameType.Poker) {
			return new PokerGame();
		}
		else if (type == GameType.BlackJack) {
			return new BlackJackGame();
		}
		return null;
	}
}
```

### --------------------

## 11.System Design and Scalability

**Handling the Question**

+ **Communicate**: A key goal of system design questions is to evaluate your ability to communicate. Stay engaged with the interviewer. Ask them questions. Be open about the issues of your system.
+ **Go broad first**: Don't dive straight into the algorithm part or get excessively focused on one part.
+ **Use the whiteboard**: Using a whiteboard helps your interviewer follow your proposed design. Get up to the whiteboard in the very beginning and use it to draw a picture of what you're proposing.
+ **Acknowledge interview concerns**: Your interviewer will likely jump in with concers. Don't brush them off; validate them. Acknowledge the issues your interviewer points out and make changes accordingly.
+ **Be careful about assumptions**: An incorrect assumption can dramatically change the problem.
+ **State your assumptions explicitly**: When you do make assumptions, state them. This allows your interviewer to correct you if you're mistaken, and shows that you at least know what assumptions you're making.
+ **Estimate when necessary**: In many cases, you might not have the data you need. You can estimate this with other data you know.
+ **Drive**: As the candidate, you should stay in the driver's seat. This doesn't mean you don't talk to your interviewer; in fact, you *must* talk to your interviewer. However, you should be driving through the question. Ask questions. Be open about tradeoffs. Continue to go deeper. Continue to make improvements.

**Design**

1. Scope the Problem
2. Make Reasonable Assumption
3. Draw the Major Components
4. Identify the Key Issues
5. Redesign for the Key Issues

**Algorithms that Scale**

In some cases, you're being asked to design a single feature or algorithm, but you have to do it in a scalable way.

1. Ask Questiosn
2. Make Believe
3. Get Real
4. Solve Problems

### Key Concepts

**Horizontal vs. Vertical Scaling**

+ Vertical scaling means increasing the resoures of a specific node. For example, you might add additional memory to a server to improve its ability to handle load changes.
+ Horizontal scaling means increasing the number of nodes. For example, you might add additional servers, thus decreasing the load on any one server.

Vertiacal scaling is generally easer than horizontal scaling, but it's limited.

**Load Balancer**

Typically, some frontend parts of a scalable website will be thrown behind a load balancer. This allows a system to distribute the load evenly so that one server doesn't crash and take down the whole system. To do so, of course, you have to build out a network of cloned servers that all have essentially the same code and access to the same data.

**Database Denormalization and NoSQL**

Joins in a relational database such as SQL can get very slow as the system grows bigger. For this reason, you would generally avoid them.

Denormalization is one part of this. Denormalization means adding redundant information into a database to speed up reads. For example, imagine a database describing projects and tasks (in addition to the project table).

Or, you can go with a NoSQL database. A NoSQL database does not support joins and might structure data in a different way. It is designed to scale better..

**Database Partitioning (Sharding)**

Sharding means splitting the data across multiple machines while ensuring you have a way of figuring out which data is on which machine.

A few common ways of partitioning include:

+ **Vertical Partitioning**: This is basically partitioning by feature.
+ **Key-Based (or Hash-Based) Partitioning**: This uses some part of the data to partition it. A very simple way to do this is to allocate N servers and put he data on mode(key, n). One issue with this is that the number of servers you have is effectively fixed. Adding additional servers means reallocating all the data -- a very expensive task.
+ **Directory-Based Partitioning**: In this scheme, you maintain a lookup table for where the data can be found. This makes it relatively easy to add additional servers, but it comes with two major drawbacks. First the lookup table can be a single point of failure. Second, constantly access this table impacts performance.

**Caching**

An in-memory cache can deliver very rapid results. It is a simple key-value pairing and typically sits between your application layer and your data store.

**Asynchronous Processing & Queues**

Slow operations should ideally be done asynchronously. Otherwise, a user might get stuck waiting and waiting for a process to complete.

**Networking Metrics**

+ **Bandwidth**: This is the maximum amount of data that can be transferred in a unit of time. It is typically expressed in bits per seconds.
+ **Throughput**: Whereas bandwidth is the maximum data that can be transferred in a unit of time, throughput is the actual amoutn of data that is transferred.
+ **Latency**: This is how long it takes data to go from one end to the other. That is, it is the delay between the sender sending information (even a very small chunk of data) and the receiver receiving it.

**MapReduce**

A MapReduce program is typically used to process large amounts of data.

+ Map takes in some data and emits a <key, value> pair
+ Reduce takes a key and a set of associated values and "reduces" them in some way, emitting a new key and value.

MapReduce allows us to do a lot of processing in parallel, which makes processing huge amounts of data more scalable.

### Considerations

+ **Failures**: Essentially any part of a system can fail. You'll need to plan for many or all of these failures.
+ **Availability and Reliability**: Availability is a function of the percentage of time the system is operatoinal. Redliability is a function of the probability that the system is operational for a certain unit of time.
+ **Read-heavy vs. Write-heavy**: Whether an application will do a lot of reads or a lot of writes implacts the design. If it's write-heavy, you could consider queuing up the writes (but think about potential failure here!). If it's read-heavy, you might want to cache.
+ **Security**: Security threats can, of course, be devastating for a system. Think about the tyupes of issues a system might face and design around thos.

### --------------------

## 12.Testing

**What the Interviewer Is Looking For**

+ Big Picture Understanding
+ Knowing How the Pieces Fit Together
+ Organization
+ Practicality

**TEsting a Real World Object**

1. Who will use it? And why?
2. What are the use cases?
3. What are the bounds of use?
4. What are the stress / failure conditions?
5. How would you perform the testing?

**Testing a Piece of Software**

1. Are we doing Black Box Testing or White Box Tesing?
2. Who will use it? And why?
3. What are the use cases?
4. What are the bounds of use?
5. What are the stress conditions / failure conditions
6. What are the test cases? How would you perform the testing?

**Testing a Function**

1. Define the test cases
	+ The normal case
	+ The extremes
	+ Nulls and "illegal" input
	+ Strange input
2. Define the expected result
3. Write test code

**Troubleshooting Questions**

1. Understand the Scenario
2. Break Down the Problem
3. Create Specific, Manageable Tests

### --------------------

## 13.C++

+ Classes and Inheritance
+ Constructors and Destructors
+ Virutal Functions
+ Virtual Destructor
+ Default Values
+ Operator Overloading
+ Pointer and References
+ Templates

### --------------------

## 14.Java

+ Overlading vs. Overriding
	+ Overloading is a term used to describe when two methods have the same name but differ in the type or number of arguments
	+ Overriding occurs when a method shares the same name and function signature as another method in its super class
+ ArrayList
	+ ArrayList<String> myArr = new ArrayList<String>();
	+ myArr.add("one");
	+ System.out.println(myArr.get(0));
+ Vector
	+ Vector<String> myVect = new Vector<String>();
	+ myVect.add("one");
	+ System.out.println(myVect.get(0));
+ LinkedList
	+ LinkedList<String> myLinkedList = new LinkedList<String>();
	+ myLinkedList.addFirst("two");
	+ myLinkedList.addFirst("one");
	+ Iterator<String> iter = myLinkedList.iterator();
	+ while (iter.hashNext()) { System.out.println(iter.next()); }
+ HashMap
	+ HashMap<String, String> map = new HashMap<String, String>();
	+ map.put("one", "uno");
	+ map.put("two", "dos");
	+ System.out.println(map.get("one"));

### Questions

> Private Constructor: In terms of inheritance, what is the effect of keeping

This has direct implications for inheritance, since a subclass calls its parent's constructor. The class A an be inherited, but only by its own or its parent's inner classes.

> Return from Finally: In java, does the `finally` block get executed if we insert a return statements inside the try block of a `try-catch-finally`?

Yes, it will get executed. The `finally` block gets executed when the `try` block exits.

There are some cases in which the `finally` block will not get executed, such as the following:

+ If the virtual machine exits during try/catch block execution
+ If the thread which is executing during the try/catch block gets killed

> Final, etc.: What is the difference between final, finally, and finalize?

+ final - control whether a variable, method, or class is "change-able"
+ finally - used in a try/catch block to ensure that a segment of code is always executed
+ finalize() - called by garbage collector once it determines that no more references exist.

> Generics vs. Templates: Explain the difference between templates in C++ and generics in Java?

The implementation of Java generics is rooted in an idea of "type erasure". This technique eliminates the parameterized types when source code is translated to the Java Virtual Machine (JVM) byte code.

The use of Java generics didn't really change much about our capabilities; it just made things a bit prettier. For this reason, Java generics are sometimes called "syntactic sugar"

In C++, templates are essentially a glorified macro set, with the compiler creating a new copy of the template code for each type.

> TreeMap, HashMap, LinkedHashMap: Explain the differences between these three. Provide an example of when each one would be best

+ `HashMap` offers O(1) lookup and insertion. It is implemented by an array of linked lists.
+ `TreeMap` offers O(log N) lookup and insertion. Keys are ordered. It is implemented by a Red-Black Tree.
+ `LinkedHashMap` offers O(1) lookup and insertion. Keys are ordered by their insertion order. It is implemented by doubly-linked buckets.

> Object Reflection: Explain what object reflection is in Java and why it is useful.

Provides a way to get relfective information about Java classes and objects, and perform operations such as:

+ Getting information about the methods and fields present inside the class at runtime.
+ Creating a new instance of a class
+ Getting and setting the object fields directly by getting field reference, regardless of what the access modifier is.

Three main reasons why Object Reflection is Useful:

1. It can help you observe or manipulate the runtime behavior of applications
2. It can help you debug or test programs, as you have direct access to methods, constructors, and fields.
3. You can call methods by name when you don't know the method in advance.

### --------------------

## Behavioral Questions

### Interview Preparation Grid

针对每个 project，列出以下几个方面的相关总结关键词，一定要是**特别精炼的短语**，不要长篇大论的句子：

+ Challenges
+ Mistakes/Failures
+ Enjoyed
+ Leadership
+ Conflicts
+ What You'd Do Differently

#### 细致准备重点项目

两三个 project 要重点准备，除了上面提到的方面，还需要能够细致介绍：

+ Technical decisions
+ Choices of technologies(tradeoff)

### 常见面试问题

> Tell me about yourself

可以按照如下的方式组织准备

1. **Current Role [Headline Only]**: I'm a graduate student in Carnegie Mellon University majored in Electrical and Computer Engineering.
2. **College**: I majored in Software Engineering for my undergraduate and had a 6-month internship in Microsoft.
3. **Current Role [Details]**: Learning both the software and the hardware, I know how to write great code on different platforms, especially computer vision and machine learning.
4. **Outside of Work**: Outside of work, I've been working on mobile app development. One of my app named League of Legends Wiki has over 700K downloads with an average rating of 4.5 out of 5.
5. **Wrap Up**: I'm looking for a full time job as I'll get my master degree next year and your company caught my eye. I've always been interested in creating something new so I'd like to talk more with you about the xxx position in your company.

注意见缝插针描述自己的闪光点，让人感兴趣和印象深刻。

> What are your weaknesses

回答技巧：实话实话，不要装逼。点明缺点之后重点强调自己是如何克服的。

个人参考答案：Sometimes, I may lose focus on the whole project while plunge into very detailed problems. It's not bad to spend more time finding the best solution. But it may be better to finish the most critical part first. As it is, I'll draw the whole design on paper and put it just in front of the monitor so that I can easily find out what I should focus on.

### 问面试官的问题

大概有三类问题

#### Genuine Questions

跟公司，工作有关的问题，例如

1. What brought you to this company?
2. What has been most challenging for you?
3. Do you have program managers? If there is a conflicts between developer and managers, how do you solve it?

#### Insightful Questions

这类问题通常需要对公司有比较深入的研究，例如

1. I noticed that you use technology X. How do you handle problem Y?
2. Why did this product choose to use technology X over technology Y?

#### Passion Questions

展现激情和学习兴趣

1. I'm very interested in machine learning, and I'd love to learn more about it. What opportunities are there at this company to learn about this?
2. I'm not familiar with technology X, but it sounds like a very interesting solution. Could you tell me a bit more about how it works?

### 回答问题技巧

+ 不要过多涉及细节，而是用数据对比或者面试官能听懂的内容来介绍
+ 多说 I 而不是 We，说自己扮演的角色和所做的工作
+ 结构式问题回答

#### Nugget First

开门见山，先用一句话概括，然后再逐步推进到细节部分

#### S.A.R. (Situation, Action, Result)

+ outline the situation
+ explain the actions you took
+ describe the result

**Action 部分是最需要着力的地方，逻辑清晰，分点叙述，主要不要涉及过多细节**。

精雕细琢故事部分，字里行间体现出自己的一些特质，如：Initiative/Leadership, Empathy, Compassion, Humility, Teamwork/Helpfulness

### --------------------

## 算法题解答技巧

+ 掌握基本的数据结构，算法及概念
+ Most interviewers won't ask about specific algorithms for binary tree balancing or other complex algorithms(他们可能自己都不太记得了，因为不常用)

### Core Data Sturctures, Algorithms, and Concepts

+ Data Structures
	+ Linked Lists
	+ Trees, Tries, & Graphs
	+ Stacks & Queues
	+ Heaps
	+ Vectors / ArrayLists
	+ **(!)Hash Tables**
+ Algorithms
	+ Breadth-First Search
	+ Depth-First Search
	+ Binary Search
	+ Merge Sort
	+ Quick Sort
+ Concepts
	+ Bit Manipulation
	+ Memory (Stack vs. Heap)
	+ Recursion
	+ Dynamic Programming
	+ Big O Time & Space

### A Problem-Solving Flow

**BUD Optimization**: **B**ottlenecks, **U**nnecessary Work, **D**uplicated Work

A bottleneck is a part of your algorithm that slows down the overall runtime. There are two common ways this occurs:

+ You have one-time work that slows down your algorithm.
+ You have a chunk of work that's done repeatedly, like searching.

#### 1.Listen

**Pay very close attention** to any information in the problem description. You probably need it all for an optimal algorithm.

+ record **unique** information
+ use all the information in the problem
+ write the pertinent information on the whiteboard

#### 2.Example

Most examples are too small or are special cases. **Debug your example**. Is there any way it's a special case? Is it big enough?

Go to the whiteboard and draw an example:

+ Specific: use real numbers or strings
+ Sufficiently large
+ Not a special case

Try to make the best example you can.

#### 3.Brute Force

Get a brute-force solution as soon as possible. Don't worry about developing an efficient algorithm yet. State a naive algorithm and its runtime, then optimize from there. Don't code yet though!

#### 4.Optimize

Walk through your brute force with **BUD optimization** and try some of these ideas:

+ Look for any unused info. You usually need all the information in a problem.
+ Solve it manually on an example, then reverse engineer your thought process. How did you solve it?
+ Solve it "incorrectly" and then think about why the algorithm fails. Can you fix those issues?
+ Make a time vs. space tradeoff. Hash tables are especially useful!
+ Precompute information. Is there a way that you can reorganize the data(sorting, etc.) or compute some values upfront that will help save time in the long run?
+ Use a hash table. Hash tables are widely used in interview questions and should be at the top of your mind.
+ Think about the best conceivable runtime.

#### 5.Walk Through

Now that you have an optimal solution, **walk through your approach in detail**. Make sure you understand each detail before you start coding.

Whiteboard coding is slow, very slow. You need to make sure that you get it as close to "perfect" int he beginning as possible.

#### 6.Implement

Your goal is to **write beautiful code**. Modularize your code from the beginning and refactor to clean up anything that isn't beautiful.

**Keep talking!** Your interviewer wants to hear how you approach the problem.

Beautiful code means:

+ **Modularized code**: good coding style & make things easier for you.
+ **Error checks**: add a `todo` and then just explain out loud what you'd like to test.
+ **Use other classes/structs where appropriate**: e.g. points in 2 or 3 dimension
+ **Good variable names**

#### 7.Test

Test in this order:

1. Conceptual test. Walk through your code like you would for a detailed code review.
2. Unusual or non-standard code.
3. Hot spots, like arithmetic and null nodes.
4. Small test cases. It's much faster than a big test case and just as effective.
5. Special cases and edge cases.

And when you find bugs, **fix them carefully!**

### --------------------

## 表现技巧

+ Whiteboards ten to encourage candidates to speak more and explain their thought process.
+ Getting a hard question isn't a bad thing.
+ If you haven't heard back from a company within 3-5 business days after your interview(1 week after on-site), check in (politely) with your recruiter.

### --------------------

## 基本面试流程

+ (1-2)phone-screen interview
+ (3-6)on-site


### --------------------

## 部分公司准备

### Microsoft

+ write code on board
+ 4 or 5 interviews, often with two different teams
+ speak with hiring manager means passing the interview with a particular team

**必须准备**

> Why do you want to work for Microsoft?

passion about technology, product, etc

### Amazon

+ usually 1 phone screen interview
+ write code via a shared document editor
+ 4 or 5 interviews, one or two teams
+ bar raiser - harder questions

**必须准备**

scalability questions, object-oriented design

### Google

+ phone screen interview - engineer - tough technical questions
+ 4 to 6 interviews

**必须准备**

scalable system, system design and scalability, algorithm skills

### Apple

+ excellent technical skills
+ passion
+ 1 recruiter phone screen
+ a series of technical phone screens
+ 6 to 8 interviews, one-on-one or two-on-one
+ code on whiteboard

**必须准备**

如果知道是哪个 team 面试你，去熟悉对应的产品。 What do you like about it? What would you improve? show the passion

### Facebook

+ 1 or 2 phone screen interview
+ homework, code style
+ (1)Behavioral, (2)Coding and Algorithms, (1)Design/Architecture

**必须准备**

entrepreneurial spirit, love to build stuff fast

### Palantir

+ interview for a specific team
+ 2 phone screen interviews(30-45 min)
+ HackerRank coding assessment
+ up to 5 interviews

**必须准备**

more challenging questions, core data structures, system design(backend), 提前准备与训练 HarkerRank.com


