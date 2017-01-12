# Google

## string 返回 word

引号需要另外处理，或者直接遍历一次

input: I have a "faux coat"
output: [I, have, a, faux coat]

---

> 给一个先递增后递减的数组，找到最大值。这数组是非严格递增递减，也就是说有重复。

写了个Binary Search之后面试官问我如果输入是1233321怎么办

> Moving Average. 给的是一个stream,求前K个数的平均值

用个dequeue存K个数就行了

> 给你一个URL让你求这个URL访问到的页面的和。面试官给了一个API，输入URL返回URL所连接到的URL

写个DFS然后调用这个API，再用个Set去重就好了。

> Given a large integer array, count the number of triplets whose sum is less than or equal to an integer T

一开始猛然间以为是3-Sum的题，仔细想想不太一样，细节问题挺多。最后写了一个O(n2lgn)的算法，然后问大叔更简便的有木有，大叔迟疑了片刻说应该有数学相关的取巧办法。。

LeetCode新题3Sum Smaller，先排序，再双指针O(n^2)就可以，参考http://www.cnblogs.com/jcliBlogger/p/4736809.html

> Given an array of Ad (profit, start_time, end_time) and a timespan [0, T], find the max profit of Ads that fit the timespan.

先说了穷举法O(2^n), 然后说了贪心法（不是最优解），最后用DP解决。小哥态度灰常好，给了很有用的提示, 就像自家人啊。

> M x N large board, with only white and black blocks, all black blocks are connected (vertically or horizontally), find the minimum rectangle boundary that contains all black blocks.

还好心地给了提示和假定。感觉交流互动非常好，可惜最后差了一点，没能想出O(n^2)以内的算法。

第三题貌似是遍历玩board 记录 最left，最top，最bottom，最right坐标就可以了吧。。。。 应该是O(n*m).

如果n*m很大，还有一种方法是先指定一个黑点（如果不让指定，可以随机猜），因为黑点都是connected的，所以可以用递归搜索黑点，搜索的同时记录最left，最top，最bottom，最right坐标

就像图像填充里的floor fill，如果黑点的个数是K，复杂度就是O(K)

> Design a algorithm to initialize the board of Candy Crush Saga. With M x N board, Q types of candies. (Rules: no 3 for run after initialization, must contain at least one valid move at the beginning)

小哥说话很和气，先让我介绍了一个project，于是兴致勃勃地讲了做过的一个游戏。他于是拿出手机给我看了这个，说那就出一道游戏题吧

先把Candy简化成数字，类型数组就成了[0, 1, 2, ..., Q-1]。规则一共三条：随机（至少玩家看上去是）；不能一开始就有3个共线的；开局至少有一步能保证有消除（不然没法玩。。）

1. 我首先关注的是前两条规则，因为觉得第三条只是小修改（尽管如果初始化完成后，再修改成符合第三条，可能导致连锁反应）。因为“随机”一直在我心头挥之不去，所以首先想到的是遍历所有格子，每次随机挑一个Q放进去，但立刻意识到这样很有可能导致死锁，尤其Q很小的时候，然后举了个死锁的例子。
2. 因为之前考虑过Q很小，所以最简单就是{0, 1}两种，立刻想到国际象棋棋盘：两色相间一定能填满而且无冲突。然后想到能不能先按照国际象棋棋盘填满，然后在这个基础上进行”随机化“。假如我有个遵循前两条规则的函数random()，对棋盘进行随机化。因为是在01棋盘改，所以第一遍下来可能还是很”假“，但既然这个函数是遵循前两条规则的，那么大可放心的多执行几遍。就像PS的滤镜叠加使用~ 然后开始讨论这个random()函数，大体思路是遍历棋盘，对每个格子有0.5 的概率进行”尝试修改“。(随机化就是一个慢慢tweak的过程，这个参数后面提到要根据实际效果调整）。尝试修改的算法就是：q = random(0, Q); 以q为中心向上下左右四个方向，一共有6条长度为3的线会造成潜在冲突，因此逐个检查一遍，假如无冲突就把当前位置替换为q。最后根据实际效果决定是否再来几次~
3. 然后就剩第三条规则：开局至少有一步能走。我上面阐述的时候就一直有个感觉，每局开始看似随机但一定有定势。然后让小哥打开手机游戏开了两局看了下，果然，每局开头一定会有{V型, _/型} 中的一种或两种排列，保证挪一步就能消除。跟小哥聊了这个想法之后，我的做法就是01棋盘生成后，随机选一个排列，比如V型，然后在棋盘上随机选一个（也可以多个）位置，把这个位置画出的V全部mark成不可修改。然后在这个基础上跑上面提到的random()算法。第三条规则也可以有很多随机性，必须类型选择，类型对应位置、个数的选择。

> 给一个整数n，返回前n个fibonacci number相邻pair的最后一个digit。听起来有点绕，其实不难，比如：

    n = 8
    fibonacci: [0, 1, 1, 2, 3, 5, 8, 13]
    return: [ (0, 1), (1, 1), (1, 2), (2, 3), (3, 5), (5, 8), (8, 3) ]

很简单，先生成前n个number到list，然后第二遍loop返回pair。

follow up：怎样确定有没有cycle？如果n很大怎么办？

维护一个visited set，每次检查一下。

很多solution: 可以用long， 用string， 或者cache，或者distributed system。

然后问最多需要查多少次就可以确定cycle的存在？

这个自己脑抽了，理解了好久才明白过来，就是计算有多少个可能的pair，10 * 10。

> 给一颗二叉树，返回重复的subtree。比如：

                      1
                    /   \
                  2      3
                 /     /   \
               4      2     4
                     /
                    4
                    
结果应该返回[ ( 2 -> 4), (4) ] 两颗树。

也很简单，BFS遍历，存每个substree到list里，然后用双重循坏找。其中需要写一个helper function判断两棵树是否相同。

> 设计一个fraction number 的class，要求实现equals和String toDecimal()

toDecimal是leetcode原题，equals的话注意先得到gcd，然后除了之后再比较。还有分子分母是否为0，符号不一样等等都需要考虑。细节挺多的。

> 给一个二维boolean array， true代表greyed， 要找出所有可能的正方形

    0 1 0
    0 0 0
    1 0 0

一共有8个正方形（边长为1的7个，为2的1个，为3的0个）。注意matrix的边长可能不等。

用DP对matrix先预处理，方法有点类似之前地里面经出现的计算matrix中rectangle面积的题，dp[j]代表从(0, 0) 到 （i, j) 里面所有可用的grid的数量。具体方法大家可以自己思索一下。\

> Given a list of boarding passes, each boarding pass contains two cities, say A-B, generate travel itinerary.  

Typical topology sort

> moving range average. Given an input array，always output the average of k item, known as window size.

use a counter and cur variable to keep track of current information.

> Given a sorted input array, write an O(lgN) algorithm to find if there is a number has appears more than 1/4 times

Binary search. Say value of current mid is k, search first appearance index of k on left and last index of mid element on right. The number of times k appears is rightIndex-leftIndex+1.


> 给int n，求n所有factors，然后问问算法的running time

开方之后遍历一波

> 上的follow up，给distinct primes list，回传所有由这些primes组成的数字。再follow up，那给的primes有重复呢？

要好好想一想

> 给个字典，要求找出一对单词。所有字符都不同。然后长度乘积最大

    cat 
    dog 
    feed 
    pull 
    space

+ cat and dog share no letters, and have a product of 3*3 = 9 
+ space and dog share no letters, and have a product of 15 
+ space does not work with either feed (e) or pull (p) 
+ feed and pull is the best answer for this dictionary (4*4 = 16) 

The dictionary will only contain lower case letters (a-z) 
=> return the numeric value of word length product, e.g. 16 for the example above

> 给一个list，长度未知，里面全是质数，然后给一个k，要求输出前k个正整数，这k个数都能被list里的质数因式分解

lz一看到这个题目就闻到了一股递归的气息，然后用大概10分钟blablabla讲怎么用stack存每次分解后的子结果。。谈笑风生了一会儿发现面试官没声音了。。之后他说不如你先写个brute－force，我去研究一下你说的算法。。

> 实现这么一个函数 void longestSubstr(string s, int m). 在s中，找到最长的字串， 使其恰好含有m个distinct char.

比如：

+ 输入 aabbccedf, 3 返回 aabbcc（含有a b c三个不同的char）
+ 输入 abcdbcedf，3 返回 bcdbc （含有b c d 三个）

> 给一个字符串s由单词组成， 比如“i have a dream”。 要求把这个字符串添到一个m x n的网格里，同一个单词不能被cut off，每一句之间空格相连。问最多添满多少个整句。

follow up （m and n are much larger than the length of s, 怎么办）

> 有一个2维数组A。实现两个函数：1) void update(int x, int y, int v), 就是更新A[x][y]的值(v).  2) int regionalSum(int x1, int y1, int x2, int y2)：就是求（x1, y1）和（x2, y2）构成矩形的所有元素和。

系统很少用带update而经常使用reginalSum, 如何设计减少复杂度。

> 给一个二维矩阵，
实现两个方法，set(int x, int y), sum(int x, int y, int val)
set 方法设一个点的值， sum得到这一点到左上角（0， 0）点左右值的和。

（1）set多，sum少
（2）set少，sum多

第二种情况主要是要在set时就把sum算好，sum就是constent time了，但是set要注意更新。

> LeetCode原题，search in 2D matrix

leetcode

> oil pipeline

其实就是在一个坐标轴上若干个点找距离各点之和最近的一个点，先sort这一组点，再找它们的median，median就是要找的这个点。如果点的数量是双数，那么求的这个点就可以取中间两点之间任意一个点。

> Given a string S, return minimum number of chars that you can add to its back to obtain a palindrome. Explain the complexity

TODO

> Write a function to return expected number of tosses of an unbiased or biased coin until there are m (>= 1) heads in a row,supposing the head probability in a toss is p: 0 < p <= 1. If the result is not integer, round it.

TODO

> 把数组奇偶数字排序 基数在左边 偶数在右边

TODO

> 两个字符串 找到里面所有不同的单词

TODO

> 略有难度，不过地里出现过几次了。 滑雪问题变种。 dp＋ dfs 搞定

TODO

> word abbreviation, 版上之前也有人发过. 一个string只保留首尾字母, 中间字母数用数字表示, 比如 "abcde" = "a3e", "ab" = "ab", "abc" = "a1c" . 给一组string, 输出相同abbreviation的所有string, 但重复的string不算.

直接用的hashmap, 存储string的时候脑子没转过来,用的array,面试官问是不是有更好的,果断换hashset.
coding完时间剩的不多了,面试官说看code没多大问题,不用测试了... 唉,写代码的速度太慢了啊.

> 给一大堆有start time, end time和ID的events，返回存在conflicts的events。

用的类似merge intervals的方法做。要注意如果俩events有conflict，俩events都要加到result里，注意别加重复了

> 给一个都是integer的matrix，找最长上升path的长度

DP做。

> 数字只有 0， 1 ， 2 三个值， 设计一个存储结构，实现数组操作， 高效的利用内存

解法 用 2bits 存储一个，这样一个32bits 的 int 可以存储16个字， 实现 get(int index) 和 set(int index , int val)

> 说有一个视频文件和许多音频文件。 有好多数组，每个数组的值是时间轴上点。求sync point

可以理解为数组里的值是一段段的视频或音频文件，其长度为数组值的段。 第一个数组 [1,5,8,9] 第二个数组[1,4,9,9] 这样对于第一数组,所有时间轴上新的起点为[1,6,14,23] 同理第二个数组[1,5,14,23] 所以所有的sync point为a[1,14,23]

> 一个数 可以表示成 n =  x*x*x + y*y*y  = z*z*z + d*d*d， 一个数可以表示成 2个数的立方和， 至少有两对这样的数。

给定一个n， 求所有小于等于这个n  满足条件的数。 

> 设计短网址服务

tinyurl 高频

> 给一个图 让求图中所有的 正方形

怎么存图，数据结构自己说的算。 自己想了半天，没说出面试官想要的。最后面试官给了提示。
    
    class point{
      double x;
      double y;
      point west;
      point east;
      point north;
      point south;
    }

> 面试官想演示贪吃蛇的游戏，之后让你想出几个类，来实现这个游戏。 还有简单说下算法。之后实现其中的一个。 让我实现吃豆的逻辑

TODO

> 平方根。给了精度就是希望有多少位小数

用的二分法

> best time to sell stock 2

leetcode

> 在上一题的基础上加了个限制，就是如果今天卖出股票，则第二天不能进行买进操作，需要隔一天，而就是说第三天才能

举例： 1，2，3，4，2，3，4； 则利润为4， 因为第一天买，第4天卖，第5天不能买，所以第六天买第7天卖。

```
  public static int maxProfit(int[] prices){ 
          if(prices == null || prices.length == 0){
                    return 0;
      }

    //整个交易过程中，我们有两种状态，一种是手头只有钱没股票，一种是手头有股票没钱
    //而最后获得最大利润的状态肯定是手头只有钱，所有股票都被抛售的状态.w
        int[] bear = new int[prices.length];
        //bear position 就是空仓，表示在这个位置我们手头没有股票
        int[] bull = new int[prices.length];
        //bull position 就是满仓，表示在这个位置我们手头已经买了股票，在等待机会抛售 
        
        bear[0] = 0;
        //初始情况，因为手头没股票，所以盈利是0
        bull[0] = 0-prices[0];
        //初始情况，我们钱买了股票，所以是 0-prices[0]
        for(int i =  1;i<prices.length;i++){
                bear[i] = Math.max(bear[i-1],bull[i-1]+prices[i]);
                //空仓的最大利润的递归式是：bear[i] = max(bear[i-1],bull[i-1]+prices[i]);
                //意思就是当前最大利润应该为前一天空仓的利润（既我们这一天不做任何买卖）和前一天满仓和今天卖出 两者中的最大值
                if(i == 1){
                        //而对于满仓的话，递归式应该为 bull[i] = max(bull[i-1],bear[i-2]-prices[i])
                        //意思即是 满仓的最大值应该是 前一天满仓，和两天之前空仓今天买入 中的最大值
                        //因为题目限定了要隔一天才能买
                        //对于第一天要单独考虑，因为之前没有买过股票
                        bull[i] = Math.max(bull[0],0-prices[1]);
                }else{
                        bull[i] = Math.max(bull[i-1],bear[i-2]-prices[i]);
                }
        }
        return bear[prices.length-1];. from: 1point3acres.com/bbs 
}
```

> Find the popular number in the array. Popular means it appeas > 1/4 size of the array。

Leetcode

遍历一次，保存一个长度为3的数组：

1. 如果数组中包括这个数，则概数count + 1
2. 如果数组中有空位，则放入概数，count置为1
3. 如果数组中有数字count为0，则替换概数，count置为1 
4. 所有数字count减1

最后数组中剩下的数，就是candidate，每个统计一下就可以了

这个方法可以解决任意1/n的majority number

> 滑雪

问一个二维数组表示的n*n的矩阵，找出一条连续的最长的路径的长度。
比如

    7 8 6
    9 4 5
    2 3 1
    最长是2,3,4,5,6，返回长度5.

poj 1088 滑雪 经典题啊

> Merge Two sorted LinkedList.

leetcode

> Sort  a Linked List.

我提出用Merge Sort， 先举了个例子 过了一遍思路， 然后开始写代码。

最开始面试官给我把函数名给写出来了， 把我思路打断了， 卡了一下。

后来自己重新写了一个函数名，写完了。

> Longest substring without repeating letters. 

leetcode

>  Longest consecutive numbers in a binary tree.

```
关于第二题，大致意思是这样，让在binary tree里挑出最长的连续（必须后面数=前面数+1）递增数列，数列顺序只能从parent到child，不可以反着来。比如：

                 1
                    \
                      3
                    /    \
                  2      4
                           \
                             5
则返回[3, 4, 5]


再比如：
                 2
                    \
                      3
                    /    \
                  1      4
                 /          \
               2             5
              /
             3
            /
           4

则返回[1, 2, 3, 4]
```

```
int ans = 0;
void dfs(TreeNode* cur, int pre, int len) {
    if (cur == nullptr) {
        return;
    }
    int value = cur->value;
    if (value == pre + 1) {
        len++;
    } else {
        len = 1;
    }
    ans = max(ans, len);
    dfs(cur->left, value, len);
    dfs(cur->right, value, len);
}

dfs(root, -INF, 0);


迭代
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestConsecutiveNumsinBT(self, root):
        if not root: return []
        stack = [(root, [root.val])]
        res = []
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                res.append(path)  
                continue. visit 1point3acres.com for more.
            if node.left:
                if node.left.val == node.val + 1:
                    stack.append((node.left, path + [node.left.val]))
                else:
                    stack.append((node.left, [node.left.val]))
            if node.right:. From 1point 3acres bbs
                if node.right.val == node.val + 1:
                    stack.append((node.right, path + [node.right.val]))
                else:. from: 1point3acres.com/bbs 
                    stack.append((node.right, [node.right.val]))
 
        longest = res[0]
        for i in range(1, len(res)):
            if len(res[i]) > len(longest):
                longest = res[i]-google 1point3acres
        return longest

```


> good number问题。 一个数如果能用（至少两组）两个立方数相加得到那么就是good number。print 小于等于n的所有good number。分析时间复杂度。

我先把小于n的所有立方数存起来。然后就变成了2 sum问题了

> Implement HashTable with get,set,delete,getRandom functions in O(1)

这题之前地里有人po过面经，楼主很幸运地当时认真实现过。。

重点在于2个hashmap+arraylist

> Given a source word, tart word and an English dictionary, transform the source word to target by changing/adding/removing 1 character at a time, while all intermediate words being valid English words.

类似Word ladder II

问了时间复杂度

