# Yahoo

## Phone Screen

一定要注意问清楚细节，要求我做什么

### Use minimum counts of coins to represent a number

从大到小排列硬币，然后动态规划，其中 dp[i] 表示面值为 i 时的最小硬币数。递推公式为

+　dp[0] = 0
+　dp[i] = min{dp[i-A[j]} + 1

这里 A[j] 表示第 j 个面值，比如现在要求 dp[10] 有面值为 1,2,5 的硬币，那么就应该找 dp[5], dp[8] 和 dp[9] 的最小值，加一表式从那个值到当前值最少需要的硬币数量。

---

### Lognest Palindrome Substring

这题从两个角度来考虑即可，一个是以每个字符为中间来进行扩张，另一个就是 manacher 算法。代码如下

```java
public String longestPalindrome_3(String s) {
    int n = s.length();
    int idx = 0, maxLen = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j <= 1; ++j) {
            boolean isP = true;
            for (int k = 0; i - k >= 0 && i + j + k < n && isP; ++k) {
                isP = (s.charAt(i - k) == s.charAt(i + j + k));
                if (isP && (j + 1 + k*2) > maxLen) {
                    idx = i - k; maxLen = j + 1 + k*2;
                }
            }
        }
    }
    return s.substring(idx, idx + maxLen);
}

public String longestPalindrome_4(String s) {
    int n = s.length();
    int idx = 0, maxLen = 0;
    StringBuffer sb = new StringBuffer();
    sb.append('^');
    for (int i = 0; i < n; ++i) {
        sb.append('#');
        sb.append(s.charAt(i));
    }
    sb.append("#$");
    n = 2 * n + 3;
    int mx = 0, id = 0;
    int[] p = new int[n];
    Arrays.fill(p,0);
    for (int i = 1; i < n - 1; ++i) {
        p[i] = (mx > i) ? Math.min(p[2 * id - i], mx - i) : 0;
        while (sb.charAt(i + 1 + p[i]) == sb.charAt(i - 1 - p[i])) ++p[i];
        if (i + p[i] > mx) {
            id = i; mx = i + p[i];
        }
        if (p[i] > maxLen) {
            idx = i; maxLen = p[i];
        }
    }
    idx = (idx - maxLen - 1) / 2;
    return s.substring(idx, idx + maxLen);
}
```

---

### Boggle game, word search

题目大概要求就是在一个 MxN 的矩阵中找到单词，所以可以使用 Trie Tree 来存储字典(具体怎么写可以暂时不管)，然后对于每一点进行各个方向的 dfs。

从 matrix 的每一个 slot 出发进行回溯，知道超过 matrix 的边缘，或者当前 slot 已经被访问呢过，或者路径超过了最长单词的长度，就三种 invalid 条件。

胜利条件是当前的路径组成一个词典中的单词，但胜利条件之后应当继续回溯（统一地，对任何回溯问题，在处理完胜利条件之后都应该继续回溯，只不过很多时候胜利节点就是末节点，因此回溯下去也会因为 invalid 条件返回而已）

考虑对这个问题剪枝，可以将字典改写为 trie tree，这样在每一步查询时，可以根据当前路径序列是否是一个有效的 prefix 来进行判断，可以大幅提高搜索的效率。

Trie Tree 的代码

```java
public class Trie {
	private Node root;
	 
    public Trie(){
        root = new Node(' '); 
    }
 
    public void insert(String word){
    	if(isWordExisted(word) == true) return;
        Node current = root; 
        for(int i = 0; i < word.length(); i++){
            Node child = current.subNode(word.charAt(i));
            if(child != null){ 
                current = child;
            } else {
                 current.childList.add(new Node(word.charAt(i)));
                 current = current.subNode(word.charAt(i));
            }
            current.count++;
        } 
        // Set isEnd to indicate end of the word
        current.isEnd = true;
    }
    public boolean isWordExisted(String word){
	    Node current = root;
        
	    for(int i = 0; i < word.length(); i++){    
            if(current.subNode(word.charAt(i)) == null)
                return false;
            else
                current = current.subNode(word.charAt(i));
        }
        if (current.isEnd == true) return true;
        else return false;
    }
    
    public boolean isPrefixExisted(String word){
	    Node current = root;
	    for(int i = 0; i < word.length(); i++){    
            if(current.subNode(word.charAt(i)) == null)
                return false;
            else
                current = current.subNode(word.charAt(i));
        }
        return true;
    }
}

class Node {
    char content; // the character in the node
    boolean isEnd; // whether the end of the words
    int count;  // the number of words sharing this character
    LinkedList<Node> childList; // the child list
  
    public Node(char c){
        childList = new LinkedList<Node>();
        isEnd = false;
        content = c;
        count = 0;
    }
  
    public Node subNode(char c){
        if(childList != null){
	        for(Node eachChild : childList){
	            if(eachChild.content == c){
	                 return eachChild;
	            }
        	}
        }
        return null;
   }
}
```

然后是 Boggle Class 的代码

```java
public class Boggle {
	
	public static void main(String[] args) {
		char[][] board = {{'d', 'g', 'h', 'i'}, {'k', 'l', 'p', 's'}, {'y', 'e', 'u', 't'}, {'e', 'o', 'r', 'n'}};
		String path = "input.in";
		ArrayList<String> allWordsList = findAllValidWords(board, path);
		for (String str : allWordsList) {
			System.out.println(str);
		}
	}
	// find all the valid words in the board, and the dictionary can be found in "path"
	public static ArrayList<String> findAllValidWords(char[][] board, String path) {
		ArrayList<String> allWordsList = new ArrayList<String>();
		if (board == null || board.length == 0 || board[0].length == 0) return allWordsList;
		// trie stores the dictionary
		Trie trie = generateTrie(path);
		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board[0].length; j++) {
				boolean[][] isVisited = new boolean[board.length][board[0].length];
				helper(board, i, j, new ArrayList<Character>(), isVisited, trie, allWordsList);
			}
		}
		return allWordsList;
	}
	
	public static void helper(char[][] arr, int i, int j, ArrayList<Character> list, boolean[][] isVisited, Trie trie, ArrayList<String> allWordsList) {
		if (i < 0 || j < 0 || i >= arr.length || j >= arr[0].length || isVisited[i][j]) return;
		list.add(arr[i][j]);
		isVisited[i][j] = true;
		String word = convertToString(list);
		// the prefix doesn't exist in the dictionary
		if (!trie.isPrefixExisted(word)) {
			list.remove(list.size() - 1);
			isVisited[i][j] = false;
			return;
		}
		//satisfy the condition
		if (word.length() >= 3 && trie.isWordExisted(word)) {
			allWordsList.add(word);
		}
		//different directions
		helper(arr, i - 1, j, list, isVisited, trie, allWordsList);
		helper(arr, i - 1, j - 1, list, isVisited, trie, allWordsList);
		helper(arr, i - 1, j + 1, list, isVisited, trie, allWordsList);
		helper(arr, i, j - 1, list, isVisited, trie, allWordsList);
		helper(arr, i, j + 1, list, isVisited, trie, allWordsList);
		helper(arr, i + 1, j, list, isVisited, trie, allWordsList);
		helper(arr, i + 1, j - 1, list, isVisited, trie, allWordsList);
		helper(arr, i + 1, j + 1, list, isVisited, trie, allWordsList);
		list.remove(list.size() - 1);
		isVisited[i][j] = false;
	}
	// convert arraylist to string
	public static String convertToString(ArrayList<Character> list) {
		StringBuilder sb = new StringBuilder();
		for (Character c : list) {
			sb.append(c);
		}
		return sb.toString();
	}
	// create trie based on the dictionary 
	public static Trie generateTrie(String path) {
		Trie trie = new Trie();
		try {
			BufferedReader br = new BufferedReader(new FileReader(path));
			String strWord = "";
			while ((strWord = br.readLine()) != null) {
				trie.insert(strWord);
			}
			br.close();
		} catch (IllegalArgumentException e) {
			System.out.println(e.getMessage());
			return null;
		} catch (IOException e) {
			System.out.println(e.getMessage());
			return null;
		}
		
		return trie;
	}
}
```
---

### 停车场设计 

考察面向对象的能力。

现实中对事物的处理的方法和软件设计的面向对象的方式是非常的相似的。现在假设我们正采用面向对象的方法为停车场设计一套软件

1. 你设计的目的是什么？（即明确需求）。为了管理停车场中的空车位，还是统计停车场中各类车的种类，还是协助残障人寻找车位等等。
2. 设计中主要的对象是什么？（车，停车位，整个停车场，停车计时等等；而对这个抽象的概念还有很多的子类（轿车，卡车，残疾助动车）；停车位的同样会有残障车位的子类。）
3. 还漏掉了什么东西了吗？我们用什么方式来停车计费呢？是按时间收费还是免费？我们可以添加一个叫Permission的类用来处理不同的付费方式。Permission类的两个子类可以分别应对付费停车和免费停车。这样的话每个停车位就应该有个方法得到一个Permission对象来决定收费问题。
4. 我们这个设计中又如何来查询某辆是在停车位上？采用怎么样的方法来实现效率会高一些呢？

---

### 设计一个地铁售票机。

思考角度

1. 需要考虑的内容：所在车站，是否是换乘车站，所在线路，
2. 付款方式：刷卡还是现金，是否需要找零
3. 计价方式，是按照距离收费还是按照站点数量收费
4. 一些统计数字：例如售票总数，平均价格等等

---

### 设计address book

问要实现哪些功能。add, remove, get

思考角度：

1. 联系人需要的变量：姓名，性别，图片，地址，电话，邮件，或者自定义键值对
2. 排序方法：按照时间，按照次数，按照字母

---

### 设计 Chess Game

OOP 设计

1. 必须有一个数据结构来存储棋盘上的棋子。不同的棋子继承抽象棋子类
2. 人类玩家和AI继承玩家类
3. 白色格子和黑色格子分开存储
4. 有一个类来专门处理悔棋，就是将上一个状态存储起来
5. GameManager类专门用来存储下棋的操作（由谁在下，下的哪步棋），ChessPieceTurn 处理下棋的顺序 PositionEstimator ，PositionPotentialValue 两个类来实现AI算法（会在ComputerPlayer类中调用）

### 实现linkedlist 

LinkedList 和 ArrayList 一样，都实现了 List 接口，但其内部的数据结构有本质的不同。LinkedList 是基于链表实现的（通过名字也能区分开来），所以它的插入和删除操作比 ArrayList 更加高效。但也是由于其为基于链表的，所以随机访问的效率要比 ArrayList 差。

看一下 LinkedList 的类的定义：

	public class LinkedList<E>
	    extends AbstractSequentialList<E>
	    implements List<E>, Deque<E>, Cloneable, java.io.Serializable
	{}

LinkedList 继承自 AbstractSequenceList，实现了 List、Deque、Cloneable、java.io.Serializable 接口。AbstractSequenceList 提供了List接口骨干性的实现以减少实现 List 接口的复杂度，Deque 接口定义了双端队列的操作。

在 LinkedList 中除了本身自己的方法外，还提供了一些可以使其作为栈、队列或者双端队列的方法。这些方法可能彼此之间只是名字不同，以使得这些名字在特定的环境中显得更加合适。

**数据结构**

LinkedList 是基于链表结构实现，所以在类中包含了 first 和 last 两个指针(Node)。Node 中包含了上一个节点和下一个节点的引用，这样就构成了双向的链表。每个 Node 只能知道自己的前一个节点和后一个节点，但对于链表来说，这已经足够了。

    transient int size = 0;
    transient Node<E> first; //链表的头指针
    transient Node<E> last; //尾指针
    //存储对象的结构 Node, LinkedList的内部类
    private static class Node<E> {
        E item;
        Node<E> next; // 指向下一个节点
        Node<E> prev; //指向上一个节点

        Node(Node<E> prev, E element, Node<E> next) {
            this.item = element;
            this.next = next;
            this.prev = prev;
        }
    }

**存储**

add(E e)

该方法是在链表的 end 添加元素，其调用了自己的方法 linkLast(E e)。

该方法首先将 last 的 Node 引用指向了一个新的 Node(l)，然后根据l新建了一个 newNode，其中的元素就为要添加的 e；而后，我们让 last 指向了 newNode。接下来是自身进行维护该链表。

	/**
     * Appends the specified element to the end of this list.
     *
     * <p>This method is equivalent to {@link #addLast}.
     *
     * @param e element to be appended to this list
     * @return {@code true} (as specified by {@link Collection#add})
     */
	public boolean add(E e) {
	    linkLast(e);
	    return true;
	}
	/**
	* Links e as last element.
	*/
	void linkLast(E e) {
	    final Node<E> l = last;
	    final Node<E> newNode = new Node<>(l, e, null);
	    last = newNode;
	    if (l == null)
	        first = newNode;
	    else
	        l.next = newNode;
	    size++;
	    modCount++;
	}

add(int index, E element)

该方法是在指定 index 位置插入元素。如果 index 位置正好等于 size，则调用 linkLast(element) 将其插入末尾；否则调用 linkBefore(element, node(index))方法进行插入。该方法的实现在下面，大家可以自己仔细的分析一下。（分析链表的时候最好能够边画图边分析）

	/**
    * Inserts the specified element at the specified position in this list.
    * Shifts the element currently at that position (if any) and any
    * subsequent elements to the right (adds one to their indices).
    *
    * @param index index at which the specified element is to be inserted
    * @param element element to be inserted
    * @throws IndexOutOfBoundsException {@inheritDoc}
    */
    public void add(int index, E element) {
       checkPositionIndex(index);
       if (index == size)
           linkLast(element);
       else
           linkBefore(element, node(index));
    }
	/**
    * Inserts element e before non-null Node succ.
    */
	void linkBefore(E e, Node<E> succ) {
		// assert succ != null;
		final Node<E> pred = succ.prev;
		final Node<E> newNode = new Node<>(pred, e, succ);
		succ.prev = newNode;
		if (pred == null)
		first = newNode;
		else
		pred.next = newNode;
		size++;
		modCount++;
	}
   
LinkedList 的方法实在是太多，在这没法一一举例分析。但很多方法其实都只是在调用别的方法而已，所以建议大家将其几个最核心的添加的方法搞懂就可以了，比如 linkBefore、linkLast。其本质也就是链表之间的删除添加等。

---

### 把一个linked list里的元素两两交换。

Leetcode, swap nodes in pairs

画清楚图基本就没有问题，直接上代码

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode cur = dummy;
        while (cur.next != null && cur.next.next != null) {
            ListNode node = cur.next.next;
            cur.next.next = node.next;
            node.next = cur.next;
            cur.next = node;
            cur = node.next;
        }
        return dummy.next;
    }
}
```

---

### 在一棵binary search tree里找到小于某个值的最大元素。

1. 如果没有指向父节点的指针，那么一个简单的办法就是 中序遍历然后找到某个值的前一个值
2. 如果有指向父节点的指针，那么可以按照如下的方法来实现

分几种情况，下面画个图来表示

```
          10
        /    \ 
      /        \
     5          20
   /  \        /  \
  3    8     15    25
 / \    \      \   / 
1   4    9     17 22
```

因为我们是要找小于某个值的最大元素，那么首先这个元素一定在左边。在左边有几种情况：

1. 如果这个节点有左子树，那么我们要找的元素就是在这个左子树里最右边的元素。这里又分两种情况，一种是左子树没有右子树(例如节点25)，那么直接返回左子树就好；另一种是左子树有右子树(例如节点5,10,20)，那么就要一路往下，直到找到最右边的元素。根据这种情况，我们可以完成第一部分的程序
2. 如果这个节点没有左子树，那么就要往上找，直到这个节点在父节点的右边，例如节点8，那么就往上找，找到节点5，节点5的右子树就是8，所以可以返回节点5。另外一种可能是走到了根节点，如果走到根节点都还不符合条件，那么就直接返回 null(节点1)，不然就应该满足条件，直接返回根节点即可(节点15)。这样我们就可以写出程序

```java
Node getRightMostNode(Node n){
	if (n == null) return null;
	
	if (n.left != null){
		return rightMostNode(n.left);
	} else {
		Node q = n;
		Node x = q.parent;
		while ( x != null && x.right != q){
			q = x;
			x = x.parent;
		}
		return x;
	}
}


Node rightMostNode(Node n){
	if (n == null) return null;
	
	while(n.right != null){
		n = n.right;
	}
	return n;
}

```

---

### implement Singleton.

注意关键词修饰即可

```java
public class Singleton {
    private static final Singleton instance = new Singleton();
   
    //private constructor to avoid client applications to use constructor
    private Singleton(){}
 
    public static Singleton getInstance(){
        return instance;
    }
}
```

Lazy Initialization

```java
public class Singleton {
    private static final Singleton instance;
   
    //private constructor to avoid client applications to use constructor
    private Singleton(){}
 
    public static Singleton getInstance(){
        if (instance == null)
        	instance = new Singleton();
        return instance;
    }
}
```
---

###  @@ 找出一个Binary tree 的 deepest node

Leetcode, Maximum Depth of Binary Tree

这题要求我们求出一个二叉树最大深度，也就是从根节点到最远的叶子节点的距离。

对于这题，我们只需要递归遍历二叉树，达到一个叶子节点的时候，记录深度，我们就能得到最深的深度了。

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        int left = maxDepth(root.left);
        int right = maxDepth(root.right);
        return Math.max(left, right) + 1;
    }
}
```

---

### compress string

cc 原题，直接上代码

```java
/**
 * check the length of the new string in the first place and then build
 * the new string with stringBuilder(if needed)
 */
public static String compressString(String str){
    StringBuilder compressed = new StringBuilder(str.length());
    int count = 0;

    for (int i = 0; i < str.length(); i++){
        count++;
        if (i+1 == str.length() || str.charAt(i) != str.charAt(i+1)){
            compressed.append(str.charAt(i));
            compressed.append(count);
            count = 0;
        }
    }

    if (compressed.toString().length() >= str.length()){
        return str;
    }

    return compressed.toString();
}

public static int countLength(String str){
    int compressedLength = 0;
    int countConsecutive = 0;
    for (int i = 0; i < str.length(); i++){
        countConsecutive++;
        if (i + 1 == str.length() || str.charAt(i) != str.charAt(i+1)){
            compressedLength += 1
                    + String.valueOf(countConsecutive).length();
            countConsecutive = 0;
        }
    }

    return compressedLength;
}
```

---

### Valid 一串 id 

> 假设id从1开始，到N (N 已知)， validate 一下这串id是否是从1到N每个数字都出现，且仅出现了一次。 输入是一个array包含了这些数字，输出是true （valid）或者false （invalid）

1. 先检查数组的长度是不是 N，如果不是 N，直接返回 false
2. 然后可以使用类似 bucket sort 的方法，见到一个数字就减去1，放到相应的index里面。遇到重复的或者超出数组范围的就返回false，否则继续检查下一个index，直到所有数字通过测试，返回true。
3. 再或者可以利用等差数列求和公式求出总和，然后一个一个去减，如果为0，那么返回 true，否则返回 false。

---

### longgest common Prefix

结合 lcs 的版本，可以看做是开头必须相同的 lcs

原始的 Longest Common Prefix 

```java
public class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 0) return new String("");
        for(int i = 0;i < strs[0].length(); ++i){
            for(int j = 1;j < strs.length; ++j){
                if(i >= strs[j].length() || 
                    strs[j].charAt(i) != strs[0].charAt(i)) 
                    return strs[0].substring(0,i);
            }
        }
        return strs[0];
    }
}
```

如果是要结合 LCS，那么因为开头必须相同，所以可以在开头确定后，用去掉开头的子串来找 LCS，找 LCS 的方法是 DP

1. D[i][j] 定义为s1, s2的前i,j个字符串的最长common subsequence.
2. D[i][j] 当char i == char j， D[i - 1][j - 1] + 1
3. 当char i != char j, D[i ][j - 1], D[i - 1][j] 里取一个大的（因为最后一个不相同，所以有可能s1的最后一个字符会出现在s2的前部分里，反之亦然。

代码如下

```java
public class Solution {
    /**
     * @param A, B: Two strings.
     * @return: The length of longest common subsequence of A and B.
     */
    public int longestCommonSubsequence(String A, String B) {
        if (A == null || B == null) {
            return 0;
        }

        int lenA = A.length();
        int lenB = B.length();
        int[][] D = new int[lenA + 1][lenB + 1];

        for (int i = 0; i <= lenA; i++) {
            for (int j = 0; j <= lenB; j++) {
                if (i == 0 || j == 0) {
                    D[i][j] = 0;
                } else {
                    if (A.charAt(i - 1) == B.charAt(j - 1)) {
                        D[i][j] = D[i - 1][j - 1] + 1;
                    } else {
                        D[i][j] = Math.max(D[i - 1][j], D[i][j - 1]);
                    }
                }
            }
        }

        return D[lenA][lenB];
    }
}
```

---

### Product of Array Exclude itself

lintcode, 另一个array来存储从左到右或者是从右到左的连续product

完全可以在最终返回结果result基础上原地计算左右两半部分的积。

```java
public class Solution {
    /**
     * @param A: Given an integers array A
     * @return: A Long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
     */
    public ArrayList<Long> productExcludeItself(ArrayList<Integer> A) {
        ArrayList<Long> result = new ArrayList<Long>();
        if (A == null || A.size() == 0) {
            return result;
        }
        //leftToI = A[0] * ... * A[i-1]
        long leftToI = 1;
        result.add(leftToI);
        for (int i = 1; i < A.size(); i++) {
            leftToI *= A.get(i-1);
            result.add(leftToI);
        }
        //rightToI = A[i-1] * A[i+1] * ... * A[n-1]
        long rightToI = 1;
        result.set(A.size() - 1, result.get(A.size() - 1) * rightToI);
        for (int i = A.size()-2; i >= 0; i--) {
            rightToI *= A.get(i+1);
            result.set(i, result.get(i) * rightToI);
        }
        return result;
    }
}
```

---

### Find missing elements

> Array a has ten elements ,array b has nine elements that are from array a, find the missing one, do not use extra space

数组 A 的元素加起来，然后逐个减去 B 的元素，剩下的就是那个 missing one

---

### @@@ remove duplicated character from string without changing character order

hashset 做，如果不给用额外的空间，那么就只能一个一个找了。

```java
public String removeDups(String str){
    HashSet<Integer> charSet = new HashSet<Integer>();
    int length = str.length();
    StringBuffer sb = new StringBuffer();
    for (int i = 0; i < length; i++){
        if (!charSet.contains(str.get(i)){
            charSet.add(str.get(i));
            sb.append(str.get(i));
        }
    }
    return sb.toString();
}
```

---

### @@@ find least common ancestor

leetcode 219(Binary Search Tree) 和 220(Binary Tree)

这题首先要知道有没有指向父节点的指针，有和没有就有很大的区别，有了父指针，就不再需要根节点，而没有父指针，则必须要有根节点。我们先处理有父指针的情况：

有父指针可以简单粗暴，每次往上挪一个，然后检查是不是在另一个 node 到父节点的路上，直到根节点。

```java
Node commonAncestro(Node p, Node q){
	if (p == q) return null;
	
	Node ancestor = p;
	while (ancestor != null){
		if (isOnPath(ancester, q)){
			return ancestor;
		}
		ancestor = ancestor.parent;
	}
	return null;
}
```

当然这样比较浪费时间，比较好的方法是，从 q 一路顺着到 root，并把 node 放到一个 hashset 里，然后每次从 p 出发往上，如果在 hashset 那么就是要找的 ancestor，如果直到根节点都没有，那么就返回 null

如果没有父指针的话，那么就可以通过根节点来做文章。

我们可以用深度优先搜索，从叶子节点向上，标记子树中出现目标节点的情况。如果子树中有目标节点，标记为那个目标节点，如果没有，标记为null。显然，如果左子树、右子树都有标记，说明就已经找到最小公共祖先了。如果在根节点为p的左右子树中找p、q的公共祖先，则必定是p本身。

换个角度，可以这么想：如果一个节点左子树有两个目标节点中的一个，右子树没有，那这个节点肯定不是最小公共祖先。如果一个节点右子树有两个目标节点中的一个，左子树没有，那这个节点肯定也不是最小公共祖先。只有一个节点正好左子树有，右子树也有的时候，才是最小公共祖先。

时间 O(h) 空间 O(h) 递归栈空间

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        //发现目标节点则通过返回值标记该子树发现了某个目标结点
        if(root == null || root == p || root == q) return root;
        //查看左子树中是否有目标结点，没有为null
        TreeNode left = lowestCommonAncestor(root.left, p, q);
        //查看右子树是否有目标节点，没有为null
        TreeNode right = lowestCommonAncestor(root.right, p, q);
        //都不为空，说明做右子树都有目标结点，则公共祖先就是本身
        if(left!=null&&right!=null) return root;
        //如果发现了目标节点，则继续向上标记为该目标节点
        return left == null ? right : left;
    }
}
```

如果是 binary search tree 那么就可以利用 left < root < right 这个关系来进行判断

```java
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        TreeNode m = root;

        if(m.val > p.val && m.val < q.val){
            return m;  
        }else if(m.val>p.val && m.val > q.val){
            return lowestCommonAncestor(root.left, p, q);
        }else if(m.val<p.val && m.val < q.val){
            return lowestCommonAncestor(root.right, p, q);
        }

        return root;
    }
}
```

还有一种方法是通过中序遍历和后序遍历的方式，在后序遍历的结果中，找到中序遍历结果 p 和 q 之间的元素(包括 p q) 最后出现的那一个，就是要找的节点了。(这个不用在意是否是 search tree)

---

### @@ min stack

leetcode 原题，直接上代码

```java
class MinStack {
    private Stack<Integer> stack = new Stack<>();
    private Stack<Integer> minStack = new Stack<>();
    public void push(int x) {
      stack.push(x);
      if (minStack.isEmpty() || x <= minStack.peek()) {
         minStack.push(x);
      }
    }
    public void pop() {
      if (stack.pop().equals(minStack.peek())) minStack.pop();
    }
    public int top() {
      return stack.peek();
    }
    public int getMin() {
      return minStack.peek();
    }
}
```

---

### 斐波那奇数列

面试考了这题，先用递归，然后不用递归，分别分析复杂度

这个算法的时间复杂度有着跟Fibonacci类似的递推方程：T(n) = T(n - 1) + T(n - 2) + O(1)，很容易得到T(n) = O(1.618 ^ n)（1.618就是黄金分割，(1+√5)/2 ）。空间复杂度取决于递归的深度，显然是O(n)。

```java
int fibonacci(int n){
    if (n == 0) return 0;
    if (n == 1) return 1;

    return fibonacci(n-1) + fibonacci(n-2);
}
```

直接找两个元素缓存着前两个结果，累加即可

```java
int fibonacci(int n){
	int a = 0;
	int b = 1;
	for (int i = 2; i < n; i++) {
		int c = a + b;
		a = b;
		b = c;
	}
	return a + b;
}
```

O(n) & O(1)

---

### Container with Most water

leetcode 4.11

两头开始每次算，移动小的那个，左边往右移，右边往左移。From both sides to the center.

```java
public class Solution {
    public int maxArea(int[] height) {
        int left = 0, right = height.length - 1;
        int res = 0;
        while (left < right) {
            res = Math.max(res, 
                    Math.min(height[left],height[right]) * (right - left));
            if (height[left] > height[right]) --right;
            else ++left;
        }
        return res;
    }
}
```

---

### 反转字符串同时判断回文

根据长度来进行翻转即可，和旋转字符串的翻转方法类似，判断回文的话，就翻转之后比较一次即可。

```java
private void reverse(char[] str, int start, int end) {
   while (start < end) {
       char temp = str[start];
       str[start] = str[end];
       str[end] = temp;
       start++;
       end--;
   }
}
```

---

### binary tree 找successor的方法

和找上一个的节点刚好相反，代码如下

```java
/**
 * This is not the most algorithmically complex problem but it can be tricky
 * to code perfectly. In a problem like this, it's useful to sketch out
 * pseudocode to carefully outline the different cases.
 */
TreeNode inorderSucc(TreeNode n){
    if (n == null)
        return null;

    // Found right children -> return leftmost node of right subtree
    if (n.right != null){
        return leftMostChild(n.right);
    }
    else{
        TreeNode q = n;
        TreeNode x = q.parent;
        // Go up until we're on left instead of right
        while (x != null && x.left != q){
            q = x;
            x = x.parent;
        }
        return x;
    }
}

TreeNode leftMostChild(TreeNode n){
    if (n == null){
        return null;
    }
    while (n.left != null){
        n = n.left;
    }
    return n;
}
```

如果是 binary search tree，那么就是 leetcode 267 题

If p has a right subtree, then get its successor from there. Otherwise do a regular search from root to p but remember the node of the last left-turn and return that. Same solution as everyone, I guess, just written a bit shorter. Runtime O(h), where h is the height of the tree.

Iterative Successor

```java
public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
    if (p.right != null) {
        p = p.right;
        while (p.left != null)
            p = p.left;
        return p;
    }
    TreeNode candidate = null;
    while (root != p)
        root = (p.val > root.val) ? root.right : (candidate = root).left;
    return candidate;
}
```


Recursive Successor

```java
public TreeNode successor(TreeNode root, TreeNode p) {
  if (root == null)
    return null;

  if (root.val <= p.val) {
    return successor(root.right, p);
  } else {
    TreeNode left = successor(root.left, p);
    return (left != null) ? left : root;
  }
}
```

Recursive predecessor

```java
public TreeNode predecessor(TreeNode root, TreeNode p) {
  if (root == null)
    return null;

  if (root.val >= p.val) {
    return predecessor(root.left, p);
  } else {
    TreeNode right = predecessor(root.right, p);
    return (right != null) ? right : root;
  }
}
```

---

### pow(x,n)

leetcode 50

```java
public class Solution {
    public double myPow(double x, int n) {
        if (x < 0) return (n % 2 == 0) ? myPow(-x, n) : -myPow(-x, n);
        if (x == 0 || x == 1) return x;
        if (n < 0) return 1.0 / myPow(x,-n);
        if (n == 0) return 1.0;
        if (n == 1) return x;
        double half = myPow(x,n/2);
        if (n % 2 == 0) return half * half;
        else return x * half * half;
    }
}
```

---

### strStr()

> 判断一个String是不是另一个String的子串，是的话就返回这个子串

先来简单粗暴的办法

```java
public int strStr(String haystack, String needle) {
    if(haystack==null || needle==null)    
        return 0;
 
    if(needle.length() == 0)
        return 0;
 
    for(int i=0; i<haystack.length(); i++){
        if(i + needle.length() > haystack.length())
            return -1;
 
        int m = i;
        for(int j=0; j<needle.length(); j++){
            if(needle.charAt(j)==haystack.charAt(m)){
                if(j==needle.length()-1)
                    return i;
                m++;
            }else{
                break;
            }
 
        }    
    }   
 
    return -1;
}
```

经典的 KMP 算法，面试碰到这个那就是故意搞你一波

```java
public int strStr(String haystack, String needle) {
	if(haystack==null || needle==null)    
		return 0;
 
	int h = haystack.length();
	int n = needle.length();
 
	if (n > h)
		return -1;
	if (n == 0)
		return 0;
 
	int[] next = getNext(needle);
	int i = 0;
 
	while (i <= h - n) {
		int success = 1;
		for (int j = 0; j < n; j++) {
			if (needle.charAt(0) != haystack.charAt(i)) {
				success = 0;
				i++;
				break;
			} else if (needle.charAt(j) != haystack.charAt(i + j)) {
				success = 0;
				i = i + j - next[j - 1];
				break;
			}
		}
		if (success == 1)
			return i;
	}
 
	return -1;
}
 
//calculate KMP array
public int[] getNext(String needle) {
	int[] next = new int[needle.length()];
	next[0] = 0;
 
	for (int i = 1; i < needle.length(); i++) {
		int index = next[i - 1];
		while (index > 0 && needle.charAt(index) != needle.charAt(i)) {
			index = next[index - 1];
		}
 
		if (needle.charAt(index) == needle.charAt(i)) {
			next[i] = next[i - 1] + 1;
		} else {
			next[i] = 0;
		}
	}
 
	return next;
}
```

---

### Unique Path

leetcode 62, 63

1. Use formula C(x,t) = t!/(x!*(t-x)!) (x should be large for calculation).
2. Dynamic programming. UP(i,j) = UP(i-1,j) + UP(i,j-1).

照常 dp，代码如下

```java
// math
public int uniquePaths_1(int m, int n) {
    if (m == 1  || n == 1) return 1;
    int t = (m-1)+(n-1);
    int x = (m > n) ? (m-1) : (n-1);
    long res = 1;
    for (int i = t; i > x; i--) res *= i;
    for (int i = t-x; i > 1; i--) res /= i;
    return (int)res;
}

// dp O(n2)
public int uniquePaths_2(int m, int n) {
    if (m == 1  || n == 1) return 1;
    int[][] dp = new int[m][n];
    for (int i = 0; i < m; i++)
        dp[i][0] = 1;
    for (int j = 0; j < n; j++)
        dp[0][j] = 1;
    for (int i = 1; i < m; i++)
        for (int j = 1; j < n; j++)
            dp[i][j] = dp[i-1][j] + dp[i][j-1];
    return dp[m-1][n-1];
}

// dp O(n)
public int uniquePaths(int m, int n) {
    if (m == 1  || n == 1) return 1;
    int[] dp = new int[n];
    for (int j = 0; j < n; j++)
        dp[j] = 1;
    for (int i = 1; i < m; i++)
        for (int j = 1; j < n; j++)
            dp[j] = dp[j] + dp[j-1];
    return dp[n-1];
}
```

---

### 数组里找最大连续sum

每次新加一个数，和原来的最大和比较，如果比最大和大，更新最大和，如果比最大和小，继续加。如果新加一个数之后和小于零，那么 sum 设为 0 重新开始累加。

```java
public class Solution {
    /**
     * @param nums: A list of integers
     * @return: A integer indicate the sum of max subarray
     */
    public int maxSubArray(ArrayList<Integer> nums) {
        if (nums.size() == 0) return 0;
        int Sum = 0;
        int maxSum = nums.get(0);

        for (int i = 0; i < nums.size(); i++) {
            Sum += nums.get(i);
            maxSum = Math.max(Sum, maxSum);
            if (Sum < 0) {
                Sum = 0;
            }

        }

        return maxSum;
    }
}
```

---

### lru implementation 

> sychronization analysis (哪些方法需要 synchronize， 为什么)

```java
import java.util.LinkedHashMap;
import java.util.Map;
public class LRUCache {
    private Map<Integer, Integer> map;
    private int capacity;
    public LRUCache(int capacity) {
        this.capacity = capacity;
        map = new LinkedHashMap<Integer, Integer>(capacity + 1);
    }

    public int get(int key) {
        Integer val = map.get(key);
        if (val == null) return -1;
        map.remove(key);
        map.put(key, val);
        return val;
    }

    public void set(int key, int value) {
        map.remove(key);
        map.put(key, value);
        if (map.size() > capacity)
            map.remove(map.entrySet().iterator().next().getKey());
    }
}
```

同步这块的东西 TODO

---

### tree 的 dfs traversal

就是前序 中序 和后序，具体直接参见代码

```java
//前序遍历
//递归实现：根左右
void preOrder1(BinTree *root)
{
    if (root != NULL)
    {
        cout<<root->data<<endl;
        preOrder1(root->lchild);
        preOrder1(root->rchild);
    }
}

//非递归实现
/*注意，如前所述，我们将二叉树的每一个结点都看作根结点。因此，从整个二叉树的根结点root出发，一路向左，遇到的每一个结点都立即访问（它是根，同时也是其父亲的左子树的根，所以这个过程访问了“根和左”）并入栈，直到不能再左，转向右（这个“右”上哪找呢？当然是父亲的右儿子。父亲去哪里找呢？当然是栈里），将这个右儿子当成新的根结点重复上述过程，直到栈为空且当前根结点也为空。*/
void preOrder2(BinTree *root)
{
	stack<BinTree *> s;
	BinTree *p=root;
 	while (p!=NULL || !s.empty())
 	{
  		//一路向左
  		while (p!=NULL)
		{      
			cout<<p->data<<endl;	 //访问根结点
			s.push(p);
   			p=p->lchild;
		}
 
		//当不能再左时，开始向右
  		if (!s.empty())
  		{
   			p=s.top();//从栈里面取出根结点
   			s.pop();
   			p=p->rchild;            //作为新的根结点
  		}
 	}
 }

//中序遍历
//递归实现：左根右
void inOrder1(BinTree *root)
{
	if (root != NULL)
	{
  		inOrder1(root->lchild);
  		cout<<root->data<<endl;
  		inOrder1(root->rchild);
 	}
}

//中序遍历 
//非递归实现
/*与前序遍历类似，但是，根结点进栈时不访问（否则就成了前序遍历），根结点弹栈时才访问（左根右）。*/
void inOrder2(BinTree *root)
{
	stack<BinTree *> s;
	BinTree *p=root;
 
	while (p!=NULL || !s.empty())
	{
  		//一路向左
 		while (p!=NULL)
 		{
 			s.push(p);
 			p=p->lchild;
 		}
 
  		//当不能再左时，访问根结点，向右
  		if (!s.empty())
  		{
   			p=s.top();
   			cout<<p->data<<endl;	//在中间访问根结点
   			s.pop();
   			p=p->rchild;
  		}
	}
}

//后序遍历
//递归实现：左右根
void postOrder1(BinTree *root)
{
	if (root != NULL)
	{
		postOrder1(root->lchild);
		postOrder1(root->rchild);
		cout<<p->data<<endl;
	}
}
//顺便说一句，删除一棵二叉树，即释放一棵二叉树的内存，用后续遍历即可实现（这里的“访问”变成了delete 结点）。

//后序遍历
//非递归实现
/*对任一结点p,边一路向左边进栈，直到其左儿子为空，这时，各个根结点在栈里存放。然后依次出栈，但是此时还不能访问（否则就是中序遍历了），出栈之后以当前根节点的右儿子设置为新的根节点，重复前述过程；直到当前根节点第二次出栈（说明它的左右儿子都已被访问），然后访问此根结点（左右根）。*/
typedef struct _poNode
{
	BinTree *btnode;
	bool isFirst;
} poNode;

void postOrder2(BinTree *root)
{
	stack<poNode *> s;
	BinTree *p=root;
 
	poNode *temp;
 
	while (p!=NULL || !s.empty())
	{
 		//一路向左直到不能再左
		while (p!=NULL)
		{
			temp = (poNode *)malloc(sizeof(poNode));
			temp->btnode = p;
			temp->isFirst = True;	 //第一次进栈标记
			s.push(temp);
 
			p=p->lchild;
		}
 
		if (!s.empty())
		{
			temp = s.top();	 //此时还不能访问，否则就是中序遍历了
			s.pop();
 
			//如果是第一次进栈，那还需要再进栈一次，之后以它的右儿子为新的根结点
			if (temp->isFirst == true)
			{
				temp->isFirst = false;
				s.push(temp);
				p = temp->btnode->rchild;
 			}
			else
			{
				cout<<temp->btnode->data<<endl;	//后序访问根结点
				p = NULL;	//不要忘了这一句，因为访问过根结点之后应该直接弹栈考察上一个父结点
			}
 		}
 	}
 }
```

---

### 写hash function

在数据结构中，哈希函数是用来将一个字符串（或任何其他类型）转化为小于哈希表大小且大于等于零的整数。一个好的哈希函数可以尽可能少地产生冲突。一种广泛使用的哈希函数算法是使用数值33，假设任何字符串都是基于33的一个大整数

这题根据题意来写即可

---

### Decode Ways 

> 给一个数字，转化成字符串，有多少种可能，比如123，1=>a, 2=>b, 3=>c; 12=>l, 3=>c;  1=>a, 23=>w

类似爬楼梯问题，但要加很多限制条件。

定义数组number，number[i]意味着：字符串s[0..i-1]可以有number[i]种解码方法。

回想爬楼梯问题一样，number[i] = number[i-1] + number[i-2]

但不同的是本题有多种限制：

+ 第一：s[i-1]不能是0，如果s[i-1]是0的话，number[i]就只能等于number[i-2]
+ 第二：s[i-2,i-1]中的第一个字符不能是0，而且Integer.parseInt(s.substring(i-2,i))获得的整数必须在0到26之间。

dp. Time : O(n); Space : O(1).

```java
public class Solution {
    public int numDecodings(String s) {
        if (s.length() == 0 || s.charAt(0) == '0') return 0;
        int N = s.length();
        int f0 = 1, f1 = 1;
        for (int i = 1; i < N; ++i) {
            // 检查当前数字是不是零
            if (s.charAt(i) == '0') f1 = 0;
            // 检查当前字符和前一个字符组合在一起是否在1-26之间
            int num = s.charAt(i) - '0' + (s.charAt(i-1) - '0') * 10;
            if (num < 10 || num > 26) {
                f0 = 0;
            }
            int tmp = f1;
            f1 = f1 + f0;
            f0 = tmp;
        }
        return f1;
    }
}
```

---

### 设计一个算法比较字符串间的相似度

返回[0,1]间的一个数

open question


### 还没整理的题目

+ 印度哥哥, Code to implement a function to calculate 一个函数在一个点的导数
+ reverse a linked list. 说这个组还挺受公司重视
+ 中国哥哥, Merge k-sorted array and find top k elements in a BST. 楼主写太快了时间用了只有一半,然后他就走了,凉了楼主一个人做了快半个小时.
+ 一脸严肃的印度大妈. split a linked list. 用python写完了说我不懂Python, 再让用C++写一遍... 啥是virtual function. overloading vs overwriting
+ very very very long string找not duplicate.
+ 问了怎么存储前n个最少数据。coding是copy random pointer。. 

