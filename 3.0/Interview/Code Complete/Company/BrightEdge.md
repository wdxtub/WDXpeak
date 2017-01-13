# BrightEdge

<!-- MarkdownTOC -->

- Online Assignment
    - Word Density Analysis
    - FAQ
- Behavior Interview
- 电面
- 一些题目

<!-- /MarkdownTOC -->


## Online Assignment

+ Grading of the assignment will be based on the following:
    + Satisfaction of the requirements specified on the following page
    + Detail orientation
    + Complete documentation presenting the approach and results
+ You are required to submit the assignment within 1 week(s) from the time the assignment email was sent to you.
+ Once you have started the assignment (by clicking the "Begin Assignment" button below), the upload option will be available only for 48 hours (2 days). To be fair to all applicants, we cannot accept late assignments.
+ It is more important to be complete and thorough rather than to turn in the assignment quickly (unless you are close to missing the deadline).
+ Be sure to upload all the deliverables specified in the next page.

### Word Density Analysis

Our Objective:

+ Evaluate core functionality and exception handling (completeness of code)
+ Design on how best to determine relevance, and how best to avoid all the clutter on a busy page
+ OOP
+ Ability to articulate how you built your solution

Expected Deliverables:

+ Executable Jar file or Python files
+ Source Code
+ Documentation - please include examples of sample output from running your program

---

Given any page (URL), be able to classify the page, and return a list of relevant topics.

We'd like to have you build it generically, but for testing purposes, please consider the following URLs.

+ [http://www.amazon.com/Cuisinart-CPT-122-Compact-2-Slice-Toaster/dp/B009GQ034C/ref=sr_1_1?s=kitchen&ie=UTF8&qid=1431620315&sr=1-1&keywords=toaster](http://www.amazon.com/Cuisinart-CPT-122-Compact-2-Slice-Toaster/dp/B009GQ034C/ref=sr_1_1?s=kitchen&ie=UTF8&qid=1431620315&sr=1-1&keywords=toaster)
+ [http://blog.rei.com/camp/how-to-introduce-your-indoorsy-friend-to-the-outdoors/](http://blog.rei.com/camp/how-to-introduce-your-indoorsy-friend-to-the-outdoors/)
+ [http://www.cnn.com/2013/06/10/politics/edward-snowden-profile/](http://www.cnn.com/2013/06/10/politics/edward-snowden-profile/)


Input:

Any URL (for testing purposes, please consider the URLs above)

Output:

+ List of common topics that best describe the contents of that page
+ e.g. 2-Slice Toaster, Cuisinart CPT-122, Compact toaster

How to run/execute the program:

+ Encapsulate your assignment inside an executable jar if you've implemented in Java (e.g. java -jar Assignment.jar ...)
+ Ability to handle the following execution:
    + java -jar Assignment.jar (e.g. java -jar Assignment.jar "http://www.cnn.com/2013/06/10/politics/edward-snowden-profile/")

### FAQ

> Q: Can I use external libraries for HTML parsing?

A: Yes, you can.

> Q: Can I use external libraries for density collection or analysis?

A: No, this is not allowed.

> Q: I am unable to submit my assignment through this webpage. What do I do?

A: Email your submission to your recruiter.

> Q: How should I label my submission?

A: Please include your first and last name in the file name.

> Q: Can I use an API to complete the assignment?

A: No, please don't use any APIs to get the results. The assignment requires you to build a web crawler

> Q: What kind of documentation should I provide?

A: Think about how best you can present the assignment to the grader so that he/she is best able to understand your approach. We would recommend a README file, and clear comments in your code to explain your approach to the problem.

## Behavior Interview

1. 说一说你对 BrightEdge 这个公司的了解。
2. 谈一个你最喜欢的project。
3. 在这个project里你遇到什么困难了吗？你是如何解决它的？
3. 你如何面对工作或者做project时的压力，例如heavy workload， long working time。
4. 假如一个team里有人不太合作你该咋办？
5. 你如何做一个不太popular的决定？（别人都不太支持这个决定）
6. 假如由于你的失误造成了你和你的team members的extra work，你如何解决这个问题？如何跟他们交流？

基本就是这些问题，跟网上大多数的behavior questions差不多，跟托福口语有点像，准备个模板各种套就行。

> 说一说你对 BrightEdge 这个公司的了解

## 电面

最开始是在CMU的校招上投的简历，一天就收到on campus的邮件。on campus轻松水过，一个可爱的中国妹子问了4个题:

1.Remove duplicates in a sorted integer array：

	public int removeDuplicates(int[] nums)

返回删好后的length。就扫一遍就完了

2.m*n的矩阵走格子，只能向下或者向右。返回总路线数量

public int pathSum(int m, int n)

3.判断二叉树是不是BST

4.生成n-bit的gray code (不知道的童鞋请自行google)

一个无难度题 ＋ 仨leetcode原题。四个题加讲一共花了30分钟，然后妹子说她就准备了四个题...问我有什么问题。她后来说这个公司还处在start up阶段，所以非常累要有心理准备。


结果过了两天又让我面下一轮online coding。这点比较奇怪，因为和我一起的其他童鞋都直接面behavior了，难道是我的assignment做的比较差？我更倾向于认为他们根本忘了我参加过on campus

下轮是个阿三哥哥。问project和background特别详细，简直查户口，用了20分钟。然后两个题：

1.deepest common ancestors (大家怎么都喜欢问这个？)

node有parent指针的。用hashmap记下来的方法他觉得就可以了。

2.design a parking lot. Each lot has several floors, and each floor has many slots. Slots can be in two status: abled or disabled.

Your design should support the following method with high efficiency:

	public int getNumberOfCars(int floor)
	public int getTotalNumberOfSlots(int floor)
	public int geNumberOfDisableSlots(int floor)

这个题真是给我坑坏了。parking lot我也看了挺多，上来就给了一个Class floor, 里面有ArrayList<Slot>和HashMap\<Slot, Car\>。三哥说我根本不在乎car你为什么要一个map？我心里想你不在乎car你设计什么parking lot...后来知道他只想要那几个方程返回的total number，所以就把他们都存起来就完了...晕。然后他又问我什么时候更改这些维护的值，我说加一个函数park(int floor)就完了。

说实话我真不懂这题他究竟想干什么，难道就是要我存那几个整数？总之这轮居然也过了...我发现三哥是不会好好问算法题的，总是会带一些design和基础知识(比如设计一个blocking queue或者singleton class)。被搞多了我也学会了

## 一些题目

1. Binary tree lowest common ancestor with parent pointer. 需要O（1）space
2. Design a parking lot. 需要实现（1）知道第二层停了多少车 （2）知道第二层有多少available残趴

一. 面试官自我介绍，询问我resume的一个项目（10min）

二. 两道算法题

Partition array

1. input: [1, 2, 3, 6, 0, 0, 3, 1, 9, 0]
2. output: [1, 2, 3, 6, 3, 1, 9, 0, 0, 0]

Fibonacci number.

Fibonacci number: 1, 1, 2, 3, 5, 8
n = 0 -> 1
n = 1 -> 1
n = 2 -> 2
F(n+2) = F(n+1) + F(n)

三. 一道OO设计题

Parking Garage

+ multiple floors
+ each floor has multiple parking spots
+ parking spots has two types. handicapped or regular parking.

Question: how many regular parking are available at 2nd floor?

1. You are given the root of the Binary Search Tree and two children nodes, please return the first common ancestor of these two nodes.
2. Mirror a binary tree.
3. implement pow(double a, int b)
4. Find the number of ways to top point in a triangle  
5. Some complex crawler used for the restaurant menu.
6. find the most points on a straight line in a 2D graph  

Applied through the career center website in the university. The first response is within a week. 1) 48-hour coding assignment: use Java to write a web scraper for a certain URL. 2) Technical phone interview: routine algorithm questions. 3) Behavioral phone interview: very common interview questions like why do you choose this company, how to handle conflict in a team. 4) Onsite interview: 2 technical interviews + a 5.5-hour coding… 

First, ask you to describe your most recent project, then talk something about your self... All general behavioral questions. Finally a project, design an app to extract certain keywords to describe a random webpage. For example, an amazon page selling a microwave, the result should be like: microwave GT200(model) 100 dollar.  

作业完成后进入电面的环节。

面试的是一个烙印，英语爆烂，烂到完全听不懂他对公司的介绍。大约听完几分钟的天书后，我们正式进入了技术问题的部分。

第一题：

String permutation，依照之前在cracking coding interview的方法迅速写了一个递归的方法。

不过后来指出这个对于有duplicate不太好。于是我告诉他用hashset存放最后的结果可以免除重复。但是后来他又说有没有其他方法。

于是我依稀记得leetcode上的permutation 2就是讲duplicate怎么处理的，于是用dfs+backtracking的方法重新写了一个可以去除duplicate的版本。同时针对这个算法还争论了一番，最后烙印表示应该是正确的。

第二题：

leetcode和cracking coding interview都有的原题，如何判断一个Binary Tree是不是Binary Search Tree。由于训练有素，很快就完成了。

第三题：

尼玛居然还有第三题，而且还是个design的题目，设计一个parking lot。这是一个非常常见的设计题目，stackoverflow有一个帖子对这个题目描述的非常好，可以参考一下。

BrightEdge：

Round 2：tech电面。一名小印。
第1题：Fibonacci数列。当时还问recursive的复杂度，我想了半天答了O(n)，不过应
该是O(2^n)才对。
第2题：Leetcode原题：如何判断一个BST是否valid。
Round 3：behavioral电面。

LinkedIn：

Round 0：HR打电话瞎聊一通。
Round 1：tech电面1。一名老印和一名小印。
第1题：Leetcode原题：由一个binary tree的inorder及preorder traversal结果，重
构原binary tree。
第2题：Leetcode原题：一个已排序的数组中查找某给定element重复的个数。

Round 2：tech电面2。国人大哥。
第1题：level sum，算是deep iterator的变种。一个多重nested array，例如{a,{b,c
},{{d},e}}，返回level sum = a + 2 * (b + c) + 3 * d + 2 * e。
第2题：First Common Ancestor with parent pointer。What if the parent pointer
is not available?

简单说来三道题目：
1. reverse linkedlist                        CC原题不能更多
2. all characters combinations          leetcode原题，不能更多，就是
combinations的变形
3. design parking lot


第一题我说，俩方法，你要哪个？然后，因为面试官是烙印，真心没有听太清，意思大
概就是，你开始就行了。然后我就开始了。直接用了最简单的iteration的方法做了。
给Node，有next指向。输入是head，reverse即可。
第二题我说，（我真的记得，前两天还专门练了一下下，但是，还是忘了），应该这样
这样，就是不断减少一个字符，排序剩下的，但是，我总以为是DFS，这段时间做DFS做
的有点凶，什么都爱往DFS上套。（PS：求问各位一个问题，你们面试的时候说方法的
时候，就说DFS还是说全名？Depth first searching？） 我反正都有说。然后，然后
，关键的来了，在答案的帮助下，我终于找到了，终于找到了。不过输入是char array
，他说随意，我说，好吧，那就array吧，然后我array，存在了ArrayList<ArrayList<
String>>中，中间好像也没有toString()，反正就这样了。开始真的没有做对，还想的
DFS，然后我俩的交流有了一点点尴尬，我说，给我one more minute， 终于，找到了
答案，思路彻底清晰起来了。（大神们轻拍，**这里只是求第一轮顺利通过。）然后，
解释了半天，小哥应该是听懂了。欢快地pass了。
第三题我直接开的CC讲的，这两天刚刚起步看design，完全没思路，昨天看了一晚上的
21点的设计。经典题目就是parking lot，反正我就刚刚开始看design，也答得很差劲
。各位看官，有懂得，能不能给发个链接或者书籍或者什么博客或者什么主页或者什么
总结？关于design的东西的？CC的design应该还是不错的，亚麻不也是考parking lot
么？好像还有什么购物系统，看到之前的面经上有说的。CTCI的作者也出了一个针对PM
的书籍，这个对design有多少帮助呢？不知道，有看过的留个言啥的呗~~~
然后，设计要求见pdf，主要就是两层，各种size的车，记录时间，确定能否停靠。还
是不难。但是，对于我这个刚看design一天的人，还是稍稍有一点难度的。
