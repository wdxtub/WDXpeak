# Liveramp 面经

<!-- MarkdownTOC -->

- 简介
- OA
    - Subsequence
    - 城市
    - 作文
- 电面
    - LRU cache
    - 像Leetcode上的Word Search
    - 六度空间
    - 四张牌
    - kth smallest element
    - quickselect
    - CSV
    - Find unique browsers in log file.
    - 投篮选择题
    - 大数据
    - 零散
    - onsite

<!-- /MarkdownTOC -->

## 简介

有关LiveRamp，在网上查了一下，LiveRamp主要是做Data onboarding(有时候也叫data onramping，可能LiveRamp就是这么来的吧)的，onboarding在wiki的意思就是让新员工获取新的知识和技能从而可以更加有效地完成特定的工作。而Data onboarding就是一个offline到online的数据处理的过程，把offline收集到数据与online中的数据connect起来。这其中的一个应用就是广告，假设一个卖衣服的商店有自己的客户会员卡，每次客户买东西都会记录下来（所谓custom data management）从而得知用户的偏好，然后data onboarding利用这些数据做一些data matching，machine learning的工作这样根据匹配的结果在各个digital的平台向不同的用户推销不同的产品。LiveRamp甚至会用到cookie。

## OA

### Subsequence

一个sequence，里面都是整数，求最长的subsequence的长度，使得这个subsquence的最大值和最小值相差不超过1. 比如[1,3,2,2,5,2,3,7]最长的subsequence是[3,2,2,2,3],所以应该返回5.

**题解**

subsequence可以是不连续的，这样的话只需要用一个hashtable统计一下各个整数的个数，所以最长的长度应该就是count[k]+count[k+1]的最大值，k是这个sequence里的某一个数，count[k]是它出现的次数。另外一个思路就是排序，这样空间复杂度小点，但是时间复杂度要高一些。

    public int maxSubsequence(int[] a){
        Arrays.sort(a);
        int last = 1;
        int current = 1;
        int max_len = 0;

        for (int i = 1; i < a.length; ++i){
            if (a[i] == a[i-1]){
                last++;
            }
            else{
                break;
            }
        }

        for(int i = last + 1 ; i < a.length ; ++i){
            if(a[i] == a[i-1]){
                current++;
            }
            else{
                if (max_len < last + current)
                    max_len = last + current;
                last = current;
                current = 1;
            }
        }

        return max_len;
    }

hashtable

    def max_subsequence(a):
        count={}
        for num in a:
            count[num]=count.get(num,0)+1
        max_len=0
        for num in count:
            max_len = max(max_len,count[num]+count.get(num+1,0))
        return max_len

### 城市

一个图，节点表示城市，有M个节点和M-1条边，所以是没有环的，用一个array表示这个图，比如T[x]=y的话那么节点x就和y相连，如果T[x]=x就说明x是首都。现在要分别求出到首都距离为1，2，3...M-1的节点数。hashmap结合arraylist搞定。

**题解**

用一个hashmap重新建了一个图，这样方便查找所有相邻的节点，而不用每次查找整个array。然后用bfs来求每个距离上的节点数。

    class Solution:

        def count_dist(self,T):
            distance=[-1]*len(T)
            count=[0]*(len(T)-1)
            for i in range(len(T)):
                if distance[i]<0:
                    self.get_dist(T,distance,i)
            for i in range(len(T)):
                if distance[i]>0:
                    count[distance[i]-1]+=1
            return count

        def get_dist(self,T,distance,i):
            next=T[i]
            if next==i:
                distance[i]=0
                return 0
            elif distance[next]>0:
                distance[i]=distance[next]+1
                return distance[i]
            else:
                distance[i]=self.get_dist(T,distance,next)+1
                return distance[i]

### 作文

what excites you about the opportunity to work at LiveRamp? 然后写了一篇 TOEFL作文就submit了

In order to avoid cliche that everyone uses to present their passion, I prefer to use a more elegant way to express my thought, that is - use ten bullet point to show my interests.

1. Data is one of the key aspects in business. To some extent it can be regarded as the future, and I want to be part of the future.
2. It is always interesting to extend my knowledge of computer science and math to other areas.
3. LiveRamp's work can be applied on so many fields that there must be many challenges and excitement to work on that.
4. The key ability to explore the world is building connections.
5. That's what LiveRamp do and what I want to get involved.
6. Though lots of people talking about Online to Offline, working on Offline to Online may also be vital to business success.
7. Most importantly, I can work on different things everyday as tomorrow will never be another today in LiveRamp.
8. I really love the creed "Fewer Rules, More Responsibility". That's the creed that every company should follow.
9. Combining the tasks of data science, business and computer science, working in LiveRamp will surely be a heart-racing journey.
10. (bonus) I really love San Francisco!

Thanks for your time.

## 电面

### LRU cache

做法很多地里都有，Leetcode上也有

LRU Cache? All of get, set, remove need to be O(1).

### 像Leetcode上的Word Search

给定一个N*N的字母矩阵，一个Dictionary里面有几个word，要求在矩阵里找这些word。一开始我给了个很随意的算法就是用DFS一个一个找。后来想到用Trie的话更好一些。

### 六度空间

OA里面要求分析各个search 算法的优缺点，描述算法，找寻路径和可能需要的数据结构，普遍认为都是bi-directional最好拉。

我给的解法是
BFS求出target actor的depth, 然后以此为upper bound, DFS解出最短路径

他问如果数据特别大会有什么问题？
我说因为要用queue 存next visiting actors 和set存visited actors，可能queue 和set会太大，放不下
然后他就问，诶你说要用set存visited actors，为啥？要我举例子，然后说如果不存visited actors 会怎样，举例子

这个解释完之后，说假设target在level k，问我的方法里BFS的话，要visit 多少node才到？DFS呢？然后又问我DFS的best case, worst case分别是多少这样然后就结束了让我举例子为啥要存visited actors那边耗了特别久我也是醉了


总体面试体验是 这个面试官人还比较nice，会重复问题以及耐心解释，但是确实给人一种感觉就是没有在认真听你说什么，感觉不是很care

另外如果想准备这家公司的人，我个人感觉是他们真的很喜欢问复杂度，一定要准备好，尤其这道6 degree

### 四张牌

四张牌，分别写着“X”，“Y”，“1”，“2”，然后给你条件：凡写着X的反面都是偶数，请问至少翻几张牌能确定这句话是真话还是假话

cards on the table, X, Y, 1, 2. . WEach card has letter on one side and number on the other side. . Given the statement "The number side of X is even", at least how many cards need to flip to prove/disprove it?

answer: we need to filp two cards, one is X card, the ohter is 1 card. if the other side of X card is odd, the statement is false. OR if the other side of 1 card is X, the statement is false. Otherwise, the statement is true;

### kth smallest element

先说的是sort the list，肯定得说，显示你没看过这道题

然后说用heap，忘了应该用max heap还是min heap了。自己研究半天，一边研究一边ramble，然后跟他说决定选minHeap了。

然后又让优化，我就说quick sort的那个solution，他问了我两遍quickselect和quicksort哪个快……然后问时间复杂度，楼主就卡了……先说worst case是o（n2）,挺好推的。然后他问average case，不会推了，研究半天小声说了句O（n）?然后他就问我是咋推得，我就完了，推半天推出O（n2）……最后说O（n）是best case，average case是O(n2)

一共面了20分钟不到，他就说到时间了……然后问了俩问题就结束了……

我说了三种算法，1. sort array，O(nlgn)，问了为啥nlgn，简单说了下merge和quick sort
2. size为K的min heap，复杂度应该是O(nlgk)吧，不知道之前从哪看了是n+klgn...刚开始照着说的，后来觉得不对劲，自己分析了一下

---

We can find kth largest element in time complexity better than O(nLogn). A simple optomization is to create a Max Heap of the given n elements and call extractMin() k times.
Time complexity of this solution is O(n + kLogn) . when k is much less than n, time complexity is O(n), when k is close to n, it is O(n)
we can use a min heap to find kth largest element. -google 1point3acres
step 1: Build a Min-Heap MH of the first k elements (arr[0] to arr[k-1]) of the given array
step 2: then we iterate through the given array from arr[k] to arr[N-1]; during each iteration, we compare the current element with the root of the Min-Heap

if element is greater than or equal to the root, use it to replace the root and call the heapify function for the Min-Heap
if element is less than the root, we ignore it.

step 3 the root is the k largest element.
time complexity is O(k + (n-k) * logk );

---

快速选择算法,是一种能在大致O(N)的时间内选取数组中第k大或者k小的算法.其基本思路与快速排序算法类似,也是分治的思想.

其实这个算法是个基础算法,但是不常用,所以今天编的时候错了POJ2388,才有了这篇文章.

执行Partition算法(就是那个快排里将区间内所有数划分为小的一部分和大的一部分的过程)
判断第k大的数是在小的部分还是大的部分
递归,直到区间足够小,返回结果

下面几段代码,尤其要注意的是

    while(i<j)

还是

    while(i<=j)

    /*
    Program:快速选择算法样例
    Author:Comzyh
    */
    #include <cstdio>
    int array[10000],temp;
    int N,K;
    int QuickSelect(int arr[],int b,int e,int k);
    int main()
    {
         scanf("%d%d",N,K);
         for (int i=1;i<=N;i++)
              scanf("%d",array[i]);
         printf("The k th :%d\n",QuickSelect(array,1,N,K));
    }
    int QuickSelect(int arr[],int b,int e,int k)
    {
         int i=b,j=e,mid=arr[(i+j)>>1];
         while (i<=j)//注意,小于等于
         {
              while (arr[i]<mid)i++;
              while (arr[j]>mid)j--;
              if (i<=j)
              {
                   temp=arr[i];arr[i]=arr[j];arr[j]=temp;
                   i++;j--;
              }
         }
         if (b<j  k<=j)return QuickSelect(arr,b,j,k);//分治
         if (i<e  k>=i)return QuickSelect(arr,i,e,k);
         return arr[k];//如果不属于任何一方,就结束,返回
    }

### quickselect

quickselect啦，复杂度问的超级细，平均是O(N),最坏是n^2,为啥呢？每一步是咋实现的？代码咋写？问的真是超级细…………所以你认为非常熟悉的算法和结论还是得好好想想，记住过程，他们真的很喜欢问复杂度相关的东西，而且问超级细，要真的搞清楚每一步，不要因为太过熟悉这个东西而忘记细节。

### CSV

一个CSV file，求最快的方法输出第一列和最后一列。我有关这个问题提了好多无所谓的问题，比如输出格式是不是另一个CSV file? 或者就存在Array里就好了。然后我就说我只知道tranverse所有文件然后输出。然后我就开玩笑似的说这肯定不是最优解，能不能给个hint，然后他ramble了一堆不知道是啥。然后我就说我用CSV file的时候是在做mapreduce的时候，然后那个是read by line 的，所以对于每一个line用split by comma然后就拿第一个和最后一个呗……

然后他说这个题没啥algorithm目的，不要担心。

### Find unique browsers in log file.

前面这两道题都会引申到larger file的问题，所以需要在distributed system上处理。今天我碰到的问题就是find unique browsers in log file。

这道题是这样的，LiveRamp每天有很多客户登陆他们的网站，每条登陆信息都记录在一个log file里面，登陆信息包含时间、ip地址、浏览器信息什么。
unique browser的定义是同一台电脑上的firefox算一个，同一台电脑上的不同浏览器比如firefox和safari算两个，不同的电脑上的safari也算两个，这里搞了好久才弄明白。
我说用hash table做这个，用ip address + browser agent information 组成一个identifier，把记录放到hash table。他问我为什么要用hash table，我说for quick lookup，他就问我time complexity是啥，我说是O(1)。
然后他就问我hash table 的缺点是啥，我说缺点是需要占用很大的空间，如果unique browser很多话，一台电脑可能没法容纳一整个hash table。
然后我给出解决方法是用多个machine，每个machine 维护一个hash table，然后用一个hash函数确定某条record要放到哪台电脑。.

这样也有缺点，如果有很多machine, 某个时刻有一台machine crash的概率很高，如果crash了，就需要重启整个系统从头开始，解决方法是每台machine都用一个backup machine。

然后问我还有没有什么缺点，我说还有就是可能某一台machine存满了，但是另一台是空的，这种情况有点像hash table里面的collision和load factor问题。这时再来一条record，我们就需要把这个record放到一台不是full的machine上。因为这条记录在另一台machine上，所以以后我们要找它的时候，如果在当前的machine上没找到，我们需要再另一个machine上找，所以我们需要存一些额外的信息告诉我们如果找不到的话还可能在哪里找。
这道题大概就是这样，这是我的想法，也不知道是不是正确的。

### 投篮选择题

问的题目是投篮3个进2个，或者8个进5个算赢，选哪个

3中2和8中5，不能计算，直觉（逻辑）来选哪一个更好

我觉得我基本就是败在这题，之前看了前面的帖子，所以我答得很快：命中率高选8中5，低就3中2

结果他问我是不是以前做过这题，我吞吞吐吐地说了no，又解释了一大堆，反正解释就是掩饰

然后他就问3中2和8中6呢？

3中2和8中7呢？

很搞笑的是，我自己加上讨论了3中2和8中8

说了几个对的，例如3中2和8中8 无论命中率高低都选3中2
同理3中2 8中7选3中2，因为两种都有一次机会miss，当然选投的少的保险

然后3中2和8中6，我当然和现在都不知道用逻辑怎么分析（数学是知道2/3比6/8小），当时我就说8中6和8中5一样，sample space的问题

according to the law of large numbers (LLN), the average of the results obtained from a large number of trials should be close to the expected value, and will tend to become closer as more trials are performed.
if your shooting probility is greater than 0.6 , I will choose ⅝.  if you are not gooding at playing basketball, I will choose ⅔, and you got that result  by chance.


### 大数据

given 1 terabyte key-value data， how do you store them so that insert， find， delete operations can be very fast？
这个问题我的回答是把这个大的file分成10,000份，then to the remainder that hashcode of each element modulo 10.000， we decide which element is in which small file。

如果有十台机器的话，先把这个big file 划分到10 台机器上，然后再载每台机器上划分成10，000份， 每一份再hash。


### 零散

下面是six degree的题目答案：

We can treat the problem as a graph. Each person represents a node. and if two people are friends, there is a edge between the two nodes that represent them. The problem becomes that find the shortest path between two node: start node and end node.

We can adopt BFS, Dijkstra algorithm,  Bidirectional BFS. |E| is the number of edges, and |V| is the number of vertex.
1   BFS runs in time O(|V| + |E|)
2   Dijkstra Algorithm with a priority queue runs in time O(|E| + |V|log|V| )
Since the weight of each edge in the search grap is same, Dijkstra algorithm  will degenerate into BFS. Besides, it needs more data structre than BFS to implement it. For example, Dijkstra algorithm needs priority queue to keep track of every vertex and distance array to keep track of the distance from source vertex to other vertex.
3   Bidirectional BFS is better than BFS.
I will talk about why Bidirectional BFS is better than BFS below.
assume the distance between source to target is k, and the branch factor is B [every vertex has B edges].
BFS will open: 1 + B + B^2 + ... + B^k vertices.
bi-directional BFS will open: 2 + 2B + 2B^2 + 2B^3 + .. + 2B^(k/2) vertices.
for large B and k, the second is obviously much better the the first.

I will choose bidirectional BFS.

Algorithm idea: do a BFS search simultaneously from the source and the target level by level. (level 0 from source and target respectively , level 1 from source and target respectively....)    The algorithm will end when the level from source meets the level from the target.

We will use the following data structures:
1   two queues to do BSF respectively from source and target node
2   we need class Node to represent every node in the graph.
Class Node {
        public String name;
        public ArrayList<Node> neighbors; //
        public ArrayList<Node> predecessors; // to keep track of predecessors of every node in order to construct the shortest path after Bi-                         BFS
        public boolean visited; // label the visited node
        public boolean visitedFromStart; //label the node that are visited from start node
}

Below is my java code to implement the bidirectional BFS. After we run the bidirectional BFS., we can construct the shortestt path by use of  predecessors of every node form start node to end node.



import java.util.ArrayList;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;


public class Solution {
        public class Node {
                public String name;
                public ArrayList<Node> neighbors;
                public ArrayList<Node> predecessors;
                public boolean visited;
                public boolean visitedFromStart; //label node that are visited from start node

        }

public        void Bi_BFS(Node start, Node end) {
                Queue<Node> Q1 = new LinkedList<Node>();
                Queue<Node> Q2 = new LinkedList<Node>();
                Q1.offer(start);
                Q2.offer(end);
                start.visited = true;
                start.visitedFromStart = true;
                end.visited = true;
                while (!Q1.isEmpty() && !Q2.isEmpty()) {

                        int LevelSize1 = Q1.size();
                        for (int i = 0; i < LevelSize1; i++) {
                                Node front1 = Q1.poll();
                                for (Node next : front1.neighbors) {
                                        if (next.visited == false) {
                                                Q1.offer(next);
                                                next.visited = true;
                                                next.visitedFromStart = true;
                                                next.predecessors.add(front1);
                                        }
                                }
                        }

                        int LevelSize2 = Q2.size();
                        for (int i = 0; i < LevelSize2; i++) {
                                Node front2 = Q2.poll();
                                if (front2.visitedFromStart ) {
                                        return;
                                        //we find the shortest path
                                }
                                for (Node next : front2.neighbors) {
                                        if(next.visited == false) {
                                                Q2.offer(next);
                                                front2.predecessors.add(next);
                                                next.visited = true;
                                        }
                                }
                        }


                }
        }

}


下面是max stack from scratch

class MaxStack {
    private Stack<Integer> stk = new Stack<Integer>();
    private Stack<Integer> maxStack = new Stack<Integer>();
    public void push(int x) {
        if (maxStack.empty() == true || x >= maxStack.peek()  ) {
            maxStack.push(x);
        } //if the input element is greater than or equal to maxStack.peek, then                          //        put it into maxStack
        stk.push(x);
    }
    public void pop() {
        int result = stk.pop();
        if ( result == maxStack.peek() ) {
            maxStack.pop();
        }

    }
    public int top() {
        return stk.peek();
    }
    public int getMax() {
        return maxStack.peek();
    }
}


一个文件找出unique words 的数目?如果是1GB?   hashset    1TB? 分布式系统design
下面是这道题目的我和朋友们讨论的答案：

思路1：把数据分块，对每块unique再把这些结果收集起来一起uniqiue
思路2： 根据STRING产生HASHCODE，再和总机器数量去余数，根据余数可以把一样的STRING都分配到一个小机器上，每台机器分组HASHSET 先把小集合里面重复的都去掉 汇总应该就可以了
assume we have n computers, then we scan the big file, and compute the hashcode of each string, then  hashcode modulo n (the number of computers) , we get a remainder. according to the remainder, we assign the string to respective computer. after scan the whole file,  each mechine will use a hashtable to count the number of unique string on that mechine. Then we add up the number from all mechines. and we get the total number of unique string.
If there are a lot of strings on one mechine, we can divide the strings into M chunks, for each chunk, we use a hashtable to find out the unique strings and put them into a file.  then merge these small files into a big file.  Then we do the same operation on the big file recursively until there are no duplicates and we count the number.
思路3： 1. 采样1% string，数据大的话实际上0.1%也成，排序。2.把这个排序的文件分成n份，记录下分点上的string。3.处理源数据，分成m块，每块uniq，然后对每个结果string，在2的结果上二分查找决定分到哪份，写下去

step 1 we take some sample strings from the big file. for example ,one percent or  zero point one percent (0.1 %) if the file is too big. Then we sort the sample strings.
step 2 we divide the sample strings into N intervals
step 3 we divdie the big file into M chunks, for each chunk we use a hashset to find out the unique strings. then for each unique string we use binary search to find its position in the smaple strings, put it into relitive interval.
step 4 we deal with the N intervals respectively.  for each intervals we use a hashmap to  find out the unique strings . Then  we add up the number of unique strings in each interval  and we get the total number of unique string. . 涓€浜�-涓夊垎-鍦帮紝鐙鍙戝竷





人很好的一个美国小哥。。。问的是那道unique id的问题。差点儿没有把我问死。。。。
首先说dataset比较小，HashMap存。然后问dataset比较大怎么办？我开始说分成chunks然后每一处理。面试官很不满意。我立马改口说，那mapReduce解。. 1point 3acres 璁哄潧
面试官说这个make a lot more sense
然后问，如果mapReduce的话，performance的瓶颈在哪里？
我说首先startup overhead可能比较高，另外，如果data 很skewed的话，一个reduce task没有办法handle
那他问怎么办？我说，那写一个partition function处理。然后他问，这个partition function怎么写？我没有写过啊！！！（此时心中已经放弃这个公司了。。。）
纠结了半天也没有写出了，然后他引导说是不是要写个combination function更好？我立马意识到找unique id嘛，在combination function里面存一个hashSet
然后把map的key value pair 预处理一下再给reduce task，如果重复出现的key就不需要给reduce了。他说那如果是combination function里面的set没有办法在内存里面
放下所有的key怎么办？然后我就说，那存到disk里面？然后在memory里面maintain一个table，这个table是key的一个range 和disk上存这个range的disk block的address的
映射关系。然后再去disk seek就可以了。。。

---

目前看得到的LiveRamp面经整理如下，希望能够帮助到将要面试的童鞋，包括我自己^_^帖子的时间都是2014下半年到2015年1、2月的，应该不会过期

// 感言及提醒
1. 首先澄清一点大家的错误认识，LiveRamp实际上最近还是一直在招人的, 否则我也不会拿到Offer。我问了其中一些人，他们说基本每天都有一个人去Onsite，所以就算去onsite拿到的比例还是很低的。现在的Engineering team大概35人，计划今年double。. more info on 1point3acres.com
Six-degree那题一定要好好准备，知道所有常见的解法及相互之间比较，时间复杂度和空间复杂度分析。

// OA
1. 电话面试之前要做一个OA，题目不是很难，大概有10道左右的关于时间复杂度和算法的选择题。然后就是那个著名的six-degree的问题，其实就是在无向图中找两个点之间的最短路径，不需要写代码，只要分析讨论一下各种不同的算法之间的优劣，然后说明自己想选择哪种算法就可以了。如果时间允许，尽量多讨论一些算法，BFS，Dijkstra, Bi-BFS等等。我选的是Bi-BFS。然后还有一个问题问为什么选择Liveramp, 随便写写就行了。glassdoor也有详细的OA的题目。. 涓€浜�-涓夊垎-鍦帮紝鐙鍙戝竷

2. 关于OA，已经有太多的面经，我在这里就再稍微简单说下吧。就是基本的算法复杂度分析和那个six-degree的题。当时我做OA的时候也没太认真想six-degree的所有解法，就只写了DFS, BFS和Bi-directional BFS，然后选bi-BFS写了要用到的数据结构（两组）：
首先是BFS需要的Queue
存距离的Map
为恢复路径存BFS路径上一个节点的信息Map. 1point 3acres 璁哄潧
上述数据结构需要两份，因为bi-BFS是双向的，而且需要step by step，每个BFS轮流走一步。. 涓€浜�-涓夊垎-鍦帮紝鐙鍙戝竷
好多人觉得自己OA做的不错但还是被拒了。。我也不知道为什么 问了一些同学朋友感觉他们答的也不错。。所以到底判断标准是什么呢？ 鏉ユ簮涓€浜�.涓夊垎鍦拌鍧�.
1小时候收到一面。

3. 之前有传闻说他家换题了，但是我碰到的还是经典的那几道题。。。前面的真的太容易了，，就一道题比较tricky
个关于算法的时间复杂度问题。其中一个题是关于求pairs和的问题。就是给定一个array，长度为n， 则有n＊（n – 1）／ 2个pairs。 先将每个pair里的两个数加起来，得到n＊（n-1 ）／2 个，然后将这些数加起来。得到一个总和。题目问的是求这个总和最快方法的复杂度是多少。这个题目比较贱。从题目的描述以为是O（n＊n）， 其实是O（n）。因为等于所有数加起来然后乘以(n-1)。。。
传闻中的六度空间还在（是不是因为我运气好，之前有几个人说等到最后也没碰到）。。然后我就bi-BFS。。。
后面的behavior看来是无所谓的，因为我没怎么答也通过了。。

// Phone Interview
1. 印度小哥面的 口音很纯.1point3acres缃�
先介绍一下面试内容 说大概20分钟
然后讲了一下简历 他看我介绍的是big data的project 于是开始问 假设有1GB数据对 怎么储存 我说HashMap就可以了
然后问如果数据量达到1TB又怎么处理 我说用一个hashMap映射到10个Map
follow up假如数据量分布不均匀怎么办 我开始说可以在数据录入的时候跟踪用别的方法来record 面试官说这样太麻烦 后来我想不起来 说应该有一种数学分布可以解决这个问题 把数据平均化 小哥说确实有一种 然后说了半天没听懂
然后小哥问 那这个分布式系统需要一个master机器吗 我说需要。。（大概会跪在这儿） 他说其实不用 问我为什么 我说可以减少流量 他说防止failure 免得一个机器废掉都废掉了。。. 1point 3acres 璁哄潧
最后我问了下公司大概有多少人 他说有34到35个engineer 在未来7个月会扩张一倍
. From 1point 3acres bbs

2. 之后就是电面了。我第一轮电面就问了为什么投Liveramp, 然后就在详细地问six degree的问题。问了各种算法的时间空间复杂度，以及BFS和双向BFS算法具体是怎么实现的，算法运行完了之后如何找出具体的最短路径。然后又follow-up了一个问题，就是如果图太大了，储存空间不够，不能用BFS，应该怎么办？ 这种情况就要用IDS算法，就是多次执行DFS，每次增加depth，直到找到最短路径。这种算法空间复杂度跟DFS一样，时间复杂度比BFS稍大，但是也没有大很多。我第一轮电面大概就20分钟就结束了。
然后当天就邮件约了第二轮电面。我看了一些其他的面经说第二轮电面会问一些概率题，然后就是继续问six-degree。可能我第一轮电面six-degree已经问的很透彻了，所以第二轮没有问six degree。上来还是先问为什么Liveramp, 接着问了那个著名的投篮概率问题。就是投篮3中2和8中5应该选哪个？ 这个问题以前很多的面经都讲过了，大概就是如果投篮命中率比较高，选3种2，投篮命中率比较低的话就选8中5. 因为投篮次数越多，结果越接近数学期望，所以如果命中率是90%，应该尽量多投，这样避免意外。如果命中率只有10%，那应该选择3中2，因为投篮次数越少，结果越离散，只投3次因为运气意外赢的可能性比较大。接着问了一个涉及dsitributed file system的问题。开始就是问有一个file，里面包含很多访问者的ID，要统计总共有多少unique ID, 这个就扫一遍文件用hashset做就行了。接着问假如ID太多，储存空间不够，不能用hashset怎么办？这样就要先sort这个文件里的ID，然后扫一遍统计一下，不需要hashset了。接下来继续问如果给你一个machine上存着这个文件，另外再给你10个machine, 怎么构建一个分布式的系统能够最快速地算出总共有多少unique ID. 会不停地问你还能不能继续优化，目前你的方案有没有缺陷之类的。



3. 第一轮电面：我觉得在电面前应该先把公司网站上写的东西认真看下对公司和产品稍微优点了解，因为在两轮电面中我都被问到了。。聊天扯淡问简历差不多就10多分钟了。接下来又问到了six-degree，具体主要是问普通的BFS和双向BFS的区别，为什么双向的能够省时间和空间，省多少时间和空间。我基本也就是举了个worst case，双向BFS的空间及时间复杂度和普通BFS相比大概都是开根号的关系，如果这点没有想明白的同学一定要把这个问题想清楚，二面也问了这个。还有问了那个X, Y, 1, 2扑克牌的问题（一面数字，一面字母）。这题那个面试官给我描述的太混乱了。。为了搞清楚题意，我让他重复了好多好多遍，大概10分钟才弄明白题意。。然后知道题意后基本就几秒钟就知道怎么做了。做这道题前没太看面经，后来看了才知道好多人已经被面过这个了。我觉得最简单的题意的表述是这样的：现在给你一个statement: “X的背面一定是偶数“，上述扑克牌你至少要翻几次才能验证这个statement是对的还是错的。扑克牌两面的数字和字母对应关系可以是不一样的，例如可以同时有以下两张扑克牌： Y/2, Y/3。理解题意后就非常简单了，就翻X和1就行了，因为只有这两者有可能证否。1.5h收到二面。. 鐣欏鐢宠璁哄潧-涓€浜╀笁鍒嗗湴
第二面电面：
就开始同样是扯淡聊简历10多分钟。然后就是那个著名的投篮问题了。我被问到的是2/3和4/6的比较，貌似和大家经常被问到的5/8不太一样。我觉得看过面经的同学基本都知道这道题应该是分命中率讨论的。因为在两个数值差不太多的时候，样本空间的大小有很大的影响。投篮次数少（样本空间小）则有很大的不确定性，如果命中率不高果断选投篮次数少的。高的话就选投篮次数多的，因为当样本空间足够大的时候，进球数会基本靠近于命中率 * 投篮次数。 以上只是最基本的分析，对于不同的数字组合，可能分析上会略微有不同，不过总体思路就是这样。. From 1point 3acres bbs
之后又是six-degree,问的内容基本重复一面的。忘了在一面还是二面的时候问我有多少中解法的时候我还说了Dijkstra,然后就问我为什么不用这个。这题很明显所有边的权重是一样的，所以Dijkstra就退化成了BFS，所以二者是一样的，况且Dijkstra还要维持一个堆，时间复杂度更高。
接下来问了下说如果要你给别人介绍他们公司的产品，你会怎么介绍。这点是非常重要的，也是为什么我让大家提前去看他们公司产品资料的原因，如果看了还不太明白的话可以直接看最下面有一些”Case Study”. 1.5h收到onsite



4. 之前做的OA 然后约的电面我没接到 他家HR连发两封邮件让重约 。。上来吐槽下那个逻辑题 四张纸 X Y 1 2 每张纸一面写数字一面写字母 问要翻几张纸才能确定X对面是不是偶
算法继续问六度 不过我刚说完BFS 他就很深入的要聊这个 最后他给了个图 把整个流程都要讲一遍 包括怎么存储路径.1point3acres缃�
最后问问题 他名字叫Roshan 我就问了他玩不玩dota
这个公司不抱什么希望 下周factset onsite 求指点求人品
. 1point 3acres 璁哄潧

// On site
1. 第一轮：一个Team Lead面的，他一个人就lead 3个team, 也是醉了。。不过每个team都挺小，就3-5人。聊天扯淡30多分钟，最后问了一道coding.
给定一个概念，叫做加密可替换，定义为两个单词间每个字母都能通过一套映射规则相互替换。为了大家理解举几个例子： aba和cdc，这两个就可以，因为映射关系可以为a-c, b-d。aba和cde这两个就不是加密可替换，因为不能同时a-c且a-e。-google 1point3acres
然后输入是Set输出格式是List>, 所有相互间加密可替换的单词组成一个group，就是一个List, 然后返回所有的group。同个group任意两个单词间都可以是不同的映射规则，只要保证任意两个可以通过某个映射规则替换成对方就行。
第二轮：
又是聊天聊了40分钟，然后让写个subset。。。为了装作没做过，假装想了一下，然后很快就写完了。
第三轮：
Decode Ways。。同上，假装想了一下，然后先随便用O(n)复杂度的DP写了。写完后写几个test case。然后说空间可以优化为O（1）。 接着问了一个很神奇的问题，做好几遍这个题都从没想过的。问我能不能给出一些答案的upper bound，不一定需要非常tight的upper bound。我最开始说了Fibonacci数列，然后说了快速计算Fibonacci数列第n个数的方法，这个答案面试官还是很满意的。然后又问有没其他的upper bound。我在很努力的想其他tricky的upper bound的同时顺便说下非常明显的upper bound是2^n，结果他说他就是要这个答案，给跪了。。害我想的非常复杂，以为有什么tricky的答案。。
第四轮：
VP面的，同样聊天聊了40分钟，最后10多分钟先是问了level order traversal，不过给的tree不是Binary的，child使用一个list来存的。只需要print不需要返回。但是基本思路反正都一样，这个很快就写完了。follow up: 如果在Queue初始化的时候就要指定分配的内存空间的大小，要怎么给出一个尽量小的值但同时保证得到正确答案。然后就是各种复杂度分析。之后的一个follow up是，如果树的层数非常多，每个node的child也非常多，怎么解决。这个问题想了挺久，还说了各种奇奇怪怪的方法，包括用分布式的计算等等等。。结果说是只能用一台机器。结果是他给我提示了下说如果要输出第10层的所有node要怎么做。有了这个提示就很简单了，对于特定层用限定深度的DFS就行了，所以就逐层DFS就行了。

// 传说中的six degree from glassdoor
Six Degrees of Turkey Bacon You've always been intrigued with the Six Degrees of Kevin Bacon game. Let's say if two actors have been in the same movie we call them 'friends' and if two actors have not been in the same movie, we say they are not 'friends'. Now choose any two actors at random -- we want to calculate the number of degrees of separation and the path between them. How do you go about this problem? • Discuss your algorithm ideas. For each algorithm talk about the tradeoffs. • Choose which method you think is best for solving this problem and describe how it works. You may also want to talk about what data structures you would use to implement it.
. Waral 鍗氬鏈夋洿澶氭枃绔�,
祝各位好运吧！！

30min电面先是闲聊，然后两个问题：
1，Word Ladder2
2， find the kth integer in array

---

上个月吧，去了onsite，第二轮被请出来了，好凄惨，但大概对这个公司有了些了解，希望可以帮到大家。

六度问题大家都会说双向bfs，说真的我身边认识的人在project里用到双向bfs的人很少，所以可以讲大家都是现学的，所以注意一点，绝对不要学着wiki或者教程里的名词以及说法，大多数教程都会讲branch factor，其实所谓branch factor无论多少都是linear，直接把n放上去就好了。他家初期有一道题是让你用ruby写black jack，借鉴了github上的一个作品的都是秒跪，他家只要看出你见过这题就是跪。

系统设计我没有做过distributed的东西，给大家一点建议就是架构和并行运算，所有存储类的，速度问题就拿架构里的cache往里套，分布存其实和memory里的paging也是一个道理。运算类的其实mapreduce就是一个机器的并行，只不过有一些自己的特性比如某个机器fail了怎么recover，但并行就是并行，玩过cuda会发现其实都是通的。

Onsite，
所有所有你能找到他们给onsite的，都是本地人，都是自己开过去的。或许有外地的我没找到。但他们会在邮件里和你谈机票的事，不能放过他们，san jose飞过去也是飞。

上面说过，这里可以找到两个onsite的面经，里面的有一道题，两个面经明显能看出说的是一题，但两人说起来的细节至少我的理解看来完全不是一回事。事实上真面起来会发现那两人都没说清楚，是另外的一回事。要小心，我就是先入为主在那题上漏出我明显是准备过的了。

onsite会见到他家的vp，此人很浮夸，他问你题的时候会在非常常识的问题上去问你，而且真心好演技，一脸脑子转不过来五官聚在一起的表情，我一开始都很惊讶这你都能卡？要心平气和的面对他。

还有一点，他家一楼要按密码才能进，邮件完全没提，楼下也没写电话，我是正好赶上一个intern上班带进去的。＃20，如果你去onsite可以直接按这个进去，因为如果你开过去，从圣何塞到三番能开3小时以上。别在这里再耽误时间了。

最后，他家很忙，很忙很忙，当然他们会说还好，但细聊会发现他们几乎每天都有feature上线，每天噢，每天都有新feature而且还要修改之前犯的错误，说真的，我觉得就算是巨牛也只能说很好的完成，不能说不忙吧。

### onsite

1. 给一个 tree，要 traverse it level by level。如果每一层有 1000 个点，共有 1000 层，会需要多少 memory？该如何修改 solution？

2. power set

3. decode ways

补充内容 (2015-3-29 03:03):
power set: Given a set, generate all possible subsets
decode ways: Given a number, find out number of possible decode ways. (Decode: 1=a, 2=b, ...; so 26 can be z or bf)

楼主是三月初时候去的onsite，OA，一轮二轮面的和地里已经有的面经基本一样，没什么特别的。
1.上午11点开始，早到了一小会儿，在一个会议室里面等着，时间到了就进来一个美国小哥，说是在这工作5年了，然后问了一堆behavior的问题，why liveramp, how do you judge a company什么什么的，之后对着简历的项目一直问，问完之后估计已经过了快四十分钟，第一道coding题目实在想不起来，印象中是非常简单的。. 1point3acres.com/bbs
-google 1point3acres
2.之后两个美国小伙带我去一家墨西哥餐厅点了菜带回到公司吃，吃完下一轮。. 1point 3acres 璁哄潧

3.带吃饭的其中一个美国小伙面的，先聊了大概十几分钟，coding是subset的题目，我自己写的input是个vector，然后他说我题目说的是个set，他们有什么区别。我说了一通之后，他说其实我只是想强调一下set里面没有duplicates，好吧。。其实有duplicates我也会。写完之后go through一遍，然后模拟一下整个函数运行过程。之后还有时间，他说再出个bonus的question吧，设计一个编码转化的方法，大概就是说如果输入个vector<string>,输出是个string，然后你能从这个string再返回原来的vector<string>，之前在哪里见到过，就说了对每个string，变成SIZE#string（abc->3#abc），他说good。

4.带吃饭的另外一个小哥面的，他先问了我一下上一个人面的是什么然后也是聊了十来分钟，后面一道coding的题目。题目是之前面经提到的一个，就是两个string能通过某种映射map起来的就是放到一个group里面，例如abc－cba（a -c,b-b,c-a）。给你一个word list，把它们group up。
. more info on 1point3acres.com
5.最后是vp，聊了一会，coding是个tree level order traversal。用queue写完，然后问如果要提前分配memory给queue的话，你要分配多少，再然后就是如果tree非常大，memory不够，你用什么方法。我用的是limited depth dps，又问这种方法可以，但是某些情况下会非常expensive，举个例子说明，之后又讲到一些space和time的tradeoff。

面得题目都不难，而且很多和面经提到的很类似，整个过程基本很顺利，过了几天就收到thank you了。楼主问feedback，不到2分钟就回了，Thanks for your continued interest and request for feedback. Unfortunately, we cannot provide any feedback on the interview process. However, we want to assure you that this does not reflect on your skills and we are confident that you will find a rewarding position.
. from: 1point3acres.com/bbs

这家公司在sf downtown，规模还蛮小的，在公司里面基本没看到几个中国人，烙印也很少，可能除了technical方面之后还看重其他一些东西，anyway，反正是挂了，希望地里其他的小伙伴加油

---

面试官是Roshan，以前都有见他问了六度的问题，这次居然没问。。。。。。

1. 上来还是卡片的问题，4种卡片，一面是字母，一面是数字，在桌子上我们看到X，Y，1，2，给一个statement：X的背面都是偶数，判断对不对。
-google 1point3acres
2. 然后问了一个如何存数据的问题. 1point3acres.com/bbs
           1. 假设有1GB的key-alue pair，用什么存储？答：HashMap-google 1point3acres
           2. 假设是1TB，key是唯一的，value可能重复？答：按value存好，然后还是hash(面试官可能想其他的，但当时一直follow up，直接就说了)
           3. 假设所有的都是唯一的，key唯一，value也唯一，只有10MB的内存，1G的数据，怎么存？答: 存在数据库里
           4. 存在数据库里怎么存，怎么搜，时间复杂度是什么？ 答：简单建个表，按key的升序存，二分查找，log(n)
           5. 按照hashmap存，查找一定快吗？ 答：如果在直接在内存中会快，如果还要有与disk交互的话就不一定了
           6. 现在有多个machine，怎么存？建个hash表，key-machine index pair
           7. 给一个hash function， k个machine，n个key？n % k
           8. 如果新增加一个机器，很多数据都要移动（因为k = k + 1了），怎么办？用B+tree结构来存数据

基本上面试官不否定我的想法，只是不停地follow up。。。。听过之前小伙伴们的吐槽，就这样把，锻炼锻炼好了. 1


1. 给你 key-value pair data, 总共”1GB" dataset, 请问如何设计系统?
    我回答用HashMap可以average O(1) for insert, delete and lookup
    另外可以用Mongo DB等NoSQL DB去实现增进performance (这句似乎未必正确)
. visit 1point3acres.com for more.
2. 给你 key-value pair data, 总共”1TB" dataset, 请问如何设计系统?.鏈枃鍘熷垱鑷�1point3acres璁哄潧
   用Hadoop + MapReduce+HBase建分散式系统, 为了No single point of failure design, 不能只有一个NameNode.
   可以用Zookeeper去做locks & synchronization, 储存metadata. 建client, server端的cache去达到faster retrieval,. Waral 鍗氬鏈夋洿澶氭枃绔�,
   降低latency of random read request. 做Block compression...
