# Tree and Graph

## 解题策略

对于树和图的性质，一般全局解依赖于局部解。通常可以用DFS来判断子问题的解，然后综合得到当前的全局结论。

值得注意的是，当我们在传递节点指针的时候，其实其代表的不只是这个节点本身，而是指对整个子树、子图进行操作。只要每次递归的操作对象的结构一致，我们就可以选择Divide and Conquer(事实上对于树和图总是如此，因为subgraph和subtree仍然是graph和tree结构)。实现函数递归的步骤是：首先设置函数出口，就此类问题而言，递归出口往往是node == NULL。其次，在构造递归的时候，不妨将递归调用自身的部分视为黑盒，并想象它能够完整解决子问题。以二叉树的中序遍历为例，函数的实现为：

```
void InOrderTraversal(TreeNode *root) {
    if (root == NULL) {
        return;
    }
    InOrderTraversal(root->left);
    root->print();
    InOrderTraversal(root->right);
}
```

想象递归调用的部分InOrderTraversal(root->left)／InOrderTraversal(root->right)能够完整地中序遍历一棵子树，那么根据中序遍历“按中序遍历左子树；访问根结点；按中序遍历右子树”的定义，写出上述实现就显得很自然了。

### DFS 处理树的问题

有一类关于树的问题是， 要求找出一条满足特定条件的路径 。对于这类问题，通常都是传入一个vector记录当前走过的路径(为尽可能模版化，统一记为path)，传入path的时候可以是引用，可以是值，具体见下面的分析。还需要传入另一个vector引用记录所有符合条件的path(为尽可能模版化，统一记为result)。注意， result可以用引用或指针形式，相当于一个全局变量，或者就开辟一个独立于函数的成员变量。由于path通常是vector<int> ，那么result就是vector<vector<int>>。当然，那个特定条件，也是函数的一个输入变量。

在解答此类问题的时候，通常都采用DFS来访问，利用回溯思想，直到无法继续访问再返回。值得注意的是，如果path本身是以引用(reference)的形式传入，那么需要在返回之前消除之前所做的影响(回溯)。因为传引用(Pass by reference)相当于把path也看作全局变量，对path的任何操作都会影响其他递归状态，而传值(pass by value)则不会。传引用的好处是可以减小空间开销。

### 树和其他数据结构的相互转换

这类题目要求将树的结构转化成其他数据结构，例如链表、数组等，或者反之，从数组等结构构成一棵树。前者通常是通过树的遍历，合并局部解来得到全局解，而后者则可以利用D&C的策略，递归将数据结构的两部分分别转换成子树，再合并。

### 寻找特定节点

此类题目通常会传入一个当前节点，要求找到与此节点具有一定关系的特定节点：例如前驱、后继、左／右兄弟等。

对于这类题目，首先可以了解一下常见特定节点的定义及性质。在存在指向父节点指针的情况下，通常可以由当前节点出发，向上倒推解决。如果节点没有父节点指针，一般需要从根节点出发向下搜索，搜索的过程就是DFS。

### 图的访问

关于图的问题一般有两类。一类是前面提到的关于图的基本问题，例如图的遍历、最短路径、可达性等；另一类是将问题转化成图，再通过图的遍历解决问题。第二类问题有一定的难度，但也有一些规律可循：如果题目有一个起始点和一个终止点，可以考虑看成图的最短路径问题。

## 树

### 树的概念

树(tree)是一种能够分层存储数据的重要数据结构，树中的每个元素被称为树的节点，每个节点有若干个指针指向子节点。从节点的角度来看，树是由唯一的起始节点引出的节点集合。这个起始结点称为根(root)。树中节点的子树数目称为节点的度(degree)。在面试中，关于树的面试问题非常常见，尤其是关于二叉树(binary tree)，二叉搜索树(Binary Search Tree, BST)的问题。

所谓的二叉树，是指对于树中的每个节点而言，至多有左右两个子节点，即任意节点的度小于等于2。而广义的树则没有如上限制。二叉树是最常见的树形结构。二分查找树是二叉树的一种特例，对于二分查找树的任意节点，该节点存储的数值一定比左子树的所有节点的值大比右子树的所有节点的值小“(与之完全对称的情况也是有效的：即该节点存储的数值一定比左子树的所有节点的值小比右子树的所有节点的值大)。

基于这个特性，二分查找树通常被用于维护有序数据。二分查找树查找、删除、插入的效率都会于一般的线性数据结构。事实上，对于二分查找树的操作相当于执行二分搜索，其执行效率与树的高度(depth)有关，检索任意数据的比较次数不会多于树的高度。这里需要引入高度的概念：对一棵树而言，从根节点到某个节点的路径长度称为该节点的层数(level)，根节点为第0层，非根节点的层数是其父节点的层数加1。树的高度定义为该树中层数最大的叶节点的层数加1，即相当于于从根节点到叶节点的最长路径加1。由此，对于n个数据，二分查找树应该以“尽可能小的高度存储所有数据。由于二叉树第L层至多可以存储 2^L 个节点，故树的高度应在logn量级，因此，二分查找树的搜索效率为O(logn)。

直观上看，尽可能地把二分查找树的每一层“塞满”数据可以使得搜索效率最高，但考虑到每次插入删除都需要维护二分查找树的性质，要实现这点并不容易。特别地，当二分查找树退化为一个由小到大排列的单链表(每个节点只有右孩子)，其搜索效率变为O(n)。为了解决这样的问题，人们引入平衡二叉树的概念。所谓平衡二叉树，是指一棵树的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。通过恰当的构造与调整，平衡二叉树能够保证每次插入删除之后都保持平衡性。平衡二叉树的具体实现算法包括AVL算法和红黑算法等。由于平衡二叉树的实现比较复杂，故一般面试官只会问些概念性的问题。

### 树型的概念

满二叉树(full binary tree)：如果一棵二叉树的任何结点，或者是叶节点，或者左右子树都存在，则这棵二叉树称作满二叉树。

完全二叉树(complete binary tree)：如果一棵二叉树最多只有最下面的两层节点度数可以小于2，并且最下面一层的节点都集中在该层最左边的连续位置上，则此二叉树称作完全二叉树。

### 二叉树的遍历

二叉树的常见操作包括树的遍历，即以一种特定的规律访问树中的所有节点。常见的遍历方式包括：

+ 前序遍历(Pre-order traversal)：访问根结点；按前序遍历左子树；按前序遍历右子树。
+ 中序遍历(In-order traversal)：按中序遍历左子树；访问根结点；按中序遍历右子树。特别地，对于二分查找树而言，中序遍历可以获得一个由小到大或者由大到小的有序序列。
+ 后续遍历(Post-order traversal)：按后序遍历左子树；按后序遍历右子树；访问根结点。

以上三种遍历方式都是深度优先搜索算法(depth-first search)。深度优先算法最自然的实现方式是通过递归实现，事实上，大部分树相关的面试问题都可以优先考虑递归。此外，另一个值得注意的要点是：深度优先的算法往往都可以通过使用栈数据结构将递归化为非递归实现。这里利用了栈先进后出的特性，其数据的进出顺序与递归顺序一致(请见 Stack and Queue) 。

层次遍历(Level traversal)：首先访问第0层，也就是根结点所在的层；当第i层的所有结点访问完之后，再从左至右依次访问第i+1层的各个结点。层次遍历属于广度优先搜索算法(breadth-first search)。广度优先算法往往通过队列数据结构实现。

## Trie

字典树(trie or prefix tree)是一个26叉树，用于在一个集合中检索一个字符串，或者字符串前缀。字典树的每个节点有一个指针数组代表其所有子树，其本质上是一个哈希表，因为子树所在的位置(index)本身，就代表了节点对应的字母。节点与每个兄弟具有相同的前缀，这就是trie也被称为prefix tree的原因。

假设我们要存储如下名字，年龄：

    Amy 12
    Ann 18
    Bob 30

则构成的字典树如下：

```
.                 root: level 0
a---------b       level 1
|         |  
m---n     o       level 2
|   |     |
y   n     b       level 3
|   |     |
12  18   30       level 4
```

由于Amy和Ann共享前缀a，故第二个字母m和n构成兄弟关系。

字典树以及字典树节点的原型：

```
class TrieNode {
    private:
        T mContent;
        vector<TrieNode*> mChildren;
    public:
        Node();
        ~Node();
        friend class Trie;
};
class Trie {
public:
    Trie();
    ~Trie();
    void addWord(string s);
    bool searchWord(string s);
    void deleteWord(string s);
private:
    TrieNode* root;
};
```

字典树的基本功能如下：

1) void addWord(string key, int value);

添加一个键:值对。添加时从根节点出发，如果在第i层找到了字符串的第i个字母，则沿该节点方向下降一层(注意，如果下一层存储的是数据，则视为没有找到)。否则，将第i个字母作为新的兄弟插入到第i层。将键插入完成后插入值节点。

2) bool searchWord(string key, int &value);

查找某个键是否存在，并返回值。从根节点出发，在第i层寻找字符串中第i个字母是否存在。如果是，沿着该节点方向下降一层；否则，返回false。

3) void deleteWord(string  key)

删除一个键:值对。删除时从底层向上删除节点，“直到遇到第一个有兄弟的节点(说明该节点向上都是与其他节点共享的前缀)，删除该节点。

## 堆与优先队列

通常所说的堆(Heap)是指二叉堆，从结构上说是完全二叉树，从实现上说一般用数组。以数组的下标建立父子节点关系：对于下标为i的节点，其父节点为(int)i/2，其左子节点为2i，右子节点为2i+1。堆最重要的性质是，它满足部分有序(partial order)：最大(小)堆的父节点一定大于等于(小于等于)当前节点，且堆顶元素一定是当前所有元素的最大(小)值。

堆算法的核心在于插入，删除算法如何保持堆的性质(以下讨论均以最大堆为例):

下移(shift-down)操作：下移是堆算法的核心。对于最大值堆而言，对于某个节点的下移操作相当于比较当前节点与其左右子节点的相对大小。如果当前节点小于其子节点，则将当前节点与其左右子节点中较大的子节点对换，直至操作无法进行(即当前节点大于其左右子节点)。

建堆：假设堆数组长度为n，建堆过程如下，注意这里数组的下标是从 1 开始的：

```
for i, n/2 downto 1
    do shift-down(A,i)
```

插入：将新元素插入堆的末尾，并且与父节点进行比较，如果新节点的值大于父节点，则与之交换，即上移(shift-up)，直至操作无法进行。

弹出堆顶元素：弹出堆顶元素(假设记为A[1]，堆尾元素记为A[n])并维护堆性质的过程如下：

```
output = A[1]
exchange A[1] <-> A[n]
heap size -= 1
shift-down(A,1)
return output
```

值得注意的是，堆的插入操作逐层上移，耗时O(log(n))，与二叉搜索树的插入相同。但建堆通过下移所有非叶子节点(下标n/2至1)实现，耗时O(n)，小于BST的O(nlog(n))。

通过上述描述，不难发现堆其实就是一个优先队列。对于C++，标准模版库中的priority_queue是堆的一种具体实现。

## 图

图(Graph)是节点集合的一个拓扑结构，节点之间通过边相连。图分为有向图和无向图。有向图的边具有指向性，即AB仅表示由A到B的路径，但并不意味着B可以连到A。与之对应地，无向图的每条边都表示一条双向路径。

图的数据表示方式也分为两种，即邻接表(adjacency list)和邻接矩阵(adjacency matrix)。对于节点A，A的邻接表将与A之间相连的所有节点以链表的形势存储起来，节点A为链表的头节点。这样，对于有V个节点的图而言，邻接表表示法包含V个链表。因此，链接表需要的空间复杂度为O(V+E)。邻接表适用于边数不多的稀疏图。但是，如果要确定图中边(u, v)是否存在，则只能在节点u对应的邻接表中以O(E)复杂度线性搜索。

对于有V个节点的图而言，邻接矩阵用V*V的二维矩阵形式表示一个图。矩阵中的元素Aij表示节点i到节点j之间是否直接有边相连。若有，则Aij数值为该边的权值，否则Aij数值为0。特别地，对于无向图，由于边的双向性，其邻接矩阵的转置矩阵为其本身。邻接矩阵的空间复杂度为O(V^2 )，适用于边较为密集的图。邻接矩阵在检索两个节点之间是否有边相连这样一个需求上，具有优势。

## 图的遍历

对于图的遍历(Graph Transversal)类似于树的遍历(事实上，树可以看成是图的一个特例)，也分为广度优先搜索和深度优先搜索。算法描述如下：

### 广度优先

对于某个节点，广度优先会先访问其所有邻近节点，再访问其他节点。即，对于任意节点，算法首先发现距离为d的节点，当所有距离为d的节点都被访问后，算法才会访问距离为d+1的节点。广度优先算法将每个节点着色为白，灰或黑，白色表示未被发现，灰色表示被发现，黑色表示已访问。算法利用先进先出队列来管理所有灰色节点。一句话总结，广度优先算法先访问当前节点，一旦发现未被访问的邻近节点，推入队列，以待访问。

《算法导论》第22章图的基本算法给出了广度优先的伪代码实现，引用如下：

```
BFS(G, s)
For each vertex u exept s
    Do Color[u] = WHITE
        Distance[u] = MAX
        Parent[u] = NIL
Color[s] = GRAY
Distance[s] = 0
Parent[s] = NIL
Enqueue(Q, s)
While Q not empty
    Do u = Dequeue(Q)
        For each v is the neighbor of u
            Do if Color[v] == WHITE
                Color[v] = GRAY
                Distance[v] = Distance[u] + 1
                Parent[v] = u
                Enqueue(Q, v)
            Color[u] = BLACK”
```

### 深度优先

深度优先算法尽可能“深”地搜索一个图。对于某个节点v，如果它有未搜索的边，则沿着这条边继续搜索下去，直到该路径无法发现新的节点，回溯回节点v，继续搜索它的下一条边。深度优先算法也通过着色标记节点，白色表示未被发现，灰色表示被发现，黑色表示已访问。算法通过递归实现先进后出。一句话总结，深度优先算法一旦发现没被访问过的邻近节点，则立刻递归访问它，直到所有邻近节点都被访问过了，最后访问自己。

《算法导论》第22章图的基本算法给出了深度优先的伪代码实现，引用如下：

```
DFS(G)
For each vertex v in G
    Do Color[v] = WHITE
    Parent[v] = NIL
For each vertex v in G
    DFS_Visit(v)

DFS_Visit(u)
Color[u] = GRAY
For each v is the neighbor of u
    If Color[v] == WHITE
        Parent[v] = u
        DFS_Visit(v)
Color[u] = BLACK
```

## 单源最短路径问题

对于每条边都有一个权值的图来说，单源最短路径问题是指从某个节点出发，到其他节点的最短距离。该问题的常见算法有Bellman-Ford和Dijkstra算法。前者适用于一般情况(包括存在负权值的情况，但不存在从源点可达的负权值回路)，后者仅适用于均为非负权值边的情况。Dijkstra的运行时间可以小于Bellman-Ford。本小节重点介绍Dijkstra算法。

特别地，如果每条边权值相同(无权图)，由于从源开始访问图遇到节点的最小深度 就等于到该节点的最短路径，因此 Priority Queue就退化成Queue，Dijkstra算法就退化成BFS。

Dijkstra的核心在于，构造一个节点集合S，对于S中的每一个节点，源点到该节点的最短距离已经确定。进一步地，对于不在S中的节点，“我们总是选择其中到源点最近的节点，将它加入S，并且更新其邻近节点到源点的距离。算法实现时需要依赖优先队列。一句话总结，Dijkstra算法利用贪心的思想，在剩下的节点中选取离源点最近的那个加入集合，并且更新其邻近节点到源点的距离，直至所有节点都被加入集合。关于Dijkstra算法的正确性分析，可以使用数学归纳法证明，详见《算法导论》第24章，单源最短路径。 给出伪代码如下：

```
DIJKSTRA(G, s)
S = EMPTY
Insert all vertexes into Q
While Q is not empty
    u = Q.top
    S.insert(u)
    For each v is the neighbor of u
        If d[v] > d[u] + weight(u, v)
            d[v] = d[u] + weight(u, v)
            parent[v] = u
```

## 任意两点之间的最短距离

另一个关于图常见的算法是，如何获得任意两点之间的最短距离(All-pairs shortest paths)。直观的想法是，可以对于每个节点运行Dijkstra算法，该方法可行，但更适合的算法是Floyd-Warshall算法。

Floyd算法的核心是动态编程，利用二维矩阵存储i，j之间的最短距离，矩阵的初始值为i，j之间的权值，如果i，j不直接相连，则值为正无穷。动态编程的递归式为：d(k)ij = min(d(k-1)ij, d(k-1)ik+ d(k-1)kj)  (1<= k <= n)。直观上理解，对于第k次更新，我们比较从i到j只经过节点编号小于k的中间节点(d(k-1)ij)，和从i到k，从k到j的距离之和(d(k-1)ik+ d(k-1)kj)。Floyd算法的复杂度是O(n^3)。关于Floyd算法的理论分析，请见《算法导论》第25章，每对顶点间的最短路径。 给出伪代码如下：

```
FLOYD(G)
Distance(0) = Weight(G)
For k = 1 to n
    For i = 1 to n
        For j = 1 to n
Distance(k)ij = min(Distance (k-1)ij, Distance (k-1)ik+ Distance(k-1)kj)  
Return Distance(n)
```

## 工具箱

### 二叉树类

一个最基本的二叉树类可以如下定义：

```
class TreeNode {
public:
    TreeNode *left;
    TreeNode *right;
    TreeNode *parent;
    int val;
};

class BinaryTree {
public:
    BinaryTree(int rootValue);
    ~BinaryTree();
    bool insertNodeWithValue(int value);
    bool deleteNodeWithValue(int value);
    void printTree();

private:
    TreeNode *root;
};
```

### 平衡二叉树

关于平衡二叉树的理论讨论请见：
《算法导论》(Introduction to Algorithms, 2nd Edition), Thomas H. Corman, Charles E.Leiserson, Ronald L.Rivest, Clifford Stein, 第13章，红黑树

### 二叉树的遍历

DFS Traversal: In-order traversal, pre-order and post-order of tree

```
void preOrderTraversal(TreeNode *root) {
    if (!root) {
        return;
    }
    visit(root);
    preOrderTraversal(root->left);
    preOrderTraversal(root->right);
}

void inOrderTraversal(TreeNode *root) {
    if (!root) {
        return;
    }
    inOrderTraversal(root->right);
    visit(root);
    inOrderTraversal(root->left);
}

void postOrderTraversal(TreeNode *root) {
    if (!root) {
        return;
    }
    postOrderTraversal(root->left);
    postOrderTraversal(root->right);
    visit(root);
}
```

BFS Traversal

```
void levelTraversal(TreeNode *root)
{
    queue<TreeNode *> nodeQueue;
    TreeNode *currentNode;
    if (!root) {
        return;
    }
    nodeQueue.push(root);
    while (!nodeQueue.empty()) {
        currentNode = nodeQueue.front();
        processNode(currentNode);
        if (currentNode->left) {
            nodeQueue.push(currentNode->left);
        }
        if (currentNode->right) {
            nodeQueue.push(currentNode->right);
        }
        nodeQueue.pop();
    }
}
```

### 字典数类

可以如下定义一个字典树:

```
class TrieNode {
private:
    char mContent;
    bool mMarker;
    vector<TrieNode *> mChildren;
public:
    TrieNode() {
        mContent = ' '; mMarker = false;
    }
    ~TrieNode() {
    }
    friend class Trie;
};
class Trie {
public:
    Trie();
    ~Trie();
    void addWord(string s);
    bool searchWord(string s);
    void deleteWord(string s);
private:
    TrieNode *root;
};
```

### 堆的重要函数

《算法导论》(Introduction to Algorithms, 2nd Edition), Thomas H. Corman, Charles E.Leiserson, Ronald L.Rivest, Clifford Stein, 第6章，堆排序

### priority_queue

`priority_queue`在C++标准模版库(Standard Template Library, STL)中实现，使用时需要`include<priority_queue>`。 简要介绍如下常见函数，更多信息请参考[这里](http://www.cplusplus.com/reference/queue/priority_queue/)：

```
// Returns whether the priority queue is empty: i.e. whether its size is zero.
bool empty() const;    

// Inserts a new element in the priority queue, effectively increasing its size by one.
void push (const value_type& val);    

Example:
priority_queue<int> myPriorityQueue;
myPriorityQueue.push(20);
myPriorityQueue.push(50);
myPriorityQueue.push(30);    // queue contains 3 elements, will be accessed in the order of 50, 30, 20

// Removes the element on top of the priority queue, effectively reducing its size by one.
void pop();

// Returns a constant reference to the top element in the priority queue.
const value_type& top() const;    

Example:
priority_queue<int> myPriorityQueue;
myPriorityQueue.push(30);
myPriorityQueue.push(10);
myPriorityQueue.push(50);
myPriorityQueue.push(40);

cout << "Popping out elements...";
while (!myPriorityQueue.empty()) {
    cout << ' ' << myPriorityQueue.top();
    myPriorityQueue.pop();
}
cout << endl;// output: Popping out elements... 50 40 30 10
```

