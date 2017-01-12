# Word Ladder

出处

Given two words (start and end), and a dictionary of words, find the length of shortest sequences of words from start to end, such that at each step only one letter is changed.

e.g: start word: hat     stop word: dog

dictionary{cat, dot, cot, fat}

sequence: hat->cat->cot->dot->dog

## Solution

这是一道比较有技巧性的题目。由于有一个起始点，一个终止点，需要求一个最短路径，故可以尝试用图来解决：我们可以将所有的单词看做一个图的节点，如果一个单词变换其中的一个字母就能变成另外一个在字典中的单词，那么我们就可以用一个有向箭头从原来的单词指向变换后的单词。那么，最短的变换次数就转化为从一个单词所在的节点到另一个单词所在的节点的最短路径。

然而，第一个难点在于如何构造图，并且建立两个节点之间的联系。比较容易想到的节点联系方式是：对于某个字典中的单词，遍历整个字典，判断其他单词与该单词是否只有一个字母不同，这样做的时间复杂度是`O(n*L)`，L是单词长度。另一个比较巧妙的做法是，对于给定单词的每个字母，逐个用26个字母全部替换一遍，并判断字典中是否有替换后的单词。由于判断是否存在可以用哈希表，时间复杂度为常数，故这样做的时间复杂度是`O(26*L)`。通常情况下，可以假定n大于26，则第二种方法更好。

在确定了如何构造图的基础上，我们考虑如何进行BFS寻找最短路径。我们在实现BFS的时候可以用一个队列作为辅助：将当前能到达的所有节点放进去，然后放一个空节点作为层次的分割；然后取出队首，将队首所指的节点都放入队尾；如果队首为空节点，可知这是层次的分割符，则路径长度加1。注意，题目中最短的要求使得我们的路径中不能有环，换言之，一旦加入过队列的节点不能再次入队。

---

分析：这种题，肯定是每次改变单词的一个字母，然后逐渐搜索，很多人一开始就想到用dfs，其实像这种求最短路径、树最小深度问题bfs最适合，可以参考我的这篇博客bfs（层序遍历）求二叉树的最小深度。本题bfs要注意的问题：

+ 和当前单词相邻的单词是：对当前单词改变一个字母且在字典中存在的单词
+ 找到一个单词的相邻单词，加入bfs队列后，要从字典中删除，因为不删除的话会造成类似于hog->hot->hog的死循环。而删除对求最短路径没有影响，因为我们第一次找到该单词肯定是最短路径，即使后面其他单词也可能转化得到它，路径肯定不会比当前的路径短（如果要输出所有最短路径，则不能立即从字典中删除，具体见下一题）
+ bfs队列中用NULL来标识层与层的间隔，每次碰到层的结尾，遍历深度+1

## Complexity

对于每个节点构图需要的时间复杂度是`O(26*L)`，BFS不重复地至多走过n个节点，故算法复杂度`O(26*L*n)`

## Code
 
```java
int wordlength(String word, ArrayList<String> dict){
	int step = 1;
	Queue<String> queue = new Queue<String>();
	HashSet<String> hashset = new HashSet<String>();
	queue.add(word);
	queue.add(null);
	
	while (!queue.isEmpty()){
		String tmp = queue.poll();
		if (tmp.equals(word)){
			return step;
		}
		if (tmp == null !&& queue.isEmpty(){
			step++;
			queue.add(null);
		} else if (!queue.isEmpty()){
			for (int i = 0; i < tmp.length(); i++){
				for (int j = 'a'; j < 'z'; j++){
					String mid = tmp.substring(0,i) + (char)j + tmp.substring(i+1);
					if (!hashset.contains(mid) && dict.contains(mid)){
						hashset.add(mid);
						queue.add(mid);
					}
				}
			}
		}		
	}
	return -1;
}
```

