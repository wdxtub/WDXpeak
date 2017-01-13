# Amazon

+ 面试的时候，人家给你两个选择，一定要选一个，分析清楚各种优劣即可
+ 设计题的时候，一定要考虑 scale 的问题，并且要着重在这上面表现，多说一点，考虑各种情况。

amazon的leadership principles熟读!http://www.amazon.com/Values-Careers- Homepage/b?node=239365011

## 算法题目

### leetcode: letter combination

输出 valid word

### 无向图距离

graph从一个source,然后输出指定的距离的node,无向图。我写的bfs level,中间 卡了一下,想了半天才写出来level 怎么做。

### 数组排序

两个数组,一个大,一个小。都是排好序的。然后大数组后面有几个空位置和小数组 长度相等,排好序的数组应该都在大数组上面。不要用额外的space

### 单词权数

给你一个字典一个,map<Character, Integer>存每个字母的权,输入是一个List<Character>(可能有重复)让你求这些字母求可以组成最大权数的 word list(List<String>). 

### leetcode: Largest K element

经典题目

### leetcode 题目

一个 无序数组,判断它是否是连续序列,其中0是magic number。也是leetcode原题。

### @@@ 合并数组

将已经有序的N个ArrayList merge 为一个有序的List,LC原题,做完后因
为其中用到了Heap,让顺便实现了一下Heap的插入,中间卡壳了一下,想到Heap可以用数组表示后,才顺利解决。

首先讲了一下bruce force的方法,然后问了时间复杂度和空间复杂度。并且怎么推导出来的 都有问哦;

然后提到了用min heap, 然后写了除了constructor以外,所有min heap的构建方法。最后 问了问heap的内部机制

### 均匀分开数组

给两个列表,每个列表装着一样的元素,合并两个列表,并要求短的列表的元素把长列表元 素尽可能均衡分开。比如列表为AAAAA和BBBBBB,返回BABABABABAB;又比如 AAAAAA和BBBB,返回AABABABABA。

### 字母统计并查找

给一列城市的名字,并且告诉你你的家是哪个城市,并且每个城市的受欢迎指数是城市名字 里的辅音字母数除以元音字母数,比如Shanghai的指数就是5/3=1.66666,要返回和家乡 城市的指数最近的其它城市,没有的话返回NOT_FOUND。 题目都很简单,不需要复杂算法,就是在写之前想好edge cases,有很多刁钻的测试用例 需要注意,好好想清楚应该所有测试都能过。

### csv 文件处理

给你一个.csv文件,每个entry有employer name, employer ssn, manager name, manager ssn, employer title几个属性,给一个FileIterator来读取每条entry,给一个 Person class,里面有String name, String ssn, String title和List<Person> reports(向
        
这个人汇报的所有人),要求用某种数据结构存这些个entry,然后在里面找谁是CEO。

### 返回数组重复元素

给一个Integer Array,返回一个 duplicate,加上各种follow up,比如ArrayList的contains怎么实现的,换成什么其他数据 结构比较好,hash function怎么实现,hash collision怎么解决,不用extra space怎么 办,Array里面有一百万个元素怎么改,返回所有的duplicates怎么写等等。

### 区间最小数字

给一个数组【1 3 -3 -2 0 53 3 1】,求startindex = 2到 endindex= 5的最小数。我说遍历,他说数组很大太慢了,我说用hashMap去存,他说存 储空间太大了,我说用二叉树去存,然后他给我画了一个区间二叉树,要求写代码。话说真 的好几个月没怎么写代码,完全不会了,我随便recursion一下,他发现bug,我改正,最 后就是说你half way done,就走了。

### BST 组新树

给我一个BST,要求得到一颗新树,每个节点的内容是比此节点的元素值大
      
的元素的总和。我一看不会,赶紧想,就说用stack去做,然后他说为什么不对每个点分别 求,还给我一个函数原型,我说不要,这样重复计算,我用stack可以n做出来,他说那你 写,我写啊写,写好了,他说不明白,给解释了很久,最后他终于明白了,简直要哭。这里 我明白一个道理,你要是解法和面试官不一样,他们很多时候就懵了,也不好意思说看不 懂,然后很长时间就在怀疑你。不过,面试后遇到cmu女神,她说这题见过,递归就行了, 我听着就泪奔了,还是要多训练,差距太大。.

### 子树

判断两颗 BT,其中一个是不是另外一个的子树

是检查tree2是不是tree1的子树,不用考虑时间,直接bfs遍历,然后 dfs检查就行了。

### 合并区间

merge interve

### 翻转字符串

leetcode

### @ 找出一个rotate过的sorted array里的最小值

leetcode

### 二维数组最长单词

给定一个词典和矩阵,矩阵中每个元素都是一个字母,从矩阵中的任何一个元 素出发,通过上下左右移动,移动的路径都可以构成一个单词,要求找出矩阵当中存在的且在词典当中的单词中最长的一个。 

我没有多想就直接用了一个矩阵遍历+DFS的基本方法,code了之后也没有要求优化啥的。

在二维矩阵中找出所有valid的单词,你可以往八个方向匹配下一个 字符,字典我用了前缀树结构,然后遍历二维矩阵DFS,要注意避免同一个cell的重复使 用。

### 选数字

问题是这样的, 两个人玩游戏,给一个数组,俩人轮流选里面的数字, 看到最后谁的数字 之和最大。

### n 个数的乘积

算法题,input 是 a[n], output 是从a[n]里面任选3个数的 最大乘积。
Follow up 比较难,不是3个数,改成了x个数。

### @ 数字转字符串

数字转英文单词。e.g 999 -> nine hundred and nighty nine.

### 拓扑排序

先修课选课顺序的题

### 单词距离

从string(一段句子)里面找出所有重复并且相距d的单词。

直接hashmap解决,然后问能不能改进啥的,接着优化。

### @@@ LRU Cache

扩展到集群,用Hash映射解决数据分布。

### @@ 实现 heap

基础算法

求n个点中离原点最近的k个点。先说思路,我说用堆。然后他就让我写了一个heap类,支 持push,pop,top等操作,然后用我自己实现的heap类来完成之前的题目。

### @@ 打印树

按行从左往右打印一棵树,写代码。follow up 是zigzag打印树,在之前代码基础上修改。 最后是写代码打印树的最外一圈。. visit 

### xml 文件读取算法

类似于 json 解析

### 缺一个整数

leetcode 原题n size 数组存储0 - n 缺一个整数 找出来, 画图油漆桶算法

### First N Prime Numbers

暴力

### Map-Reduce 的 Reducer方法

暴力

### 城市到达

给你一个API,input是一个城市,输出是邻近城市,问实现一个方法,判断 两个城市之间是否可以到达

BFS

### 城市路径

继续上问,实现一个方法,找出两个城市之间所有的路径。答:DFS

### 用户特殊请求

继续上问,如果client有很多特殊请求(如不想经过城市A,不想途转太多城
市)怎么办?答:Strategy Design Pattern

### @@ isValidBST()

leetcode

validate BST using three different methods, array vs linked list, how to implement hashtable

### 数组单词

给你一个dictionary(all English word)和一个一维的character数组 (duplicated),找出所有可以用数组表示的字典里的单词

答:遍历字 典,判断是否能被表示

### @@@ 偶数/奇数次元素

给一个array 找出里面出现奇数次的数字。我先用hashmap, 后来用int[],最后小哥说 no extra space

一个数出现odd times 其他even times 找这个数 实现2种方法

follow up

integer换成ojbect,所以不能用异或。

可不可以不用extra memory

### 复制链表

linkedlist 每个节点多一个random pointer,问怎么复制,hashmap,很简单, 没让写代码。

### 求平方根

给一个平方数,求平方根。就/2 /2 /2。。。 log(n)的复杂度

### 循环链表删除

循环列表,删除指定节点,写完让想一些edge case 测试一下代码正确性

### 递归复制数组元素

给你一个array,不用循环把所有元素复制到另一个array里,用recursive

### 找中位数

无限输入流找中位数,follow up,如果memory非常小怎么办

### @@ 有序数组的 two sum

先讲了用hashmap, 然后用binary search。follow up问了一下如果有duplicate 怎么办

2sum要求输出所有可能的pair,而且原数组可能有duplicate

标准leetcode的two sum。我分别写了O(n2), O(logn)和O(n)(哈希表)三种方法的代 码,每种方法其实就5-8行代码就搞定,不费什么时间。然后面试官说,让我给代码加注 释,然后写单元测试。。

### 3 sum

leetcode

### word ladder

介于1和2中间吧,只需要输出最短的一条路径就可以

### @@@@ 矩阵 island

给一个矩阵,连通的非0元素组成一个island,问这个矩阵里island的数量. 

### min/max stack

先问了stack的pop, push, peek的时间复杂度。写了stack类的pop, push 和 peek方法。然 后让在自己设计的stack类的基础上实现min stack

### 分配 job

一个set里面装的是很多job, 每个job有开始的时间和结束的时间。现在需要分配这一堆job给 尽可能少的machine, 要求是每一个machine在同一个时间段只能做一个job,问怎么让 machine数量最少。

我用了bruth force的方法,in worst case, time complexity is O(n ^ 2), 当讨论怎么降到 O(n)的时候,没时间了

### @ 数组转 range

把一串连续的整数表示为一个range, range包含begin和end.比如3,4,5,6就表示为 begin=3,end=6的range

一个排好序的整数数组,返回所有的range. 比如1,2,3,5,7,8,10返回[1,3],[5,5],[7,8],[10,10] follow up是用迭代器实现。。。

### trie tree

给一个prefix字符串,找出字典中所有包含这个prefix的词

先问用什么数据结构表示这个字典,我说用trie

然后用dfs实现找词。面试官问bfs和dfs区别。

然后要求实现往trie里添加词的方法。

最后面试官提出apple和apples在我的代码里没法区分出来,经提醒我在trieNode中加一个 mark表示一个词的终止。然后重新修改了部分代码。

### @ 罗马数字转 Integer

口述Integer转罗马数字。我提出要把IX, IV这种也算一种特殊的罗马数字单位。

于是面试官出题: 给一个整数,返回这个整数对应的罗马数字中最大的单位代表的整数,比如8表示为罗马数字为VIII,最大单位为V,即5。 我用一次遍历实现的,面试官问怎么优化,我说可以二分搜索,复杂度降到O(logn)

### @@ compress string

input: aabccc output: 2ab3c 然后讨论可以不可以再优化

如果要 in place 怎么做

### valid parentheses

leetcode, Valid Parentheses, 然后follow up 到如果有很多对open, close的character怎么办

### reverse string

让我说出所有想到的方法 然后讨论复杂度 然后挑了其中一种写code

### @@@ find lowest common ancester

最开始假设有parent, 然后没有parent的话怎么做,我说了一个top down approach,然后他说要优化,然后我说 了botom up,最后实现bottom up的代码。期间每种都要比较复杂度。

说如果这两个 Node不一定在这个tree里怎么办。

### 最长 leaf nodes 包含的 nodes 个数

binary tree找到距离最长的两个leaf nodes包含的nodes个数。

### 从 log 文件提取电话号码

从 log 文件提取电话号码

### 矩形重叠

一个window里有两个矩形,怎么判断它们有没有overlap

### decoding leetcode

给了一个dict,比如a->1,b->2...z->26, 那么“ab"->12; 现在给你一个数字,让你decoding。

### 存数据

有很多整数,和n台电脑,怎么把这些 整数分别存到不同的电脑上,第一台电脑上存得数要比第二台小,依次类推。

### 表达式求值

给了一个表达式让求值,比如7-10/5, 我说先转换成逆波兰式,然后用逆波 兰式求值。 他让我写逆波兰式求值部分的代码。

### substring 判断

给定一个string。比如说是“hello”。 判断输入的string是不是他的substring。输入 “ell” 返回true,输入“eo”返回false。(我面完这题觉得很简单,但后来同学告诉我, 这题要用kmp算法做)

写完之后,问如果“oh”和“ohel”这种也算是原string的substring,应该怎么办。(把两个元数组相加,其他代码不变)

### @ 地图搜索

输入是一个城市的地图的大小(m,n),和一个list,里面包含所有有locker的地理位置。 输出一个m*n的二位数组,每个单元的值为到最近locker的距离。问时间复杂度(这题要从 每个locker同时开始bfs)

### 二维数组搜索

给一个二维数组,都是整数,每行都是从小到大排列,每列也是从小到大。(但是第二行的 第一个不一定大于第一行最后一个),给一个target,判断是否存在于这个矩阵中。 先用mlgn,再用lgn做。(lgn的方法就是对整个二维数组做binary search,然后每次可以 把问题缩减为原来的3/4)

### 括号检验

一个string里面有括号,怎么判断这些括号是合法的,拓展: 如果还有中括号,大 括号呢

### @@ 比节点大的最小节点

给一个binary search tree里面的一个节点,找到比这个节点大的最小节点

### 存水问题

给一个int的array,值代表高度。求这个东西能储存多少水。

### 日期间隔

输入两个时期,有天,月,年,计算出这两个日期差多少天

### 迷宫出路

一个迷宫, 指定起始点和终点,找任意一条路线即可。自己设计数据结构存路线和迷宫。

### 回文串

是否是回文串

一定要递归，如何写

以及最长回文子串

### pow

pow(int, int)

### @ 两个栈实现队列

两个栈实现一个队列

### 排序基本

heapsort quicksort怎么做 给你数据模拟一下流程

### unique ip

给你一个file 里头是IP地址 然后统计多少个unique的

### string 统计

统计一个string里头各字母出现了多少 排序输出字母和对应次数

### 最大连续数组和

给定一个数组 求连续k个数之和的最大值 以及从哪个index开始

### 打僵尸

就是一圈zombies,给你一 个starting point,然后每隔k步你shoot一个zombie,完后依次下去直到剩下一个 zombie,让你输出最后剩下的zombie。我用linkedlist做的,然后while loop每次shoot一个zombie,num-1删除那个listnode,直到最后num变成1跳出循环。

### 数组中元素出现次数

给你一个sorted array,完后输入一个数,让你output它在array里面出现的次数。这道题比 较tricky的地方是,corner case的考虑。每个人都能想到binary search, 但是在处理 binary search的时候有些corner case要处理好。

### reverse string

只能用recursive的方法reverse一个string,比如“I am a cat” -> "cat a am I". 

### 去掉重复元素

有两个array,a和b,输出一个新的array,只包含a里的元素,但是不包含b里的 元素,两个array都可能有duplicate。

### 找 host

社交网络,一个房间里有很多人,有一个host,所有人都认识host,但是host不认识任何人。你走进房间,你可以问任何一个人,你是否认识他 isKnow(A,B)
得到的回答是true 或者false 

怎么样最快找出来谁是host

### 数独判断

给出了所有数字，判断即可，如何优化

### anagram

leetcode 原题

find all anagrams in a string. `"abc cba aaa bbb bac !** *!* " return: {{abc, cba, bac}, {!**, *!*}}`

### 身高

给一个数组,代表一组人的身高。然后输出一个数组,表示在当前人之后的所有 比他高的人里,离他最近的人的身高。比如输入是[3, 6, 7, 2, 3] 输出就是[6, 7, null, 3, null]。 我给出了俩解,都是O(n2)的。她希望得到一个O(n)的解

### @ 买卖股票

leetcode 原题

### matrix search

题目是2d matrix,从给定的一个坐标出发,往四个方向search,搜到2返回true,搜到1能走,搜到0不能走

### coin

代码题,给你一个金额,几种面额,问你几种组合方式

### 数字与 index 相等

找到integer array里,数字和index相等的数。

### 上一个/下一个节点

问BST,然后让写个查找函数,再就是给一个target,然后找前一个节点和后 一个节点

### 迷宫路径

find maze path (bar rasier)...

### 找最小连续空间

sample: {1,1,1,0,0,0,0,1,0,0,1,1},1代表内存被使用, 0代表空 闲,然后找出至少为2的最小连续空间的index,此例应该返回8

### binary tree serialization

lintcode

### 翻转二叉树

经典题目。。

---

## 设计题目

### 设计一个 zoo

问清楚

### Opentable

opentable, design. 完全自己设计数据结构 和 接口需求, 用户输入 restaurant, timeslot, 人数, 返回是否可以预订

一个restaurant 可能有多个桌子, 每个桌子可能可以坐多个人 如果预订的时候,人数大于一个桌子, 可以把相邻的桌子 combine timeslot 30分钟算一个, 一天就可以算24*2个, 编号从0到47, 用户的输入只能有一个 timeslot

### 三角形棋盘

只有一个空,像跳棋那么走,走过空就可以把中间那抽掉,然后OOD设计。然后follow就是如果不同棋盘怎 么设计


### traffic management system

大 概就是一个十字路口,有好几个方向的汽车,红绿灯,行人,设计这个的controller吧,然 后边讨论思路边写controller的method什么的,最后讨论讨论怎么initialization

问题是很模糊的问题,让我设计一个交 通路口,目的是统计车流,反馈给我们的用户。一听我就知道是故意很模糊的,所以我就加 紧clarify,比如问每个时段和日期车流不同,如何区别;这个application是给谁用的;交 通路口可以分N车道,如何规范;等等一系列

### 图书推荐系统

你有朋友A,朋友A有他的朋友B, 你要看到所有A,B,B的朋友的推荐书单。要代码实现

### OO DESIGN一个“UBER”

问清楚

### 文件系统

主要focus文件权限的设计

### poker game

OOD design a poker game and different methods in each class.1

### 电梯设计

经典设计题

设计电梯箱,按键面板等对象和它们之间的关系,没有深入调度
算法细节。

### 解析表达式

解析表达 式,例如“1*2 + 3”,关键要用面向对象的思想设计。需要可以拓展,支持括号,支持开 方之类的。这题感觉自己没思路,瞎答了一通

### @@@ Parking Lot

传统题目

一开始从OOD的角度来设计。后来面试官说我应该think bigger,才意识到应该是从一个 通用系统架构的角度来回答这个问题。于是就开始扯后台系统架构,想到经典的三层系统机 构从来不会答偏题于是就开始往上搬了。第一层接入层,第二层逻辑层,第三层存储层。接 入层收到用户请求根据协议和请求类型转发给合适的逻辑层。逻辑层包括多个不同服务,各 干各的事,完成库存啊计费啊汇率转换啊等等操作。存储层当然就是数据库,mysql和 nosql大家都懂的,上来把基本表建好,就直接用吧,有需要就扯缓存。比如我就扯了用 redis当缓存,缓存当然有各种不同粒度,各自命中率肯定不一样等等。问我如何扩展方 面,我的回答就是各层内部放入是随便加服务的,只要服务起来了之后到Zookeeper去注 册让其他层的服务调用的时候能找到就好了,存储层扩展有很多Proxy可以用,比如我厂就 有一个叫Atlas的开源项目,是一个很出色的Mysql Proxy,大家可以去Git看看。然后大家 可以根据需要扯一些优化点,找不到也无所谓。

### 设计一个机场调度系统

和面试官多 交流有哪些实体需要抽象吧,要想清楚业务流程里的参与者和用例,还有之后的耦合内聚怎么优化等等。

### 查询机制

给一个数组和一个范围,要返回范围里的最小值,然后扩 展到如何缓存这个查询。一开始搞我以为是算法题,DP?排序?扯了半天,后来发现原来 是OOD,囧。。。关键是如何解耦缓存查询和实时查询这俩类,然后扯了扯工厂模式,依 赖注入等等。

### 设计电话本

http://www.cs.gordon.edu/courses/cs211/AddressBookExample/

### 生物分类

设计数据结构表示生物学门纲目科属种

### OOD (Tic-tac Game) Followups

CC150

### HashTable出现很多collision怎么办

(Rehashing)load factor

### truck tracking system

要求实现查询truck的地点,每天的行程之类 的。一开始写了一个truck class,然后在引导下一点一点的增加功能

### 火箭打彗星

火箭每次发射之后需要五分钟准备时间,雷达会监控彗星出现的距离,每 个火箭只能打最近的一个彗星,问用什么data structure 记录彗星的情况,要求时间复杂度 O(1)的

### 图书推荐系统

类似facebook, twitter那样的好友系统,可以看评价,可以写评价,有好友
列表一类的。

### 顺序 hashmap

重写一个HashMap,多加一个功能,可以按照insert的顺序输出出来

### 设计一个邮件系统

新题目

### Java 基础

概念问了 reflection(我不 清楚。。),garbage collector具体是怎么工作的以及几种GC的区别(我也不会), abstract class跟 interface区别(就知道这个。。) 然后让实现一个interface 实现两个功 能: 一个是能够check input的单词拼写有没有错误 二是可以给你alternative words。这 个我答的不太好。我开始说用trie,他说用一般的,就用hashSet

### deck of cards

给一个deck of cards, 实现两个methods,一个是 deal,这个method可以发一张random的card。 另一个method是shuffle,就是类似 reset deck。

## 家具质量测试

OO design:要给一个家具工厂的所有家具做质量测试(压力测试,是否易燃等等)

---

> Round Robin，求average waiting time，就是 http://www.1point3acres.com/bbs/thread-142143-1-1.html 这个帖子里说的这个题，友情提示楼里有代码~

TODO

> 0，1的list，每天更新，每个单元的新值看前一天的左右邻居，一样就是1，不一样就是0，求n天以后的list。

TODO

> Shortest Job First

地里很多人贴过面经了

