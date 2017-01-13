# BrightEdge

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

2.m\*n的矩阵走格子，只能向下或者向右。返回总路线数量

public int pathSum(int m, int n)

3.判断二叉树是不是BST

4.生成n-bit的gray code (不知道的童鞋请自行google)

一个无难度题 ＋ 仨leetcode原题。四个题加讲一共花了30分钟，然后妹子说她就准备了四个题...问我有什么问题。她后来说这个公司还处在start up阶段，所以非常累要有心理准备。

面过了以后去做著名的coding assignment。和这个帖子说的基本一样http://www.1point3acres.com/bbs/ ... D311%26sortid%3D311只是网站不一样。做的时候是一定要用其他library分析html的，不然会死...然后其写文档也非常重要。我当作一个课程project去写了15页....

结果过了两天又让我面下一轮online coding。这点比较奇怪，因为和我一起的其他童鞋都直接面behavior了，难道是我的assignment做的比较差？我更倾向于认为他们根本忘了我参加过on campus =\_=

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
n = 0 -\> 1
n = 1 -\> 1
n = 2 -\> 2
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