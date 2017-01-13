# Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the word list
For example,

Given:

    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]

Return

    [
        ["hit","hot","dot","dog","cog"],
        ["hit","hot","lot","log","cog"]
    ]

Note:

+ All words have the same length.
+ All words contain only lowercase alphabetic characters.

## Solution

BFS + DFS

先用BFS找出最短路径，在Word Ladder I的基础上修改，使BFS遍历到的word按遍历先后层级排列；然后用DFS找出所有可能的最短路径。
 
这个问题从Word Ladder I的基础上演变而来。Word Ladder I相对简单，只需求出两个单词间的最短路径即可。普遍的做法使用BFS。而这个问题则要求所有可能的最短路径。

II的解法也有很多种，但是却不容易[AC]通过，主要原因是时间复杂度太大： 造成时间复杂度过大的可能有两个原因：

原因1. 在字典很大的情况下，Word Ladder I也有相同原因，即与其遍历整个Set<String> dicts，不如在当前word string的基础上把每个char分别尝试替换为[a-z]，总共遍历长度是word.length() * 26；可能远远小于遍历整个字典所需要的时间。 
(题外话：我称这种为小学生思路，因为我觉得如果让一个小学生来做这类题目，他们可能往往想到的就是这种最朴素的解决办法。而由于大部分程序员的思路会受到刷题训练的限制，往往想到iteration就是用while或者for loop来遍历，而忽略了看似简单幼稚，实则可能更实用的解法)

原因2. 第二个超时原因就在于具体如何找出所有的最短路径的方法上了;

原因3. 在以上两个解决的前提下，可能还需要用到DP Cache来保存结果避免重复计算。

我的想法是这样的：

(1) 在原因1.解决的前提下，既然用BFS去寻找第一条最短路径是肯定不会超时的，那么如果我用一个时间复杂度不大于BFS的算法去找出所有路径，也不会超时；

(2) 我先想到了DFS，但是还不知道如何应用DFS去解决。我先在纸上画出了BFS的队列模型，试着找出线索。

看一个稍微复杂点的例子：

    start = hit
    end = cog
    dict = [hot,dot,dog,lot,log,dof,mit,sit,set,mog,mig,seg,nax,max]
    Return
      [["hit","hot","dot","dog","cog"],
       ["hit","hot","lot","log","cog"],
       ["hit","mit","mig","mog","cog"]]
    word ladder bfs level

蓝色的线表示valid（可以连通start -> end），红色的线表示invalid。其中，"nax"和"max"这两个单词均未遍历到。

可以发现BFS遍历到的word是有层级先后顺序的：

    level 1: [hit] 
    level 2: [mit, sit, hot] 
    level 3: [mig, set, dot, lot] 
    level 4: [mog, seg, dof, dog, log] 
    level 5: [cog]

在建立了这个样个BFS层级结构的基础上，不难想到最短路径就是在每一层level中选一个word组成的。这里就可以用DFS来解决了。

到这里初步的想法成型了，还有两个需要想清楚的问题：

(1) 字典中其他尚未遍历到的单词，比如"nax"和"max"，如何处理，是否可以被忽略？ 必要性 
是。这些单词有两种情况，"nax"和"max"是属于同一种情况，他们不参与任何形成start -> end的路径；还有一种情况，比如加入一个单词"sog"，那么便有一条长度为6的路径[hit,sit,set,seg,sog,cog]，但是这条路径由于超过了最短路径长度5，所以"sog"可以被忽略。

(2) BFS建立的层级结构，它包含了所有可能构成最短路径的word吗？ 充分性 
能。但是需要在Word Ladder I的基础上修改，防止一找到路径就结束程序。而是要继续找出同一层级中的其他word，倒数第二层(end 前一层)上的word都有可能是构成最短路径的最后一步。

## Code

```java
public class Solution {
    public List<List<String>> findLadders(String start, String end, Set<String> dict) {
        List<List<String>> res = new ArrayList<List<String>>();
        if(start.compareTo(end) == 0) return res;
        Set<String> visited = new HashSet<String>();
        Set<String> cur = new HashSet<String>();
        HashMap<String, ArrayList<String>> graph = new HashMap<String, ArrayList<String>>();
        graph.put(end,new ArrayList<String>());
        cur.add(start);
        boolean found = false;
        while (cur.isEmpty() == false && found == false) {
            Set<String> queue = new HashSet<String>();
            for(Iterator<String> it=cur.iterator();it.hasNext();) {
                visited.add(it.next());
            }
            for(Iterator<String> it=cur.iterator();it.hasNext();) {
                String str = it.next();
                char[] word = str.toCharArray();
                for (int j = 0; j < word.length; ++j) {
                    char before = word[j];
                    for (char ch = 'a'; ch <= 'z'; ++ch) {
                        if (ch == before) continue;
                        word[j] = ch;
                        String temp = new String(word);
                        if (dict.contains(temp) == false) continue;
                        if (found == true && end.compareTo(temp) != 0) continue;
                        if (end.compareTo(temp) == 0) {
                            found = true;
                            (graph.get(end)).add(str);
                            continue;
                        }
                        if (visited.contains(temp) == false) {
                            queue.add(temp);
                            if (graph.containsKey(temp) == false) {
                                ArrayList<String> l = new ArrayList<String>();
                                l.add(str);
                                graph.put(temp,l);
                            } else {
                                (graph.get(temp)).add(str);
                            }
                        }
                    }
                    word[j] = before;
                }
            }
            cur = queue;
        }
        if (found == true) {
            ArrayList<String> path = new ArrayList<String>();
            trace(res, graph, path, start, end);
        }
        return res;
    }
    public void trace(List<List<String>> res, 
                    HashMap<String, ArrayList<String>> graph,
                    ArrayList<String> path,
                    String start, String now) {
        path.add(now);
        if (now.compareTo(start) == 0) {
            ArrayList<String> ans = new ArrayList<String>(path);
            Collections.reverse(ans);
            res.add(ans);
            path.remove(path.size()-1);
            return;
        }
        ArrayList<String> cur = graph.get(now);
        for (int i = 0; i < cur.size(); ++i) {
            trace(res,graph,path,start,cur.get(i));
        }
        path.remove(path.size()-1);
    }
}
```

