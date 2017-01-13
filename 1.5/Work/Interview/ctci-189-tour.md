# Cracking the Code Interview 6th Edition

<!-- MarkdownTOC -->

- 任务列表
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
- Big O
	- 例题
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
- Arrays and Strings
	- Hash Tables
- Linked List
	- The "Runner" Technique
- Stacks and Queues
- Trees and Graphs
	- Binary Tree Traversal
	- Binary Heaps (Min-Heaps and Max-Heaps)
	- Tries(Prefix Trees)
	- Graphs
	- Graph Search
- Sorting and Searching
	- Merge Sort
	- Quick Sort
	- Radix Sort
	- Binary Search
- 表现技巧
- 基本面试流程
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
8. Recursion and Dynamic Programming: 14
9. System Design and Scalability: 8
10. Sorting and Searching: 11
11. Testing: 6
12. C and C++: 11
13. Java: 8
14. Database: 7
15. Threads and Locks: 7
16. Moderate: 26
17. Hard: 26

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

---

## Big O

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

---

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
+ You have a chun of work that's done repeatedly, like searching.

#### 1.Listen

**Pay very close attention** to any information in the problem description. You probably need it all for an optimal algorithm.

+ record **unique** information
+ use all the information in the problem
+ write the pertinent information on the whiteborad

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
+ Precompute information. Is there a way that you can reorganize the data(sorting, etc.) or compute som evalues upfront that will help save time in the long run?
+ Use a hash table. Hash tables are widely used in interview questions and should be at the top of your mind.
+ Think about the best conceivable runtime.

#### 5.Walk Through

Now that you have an opimal solution, **walk through your approach inh detail**. Make sure you understand each detail before you start coding.

Whiteborad coding is slow, very slow. You need to make sure that you get it as close to "perfect" int he beginning as possible.

#### 6.Implement

Your goal is to **write beautiful code**. Modularize your code from the beginning and refactor to clean up anything that isn't beautiful.

**Keep taling!** Your interviewer wants to hear how you approach the problem.

Beautiful code means:

+ **Modularized code**: good codign style & make things easier for you.
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

## Arrays and Strings

### Hash Tables

A hash table is ad data structure that maps keys to values for highly efficient lookup.

If the number of collisions is very high, the worst case runtime is O(N), where N is the number of keys. However, we generally assume a good implementation that keeps collisions to a minimum, in which case the **lookup time is O(1)**.

可以用一个数组，数组的每个元素是一个链表来实现。

## Linked List

When you're discussing a linked list in an interview, you must understand whether it is a singly linked list or a doubly linked list.

### The "Runner" Technique

The "runner"(or second pointer) technique is used in many linked list problems. The runner technique means that you iterate through the linked list with two pointers simultaneously, with one ahead. The "fast" node might be ahead by a fixed amount, or it might be hopping multiple nodes for each one node that "slow" node iterrates through.

## Stacks and Queues

+ Stack - LIFO
+ Queue - FIFO

Both can be implemented by linked list

## Trees and Graphs

Tree and graph questions are rife with ambiguous details and incorrect assumptions. Be sure to watch out for the following issues and seek clarification when necessary

+ Trees vs. Binary Trees
+ Binary Tree vs. Binary Search Tree
	+ all left descendents \<= n \< all right descendents
	+ the definition of a binary search tree can vary slightly with respect to quality. Under some definitions, the tree cannot have duplicate values. In others, the duplicate values will be on the right or can be on either side. All are valid definitions, but you should clarify this with your interviewer.
+ Balanced vs. Unbalanced
+ Complete Binary Trees
	+ A complete binary tree is a binary tree in which every level of the tree is fully filled, except for perhaps the lst level. To the extent that th last level is filled, it is filled left to right.
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

Very commonly, a trie is used to store the entire (English) language for quick prefix lookups. While a hash table can quikcly look up whether a string is a valid word, it cannot tell us if a string is a prefix of any valid words.

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

**Adjacentcy Matrices**

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

## Sorting and Searching

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

---

## 表现技巧

+ Whiteboards ten to encourage candidates to speak more and explain their thought process.
+ Getting a hard question isn't a bad thing.
+ If you haven't heard back from a company within 3-5 business days after your interview(1 week after on-site), check in (politely) with your recruiter.

## 基本面试流程

+ (1-2)phone-screen interview
+ (3-6)on-site

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

+ phone screen interview - enginner - tough technical questions
+ 4 to 6 interviews

**必须准备**

scalable system, system design and scalability, algorithm skills

### Apple

+ excellen technical skills
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

