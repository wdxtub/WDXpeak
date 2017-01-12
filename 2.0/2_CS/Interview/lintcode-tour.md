# LintCode 思路及个人想法

用 python/java 来进行解答

## @ 要注意的知识点

- lambda 表达式
- xrange
- 递归

## ---- 容易题 ----

这一部分是容易题

## @@ O(1)检测2的幂次 

用 O(1) 时间检测整数 n 是否是 2 的幂次。

样例

    n=4，返回 true;
    n=5，返回 false.

注意

    O(1) 时间复杂度

**题解**

注意因为对时间复杂度有要求，所以必须利用位操作来进行判断。注意一些边界情况，例如是负数或者是0,1 之类的，需要分别处理。



```python
class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        # write your code here
        if n < 0:
            return False
        elif n == 1:
            return True
        elif n == 0:
            return False
        elif (n & n - 1) == 0:
            return True
        return False


```

---

## @@ x的平方根

实现 `int sqrt(int x)` 函数，计算并返回 x 的平方根。

样例

    sqrt(3) = 1
    sqrt(4) = 2
    sqrt(5) = 2
    sqrt(10) = 3

挑战

    O(log(x))

**题解**

用枚举的办法会超时以及超过时间限制，所以必须使用二分来进行查找和判断，注意二分的写法


```python
class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        # write your code here
        low = 0
        high = x
        while low <= high:
            mid = low + (high - low) / 2
            square = mid * mid
            lsquare = (mid-1)*(mid-1)
            hsquare = (mid+1)*(mid+1)

            if square == x:
                return mid
            if lsquare <= x and square > x:
                return mid - 1
            if square < x and hsquare > x:
                return mid
            if square < x:
                low = mid + 1
            else:
                high = mid - 1
```

---

## @@ 不同的路径

有一个机器人的位于一个M×N个网格左上角。

机器人每一时刻只能向下或者向右移动一步。机器人试图达到网格的右下角（下图中标记为'Finish'）。

问有多少条不同的路径？

注意

    n和m均不超过100

**题解**

这个和之前语音识别做编辑距离有点类似，本质就是一个矩阵的递推：当前位置的值等于左边和上边的值相加，然后循环处理即可



```python
class Solution:
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        result = [1] * n
        if m == 1:
            return result[-1]
        for i in range(1,m):
            for j in range(1,n):
                result[j] = result[j] + result[j-1]
        return result[-1]
```

---

## @@ 不同的路径 II

跟进“不同的路径”：

现在考虑网格中有障碍物，那样将会有多少条不同的路径？

网格中的障碍和空位置分别用1和0来表示。

样例

如下所示在3x3的网格中有一个障碍物：

    [
    [0,0,0],
    [0,1,0],
    [0,0,0]
    ]

一共有2条不同的路径从左上角到右下角。

注意

m和n均不超过100

**题解**

这里需要注意的是处理有障碍物时的情况，即直接表示为零，然后按照同样的方式进行累加。而因为要从第一个元素进行处理，所以需要注意如果还是用 `result[j] = result[j] + result[j-1]` 在 `j==0` 时会出现 `result[-1]` 的情况，就不符合题目意思了，所以在边界需要特别处理一下



```python
class Solution:
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        result = [1] * n
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                for j in range(i, n):
                    result[j] = 0

        for i in range(1, m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    result[j] = 0
                elif j != 0:
                    result[j] = result[j] + result[j-1]

        return result[-1]
```

---

## @@ 两个字符串是变位词

写出一个函数 anagram(s, t) 去判断两个字符串是否是颠倒字母顺序构成的

样例

    给出 s="abcd"，t="dcab"，返回 true

**题解**

分别对两个字符串排序，然后比较即可，注意在 python 中字符串是没有办法修改的，所以需要转换成 list 然后进行处理



```python
class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        # write your code here
        ls = list(s)
        lt = list(t)
        ls.sort()
        lt.sort()
        s = "".join(ls)
        t = "".join(lt)

        if s == t:
            return True
        return False
```

---

## @@ 两个链表的和

你有两个用链表代表的整数，其中每个节点包含一个数字。数字存储按照在原来整数中相反的顺序，使得第一个数字位于链表的开头。写出一个函数将两个整数相加，用链表形式返回和。

样例

给出两个链表 `3->1->5->null` 和 `5->9->2->null` ，返回 8->0->8->null

**题解**

注意进位，按照规则加即可。这里有一个技巧，因为两个数字相加的和肯定不超过二十，也就是进位的可能只有 1 或者 0，所以就不需要用 `ans / 10` 这种开销较大的运算方式，直接判断是否大于等于 10 来确定进位的数字即可，这样时间可以从 512ms 缩短至 345 ms



```python
"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2
    def addLists(self, l1, l2):
        # write your code here
        if l1 == None and l2 != None:
            return l2
        elif l1 != None and l2 == None:
            return l1
        elif l1 == None and l2 == None:
            return None

        head = ListNode(0)
        prehead = head
        addit = 0

        while l1 != None and l2 != None:
            head.next = ListNode((l1.val + l2.val + addit) % 10)
            if l1.val + l2.val + addit >= 10:
                addit = 1
            else:
                addit = 0
            l1 = l1.next
            l2 = l2.next
            head = head.next

        if l1 != None:
            while l1 != None:
                head.next = ListNode((l1.val + addit) % 10)
                if l1.val + addit >= 10:
                    addit = 1
                else:
                    addit = 0
                l1 = l1.next
                head = head.next
        else:
            while l2 != None:
                head.next = ListNode((l2.val + addit) % 10)
                if l2.val + addit >= 10:
                    addit = 1
                else:
                    addit = 0
                l2 = l2.next
                head = head.next

        if l1 == None and l2 == None and addit > 0:
            head.next = ListNode(addit)

        return prehead.next

```

---

## @@ 中位数

给定一个未排序的整数数组，找到其中位数。

中位数是排序后数组的中间值，如果数组的个数是偶数个，则返回排序后数组的第N/2个数。

样例

    给出数组[4, 5, 1, 2, 3]， 返回 3
    给出数组[7, 9, 4, 5]，返回 5

挑战

    时间复杂度为O(n)

**题解**

这一题比较简单，就是判断一个奇偶性，然后排序即可，注意下标是从零开始的



```python
class Solution:
    """
    @param nums: A list of integers.
    @return: An integer denotes the middle number of the array.
    """
    def median(self, nums):
        # write your code here
        l = len(nums)
        nums.sort()

        if l % 2 == 0:
            return nums[l / 2 - 1]
        else:
            return nums[l / 2]
```

---

## @@ 主元素

给定一个整型数组，找出主元素，它在数组中的出现次数严格大于数组元素个数的二分之一。

样例

    给出数组[1,1,1,1,2,2,2]，返回 1

挑战

    要求时间复杂度为O(n)，空间复杂度为O(1)

**题解**

逐个标记，一旦遇到不同的，计数减一，否则加一，计数为零时，更换答案。因为一定大于二分之一，所以可以保证最后留下来的就是那个主元素



```python
class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        count = 0
        ans = 0
        for i in nums:
            if count == 0:
                ans = i
                count = count + 1
            elif count > 0 and ans == i:
                count = count + 1
            elif count > 0 and ans != i:
                count = count - 1

        return ans
```

---

## @@ 二分查找

给定一个排序的整数数组（升序）和一个要查找的整数 `target`，用`O(logn)`的时间查找到`target`第一次出现的下标（从0开始），如果`target`不存在于数组中，返回`-1`。

**题解**

标准的二分，注意如果找到之后，需要顺着往前再找相同的，以确定第一个出现的下标



```python
class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0
    def binarySearch(self, nums, target):
        # write your code here
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if nums[mid] == target:
                while nums[mid] == target:
                    mid = mid - 1
                return mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1
```

---

## @@ 二叉树的中序遍历

给出一棵二叉树,返回其中序遍历

样例

给出二叉树 {1,#,2,3},

    1
     \
      2
     /
    3

返回 [1,3,2].

挑战

你能使用非递归算法来实现么?

**题解**

若二叉树为空，则不进行任何操作：否则

1. 中序遍历左子树。
2. 访问根结点。
3. 中序遍历右子树

非递归的话，则需要麻烦很多，注意入栈出栈的顺序和限制规则。我们采用「左根右」的访问顺序主要由如下四步构成：

1. 首先需要一直对左子树迭代并将非空节点入栈
2. 节点指针为空后不再入栈
3. 当前节点为空时进行出栈操作，并访问栈顶节点
4. 将当前指针p用其右子节点替代

步骤2,3,4对应「左根右」的遍历结构，只是此时的步骤2取的左值为空。



先是递归版本，比较简单粗暴

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        if root is None:
            return []
        else:
            return self.inorderTraversal(root.left) + [root.val] +  self.inorderTraversal(root.right)

```

迭代版本

```python

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        result = []
        s = []
        while root is not None or s:
            if root is not None:
                s.append(root)
                root = root.left
            else:
                root = s.pop()
                result.append(root.val)
                root = root.right

        return result

```

---

## @@ 二叉树的前序遍历

给出一棵二叉树，返回其节点值的前序遍历。

样例

给出二叉树 {1,#,2,3},

    1
     \
      2
     /
    3

返回 [1,2,3].

挑战

你能使用非递归实现么？

**题解**

若二叉树为空，则不进行任何操作：否则

1. 访问根结点。
2. 先序方式遍历左子树。
3. 先序遍历右子树。

迭代时需要利用栈来保存遍历到的节点，纸上画图分析后发现应首先进行出栈抛出当前节点，保存当前节点的值，随后将右、左节点分别入栈(注意入栈顺序，先右后左)，迭代到其为叶子节点(NULL)为止。



先是递归版本，比较简单粗暴

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        if root is None:
            return []
        else:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

```

迭代版本

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # write your code here
        if root is None:
            return []

        result = []
        s = []
        s.append(root)
        while s:
            root = s.pop()
            result.append(root.val)
            if root.right is not None:
                s.append(root.right)
            if root.left is not None:
                s.append(root.left)

        return result

```

---

## @@ 二叉树的后序遍历

给出一棵二叉树，返回其节点值的后序遍历。

样例

给出二叉树 {1,#,2,3},

    1
     \
      2
     /
    3

返回 [3,2,1]

挑战

你能使用非递归实现么？

**题解**

若二叉树为空，则不进行任何操作：否则

1. 后序遍历左子树。
2. 后序遍历右子树。
3. 访问根结点。

使用递归写后序遍历那是相当的简单，我们来个不使用递归的迭代版。整体思路仍然为「左右根」，那么怎么才能知道什么时候该访问根节点呢？问题即转化为如何保证左右子节点一定先被访问到？由于入栈之后左右节点已无法区分，因此需要区分左右子节点是否被访问过(加入到最终返回结果中)。除了有左右节点的情况，根节点也可能没有任何子节点，此时也可直接将其值加入到最终返回结果中。



先是递归版本，比较简单粗暴

```python

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        if root is None:
            return []
        else:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

```

递归版本

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        result = []
        if root is None:
            return result
        s = []
        # previously traversed node
        prev = None
        s.append(root)
        while s:
            curr = s[-1]
            noChild = curr.left is None and curr.right is None
            childVisited = (prev is not None) and \
                           (curr.left == prev or curr.right == prev)
            if noChild or childVisited:
                result.append(curr.val)
                s.pop()
                prev = curr
            else:
                if curr.right is not None:
                    s.append(curr.right)
                if curr.left is not None:
                    s.append(curr.left)

        return result
```

---

## @@ 二叉树的最大深度

给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的距离。

样例

给出一棵如下的二叉树:

      1
     / \
    2   3
       / \
      4   5

这个二叉树的最大深度为3.

**题解**

这里先整一个递归的，就是逐层遍历，深度优先



```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxDepth(self, root):
        # write your code here
        if root is None:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        if left < right:
            return right + 1
        else:
            return left + 1

```

---


## @@ 二叉树的最小深度

给定一个二叉树，找出其最小深度。

二叉树的最小深度为根节点到最近叶子节点的距离。

样例

给出一棵如下的二叉树:

       1
     /   \
    2     3
        /   \
       4     5

这个二叉树的最小深度为 2

**题解**

与上面的类似，找到没有左右节点的节点就停手，然后返回当时的深度即可，也属于深度优先搜索



```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def minDepth(self, root):
        # write your code here
        if root is None:
            return 0

        return self.getMin(root)

    def getMin(self, node):
        if node is None:
            return 99999

        if node.left is None and node.right is None:
            return 1

        return min(self.getMin(node.left), self.getMin(node.right)) + 1

```

---

## @@ 二进制中有多少个1

计算在一个 32 位的整数的二进制表式中有多少个 1.

样例

    给定 32 (100000)，返回 1
    给定 5 (101)，返回 2
    给定 1023 (111111111)，返回 9

**题解**

直接一直除2，看看有多少个1即可



```python
class Solution:
    # @param num: an integer
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        # write your code here
        count = 0
        while num > 0:
            if num % 2 != 0:
                count = count + 1
                num = (num-1) / 2
            else:
                num = num / 2
        return count
```

---

## @@ 二进制求和

给定两个二进制字符串，返回他们的和（用二进制表示）。

样例

    a = 11
    b = 1
    返回 100

**题解**

超级简单粗暴的办法，先把两个字符串翻转，然后对应一位一位加，然后结果最后翻转回来即可，注意 string 与 list 类型的转换



```python
class Solution:
    # @param {string} a a number
    # @param {string} b a number
    # @return {string} the result
    def addBinary(self, a, b):
        # Write your code here
        la = len(a)
        lb = len(b)
        anslist = []
        addit = 0

        a = a[::-1] # 这个翻转字符串的技巧特别靠谱
        b = b[::-1]

        if lb > la:
            a, b = b, a
            lb, la = la, lb

        for i in range(lb):
            if a[i] == '1' and b[i] == '1':
                if addit == 1:
                    addit = 1
                    anslist.append('1')
                else:
                    addit = 1
                    anslist.append('0')
            elif (a[i] == '0' and b[i] == '1') or (a[i] == '1' and b[i] == '0'):
                if addit == 0:
                    addit = 0
                    anslist.append('1')
                else:
                    addit = 1
                    anslist.append('0')
            elif a[i] == '0' and b[i] == '0':
                if addit == 0:
                    addit = 0
                    anslist.append('0')
                else:
                    addit = 0
                    anslist.append('1')
        for i in range(lb, la):
            if addit == 1 and a[i] == '1':
                addit = 1
                anslist.append('0')
            elif addit == 1 and a[i] == '0':
                addit = 0
                anslist.append('1')
            else:
                anslist.append(a[i])

        if addit == 1:
            anslist.append('1')

        anslist.reverse()
        return ''.join(anslist)

```

---

## @@ 删除元素

给定一个数组和一个值，在原地删除与值相同的数字，返回新数组的长度。

元素的顺序可以改变，并且对新的数组不会有影响。

样例

    给出一个数组 [0,4,4,0,0,2,4,4]，和值 4
    返回 4 并且4个元素的新数组为[0,0,0,2]

**题解**

利用 python 的特性可以快速删除，注意下标的范围会变化，所以找一个值来记录之后遍历时对应到正确的元素即可

```python
class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        # write your code here
        dc = 0
        for i in range(len(A)):
            if A[i-dc] == elem:
                A.remove(elem)
                dc = dc + 1
        return A

```

C++ 版本1 - 使用容器

遍历容器内元素，若元素值与给定删除值相等，删除当前元素并往后继续遍历。

```cpp
class Solution {
public:
    /**
     *@param A: A list of integers
     *@param elem: An integer
     *@return: The new length after remove
     */
    int removeElement(vector<int> &A, int elem) {
        // write your code here
        for (vector<int>::iterator iter = A.begin(); iter < A.end(); ++iter){
            if (*iter == elem){
                iter = A.erase(iter);
                --iter;
            }
        }
        return A.size();
    }
};

```

注意在遍历容器内元素和指定欲删除值相等时，需要先自减`--iter`, 因为`for`循环会对`iter`自增，`A.erase()`删除当前元素值并返回指向下一个元素的指针，一增一减正好平衡。如果改用`while`循环，则需注意访问数组时是否越界。

C++ 版本2 - 两根指针

由于题中明确暗示元素的顺序可变，且新长度后的元素不用理会。我们可以使用两根指针分别往前往后遍历，头指针用于指示当前遍历的元素位置，尾指针则用于在当前元素与欲删除值相等时替换当前元素，两根指针相遇时返回尾指针索引——即删除元素后「新数组」的长度。

```cpp
public:
    int removeElement(int A[], int n, int elem) {
        for (int i = 0; i < n; ++i) {
            if (A[i] == elem) {
                A[i] = A[n - 1];
                --i;
                --n;
            }
        }

        return n;
    }
};
```
遍历当前数组，A[i] == elem时将数组「尾部(以 n 为长度时的尾部)」元素赋给当前遍历的元素。同时自减i和n，原因见题解1的分析。需要注意的是n在遍历过程中可能会变化。

---

## @@ 删除排序数组中的重复数字

给定一个排序数组，在原数组中删除重复出现的数字，使得每个元素只出现一次，并且返回新的数组的长度。

不要使用额外的数组空间，必须在原地没有额外空间的条件下完成。

样例

给出数组A =[1,1,2]，你的函数应该返回长度2，此时A=[1,2]。

**题解**

与上题类似，如果需要删除的话则需要给删除计数，然后对应即可，注意下标的正确性



```python
class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        dc = 0
        for i in range(len(A)-1):
            if A[i-dc] == A[i-dc+1]:
                A.remove(A[i-dc])
                dc = dc + 1
        return len(A)
```

---

## @@ 删除排序数组中的重复数字 II

跟进“删除重复数字”：

如果可以允许出现两次重复将如何处理？

样例

    给出数组A =[1,1,1,2,2,3]，你的函数应该返回长度5，此时A=[1,1,2,2,3]

**题解**

就是需要多加一个计数器，以及状态改变之后的值恢复，其他的和上面那题差不多，注意用 `len(A)` 的时候需要 `-1`才是正确的下标值



```python
class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        # write your code here
        count = 0
        dc = 0
        for i in range(len(A)-1):
            if count == 0:
                if A[i-dc] == A[i-dc+1]:
                    count = count + 1
            elif count == 1:
                if A[i-dc] == A[i-dc+1]:
                    A.remove(A[i-dc])
                    dc = dc + 1
                else:
                    count = 0
        return len(A)

```

---

## @@ 删除排序链表中的重复元素

给定一个排序链表，删除所有重复的元素每个元素只留下一个。

样例

    给出1->1->2->null，返回 1->2->null
    给出1->1->2->3->3->null，返回 1->2->3->null

**题解**

遍历之，遇到当前节点和下一节点的值相同时，删除下一节点，并将当前节点next值指向下一个节点的next, 当前节点首先保持不变，直到相邻节点的值不等时才移动到下一节点。



```python
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        # write your code here
        if head is None:
            return None

        node = head
        while node.next is not None:
            if node.val == node.next.val:
                node.next = node.next.next
            else:
                node = node.next

        return head
```

---

## @@ 删除链表中倒数第n个节点

给定一个链表，删除链表中倒数第n个节点，返回链表的头节点。

样例

    给出链表1->2->3->4->5->null和 n = 2.
    删除倒数第二个节点之后，这个链表将变成1->2->3->5->null.

注意

    链表中的节点个数大于等于n

挑战

    O(n)时间复杂度

**题解**

简单题， 使用快慢指针解决此题，需要注意最后删除的是否为头节点。让快指针先走n步，直至快指针走到终点，找到需要删除节点之前的一个节点，改变node->next域即可。



```python
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        # write your code here
        if head is None or n < 0:
            return None

        preN = head
        tail = head
        # slow fast pointer
        for i in range(n):
            if tail is None:
                return None
            tail = tail.next

        if tail is None:
            return head.next

        while tail.next:
            tail = tail.next
            preN = preN.next

        preN.next = preN.next.next
        return head;
```

---

## @@ 判断字符串是否没有重复字符

实现一个算法确定字符串中的字符是否均唯一出现

样例

    给出"abc"，返回 true
    给出"aab"，返回 false

挑战

    如果不使用额外的存储空间，你的算法该如何改变？

**题解**

用额外空间的话，一个 hash 表就可以快速完成，如果不用的话，那就只能简单粗暴的枚举找一次了



```python
class Solution:
    # @param s: a string
    # @return: a boolean
    def isUnique(self, str):
        # write your code here
        for i in range(len(str)-1):
            for j in range(i+1, len(str)-1):
                if str[i] == str[j]:
                    return False
        return True
```

---

## @@ 合并排序数组

合并两个排序的整数数组A和B变成一个新的数组。

样例

    给出A=[1,2,3,4]，B=[2,4,5,6]，返回 [1,2,2,3,4,4,5,6]

挑战

    你能否优化你的算法，如果其中一个数组很大而另一个数组很小？

**题解**

自尾部向首部逐个比较两个数组内的元素，取较大的置于新数组尾部元素中。用 python 的话可以非常简单粗暴，直接正着弄就行，注意数组长度的差异可能导致的越界



```python
class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        # write your code here
        ai = 0
        bi = 0
        c = []
        for i in range(len(A)+len(B)):
            if ai < len(A) and bi < len(B):
                if A[ai] < B[bi]:
                    c.append(A[ai])
                    ai = ai + 1
                else:
                    c.append(B[bi])
                    bi = bi + 1
            elif ai < len(A) and bi >= len(B):
                c.append(A[ai])
                ai = ai + 1
            elif ai >= len(A) and bi < len(B):
                c.append(B[bi])
                bi = bi + 1
        return c
```

---

## @@ 合并排序数组 II

合并两个排序的整数数组A和B变成一个新的数组。

样例

    给出A = [1, 2, 3, empty, empty] B = [4,5]
    合并之后A将变成[1,2,3,4,5]

注意

    你可以假设A具有足够的空间（A数组的大小大于或等于m+n）去添加B中的元素。

**题解**

在上题的基础上加入了in-place的限制。将上题的新数组视为length相对较大的数组即可，仍然从数组末尾进行归并，取出较大的元素。



```python
class Solution:
    """
    @param A: sorted integer array A which has m elements,
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        # resize nums1 to required size
        A += [0] * (n + m - len(A))
        index = m + n
        while m > 0 and n > 0:
            if A[m - 1] > B[n - 1]:
                index -= 1
                m -= 1
                A[index] = A[m]
            else:
                index -= 1
                n -= 1
                A[index] = B[n]

        while n > 0:
            index -= 1
            n -= 1
            A[index] = B[n]


```

---


## @@ 合并两个排序链表

将两个排序链表合并为一个新的排序链表

样例

    给出 1->3->8->11->15->null，2->null， 返回 1->2->3->8->11->15->null。

**题解**

此题为两个链表的合并，合并后的表头节点不一定，故应联想到使用dummy节点。链表节点的插入主要涉及节点next指针值的改变，两个链表的合并操作则涉及到两个节点的next值变化，若每次合并一个节点都要改变两个节点next的值且要对NULL指针做异常处理，势必会异常麻烦。嗯，第一次做这个题时我就是这么想的... 下面看看相对较好的思路。

首先dummy节点还是必须要用到，除了dummy节点外还引入一个lastNode节点充当下一次合并时的头节点。在l1或者l2的某一个节点为空指针NULL时，退出while循环，并将非空链表的头部链接到lastNode->next中。



```python
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        dummy = ListNode(0)
        lastNode = dummy
        while (l1 != None) and (l2 != None):
            if l1.val < l2.val:
                lastNode.next = l1
                l1 = l1.next
            else:
                lastNode.next = l2
                l2 = l2.next

            lastNode = lastNode.next

        if l1 != None:
            lastNode.next = l1
        else:
            lastNode.next = l2

        return dummy.next

```

源码分析

1. 异常处理，包含在dummy->next中。
2. 引入dummy和lastNode节点，此时lastNode指向的节点为dummy
3. 对非空l1,l2循环处理，将l1/l2的较小者链接到lastNode->next，往后递推lastNode
4. 最后处理l1/l2中某一链表为空退出while循环，将非空链表头链接到lastNode->next
5. 返回dummy->next，即最终的首指针

注意lastNode的递推并不影响dummy->next的值，因为lastNode和dummy是两个不同的指针变量。

链表的合并为常用操作，务必非常熟练，以上的模板非常精炼，有两个地方需要记牢。

1. 循环结束条件中为条件与操作；
2. 最后处理lastNode->next指针的值。

---

## @@ 合并区间

给出若干闭合区间，合并所有重叠的部分。

样例

    给出的区间列表 => 合并后的区间列表：
    [                     [
      [1, 3],               [1, 6],
      [2, 6],      =>       [8, 10],
      [8, 10],              [15, 18]
      [15, 18]            ]
    ]

挑战

    O(n log n) 的时间和 O(1) 的额外空间。

**题解**

To check the intersections between interval [a,b] and [c,d],  there are four cases (equal not shown in the figures):

        a____b
    c____d

    a____b
         c____d

    a_______b
        c___d

       a___b
    c_______d

But we can simplify these into 2 cases when check the smaller (smaller start point) interval with the bigger interval.

For the problem, the idea is simple. First sort the vector according to the start value. Second, scan every interval, if it can be merged to the previous one, then merge them, else push it into the result vector.




```python


"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        # write your code here
        res = []    # result list

        if len(intervals)==0:
            return res

        #sort list according to the start value
        intervals.sort(key=lambda x:x.start)

        res.append(intervals[0])

        #scan the list
        for i in xrange(1,len(intervals)):
            cur = intervals[i]
            pre = res[-1]
            #check if current interval intersects with previous one
            if cur.start <= pre.end:
                res[-1].end = max(pre.end, cur.end) #merge
            else:
                res.append(cur) #insert

        return res
```

---


## @@ 加一

给定一个非负数，表示一个数字数组，在该数的基础上+1，返回一个新的数组。

该数字按照大小进行排列，最大的数在列表的最前面。

**题解**

先翻转，然后逐个加，最后再翻转，注意最后的进位



```python
class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        # Write your code here
        l = len(digits)
        addit = 1
        digits.reverse()
        ans = []
        for i in range(l):
            if digits[i] + addit == 10:
                ans.append(0)
                addit = 1
            else:
                ans.append(digits[i] + addit)
                addit = 0
        if addit == 1:
            ans.append(1)
        ans.reverse()
        return ans

```

---


## @@ 哈希函数

在数据结构中，哈希函数是用来将一个字符串（或任何其他类型）转化为小于哈希表大小且大于等于零的整数。一个好的哈希函数可以尽可能少地产生冲突。一种广泛使用的哈希函数算法是使用数值33，假设任何字符串都是基于33的一个大整数，比如：

    hashcode("abcd") = (ascii(a) * 333 + ascii(b) * 332 + ascii(c) *33 + ascii(d)) % HASH_SIZE
    = (97* 333 + 98 * 332 + 99 * 33 +100) % HASH_SIZE
    = 3595978 % HASH_SIZE
    其中HASH_SIZE表示哈希表的大小(可以假设一个哈希表就是一个索引0 ~ HASH_SIZE-1的数组)。

给出一个字符串作为key和一个哈希表的大小，返回这个字符串的哈希值。

样例

    对于key="abcd" 并且 size=100， 返回 78

注意

    对于这个问题你不需要自己设计hash算法，你只需要实现上述描述的hash算法即可。

**题解**

根据题意来写即可，用 python 的话不需要担心溢出的问题



```python
class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        w = 1
        ret = 0
        for i in xrange(len(key)-1, -1, -1):
            ret = (ret+ord(key[i])*w)%HASH_SIZE
            w = (w*33)%HASH_SIZE
        return ret

```

---

## @@ 颠倒整数

将一个整数中的数字进行颠倒，当颠倒后的整数溢出时，返回 0 (标记为 32 位整数)。

样例

    给定 x = 123，返回 321
    给定 x = -123，返回 -321

**题解**

注意溢出即可



```python
class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        # Write your code here
        res = 0
        if n >= 0:
            pos = True
        else:
            pos  = False
            n = -n
        while not n == 0:
            if res > 214748364:
                return 0
            else:
                res = res*10 + n%10
                n = n/10
        if pos:
            return res
        else:
            return -res

```

---

## @@ 空格替换

设计一种方法，将一个字符串中的所有空格替换成 %20 。你可以假设该字符串有足够的空间来加入新的字符，且你得到的是“真实的”字符长度。

样例

    对于字符串"Mr John Smith", 长度为 13
    替换空格之后的结果为"Mr%20John%20Smith"

注意

    如果使用 Java 或 Python, 程序中请用字符数组表示字符串。

挑战

    在原字符串(字符数组)中完成替换，不使用额外空间

**题解**

主要就是数组操作，注意即可



```python
class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        # Write your code here
        i = 0
        while i < length:
            if string[i] == " ":
                string.append("")
                string.append("")
                length += 2
                for j in xrange(length-1, i, -1):
                    string[j] = string[j-2]

                string[i:i+3] = list("%20")
                i += 2
            i += 1

        return length

```

---

## @@ 斐波纳契数列

查找斐波纳契数列中第 N 个数。

所谓的斐波纳契数列是指：

+ 前2个数是 0 和 1 。
+ 第 i 个数是第 i-1 个数和第i-2 个数的和。

斐波纳契数列的前10个数字是：0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...

样例

    给定 1，返回 0
    给定 2，返回 1
    给定 10，返回 34

**题解**

这题利用 lambda 表达式可以有非常间接的代码



lambda 表达式版本

```python
f = lambda n: reduce(lambda x, n: [x[1], x[0]+x[1]], range(n), [0, 1])[0]  # reduce(func, itr, accumulator)
        return f(n-1)
```

普通版本

```python

```


---

## @@ 搜索二维矩阵

写出一个高效的算法来搜索 m × n矩阵中的值。

这个矩阵具有以下特性：

+ 每行中的整数从左到右是排序的。
+ 每行的第一个数大于上一行的最后一个整数。

样例

考虑下列矩阵：

    [
      [1, 3, 5, 7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    给出 target = 3，返回 true

挑战

    O(log(n) + log(m)) 时间复杂度

**题解**

二分确定在哪一行，然后再二分确定是哪一个

一次二分搜索: 由于矩阵按升序排列，因此可将二维矩阵转换为一维问题。对原始的二分搜索进行适当改变即可(求行和列)。

两次二分搜索: 先按行再按列进行搜索，即两次二分搜索。时间复杂度相同。



```python
class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if len(matrix) == 0:
            return False

        low, high = 0, len(matrix)*len(matrix[0])-1
        while(low<=high):
            m = low + ((high-low)>>1)
            v = matrix[m / len(matrix[0])][m % len(matrix[0])]
            if v < target:
                low = m + 1
            elif v > target:
                high = m-1
            elif v == target:
                return True
        return False


```

---

## @@ 报数

报数指的是，按照其中的整数的顺序进行报数，然后得到下一个数。如下所示：

1, 11, 21, 1211, 111221, ...

+ 1 读作 "one 1" -> 11.
+ 11 读作 "two 1s" -> 21.
+ 21 读作 "one 2, then one 1" -> 1211.

给定一个整数 n, 返回 第 n 个顺序。

样例

    给定 n = 5, 返回 "111221".

注意

    整数的顺序将表示为一个字符串。

**题解**

按照规则进行递推即可



```python
class Solution:
    # @param {int} n the nth
    # @return {string} the nth sequence
    def countAndSay(self, n):
        # Write your code here
        say = '1'
        for i in range(n-1):
            say = self._count_say(say)
        return say

    def _count_say(self, s):
        curr = None
        count = 0
        say = ""
        for c in s:
            if c == curr:
                count += 1
            else:
                if curr:
                    say += str(count)+str(curr)
                curr = c
                count = 1
        say += str(count)+str(curr)
        return say

```

---

## @@ 恢复旋转排序数组

给定一个旋转排序数组，在原地恢复其排序。

样例

    [4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]

挑战

    使用O(1)的额外空间和O(n)时间复杂度

说明

    什么是旋转数组？
    比如，原始数组为[1,2,3,4], 则其旋转数组可以是[1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]

**题解**

首先找到分割点，随后分三步调用翻转函数。



```python
class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                self.recover(nums, 0, i)
                self.recover(nums, i+1, len(nums)-1)
                self.recover(nums, 0, len(nums) -1)
        return

    def recover(self, nums, start, end):
        i, j = start, end
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i = i + 1
            j = j - 1
        return nums
```

---

## @@ 尾部的零

设计一个算法，计算出n阶乘中尾部零的个数

样例

    11! = 39916800，因此应该返回 2

挑战

    O(logN)的时间复杂度

**题解**

找阶乘数中末尾的连零数量，容易想到的是找相乘能为10的整数倍的数，如 2×5, 1×10 等，遥想当初做阿里笔试题时遇到过类似的题，当时想着算算5和10的个数就好了，可万万没想到啊，25可以变为两个5相乘！真是蠢死了... 根据数论里面的知识，任何正整数都可以表示为它的质因数的乘积。所以比较准确的思路应该是计算质因数5和2的个数，取小的即可。质因数2的个数显然要大于5的个数，故只需要计算给定阶乘数中质因数中5的个数即可。原题的问题即转化为求阶乘数中质因数5的个数，首先可以试着分析下100以内的数，再试试100以上的数，聪明的你一定想到了可以使用求余求模等方法 :)



分析法代码

```python
class Solution:
    # @param n a integer
    # @return ans a integer
    def trailingZeros(self, n):
        if n < 0:
            return -1
        count = 0
        while n > 0:
            n /= 5
            count += n

        return count

```

代码分析

1. 异常处理，小于0的数返回-1.
2. 先计算5的正整数幂都有哪些，不断使用 n / 5 即可知质因数5的个数。
3. 在循环时使用 n /= 5 而不是 i *= 5, 可有效防止溢出。

递归版本再议，有些没看懂

---

## @@ 在O(1)时间复杂度删除链表节点

给定一个单链表中的表头和一个等待被删除的节点(非表头或表尾)。请在在O(1)时间复杂度删除该链表节点。并在删除该节点后，返回表头。

样例

    给定 1->2->3->4，和节点 3，返回 1->2->4。

**题解**

在链表中删除一个结点，最常规的做法是从链表的头结点开始，顺序查找要删除的结点，找到之后再删除。由于需要顺序查找，时间复杂度自然就是O(n) 了。

我们之所以需要从头结点开始查找要删除的结点，是因为我们需要得到要删除的结点的前面一个结点。我们试着换一种思路。我们可以从给定的结点得到它的下一个结点。这个时候我们实际删除的是它的下一个结点，由于我们已经得到实际删除的结点的前面一个结点，因此完全是可以实现的。当然，在删除之前，我们需要需要把给定的结点的下一个结点的数据拷贝到给定的结点中。此时，时间复杂度为O(1)。

上面的思路还有一个问题：如果删除的结点位于链表的尾部，没有下一个结点，怎么办？我们仍然从链表的头结点开始，顺便遍历得到给定结点的前序结点，并完成删除操作。这个时候时间复杂度是O(n)。那题目要求我们需要在O(1)时间完成删除操作，我们的算法是不是不符合要求？实际上，假设链表总共有n个结点，我们的算法在n-1总情况下时间复杂度是O(1)，只有当给定的结点处于链表末尾的时候，时间复杂度为O(n)。那么平均时间复杂度[(n-1)*O(1)+O(n)]/n，仍然为O(1)。



```python
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    # @param node: the node in the list should be deleted
    # @return: nothing
    def deleteNode(self, node):
        # write your code here
        p = node.next
        node.val = p.val
        node.next = p.next
        p = None
```

注意这里只考虑了节点在中间的情况（因为压根没有给头节点），所以可以轻松处理完成

---

## @@ 链表插入排序

用插入排序对链表排序

样例

    Given 1->3->2->0->null, return 0->1->2->3->null

**题解**

插入排序常见的实现是针对数组的，如前几章总的的 Insertion Sort，但这道题中的排序的数据结构为单向链表，故无法再从后往前遍历比较值的大小了。好在天无绝人之路，我们还可以从前往后依次遍历比较和交换。

由于排序后头节点不一定，故需要引入 dummy 大法，并以此节点的next作为最后返回结果的头节点，返回的链表从dummy->next这里开始构建。首先我们每次都从dummy->next开始遍历，依次和上一轮处理到的节点的值进行比较，直至找到不小于上一轮节点值的节点为止，随后将上一轮节点插入到当前遍历的节点之前，依此类推。



这题 python 版本的会超时，所以用了 c++ 版本

```cpp
/**
 * Definition of ListNode
 * class ListNode {
 * public:
 *     int val;
 *     ListNode *next;
 *     ListNode(int val) {
 *         this->val = val;
 *         this->next = NULL;
 *     }
 * }
 */
class Solution {
public:
    /**
     * @param head: The first node of linked list.
     * @return: The head of linked list.
     */
    ListNode *insertionSortList(ListNode *head) {
        // write your code here
        ListNode *dummy = new ListNode(0);
        ListNode *cur = head;
        while (cur != NULL) {
            ListNode *pre = dummy;
            while (pre->next != NULL && pre->next->val < cur->val) {
                pre = pre->next;
            }
            ListNode *temp = cur->next;
            cur->next = pre->next;
            pre->next = cur;
            cur = temp;
        }

        return dummy->next;
    }
};


```

附上 python 版本

```python
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    """
    def insertionSortList(self, head):
        # write your code here
        dummy = ListNode(0)
        cur = head
        while cur is not None:
            pre = dummy
            while pre.next is not None and pre.next.val < cur.val:
                pre = pre.next
            temp = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = temp
        return dummy.next


```

---

## @@ 链表划分

给定一个单链表和数值x，划分链表使得所有小于x的节点排在大于等于x的节点之前。

你应该保留两部分内链表节点原有的相对顺序。

样例

    给定链表 1->4->3->2->5->2->null，并且 x=3
    返回 1->2->2->4->3->5->null

**题解**

此题出自 CTCI 题 2.4，依据题意，是要根据值x对链表进行分割操作，具体是指将所有小于x的节点放到不小于x的节点之前，咋一看和快速排序的分割有些类似，但是这个题的不同之处在于只要求将小于x的节点放到前面，而并不要求对元素进行排序。

这种分割的题使用两路指针即可轻松解决。左边指针指向小于x的节点，右边指针指向不小于x的节点。由于左右头节点不确定，我们可以使用两个dummy节点。



```python
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param x: an integer
    @return: a ListNode
    """
    def partition(self, head, x):
        # write your code here
        if head is None:
            return None

        leftDummy = ListNode(0)
        left = leftDummy
        rightDummy = ListNode(0)
        right = rightDummy
        node = head
        while node is not None:
            if node.val < x:
                left.next = node
                left = left.next
            else:
                right.next = node
                right = right.next
            node = node.next
        # post-processing
        right.next = None
        left.next = rightDummy.next

        return leftDummy.next

```

---

## @@ 链表倒数第n个节点

找到单链表倒数第n个节点，保证链表中节点的最少数量为n。

样例

    给出链表 3->2->1->5->null和n = 2，返回倒数第二个节点的值1.

**题解**

快慢指针，快指针先走 n 步即可



```python
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: Nth to last node of a singly linked list.
    """
    def nthToLast(self, head, n):
        # write your code here
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next
        while fast != None:
            slow = slow.next
            fast = fast.next
        return slow

```

---

## @@ 翻转链表

翻转一个链表

样例

    给出一个链表1->2->3->null，这个翻转后的链表为3->2->1->null

挑战

    在原地一次翻转完成

**题解**

在纸上画清晰即可，注意需要用一个临时变量保存节点，最多同时需要三个节点的信息



```python
"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list.
                  Reverse it in-place.
    """
    def reverse(self, head):
        # write your code here
        if head is None:
            return None
        fast = head.next
        head.next = None
        while fast != None:
            next = fast.next
            fast.next = head
            head = fast
            fast = next
        return head


```

---

## @@ 翻转字符串

给定一个字符串，逐个翻转字符串中的每个单词。

样例

    给出s = "the sky is blue"，返回"blue is sky the"

说明

+ 单词的构成：无空格字母构成一个单词
+ 输入字符串是否包括前导或者尾随空格？可以包括，但是反转后的字符不能包括
+ 如何处理两个单词间的多个空格？在反转字符串中间空格减少到只含一个

**题解**

1. 由第一个提问可知：题中只有空格字符和非空格字符之分，因此空格字符应为其一关键突破口。
2. 由第二个提问可知：输入的前导空格或者尾随空格在反转后应去掉。
3. 由第三个提问可知：两个单词间的多个空格字符应合并为一个或删除掉。

首先找到各个单词(以空格隔开)，根据题目要求，单词应从后往前依次放入。正向取出比较麻烦，因此可尝试采用逆向思维——先将输入字符串数组中的单词从后往前逆序取出，取出单词后即翻转并append至新字符串数组。在append之前加入空格即可。



```python
class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        # write your code here
        res = ""    # result string
        word = ""   # single word string
        for ch in s:
            if (ch!=' '):
                word+=ch
            if (ch==' '):
                if (len(word)!=0):
                    if (res!=""):   # add space between words
                        res = ' ' + res
                    res = word + res
                    word = ""

        if (len(word)!=0):  #handle the final word
            if (res!=""):
                res = ' ' + res
            res = word + res

        return res

```

---

## @@ 矩阵的之字型遍历

给你一个包含 m x n 个元素的矩阵 (m 行, n 列), 求该矩阵的之字型遍历。

样例

对于如下矩阵：

    [
      [1, 2,  3,  4],
      [5, 6,  7,  8],
      [9,10, 11, 12]
    ]
    返回 [1, 2, 5, 9, 6, 3, 4, 7, 10, 11, 8, 12]

**题解**

注意越界问题



```python
class Solution:
    # @param: a matrix of integers
    # @return: a list of integers
    def printZMatrix(self, matrix):
        # write your code here
        i = 0
        j = 0
        m = len(matrix)
        n = len(matrix[0])
        ret = []

        up = True
        for _ in xrange(m*n):
            ret.append(matrix[i][j])
            if up:
                if i-1<0 or j+1>=n:
                    up = False
                    if j+1>=n:  # go down
                        i += 1
                    else:  # go right
                        j += 1
                else:
                    i -= 1
                    j += 1
            else:
                if i+1>=m or j-1<0:
                    up = True
                    if i+1>=m:
                        j += 1  # go right
                    else:
                        i += 1  # go up
                else:
                    i += 1
                    j -= 1

        return ret

```

---

## @@ 爬楼梯

假设你正在爬楼梯，需要n步你才能到达顶部。但每次你只能爬一步或者两步，你能有多少种不同的方法爬到楼顶部？

样例

    比如 n=3，1+1+1=1+2=2+1=3，共有3中不同的方法
    返回 3

**题解**

可以用迭代或者递归，我个人比较喜欢迭代，简单粗暴，就是到达第 n 级台阶的方法数目等于 第 n-1 级加上第 n-2 级，循环即可



```python
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        # write your code here
        ans = [1,2]
        for i in range(2,n):
            c = ans[i-2] + ans[i-1]
            ans.append(c)
        return ans[n-1]

```

---

## @@ 比较字符串

比较两个字符串A和B，确定A中是否包含B中所有的字符。字符串A和B中的字符都是 大写字母

样例

    给出 A = "ABCD" B = "ACD"，返回 true
    给出 A = "ABCD" B = "AABC"， 返回 false

注意

    在 A 中出现的 B 字符串里的字符不需要连续或者有序。

**题解**

用一个数组标记每个字母出现的次数，注意这里 lintcode 里的测试用例很坑，字符串是带有 `""`符号的，需要在一开始处理一下



```python
class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        # write your code here
        cnt = [0] * 26
        A = A[1:-1]
        B = B[1:-1]
        for c in A:
            cnt[ord(c)-ord('A')] += 1
        for c in B:
            cnt[ord(c)-ord('A')] -= 1
            if cnt[ord(c)-ord('A')] < 0:
                return False
        return True

```

---

## @@ 有效的括号序列

给定一个字符串所表示的括号序列，包含以下字符： '(', ')', '{', '}', '[' and ']'， 判定是否是有效的括号序列。

样例

    括号必须依照 "()" 顺序表示， "()[]{}" 是有效的括号，但 "([)]"则是无效的括号。

挑战

    O(n)的时间，n为括号的个数

**题解**

用一个 stack（或者自己模拟）即可



```python
class Solution:
    # @param {string} s A string
    # @return {boolean} whether the string is a valid parentheses
    def isValidParentheses(self, s):
        # Write your code here
        ans = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                ans.append(s[i])
            else:
                if len(ans) < 1:
                    return False
                cur = ans.pop()
                if s[i] == ')' and cur != '(':
                    return False
                if s[i] == ']' and cur != '[':
                    return False
                if s[i] == '}' and cur != '{':
                    return False
        if len(ans) < 1:
            return True
        else:
            return False

```

---

## @@ 最后一个单词的长度

给定一个字符串， 包含大小写字母、空格' '，请返回其最后一个单词的长度。

如果不存在最后一个单词，请返回 0 。

样例

    给定 s = "Hello World"，返回 5。

注意

    一个单词的界定是，由字母组成，但不包含任何的空格。

**题解**

就正常倒着一个一个数即可



```python
class Solution:
    # @param {string} s A string
    # @return {int} the length of last word
    def lengthOfLastWord(self, s):
        # Write your code here
        l = len(s)
        if l == 0:
            return 0
        ans = 0
        for i in range(1,l+1):
            if s[-i] != ' ':
                ans = ans + 1
            else:
                if ans > 0:
                    return ans
        return ans

```

---

## @@ 旋转字符串

给定一个字符串和一个偏移量，根据偏移量旋转字符串(从左向右旋转)

样例

对于字符串 "abcdefg".

    offset=0 => "abcdefg"
    offset=1 => "gabcdef"
    offset=2 => "fgabcde"
    offset=3 => "efgabcd"

挑战

    在数组上原地旋转，使用O(1)的额外空间

**题解**

三步翻转法即可



应该是 lintcode 的代码问题，这个版本应该是有效的

```python
class Solution:
    # @param s: a list of char
    # @param offset: an integer
    # @return: nothing
    def rotateString(self, s, offset):
        # write you code here
        if s is None or len(s) == 0:
            return s

        offset = offset % len(s)
        head = s[:len(s) - offset]
        tail = s[len(s) - offset:]
        # [::-1] means reverse in Python
        s = head[::-1] + tail[::-1]
        s = s[::-1]
        return s



```
附上 java 版本

```java
public class Solution {
    /**
     * @param str: an array of char
     * @param offset: an integer
     * @return: nothing
     */
    public void rotateString(char[] str, int offset) {
        // write your code here
        if (str == null || str.length == 0) {
            return ;
        }

        int len = str.length;
        offset %= len;
        reverse(str, 0, len - offset - 1);
        reverse(str, len - offset, len - 1);
        reverse(str, 0, len - 1);

    }

    private void reverse(char[] str, int start, int end) {
        while (start < end) {
            char temp = str[start];
            str[start] = str[end];
            str[end] = temp;
            start++;
            end--;
        }
    }
}

```

---

## @@ 翻转二叉树

翻转一棵二叉树

样例

      1         1
     / \       / \
    2   3  => 3   2
       /       \
      4         4

挑战

    递归固然可行，能否写个非递归的？

**题解**

递归版本

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def invertBinaryTree(self, root):
        # write your code here
        if root is None:
            return None
        if root.left:
            self.invertBinaryTree(root.left)
        if root.right:
            self.invertBinaryTree(root.right)
        root.left, root.right = root.right, root.left
        return root

```

非递归版本

```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def invertBinaryTree(self, root):
        # write your code here
        if root is None:
            return None
        queue = [root]
        while queue:
            front = queue.pop(0)
            if front.left:
                queue.append(front.left)
            if front.right:
                queue.append(front.right)
            front.left, front.right = front.right, front.left
        return root

```

---

## @@ 最长单词

给一个词典，找出其中所有最长的单词。

样例

在词典

    {
      "dog",
      "google",
      "facebook",
      "internationalization",
      "blabla"
    }

中, 最长的单词集合为 ["internationalization"]

在词典

    {
      "like",
      "love",
      "hate",
      "yes"
    }

中，最长的单词集合为 ["like", "love", "hate"]

挑战

遍历两次的办法很容易想到，如果只遍历一次你有没有什么好办法？

**题解**

具体计算的时候，保持一个计数和一个当前计数的单词数组，就可以一次搞定

```python
class Solution:
    # @param dictionary: a list of strings
    # @return: a list of strings
    def longestWords(self, dictionary):
        # write your code here
        ret = []
        for word in dictionary:
            if not ret or len(word) > len(ret[0]):
                ret = [word]

            elif len(word) == len(ret[0]):
                ret.append(word)

        return ret

```

---

## @@ 落单的数

给出2*n + 1 个的数字，除其中一个数字之外其他每个数字均出现两次，找到这个数字。

样例

    给出 [1,2,2,1,3,4,3]，返回 4

挑战

    一次遍历，常数级的额外空间复杂度

**题解**

根据题意，共有2*n + 1个数，且有且仅有一个数落单，要找出相应的「单数」。鉴于有空间复杂度的要求，不可能使用另外一个数组来保存每个数出现的次数，考虑到异或运算的特性，根据x ^ x = 0和x ^ 0 = x可将给定数组的所有数依次异或，最后保留的即为结果。

```python
class Solution:
    """
    @param A : an integer array
    @return : a integer
    """
    def singleNumber(self, A):
        # write your code here
        res = 0
        for a in A:
            res = res ^ a
        return res

```

---

## @@ 单例

单例 是最为最常见的设计模式之一。对于任何时刻，如果某个类只存在且最多存在一个具体的实例，那么我们称这种设计模式为单例。例如，对于 class Mouse (不是动物的mouse哦)，我们应将其设计为 singleton 模式。

你的任务是设计一个 getInstance 方法，对于给定的类，每次调用 getInstance 时，都可得到同一个实例。

样例

在 Java 中:

    A a = A.getInstance();
    A b = A.getInstance();

a 应等于 b.

挑战

    如果并发的调用 getInstance，你的程序也可以正确的执行么？

**题解**

这个属于设计题，熟悉即可

```python
import threading

class Solution:
    __lock = threading.Lock()
    __obj = None

    # @return: The same instance of this class every time
    @classmethod
    def getInstance(cls):
        # write your code here
        if not cls.__obj:
            with cls.__lock:
                if not cls.__obj:
                    cls.__obj = cls()

        return cls.__obj

```

---

## @@ 奇偶分割数组

分割一个整数数组，使得奇数在前偶数在后。

样例

    给定 [1, 2, 3, 4]，返回 [1, 3, 2, 4]。

挑战

    在原数组中完成，不使用额外空间。

**题解**

两个索引，分别指向需要交换的数，然后交换即可

```python
class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        # write your code here
        left = 0
        right = len(nums) - 1

        while left < right:
            while left <= right and nums[left] % 2 == 1:
                left = left + 1
            while left <= right and nums[right] % 2 == 0:
                right = right - 1

            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left = left + 1
                right = right - 1

```

---

## @@ 字符串查找

字符串查找（又称查找子字符串），是字符串操作中一个很有用的函数。你的任务是实现这个函数。

对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。

如果不存在，则返回 -1。

样例

    如果 source = "source" 和 target = "target"，返回 -1。
    如果 source = "abcdabcdefg" 和 target = "bcd"，返回 1。

挑战

    O(n2)的算法是可以接受的。如果你能用O(n)的算法做出来那更加好。（提示：KMP）

说明

    在面试中我是否需要实现KMP算法？

不需要，当这种问题出现在面试中时，面试官很可能只是想要测试一下你的基础应用能力。当然你需要先跟面试官确认清楚要怎么实现这个题。

**题解**

O(n2) 方法需要注意边界条件

```python
class Solution:
    def strStr(self, source, target):
        # write your code here
        index = -1
        if source is None or target is None:
            return -1
        if source == target:
            return 0
        if target == "":
            return 0

        for i in range(len(source)-len(target)):
            for j in range(len(target)):
                if source[i+j] == target[j]:
                    index = i
                else:
                    index = -1
                    break
            if index != -1:
                break
        return index

```

---

## @@ 子数组之和(为零)

给定一个整数数组，找到和为零的子数组。你的代码应该返回满足要求的子数组的起始位置和结束位置

样例

    给出[-3, 1, 2, -3, 4]，返回[0, 2] 或者 [1, 3].

**题解**

```python

```

C++ 方法 - 哈希表

题目中的对象是分析子串和，那么我们先从常见的对数组求和出发，
f(i) 表示从数组下标 0 开始至下标 i 的和。子串和为0，也就意味着存在不同的
i1 和 i2 使得 f(i1) - f(i2) = 0 即 f(i1) = f(i2)。思路很快就明晰了，使用一 vector 保存数组中从 0 开始到索引i的和，在将值 push 进 vector 之前先检查 vector 中是否已经存在，若存在则将相应索引加入最终结果并返回。

```cpp
class Solution {
public:
    /**
     * @param nums: A list of integers
     * @return: A list of integers includes the index of the first number
     *          and the index of the last number
     */
    vector<int> subarraySum(vector<int> nums){
        // write your code here
        vector<int> results;
        // curr_cum for the first item, index for the second item
        map<int, int> hash;
        hash[0] = 0;

        int curr_sum = 0;
        for (int i = 0; i != nums.size(); ++i){
            curr_sum += nums[i];
            if (hash.find(curr_sum) != hash.end()){
                results.push_back(hash[curr_sum]);
                results.push_back(i);
                return results;
            } else {
                hash[curr_sum] = i + 1;
            }
        }

        return results;
    }
};

```

---

## @@ 子数组之和(为 K)

Given an nonnegative integer array, find a subarray where the sum of numbers is k.

Your code should return the index of the first number and the index of the last number.

Example

    Given [1, 4, 20, 3, 10, 5], sum k = 33, return [2, 4].


**题解**

核心约束条件变成 f(i1) - f(i2) = k

```cpp
vector<int> subarraySum(vector<int> nums, int k){
    vector<int> result;
    // curr_sum for the first item, index for the second item
    // unordered_map<int, int> hash;
    map<int, int> hash;
    hash[0] = 0;

    int curr_sum = 0;
    for (int i = 0; i != nums.size(); ++i) {
        curr_sum += nums[i];
        if (hash.find(curr_sum - k) != hash.end()) {
            result.push_back(hash[curr_sum - k]);
            result.push_back(i);
            return result;
        } else {
            hash[curr_sum] = i + 1;
        }
    }

    return result;
}

```

与上一题的变化之处有两个地方，第一个是判断是否存在哈希表中时需要使用`hash.find(curr_sum - k)`, 最终返回结果使用`result.push_back(hash[curr_sum - k]);`而不是`result.push_back(hash[curr_sum]);`

**利用单调函数特性的方法**

f(i)为单调不减函数，题中要寻找 f(i2) - f(i1) = k 则必有 f(i2) >= k，类似于两个指针的方法来进行遍历

```cpp
vector<int> subarraySum2(vector<int> nums, int k){
    vector<int> result;

    int left_index = 0;
    int curr_sum = 0;
    for (int i = 0; i != nums.size(); ++i) {
        curr_sum += nums[i];
        if (curr_sum == k) {
            result.push_back(left_index);
            result.push_back(i);
            return result;
        }

        while (curr_sum > k) {
            curr_sum -= nums[left_index];
            ++left_index;
        }
    }

    return result;
}

```
使用for循环累加`curr_sum`, 在`curr_sum > k`时再使用`while`递减`curr_sum`, 同时递增左边索引`left_index`.


---

## @@ 最接近零的子数组和

给定一个整数数组，找到一个和最接近于零的子数组。返回第一个和最右一个指数。你的代码应该返回满足要求的子数组的起始位置和结束位置。

样例

    给出[-3, 1, 1, -3, 5]，返回[0, 2]，[1, 3]， [1, 1]， [2, 2] 或者 [0, 4]

挑战

    O(nlogn)的时间复杂度

**题解**

排序即可在 O(nlogn) 内解决。

1. 遍历一次数组求得子串和
2. 对子串和排序
3. 逐个比较相邻两项差值的绝对值，返回差值绝对值最小的两项

```cpp
class Solution {
public:
    /**
     * @param nums: A list of integers
     * @return: A list of integers includes the index of the first number
     *          and the index of the last number
     */
    vector<int> subarraySumClosest(vector<int> nums){
        // write your code here
        vector<int> result;
        if (nums.empty()) {
            return result;
        }

        const int num_size = nums.size();
        vector<pair<int, int> > sum_index(num_size + 1);

        for (int i = 0; i < num_size; ++i) {
            sum_index[i + 1].first = sum_index[i].first + nums[i];
            sum_index[i + 1].second = i + 1;
        }

        sort(sum_index.begin(), sum_index.end());

        int min_diff = INT_MAX;
        int closest_index = 1;
        for (int i = 1; i < num_size + 1; ++i) {
            int sum_diff = abs(sum_index[i].first - sum_index[i - 1].first);
            if (min_diff > sum_diff) {
                min_diff = sum_diff;
                closest_index = i;
            }
        }

        int left_index = min(sum_index[closest_index - 1].second,\
                             sum_index[closest_index].second);
        int right_index = -1 + max(sum_index[closest_index - 1].second,\
                                   sum_index[closest_index].second);
        result.push_back(left_index);
        result.push_back(right_index);
        return result;
    }
};

```
为避免对单个子串和是否为最小情形的单独考虑，我们可以采取类似链表 dummy 节点的方法规避，简化代码实现。故初始化`sum_index`时需要`num_size + 1`个。这里为避免 vector 反复扩充空间降低运行效率，使用resize一步到位。`sum_index`即最后结果中`left_index`和`right_index`等边界可以结合简单例子分析确定。

---

## @@ Cosine Similarity

Cosine similarity is a measure of similarity between two vectors of an inner product space that measures the cosine of the angle between them. The cosine of 0° is 1, and it is less than 1 for any other angle.

See wiki: Cosine Similarity

Given two vectors A and B with the same size, calculate the cosine similarity.

Return 2.0000 if cosine similarity is invalid (for example A = [0] and B = [0]).

样例

    Given A = [1, 2, 3], B = [2, 3 ,4].
    Return 0.9926.
    Given A = [0], B = [0].
    Return 2.0000

**题解**

```java
class Solution {
    /**
     * @param A: An integer array.
     * @param B: An integer array.
     * @return: Cosine similarity.
     */
    public double cosineSimilarity(int[] A, int[] B) {
        if ( A.length != B.length){
            return 2.0000;
        }

        double up = 0.0;
        double down1 = 0.0;
        double down2 = 0.0;

        for (int i = 0; i < A.length; i++){
            up += A[i] * B[i];
            down1 += A[i] * A[i];
            down2 += B[i] * B[i];
        }

        if (down1 == 0 || down2 == 0){
            return 2.0000;
        }

        return up / (Math.sqrt(down1*down2));
    }
}
```

---

## @@ 岛屿的个数

给一个01矩阵，求不同的岛屿的个数。

0代表海，1代表岛，如果两个1相邻，那么这两个1属于同一个岛。我们只考虑上下左右为相邻。

DFS

**题解**

Use DFS to find the number of connected components of the graph. One full DFS traversal of a node yields a connected component, which could be viewed as an island containing adjacent nodes (by left,right,up and down). Then we could traverse other isolated node excluded from this connected component, in the same manner.

```java
public class Solution {
    /**
     * @param grid a boolean 2D matrix
     * @return an integer
     */
    public int numIslands(boolean[][] grid) {
        if(grid == null || grid.length == 0) {
            return 0;
        }

        final int N = grid.length;
        final int M = grid[0].length;
        final boolean visited[][] = new boolean[N][M];
        int count = 0;

        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {

                if(grid[i][j] && !visited[i][j]) {
                    dfs(grid, i, j, visited);
                    count++;
                }
            }
        }
        return count;
    }

    private void dfs(boolean[][] grid, int i, int j, boolean[][] visited) {
        if(i < 0 || i >= grid.length || j < 0 || j >= grid[0].length) {
            return;
        } else if (visited[i][j] || !grid[i][j] ) {
            return;
        }

        visited[i][j] = true;
        dfs(grid, i - 1, j, visited);
        dfs(grid, i + 1, j, visited);
        dfs(grid, i, j - 1, visited);
        dfs(grid, i, j + 1, visited);
    }
}

```

---

## @@ 子树

有两个不同大小的二进制树： T1 有上百万的节点； T2 有好几百的节点。请设计一种算法，判定 T2 是否为 T1的子树。

样例

下面的例子中 T2 是 T1 的子树：

           1                3
          / \              /
    T1 = 2   3      T2 =  4
            /
           4

下面的例子中 T2 不是 T1 的子树：

           1               3
          / \               \
    T1 = 2   3       T2 =    4
            /
           4

注意

若 T1 中存在从节点 n 开始的子树与 T2 相同，我们称 T2 是 T1 的子树。也就是说，如果在 T1 节点 n 处将树砍断，砍断的部分将与 T2 完全相同。

**题解**

```java
/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param T1, T2: The roots of binary tree.
     * @return: True if T2 is a subtree of T1, or false.
     */
    public boolean isSubtree(TreeNode T1, TreeNode T2) {
        if(T2 == null)
            return true;
        else if(T1 == null)
            return false;
        else return isSameTree(T1, T2) || isSubtree(T1.left, T2) || isSubtree(T1.right, T2);
    }

    public boolean isSameTree(TreeNode T1, TreeNode T2) {
        if(T1 == null && T2 == null)
            return true;
        if(T1 == null || T2 == null)
            return false;
        if(T1.val != T2.val)
            return false;
        return isSameTree(T1.left,T2.left) && isSameTree(T1.right, T2.right);
    }
}

```

---


## @@ 最长上升连续子序列

给定一个整数数组（下标从 0 到 n-1， n 表示整个数组的规模），请找出该数组中的最长上升连续子序列。（最长上升连续子序列可以定义为从右到左或从左到右的序列。）

样例

    给定 [5, 4, 2, 1, 3], 其最长上升连续子序列（LICS）为 [5, 4, 2, 1], 返回 4.
    给定 [5, 1, 2, 3, 4], 其最长上升连续子序列（LICS）为 [1, 2, 3, 4], 返回 4.

**题解**

题目只要返回最大长度，注意此题中的连续递增指的是双向的，即可递增也可递减。简单点考虑可分两种情况，一种递增，另一种递减，跟踪最大递增长度，最后返回即可。也可以在一个 for 循环中搞定，只不过需要增加一布尔变量判断之前是递增还是递减。

```java
public class Solution {
    /**
     * @param A an array of Integer
     * @return  an integer
     */
    public int longestIncreasingContinuousSubsequence(int[] A) {
        if (A == null || A.length == 0) return 0;

        int start = 0, licsMax = 1;
        boolean ascending = false;
        for (int i = 1; i < A.length; i++) {
            // ascending order
            if (A[i - 1] < A[i]) {
                if (!ascending) {
                    ascending = true;
                    start = i - 1;
                }
            } else if (A[i - 1] > A[i]) {
            // descending order
                if (ascending) {
                    ascending = false;
                    start = i - 1;
                }
            } else {
                start = i - 1;
            }
            licsMax = Math.max(licsMax, i - start + 1);
        }

        return licsMax;
    }
}

```

---

## @@ 有效回文串

给定一个字符串，判断其是否为一个回文串。只包含字母和数字，忽略大小写。

样例

    "A man, a plan, a canal: Panama" 是一个回文。
    "race a car" 不是一个回文。

注意

你是否考虑过，字符串有可能是空字符串？这是面试过程中，面试官常常会问的问题。

在这个题目中，我们将空字符串判定为有效回文。

挑战

O(n) 时间复杂度，且不占用额外空间。

**题解**

两步走：

1. 找到最左边和最右边的第一个合法字符(字母或者字符)
2. 一致转换为小写进行比较

字符的判断尽量使用语言提供的 API

```java
public class Solution {
    /**
     * @param s A string
     * @return Whether the string is a valid palindrome
     */
    public boolean isPalindrome(String s) {
        if (s == null || s.isEmpty()) return true;

        int l = 0, r = s.length() - 1;
        while (l < r) {
            // find left alphanumeric character
            if (!Character.isLetterOrDigit(s.charAt(l))) {
                l++;
                continue;
            }
            // find right alphanumeric character
            if (!Character.isLetterOrDigit(s.charAt(r))) {
                r--;
                continue;
            }
            // case insensitive compare
            if (Character.toLowerCase(s.charAt(l)) == Character.toLowerCase(s.charAt(r))) {
                l++;
                r--;
            } else {
                return false;
            }
        }

        return true;
    }
}

```

---

## @@ 把排序数组转换为高度最小的二叉搜索树

给一个排序数组（从小到大），将其转换为一棵高度最小的排序二叉树。

样例

给出数组 [1,2,3,4,5,6,7], 返回

         4
       /   \
      2     6
     / \    / \
    1   3  5   7

挑战

可能有多个答案，返回任意一个即可

**题解**

要达到「平衡二叉搜索树」这个条件，我们首先应从「平衡二叉搜索树」的特性入手。简单起见，我们先考虑下特殊的满二叉搜索树，满二叉搜索树的一个重要特征就是各根节点的 key 不小于左子树的 key ，而小于右子树的所有 key；另一个则是左右子树数目均相等，那么我们只要能将所给升序序列分成一大一小的左右两半部分即可满足题目要求。又由于此题所给的链表结构中仅有左右子树的链接而无指向根节点的链接，故我们只能从中间的根节点进行分析逐层往下递推直至取完数组中所有 key, 数组中间的索引自然就成为了根节点。由于 OJ 上方法入口参数仅有升序序列，方便起见我们可以另写一私有方法，加入start和end两个参数，至此递归模型初步建立。

```java
/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param A: an integer array
     * @return: a tree node
     */
    public TreeNode sortedArrayToBST(int[] A) {
        if (A == null || A.length == 0) return null;

        return helper(A, 0, A.length - 1);
    }

    private TreeNode helper(int[] nums, int start, int end) {
        if (start > end) return null;

        int mid = start + (end - start) / 2;
        TreeNode root = new TreeNode(nums[mid]);
        root.left = helper(nums, start, mid - 1);
        root.right = helper(nums, mid + 1, end);

        return root;
    }
}


```

---

## @@ 排列序号

给出一个不含重复数字的排列，求这些数字的所有排列按字典序排序后该排列的编号。其中，编号从1开始。

样例

例如，排列[1,2,4]是第1个排列。

**题解**

以序列1, 2, 4为例，其不同的排列共有 3!=6 种，以排列[2, 4, 1]为例，若将1置于排列的第一位，后面的排列则有 2!=2 种。将2置于排列的第一位，由于[2, 4, 1]的第二位4在1, 2, 4中为第3大数，故第二位可置1或者2，那么相应的排列共有 2 * 1! = 2种，最后一位1为最小的数，故比其小的排列为0。综上，可参考我们常用的十进制和二进制的转换，对于[2, 4, 1], 可总结出其排列的index为2! * (2 - 1) + 1! * (3 - 1) + 0! * (1 - 1) + 1.

以上分析看似正确无误，实则有个关键的漏洞，在排定第一个数2后，第二位数只可为1或者4，而无法为2, 故在计算最终的 index 时需要动态计算某个数的相对大小。按照从低位到高位进行计算，我们可通过两重循环得出到某个索引处值的相对大小。

```java
public class Solution {
    /**
     * @param A an integer array
     * @return a long integer
     */
    public long permutationIndex(int[] A) {
        if (A == null || A.length == 0) return 0;

        long index = 1;
        long factor = 1;
        for (int i = A.length - 1; i >= 0; i--) {
            int rank = 0;
            for (int j = i + 1; j < A.length; j++) {
                if (A[i] > A[j]) rank++;
            }
            index += rank * factor;
            factor *= (A.length - i);
        }

        return index;
    }
}

```

---

## @@ 将整数A转换为B

如果要将整数A转换为B，需要改变多少个bit位？

样例

    如把31转换为14，需要改变2个bit位。
    (31)10=(11111)2
    (14)10=(01110)2

挑战

    你能想出几种方法？

**题解**


```java
class Solution {
    /**
     *@param a, b: Two integer
     *return: An integer
     */
    public static int bitSwapRequired(int a, int b) {
        int result = a^b;
        int counter = 0;
        while (result != 0) {
            result = result & (result - 1);
            counter++;
        }
        return counter;
    }
};

```

---

## @@ 分割回文串

给定一个字符串s，将s分割成一些子串，使每个子串都是回文串。

返回s所有可能的回文串分割方案。

样例

    给出 s = "aab"，返回

    [
     ["aa","b"],
     ["a","a","b"]
    ]

**题解**

dfs

```java
public class Solution {
    /**
     * @param s: A string
     * @return: A list of lists of string
     */
    public ArrayList<ArrayList<String>> partition(String s) {
        ArrayList<ArrayList<String>> result = new ArrayList<ArrayList<String>>();

        if (s == null || s.length() == 0) {
            return result;
        }

        ArrayList<String> partition = new ArrayList<String>();//track each possible partition
        addPalindrome(s, 0, partition, result);

        return result;
    }

    private void addPalindrome(String s, int start, ArrayList<String> partition,
            ArrayList<ArrayList<String>> result) {
        //stop condition
        if (start == s.length()) {
            ArrayList<String> temp = new ArrayList<String>(partition);
            result.add(temp);
            return;
        }

        for (int i = start + 1; i <= s.length(); i++) {
            String str = s.substring(start, i);
            if (isPalindrome(str)) {
                partition.add(str);
                addPalindrome(s, i, partition, result);
                partition.remove(partition.size() - 1);
            }
        }
    }

    private boolean isPalindrome(String str) {
        int left = 0;
        int right = str.length() - 1;

        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false;
            }

            left++;
            right--;
        }

        return true;
    }
}

```

---

## @@ 插入区间

给出一个无重叠的按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

样例

插入区间[2, 5] 到 [[1,2], [5,9]]，我们得到 [[1,9]]。

插入区间[3, 4] 到 [[1,2], [5,9]]，我们得到 [[1,2], [3,4], [5,9]]。

**题解**

逐个融合即可

```java
/**
 * Definition of Interval:
 * public classs Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 */

class Solution {
    /**
     * Insert newInterval into intervals.
     * @param intervals: Sorted interval list.
     * @param newInterval: A new interval.
     * @return: A new sorted interval list.
     */
    public ArrayList<Interval> insert(ArrayList<Interval> intervals, Interval newInterval) {
        if (newInterval == null || intervals == null) {
            return intervals;
        }

        ArrayList<Interval> results = new ArrayList<Interval>();
        int insertPos = 0;

        for (Interval interval : intervals) {
            if (interval.end < newInterval.start) {
                results.add(interval);
                insertPos++;
            } else if (interval.start > newInterval.end) {
                results.add(interval);
            } else {
                newInterval.start = Math.min(interval.start, newInterval.start);
                newInterval.end = Math.max(interval.end, newInterval.end);
            }
        }

        results.add(insertPos, newInterval);

        return results;
    }
}

```

---


## @@ 数组剔除元素后的乘积

给定一个整数数组A。

定义B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]， 计算B的时候请不要使用除法。

样例

    给出A=[1, 2, 3]，返回 B为[6, 3, 2]

**题解**

左右分治法

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

## @@ 字符大小写排序

给定一个只包含字母的字符串，按照先小写字母后大写字母的顺序进行排序。

样例

给出"abAcD"，一个可能的答案为"acbAD"

注意

小写字母或者大写字母他们之间不一定要保持在原始字符串中的相对位置。

挑战

在原地扫描一遍完成

**题解**

```java
public class Solution {
    /**
     *@param chars: The letter array you should sort by Case
     *@return: void
     */
    public void sortLetters(char[] chars) {
        int len = chars.length;
        if (len <= 1) return;

        int p1 = 0, p2 = len-1;
        while (p1<len && chars[p1]>='a' && chars[p1]<='z') p1++;
        while (p2>=0 && chars[p2]>='A' && chars[p2]<='Z') p2--;
        while (p1<p2){
            //swap p1 and p2.
            char temp = chars[p1];
            chars[p1] = chars[p2];
            chars[p2] = temp;
            //find next swap positions.
            while (p1<len && chars[p1]>='a' && chars[p1]<='z') p1++;
            while (p2>=0 && chars[p2]>='A' && chars[p2]<='Z') p2--;
        }
    }
}


```

---

## @@ 最小子数组

给定一个整数数组，找到一个具有最小和的子数组。返回其最小和。

样例

给出数组[1, -1, -2, 1]，返回 -3

注意

子数组最少包含一个数字

**题解**

Greddy.
1. Initialize sum = 0, min_sum = MAX_INT
2. for each num n, sum + n, check sum with min_sum
3. if sum > 0, no need to keep it, reset sum to 0.
Time complexity = O(n)

```java
public class Solution {
    /**
     * @param nums: a list of integers
     * @return: A integer indicate the sum of minimum subarray
     */
    public int minSubArray(ArrayList<Integer> nums) {
        int len = nums.size();
        if (len==0) return 0;

        int curMin = nums.get(0);
        int minRes = nums.get(0);

        for (int i=1;i<len;i++){
            curMin = Math.min(nums.get(i),curMin+nums.get(i));
            minRes = Math.min(curMin,minRes);
        }
        return minRes;
    }
}


```

---

## @@ 最大子数组

给定一个整数数组，找到一个具有最大和的子数组，返回其最大和。

给出数组[−2,2,−3,4,−1,2,1,−5,3]，符合要求的子数组为[4,−1,2,1]，其最大和为6

注意

子数组最少包含一个数

挑战

要求时间复杂度为O(n)

**题解**

dp

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

## @@ 搜索插入位置

给定一个排序数组和一个目标值，如果在数组中找到目标值则返回索引。如果没有，返回到它将会被按顺序插入的位置。

你可以假设在数组中无重复元素。

样例

[1,3,5,6]，5 → 2

[1,3,5,6]，2 → 1

[1,3,5,6]，7 → 4

[1,3,5,6]，0 → 0

**题解**

应该把二分法的问题拆解为find the first/last position of...的问题。由最原始的二分查找可找到不小于目标整数的最小下标。返回此下标即可。

```java
public class Solution {
    /**
     * param A : an integer sorted array
     * param target :  an integer to be inserted
     * return : an integer
     */
    public int searchInsert(int[] A, int target) {
        if (A == null) {
            return -1;
        }
        if (A.length == 0) {
            return 0;
        }

        int start = 0, end = A.length - 1;
        int mid;

        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (A[mid] == target) {
                return mid; // no duplicates, if not `end = target;`
            } else if (A[mid] < target) {
                start = mid;
            } else {
                end = mid;
            }
        }

        if (A[start] >= target) {
            return start;
        } else if (A[end] >= target) {
            return end; // in most cases
        } else {
            return end + 1; // A[end] < target;
        }
    }
}


```

---

## @@ 在二叉查找树中插入节点

给定一棵二叉查找树和一个新的树节点，将节点插入到树中。

你需要保证该树仍然是一棵二叉查找树。

样例

给出如下一棵二叉查找树，在插入节点6之后这棵二叉查找树可以是这样的：

      2             2
     / \           / \
    1   4   -->   1   4
       /             / \
      3             3   6

挑战

能否不使用递归？

**题解**

很简单题，每个node决定是往左还是往右还是就是这个节点。类似二分的做法。

```java
/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param root: The root of the binary search tree.
     * @param node: insert this node into the binary search tree
     * @return: The root of the new binary search tree.
     */
    public TreeNode insertNode(TreeNode root, TreeNode node) {
        if (root == null) {
            root = node;
            return root;
        }
        TreeNode tmp = root;
        TreeNode last = null;
        while (tmp != null) {
            last = tmp;
            if (tmp.val > node.val) {
                tmp = tmp.left;
            } else {
                tmp = tmp.right;
            }
        }
        if (last != null) {
            if (last.val > node.val) {
                last.left = node;
            } else {
                last.right = node;
            }
        }
        return root;
    }
}

```

---

## @@ 最小路径和

给定一个只含非负整数的m*n网格，找到一条从左上角到右下角的可以使数字和最小的路径。

注意

你在同一时间只能向下或者向右移动一步

**题解**

```java
public class Solution {
    /**
     * @param grid: a list of lists of integers.
     * @return: An integer, minimizes the sum of all numbers along its path
     */
    public int minPathSum(int[][] grid) {
        int rowNum = grid.length;
        if (rowNum==0) return 0;
        int colNum = grid[0].length;
        if (colNum==0) return 0;

        int[][] sum = new int[rowNum][colNum];
        sum[0][0] = grid[0][0];
        for (int i=1;i<rowNum;i++) sum[i][0] = sum[i-1][0]+grid[i][0];
        for (int i=1;i<colNum;i++) sum[0][i] = sum[0][i-1]+grid[0][i];

        for (int i=1;i<rowNum;i++)
            for (int j=1;j<colNum;j++){
                sum[i][j] = Math.min(sum[i-1][j],sum[i][j-1])+grid[i][j];
            }

        return sum[rowNum-1][colNum-1];
    }
}


```

---


## @@ 数字三角形

给定一个数字三角形，找到从顶部到底部的最小路径和。每一步可以移动到下面一行的相邻数字上。

样例

比如，给出下列数字三角形：

    [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]

从顶到底部的最小路径和为11 ( 2 + 3 + 5 + 1 = 11)。

注意

如果你只用额外空间复杂度O(n)的条件下完成可以获得加分，其中n是数字三角形的总行数。

**题解**

It’s an easy question. Instead of normal DP transition function, this one is so-called bottom-up approach.

```java
public class Solution {
    /**
     * @param triangle: a list of lists of integers.
     * @return: An integer, minimum path sum.
     */
    public int minimumTotal(ArrayList<ArrayList<Integer>> triangle) {
        int len = triangle.size();
        if (len == 0) return 0;
        int[] m = new int[len];
        m[0] = triangle.get(0).get(0);
        for (int i = 1; i < len; i ++) {
            ArrayList<Integer> cur = triangle.get(i);
            for (int j = i; j >= 0; j --) {
                if (j == i) m[j] = m[j-1] + cur.get(j);
                else if (j == 0) m[j] = m[0] + cur.get(0);
                else m[j] = Math.min(m[j-1], m[j]) + cur.get(j);
            }
        }
        int min = Integer.MAX_VALUE;
        for (Integer k: m)
            min = Math.min(min, k);
        return min;
    }
}


```

---


## @@ 找出无向图汇总的相连要素

请找出无向图中相连要素的个数。

图中的每个节点包含其邻居的 1 个标签和 1 个列表。（一个无向图的相连节点（或节点）是一个子图，其中任意两个顶点通过路径相连，且不与超级图中的其它顶点相连。）

样例

给定图:

    A------B  C
     \     |  |
      \    |  |
       \   |  |
        \  |  |
          D   E

返回 {A,B,D}, {C,E}。其中有 2 个相连的元素，即{A,B,D}, {C,E}

**题解**

How do we check for a connected graph (any two nodes are connected)?
Maybe check for each node: each node represents a lead to a subgraph, then check if this subgraph
is valid.
1. In real case, need to ask the intervier: can we assume the given nodes are valid, so that we only
need to check for success case? That means, we assume for example a linear list A-B-C does not exist.
2. Then, we can use a 'set' to mark: we've checked this node.
3. Use a queue for BFS
4. Use a arraylist to save the results.
5. Key point: when the queue is empty(), that means one set of connected component is ready to go
6. Iterate through nodes, when it's not empty.
More Notes:Have to do Collections.sort()....somehow it want me to sort the results?
Note2: Get rid of a node from nodes, whenever add it to component ... don't forget this.
Note3: Well, there is a chance that compoents are added, queue is cleaned, but nodes are empty as well..
that means, need to catch the last case of 'remaining component' and add it to rst.

bfs

```java
/**
 * Definition for Undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     ArrayList<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */
public class Solution {
    /**
     * @param nodes a array of Undirected graph node
     * @return a connected set of a Undirected graph
     */
    public List<List<Integer>> connectedSet(ArrayList<UndirectedGraphNode> nodes) {
        List<List<Integer>> rst = new ArrayList<>();
        if (nodes == null || nodes.size() == 0) {
            return rst;
        }
        //Init:
        Set<UndirectedGraphNode> checked = new HashSet();
        Queue<UndirectedGraphNode> queue = new LinkedList();
        ArrayList<Integer> component = new ArrayList<Integer>();

        queue.offer(nodes.get(0));

        while (!nodes.isEmpty()) {
            if (queue.isEmpty()) {
                Collections.sort(component);
                rst.add(component);
                queue.offer(nodes.get(0));
                component = new ArrayList<Integer>();
            } else {
                UndirectedGraphNode curr = queue.poll();
                if (!checked.contains(curr)) {
                    checked.add(curr);
                    component.add(curr.label);
                    nodes.remove(curr);
                    for (UndirectedGraphNode node : curr.neighbors) {
                            queue.add(node);
                    }
                }
            }
        }
        if (!component.isEmpty()) {
            rst.add(component);
        }
        return rst;
    }
}

```

dfs

```java
/**
 * Definition for Undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     ArrayList<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */
public class Solution {
    /**
     * @param nodes a array of Undirected graph node
     * @return a connected set of a Undirected graph
     */
    public List<List<Integer>> connectedSet(ArrayList<UndirectedGraphNode> nodes) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> path = new ArrayList<Integer>();
        Set<UndirectedGraphNode> visited = new HashSet<UndirectedGraphNode>();
        for(UndirectedGraphNode node : nodes){
            if(!visited.contains(node)){
                dfs(node, visited, path);
                Collections.sort(path);
                result.add(new ArrayList<Integer>(path));
                path.clear();
            }
        }
        return result;

    }

    public void dfs(UndirectedGraphNode node, Set<UndirectedGraphNode> visited, List<Integer> path){
        visited.add(node);
        path.add(node.label);
        for(UndirectedGraphNode n : node.neighbors){
            if(!visited.contains(n)){
                dfs(n, visited, path);
            }
        }
    }
}

```

---


## @@ 判断数独是否合法

请判定一个数独是否有效。

该数独可能只填充了部分数字，其中缺少的数字用 . 表示。

注意

    一个合法的数独（仅部分填充）并不一定是可解的。我们仅需使填充的空格有效即可。

说明 什么是数独？

+ [英文版](http://sudoku.com.au/TheRules.aspx)
+ [中文版](http://baike.baidu.com/subview/961/10842669.htm)

**题解**

```java
class Solution {
    /**
      * @param board: the board
        @return: wether the Sudoku is valid
      */
    public boolean isValidSudoku(char[][] board) {
        if(board == null || board.length == 0 || board[0].length == 0) return false;

        int m = 9, n = 9;
        // check row
        boolean[] visited = new boolean[9];
        for(int i = 0; i < m; i++){
            Arrays.fill(visited, false);
            for(int j = 0; j < n; j++){
                if(!precess(visited, board[i][j])) return false;
            }
        }

        for(int i = 0; i < n; i++){
            Arrays.fill(visited, false);
            for(int j = 0; j < m; j++){
                if(!precess(visited, board[j][i])) return false;
            }
        }

        for(int i = 0; i < m; i+=3){

          for(int j = 0; j < n; j+=3){
              Arrays.fill(visited, false);
              for(int k = 0; k < 9; k++){
                  if(!precess(visited, board[i+k/3][j+k%3])) return false;
              }

            }
        }
        return true;

    }

    private boolean precess(boolean[] visited, char c){
        if(c == '.') return true;
        int num = c - '0';
        if(num > 9 || num < 1 || visited[num-1]) return false;
        visited[num-1] = true;
        return true;
    }
};

```

---




## ---- 中等题 ----

## @@ 罗马数字转整数

给定一个罗马数字，将其转换成整数。

返回的结果要求在1到3999的范围内。

样例

    IV -> 4
    XII -> 12
    XXI -> 21
    XCIX -> 99



**题解**

```java
public class Solution {
    /**
     * @param s Roman representation
     * @return an integer
     */
    public int romanToInt(String s) {
         if (s == null) {
            return 0;
        }

        // bug 1: forget new.
        HashMap<Character, Integer> map = new HashMap<Character, Integer>();
        map.put('I', 1);
        map.put('V', 5);
        map.put('X', 10);
        map.put('L', 50);
        map.put('C', 100);
        map.put('D', 500);
        map.put('M', 1000);

        int len = s.length();
        int num = 0;
        for (int i = len - 1; i >= 0; i--) {
            int cur = map.get(s.charAt(i));
            if (i < len - 1 && cur < map.get(s.charAt(i + 1))) {
                num -= cur;
            } else {
                num += cur;
            }
        }

        return num;
    }
}

```

---

## @@ 整数转罗马数字

给定一个整数，将其转换成罗马数字。

返回的结果要求在1-3999的范围内。

样例

    4 -> IV
    12 -> XII
    21 -> XXI
    99 -> XCIX

**题解**

```java
public class Solution {
    /**
     * @param n The integer
     * @return Roman representation
     */
    public String intToRoman(int n) {
        if(n <= 0) {
            return "";
        }
        int[] nums = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] symbols = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        StringBuilder res = new StringBuilder();
        int digit=0;
        while (n > 0) {
            int times = n / nums[digit];
            n -= nums[digit] * times;
            for ( ; times > 0; times--) {
                res.append(symbols[digit]);
            }
            digit++;
        }
        return res.toString();
    }
}

```

---


## @@ 排序矩阵中的从小到大第k个数

在一个排序矩阵中找从小到大的第 k 个整数。

排序矩阵的定义为：每一行递增，每一列也递增。

样例

给出 k = 4 和一个排序矩阵：

    [
      [1 ,5 ,7],
      [3 ,7 ,8],
      [4 ,8 ,9],
    ]

返回 5。

挑战

使用O(k log n)的方法，n为矩阵的宽度和高度中的最大值。

**题解**

用优先队列

```java
public class Solution {
    /**
     * @param matrix: a matrix of integers
     * @param k: an integer
     * @return: the kth smallest number in the matrix
     */
    public int kthSmallest(final int[][] matrix, int k) {
        int m = matrix.length, n = matrix[0].length;
        boolean[][] visited = new boolean[m][n];

        PriorityQueue<int[]> queue = new PriorityQueue<int[]>(k, new Comparator<int[]>(){
            public int compare(int[] a, int[]b){
                return matrix[a[0]][a[1]] - matrix[b[0]][b[1]];
            }
        });
        queue.add(new int[]{0,0});
        visited[0][0] = true;
        while(k > 1){
            int[] res = queue.poll();
            k--;
            int x = res[0];
            int y = res[1];
            if(x+1 < m && visited[x+1][y] == false){
                queue.add(new int[]{x+1, y});
                visited[x+1][y] = true;
            }

            if(y+1 < n && visited[x][y+1] == false){
                queue.add(new int[]{x, y+1});
                visited[x][y+1] = true;
            }
        }
        int[] res = queue.poll();
        return matrix[res[0]][res[1]];
    }
}

```

---

## @@ 简化路径

给定一个文档(Unix-style)的完全路径，请进行路径简化。

样例

    "/home/", => "/home"
    "/a/./b/../../c/", => "/c"

挑战

+ 你是否考虑了 路径 = "/../" 的情况？在这种情况下，你需返回"/"。
+ 此外，路径中也可能包含双斜杠'/'，如 "/home//foo/"。 在这种情况下，可忽略多余的斜杠，返回 "/home/foo"。

**题解**

```java
public class Solution {
    /**
     * @param path the original path
     * @return the simplified path
     */
    public String simplifyPath(String path) {
        String result = "/";
        String[] stubs = path.split("/+");
        ArrayList<String> paths = new ArrayList<String>();
        for (String s : stubs){
            if(s.equals("..")){
                if(paths.size() > 0){
                    paths.remove(paths.size() - 1);
                }
            }
            else if (!s.equals(".") && !s.equals("")){
                paths.add(s);
            }
        }
        for (String s : paths){
            result += s + "/";
        }
        if (result.length() > 1)
            result = result.substring(0, result.length() - 1);
        return result;
    }
}

```

---



## @@ 最长公共子串

给出两个字符串，找到最长公共子串，并返回其长度。

样例

    给出A=“ABCD”，B=“CBCE”，返回 2

注意

    子串的字符应该连续的出现在原字符串中，这与子序列有所不同。

**题解**

求最长公共子串，注意「子串」和「子序列」的区别！简单考虑可以使用两根指针索引分别指向两个字符串的当前遍历位置，若遇到相等的字符时则同时向后移动一位

```python


```

```cpp
class Solution {
public:
    /**
     * @param A, B: Two string.
     * @return: the length of the longest common substring.
     */
    int longestCommonSubstring(string &A, string &B) {
        // write your code here
        if (A.empty() || B.empty()){
            return 0;
        }

        int lcs = 0, tlcs = 0;
        for (int i = 0; i < A.size(); i++){
            for (int j = 0; j < B.size(); j++){
                tlcs = 0;
                while ((i + tlcs < A.size()) && (j + tlcs < B.size()) && (A[i + tlcs] == B[j + tlcs])){
                    tlcs++;
                }
                if (tlcs > lcs){
                    lcs = tlcs;
                }
            }
        }
        return lcs;
    }
};

```

---

## @@ 寻找缺失的数

给出一个包含 0 .. N 中 N 个数的序列，找出0 .. N 中没有出现在序列中的那个数。

样例

N = 4 且序列为 [0, 1, 3] 时，缺失的数为2。

注意

可以改变序列中数的位置。

挑战

在数组上原地完成，使用O(1)的额外空间和O(N)的时间。

**题解**

```java
public class Solution {
    /**
     * @param nums: an array of integers
     * @return: an integer
     */
    public int findMissing(int[] nums) {
        int length = nums.length;
        int sum = length * (length + 1) / 2;

        for (int i = 0; i < length; i++){
            sum -= nums[i];
        }

        return sum;
    }
}
```

---

## @@ 最多有多少个点在一条直线上

给出二维平面上的n个点，求最多有多少点在同一条直线上。

样例

给出4个点：(1, 2), (3, 6), (0, 0), (1, 3)。

一条直线上的点最多有3个。

**题解**

取定一个点(xk,yk), 遍历所有节点(xi, yi), 然后统计斜率相同的点数，并求取最大值即可

```java

/**
 * Definition for a point.
 * class Point {
 *     int x;
 *     int y;
 *     Point() { x = 0; y = 0; }
 *     Point(int a, int b) { x = a; y = b; }
 * }
 */
public class Solution {
    /**
     * @param points an array of point
     * @return an integer
     */
    public int maxPoints(Point[] points) {
        if(points == null || points.length == 0)
            return 0;

        HashMap<Double, Integer> result = new HashMap<Double, Integer>();
        int max=0;

        for(int i=0; i < points.length; i++){
            int duplicate = 1;//
            int vertical = 0;
            for(int j=i+1; j<points.length; j++){
                //handle duplicates and vertical
                if(points[i].x == points[j].x){
                    if(points[i].y == points[j].y){
                        duplicate++;
                    }else{
                        vertical++;
                    }
                }else{
                    double slope = points[j].y == points[i].y ? 0.0
                            : (1.0 * (points[j].y - points[i].y))
                            / (points[j].x - points[i].x);

                    if(result.get(slope) != null){
                        result.put(slope, result.get(slope) + 1);
                    }else{
                        result.put(slope, 1);
                    }
                }
            }

            for(Integer count: result.values()){
                if(count+duplicate > max){
                    max = count+duplicate;
                }
            }

            max = Math.max(vertical + duplicate, max);
            result.clear();
        }


        return max;
    }
}


```

---

## @@ Maximal Square

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

样例

For example, given the following matrix:

    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0

Return 4.

**题解**

动态规划（Dynamic Programming）

状态转移方程：

    dp[x][y] = min(dp[x - 1][y - 1], dp[x][y - 1], dp[x - 1][y]) + 1

上式中，`dp[x][y]`表示以坐标(x, y)为右下角元素的全1正方形矩阵的最大长度（宽度）

```java
public class Solution {
    /**
     * @param matrix: a matrix of 0 and 1
     * @return: an integer
     */
    public int maxSquare(int[][] matrix) {
        // write your code here
        if (matrix == null || matrix.length == 0) {
            return 0;
        }

        int[][] dp = new int[matrix.length][matrix[0].length];
        int max = 0;

        for (int i = 0; i < matrix.length; i++) {
            dp[i][0] = matrix[i][0] == 1 ? 1 : 0;
            max = Math.max(max, dp[i][0]);
        }

        for (int j = 0; j < matrix[0].length; j++) {
            dp[0][j] = matrix[0][j] == 1 ? 1 : 0;
            max = Math.max(max, dp[0][j]);
        }


        for (int i = 1; i < matrix.length; i++) {
            for (int j = 1; j < matrix[0].length; j++) {
                dp[i][j] = matrix[i][j] == 1 ?
                Math.min(Math.min(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + 1 : 0;
                max = Math.max(max, dp[i][j]);
            }
        }

        return (int)Math.pow(max, 2);
    }
}

```

---

## @@ 和为零的子矩阵

给定一个整数矩阵，请找出一个子矩阵，使得其数字之和等于0.输出答案时，请返回左上数字和右下数字的坐标。

样例

给定矩阵

    [
      [1 ,5 ,7],
      [3 ,7 ,-8],
      [4 ,-8 ,9],
    ]

返回 [(1,1), (2,2)]

挑战

O(n3) 时间复杂度。

**题解**

```java
public class Solution {
    /**
     * @param matrix an integer matrix
     * @return the coordinate of the left-up and right-down number
     */
    public int[][] submatrixSum(int[][] matrix) {
        int[][] result = new int[2][2];
        int M = matrix.length;
        if (M == 0) return result;
        int N = matrix[0].length;
        if (N == 0) return result;
        // pre-compute: sum[i][j] = sum of submatrix [(0, 0), (i, j)]
        int[][] sum = new int[M+1][N+1];
        for (int j=0; j<=N; ++j) sum[0][j] = 0;
        for (int i=1; i<=M; ++i) sum[i][0] = 0;
        for (int i=0; i<M; ++i) {
            for (int j=0; j<N; ++j)
                sum[i+1][j+1] = matrix[i][j] + sum[i+1][j] + sum[i][j+1] - sum[i][j];
        }
        for (int l=0; l<M; ++l) {
            for (int h=l+1; h<=M; ++h) {
                Map<Integer, Integer> map = new HashMap<Integer, Integer>();
                for (int j=0; j<=N; ++j) {
                    int diff = sum[h][j] - sum[l][j];
                    if (map.containsKey(diff)) {
                        int k = map.get(diff);
                        result[0][0] = l;   result[0][1] = k;
                        result[1][0] = h-1; result[1][1] = j-1;
                        return result;
                    } else {
                        map.put(diff, j);
                    }
                }
            }
        }
        return result;
    }
}

```

---

## @@ 连续子数组求和

给定一个整数数组，请找出一个连续子数组，使得该子数组的和最大。输出答案时，请分别返回第一个数字和最后一个数字的值。（如果两个相同的答案，请返回其中任意一个）

样例

给定 [-3, 1, 3, -3, 4], 返回[1,4].

**题解**

```java
public class Solution {
    /**
     * @param A an integer array
     * @return  A list of integers includes the index of the first number and the index of the last number
     */
    public ArrayList<Integer> continuousSubarraySum(int[] A) {
        ArrayList<Integer> res = new ArrayList<Integer>();
        if (A == null || A.length == 0) {
            return res;
        }
        int sum = A[0];
        int max = sum;
        int start = 0, end = 0;
        res.add(0);
        res.add(0);
        for (int i = 1; i < A.length; i++) {
            if (sum > max) {
                res.set(0, start);
                res.set(1, i-1);
                max = sum;
            }
            if (sum < 0) {
                sum = 0;
                start = i;
                end = i;
            }
            sum += A[i];
        }
        if (sum > max) {
            res.set(0, start);
            res.set(1, A.length-1);
        }
        return res;
    }
}

```

---


## @@ 逆波兰表达式求值

求逆波兰表达式的值。

在逆波兰表达法中，其有效的运算符号包括 +, -, *, / 。每个运算对象可以是整数，也可以是另一个逆波兰计数表达。

样例

    ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
    ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

**题解**

```java
public class Solution {
    /**
     * @param tokens The Reverse Polish Notation
     * @return the value
     */
    public int evalRPN(String[] tokens) {
        if (tokens == null) {
            return 0;
        }
        
        int len = tokens.length;
        Stack<Integer> s = new Stack<Integer>();
        
        for (int i = 0; i < len; i++) {
            String str = tokens[i];
            if (str.equals("+") || str.equals("-") || str.equals("*") || str.equals("/")) {
                // get out the two operation number.
                int n2 = s.pop();
                int n1 = s.pop();
                if (str.equals("+")) {
                    s.push(n1 + n2);
                } else if (str.equals("-")) {
                    s.push(n1 - n2);
                } else if (str.equals("*")) {
                    s.push(n1 * n2);
                } else if (str.equals("/")) {
                    s.push(n1 / n2);
                }
            } else {
                s.push(Integer.parseInt(str));
            }
        }
        
        if (s.isEmpty()) {
            return 0;
        }
        
        return s.pop();
    }
}

```

---

## @@ 下一个排列

给定一个若干整数的排列，给出按正数大小进行字典序从小到大排序后的下一个排列。

如果没有下一个排列，则输出字典序最小的序列。

样例

左边是原始排列，右边是对应的下一个排列。

    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1

挑战

不允许使用额外的空间。

**题解**

下面简要介绍一下字典序算法：

1. 从后往前寻找索引满足 a[k] < a[k + 1], 如果此条件不满足，则说明已遍历到最后一个。
2. 从后往前遍历，找到第一个比a[k]大的数a[l], 即a[k] < a[l].
3. 交换a[k]与a[l].
4. 反转k + 1 ~ n之间的元素。

由于这道题中规定对于[4,3,2,1], 输出为[1,2,3,4], 故在第一步稍加处理即可。

```java
public class Solution {
    /**
     * @param nums: an array of integers
     * @return: return nothing (void), do not return anything, modify nums in-place instead
     */
    public void nextPermutation(int[] nums) {
        if (nums == null || nums.length <= 1) {
            return;
        }
        // step1: find nums[i] < nums[i + 1]
        int i = 0;
        for (i = nums.length - 2; i >= 0; i--) {
            if (nums[i] < nums[i + 1]) {
                break;
            } else if (i == 0) {
                // reverse nums if reach maximum
                reverse(nums, 0, nums.length - 1);
                return;
            }
        }
        // step2: find nums[i] < nums[j]
        int j = 0;
        for (j = nums.length - 1; j > i; j--) {
            if (nums[i] < nums[j]) {
                break;
            }
        }
        // step3: swap betwenn nums[i] and nums[j]
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
        // step4: reverse between [i + 1, n - 1]
        reverse(nums, i + 1, nums.length - 1);

        return;
    }

    private void reverse(int[] nums, int start, int end) {
        for (int i = start, j = end; i < j; i++, j--) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }
}

```

---

## @@ 最长回文子串

给出一个字符串（假设长度最长为1000），求出它的最长回文子串，你可以假定只有一个满足条件的最长回文串。

样例

给出字符串 "abcdzdcab"，它的最长回文子串为 "cdzdc"。

挑战

O(n2) 时间复杂度的算法是可以接受的，如果你能用 O(n) 的算法那自然更好。

**题解**

这个方法其实很直观，就是从头扫描到尾部，每一个字符以它为中心向2边扩展，扩展到不能扩展为止（有不同的字符），返回以每一个字符为中心的回文，然后不断更新最大回文并返回之。

算法简单，而且复杂度为O(n^2),空间复杂度为O(1)


```java
public class Solution {
    /**
     * @param s input string
     * @return the longest palindromic substring
     */
    public String longestPalindrome(String s) {
        if (s == null) {
            return null;
        }

        String ret = null;

        int len = s.length();
        int max = 0;
        for (int i = 0; i < len; i++) {
            String s1 = getLongest(s, i, i);
            String s2 = getLongest(s, i, i + 1);

            if (s1.length() > max) {
                max = Math.max(max, s1.length());
                ret = s1;
            }

            if (s2.length() > max) {
                max = Math.max(max, s2.length());
                ret = s2;
            }
        }

        return ret;
    }

    public String getLongest(String s, int left, int right) {
        int len = s.length();
        while (left >= 0 && right < len) {
            // when i is in the center.
            if (s.charAt(left) != s.charAt(right)) {
                break;
            }

            left--;
            right++;
        }

        return s.substring(left + 1, right);
    }
}

```

---

## @@ 和大于S的最小子数组

给定一个由 n 个整数组成的数组和一个正整数 s ，请找出该数组中满足其和 ≥ s 的最小长度子数组。如果无解，则返回 -1。

样例

给定数组 [2,3,1,2,4,3] 和 s = 7, 子数组 [4,3] 是该条件下的最小长度子数组。

挑战

如果你已经完成了O(n)时间复杂度的编程，请再试试 O(n log n)时间复杂度。

**题解**

two pointers.当当前sum已经满足条件后，将start往后移至不满足条件的index为止，再更新结果。复杂度O(n)。

```java
public class Solution {
    /**
     * @param nums: an array of integers
     * @param s: an integer
     * @return: an integer representing the minimum size of subarray
     */
    public int minimumSize(int[] nums, int s) {
        if (nums == null || nums.length == 0) {
            return -1;
        }
        int res = -1;
        int sum = 0;
        int start = 0;
        for (int end = 0; end < nums.length; end++) {
            sum += nums[end];
            if (sum >= s) {
                if (start == end) {
                    res = 1;
                    break;
                }
                while (start < end && sum - nums[start] >= s) {
                    sum -= nums[start];
                    start++;
                }
                res = res == -1 ? end - start + 1 : Math.min(res, end - start + 1);
            }
        }
        return res == -1 ? -1 : res;
    }
}

```

---

## @@ 硬币排成线

有 n 个硬币排成一条线。两个参赛者轮流从右边依次拿走 1 或 2 个硬币，直到没有硬币为止。拿到最后一枚硬币的人获胜。

请判定 第一个玩家 是输还是赢？

样例

    n = 1, 返回 true.
    n = 2, 返回 true.
    n = 3, 返回 false.
    n = 4, 返回 true.
    n = 5, 返回 true.

挑战

O(1) 时间复杂度且O(1) 存储。

**题解**

递推一下即可找到规律

```java
public class Solution {
    /**
     * @param n: an integer
     * @return: a boolean which equals to true if the first player will win
     */
    public boolean firstWillWin(int n) {
        // write your code here
        if (n % 3 == 0){
            return false;
        }
        else {
            return true;
        }
    }
}

```

---

## @@ 硬币排成线 II

有 n 个不同价值的硬币排成一条线。两个参赛者轮流从右边依次拿走 1 或 2 个硬币，直到没有硬币为止。计算两个人分别拿到的硬币总价值，价值高的人获胜。

请判定 第一个玩家 是输还是赢？

样例

    给定数组 A = [1,2,2], 返回 true.
    给定数组 A = [1,2,4], 返回 false.

**题解**

```python
class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        if not values:
            return True
        length = len(values)
        dp = [0 for i in range(length)]
        dp[length-1] = values[length-1]
        dp[length-2] = values[length-1] + values[length-2]
        for i in range(length - 3, -1, -1):
            if i + 4 <= length - 1:
                a = dp[i+4]
            else:
                a = 0
            if i + 3 <= length - 1:
                b = dp[i+3]
            else:
                b = 0
            if i + 2 <= length - 1:
                c = dp[i+2]
            else:
                c = 0

            v1 = values[i] + min(c, b)
            v2 = values[i] + values[i+1] + min(a,b)
            dp[i] = max(v1,v2)

        total = 0
        for j in range(length):
            total += values[j]

        second = total-dp[0]
        if dp[0] > second:
            return True
        else:
            return False

```

---

## @@ 用递归打印数字

用递归的方法找到从1到最大的N位整数。

样例

    给出 N = 1, 返回[1,2,3,4,5,6,7,8,9].
    给出 N = 2, 返回[1,2,3,4,5,6,7,8,9,10,11,...,99].

注意

用下面这种方式去递归其实很容易：

    recursion(i) {
        if i > largest number:
            return
        results.add(i)
        recursion(i + 1)
    }

但是这种方式会耗费很多的递归空间，导致堆栈溢出。你能够用其他的方式来递归使得递归的深度最多只有 N 层么？

挑战

用递归完成，而非循环的方式。

**题解**

注意整体思路的理解

```java
public class Solution {
    /**
     * @param n: An integer.
     * return : An array storing 1 to the largest number with n digits.
     */
    public List<Integer> numbersByRecursion(int n) {
        List<Integer> res = new ArrayList<Integer>();
        if (n >= 0) {
            sub(n, res);
        }
        return res;
    }

    private int sub(int n, List<Integer> res) {
        if (n == 0) {
            return 1;
        }
        int base = sub(n - 1, res);
        int size = res.size();
        for (int i = 1; i <= 9; i++) {
            int curBase = i * base;
            res.add(curBase);
            for (int j = 0; j < size; j++) {
                res.add(curBase + res.get(j));
            }
        }
        return base * 10;
    }
}

```

---

## @@ 两个整数相除

将两个整数相除，要求不使用乘法、除法和 mod 运算符。

如果溢出，返回 2147483647 。

样例

给定被除数 = 100 ，除数 = 9，返回 11。

**题解**

```java
public class Solution {
    /**
     * @param dividend the dividend
     * @param divisor the divisor
     * @return the result
     */
    public int divide(int dividend, int divisor) {
        if (divisor == 0) {
             return dividend >= 0? Integer.MAX_VALUE : Integer.MIN_VALUE;
        }

        if (dividend == 0) {
            return 0;
        }

        if (dividend == Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }

        boolean isNegative = (dividend < 0 && divisor > 0) ||
                             (dividend > 0 && divisor < 0);

        long a = Math.abs((long)dividend);
        long b = Math.abs((long)divisor);
        int result = 0;
        while(a >= b){
            a -= b;
            result++;
        }
        return isNegative? -result: result;
    }
}

```

---

## @@ 格雷编码

格雷编码是一个二进制数字系统，在该系统中，两个连续的数值仅有一个二进制的差异。

给定一个非负整数 n ，表示该代码中所有二进制的总数，请找出其格雷编码顺序。一个格雷编码顺序必须以 0 开始，并覆盖所有的 2n 个整数。

样例

给定 n = 2， 返回 [0,1,3,2]。其格雷编码顺序为：

    00 - 0
    01 - 1
    11 - 3
    10 - 2

注意

对于给定的 n，其格雷编码顺序并不唯一。

根据以上定义， [0,2,3,1] 也是一个有效的格雷编码顺序。

挑战

O(2n) 时间复杂度。

**题解**

n 位的格雷码可由 n-1位的格雷码递推，在最高位前顺序加0，逆序加1即可。实际实现时我们可以省掉在最高位加0的过程，因为其在数值上和前 n-1位格雷码相同。另外一点则是初始化的处理，图中为从1开始，但若从0开始可进一步简化程序。而且根据 格雷码 的定义，n=0时确实应该返回0.

加0 的那一部分已经在前一组格雷码中出现，故只需将前一组格雷码镜像后在最高位加1即可。第二重 for 循环中需要注意的是currGray.size() - 1并不是常量，只能用于给 j 初始化。本应该使用 2^n 和上一组格雷码相加，这里考虑到最高位为1的特殊性，使用位运算模拟加法更好。

```java
public class Solution {
    /**
     * @param n a number
     * @return Gray code
     */
    public ArrayList<Integer> grayCode(int n) {
        if (n < 0) return null;

        ArrayList<Integer> currGray = new ArrayList<Integer>();
        currGray.add(0);

        for (int i = 0; i < n; i++) {
            int msb = 1 << i;
            // backward - symmetry
            for (int j = currGray.size() - 1; j >= 0; j--) {
                currGray.add(msb | currGray.get(j));
            }
        }

        return currGray;
    }
}

```

---

## @@ 打劫房屋

假设你是一个专业的窃贼，准备沿着一条街打劫房屋。每个房子都存放着特定金额的钱。你面临的唯一约束条件是：相邻的房子装着相互联系的防盗系统，且 当相邻的两个房子同一天被打劫时，该系统会自动报警。

给定一个非负整数列表，表示每个房子中存放的钱， 算一算，如果今晚去打劫，你最多可以得到多少钱 在不触动报警装置的情况下。

样例

给定 [3, 8, 4], 返回 8.

挑战

O(n) 时间复杂度 且 O(1) 存储。

**题解**

用两个变量来代替 dp 中原来要有的数组

dp[i] = max(dp[i - 1], dp[i - 2] + num[i - 1])

```java
public class Solution {
    /**
     * @param A: An array of non-negative integers.
     * return: The maximum amount of money you can rob tonight
     */
    public long houseRobber(int[] A) {
        int length = A.length;
        long even = 0, odd = 0;
        for(int i = 0; i < A.length; i++){
            if(i % 2 == 1){
                odd = Math.max(odd + A[i], even);
            } else even = Math.max(even + A[i], odd);
        }
        return Math.max(even, odd);
    }
}

```

---

## @@ 最多有k个不同字符的最长子字符串

给定一个字符串，找到最多有k个不同字符的最长子字符串。

样例

例如，给定 s = "eceba" , k = 3,

T 是 "eceb"，长度为 4.

挑战
O(n), n 是所给字符串的长度

**题解**

解法是维护一个sliding window，以及一个hash map， key是char，value是这个char在当前window中得出现次数。
start和end是当前字符串的起始和终止index。
当当前window 字符数超过k的时候，从start开始remove，只要遇到一个char的个数降为0的时候，可以跳出，因为说明当前window的char个数已经为k-1,满足条件。
如果字符集比较小的话可以维护一个int[]来对char计数。

```java
public class Solution {
    /**
     * @param s : A string
     * @return : The length of the longest substring
     *           that contains at most k distinct characters.
     */
    public int lengthOfLongestSubstringKDistinct(String s, int k) {
        if (s == null || s.length() == 0 || k <= 0) {
            return 0;
        }
        int start = 0;
        int res = 1;
        Map<Character, Integer> map = new HashMap<Character, Integer>();
        map.put(s.charAt(0), 1);
        for (int end = 1; end < s.length(); end++) {
            char ch = s.charAt(end);
            if (map.containsKey(ch)) {
                map.put(ch, map.get(ch)+1);
            } else {
                if (map.size() == k) {
                    res = Math.max(res, end - start);
                    //full map, need to remove the first character in ths substring
                    for (int index = start; index < end; index++) {
                        map.put(s.charAt(index), map.get(s.charAt(index))-1);
                        start++;
                        if (map.get(s.charAt(index)) == 0) {
                            //have removed all occurance of a char
                            map.remove(s.charAt(index));
                            break;
                        }
                    }
                }
                map.put(ch, 1);
            }
        }
        res = Math.max(res, s.length() - start);
        return res;
    }
}

```

---

## @@ 最小差

给定两个整数数组（第一个是数组 A，第二个是数组 B），在数组 A 中取 A[i]，数组 B 中取 B[j]，A[i] 和 B[j]两者的差越小越好(|A[i] - B[j]|)。返回最小差。

样例

给定数组 A = [3,4,6,7]， B = [2,3,8,9]，返回 0。

挑战

时间复杂度 O(n log n)

**题解**

Given the hint of time complexity O(nlogn), we know that we should sort two arrays first, and then, use two pointers going through two arrays. To get the smallest difference, keep the tragedy of moving smaller pointer forward.

```java
public class Solution {
    /**
     * @param A, B: Two integer arrays.
     * @return: Their smallest difference.
     */
    public int smallestDifference(int[] A, int[] B) {
        Arrays.sort(A);
        Arrays.sort(B);

        int i = 0, j = 0;
        int min = Integer.MAX_VALUE;

        while (i < A.length && j < B.length) {
            min = Math.min(min, Math.abs(A[i] - B[j]));
            if (A[i] <= B[j]) {
                i++;
            } else {
                j++;
            }
        }
        return min;
    }
}


```

---

## @@ 数飞机

给出飞机的起飞和降落时间的列表，用 interval 序列表示. 请计算出天上同时最多有多少架飞机？

样例

对于每架飞机的起降时间列表：[[1,10],[2,3],[5,8],[4,7]], 返回3。

注意

如果多架飞机降落和起飞在同一时刻，我们认为降落有优先权。

**题解**

将interval的开始和结束都看做一个point，进行排序。对于排好序的数组便利，如果当前point是interval的开始点，那么cur++，否则cur–-。

```java
/**
 * Definition of Interval:
 * public classs Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 */

class Solution {
    /**
     * @param intervals: An interval array
     * @return: Count of airplanes are in the sky.
     */
    public int countOfAirplanes(List<Interval> airplanes) {
        if (airplanes == null || airplanes.size() == 0) {
            return 0;
        }
        //this round of sort is to make sure landing takes place before flying, if
        //they happen at the same time
        Collections.sort(airplanes, new Comparator<Interval>() {
            public int compare(Interval i1, Interval i2) {
                return Integer.compare(i1.start, i2.start);
            }
        });
        Point[] points = new Point[airplanes.size()*2];
        for (int i = 0; i < airplanes.size(); i++) {
            points[i*2] = new Point(airplanes.get(i).start, true);
            points[i*2 + 1] = new Point(airplanes.get(i).end, false);
        }
        Arrays.sort(points, new Comparator<Point>(){
            public int compare(Point i1, Point i2) {
                return Integer.compare(i1.time, i2.time);
            }
        });
        int res = 0;
        int cur = 0;
        for (Point p : points) {
            if (!p.isStart) {
                cur--;
            } else {
                cur++;
                res = Math.max(res, cur);
            }
        }
        return res;
    }

    class Point {
        int time;
        boolean isStart;
        public Point(int time, boolean isStart) {
            this.time = time;
            this.isStart = isStart;
        }
    }
}

```

---

## @@ 最长无重复字符的子串

给定一个字符串，请找出其中无重复字符的最长子字符串。

样例

例如，在"abcabcbb"中，其无重复字符的最长子字符串是"abc"，其长度为 3。

对于，"bbbbb"，其无重复字符的最长子字符串为"b"，长度为1。

挑战

O(n) 时间

**题解**

```java
public class Solution {
    /**
     * @param s: a string
     * @return: an integer
     */
    public int lengthOfLongestSubstring(String s) {
        if (s == null || s.length() == 0) {
            return 0;
        }

        HashSet<Character> set = new HashSet<Character>();

        int leftBound = 0, max = 0;
        for (int i = 0; i < s.length(); i++) {
            if (set.contains(s.charAt(i))) {
                while (leftBound < i && s.charAt(leftBound) != s.charAt(i)) {
                    set.remove(s.charAt(leftBound));
                    leftBound ++;
                }
                leftBound ++;
            } else {
                set.add(s.charAt(i));
                max = Math.max(max, i - leftBound + 1);
            }
        }

        return max;
    }
}

```

---

## @@ 装最多水的容器

给定 n 个非负整数 a1, a2, ..., an, 每个数代表了坐标中的一个点 (i, ai)。画 n 条垂直线，使得 i 垂直线的两个端点分别为(i, ai)和(i, 0)。找到两条线，使得其与 x 轴共同构成一个容器，以容纳最多水。

样例

给出[1,3,2], 最大的储水面积是2.

注意

容器不可倾斜。

**题解**

思路是从两头到中间扫描，设i,j分别指向height数组的首尾。

那么当前的area是min(height[i],height[j]) * (j-i)。

当height[i] < height[j]的时候，我们把i往后移，否则把j往前移，直到两者相遇。
这个正确性如何证明呢？

代码里面的注释说得比较清楚了，即每一步操作都能保证当前位置能取得的最大面积已经记录过了，而最开始初始化的时候最大面积记录过，所以有点类似于数学归纳法，证明这个算法是正确的。

```java
public class Solution {
    /**
     * @param heights: an array of integers
     * @return: an integer
     */
    public int maxArea(int[] heights) {
        int length = heights.length;
        if (length< 2) return 0;
        int i = 0, j = length - 1;
        int maxarea = 0;
        while(i < j) {
            int area = 0;
            if(heights[i] < heights[j]) {
                area = heights[i] * (j-i);
                //Since i is lower than j,
                //so there will be no jj < j that make the area from i,jj
                //is greater than area from i,j
                //so the maximum area that can benefit from i is already recorded.
                //thus, we move i forward.
                //因为i是短板，所以如果无论j往前移动到什么位置，都不可能产生比area更大的面积
                //换句话所，i能形成的最大面积已经找到了，所以可以将i向前移。
                ++i;
            } else {
                area = heights[j] * (j-i);
                //the same reason as above
                //同理
                --j;
            }
            if(maxarea < area) maxarea = area;
        }
        return maxarea;
    }
}

```

---

## @@ 乘积最大子序列

求出一个序列中乘积最大的连续子序列（至少包含一个数）。

比如, 序列 [2,3,-2,4] 中乘积最大的子序列为 [2,3] ，其乘积为6。

**题解**

用两个变量分别记录乘积的最大值和乘积的最小值.用一个变量记录当前值是否为负数.
让后遍历array中的每个数,并累乘起来,更新乘积的最大值和乘积的最小值.

取累乘的数值和当前的数值中大的,存为乘积的最大值
取累乘的数值和当前的数值中小的,存为乘积的最小值

因为:如果当前的数值较大,则前面的都可以抛弃不要,从当前的地方开始继续累乘可能会出现最大值; 如果累乘值较大,则后面可能会继续增大.
同理,如果当前值最小,则如果出现一个负数,可能反而会出现最大值.

所以要同时记录最大和最小值!

```java
public class Solution {
    /**
     * @param nums: an array of integers
     * @return: an integer
     */
    public int maxProduct(int[] nums) {
        int[] max = new int[nums.length];
        int[] min = new int[nums.length];

        min[0] = max[0] = nums[0];
        int result = nums[0];
        for (int i = 1; i < nums.length; i++) {
            min[i] = max[i] = nums[i];
            if (nums[i] > 0) {
                max[i] = Math.max(max[i], max[i - 1] * nums[i]);
                min[i] = Math.min(min[i], min[i - 1] * nums[i]);
            } else if (nums[i] < 0) {
                max[i] = Math.max(max[i], min[i - 1] * nums[i]);
                min[i] = Math.min(min[i], max[i - 1] * nums[i]);
            }

            result = Math.max(result, max[i]);
        }

        return result;
    }
}

```

---

## @@ 排列序号II

给出一个可能包含重复数字的排列，求这些数字的所有排列按字典序排序后该排列在其中的编号。编号从1开始。

样例

给出排列[1, 4, 2, 2]，其编号为3。

**题解**

这里需要考虑重复元素，有无重复元素最大的区别在于原来的1!, 2!, 3!...等需要除以重复元素个数的阶乘，颇有点高中排列组合题的味道。记录重复元素个数同样需要动态更新，引入哈希表这个万能的工具较为方便。

```java
public class Solution {
    /**
     * @param A an integer array
     * @return a long integer
     */
    public long permutationIndexII(int[] A) {
        if (A == null || A.length == 0) return 0;

        long index = 1;
        long factor = 1;
        for (int i = A.length - 1; i >= 0; i--) {
            HashMap<Integer, Integer> hash = new HashMap<Integer, Integer>();
            hash.put(A[i], 1);
            int rank = 0;
            for (int j = i + 1; j < A.length; j++) {
                if (hash.containsKey(A[j])) {
                    hash.put(A[j], hash.get(A[j]) + 1);
                } else {
                    hash.put(A[j], 1);
                }

                if (A[i] > A[j]) {
                    rank++;
                }
            }
            index += rank * factor / dupPerm(hash);
            factor *= (A.length - i);
        }

        return index;
    }

    private long dupPerm(HashMap<Integer, Integer> hash) {
        if (hash == null || hash.isEmpty()) return 1;

        long dup = 1;
        for (int val : hash.values()) {
            dup *= fact(val);
        }

        return dup;
    }

    private long fact(int num) {
        long val = 1;
        for (int i = 1; i <= num; i++) {
            val *= i;
        }

        return val;
    }
}

```

---


## @@ 丢失的第一个正整数

给出一个无序的正数数组，找出其中没有出现的最小正整数。

样例

如果给出 [1,2,0], return 3 如果给出 [3,4,-1,1], return 2

挑战

只允许时间复杂度O(n)的算法，并且只能使用常数级别的空间。

**题解**

容易想到的方案是先排序，然后遍历求得缺的最小整数。排序算法中常用的基于比较的方法时间复杂度的理论下界为 O(nlogn), 不符题目要求。常见的能达到线性时间复杂度的排序算法有 基数排序，计数排序 和 桶排序。

基数排序显然不太适合这道题，计数排序对元素落在一定区间且重复值较多的情况十分有效，且需要额外的 O(n) 空间，对这道题不太合适。最后就只剩下桶排序了，桶排序通常需要按照一定规则将值放入桶中，一般需要额外的 O(n) 空间，咋看一下似乎不太适合在这道题中使用，但是若能设定一定的规则原地交换原数组的值呢？这道题的难点就在于这种规则的设定。

设想我们对给定数组使用桶排序的思想排序，第一个桶放1，第二个桶放2，如果找不到相应的数，则相应的桶的值不变(可能为负值，也可能为其他值)。

那么怎么才能做到原地排序呢？即若 A[i]=x, 则将 x 放到它该去的地方 - A[x−1]=x, 同时将原来 A[x−1] 地方的值交换给 A[i].

排好序后遍历桶，如果不满足 f[i]=i+1, 那么警察叔叔就是它了！如果都满足条件怎么办？那就返回给定数组大小再加1呗。

```java
public class Solution {
    /**
     * @param A: an array of integers
     * @return: an integer
     */
    public int firstMissingPositive(int[] A) {
        int size = A.length;

        for (int i = 0; i < size; ++i) {
            while (A[i] > 0 && A[i] <= size &&
                  (A[i] != i + 1) && (A[i] != A[A[i] - 1])) {
                int temp = A[A[i] - 1];
                A[A[i] - 1] = A[i];
                A[i] = temp;
            }
        }

        for (int i = 0; i < size; ++i) {
            if (A[i] != i + 1) {
                return i + 1;
            }
        }

        return size + 1;
    }
}

```

核心代码为那几行交换，但是要很好地处理各种边界条件则要下一番功夫了，要能正常的交换，需满足以下几个条件：

1. A[i] 为正数，负数和零都无法在桶中找到生存空间...
2. A[i] \leq size 当前索引处的值不能比原数组容量大，大了的话也没用啊，肯定不是缺的第一个正数。
3. A[i] != i + 1, 都满足条件了还交换个毛线，交换也是自身的值。
4. A[i] != A[A[i] - 1], 避免欲交换的值和自身相同，否则有重复值时会产生死循环。
如果满足以上四个条件就可以愉快地交换彼此了，使用while循环处理，此时i并不自增，直到将所有满足条件的索引处理完。

---

## @@ 接雨水

给出 n 个非负整数，代表一张X轴上每个区域宽度为 1 的海拔图, 计算这个海拔图最多能接住多少（面积）雨水。

样例

如上图所示，海拔分别为 [0,1,0,2,1,0,1,3,2,1,2,1], 返回 6.

挑战

    O(n) 时间, O(1) 空间
    O(n) 时间, O(n) 空间也可以接受

**题解**

对于任何一个坐标，检查其左右的最大坐标，然后相减就是容积。所以，

1. 从左往右扫描一遍，对于每一个坐标，求取左边最大值。
2. 从右往左扫描一遍，对于每一个坐标，求最大右值。
3. 再扫描一遍，求取容积并加和。

```java
public class Solution {
    /**
     * @param heights: an array of integers
     * @return: a integer
     */
    public int trapRainWater(int[] heights) {
        if(heights.length < 3) return 0;
        int max = heights[0];
        int[] left = new int[heights.length];
        int[] right = new int[heights.length];
        int sum = 0;

        for(int i = 1; i < heights.length-1; i++){
            left[i] = max;
            if(heights[i] > max){
                max = heights[i];
            }
        }
        max = heights[heights.length-1];
        for(int i = heights.length-2; i >=1; i--){
            right[i] = max;
            if(heights[i] > max){
                max = heights[i];
            }
        }
        for(int i = 1; i < heights.length-1; i++){
            int cur = Math.min(left[i], right[i]) - heights[i];
            if(cur > 0){
                sum += cur;
            }
        }
        return sum;
    }
}

```

---

## @@ 第k个排列

给定 n 和 k，求123..n组成的排列中的第 k 个排列。

样例

对于 n = 3, 所有的排列如下：

    123
    132
    213
    231
    312
    321

如果 k = 4, 第4个排列为，231.

注意

1 ≤ n ≤ 9

**题解**

基本的想法是，对于第k个排列，{a1, a2, a3, ..., an}, a1 是多少呢？

因为{a2, a3, ..., an} 一共有 (n-1)!种，a1在num中的index相当于 k / (n-1)!。换句话解释，就是一共有n个block，每个block大小是(n-1)!这么大，现在要求的就是在哪个block。

同理，求a2的时候，a1（在哪个block）已经求出来了，update k = k % (n-1)!, block的大小变成了(n-2)!, 这又是一个子问题了。

```java
class Solution {
    /**
      * @param n: n
      * @param k: the kth permutation
      * @return: return the k-th permutation
      */
    public String getPermutation(int n, int k) {
        int[] num = new int[n];
        int perNumCount = 1;

        for(int i = 0; i < n; i++) {
            num[i] = i+1;
            perNumCount *= i + 1;
        }
        k--;
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < n; i++) {
            perNumCount = perNumCount / (n - i);
            int choosed = k / perNumCount;
            sb.append(String.valueOf(num[choosed]));
            for(int j = choosed; j < n - i - 1; j++) {
                num[j] = num[j+1]; 
            }
            k = k % perNumCount;
        }
        return sb.toString();
    }
}


```

---

## @@ 最大数

给出一组非负整数，重新排列他们的顺序把他们组成一个最大的整数

样例

给出样例 [1, 20, 23, 4, 8]，返回组合最大的整数为8423201

注意

最后的结果可能很大，所以我们返回一个字符串来代替这个整数

**题解**

Override comparator:  put the larger number ahead of smaller number.

```java
public class Solution {
    /**
     *@param num: A list of non negative integers
     *@return: A string
     */
    public String largestNumber(int[] num) {
        if (num == null || num.length == 0) {
            return "0";
        }

        String[] strs = new String[num.length];
        for (int i = 0; i < num.length; i++) {
            strs[i] = Integer.toString(num[i]);
        }

        Arrays.sort(strs, new NumberComparator());

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < strs.length; i++) {
            sb.append(strs[i]);
        }
        String res = sb.toString();

        if(res.charAt(0) == '0') {
            return "0";
        }

        return res;
    }


    class NumberComparator implements Comparator<String> {
        @Override
        public int compare(String s1, String s2){
            return (s2 + s1).compareTo(s1 + s2);
        }
    }
}

```

---

## @@ 删除数字

给出一个字符串 A, 表示一个 n 位正整数, 删除其中 k 位数字, 使得剩余的数字仍然按照原来的顺序排列产生一个新的正整数。

找到删除 k 个数字之后的最小正整数。

N <= 240, k <= N

样例

给出一个字符串代表的正整数 A 和一个整数 k, 其中 A = 178542, k = 4

返回一个字符串 "12"

**题解**

这道题跟Leetcode里面的那道Next Permutation很像，那个题要找比一个数大的下一个数，于是从这个数的右边开始，找第一个递减的位置所在。这道题也是类似，只不过从这个数的左边开始，找第一个递减的位置所在。那道题是想要改动的影响最小，所以从右边开始扫描。这道题是想要改动的影响最大，所以从左边开始扫描。

这道题，删掉一个数，相当于用这个数后面的数代替这个数。所以后面这个数一定要比当前小才行。所以找的是第一个递减的位置，把大的那个数删了。

这样做一次就是找到了：删除哪一个数，使得剩下的数最小。对剩下的数再做k次，就可以找到删除哪k个数，使得剩下的数最小。这其实是一个Greedy算法，因为这样每做一次，得到的都是当前最优的结果。

看起来需要O(Nk)时间复杂度，但其实用一个Stack，再记录pop了几次，O(2N)就好了

```java
public class Solution {
    /**
     *@param A: A positive integer which has N digits, A is a string.
     *@param k: Remove k digits.
     *@return: A string
     */
    public String DeleteDigits(String A, int k) {
        Stack<Integer> st = new Stack<Integer>();
        int popCount = 0;
        StringBuffer res = new StringBuffer();
        for (int i=0; i<A.length(); i++) {
            int num = (int)(A.charAt(i) - '0');
            if (st.isEmpty()) st.push(num);
            else if (num >= st.peek()) {
                st.push(num);
            }
            else {
                if (popCount < k) {
                    st.pop();
                    i--;
                    popCount++;
                }
                else {
                    st.push(num);
                }
            }
        }
        while (popCount < k) {
            st.pop();
            popCount++;
        }
        while (!st.isEmpty()) {
            res.insert(0, st.pop());
        }
        while (res.length() > 1 && res.charAt(0) == '0') {
            res.deleteCharAt(0);
        }
        return res.toString();
    }
}

```

---

## @@ 木材加工

有一些原木，现在想把这些木头切割成一些长度相同的小段木头，需要得到的小段的数目至少为 k。当然，我们希望得到的小段越长越好，你需要计算能够得到的小段木头的最大长度。

样例

有3根木头[232, 124, 456], k=7, 最大长度为114.

注意

木头长度的单位是厘米。原木的长度都是正整数，我们要求切割得到的小段木头的长度也要求是整数。无法切出要求至少 k 段的,则返回 0 即可。

挑战

O(n log Len), Len为 n 段原木中最大的长度

**题解**

这道题要直接想到二分搜素其实不容易，但是看到题中 Challenge 的提示后你大概就能想到往二分搜索上靠了。首先来分析下题意，题目意思是说给出 n 段木材L[i], 将这 n 段木材切分为至少 k 段，这 k 段等长，求能从 n 段原材料中获得的最长单段木材长度。以 k=7 为例，要将 L 中的原材料分为7段，能得到的最大单段长度为114, 232/114 = 2, 124/114 = 1, 456/114 = 4, 2 + 1 + 4 = 7.

理清题意后我们就来想想如何用算法的形式表示出来，显然在计算如2, 1, 4等分片数时我们进行了取整运算，在计算机中则可以使用下式表示：

∑^(i=1)~(​n) (L[i]/l) ≥ k
​​
其中 l 为单段最大长度，显然有 1 ≤ l ≤ max(L[i]). 单段长度最小为1，最大不可能超过给定原材料中的最大木材长度。

注意求和与取整的顺序，是先求 L[i]/l的单个值，而不是先对L[i]求和。

分析到这里就和题 Sqrt x 差不多一样了，要求的是 l 的最大可能取值，同时
l 可以看做是从有序序列[1, max(L[i])]的一个元素，典型的二分搜索！

```java
public class Solution {
    /**
     *@param L: Given n pieces of wood with length L[i]
     *@param k: An integer
     *return: The maximum length of the small pieces.
     */
    public int woodCut(int[] L, int k) {
        if(L == null || L.length == 0) return 0;
        if(L.length == 1){
            return L[0] / (L[0] / k);
        }
        Arrays.sort(L);
        int start = 1, end = L[L.length - 1];
        int max = 0;
        while(start <= end){
            int mid = (end - start) / 2 + start;
            int count = 0;
            for(int l : L){
                count += (l / mid);
            }
            if(count < k){
                end = mid-1;
            } else{
                start = mid+1;
                max = mid;
            }
        }
        return max;
    }
}

```

---

## @@ 寻找旋转排序数组中的最小值

假设一个旋转排序的数组其起始位置是未知的（比如0 1 2 4 5 6 7 可能变成是4 5 6 7 0 1 2）。

你需要找到其中最小的元素。

你可以假设数组中不存在重复的元素。

样例

给出[4,5,6,7,0,1,2]  返回 0

**题解**

1.如何找中间断开的区间（也就是说旋转过）

我们的目的是要找出存在断口的地方。所以我们可以每次求一下mid的值，把mid 跟左边比一下，如果是正常序，就丢掉左边，反之丢掉右边，不断反复直到找到断口。

分析一下：

比如4 5 6 7 0 1 2  从中间断开后，它是由一个有序跟一个无序的序列组成的。

如果left = 0, right = 6,mid = 3, 那么4， 5， 6， 7 是正序， 7， 0， 1， 2是逆序，所以我们要丢掉左边。这样反复操作，直到数列中只有2个数字，就是断开处，这题我们会得到7，0，返回后一个就可以了。

2.特别的情况：

如果发现 A.mid > A.left，表示左边是有序，丢掉左边。

如果发现 A.mid < A.left, 表示无序的状态在左边，丢掉右边

如果A.mid = A.left，说明无法判断。这时我们可以把left++，丢弃一个即可。不必担心丢掉我们的目标值。因为A.left == A.mid，即使丢掉了left,还有mid在嘛！

每次进入循环，我们都要判断A.left < A.right，原因是，前面我们丢弃一些数字时，有可能造成余下的数组是有序的，这时应直接返回A.left! 否则的话 我们可能会丢掉解。

就像以下的例子，在1 10 10中继续判断会丢弃1 10.

举例: 10 1 10 10 如果我们丢弃了最左边的10，则1 10 10 是有序的

```java
public class Solution {
    /**
     * @param num: a rotated sorted array
     * @return: the minimum number in the array
     */
    public int findMin(int[] num) {
        if (num == null || num.length == 0) {
            return 0;
        }

        int len = num.length;
        if (len == 1) {
            return num[0];
        } else if (len == 2) {
            return Math.min(num[0], num[1]);
        }

        int left = 0;
        int right = len - 1;

        while (left < right - 1) {
            int mid = left + (right - left) / 2;
            // In this case, the array is sorted.
            // 这一句很重要，因为我们移除一些元素后，可能会使整个数组变得有序...
            if (num[left] < num[right]) {
                return num[left];
            }

            // left side is sorted. CUT the left side.
            if (num[mid] > num[left]) {
                left = mid;
            // left side is unsorted, right side is sorted. CUT the right side.
            } else if (num[mid] < num[left]) {
                right = mid;
            } else {
                left++;
            }
        }

        return Math.min(num[left], num[right]);
    }
}

```

---

## @@ 寻找旋转排序数组中的最小值 II

假设一个旋转排序的数组其起始位置是未知的（比如0 1 2 4 5 6 7 可能变成是4 5 6 7 0 1 2）。

你需要找到其中最小的元素。

数组中可能存在重复的元素。

**题解**

1.如何找中间断开的区间（也就是说旋转过）

我们的目的是要找出存在断口的地方。所以我们可以每次求一下mid的值，把mid 跟左边比一下，如果是正常序，就丢掉左边，反之丢掉右边，不断反复直到找到断口。

分析一下：

比如4 5 6 7 0 1 2  从中间断开后，它是由一个有序跟一个无序的序列组成的。

如果left = 0, right = 6,mid = 3, 那么4， 5， 6， 7 是正序， 7， 0， 1， 2是逆序，所以我们要丢掉左边。这样反复操作，直到数列中只有2个数字，就是断开处，这题我们会得到7，0，返回后一个就可以了。

2.特别的情况：

如果发现 A.mid > A.left，表示左边是有序，丢掉左边。

如果发现 A.mid < A.left, 表示无序的状态在左边，丢掉右边

如果A.mid = A.left，说明无法判断。这时我们可以把left++，丢弃一个即可。不必担心丢掉我们的目标值。因为A.left == A.mid，即使丢掉了left,还有mid在嘛！

每次进入循环，我们都要判断A.left < A.right，原因是，前面我们丢弃一些数字时，有可能造成余下的数组是有序的，这时应直接返回A.left! 否则的话 我们可能会丢掉解。

就像以下的例子，在1 10 10中继续判断会丢弃1 10.

举例: 10 1 10 10 如果我们丢弃了最左边的10，则1 10 10 是有序的

```java
public class Solution {
    /**
     * @param num: a rotated sorted array
     * @return: the minimum number in the array
     */
    public int findMin(int[] num) {
        if (num == null || num.length == 0) {
            return 0;
        }

        int len = num.length;
        if (len == 1) {
            return num[0];
        } else if (len == 2) {
            return Math.min(num[0], num[1]);
        }

        int left = 0;
        int right = len - 1;

        while (left < right - 1) {
            int mid = left + (right - left) / 2;
            // In this case, the array is sorted.
            // 这一句很重要，因为我们移除一些元素后，可能会使整个数组变得有序...
            if (num[left] < num[right]) {
                return num[left];
            }

            // left side is sorted. CUT the left side.
            if (num[mid] > num[left]) {
                left = mid;
            // left side is unsorted, right side is sorted. CUT the right side.
            } else if (num[mid] < num[left]) {
                right = mid;
            } else {
                left++;
            }
        }

        return Math.min(num[left], num[right]);
    }
}

```

---

## @@ 旋转图像

给定一个N×N的二维矩阵表示图像，90度顺时针旋转图像。

样例

给出一个矩形[[1,2],[3,4]]，90度顺时针旋转后，返回[[3,1],[4,2]]

挑战

能否在原地完成？

**题解**

一次转一层，画图即可

```java
public class Solution {
    /**
     * @param matrix: A list of lists of integers
     * @return: Void
     */
    public void rotate(int[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return;
        }

        int length = matrix.length;

        for (int i = 0; i < length / 2; i++) {
            for (int j = 0; j < (length + 1) / 2; j++){
                int tmp = matrix[i][j];
                matrix[i][j] = matrix[length - j - 1][i];
                matrix[length -j - 1][i] = matrix[length - i - 1][length - j - 1];
                matrix[length - i - 1][length - j - 1] = matrix[j][length - i - 1];
                matrix[j][length - i - 1] = tmp;
            }
        }
    }
}

```

---

## @@ 矩阵归零

给定一个m×n矩阵，如果一个元素是0，则将其所在行和列全部元素变成0。

需要在原地完成。

样例

给出一个矩阵[[1,2],[0,3]]，返回[[0,2],[0,0]]

挑战

你是否使用了额外的空间？

一个直接的解决方案是使用O(MN)的额外空间，但这并不是一个好的方案。

一个简单的改进方案是使用O(M + N)的额外空间，但这仍然不是最好的解决方案。

你能想出一个常数空间的解决方案吗？

**题解**

1. 设置两个布尔型标示符flag_row,flag_col用来保存第0行和第0列是否需要置0,初始值false
2. 遍历第0行，如果遇到0，则将flag_row=true
3. 同上遍历第0列，如果遇到0，则将flag_col=true
4. 遍历剩下的元素即i从1开始，j从一开始，如果遇到某个元素【i,j】为0，则将matrix[i][0]=0,matrix[0][j]=0
5. 遍历第0行，遇到matrix[0][j]=0则设置此列上的所有元素为0
6. 遍历第0列，遇到matrix[i][0]=0则设置此行上的所有元素为0
7. 判断flag_row是否为true，是的话设置第0行元素均为0
8. 判断flag_col是否为true，是的话设置第0列元素均为0
9. 至此，题目完成

```java
public class Solution {
    /**
     * @param matrix: A list of lists of integers
     * @return: Void
     */
    public void setZeroes(int[][] matrix) {
        int row = matrix.length;
        if (row == 0) {
            return;
        }
        int col = matrix[0].length;

        int rowIndex = 0;
        int colIndex = 0;
        boolean stop = false;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (matrix[i][j] == 0) {
                    rowIndex = i;
                    colIndex = j;
                    stop = true;
                    break;
                }
            }
            if (stop) {
                break;
            }
        }

        if (!stop) {
            return;
        }

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (i == rowIndex || j == colIndex) {
                    continue;
                }

                if (matrix[i][j] == 0) {
                    matrix[rowIndex][j] = 0;
                    matrix[i][colIndex] = 0;
                }
            }
        }

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (i == rowIndex || j == colIndex) {
                    continue;
                }
                if (matrix[rowIndex][j] == 0 || matrix[i][colIndex] == 0) {
                    matrix[i][j] = 0;
                }
            }
        }

        for (int i = 0; i < row; i++) {
            matrix[i][colIndex] = 0;
        }
        for (int j = 0; j < col; j++) {
            matrix[rowIndex][j] = 0;
        }
    }
}

```

---

## @@ 不同的二叉查找树

给出 n，问由 1...n 为节点组成的不同的二叉查找树有多少种？

样例

给出n = 3，有5种不同形态的二叉查找树：

    1           3    3       2      1
     \         /    /       / \      \
      3      2     1       1   3      2
     /      /       \                  \
    2     1          2                  3

**题解**

The case for 3 elements example

    Count[3] = Count[0]*Count[2]  (1 as root)
               + Count[1]*Count[1]  (2 as root)
               + Count[2]*Count[0]  (3 as root)

Therefore, we can get the equation:

    count[n] = sum(count[0..k]*count[k+1...n]) 0 <= k < n-1

```java
public class Solution {
    /**
     * @paramn n: An integer
     * @return: An integer
     */
    public int numTrees(int n) {
        int[] count = new int[n+2];
        count[0] = 1;
        count[1] = 1;

        for(int i=2;  i<= n; i++){
            for(int j=0; j<i; j++){
                count[i] += count[j] * count[i - j - 1];
            }
        }
        return count[n];
    }
}

```

---

## @@ 不同的二叉查找树 II

给出n，生成所有由1...n为节点组成的不同的二叉查找树

样例

给出n = 3，生成所有5种不同形态的二叉查找树：

    1         3     3       2    1
     \       /     /       / \    \
      3     2     1       1   3    2
     /     /       \                \
    2     1         2                3

**题解**

使用递归来做。

1. 先定义递归的参数为左边界、右边界，即1到n.
2. 考虑从left, 到right 这n个数字中选取一个作为根，余下的使用递归来构造左右子树。
3. 当无解时，应该返回一个null树，这样构造树的时候，我们会比较方便，不会出现左边解为空，或是右边解为空的情况。
4. 如果说左子树有n种组合，右子树有m种组合，那最终的组合数就是n*m. 把这所有的组合组装起来即可

```java
/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @paramn n: An integer
     * @return: A list of root
     */
    public List<TreeNode> generateTrees(int n) {
        return dfs(1, n);
    }

    public List<TreeNode> dfs(int left, int right) {
        List<TreeNode> ret = new ArrayList<TreeNode>();

        // The base case;
        if (left > right) {
            ret.add(null);
            return ret;
        }

        for (int i = left; i <= right; i++) {
            List<TreeNode> lTree = dfs(left, i - 1);
            List<TreeNode> rTree = dfs(i + 1, right);
            for (TreeNode nodeL: lTree) {
                for (TreeNode nodeR: rTree) {
                    TreeNode root = new TreeNode(i);
                    root.left = nodeL;
                    root.right = nodeR;
                    ret.add(root);
                }
            }
        }

        return ret;
    }
}

```

---

## @@ 更新二进制位

给出两个32位的整数N和M，以及两个二进制位的位置i和j。写一个方法来使得N中的第i到j位等于M（M会是N中从第i为开始到第j位的子串）

样例

给出N = (10000000000)2，M = (10101)2， i = 2, j = 6

返回 N = (10001010100)2

挑战

最少的操作次数是多少？

**题解**

Cracking The Coding Interview 上的题，题意简单来讲就是使用 M 代替 N 中的第i位到第j位。很显然，我们需要借用掩码操作。大致步骤如下：

1. 得到第i位到第j位的比特位为0，而其他位均为1的掩码mask。
2. 使用mask与 N 进行按位与，清零 N 的第i位到第j位。
3. 对 M 右移i位，将 M 放到 N 中指定的位置。
4. 返回 N | M 按位或的结果。

获得掩码mask的过程可参考 CTCI 书中的方法，先获得掩码(1111...000...111)的左边部分，然后获得掩码的右半部分，最后左右按位或即为最终结果。

在给定测试数据[-521,0,31,31]时出现了 WA, 也就意味着目前这段程序是存在 bug 的，此时m = 0, i = 31, j = 31，仔细瞅瞅到底是哪几行代码有问题？本地调试后发现问题出在left那一行，left移位后仍然为ones, 这是为什么呢？在j为31时j + 1为32，也就是说此时对left位移的操作已经超出了此时int的最大位宽！

使用~0获得全1比特位，在j == 31时做特殊处理，即不必求left。求掩码的右侧1时使用了(1 << i) - 1, 题中有保证第i位到第j位足以容纳 M, 故不必做溢出处理。

```java
class Solution {
    /**
     *@param n, m: Two integer
     *@param i, j: Two bit positions
     *return: An integer
     */
    public int updateBits(int n, int m, int i, int j) {
        int mask;
        if (j < 31) {
            mask = ~((1 << (j + 1)) - (1 << i));
        } else {
            mask = (1 << i) - 1;
        }
        return (m << i) + (mask & n);
    }
}


```

---

## @@ 旋转链表

给定一个链表，旋转链表，使得每个节点向右移动k个位置，其中k是一个非负数

样例

    给出链表1->2->3->4->5->null和k=2
    返回4->5->1->2->3->null

**题解**

```java
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param head: the List
     * @param k: rotate to the right k places
     * @return: the list after rotation
     */
    public ListNode rotateRight(ListNode head, int k) {
        int len = 0;
        ListNode run = head;
        if(head == null || head.next == null) return head;
        while(run != null){
            len++;
            run = run.next;
        }

        k = k % len;
        int m = len - k;

        ListNode nextHead = head;
        ListNode pre = null;

        while(m-- > 0){
            pre = nextHead;
            nextHead = nextHead.next;
        }
        pre.next = null;
        run = nextHead;
        while(run.next != null){
            run = run.next;
        }

        run.next = head;
        return nextHead;
    }
}

```

---

## @@ 乱序字符串

给出一个字符串数组S，找到其中所有的乱序字符串(Anagram)。如果一个字符串是乱序字符串，那么他存在一个字母集合相同，但顺序不同的字符串也在S中。

样例

对于字符串数组 ["lint","intl","inlt","code"]

返回 ["lint","inlt","intl"]

注意

所有的字符串都只包含小写字母

**题解**

在题 Two Strings Are Anagrams | Data Structure and Algorithm 中曾介绍过使用排序和 hashmap 两种方法判断变位词。这里我们将这两种方法同时引入！只不过此时的 hashmap 的 key 为字符串，value 为该字符串在 vector 中出现的次数。两次遍历字符串数组，第一次遍历求得排序后的字符串数量，第二次遍历将排序后相同的字符串取出放入最终结果中。

```java
public class Solution {
    /**
     * @param strs: A list of strings
     * @return: A list of strings
     */
    public List<String> anagrams(String[] strs) {
        List<String> ret = new ArrayList<String>();

        if (strs == null) {
            return ret;
        }

        HashMap<String, List<String>> map = new HashMap<String, List<String>>();

        int len = strs.length;
        for (int i = 0; i < len; i++) {
            String s = strs[i];

            // Sort the string.
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String strSort = new String(chars);

            // Create a ArrayList for the sorted string.
            if (!map.containsKey(strSort)) {
                map.put(strSort, new ArrayList<String>());
            }

            // Add a new string to the list of the hashmap.
            map.get(strSort).add(s);
        }

        // go through the map and add all the strings into the result.
        for (Map.Entry<String, List<String>> entry: map.entrySet()) {
            List<String> list = entry.getValue();

            // skip the entries which only have one string.
            if (list.size() == 1) {
                continue;
            }

            // add the strings into the list.
            ret.addAll(list);
        }

        return ret;
    }
}

```

---

## @@ 图中两个点之间的路线

给出一张有向图，设计一个算法判断两个点 s 与 t 之间是否存在路线。

样例

如下图:

    A----->B----->C
     \     |
      \    |
       \   |
        \  v
         ->D----->E

for s = B and t = E, return true

for s = D and t = C, return false

**题解**

bfs dfs 均可，不要递归即可

```java
/**
 * Definition for Directed graph.
 * class DirectedGraphNode {
 *     int label;
 *     ArrayList<DirectedGraphNode> neighbors;
 *     DirectedGraphNode(int x) {
 *         label = x;
 *         neighbors = new ArrayList<DirectedGraphNode>();
 *     }
 * };
 */
public class Solution {
   /**
     * @param graph: A list of Directed graph node
     * @param s: the starting Directed graph node
     * @param t: the terminal Directed graph node
     * @return: a boolean value
     */
    public boolean hasRoute(ArrayList<DirectedGraphNode> graph,
                            DirectedGraphNode s, DirectedGraphNode t) {
        if (s == t) {
            return true;
        }
        if (graph == null || graph.size() == 0 || s == null || t == null) {
            return false;
        }
        Set<DirectedGraphNode> visited = new HashSet<DirectedGraphNode>();
        Stack<DirectedGraphNode> stack = new Stack<DirectedGraphNode>();
        stack.push(s);
        while (!stack.isEmpty()) {
            DirectedGraphNode node = stack.pop();
            if (visited.contains(node)) {
                continue;
            }
            visited.add(node);
            for (DirectedGraphNode neighbor : node.neighbors) {
                if (neighbor == t) {
                    return true;
                }
                stack.push(neighbor);
            }
        }
        return false;
    }
}

```

---

## @@ 数字组合

给出一组候选数字(C)和目标数字(T),找到C中所有的组合，使找出的数字和为T。C中的数字可以无限制重复被选取。

例如,给出候选数组[2,3,6,7]和目标数字7，所求的解为：

[7]，

[2,2,3]

样例

给出候选数组[2,3,6,7]和目标数字7

返回 [[7],[2,2,3]]

注意

+ 所有的数字(包括目标数字)均为正整数。
+ 元素组合(a1, a2, … , ak)必须是非降序(ie, a1 ≤ a2 ≤ … ≤ ak)。
+ 解集不能包含重复的组合

**题解**

和 Permutations 十分类似，区别在于剪枝函数不同。这里允许一个元素被多次使用，故递归时传入的索引值不自增，而是由 for 循环改变。

对数组首先进行排序是必须的，递归函数中本应该传入 target 作为入口参数，这里借用了 Soulmachine 的实现，使用 gap 更容易理解。注意在将临时 list 添加至 result 中时需要 new 一个新的对象。

复杂度分析

按状态数进行分析，时间复杂度 O(n!), 使用了list 保存中间结果，空间复杂度 O(n).

```java
public class Solution {
    /**
     * @param candidates: A list of integers
     * @param target:An integer
     * @return: A list of lists of integers
     */
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> list = new ArrayList<Integer>();
        if (candidates == null) return result;

        Arrays.sort(candidates);
        helper(candidates, 0, target, list, result);

        return result;
    }

    private void helper(int[] candidates, int pos, int gap,
                        List<Integer> list, List<List<Integer>> result) {

        if (gap == 0) {
            // add new object for result
            result.add(new ArrayList<Integer>(list));
            return;
        }

        for (int i = pos; i < candidates.length; i++) {
            // cut invalid candidate
            if (gap < candidates[i]) {
                return;
            }
            list.add(candidates[i]);
            helper(candidates, i, gap - candidates[i], list, result);
            list.remove(list.size() - 1);
        }
    }
}

```

---

## @@ 数字组合 II

给出一组候选数字(C)和目标数字(T),找出C中所有的组合，使组合中数字的和为T。C中每个数字在每个组合中只能使用一次

样例

给出一个例子，候选数字集合为[10,1,6,7,2,1,5] 和目标数字 8  ,

解集为：[[1,7],[1,2,5],[2,6],[1,1,6]]

注意

+ 所有的数字(包括目标数字)均为正整数。
+ 元素组合(a1, a2, … , ak)必须是非降序(ie, a1 ≤ a2 ≤ … ≤ ak)。
+ 解集不能包含重复的组合。

**题解**

```java
public class Solution {
    /**
     * @param num: Given the candidate numbers
     * @param target: Given the target number
     * @return: All the combinations that sum to target
     */
    public List<List<Integer>> combinationSum2(int[] num, int target) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> list = new ArrayList<Integer>();
        if (num == null) return result;

        Arrays.sort(num);
        helper(num, 0, target, list, result);

        return result;
    }

    private void helper(int[] nums, int pos, int gap,
                        List<Integer> list, List<List<Integer>> result) {

        if (gap == 0) {
            result.add(new ArrayList<Integer>(list));
            return;
        }

        for (int i = pos; i < nums.length; i++) {
            // ensure only the first same num is chosen, remove duplicate list
            if (i != pos && nums[i] == nums[i - 1]) {
                continue;
            }
            // cut invalid num
            if (gap < nums[i]) {
                return;
            }
            list.add(nums[i]);
            // i + 1 ==> only be used once
            helper(nums, i + 1, gap - nums[i], list, result);
            list.remove(list.size() - 1);
        }
    }
}

```

---

## @@ 交错正负数

给出一个含有正整数和负整数的数组，重新排列成一个正负数交错的数组。

样例

给出数组[-1, -2, -3, 4, 5, 6]，重新排序之后，变成[-1, 5, -2, 4, -3, 6]或者其他任何满足要求的答案

注意

不需要保持正整数或者负整数原来的顺序。

挑战

原地完成，没有额外的空间

**题解**

这道题没有给出正数、负数谁多谁少，所以需要先统计数量，数量多的要包着数量少的，然后数组尾部全是数量多的数

```java
class Solution {
    /**
     * @param A: An integer array.
     * @return: void
     */
    public void rerange(int[] A) {
        int posNum = 0, negNum = 0;
        for (int elem : A) {
            if (elem < 0) {
                negNum++;
            }
            else {
                posNum++;
            }
        }
        int posInd = 1, negInd = 0;
        if (posNum > negNum) {
            negInd = 1;
            posInd = 0;
        }
        while (posInd<A.length && negInd<A.length) {
            while (posInd < A.length && A[posInd] > 0) {
                posInd += 2;
            }
            while (negInd < A.length && A[negInd] < 0) {
                negInd += 2;
            }
            if (posInd<A.length && negInd<A.length) {
                swap(A, posInd, negInd);
            }
        }
        return ;
   }

   public void swap(int[] A, int l, int r) {
       int temp = A[l];
       A[l] = A[r];
       A[r] = temp;
   }
}

```

---



## @@ 快速幂

计算 a^n % b，其中a，b和n都是32位的整数。

样例

例如 231 % 3 = 2

例如 1001000 % 1000 = 0

挑战

O(logn)

**题解**

数学题，考察整数求模的一些特性，不知道这个特性的话此题一时半会解不出来，本题中利用的关键特性为：

(a * b) % p = ((a % p) * (b % p)) % p
即 a 与 b 的乘积模 p 的值等于 a, b 分别模 p 相乘后再模 p 的值，只能帮你到这儿了，不看以下的答案先想想知道此关系后如何解这道题。

首先不太可能先把 a^n 具体值求出来，太大了... 所以利用以上求模公式，可以改写为：

a^n = a^(n/2)⋅a^(n/2) = a^(n/4)⋅a^(n/4)⋅a^(n/4)⋅a^(n/4) = ...
​​
至此递归模型建立。

```java
class Solution {
    /*
     * @param a, b, n: 32bit integers
     * @return: An integer
     */
    public int fastPower(int a, int b, int n) {
       if (n == 1) {
            return a % b;
        } else if (n == 0) {
            return 1 % b;
        } else if (n < 0) {
            return -1;
        }

        // (a * b) % p = ((a % p) * (b % p)) % p
        // use long to prevent overflow
        long product = fastPower(a, b, n / 2);
        product = (product * product) % b;
        if (n % 2 == 1) {
            product = (product * a) % b;
        }

        // cast long to int
        return (int) product;
    }
};

```

源码分析

分三种情况讨论 n 的值，需要特别注意的是n == 0，虽然此时 a0 的值为1，但是不可直接返回1，因为b == 1时应该返回0，故稳妥的写法为返回1 % b.

递归模型中，需要注意的是要分 n 是奇数还是偶数，奇数的话需要多乘一个 a, 保存乘积值时需要使用long型防止溢出，最后返回时强制转换回int。

复杂度分析

使用了临时变量product，空间复杂度为 O(1), 递归层数约为 logn, 时间复杂度为 O(logn), 栈空间复杂度也为 O(logn).

---

## @@ 组合

给出两个整数n和k，返回从1......n中选出的k个数的组合。

样例

例如 n = 4 且 k = 2

返回的解为：

[[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]

**题解**

```java
public class Solution {
    /**
     * @param n: Given the range of numbers
     * @param k: Given the numbers of combinations
     * @return: All the combinations of k numbers out of 1..n
     */
    public List<List<Integer>> combine(int n, int k) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> list = new ArrayList<Integer>();
        if (n <= 0 || k <= 0) return result;

        helper(n, k, 1, list, result);
        return result;
    }

    private void helper(int n, int k, int pos,
                        List<Integer> list, List<List<Integer>> result) {

        if (list.size() == k) {
            result.add(new ArrayList<Integer>(list));
            return;
        }

        for (int i = pos; i <= n; i++) {
            list.add(i);
            helper(n, k, i + 1, list, result);
            list.remove(list.size() - 1);
        }
    }
}

```

---

## @@ 颜色分类

给定一个包含红，白，蓝且长度为n的数组，将数组元素进行分类使相同颜色的元素相邻，并按照红、白、蓝的顺序进行排序。

我们可以使用整数0，1和2分别代表红，白，蓝。

注意
不能使用代码库中的排序函数来解决这个问题

说明

一个相当直接的解决方案是使用计数排序扫描2遍的算法。

首先，迭代数组计算0,1,2出现的次数，然后依次用0,1,2出现的次数去覆盖数组。

你否能想出一个仅使用常数级额外空间复杂度且只扫描遍历一遍数组的算法？

**题解**

By keeping three pointers, red = 0, blue = n - 1, and use white to scan through the whole array, when encountering 0, swap A[red] and A[white], when encountering 2, swap A[blue] and A[white] and move the pointers red, white, blue correspondingly

```java
class Solution {
    /**
     * @param nums: A list of integer which is 0, 1 or 2
     * @return: nothing
     */
    public void sortColors(int[] nums) {
        if(nums == null || nums.length <= 1)
            return;

        int pl = 0;
        int pr = nums.length - 1;
        int i = 0;
        while(i <= pr){
            if(nums[i] == 0){
                swap(nums, pl, i);
                pl++;
                i++;
            }else if(nums[i] == 1){
                i++;
            }else{
                swap(nums, pr, i);
                pr--;
            }
        }
    }

    private void swap(int[] a, int i, int j){
        int tmp = a[i];
        a[i] = a[j];
        a[j] = tmp;
    }
}

```

---

## @@ 排颜色 II

给定一个有n个对象（包括k种不同的颜色，并按照1到k进行编号）的数组，将对象进行分类使相同颜色的对象相邻，并按照1,2，...k的顺序进行排序。

样例

给出colors=[3, 2, 2, 1, 4]，k=4, 你的代码应该在原地操作使得数组变成[1, 2, 2, 3, 4]

注意

不能使用代码库中的排序函数来解决这个问题

挑战

一个相当直接的解决方案是使用计数排序扫描2遍的算法。这样你会花费O(k)的额外空间。你否能在不使用额外空间的情况下完成？

**题解**

inplace，并且O(N)时间复杂度的算法。

我们可以使用类似桶排序的思想，对所有的数进行计数。

1. 从左扫描到右边，遇到一个数字，先找到对应的bucket.比如 3 2 2 1 4 第一个3对应的bucket是index = 2 (bucket从0开始计算）
2. Bucket 如果有数字，则把这个数字移动到i的position(就是存放起来），然后把bucket记为-1(表示该位置是一个计数器，计1）。
3. Bucket 存的是负数，表示这个bucket已经是计数器，直接减1. 并把color[i] 设置为0 （表示此处已经计算过）
4. Bucket 存的是0，与3一样处理，将bucket设置为-1， 并把color[i] 设置为0 （表示此处已经计算过）
5. 回到position i，再判断此处是否为0（只要不是为0，就一直重复2-4的步骤）。
6.完成1-5的步骤后，从尾部到头部将数组置结果。（从尾至头是为了避免开头的计数器被覆盖）

例子(按以上步骤运算)：

    3 2 2 1 4
    2 2 -1 1 4
    2 -1 -1 1 4
    0 -2 -1 1 4
    -1 -2 -1 0 4
    -1 -2 -1 -1 0

```java
class Solution {
    /**
     * @param colors: A list of integer
     * @param k: An integer
     * @return: nothing
     */
    public void sortColors2(int[] colors, int k) {
        if (colors == null) {
            return;
        }

        int len = colors.length;
        for (int i = 0; i < len; i++) {
            // Means need to deal with A[i]
            while (colors[i] > 0) {
                int num = colors[i];
                if (colors[num - 1] > 0) {
                    // 1. There is a number in the bucket,
                    // Store the number in the bucket in position i;
                    colors[i] = colors[num - 1];
                    colors[num - 1] = -1;
                } else if (colors[num - 1] <= 0) {
                    // 2. Bucket is using or the bucket is empty.
                    colors[num - 1]--;
                    // delete the A[i];
                    colors[i] = 0;
                }
            }
        }

        int index = len - 1;
        for (int i = k - 1; i >= 0; i--) {
            int cnt = -colors[i];

            // Empty number.
            if (cnt == 0) {
                continue;
            }

            while (cnt > 0) {
                colors[index--] = i + 1;
                cnt--;
            }
        }
    }
}

```

---

## @@ 买卖股票的最佳时机

假设有一个数组，它的第i个元素是一支给定的股票在第i天的价格。如果你最多只允许完成一次交易(例如,一次买卖股票),设计一个算法来找出最大利润。

样例

给出一个数组样例 [3,2,3,1,2], 返回 1


**题解**

keep updating the smallest value and the max difference.

```java
public class Solution {
    /**
     * @param prices: Given an integer array
     * @return: Maximum profit
     */
    public int maxProfit(int[] prices) {
        if (prices.length == 0) return 0;
        int min = prices[0];
        int res = 0;
        for (int i=1; i<prices.length; i++){
            if (prices[i] < min) min = prices[i];
            else if ((prices[i]-min) > res){
                res = (prices[i]-min);
            }
        }
        return res;
    }
}

```

---

## @@ 买卖股票的最佳时机 II

假设有一个数组，它的第i个元素是一个给定的股票在第i天的价格。设计一个算法来找到最大的利润。你可以完成尽可能多的交易(多次买卖股票)。然而,你不能同时参与多个交易(你必须在再次购买前出售股票)。

样例

给出一个数组样例[2,1,2,0,1], 返回 2

**题解**

Add all the positive change into the result.

```java
class Solution {
    /**
     * @param prices: Given an integer array
     * @return: Maximum profit
     */
    public int maxProfit(int[] prices) {
        if(prices == null || prices.length==0)
            return 0;
        int res = 0;
        for(int i=0;i<prices.length-1;i++)
        {
            int diff = prices[i+1]-prices[i];
            if(diff>0)
                res += diff;
        }
        return res;
    }
};

```

---

## @@ 买卖股票的最佳时机 III

假设你有一个数组，它的第i个元素是一支给定的股票在第i天的价格。设计一个算法来找到最大的利润。你最多可以完成两笔交易。

样例

给出一个样例数组 [4,4,6,1,1,4,2,5], 返回 6

注意

你不可以同时参与多笔交易(你必须在再次购买前出售掉之前的股票)

**题解**

这道题是Best Time to Buy and Sell Stock的扩展，现在我们最多可以进行两次交易。我们仍然使用动态规划来完成，事实上可以解决非常通用的情况，也就是最多进行k次交易的情况。
这里我们先解释最多可以进行k次交易的算法，然后最多进行两次我们只需要把k取成2即可。我们还是使用“局部最优和全局最优解法”。我们维护两种量，一个是当前到达第i天可以最多进行j次交易，最好的利润是多少（global[i][j]），另一个是当前到达第i天，最多可进行j次交易，并且最后一次交易在当天卖出的最好的利润是多少（local[i][j]）。

下面我们来看递推式，全局的比较简单，

global[i][j]=max(local[i][j],global[i-1][j])
全局（到达第i天进行j次交易的最大收益） = max{局部（在第i天交易后，恰好满足j次交易），全局（到达第i-1天时已经满足j次交易）}
对于局部变量的维护，递推式是

local[i][j]=max(global[i-1][j-1]+max(diff,0),local[i-1][j]+diff)，
局部（在第i天交易后，总共交易了j次） =  max{情况2，情况1}

情况1：在第i-1天时，恰好已经交易了j次（local[i-1][j]），那么如果i-1天到i天再交易一次：即在第i-1天买入，第i天卖出（diff），则这不并不会增加交易次数！【例如我在第一天买入，第二天卖出；然后第二天又买入，第三天再卖出的行为  和   第一天买入，第三天卖出  的效果是一样的，其实只进行了一次交易！因为有连续性】

情况2：第i-1天后，共交易了j-1次（global[i-1][j-1]），因此为了满足“第i天过后共进行了j次交易，且第i天必须进行交易”的条件：我们可以选择在第i-1天买入，然后再第i天卖出（diff），或者选择在第i天买入，然后同样在第i天卖出（收益为0）。
上面的算法中对于天数需要一次扫描，而每次要对交易次数进行递推式求解，所以时间复杂度是O(n*k)，如果是最多进行两次交易，那么复杂度还是O(n)。空间上只需要维护当天数据皆可以，所以是O(k)，当k=2，则是O(1)。

```java
class Solution {
    /**
     * @param prices: Given an integer array
     * @return: Maximum profit
     */
    public int maxProfit(int[] prices) {
        if(prices == null || prices.length == 0)
        return 0;
        int[] local = new int[3];
        int[] global = new int[3];
        for(int i = 0; i < prices.length - 1; i++)
        {
            int diff = prices[i + 1] - prices[i];
            for(int j = 2; j >= 1; j--) //go backwards to use old data, and then override it.
            {
                local[j] = Math.max(global[j - 1] + (diff > 0 ? diff : 0), local[j] + diff);
                global[j] = Math.max(local[j],global[j]);
            }
        }
        return global[2];
    }
};

```

---

## @@ 链表排序

在O(nlogn)时间复杂度和常数级的空间复杂度下给链表排序。

样例

给出1-3->2->null，给它排序变成1->2->3->null

**题解**

merge sort

```java
/**
 * Definition for ListNode.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int val) {
 *         this.val = val;
 *         this.next = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param head: The head of linked list.
     * @return: You should return the head of the sorted linked list,
                    using constant space complexity.
     */
    private ListNode findMiddle(ListNode head) {
        ListNode slow = head, fast = head.next;
        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        return slow;
    }

    private ListNode merge(ListNode head1, ListNode head2) {
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        while (head1 != null && head2 != null) {
            if (head1.val < head2.val) {
                tail.next = head1;
                head1 = head1.next;
            } else {
                tail.next = head2;
                head2 = head2.next;
            }
            tail = tail.next;
        }
        if (head1 != null) {
            tail.next = head1;
        } else {
            tail.next = head2;
        }

        return dummy.next;
    }

    public ListNode sortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        ListNode mid = findMiddle(head);

        ListNode right = sortList(mid.next);
        mid.next = null;
        ListNode left = sortList(head);

        return merge(left, right);
    }
}


```

---

## @@ 重排链表

给定一个单链表L： L0→L1→…→Ln-1→Ln,

重新排列后为：L0→Ln→L1→Ln-1→L2→Ln-2→…

必须在不改变节点值的情况下进行原地操作

样例

给出链表1->2->3->4->null，重新排列后为1->4->2->3->null。

**题解**

```java
/**
 * Definition for ListNode.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int val) {
 *         this.val = val;
 *         this.next = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param head: The head of linked list.
     * @return: void
     */
    public void reorderList(ListNode head) {
        if(head == null || head.next == null || head.next.next == null) return;
        ListNode slow = head, fast = head;

        while(fast.next != null && fast.next.next != null){
            fast = fast.next.next;
            slow = slow.next;
        }
        fast = slow.next;
        slow.next = null;
        // reverse
        ListNode pre = null;
        while(fast != null){
            ListNode temp = fast.next;
            fast.next = pre;
            pre = fast;
            fast = temp;
        }

        while(head != null && pre != null){
            ListNode temp = head.next;
            head.next = pre;
            pre = pre.next;
            head.next.next = temp;
            head = temp;
        }
    }
}


```

---

## @@ 带环链表

给定一个链表，判断它是否有环。

样例

给出 -21->10->4->5, tail connects to node index 1，返回 true

挑战

不要使用额外的空间

**题解**

快慢指针

```java
/**
 * Definition for ListNode.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int val) {
 *         this.val = val;
 *         this.next = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param head: The first node of linked list.
     * @return: True if it has a cycle, or false
     */
    public boolean hasCycle(ListNode head) {
        if(head == null)
            return false;
        ListNode fast = head;
        ListNode slow = head;
        while(fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if(slow == fast)
                return true;
        }
        return false;
    }
}


```

---

## @@ 合并k个排序链表

合并k个排序链表，并且返回合并后的排序链表。尝试分析和描述其复杂度。

样例

给出3个排序链表[2->4->null,null,-1->null]，返回 -1->2->4->null

**题解**

merge two by two

```java
/**
 * Definition for ListNode.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int val) {
 *         this.val = val;
 *         this.next = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param lists: a list of ListNode
     * @return: The head of one sorted list.
     */
    public ListNode mergeKLists(List<ListNode> lists) {
        if (lists == null || lists.size() == 0) {
            return null;
        }

        while (lists.size() > 1) {
            List<ListNode> new_lists = new ArrayList<ListNode>();
            for (int i = 0; i + 1 < lists.size(); i += 2) {
                ListNode merged_list = merge(lists.get(i), lists.get(i+1));
                new_lists.add(merged_list);
            }
            if (lists.size() % 2 == 1) {
                new_lists.add(lists.get(lists.size() - 1));
            }
            lists = new_lists;
        }

        return lists.get(0);
    }

    private ListNode merge(ListNode a, ListNode b) {
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        while (a != null && b != null) {
            if (a.val < b.val) {
                tail.next = a;
                a = a.next;
            } else {
                tail.next = b;
                b = b.next;
            }
            tail = tail.next;
        }

        if (a != null) {
            tail.next = a;
        } else {
            tail.next = b;
        }

        return dummy.next;
    }
}


```

---


## @@ 排序链表转换为二分查找树

给出一个所有元素以升序排序的单链表，将它转换成一棵高度平衡的二分查找树


**题解**

快慢指针找到中间，属于暴力法

```java
/**
 * Definition for ListNode.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int val) {
 *         this.val = val;
 *         this.next = null;
 *     }
 * }
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param head: The first node of linked list.
     * @return: a tree node
     */
    public TreeNode sortedListToBST(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;

        ListNode pre = head;

        if (head == null) {
            return null;
        }

        TreeNode root = null;
        if (head.next == null) {
            root = new TreeNode(head.val);
            root.left = null;
            root.right = null;
            return root;
        }

        // get the middle node.
        while (fast != null && fast.next != null) {
            fast = fast.next.next;

            // record the node before the SLOW.
            pre = slow;
            slow = slow.next;
        }

        // cut the list to two parts.
        pre.next = null;
        TreeNode left = sortedListToBST(head);
        TreeNode right = sortedListToBST(slow.next);

        root = new TreeNode(slow.val);
        root.left = left;
        root.right = right;

        return root;
    }
}


```

---

## @@ 单词切分

给出一个字符串s和一个词典，判断字符串s是否可以被空格切分成一个或多个出现在字典中的单词。

样例

给出

s = "lintcode"

dict = ["lint","code"]

返回 true 因为"lintcode"可以被空格切分成"lint code"

**题解**

It is a DP problem. However, we need to use charAt() instead of substring() to optimize speed. Also, we can first check whether each char in s has appeared in dict, if not, then directly return false. (This is used to pass the last test case in LintCode).

```java
public class Solution {
    /**
     * @param s: A string s
     * @param dict: A dictionary of words dict
     */
    public boolean wordBreak(String s, Set<String> dict) {
        if (s.length()==0) return true;

        char[] chars = new char[256];
        for (String word : dict)
            for (int i=0;i<word.length();i++)
                chars[word.charAt(i)]++;

        for (int i = 0;i<s.length();i++)
            if (chars[s.charAt(i)]==0) return false;

        boolean[] d = new boolean[s.length()+1];
        Arrays.fill(d,false);
        d[0] = true;
        for (int i=1;i<=s.length();i++){
        StringBuilder builder = new StringBuilder();
            for (int j=i-1;j>=0;j--){
                builder.insert(0,s.charAt(j));
                String cur = builder.toString();
                if (d[j] && dict.contains(cur)){
                    d[i]=true;
                    break;
                }
            }
        }

        return d[s.length()];
    }
}

```

---

## @@ 二叉树的序列化和反序列化

设计一个算法，并编写代码来序列化和反序列化二叉树。将树写入一个文件被称为“序列化”，读取文件后重建同样的二叉树被称为“反序列化”。

如何反序列化或序列化二叉树是没有限制的，你只需要确保可以将二叉树序列化为一个字符串，并且可以将字符串反序列化为原来的树结构。

样例

给出一个测试数据样例， 二叉树{3,9,20,#,#,15,7}，表示如下的树结构：

      3
     / \
    9  20
      /  \
     15   7

我们的数据是进行BFS遍历得到的。当你测试结果wrong answer时，你可以作为输入调试你的代码。

你可以采用其他的方法进行序列化和反序列化。

**题解**

Serialize

+ 注意这个是Lintcode的Serialize, 和Leetcode的区别在于他使用的是BFS. 而后者则是使用的pre-order DFS.
+null object 和 null的区别.
+ flag的设计: 要有初始值, 在进入循环的时候update, 对于每一个节点再次update. 那么当这一层结束后就是有效的flag.

De-serialize

+ 还是使用BFS解决. 和Pre-order的de-serialize一样, 和各自的Serialize有一个一一对应的关系.
+ 第一次写的时候出现idx超出array size的问题. 这是为什么呢? 因为我在判断token[idx]的时候居然判断了4次. 因为每一次判断都要idx++. 然后我把4个if并成2个if…else就OK了.
+ 注意这个时候的while loop判断不是parents queue是否为空, 而是判断token[] array走完没有. 我一开始这里搞错了, 居然去判断string走完没有. 注意string就是char Array. 例如{3, 9, 20, #, #, 15, 7}, 这个string的length是21. 而token[]则是7.
+ 还有注意这里update parents queue的时候要注意. 这里的做法是对于”#”, 则不加入null到queue. 不然queue的size()就不对了. 因为这里不用traverse null node.

```java
/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */
class Solution {
    /**
     * This method will be invoked first, you should design your own algorithm
     * to serialize a binary tree which denote by a root node to a string which
     * can be easily deserialized by your own "deserialize" method later.
     */
    public String serialize(TreeNode root) {
        StringBuffer buffer = new StringBuffer();
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        if(root != null){
             queue.offer(root);
             buffer.append(root.val);
        }

        while(!queue.isEmpty()){
            int size = queue.size();

            for(int i = 0; i < size; i++){
                TreeNode node = queue.poll();

                if(node.left == null){
                    buffer.append(",#");
                } else {
                    buffer.append(","+node.left.val);
                    queue.offer(node.left);
                }

                if(node.right == null){
                    buffer.append(",#");
                } else {
                    buffer.append(","+node.right.val);
                    queue.offer(node.right);
                }
            }
        }
        return buffer.toString();
    }

    /**
     * This method will be invoked second, the argument data is what exactly
     * you serialized at method "serialize", that means the data is not given by
     * system, it's given by your own serialize method. So the format of data is
     * designed by yourself, and deserialize it here as you serialize it in
     * "serialize" method.
     */
    public TreeNode deserialize(String data) {
        if(data == null || data.length() == 0) return null;
        Queue<TreeNode> queue = new LinkedList<TreeNode>();

        String[] arr = data.split(",");
        TreeNode root = new TreeNode(Integer.parseInt(arr[0]));
        queue.offer(root);
        for(int i = 1; i < arr.length; i++){
            TreeNode left = null, right = null;
            if(!arr[i].equals("#")){
                left = new TreeNode(Integer.parseInt(arr[i]));
            }
            if(++i < data.length() && !arr[i].equals("#")){
                right = new TreeNode(Integer.parseInt(arr[i]));
            }
            TreeNode parent = queue.poll();
            parent.left = left;
            parent.right = right;
            if(left != null)
                queue.offer(left);
            if(right != null)
                queue.offer(right);
        }
        return root;
    }
}


```

---

## @@ 第k大元素

在数组中找到第k大的元素

样例

给出数组[9,3,2,4,8]，第三大的元素是4

给出数组 [1,2,3,4,5]，第一大的元素是5，第二大的元素是4，第三大的元素是3，以此类推

注意

你可以交换数组中的元素的位置

挑战

要求时间复杂度为O(n），空间复杂度为O(1）

**题解**

Quickselect uses the same overall approach as quicksort, choosing one element as a pivot and partitioning the data in two based on the pivot, accordingly as less than or greater than the pivot. However, instead of recursing into both sides, as in quicksort, quickselect only recurses into one side – the side with the element it is searching for. This reduces the average complexity from O(n log n) (in quicksort) to O(n) (in quickselect).

下面这个code几个注意的地方：

1. 第8行Kth largest element = len-K+1 th smallest element

2. 第24行，l、r在相遇之后，l 所处的位置就是第一个大于等于pivot元素所在位置，把它跟pivot交换，pivot就放在了它应该在的位置

```java
class Solution {
    //param k : description of k
    //param numbers : array of numbers
    //return: description of return
    public int kthLargestElement(int k, ArrayList<Integer> numbers) {
        if (k > numbers.size())
            return 0;
        return helper(numbers.size()-k+1, numbers, 0, numbers.size()-1);
    }

    public int helper(int k, ArrayList<Integer> numbers, int start, int end) {
        int l=start, r=end;
        int pivot = end;
        while (true) {
            while (numbers.get(l)<numbers.get(pivot) && l<r) {
                l++;
            }
            while (numbers.get(r)>=numbers.get(pivot) && l<r) {
                r--;
            }
            if (l == r) break;
            swap(numbers, l, r);
        }
        swap(numbers, l, end);  // l here is the first one which is bigger than pivot, swap it with the pivot
        if (l+1 == k) return numbers.get(l);
        else if (l+1 < k) return helper(k, numbers, l+1, end);
        else return helper(k, numbers, start, l-1);
    }

    public void swap(ArrayList<Integer> numbers, int l, int r) {
        int temp = numbers.get(l);
        numbers.set(l, numbers.get(r).intValue());
        numbers.set(r, temp);
    }
};

```

---

## @@ 丑数

设计一个算法，找出只含素因子3，5，7 的第 k 大的数。

符合条件的数如：3，5，7，9，15......

样例

如果k=4， 返回 9

挑战

要求时间复杂度为O(nlogn)或者O(n)

**题解**

DP method O(k)

For 3, 5 and 7, multiply each one by 1 (default ugly number) at first, then find which prime number yields the smallest product and update its multiplier to the next ugly number. In this manner, accumulatively multiply each one with the next smallest ugly number.

We cannot use if else for checking which prime number (3, 5, or 7) yields the smallest product as there may be duplicates. (for e.g., 3 x 5 == 5 x 3)

```java
class Solution {
    /**
     * @param k: The number k.
     * @return: The kth prime number as description.
     */
    public long kthPrimeNumber(int k) {
        long[] uglyNumbers = new long[k + 1];
        int indexFor3 = 0, indexFor5 = 0, indexFor7 = 0; //multiplier index
        uglyNumbers[0] = 1;
        for (int i = 1; i <= k; i++) {
            uglyNumbers[i] = Math.min(Math.min(3 * uglyNumbers[indexFor3], 5 * uglyNumbers[indexFor5]), 7 * uglyNumbers[indexFor7]);
            if (uglyNumbers[i] == 3 * uglyNumbers[indexFor3]) {
                indexFor3++;
            }
            if (uglyNumbers[i] == 5 * uglyNumbers[indexFor5]) {
                indexFor5++;
            }
            if (uglyNumbers[i] == 7 * uglyNumbers[indexFor7]) {
                indexFor7++;
            }
        }
        return uglyNumbers[k];
    }
};


```

---

## @@ 统计数字

计算数字k在0到n中的出现的次数，k可能是0~9的一个值

样例

例如n=12，k=1，在 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]，我们发现1出现了5次 (1, 10, 11, 12)

**题解**

当某一位的数字小于i时，那么该位出现i的次数为：更高位数字x当前位数
当某一位的数字等于i时，那么该位出现i的次数为：更高位数字x当前位数+低位数字+1
当某一位的数字大于i时，那么该位出现i的次数为：(更高位数字+1)x当前位数

假设一个5位数N=abcde，我们现在来考虑百位上出现2的次数，即，从0到abcde的数中， 有多少个数的百位上是2。分析完它，就可以用同样的方法去计算个位，十位，千位， 万位等各个位上出现2的次数。

当百位c为0时，比如说12013，0到12013中哪些数的百位会出现2？我们从小的数起， 200~299, 1200~1299, 2200~2299, … , 11200~11299, 也就是固定低3位为200~299，然后高位依次从0到11，共12个。再往下12200~12299 已经大于12013，因此不再往下。所以，当百位为0时，百位出现2的次数只由更高位决定， 等于更高位数字(12)x当前位数(100)=1200个。

当百位c为1时，比如说12113。分析同上，并且和上面的情况一模一样。 最大也只能到11200~11299，所以百位出现2的次数也是1200个。

上面两步综合起来，可以得到以下结论：

当某一位的数字小于2时，那么该位出现2的次数为：更高位数字x当前位数
当百位c为2时，比如说12213。那么，我们还是有200~299, 1200~1299, 2200~2299, … , 11200~11299这1200个数，他们的百位为2。但同时，还有一部分12200~12213， 共14个(低位数字+1)。所以，当百位数字为2时， 百位出现2的次数既受高位影响也受低位影响，结论如下：

当某一位的数字等于2时，那么该位出现2的次数为：更高位数字x当前位数+低位数字+1
当百位c大于2时，比如说12313，那么固定低3位为200~299，高位依次可以从0到12， 这一次就把12200~12299也包含了，同时也没低位什么事情。因此出现2的次数是： (更高位数字+1)x当前位数。结论如下：

当某一位的数字大于2时，那么该位出现2的次数为：(更高位数字+1)x当前位数

```java
class Solution {
    /*
     * param k : As description.
     * param n : As description.
     * return: An integer denote the count of digit k in 1..n
     */
    public int digitCounts(int k, int n) {
        int count = 0;
        int base = 1;
        while (n / base >= 1) {
            int curBit = n % (base*10) / base;
            int higher = n / (base*10);
            int lower = n % base;
            if (curBit < k) {
                count += higher * base;
            }
            else if (curBit == k) {
                count += higher * base + lower + 1;
            }
            else {
                count += (higher + 1) * base;
            }
            base *= 10;
        }
        return count;
    }
};


```

---


## @@ A + B 问题

给出两个整数a和b, 求他们的和, 但不能使用 + 等数学运算符

样例

如果 a=1 并且 b=2，返回3

注意

你不需要从输入流读入数据，只需要根据aplusb的两个参数a和b，计算他们的和并返回就行。

挑战

显然你可以直接 return a + b，但是你是否可以挑战一下不这样做？

说明

a和b都是 32位 整数么？是的

我可以使用位运算符么？当然可以

**题解**

位运算实现整数加法本质就是用二进制进行运算。
其主要用了两个基本表达式：

+ x^y //执行加法，不考虑进位。
+ (x&y)<<1 //进位操作

令x=x^y ；y=(x&y)<<1 进行迭代，每迭代一次进位操作右面就多一位0，最多需要“加数二进制位长度”次迭代就没有进位了，此时x^y的值就是结果。

我们来做个3位数的加法：

101+011=1000 //正常加法

位运算加法：

    （1） 101 ^ 011 = 110
    (101 & 011)<<1 = 010
    （2） 110 ^ 010 = 100
    (110 & 010)<<1 = 100
    （3） 100 ^ 100 = 000
    (100 & 100)<<1 = 1000

此时进行相加操作就没有进位了，即000 ^ 1000=1000即是最后结果。

```java
class Solution {
    /*
     * param a: The first integer
     * param b: The second integer
     * return: The sum of a and b
     */
    public int aplusb(int a, int b) {
        // write your code here, try to do it without arithmetic operators.
        while(b != 0){
            int carry = a & b;
            a = a ^ b;
            b = carry << 1;
        }
        return a;
    }
};

```

---

## @@ 最小子串覆盖

给定一个字符串source和一个目标字符串target，在字符串source中找到包括所有目标字符串字母的子串。

样例

给出source = "ADOBECODEBANC"，target = "ABC" 满足要求的解  "BANC"

注意

如果在source中没有这样的子串，返回""，如果有多个这样的子串，返回起始位置最小的子串。

挑战

要求时间复杂度为O(n)

说明

在答案的子串中的字母在目标字符串中是否需要具有相同的顺序？

——不需要。

**题解**

he idea is from here. I try to rephrase it a little bit here. The general idea is that we find a window first, not necessarily the minimum, but it’s the first one we could find, traveling from the beginning of S. We could easily do this by keeping a count of the target characters we have found. After finding an candidate solution, we try to optimize it. We do this by going forward in S and trying to see if we could replace the first character of our candidate. If we find one, we then find a new candidate and we update our knowledge about the minimum. We keep doing this until we reach the end of S. For the giving example:

1. We start with our very first window: “ADOBEC”, windowSize = 6. We now have “A”:1, “B”:1, “C”:1 （保存在needToFind数组里）
2. We skip the following character “ODE” since none of them is in our target T. We then see another “B” so we update “B”:2. Our candidate solution starts with an “A” so getting another “B” cannot make us a “trade”. （体现在代码就是只有满足hasFound[S.charAt(start)] > needToFind[S.charAt(start)]) 才能移动左指针start）
3. We then see another “A” so we update “A”:2. Now we have two “A”s and we know we only need 1. If we keep the new position of this “A” and disregard the old one, we could move forward of our starting position of window. We move from A->D->O->B. Can we keep moving? Yes, since we know we have 2 “B”s so we can also disregard this one. So keep moving until we hit “C”: we only have 1 “C” so we have to stop. Therefore, we have a new candidate solution, “CODEBA”. Our new map is updated to “A”:1, “B”:1, “C”:1.
4. We skip the next “N” （这里忽略所有不在T的字符：用needToFind[S.charAt(start)] == 0来判断） and we arrive at “C”. Now we have two “C”s so we can move forward the starting position of last candidate: we move along this path C->O->D->E until we hit “B”. We only have one “B” so we have to stop. We have yet another new candidate, “BANC”.
5. We have hit the end of S so we just output our best candidate, which is “BANC”.

底下这个做法看似简单，其实里面各种精巧的设计啊：先找到满足条件的一个window(不一定是最优)，每次移动右窗口，吸纳一个新元素进去，如果不是目标元素就跳过continue，如果是的话，hasFound数组对应位置值+1，然后看能不能优化窗口大小 by 看能不能移动左窗口，移动条件就是：始终保证窗口里面含有一个T的所有必要元素（个数要保证），直到移不动为止（再移就无法保证一个完整T的各元素个数了），这时就找到一个新的window，看是否最优。

```java
public class Solution {
    /**
     * @param source: A string
     * @param target: A string
     * @return: A string denote the minimum window
     *          Return "" if there is no such a string
     */
    public String minWindow(String source, String target) {
        int[] hasFound = new int[256];
        int[] needtoFind = new int[256];
        for (int i=0; i<target.length(); i++) {
            needtoFind[(int)(target.charAt(i)-'\0')]++;
        }
        int count = 0;
        int start = 0;
        int end = 0;
        String minWindow = "";
        int minWinSize = Integer.MAX_VALUE;
        for (; end<source.length(); end++) {
            if (needtoFind[(int)(source.charAt(end)-'\0')] == 0) continue;
            char c = source.charAt(end);
            hasFound[(int)(c-'\0')]++;
            if (hasFound[(int)(c-'\0')] <= needtoFind[(int)(c-'\0')]) {
                count++;
            }
            if (count == target.length()) { //the current window contains at least T, optimize the window now
                while (needtoFind[source.charAt(start)]==0 || hasFound[source.charAt(start)]>needtoFind[source.charAt(start)]) {
                    if (hasFound[source.charAt(start)] > needtoFind[source.charAt(start)]) {
                        hasFound[source.charAt(start)]--;
                    }
                    start++;
                }
                if (end-start+1 < minWinSize) {
                    minWinSize = end - start + 1;
                    minWindow = source.substring(start, end+1);
                }
            }
        }
        return minWindow;
    }
}

```

---

## @@ 数组划分

给出一个整数数组nums和一个整数k。划分数组（即移动数组nums中的元素），使得：

+ 所有小于k的元素移到左边
+ 所有大于等于k的元素移到右边

返回数组划分的位置，即数组中第一个位置i，满足nums[i]大于等于k。

样例

给出数组nums=[3,2,2,1]和 k=2，返回 1

注意

你应该真正的划分数组nums，而不仅仅只是计算比k小的整数数，如果数组nums中的所有元素都比k小，则返回nums.length。

挑战

要求在原地使用O(n)的时间复杂度来划分数组

**题解**

Quick Sort 一样的做法，只是有两种情况特殊处理：我第一次做的时候没有考虑到

1. all elements in nums are greater than or equal to k, l pointer never shift， should return r

2. all elements in nums are smaller than k, r pointer never shift, shoud return r+1

```java
public class Solution {
    /**
     *@param nums: The integer array you should partition
     *@param k: As description
     *return: The index after partition
     */
     public int partitionArray(int[] nums, int k) {
        if (nums==null || nums.length==0) return 0;
        int l=0, r=nums.length-1;
        while (true) {
            while (l < r && nums[r] >= k) {
                r--;
            }
            while (l < r && nums[l] < k) {
                l++;
            }
            if (l == r) break;
            swap(l, r, nums);
        }
        if (l==0 && nums[l]>=k) return r;
        if (r==nums.length-1 && nums[l] < k) return r+1;
        return r+1;
    }

    public void swap(int l, int r, int[] nums) {
        int temp = nums[l];
        nums[l] = nums[r];
        nums[r] = temp;
    }
}
```

---

## @@ 交叉字符串

给出三个字符串:s1、s2、s3，判断s3是否由s1和s2交叉构成。

样例

比如 s1 = "aabcc" s2 = "dbbca"

+ 当 s3 = "aadbbcbcac"，返回  true.
+ 当 s3 = "aadbbbaccc"， 返回 false.

挑战

要求时间复杂度为O(n^2)或者更好

**题解**

这是一道关于字符串操作的题目，要求是判断一个字符串能不能由两个字符串按照他们自己的顺序，每次挑取两个串中的一个字符来构造出来。
像这种判断能否按照某种规则来完成求是否或者某个量的题目，很容易会想到用动态规划来实现。

动态规划重点在于找到：维护量，递推式。维护量通过递推式递推，最后往往能得到想要的结果

先说说维护量，res[i][j]表示用s1的前i个字符和s2的前j个字符能不能按照规则表示出s3的前i+j个字符，如此最后结果就是res[s1.length()][s2.length()]，判断是否为真即可。接下来就是递推式了，假设知道res[i][j]之前的所有历史信息，我们怎么得到res[i][j]。可以看出，其实只有两种方式来递推，一种是选取s1的字符作为s3新加进来的字符，另一种是选s2的字符作为新进字符。而要看看能不能选取，就是判断s1(s2)的第i(j)个字符是否与s3的i+j个字符相等。如果可以选取并且对应的res[i-1][j](res[i][j-1])也为真，就说明s3的i+j个字符可以被表示。这两种情况只要有一种成立，就说明res[i][j]为真，是一个或的关系。所以递推式可以表示成

res[i][j] = res[i-1][j]&&s1.charAt(i-1)==s3.charAt(i+j-1) || res[i][j-1]&&s2.charAt(j-1)==s3.charAt(i+j-1)

```java
public class Solution {
    /**
     * Determine whether s3 is formed by interleaving of s1 and s2.
     * @param s1, s2, s3: As description.
     * @return: true or false.
     */
    public boolean isInterleave(String s1, String s2, String s3) {
        if (s3.length() != s1.length() + s2.length()) return false;
        if (s1=="" && s2=="" && s3=="") return true;
        boolean[][] res = new boolean[s1.length()+1][s2.length()+1];
        for (int i=0; i<=s1.length(); i++) {
            for (int j=0; j<=s2.length(); j++) {
                if (i==0 && j==0) res[i][j] = true;
                else if (i>0 && j==0) res[i][j] = res[i-1][j] && s1.charAt(i-1)==s3.charAt(i+j-1);
                else if (i==0 && j>0) res[i][j] = res[i][j-1] && s2.charAt(j-1)==s3.charAt(i+j-1);
                else {
                    res[i][j] = res[i-1][j] && s1.charAt(i-1)==s3.charAt(i+j-1) || res[i][j-1] && s2.charAt(j-1)==s3.charAt(i+j-1);
                }
            }
        }
        return res[s1.length()][s2.length()];
    }
}

```

---

## @@ 子集

给定一个含不同整数的集合，返回其所有的子集

样例

如果 S = [1,2,3]，有如下的解：

    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]

注意

子集中的元素排列必须是非降序的，解集必须不包含重复的子集

**题解**

```java
class Solution {
    /**
     * @param S: A set of numbers.
     * @return: A list of lists. All valid subsets.
     */
    public ArrayList<ArrayList<Integer>> subsets(ArrayList<Integer> S) {
        ArrayList<ArrayList<Integer>> pre = new ArrayList<ArrayList<Integer>>();
        pre.add(new ArrayList<Integer>());
        Collections.sort(S);
        for(Integer num : S){
            ArrayList<ArrayList<Integer>> next = new ArrayList<ArrayList<Integer>>();
            next.addAll(pre);
            for(ArrayList<Integer> subList : pre){
                ArrayList<Integer> cur = new ArrayList<Integer>(subList);
                cur.add(num);
                next.add(cur);
            }
            pre = next;
        }
        return pre;
    }
}

```

---


## @@ 带重复元素的子集

给定一个可能具有重复数字的列表，返回其所有可能的子集

样例

如果S = [1,2,2]，一个可能的答案为：

    [
      [2],
      [1],
      [1,2,2],
      [2,2],
      [1,2],
      []
    ]

注意

子集中的每个元素都是非降序的

两个子集间的顺序是无关紧要的

解集中不能包含重复子集

**题解**

```java
class Solution {
    /**
     * @param S: A set of numbers.
     * @return: A list of lists. All valid subsets.
     */
    public ArrayList<ArrayList<Integer>> subsetsWithDup(ArrayList<Integer> S) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
         res.add(new ArrayList<Integer>());
         int start = 0;
         Collections.sort(S);
         for(int i = 0; i < S.size(); i++){
             int curSize = res.size();
             for(int j = start; j < curSize; j++){
                 ArrayList<Integer> newList = new ArrayList<Integer>(res.get(j));
                 newList.add(S.get(i));
                 res.add(newList);
             }
             if((i+1) < S.size() && S.get(i) == S.get(i+1)){
                 start = curSize;
             } else{
                 start = 0;
             }
         }

         return res;
    }
}


```

---

## @@ 全排列

给定一个数字列表，返回其所有可能的排列。

样例
给出一个列表[1,2,3]，其全排列为：

    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]

挑战

能否不使用递归来实现？

**题解**

```java
class Solution {
    /**
     * @param nums: A list of integers.
     * @return: A list of permutations.
     */
    public ArrayList<ArrayList<Integer>> permute(ArrayList<Integer> nums) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        if (nums == null || nums.size() == 0) {
            return result;
        }

        //start from an empty list
        result.add(new ArrayList<Integer>());

        //add nums[i] to all positions of each list in the current result => new result
        for (int i = 0; i < nums.size(); i++) {
            ArrayList<ArrayList<Integer>> nextResult = new ArrayList<ArrayList<Integer>>();

            //for each list l in the result
            for (ArrayList<Integer> l : result) {
                // insert num[i] from 0 to l.size()
                for (int j = 0; j < l.size() + 1; j++) {
                    l.add(j, nums.get(i));
                    ArrayList<Integer> temp = new ArrayList<Integer>(l);
                    nextResult.add(temp); //add the new list to the next result.
                    l.remove(j);
                }
            }
            result = nextResult;
        }
        return result;
    }
}


```

---

## @@ 带重复元素的排列

给出一个具有重复数字的列表，找出列表所有不同的排列

样例

给出列表[1,2,2]，不同的排列有：

    [
        [1,2,2],
        [2,1,2],
        [2,2,1]
    ]

挑战

能否不使用递归完成？

**题解**

用 hashset 就不用考虑重复的问题

```java
class Solution {
    /**
     * @param nums: A list of integers.
     * @return: A list of unique permutations.
     */
    public ArrayList<ArrayList<Integer>> permuteUnique(ArrayList<Integer> nums) {
        Set<ArrayList<Integer>> result = new HashSet<ArrayList<Integer>>();
        Collections.sort(nums);
        int[] visited = new int[nums.size()];

        result.add(new ArrayList<Integer>());
        for (int i = 0; i < nums.size(); i++) {
            Set<ArrayList<Integer>> nextResult = new HashSet<ArrayList<Integer>>();
            for (ArrayList<Integer> l : result) {
                for (int j = 0; j <= l.size(); j++) {
                    //skip duplicates
                    //while (j < l.size() && nums.get(i) == nums.get(j)) {
                    //    j++;
                    //}
                    l.add(j, nums.get(i));
                    nextResult.add(new ArrayList<Integer>(l));
                    l.remove(j);
                }
            }
            result = nextResult;
        }
        return new ArrayList<ArrayList<Integer>>(result);
    }
}


```

---


## @@ 带最小值操作的栈

实现一个带有取最小值min方法的栈，min方法将返回当前栈中的最小值。

你实现的栈将支持push，pop 和 min 操作，所有操作要求都在O(1)时间内完成。

样例

如下操作：push(1)，pop()，push(2)，push(3)，min()， push(1)，min() 返回 1，2，1

注意

如果堆栈中没有数字则不能进行min方法的调用

**题解**

维护另一个 stack 即可

```java
public class Solution {

    private Stack<Integer> stack;
    private Stack<Integer> minStack;
    public Solution() {
        stack = new Stack<Integer>();
        minStack = new Stack<Integer>();
    }

    public void push(int number) {
        stack.push(number);
        if (minStack.isEmpty()) {
            minStack.push(number);
        } else {
            minStack.push(Math.min(number, minStack.peek()));
        }
    }

    public int pop() {
        minStack.pop();
        return stack.pop();
    }

    public int min() {
        return minStack.peek();
    }
}


```

---

## @@ 二叉查找树中搜索区间

给定两个值 k1 和 k2（k1 < k2）和一个二叉查找树的根节点。找到树中所有值在 k1 到 k2 范围内的节点。即打印所有x (k1 <= x <= k2) 其中 x 是二叉查找树的中的节点值。返回所有升序的节点值。

样例
如果有 k1 = 10 和 k2 = 22, 你的程序应该返回 [12, 20, 22].

        20
       /  \
      8   22
     / \
    4   12

**题解**

正常回溯一波二分即可

```java
/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param root: The root of the binary search tree.
     * @param k1 and k2: range k1 to k2.
     * @return: Return all keys that k1<=key<=k2 in ascending order.
     */
    public ArrayList<Integer> searchRange(TreeNode root, int k1, int k2) {
        ArrayList<Integer> res = searchRangeRecur(root,k1,k2);
        return res;
    }

    public ArrayList<Integer> searchRangeRecur(TreeNode cur, int k1, int k2){
        ArrayList<Integer> res = new ArrayList<Integer>();
        if (cur==null) return res;
        if (k1>k2) return res;

        ArrayList<Integer> left = searchRangeRecur(cur.left,k1,Math.min(cur.val-1,k2));
        ArrayList<Integer> right = searchRangeRecur(cur.right,Math.max(cur.val+1,k1),k2);

        res.addAll(left);
        if (cur.val>=k1 && cur.val<=k2) res.add(cur.val);
        res.addAll(right);

        return res;
    }
}

```

---

## @@ 主元素 II

给定一个整型数组，找到主元素，它在数组中的出现次数严格大于数组元素个数的三分之一。

样例

给出数组[1,2,1,2,1,3,3] 返回 1

注意

数组中只有唯一的主元素

挑战

要求时间复杂度为O(n)，空间复杂度为O(1)。

**题解**

三三抵销法，但是也有需要注意的地方：

1. 我们对cnt1,cnt2减数时，相当于丢弃了3个数字（当前数字，candidate1, candidate2）。也就是说，每一次丢弃数字，我们是丢弃3个不同的数字。

而Majority number超过了1/3所以它最后一定会留下来。

设定总数为N, majority number次数为m。丢弃的次数是x。则majority 被扔的次数是x

而m > N/3, N - 3x > 0.

3m > N,  N > 3x 所以 3m > 3x, m > x 也就是说 m一定没有被扔完

最坏的情况，Majority number每次都被扔掉了，但它一定会在n1,n2中。

2. 为什么最后要再检查2个数字呢(从头开始统计，而不用剩下的count1, count2)？因为数字的编排可以让majority 数被过度消耗，使其计数反而小于n2，或者等于n2.前面举的例子即是。

另一个例子：

1 1 1 1 2 3 2 3 4 4 4 这个 1就会被消耗过多，最后余下的反而比4少。

```java
public class Solution {
    /**
     * @param nums: A list of integers
     * @return: The majority number that occurs more than 1/3
     */
    public int majorityNumber(ArrayList<Integer> nums) {
        int candidate1 = 0;
        int candidate2 = 0;
        int count1 = 0;
        int count2 = 0;
        for (int elem : nums) {
            if (count1 == 0) {
                candidate1 = elem;
            }
            if (count2 == 0 && elem != candidate1) {
                candidate2 = elem;
            }
            if (candidate1 == elem) {
                count1++;
            }
            if (candidate2 == elem) {
                count2++;
            }
            if (candidate1 != elem && candidate2 != elem) {
                count1--;
                count2--;
            }
        }

        count1 = 0;
        count2 = 0;
        for (int elem : nums) {
            if (elem == candidate1) count1++;
            else if (elem == candidate2) count2++;
        }
        return count1>count2? candidate1 : candidate2;
    }
}


```

---


## @@ 主元素 III

给定一个整型数组，找到主元素，它在数组中的出现次数严格大于数组元素个数的1/k。

样例

给出数组 [3,1,2,3,2,3,3,4,4,4] ，和 k = 3，返回 3

注意

数组中只有唯一的主元素

挑战

要求时间复杂度为O(n)，空间复杂度为O(k)

**题解**

```java
public class Solution {
    /**
     * @param nums: A list of integers
     * @param k: As described
     * @return: The majority number
     */
    public int majorityNumber(ArrayList<Integer> nums, int k) {
        int len = nums.size();
        if (len < k) {
            return -1;
        }
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int x : nums) {
            if (map.size() < k && !map.containsKey(x)) {
                map.put(x, 1);
            } else if (map.containsKey(x)) {
                map.put(x, map.get(x) + 1);
            } else {
                Map<Integer, Integer> tmp = new HashMap<Integer, Integer>();
                for (int key : map.keySet()) {
                    if (map.get(key) > 1) {
                        tmp.put(key, map.get(key)-1);
                    }
                }
                map = tmp;
            }
        }
        int result = 0;
        int count = 0;
        for (int key : map.keySet()) {
            if (map.get(key) > count) {
                result = key;
                count = map.get(key);
            }
        }
        return result;
    }
}


```

---

## @@ 用栈实现队列

正如标题所述，你需要使用两个栈来实现队列的一些操作。

队列应支持push(element)，pop() 和 top()，其中pop是弹出队列中的第一个(最前面的)元素。

pop和top方法都应该返回第一个元素的值。

样例

比如push(1), pop(), push(2), push(3), top(), pop()，你应该返回1，2和2

挑战

仅使用两个栈来实现它，不使用任何其他数据结构，push，pop 和 top的复杂度都应该是均摊O(1)的

**题解**

```java
public class Solution {
    private Stack<Integer> stack1;
    private Stack<Integer> stack2;

    public Solution() {
       // do initialization if necessary
       stack1 = new Stack<Integer>();
       stack2 = new Stack<Integer>();
    }

    public void push(int element) {
        stack1.push(element);
    }

    public int pop() {
        if (stack2.isEmpty()) {
            while (!stack1.isEmpty()) {
                stack2.push(stack1.pop());
            }
        }

        return stack2.pop();
    }

    public int top() {
        if (stack2.isEmpty()) {
            while (!stack1.isEmpty()) {
                stack2.push(stack1.pop());
            }
        }

        return stack2.peek();
    }
}


```

---

## @@ 最大子数组差

给定一个整数数组，找出两个不重叠的子数组A和B，使两个子数组和的差的绝对值|SUM(A) - SUM(B)|最大。

返回这个最大的差值。

样例

给出数组[1, 2, -3, 1]，返回 6

注意

子数组最少包含一个数

挑战

时间复杂度为O(n)，空间复杂度为O(n)

**题解**

用到了max subarray的技巧，并且分别从左边和右边扫，对于每一个index， 更新res = Math.max(res, Math.max(maxFromRight[i] – minFromLeft[i-1], maxFromLeft[i] – maxFromRight[i-1]));

```java
public class Solution {
    /**
     * @param nums: A list of integers
     * @return: An integer indicate the value of maximum difference between two
     *          Subarrays
     */
    public int maxDiffSubArrays(ArrayList<Integer> nums) {
        if (nums == null || nums.size() == 0) {
            return 0;
        }
        int[] maxFromLeft = new int[nums.size()];
        int[] minFromLeft = new int[nums.size()];
        int min = nums.get(0);
        int max = min;
        int localmin = min;
        int localmax = max;
        maxFromLeft[0] = minFromLeft[0] = min;
        for (int i = 1; i < nums.size(); i++) {
            localmin = Math.min(nums.get(i), localmin+nums.get(i));
            localmax = Math.max(nums.get(i), localmax+nums.get(i));
            max = Math.max(max, localmax);
            min = Math.min(min, localmin);
            maxFromLeft[i] = max;
            minFromLeft[i] = min;
        }
        min = nums.get(nums.size() - 1);
        max = min;
        localmin = min;
        localmax = max;
        int res = Math.max(max - minFromLeft[nums.size()-2],
                           maxFromLeft[nums.size() - 2] - min);
        for (int i = nums.size() - 2; i > 0; i--) {
            localmin = Math.min(nums.get(i), localmin+nums.get(i));
            localmax = Math.max(nums.get(i), localmax+nums.get(i));
            max = Math.max(max, localmax);
            min = Math.min(min, localmin);
            res = Math.max(res, Math.max(max - minFromLeft[i-1],
                           maxFromLeft[i-1] - min));
        }
        return res;
    }
}
```

---


## @@ 最大子数组 II

给定一个整数数组，找出两个不重叠子数组使得它们的和最大。

每个子数组的数字在数组中的位置应该是连续的。

返回最大的和。

样例

给出数组[1, 3, -1, 2, -1, 2]，这两个子数组分别为[1, 3]和[2, -1, 2]或者[1, 3, -1, 2]和[2]，它们的最大和都是7

注意

子数组最少包含一个数

挑战

要求时间复杂度为O(n)

**题解**

类似max subarray I的解法，区别是我们这里扫两遍，从左边向右边的时候算出globalmax，从右边向左边的时候算出localMax，然后找两边加起来的最大值。首先我们定义两个变量，localMax[i]为以i结尾的subarray中最大的值，globalMax[i]定义为[0, i]范围中最大的subarray(subarray不一定需要以i结尾)。递推表达式是：

+ localMax[i] = max(localMax[i - 1] + A[i], A[i]);
+ globalMax[i] = max(globalMax[i - 1], localMax[i]);

从右边向左边的时候维护localMax[i]，这时的localMax[i]指的是以i开头的最大的subarray

+ localMax[i] = max(localMax[i + 1] + A[i], A[i]);

扫两遍，时间复杂度O(n)，空间复杂度O(n)，从右边向左边扫的时候不需要开辟一个新的数组，并且计算最后最大值可以在第二次循环的时候一起做了

```java
public class Solution {
    /**
     * @param nums: A list of integers
     * @return: An integer denotes the sum of max two non-overlapping subarrays
     */
    public int maxTwoSubArrays(ArrayList<Integer> nums) {
        if (nums == null)
            return 0;
        int len = nums.size(), currSum = 0;
        int[] left = new int[len];
        for (int i = 0; i < len - 1; i++) {
            int sum = currSum + nums.get(i);
            if (i == 0)
                left[i + 1] = sum;
            else
                left[i + 1] = sum > left[i]? sum: left[i];
            currSum = sum <= 0? 0: sum;
        }
        currSum = 0;
        int max = Integer.MIN_VALUE;
        for (int i = len - 1; i > 0; i--) {
            int sum = currSum + nums.get(i);
            if (sum + left[i] > max)
                max = sum + left[i];
            currSum = sum <= 0? 0: sum;
        }
        return max;
    }
}



```

---

## @@ N皇后问题

n皇后问题是将n个皇后放置在n*n的棋盘上，皇后彼此之间不能相互攻击。

给定一个整数n，返回所有不同的n皇后问题的解决方案。

每个解决方案包含一个明确的n皇后放置布局，其中“Q”和“.”分别表示一个女王和一个空位置。

样例

对于4皇后问题存在两种解决的方案：

    [
        [".Q..", // Solution 1
         "...Q",
         "Q...",
         "..Q."],
        ["..Q.", // Solution 2
         "Q...",
         "...Q",
         ".Q.."]
    ]

挑战

你能否不使用递归完成？

**题解**

```java
class Solution {
    /**
     * Get all distinct N-Queen solutions
     * @param n: The number of queens
     * @return: All distinct solutions
     * For example, A string '...Q' shows a queen on forth position
     */
    ArrayList<ArrayList<String>> solveNQueens(int n) {
        ArrayList<ArrayList<String>> res = new ArrayList<ArrayList<String>>();
        dfs(n, 0, new int[n], res);
        return res;
    }


    private void dfs(int n, int start, int[] row, ArrayList<ArrayList<String>> res){
        if(n == start){
            res.add(generating(row, n));
            return;
        }
        for(int i = 0; i < n; i++){
            row[start] = i;
            boolean isValid = true;
            for(int j = 0; j < start; j++){
                if(row[j] == i || Math.abs(row[j] - row[start]) == start - j){
                    isValid = false;
                    break;
                }

            }

            if(isValid == true)
                dfs(n, start+1, row, res);

        }
    }

    private ArrayList<String> generating(int[] row, int n){
        ArrayList<String> res = new ArrayList<String>();
        for(int i = 0; i < n; i++){
            StringBuffer buffer = new StringBuffer();
            for(int j = 0; j < n; j++){

                if(row[i] == j){
                    buffer.append("Q");
                } else {
                    buffer.append(".");
                }

            }
            res.add(buffer.toString());
        }
        return res;
    }
};

```

---

## @@ N皇后问题 II

根据n皇后问题，现在返回n皇后不同的解决方案的数量而不是具体的放置布局。

样例

比如n=4，存在2种解决方案

**题解**

```java
class Solution {
    /**
     * Calculate the total number of distinct N-Queen solutions.
     * @param n: The number of queens.
     * @return: The total number of distinct solutions.
     */
    public int totalNQueens(int n) {
        if (n == 0) {
            return 0;
        }

        // Bug 1: forget to modify the parameters of the function.
        return dfs(n, 0, new ArrayList<Integer>());
    }

    public int dfs(int n, int row, ArrayList<Integer> path) {
        if (row == n) {
            // The base case: 当最后一行，皇后只有1种放法(就是不放)
            return 1;
        }

        int num = 0;

        // The queen can select any of the slot.
        for (int i = 0; i < n; i++) {
            if (!isValid(path, i)) {
                continue;
            }
            path.add(i);

            // All the solutions is all the possiablities are add up.
            num += dfs(n, row + 1, path);
            path.remove(path.size() - 1);
        }

        return num;
    }

    public boolean isValid(ArrayList<Integer> path, int col) {
        int size = path.size();
        for (int i = 0; i < size; i++) {
            // The same column with any of the current queen.
            if (col == path.get(i)) {
                return false;
            }

            // diagonally lines.
            // Bug 2: forget to add a ')'
            if (size - i == Math.abs(col - path.get(i))) {
                return false;
            }
        }

        return true;
    }
};



```

---

## @@ 翻转链表 II

翻转链表中第m个节点到第n个节点的部分

样例

给出链表1->2->3->4->5->null， m = 2 和n = 4，返回1->4->3->2->5->null

注意

m，n满足1 ≤ m ≤ n ≤ 链表长度

挑战

在原地一次翻转完成

**题解**

```java
/**
 * Definition for ListNode
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param ListNode head is the head of the linked list
     * @oaram m and n
     * @return: The head of the reversed ListNode
     */
    public ListNode reverseBetween(ListNode head, int m , int n) {
        if (m >= n || head == null) {
            return head;
        }

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        head = dummy;

        for (int i = 1; i < m; i++) {
            if (head == null) {
                return null;
            }
            head = head.next;
        }

        ListNode premNode = head;
        ListNode mNode = head.next;
        ListNode nNode = mNode, postnNode = mNode.next;
        for (int i = m; i < n; i++) {
            if (postnNode == null) {
                return null;
            }
            ListNode temp = postnNode.next;
            postnNode.next = nNode;
            nNode = postnNode;
            postnNode = temp;
        }
        mNode.next = postnNode;
        premNode.next = nNode;

        return dummy.next;
    }
}

```

---

## @@ 搜索二维矩阵 II

写出一个高效的算法来搜索m×n矩阵中的值，返回这个值出现的次数。

这个矩阵具有以下特性：

+ 每行中的整数从左到右是排序的。
+ 每一列的整数从上到下是排序的。
+ 在每一行或每一列中没有重复的整数。

样例

考虑下列矩阵：

    [
        [1, 3, 5, 7],
        [2, 4, 7, 8],
        [3, 5, 9, 10]
    ]

给出target = 3，返回 2

挑战

要求O(m+n) 时间复杂度和O(1) 额外空间

**题解**

很巧妙的思路，可以从左下或者右上开始找

```java
public class Solution {
    /**
     * @param matrix: A list of lists of integers
     * @param: A number you want to search in the matrix
     * @return: An integer indicate the occurrence of target in the given matrix
     */
    public int searchMatrix(int[][] matrix, int target) {
        if (matrix==null || matrix.length==0 || matrix[0].length==0) return 0;
        int m = matrix.length;
        int n = matrix[0].length;
        int count = 0;
        int row = m-1;
        int col = 0;
        while (row>=0 && row < m && col >= 0 && col < n) {
            int cur = matrix[row][col];
            if (cur == target) {
                count++;
                col++;
                row--;
            }
            else if (cur > target) {
                row--;
            }
            else col++;
        }
        return count;
    }
}


```

---

## @@ 搜索旋转排序数组

假设有一个排序的按未知的旋转轴旋转的数组(比如，0 1 2 4 5 6 7 可能成为4 5 6 7 0 1 2)。给定一个目标值进行搜索，如果在数组中找到目标值返回数组中的索引位置，否则返回-1。

你可以假设数组中不存在重复的元素。

样例

给出[4, 5, 1, 2, 3]和target=1，返回 2

给出[4, 5, 1, 2, 3]和target=0，返回 -1

**题解**

对于有序数组，使用二分搜索比较方便。分析题中的数组特点，旋转后初看是乱序数组，但仔细一看其实里面是存在两段有序数组的。因此该题可转化为如何找出旋转数组中的局部有序数组，并使用二分搜索解之。结合实际数组在纸上分析较为方便。

源码分析

1. 若target == A[mid]，索引找到，直接返回
2. 寻找局部有序数组，分析A[mid]和两段有序的数组特点，由于旋转后前面有序数组最小值都比后面有序数组最大值大。故若A[start] < A[mid]成立，则start与mid间的元素必有序（要么是前一段有序数组，要么是后一段有序数组，还有可能是未旋转数组）。
3. 接着在有序数组A[start]~A[mid]间进行二分搜索，但能在A[start]~A[mid]间搜索的前提是A[start] <= target <= A[mid]。
4. 接着在有序数组A[mid]~A[end]间进行二分搜索，注意前提条件。
5. 搜索完毕时索引若不是mid或者未满足while循环条件，则测试A[start]或者A[end]是否满足条件。
6. 最后若未找到满足条件的索引，则返回-1.

```java
public class Solution {
    /**
     *@param A : an integer rotated sorted array
     *@param target :  an integer to be searched
     *return : an integer
     */
    public int search(int[] A, int target) {
        if (A == null || A.length == 0) {
            return -1;
        }

        int start = 0, end = A.length - 1, mid = 0;
        while (start + 1 < end) {
            mid = start + (end - start)/2;
            if (A[mid] == target) {
                return mid;
            }
            if (A[start] < A[mid]) {//part 1
                if (A[start] <= target && target <= A[mid]) {
                    end = mid;
                } else {
                    start = mid;
                }
            } else { //part 2
                if (A[mid] <= target && target <= A[end]) {
                    start = mid;
                } else {
                    end = mid;
                }
            }
        } // end while

        if (A[start] == target) {
            return start;
        } else if (A[end] == target) {
            return end;
        } else {
            return -1; // not found
        }
    }
}


```

---

## @@ 搜索旋转排序数组 II

跟进“搜索旋转排序数组”，假如有重复元素又将如何？

是否会影响运行时间复杂度？

如何影响？

为何会影响？

写出一个函数判断给定的目标值是否出现在数组中。

样例

给出[3,4,4,5,7,0,1,2]和target=4，返回 true

**题解**

仔细分析此题和之前一题的不同之处，前一题我们利用A[start] < A[mid]这一关键信息，而在此题中由于有重复元素的存在，在A[start] == A[mid]时无法确定有序数组，此时只能依次递增start/递减end以缩小搜索范围，时间复杂度最差变为O(n)。

在A[start] == A[mid]时递增start序号即可。

```java
public class Solution {
    /**
     * param A : an integer ratated sorted array and duplicates are allowed
     * param target :  an integer to be search
     * return : a boolean
     */
    public boolean search(int[] A, int target) {
        if(A==null || A.length==0) {
            return false;
        }
        int l = 0;
        int r = A.length-1;

        while(l <= r) {
            int m = (l + r) / 2;
            if (target == A[m]) {
                return true;
            }
            if (A[l] < A[m]) {
                // situation 1, numbers between start and mid are sorted
                if(target >= A[l] && target < A[m]) {
                    r = m - 1;
                }
                else {
                    l =m + 1;
                }
            }
            else if (A[l] > A[m]) {
                // situation 2, numbers between mid and end are sorted
                if (target > A[m] && target <= A[r]) {
                    l = m + 1;
                }
                else {
                    r = m - 1;
                }
            }
            else {
                l++;
            }
        }
        return false;
    }
}


```

---

## @@ 搜索区间

给定一个包含 n 个整数的排序数组，找出给定目标值 target 的起始和结束位置。

样例

给出[5, 7, 7, 8, 8, 10]和目标值target=8,

返回[3, 4]

挑战

时间复杂度 O(log n)

**题解**

Search for a range 的题目可以拆解为找 first & last position 的题目，即要做两次二分。由上题二分查找可找到满足条件的左边界，因此只需要再将右边界找出即可。注意到在(target == nums[mid]时赋值语句为end = mid，将其改为start = mid即可找到右边界，解毕。

```java
public class Solution {
    /**
     *@param A : an integer sorted array
     *@param target :  an integer to be inserted
     *return : a list of length 2, [index1, index2]
     */
    public ArrayList<Integer> searchRange(ArrayList<Integer> A, int target) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        int start, end, mid;
        result.add(-1);
        result.add(-1);

        if (A == null || A.size() == 0) {
            return result;
        }

        // search for left bound
        start = 0;
        end = A.size() - 1;
        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (A.get(mid) == target) {
                end = mid; // set end = mid to find the minimum mid
            } else if (A.get(mid) > target) {
                end = mid;
            } else {
                start = mid;
            }
        }
        if (A.get(start) == target) {
            result.set(0, start);
        } else if (A.get(end) == target) {
            result.set(0, end);
        } else {
            return result;
        }

        // search for right bound
        start = 0;
        end = A.size() - 1;
        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (A.get(mid) == target) {
                start = mid; // set start = mid to find the maximum mid
            } else if (A.get(mid) > target) {
                end = mid;
            } else {
                start = mid;
            }
        }
        if (A.get(end) == target) {
            result.set(1, end);
        } else if (A.get(start) == target) {
            result.set(1, start);
        } else {
            return result;
        }

        return result;
    }
}


```

源码分析

1. 首先对输入做异常处理，数组为空或者长度为0
2. 初始化 start, end, mid三个变量，注意mid的求值方法，可以防止两个整型值相加时溢出
3. 使用迭代而不是递归进行二分查找
4. while终止条件应为start + 1 < end而不是start <= end，start == end时可能出现死循环
5. 先求左边界，迭代终止时先判断A.get(start) == target，再判断A.get(end) == target，因为迭代终止时target必取start或end中的一个，而end又大于start，取左边界即为start.
6. 再求右边界，迭代终止时先判断A.get(end) == target，再判断A.get(start) == target
7. 两次二分查找除了终止条件不同，中间逻辑也不同，即当A.get(mid) == target如果是左边界（first postion），中间逻辑是end = mid；若是右边界（last position），中间逻辑是start = mid
8. 两次二分查找中间勿忘记重置 start, end 的变量值。

---

## @@ 两数之和

给一个整数数组，找到两个数使得他们的和等于一个给定的数target。

你需要实现的函数twoSum需要返回这两个数的下标, 并且第一个下标小于第二个下标。注意这里下标的范围是1到n，不是以0开头。

样例

numbers=[2, 7, 11, 15],  target=9

return [1, 2]

注意

你可以假设只有一组答案。

**题解**

O(n) Space, O(n) Time solution:

Use a hashmap to store element of array as key, index as value.

Then use a for loop to check whether target - current exist in hashmap.
However, if element in the array is repeated, the hashmap has to hold repetitive keys.

So we keep comparing and storage at the same time and don't need to worry about repetitions.


```java
public class Solution {
    /*
     * @param numbers : An array of Integer
     * @param target : target = numbers[index1] + numbers[index2]
     * @return : [index1 + 1, index2 + 1] (index1 < index2)
     */
    public int[] twoSum(int[] numbers, int target) {
        if(numbers == null || numbers.length < 2) return null;
        int[] res = new int[2];
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(int i = 0; i < numbers.length; i++){
            if(map.containsKey(numbers[i])){
                res[0] = map.get(numbers[i]) + 1;
                res[1] = i+1;
            } else{
                map.put(target-numbers[i], i);
            }
        }
        return res;
    }
}

```

---

## @@ 三数之和

给出一个有n个整数的数组S，在S中找到三个整数a, b, c，找到所有使得a + b + c = 0的三元组。

样例

如S = {-1 0 1 2 -1 -4}, 你需要返回的三元组集合的是：

(-1, 0, 1)

(-1, -1, 2)

注意

在三元组(a, b, c)，要求a <= b <= c。

结果不能包含重复的三元组。

**题解**

brute force时间复杂度为O(n^3), 对每三个数进行比较。这道题和Two Sum有所不同，使用哈希表的解法并不是很方便，因为结果数组中元素可能重复，如果不排序对于重复的处理将会比较麻烦，因此这道题一般使用排序之后夹逼的方法，总的时间复杂度为O(n^2+nlogn)=(n^2),空间复杂度是O(n),Two Sum的时间复杂度是O(n+nlogn)

困难点主要在于去重

排序后每一次假设把nums[i]作为第一个数字，在剩下的数字取两个

```java
public class Solution {
    /**
     * @param numbers : Give an array numbers of n integer
     * @return : Find all unique triplets in the array which gives the sum of zero.
     */
    public ArrayList<ArrayList<Integer>> threeSum(int[] numbers) {
        if(numbers == null || numbers.length <= 2) return null;
        ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
        Arrays.sort(numbers);
        for(int i = 0; i < numbers.length - 2; i++){
            if(i > 0 && numbers[i] == numbers[i-1])
                continue;
            int j = i + 1, k = numbers.length - 1;
            while(j < k){
                if(j > i + 1 && numbers[j] == numbers[j-1]){
                    j++;
                    continue;
                }
                if(numbers[i] + numbers[j] + numbers[k] == 0){
                    ArrayList<Integer> sub = new ArrayList<Integer>();
                    sub.add(numbers[i]);
                    sub.add(numbers[j]);
                    sub.add(numbers[k]);
                    res.add(sub);
                    j++; k--;
                } else if(numbers[i] + numbers[j] + numbers[k] > 0) k--;
                else j++;
            }
        }
        return res;
    }
}

```

---

## @@ 三数之和 II

给一个包含n个整数的数组S, 找到和与给定整数target最接近的三元组，返回这三个数的和。

样例

例如S = [-1, 2, 1, -4] and target = 1.  和最接近1的三元组是 -1 + 2 + 1 = 2.

注意

只需要返回三元组之和，无需返回三元组本身

**题解**

Similar to 3 SUM.

Starting from the left-element, assume it's the solution. Move the 2 pointers in the right-side-array.

Using the two pointers, trying to find ele1 + ele2 + ele3 = closest number to target.

Note: for comparing closet, use initial value Integer.MAX_VALUE. Be aware of the overflow of integer, use long to handle.

```java
public class Solution {
    /**
     * @param numbers: Give an array numbers of n integer
     * @param target : An integer
     * @return : return the sum of the three integers, the sum closest target.
     */
    public int threeSumClosest(int[] num ,int target) {
        if (num == null || num.length < 3) {
            return Integer.MAX_VALUE;
        }
        Arrays.sort(num);
        long closest = (long) Integer.MAX_VALUE;
        for (int i = 0; i < num.length - 2; i++) {
            int left = i + 1;
            int right = num.length - 1;
            while (left < right) {
                int sum = num[i] + num[left] + num[right];
                if (sum == target) {
                    return sum;
                } else if (sum < target) {
                    left++;
                } else {
                    right--;
                }
                closest = Math.abs(sum - target) < Math.abs(closest - target)
                            ? (long) sum : closest;
            }//while
        }//for
        return (int) closest;
    }
}


```

---

## @@ 四数之和

给一个包含n个数的整数数组S，在S中找到所有使得和为给定整数target的四元组(a, b, c, d)。

样例

例如，对于给定的整数数组S=[1, 0, -1, 0, -2, 2] 和 target=0. 满足要求的四元组集合为：

(-1, 0, 0, 1)

(-2, -1, 1, 2)

(-2, 0, 0, 2)

注意

四元组(a, b, c, d)中，需要满足a <= b <= c <= d

答案中不可以包含重复的四元组。

**题解**

```java
public class Solution {
    /**
     * @param numbers : Give an array numbersbers of n integer
     * @param target : you need to find four elements that's sum of target
     * @return : Find all unique quadruplets in the array which gives the sum of
     *           zero.
     */
    public ArrayList<ArrayList<Integer>> fourSum(int[] numbers, int target) {   ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
        if(numbers == null || numbers.length <= 3) return res;
        Arrays.sort(numbers);
        for(int i = 0; i < numbers.length - 3; i++){
            if(i > 0 && numbers[i] == numbers[i-1])
                continue;
            for(int j = i + 1; j < numbers.length - 2; j++){
                if(j > i + 1 && numbers[j] == numbers[j-1])
                    continue;
                int h = j + 1, k = numbers.length - 1;
                while(h < k){
                    if(h > j + 1 && numbers[h] == numbers[h-1]){
                        h++;
                        continue;
                    }
                    int sum = numbers[i] + numbers[j] + + numbers[h] + numbers[k];
                    if(sum == target){
                        ArrayList<Integer> sub = new ArrayList<Integer>();
                        sub.add(numbers[i]);
                        sub.add(numbers[j]);
                        sub.add(numbers[h]);
                        sub.add(numbers[k]);
                        res.add(sub);
                        h++; k--;
                    } else if(sum > target) k--;
                    else h++;
                }
            }
        }
        return res;
    }
}


```

---

## @@ 上一个排列

给定一个整数数组来表示排列，找出其上一个排列。

样例

给出排列[1,3,2,3]，其上一个排列是[1,2,3,3]

给出排列[1,2,3,4]，其上一个排列是[4,3,2,1]

注意

排列中可能包含重复的整数

**题解**

这里找上一个排列，仍然使用字典序算法，大致步骤如下：

1. 从后往前寻找索引满足 a[k] > a[k + 1], 如果此条件不满足，则说明已遍历到最后一个。
2. 从后往前遍历，找到第一个比a[k]小的数a[l], 即a[k] > a[l].
3. 交换a[k]与a[l].
4. 反转k + 1 ~ n之间的元素。

为何不从前往后呢？因为只有从后往前才能保证得到的是相邻的排列，可以举个实际例子自行分析。

```java
public class Solution {
    /**
     * @param nums: A list of integers
     * @return: A list of integers that's previous permuation
     */
    public ArrayList<Integer> previousPermuation(ArrayList<Integer> nums) {
        if (nums == null || nums.size() <= 1) {
            return nums;
        }
        // step1: find nums[i] > nums[i + 1]
        int i = 0;
        for (i = nums.size() - 2; i >= 0; i--) {
            if (nums.get(i) > nums.get(i + 1)) {
                break;
            } else if (i == 0) {
                // reverse nums if reach minimum
                reverse(nums, 0, nums.size() - 1);
                return nums;
            }
        }
        // step2: find nums[i] > nums[j]
        int j = 0;
        for (j = nums.size() - 1; j > i; j--) {
            if (nums.get(i) > nums.get(j)) {
                break;
            }
        }
        // step3: swap betwenn nums[i] and nums[j]
        Collections.swap(nums, i, j);
        // step4: reverse between [i + 1, n - 1]
        reverse(nums, i + 1, nums.size() - 1);

        return nums;
    }

    private void reverse(List<Integer> nums, int start, int end) {
        for (int i = start, j = end; i < j; i++, j--) {
            Collections.swap(nums, i, j);
        }
    }
}


```

---

## @@ 最长公共前缀

给k个字符串，求出他们的最长公共前缀(LCP)

样例

在 "ABCD" "ABEF" 和 "ACEF" 中,  LCP 为 "A"

在 "ABCDEFG", "ABCEFG", "ABCEFA" 中, LCP 为 "ABC"

**题解**

To solve this problem, we need to find the two loop conditions. One is the length of the shortest string. The other is iteration over every element of the string array.

```java
public class Solution {
    /**
     * @param strs: A list of strings
     * @return: The longest common prefix
     */
    public String longestCommonPrefix(String[] strs) {
        if(strs == null || strs.length == 0)
            return "";
        String prefix = strs[0];
        for(int i = 1; i < strs.length; i++) {
            int j = 0;
            while(j < prefix.length() && j < strs[i].length() && prefix.charAt(j)==strs[i].charAt(j))
                j++;
            prefix = prefix.substring(0,j);
        }
        return prefix;
    }
}

```

---

## @@ 最长公共子序列

给出两个字符串，找到最长公共子序列(LCS)，返回LCS的长度。

样例

给出"ABCD" 和 "EDCA"，这个LCS是 "A" (或 D或C)，返回1

给出 "ABCD" 和 "EACB"，这个LCS是"AC"返回 2

**题解**

DP.

1. D[i][j] 定义为s1, s2的前i,j个字符串的最长common subsequence.
2. D[i][j] 当char i == char j， D[i - 1][j - 1] + 1

当char i != char j, D[i ][j - 1], D[i - 1][j] 里取一个大的（因为最后一个不相同，所以有可能s1的最后一个字符会出现在s2的前部分里，反之亦然。

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

## @@ 最长上升子序列

给定一个整数序列，找到最长上升子序列（LIS），返回LIS的长度。

样例

给出[5,4,1,2,3]，这个LIS是[1,2,3]，返回 3

给出[4,2,4,5,3,7]，这个LIS是[4,4,5,7]，返回 4

挑战

要求时间复杂度为O(n^2) 或者O(nlogn)

**题解**

A DP Solution:

This is a sequence DP problem, so we define

1. dp[N], whereas dp[i] denotes the length of the LIS including the array element arr[i].
2. Initial state: dp[i] = 1
3. Transit function: for each j, where 0 <= j < i, if (A[i] >= A[j]), dp[i] = Math.max(dp[i], dp[j] + 1);
4. Final state: result = 1, Math.max(result, dp[i]);

```java
public class Solution {
    /**
     * @param nums: The integer array
     * @return: The length of LIS (longest increasing subsequence)
     */
    public int longestIncreasingSubsequence(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }

        if (nums.length == 1) {
            return 1;
        }

        int[] dp = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            dp[i] = 1;
        }

        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] >= nums[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }

        int result = 1;
        for (int i = 0; i < nums.length; i++) {
            result = Math.max(dp[i], result);
        }

        return result;
    }
}


```

---

## @@ 寻找峰值

你给出一个整数数组(size为n)，其具有以下特点：

+ 相邻位置的数字是不同的
+ A[0] < A[1] 并且 A[n - 2] > A[n - 1]

假定P是峰值的位置则满足A[P] > A[P-1]且A[P] > A[P+1]，返回数组中任意一个峰值的位置。

样例

给出数组[1, 2, 1, 3, 4, 5, 7, 6]返回1, 即数值 2 所在位置, 或者6, 即数值 7 所在位置.

注意

数组可能包含多个峰值，只需找到其中的任何一个即可

**题解**

由时间复杂度的暗示可知应使用二分搜索。首先分析若使用传统的二分搜索，若A[mid] > A[mid - 1] && A[mid] < A[mid + 1]，则找到一个peak为A[mid]；若A[mid - 1] > A[mid]，则A[mid]左侧必定存在一个peak，可用反证法证明：若左侧不存在peak，则A[mid]左侧元素必满足A[0] > A[1] > ... > A[mid -1] > A[mid]，与已知A[0] < A[1]矛盾，证毕。同理可得若A[mid + 1] > A[mid]，则A[mid]右侧必定存在一个peak。如此迭代即可得解。

```java
class Solution {
    /**
     * @param A: An integers array.
     * @return: return any of peek positions.
     */
    public int findPeak(int[] A) {
        if (A == null) {
            return -1;
        }
        if (A.length == 0) {
            return 0;
        }

        int start = 0, end = A.length - 1, mid = end / 2;
        while (start + 1 < end) {
            mid = start + (end - start)/2;
            if (A[mid] < A[mid - 1]) {
                end = mid;
            } else if (A[mid] < A[mid + 1]) {
                start = mid;
            } else {
                return mid;
            }
        }

        mid = (A[start] > A[end]) ? start : end;
        return mid;
    }
}


```

---

## @@ 第一个错误的代码版本

代码库的版本号是从 1 到 n 的整数。某一天，有人提交了错误版本的代码，因此造成自身及之后版本的代码在单元测试中均出错。请找出第一个错误的版本号。

你可以通过 isBadVersion 的接口来判断版本号 version 是否在单元测试中出错，具体接口详情和调用方法请见代码的注释部分。

样例

给出 n=5

调用isBadVersion(3)，得到false

调用isBadVersion(5)，得到true

调用isBadVersion(4)，得到true

此时我们可以断定4是第一个错误的版本号

注意

请阅读上述代码，对于不同的语言获取正确的调用 isBadVersion 的方法，比如java的调用方式是VersionControl.isBadVersion

挑战

调用 isBadVersion 的次数越少越好

**题解**

二分法即可

```java
/**
 * public class VersionControl {
 *     public static boolean isBadVersion(int k);
 * }
 * you can use VersionControl.isBadVersion(k) to judge whether
 * the kth code version is bad or not.
*/
class Solution {
    /**
     * @param n: An integers.
     * @return: An integer which is the first bad version.
     */
    public int findFirstBadVersion(int n) {
        if (n == 1) {
            return 1;
        }

        int left = 1;
        int right = n;

        while (left < right) {
            int mid = left + (right - left) / 2;
            if (VersionControl.isBadVersion(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return right;
    }
}


```

---

## @@ 前序遍历和中序遍历树构造二叉树

根据前序遍历和中序遍历树构造二叉树.

样例

给出中序遍历：[1,2,3]和前序遍历：[2,1,3]. 返回如下的树:

      2
     / \
    1   3

注意

你可以假设树中不存在相同数值的节点

**题解**

二叉树的重建，典型题。核心有两点：

1. preorder 先序遍历的第一个节点即为根节点。
2. 确定 inorder 数组中的根节点后其左子树和右子树也是 preorder 的左子树和右子树。

其中第二点是隐含条件，数组中没有重复元素，故可以根据先序遍历中第一个元素（根节点）得到根节点的值，然后在 inorder 中序遍历的数组中搜索得到根节点的索引值，即为左子树，右边为右子树。根据中序遍历中左子树的索引确定先序遍历数组中左子树的起止索引。递归直至处理完所有数组元素

```java
/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */


public class Solution {
    /**
     *@param preorder : A list of integers that preorder traversal of a tree
     *@param inorder : A list of integers that inorder traversal of a tree
     *@return : Root of a tree
     */
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder == null || inorder == null) return null;
        if (preorder.length == 0 || inorder.length == 0) return null;
        if (preorder.length != inorder.length) return null;

        TreeNode root = helper(preorder, 0, preorder.length - 1,
                               inorder, 0, inorder.length - 1);
        return root;
    }

    private TreeNode helper(int[] preorder, int prestart, int preend,
                            int[] inorder, int instart, int inend) {
        // corner cases
        if (prestart > preend || instart > inend) return null;
        // build root TreeNode
        int root_val = preorder[prestart];
        TreeNode root = new TreeNode(root_val);
        // find index of root_val in inorder[]
        int index = findIndex(inorder, instart, inend, root_val);
        // build left subtree
        root.left = helper(preorder, prestart + 1, prestart + index - instart,
               inorder, instart, index - 1);
        // build right subtree
        root.right = helper(preorder, prestart + index - instart + 1, preend,
               inorder, index + 1, inend);
        return root;
    }

    private int findIndex(int[] nums, int start, int end, int target) {
        for (int i = start; i <= end; i++) {
            if (nums[i] == target) return i;
        }
        return -1;
    }
}

```
源码分析

由于需要知道左右子树在数组中的索引，故需要引入辅助方法。找根节点这个大家都能很容易地想到，但是最关键的一步——找出左右子树的起止索引，这一点就不那么直接了，老实说想了很久忽略了这个突破点。

复杂度分析

findIndex 时间复杂度近似 O(n), helper 递归调用，每次调用都需要找中序遍历数组中的根节点，故总的时间复杂度为 O(n^2). 原地生成最终二叉树，空间复杂度为 O(1).

---

## @@ 中序遍历和后序遍历树构造二叉树

根据中序遍历和后序遍历树构造二叉树

样例

给出树的中序遍历： [1,2,3] 和后序遍历： [1,3,2]

返回如下的树：

      2
     /  \
    1    3

注意

你可以假设树中不存在相同数值的节点

**题解**

和题 Construct Binary Tree from Preorder and Inorder Traversal 几乎一致，关键在于找到中序遍历中的根节点和左右子树，递归解决。

```java
/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */


public class Solution {
    /**
     *@param inorder : A list of integers that inorder traversal of a tree
     *@param postorder : A list of integers that postorder traversal of a tree
     *@return : Root of a tree
     */
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if (inorder == null || postorder == null) return null;
        if (inorder.length == 0 || postorder.length == 0) return null;
        if (inorder.length != postorder.length) return null;

        TreeNode root = helper(inorder, 0, inorder.length - 1,
               postorder, 0, postorder.length - 1);
        return root;
    }

    private TreeNode helper(int[] inorder, int instart, int inend,
                            int[] postorder, int poststart, int postend) {
        // corner cases
        if (instart > inend || poststart > postend) return null;

        // build root TreeNode
        int root_val = postorder[postend];
        TreeNode root = new TreeNode(root_val);
        // find index of root_val in inorder[]
        int index = findIndex(inorder, instart, inend, root_val);
        // build left subtree
        root.left = helper(inorder, instart, index - 1,
                           postorder, poststart, poststart + index - instart - 1);
        // build right subtree
        root.right = helper(inorder, index + 1, inend,
                           postorder, poststart + index - instart, postend - 1);
        return root;
    }

    private int findIndex(int[] nums, int start, int end, int target) {
        for (int i = start; i <= end; i++) {
            if (nums[i] == target) return i;
        }
        return -1;
    }
}

```

---

## @@ 二叉树的锯齿形层次遍历

给出一棵二叉树，返回其节点值的锯齿形层次遍历（先从左往右，下一层再从右往左，层与层之间交替进行）

样例

给出一棵二叉树 {3,9,20,#,#,15,7},

        3
       / \
      9  20
        /  \
       15   7

返回其锯齿形的层次遍历为：

    [
      [3],
      [20,9],
      [15,7]
    ]

**题解**

```java
/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */


public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: A list of lists of integer include
     *          the zigzag level order traversal of its nodes' values
     */
    public ArrayList<ArrayList<Integer>> zigzagLevelOrder(TreeNode root) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
        if(root == null) return res;
        Stack<TreeNode> stack = new Stack<TreeNode>();
        stack.push(root);
        boolean left = true;
        while(!stack.isEmpty()){
            int size = stack.size();
            ArrayList<Integer> sub = new ArrayList<Integer>();
            Stack<TreeNode> nextStack = new Stack<TreeNode>();
            while(!stack.isEmpty()){
                TreeNode node = stack.pop();
                sub.add(node.val);
                if(left){
                    if(node.left != null) nextStack.add(node.left);
                    if(node.right != null) nextStack.add(node.right);
                } else {
                    if(node.right != null) nextStack.add(node.right);
                    if(node.left != null) nextStack.add(node.left);
                }

            }
            res.add(sub);
            left = !left;
            stack = nextStack;
        }

        return res;
    }
}

```

---

## @@ 二叉树的层次遍历

给出一棵二叉树，返回其节点值的层次遍历（逐层从左往右访问）

样例
给出一棵二叉树 {3,9,20,#,#,15,7},

        3
       / \
      9  20
        /  \
       15   7

返回它的层次遍历为：

    [
      [3],
      [9,20],
      [15,7]
    ]

挑战

只使用一个队列去实现它

**题解**

正常队列 bfs

```java
/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */


public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: Level order a list of lists of integer
     */
    public ArrayList<ArrayList<Integer>> levelOrder(TreeNode root) {
        ArrayList result = new ArrayList();

        if (root == null) {
            return result;
        }

        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.offer(root);

        while (!queue.isEmpty()) {
            ArrayList<Integer> level = new ArrayList<Integer>();
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                TreeNode head = queue.poll();
                level.add(head.val);
                if (head.left != null) {
                    queue.offer(head.left);
                }
                if (head.right != null) {
                    queue.offer(head.right);
                }
            }
            result.add(level);
        }

        return result;
    }
}

```

---

## @@ 二叉树的层次遍历 II

给出一棵二叉树，返回其节点值从底向上的层次序遍历（按从叶节点所在层到根节点所在的层遍历，然后逐层从左往右遍历）

样例

给出一棵二叉树 {3,9,20,#,#,15,7},

        3
       / \
      9  20
        /  \
       15   7

按照从下往上的层次遍历为：

    [
      [15,7],
      [9,20],
      [3]
    ]

**题解**

```java
/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */


public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: buttom-up level order a list of lists of integer
     */
    public ArrayList<ArrayList<Integer>> levelOrderBottom(TreeNode root) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
        if(root == null) return res;
        Queue<TreeNode> queue = new LinkedList<TreeNode>();
        queue.offer(root);
        while(!queue.isEmpty()){
            int size = queue.size();
            ArrayList<Integer> sub = new ArrayList<Integer>();
            for(int i = 0; i < size; i++){
                TreeNode node = queue.poll();
                sub.add(node.val);
                if(node.left != null) queue.add(node.left);
                if(node.right != null) queue.add(node.right);
            }
            res.add(0,sub);
        }

        return res;
    }
}

```

---

## @@ 背包问题

在n个物品中挑选若干物品装入背包，最多能装多满？假设背包的大小为m，每个物品的大小为A[i]

样例

如果有4个物品[2, 3, 5, 7]

如果背包的大小为11，可以选择[2, 3, 5]装入背包，最多可以装满10的空间。

如果背包的大小为12，可以选择[2, 3, 7]装入背包，最多可以装满12的空间。

函数需要返回最多能装满的空间大小。

注意

你不可以将物品进行切割。

**题解**

The problem does not care how many items you can put in the backpack, it cares how you can choose the proper combination of items to fully fill the backpack.
We create a boolean array full[n + 1][m + 1], with full[i][j] indicating whether items in A[0] … A[i] could fulfill the backpack with size j.

```java
public class Solution {
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A: Given n items with size A[i]
     * @return: The maximum size
     */
    public int backPack(int m, int[] A) {
        if (A == null || A.length == 0) {
            return 0;
        }
        boolean full[] = new boolean[m + 1];
        boolean lastFull[] = new boolean[m + 1];
        full[0] = true;
        for (int i = 0; i < A.length; i++) {
            System.arraycopy(full, 0, lastFull, 0, m + 1);
            for (int size = 1; size <= m; size++) {
                if (size >= A[i] && lastFull[size - A[i]]) {
                    full[size] = true;
                } else {
                    full[size] = lastFull[size];
                }
            }
        }
        for (int size = m; size >= 1; size--) {
            if (full[size]) {
                return size;
            }
        }
        return 0;
    }
}

```

---

## @@ 平衡二叉树

给定一个二叉树,确定它是高度平衡的。对于这个问题,一棵高度平衡的二叉树的定义是：一棵二叉树中每个节点的两个子树的深度相差不会超过1。

样例

给出二叉树 A={3,9,20,#,#,15,7}, B={3,#,20,15,7}

    A)  3            B)    3
       / \                  \
      9  20                 20
        /  \                / \
       15   7              15  7

二叉树A是高度平衡的二叉树，但是B不是

**题解**

很锻炼DP/recursive思路的一道题，个人感觉DP/recursive算是比较难写的题目了。这道题解法的巧妙之处在于巧用-1，并且使用临时存储，节省了很多开支。

```java
/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: True if this Binary tree is Balanced, or false.
     */
    public boolean isBalanced(TreeNode root) {
        if (root == null) return true;
        if (checkBalance(root) != -1) return true;
        else return false;
    }

    public int checkBalance(TreeNode root) {
        if (root == null) return 0;
        int leftHeight = checkBalance(root.left);
        int rightHeight = checkBalance(root.right);
        if (leftHeight == -1 || rightHeight == -1) return -1;
        else if (Math.abs(leftHeight - rightHeight) > 1) return -1;
        return Math.max(leftHeight, rightHeight) + 1;
    }
}

```

---


## @@ 二叉树中的最大路径和

给出一棵二叉树，寻找一条路径使其路径和最大，路径可以在任一节点中开始和结束（路径和为两个节点之间所在路径上的节点权值之和）

样例

给出一棵二叉树：

       1
      / \
     2   3

返回 6

**题解**

思路

1. 最优路径上的节点一定是连续的，不能中断
2. 最优路径中一定包含某个子树的根节点
3. 写一个递归函数，实现计算根节点到任意点的最大路径和，以及穿过根节点的最大路径和，用一个全局变量保存最优解。

```java
/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: An integer.
     */
    int maxSum = Integer.MIN_VALUE;
    public int maxPathSum(TreeNode root) {
        _getMaxSum(root);
        return maxSum;
    }

    private int _getMaxSum(TreeNode root){
        if(root == null) return 0;
        int left = _getMaxSum(root.left);
        int right = _getMaxSum(root.right);
        int sum = left > 0 ? left : 0;
        sum += right > 0 ? right : 0;
        sum += root.val;
        maxSum = Math.max(maxSum, sum);
        return Math.max(left, right) + root.val;
    }
}

```

---

## @@ 验证二叉查找树

给定一个二叉树，判断它是否是合法的二叉查找树(BST)

一棵BST定义为：

1. 节点的左子树中的值要严格小于该节点的值。
2. 节点的右子树中的值要严格大于该节点的值。
3. 左右子树也必须是二叉查找树。

样例

一个例子：

       1
      / \
     2   3
        /
       4
        \
         5

上述这棵二叉树序列化为"{1,2,3,#,#,4,#,#,5}".

**题解**

用中序遍历的方法遍历BST，BST的性质是遍历后数组是有序的。根据这一点我们只需要中序遍历这棵树，然后保存前驱结点，每次检测是否满足递增关系即可。注意以下代码我么用一个一个变量的数组去保存前驱结点，原因是java没有传引用的概念，如果传入一个变量，它是按值传递的，所以是一个备份的变量，改变它的值并不能影响它在函数外部的值，算是java中的一个小细节。

```java
/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: True if the binary tree is BST, or false
     */
    public boolean isValidBST(TreeNode root) {
        ArrayList<Integer> pre = new ArrayList<Integer>();
        pre.add(null);
        return helper(root, pre);
    }
    private boolean helper(TreeNode root, ArrayList<Integer> pre)
    {
        if(root == null)
            return true;
        boolean left = helper(root.left,pre);
        if(pre.get(0)!=null && root.val<=pre.get(0))
            return false;
        pre.set(0,root.val);
        return left && helper(root.right,pre);
    }
}

```

---

## @@ k 数和 II

给定 n 个不同的正整数，整数 k（1<= k <= n）以及一个目标数字。　　　　

在这 n 个数里面找出 K 个数，使得这 K 个数的和等于目标数字，你需要找出所有满足要求的方案。

样例

给出[1,2,3,4]，k=2， target=5，返回 [[1,4],[2,3]]

**题解**

同Combination Sum II

```java
public class Solution {
    /**
     * @param A: an integer array.
     * @param k: a positive integer (k <= length(A))
     * @param target: a integer
     * @return a list of lists of integer
     */
    public ArrayList<ArrayList<Integer>> kSumII(int A[], int k, int target) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> path = new ArrayList<Integer>();
        helper(res, path, A, k, target, 0);
        return res;
    }

    public void helper(ArrayList<ArrayList<Integer>> res, ArrayList<Integer> path, int[] A, int k, int remain, int index) {
        if (path.size() == k) {
            if (remain == 0) {
                res.add(new ArrayList<Integer>(path));
            }
            return;
        }
        for (int i=index; i<A.length; i++) {
            path.add(A[i]);
            helper(res, path, A, k, remain-A[i], i+1);
            path.remove(path.size()-1);
        }
    }
}


```

---

## @@ 最近公共祖先

给定一棵二叉树，找到两个节点的最近公共父节点(LCA)。

最近公共祖先是两个节点的公共的祖先节点且具有最大深度。

样例

对于下面这棵二叉树

      4
     / \
    3   7
       / \
      5   6

LCA(3, 5) = 4

LCA(5, 6) = 7

LCA(6, 7) = 7

**题解**

前提条件是查询的两个节点node1和node2是在tree里的，如果没有这个前提条件，我们可以先遍历一遍tree来看这两个node是不是在tree里，由于LCA的算法是O(n)，执行之前确定两个node是否在tree里也是O(n)的，不会影响时间复杂度。这里我们假设这个前提条件是成立的。同样用bottom-up的方法，return的策略如下：

+ 如果curr是null，return null
+ 如果curr等于node1或者node2，return curr。这时候有两种情况，curr就是LCA或者LCA是其他。，如果curr就是LCA那么它会被一直return上去，如果不是的话，找到其他的会return真正的LCA
+ 如果left和right return的都不是null，说明curr就是LCA，return curr, curr会一直被return上去
+ 如果left和right return的都是null，return null
+ 如果left或者right不等于null，return 不是null的那一个，这是为了保证可能是结果的node可以被传上去

```java
/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param root: The root of the binary search tree.
     * @param A and B: two nodes in a Binary.
     * @return: Return the least common ancestor(LCA) of the two nodes.
     */
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode A, TreeNode B) {
        if (root == null)
            return null;
        if (root == A || root == B)
            return root;
        TreeNode left = lowestCommonAncestor(root.left, A, B);
        TreeNode right = lowestCommonAncestor(root.right, A, B);
        if (left != null && right != null)
            return root;
        else
            return left == null? right: left;
    }
}

```

---

## @ 落单的数 II

给出3*n + 1 个的数字，除其中一个数字之外其他每个数字均出现三次，找到这个数字。

样例

给出 [1,1,2,3,3,3,2,2,4,1] ，返回 4

挑战

一次遍历，常数级的额外空间复杂度

**题解**

三个相同的数相加，不仅其和能被3整除，其二进制位上的每一位也能被3整除！因此我们只需要一个和int类型相同大小的数组记录每一位累加 的结果即可。时间复杂度约为 O((3n+1)⋅sizeof(int)⋅8)

```java
public class Solution {
    /**
     * @param A : An integer array
     * @return : An integer
     */
    public int singleNumberII(int[] A) {
        if (A == null || A.length == 0) {
            return -1;
        }
        int result=0;
        int[] bits=new int[32];
        for (int i = 0; i < 32; i++) {
            for(int j = 0; j < A.length; j++) {
                bits[i] += A[j] >> i & 1;
                bits[i] %= 3;
            }

            result |= (bits[i] << i);
        }
        return result;
    }
}

```

---

## @@ 落单的数 III

给出2*n + 2个的数字，除其中两个数字之外其他每个数字均出现两次，找到这两个数字。

样例

给出 [1,2,2,3,4,4,5,3]，返回 1和5

挑战

O(n)时间复杂度，O(1)的额外空间复杂度

**题解**

与以上两题不同的是，这道题有两个数只出现一次。基本的思路还是利用位运算，除去出现次数为2次的数。

如果对所有元素进行异或操作，最后剩余的结果是出现次数为1次的两个数的异或结果，此时无法直接得到这两个数具体的值。但是，因为这两个数一定是不同的，所以最终异或的值至少有一个位为1。我们可以找出异或结果中第一个值为1的位，然后根据该位的值是否为1，将数组中的每一个数，分成两个部分。这样每个部分，就可以采用Sing number I中的方法得到只出现一次的数。

利用bitwise XOR的特点，n个数（0或1），如果1的个数为奇数，则n个数bitwise XOR结果为1，否则为0

先将所有的数异或，得到的将是x和y以后之后的值n。 找到这个数n的为1的某一位（为了方便就取最右边为1的一位， n & ~(n-1)，再将这一位为1的数异或，其余的数异或，得到的就是x和y的值。

```java
public class Solution {
    /**
     * @param A : An integer array
     * @return : Two integers
     */
    public List<Integer> singleNumberIII(int[] A) {
        ArrayList<Integer> res = new ArrayList<Integer>();
        res.add(0);
        res.add(0);
        int n = 0;
        for (int elem : A) {
            n ^= elem;
        }
        n = n & (~(n-1));
        for (int elem : A) {
            if ((elem & n) != 0) {
                res.set(0, res.get(0)^elem);
            }
            else res.set(1, res.get(1)^elem);
        }
        return res;
    }
}

```

---


## @@ 单词接龙

给出两个单词（start和end）和一个字典，找到从start到end的最短转换序列

比如：

1. 每次只能改变一个字母。
2. 变换过程中的中间单词必须在字典中出现。

样例

给出数据如下：

start = "hit"

end = "cog"

dict = ["hot","dot","dog","lot","log"]

一个最短的变换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog"，

返回它的长度 5

注意

+ 如果没有转换序列则返回0。
+ 所有单词具有相同的长度。
+ 所有单词都只包含小写字母。

**题解**

一开始看到string会以为是类似array的问题，但是其实是graph的问题 找最短路径，应该用BFS而不是DFS BFS搜索，最先搜索到的一定是最短路径

这种题，肯定是每次改变单词的一个字母，然后逐渐搜索，很多人一开始就想到用dfs，其实像这种求最短路径、树最小深度问题bfs最适合，可以参考我的这篇博客bfs（层序遍历）求二叉树的最小深度。本题bfs要注意的问题：

和当前单词相邻的单词是：对当前单词改变一个字母且在字典中存在的单词
一开始我使用每个dict里面的word和curr比较是否是neighbour的方式，但是这个会随着dict越大计算次数越多，会超时

使用每个位置改变26个字母来找neighbours的方法，只需要使用固定的26 * len(word)的time

找到一个单词的相邻单词，加入bfs队列后，要从字典中删除，因为不删除的话会造成类似于hog->hot->hog的死循环。而删除对求最短路径没有影响，因为我们第一次找到该单词肯定是最短路径，即使后面其他单词也可能转化得到它，路径肯定不会比当前的路径短（如果要输出所有最短路径，则不能立即从字典中删除，具体见下一题）

```java
public class Solution {
    /**
      * @param start, a string
      * @param end, a string
      * @param dict, a set of string
      * @return an integer
      */
    public int ladderLength(String start, String end, Set<String> dict) {
         if(start == null || end == null || start.equals(end)) return 0;

        Queue<String> from = new LinkedList<String>();
        HashSet<String> record = new HashSet<String>();
        from.offer(start);
        record.add(start);
        int count = 1;
        while(!from.isEmpty()){
            Queue<String> to = new LinkedList<String>();
            while(!from.isEmpty()){
                String word = from.poll();
                if(word.equals(end)) return count;
                for(int i = 0; i < word.length(); i++){
                    for(char c = 'a'; c <= 'z'; c++){
                        char[] arr = word.toCharArray();
                        if(arr[i] != c){
                            arr[i] = c;
                            String newWord = new String(arr);
                            if(end.equals(newWord)) return count+1;
                            if(!record.contains(newWord) && dict.contains(newWord)){
                                record.add(newWord);
                                to.add(newWord);
                            }
                        }
                    }
                }
            }
            count++;
            from = to;
        }
        return count;
    }
}

```

---

## @@ 编辑距离

给出两个单词word1和word2，计算出将word1 转换为word2的最少操作次数。

你总共三种操作方法：

+ 插入一个字符
+ 删除一个字符
+ 替换一个字符

样例

给出 work1="mart" 和 work2="karma"

返回 3

**题解**

res[i][j]表示Edit Distance between X数组的前i个元素以及Y数组的前j个元素，或者the minimum # of operations to convert X前i个元素 into Y的前j个元素

因为对于Xi 和 Yj，操作无非是 insert, delete, replace三种，所以递归式就是三项：根据上面这个图很清楚：res[i][j] = min{res[i-1][j]+1, res[i][j-1]+1, Xi == Yj ? res[i-1][j-1] : res[i-1][j-1] + 1}

```java
public class Solution {
    /**
     * @param word1 & word2: Two string.
     * @return: The minimum number of steps.
     */
    public int minDistance(String word1, String word2) {
        if (word1==null && word2!=null) return word2.length();
        if (word1!=null && word2==null) return word1.length();
        if (word1==null && word2==null) return 0;
        int[][] res = new int[word1.length()+1][word2.length()+1];
        for (int i=1; i<=word1.length(); i++) {
            res[i][0] = i;
        }
        for (int j=1; j<=word2.length(); j++) {
            res[0][j] = j;
        }
        for (int m=1; m<=word1.length(); m++) {
            for (int n=1; n<=word2.length(); n++) {
                res[m][n] = Math.min(Math.min(res[m-1][n]+1, res[m][n-1]+1), word1.charAt(m-1)==word2.charAt(n-1)? res[m-1][n-1] : res[m-1][n-1]+1);
            }
        }
        return res[word1.length()][word2.length()];
    }
}

```

---

## @@ 不同的子序列

给出字符串S和字符串T，计算S的不同的子序列中T出现的个数。

子序列字符串是原始字符串通过删除一些(或零个)产生的一个新的字符串，并且对剩下的字符的相对位置没有影响。(比如，“ACE”是“ABCDE”的子序列字符串,而“AEC”不是)。

样例

给出S = "rabbbit", T = "rabbit"

返回 3

**题解**

递归解法，首先，从个字符串S的尾部开始扫描，找到第一个和T最后一个字符相同的位置k，那么有下面两种匹配：a. T的最后一个字符和S[k]匹配，b. T的最后一个字符不和S[k]匹配。a相当于子问题:从S[0...lens-2]中删除几个字符得到T[0...lent-2]，b相当于子问题：从S[0...lens-2]中删除几个字符得到T[0...lent-1]。那么总的删除方法等于a、b两种情况的删除方法的和。递归解法代码如下，但是通过大数据会超时：

动态规划，设dp[i][j]是从字符串S[0...i]中删除几个字符得到字符串T[0...j]的不同的删除方法种类，有上面递归的分析可知，动态规划方程如下

+ 如果S[i] = T[j], dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
+ 如果S[i] 不等于 T[j], dp[i][j] = dp[i-1][j]

初始条件：当T为空字符串时，从任意的S删除几个字符得到T的方法为1

Consider s=”EEACC” and t=”EAC”. num[i][j] means how many distinct sequence for T[0..i-1] in S[0..j-1]

Two cases for each num[i][j]:

num[i][j] inherits from num[i][j-1]. This means overlooking s[j], t[0..i] at least keeps the number of distinct sequences in s[0..j-1]. This case finds all sequences of t[0..i] in s[o..j] without s[j].

if t[i]==s[j], this means t[i] could be mapped to s[j], we cannot overlook s[j].  We look at the number of t[0..i-1] in s[0..j-1], and add it to the result. This case finds all sequences of t[0..i] in s[o..j] with s[j].

```java
public class Solution {
    /**
     * @param S, T: Two string.
     * @return: Count the number of distinct subsequences
     */
    public int numDistinct(String s, String t) {
        if (s==null || t==null || (s.length()==0 && t.length()!=0)) return 0;
        if (t.length()==0) return 1;
        int[] pre = new int[s.length()+1];
        Arrays.fill(pre,1);
        for (int i=1; i<=t.length(); i++){
            int[] cur = new int[s.length()+1];
            cur[0] = 0;
            for (int j=1; j<=s.length(); j++){
                if (s.charAt(j-1)==t.charAt(i-1)){
                    cur[j]+=pre[j-1];
                }
                cur[j] += cur[j-1];
            }
            System.arraycopy(cur, 0, pre, 0, cur.length);
        }
        return pre[s.length()];
    }
}

```

---

## @@ 跳跃游戏

给出一个非负整数数组，你最初定位在数组的第一个位置。　　　

数组中的每个元素代表你在那个位置可以跳跃的最大长度。　　　　

判断你是否能到达数组的最后一个位置。

样例

A = [2,3,1,1,4]，返回 true.

A = [3,2,1,0,4]，返回 false.

注意

这个问题有两个方法，一个是贪心和 动态规划。

贪心方法时间复杂度为O（N）。

动态规划方法的时间复杂度为为O（n^2）。

我们手动设置小型数据集，使大家阔以通过测试的两种方式。这仅仅是为了让大家学会如何使用动态规划的方式解决此问题。如果您用动态规划的方式完成它，你可以尝试贪心法，以使其再次通过一次。

**题解**

dp

```java
public class Solution {
    /**
     * @param A: A list of integers
     * @return: The boolean answer
     */
    public boolean canJump(int[] A) {
        boolean[] can = new boolean[A.length];
        can[0] = true;

        for (int i = 1; i < A.length; i++) {
            for (int j = 0; j < i; j++) {
                if (can[j] && j + A[j] >= i) {
                    can[i] = true;
                    break;
                }
            }
        }

        return can[A.length - 1];
    }
}


```

---

## @@ 跳跃游戏 II

给出一个非负整数数组，你最初定位在数组的第一个位置。

数组中的每个元素代表你在那个位置可以跳跃的最大长度。　　　

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

样例

给出数组A = [2,3,1,1,4]，最少到达数组最后一个位置的跳跃次数是2(从数组下标0跳一步到数组下标1，然后跳3步到数组的最后一个位置，一共跳跃2次)

**题解**

dp

```java
public class Solution {
    /**
     * @param A: A list of lists of integers
     * @return: An integer
     */
    public int jump(int[] A) {
        int[] steps = new int[A.length];

        steps[0] = 0;
        for (int i = 1; i < A.length; i++) {
            steps[i] = Integer.MAX_VALUE;
            for (int j = 0; j < i; j++) {
                if (steps[j] != Integer.MAX_VALUE && j + A[j] >= i) {
                    steps[i] = steps[j] + 1;
                    break;
                }
            }
        }

        return steps[A.length - 1];
    }
}


```

---

## @@ 删除排序链表中的重复数字 II

给定一个排序链表，删除所有重复的元素只留下原链表中没有重复的元素。

样例

给出1->2->3->3->4->4->5->null，返回1->2->5->null

给出1->1->1->2->3->null，返回 2->3->null

**题解**

上题为保留重复值节点的一个，这题删除全部重复节点，看似区别不大，但是考虑到链表头不确定(可能被删除，也可能保留)，因此若用传统方式需要较多的if条件语句。这里介绍一个处理链表头节点不确定的方法——引入dummy node.

    ListNode *dummy = new ListNode(0);
    dummy->next = head;
    ListNode *node = dummy;

引入新的指针变量dummy，并将其next变量赋值为head，考虑到原来的链表头节点可能被删除，故应该从dummy处开始处理，这里复用了head变量。考虑链表A->B->C，删除B时，需要处理和考虑的是A和C，将A的next指向C。如果从空间使用效率考虑，可以使用head代替以上的node，含义一样，node比较好理解点。

与上题不同的是，由于此题引入了新的节点dummy，不可再使用node->val == node->next->val，原因有二：

1. 此题需要将值相等的节点全部删掉，而删除链表的操作与节点前后两个节点都有关系，故需要涉及三个链表节点。且删除单向链表节点时不能删除当前节点，只能改变当前节点的next指向的节点。
2. 在判断val是否相等时需先确定node->next和node->next->next均不为空，否则不可对其进行取值。

```java
/**
 * Definition for ListNode
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param ListNode head is the head of the linked list
     * @return: ListNode head of the linked list
     */
    public static ListNode deleteDuplicates(ListNode head) {
        if (head == null) return null;

        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode node = dummy;
        while(node.next != null && node.next.next != null) {
            if (node.next.val == node.next.next.val) {
                int val_prev = node.next.val;
                while (node.next != null && node.next.val == val_prev) {
                    node.next = node.next.next;
                }
            } else {
                node = node.next;
            }
        }

        return dummy.next;
    }
}


```

---

## @@ 分割回文串 II

给定一个字符串s，将s分割成一些子串，使每个子串都是回文。

返回s符合要求的的最少分割次数。

样例

比如，给出字符串s = "aab"，

返回 1， 因为进行一次分割可以将字符串s分割成["aa","b"]这样两个回文子串

**题解**

使用DP来解决：

1. D[i]  表示前i 个字符切为回文需要的切割数
2. P[i][j]: S.sub(i-j) is a palindrome.
3. 递推公式： D[i] = Math.min(D[i], D[j] + 1), 0 <= j <= i - 1) ，并且要判断 P[j][i - 1]是不是回文。
4. 注意D[0] = -1的用意，它是指当整个字符串判断出是回文是，因为会D[0] + 1 其实应该是结果为0（没有任何切割），所以，应把D[0] 设置为-1

有个转移函数之后，一个问题出现了，就是如何判断[i,j]是否是回文？每次都从i到j比较一遍？太浪费了，这里也是一个DP问题。

定义函数

P[i][j] = true if [i,j]为回文

那么
P[i][j] = str[i] == str[j] && P[i+1][j-1];

```java
public class Solution {
    /**
     * @param s a string
     * @return an integer
     */
    public int minCut(String s) {
        if (s == null || s.length() == 0) {
            return 0;
        }

        int len = s.length();

        // D[i]: 前i 个字符切为回文需要的切割数
        int[] D = new int[len + 1];
        D[0] = -1;

        // P[i][j]: S.sub(i-j) is a palindrome.
        boolean[][] P = new boolean[len][len];

        for (int i = 1; i <= len; i++) {
            // The worst case is cut character one by one.
            D[i] = i - 1;
            for (int j = 0; j <= i - 1; j++) {
                P[j][i - 1] = false;
                if (s.charAt(j) == s.charAt(i - 1) && (i - 1 - j <= 2 || P[j + 1][i - 2])) {
                    P[j][i - 1] = true;
                    D[i] = Math.min(D[i], D[j] + 1);
                }
            }
        }

        return D[len];
    }
};

```

---

## @@ 复制带随机指针的链表

给出一个链表，每个节点包含一个额外增加的随机指针可以指向链表中的任何节点或空的节点。

返回一个深拷贝的链表。

挑战

可否使用O(1)的空间

**题解**

Using HashMap to store the RandomListNode info.

We can create a hashMap<RandomListNode, RandomListNode>, the Key stores the original ListNode, and the value stores the new RandomListNode.

In the implementation, we only need to iterate the RandomListNode once. and for each original node, we first copy the next pointer. and then copy the Random pointer.

The important is every time when you copy the next or the random pointer, you should check whether the node is/not exist.

```java
/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    /**
     * @param head: The head of linked list with a random pointer.
     * @return: A new head of a deep copy of the list.
     */
    public RandomListNode copyRandomList(RandomListNode head) {
        if (null == head) {
       return null;
       }
       Map<RandomListNode, RandomListNode> map = new HashMap<RandomListNode, RandomListNode>();
       RandomListNode dummy = new RandomListNode(-1);
       dummy.next = head;

       RandomListNode copyNode = dummy;
       RandomListNode temp;

       while (head != null) {
           // copy current node
           if (map.containsKey(head)) {
               temp = map.get(head);
           } else {
               temp = new RandomListNode(head.label);
               map.put(head, temp);
           }
           copyNode.next = temp;
           // copy random node
           if (head.random != null) {
               if (map.containsKey(head.random)) {
                   temp.random = map.get(head.random);
               } else {
                   temp.random = new RandomListNode(head.random.label);
                   map.put(head.random, temp.random);
               }
           }
           copyNode = copyNode.next;
           head = head.next;
       }
       return dummy.next;
    }
}

```

---

## @@ 最小调整代价

给一个整数数组，调整每个数的大小，使得相邻的两个数的差小于一个给定的整数target，调整每个数的代价为调整前后的差的绝对值，求调整代价之和最小是多少。

样例

对于数组[1, 4, 2, 3]和target=1，最小的调整方案是调整为[2, 3, 2, 3]，调整代价之和是2。返回2。

注意

你可以假设数组中每个整数都是正整数，且小于等于100。

**题解**

这道题要看出是背包问题，不容易，跟FB一面 paint house很像，比那个难一点

定义res[i][j] 表示前 i个number with 最后一个number是j，这样的minimum adjusting cost

如果第i-1个数是j, 那么第i-2个数只能在[lowerRange, UpperRange]之间，lowerRange=Math.max(0, j-target), upperRange=Math.min(99, j+target),

这样的话，transfer function可以写成：

    for (int p=lowerRange; p<= upperRange; p++) {
    　　res[i][j] = Math.min(res[i][j], res[i-1][p] + Math.abs(j-A.get(i-1)));
    }

```java
public class Solution {
    /**
     * @param A: An integer array.
     * @param target: An integer.
     */
    public int MinAdjustmentCost(ArrayList<Integer> A, int target) {
        int[][] res = new int[A.size()+1][100];
        for (int j=0; j<=99; j++) {
            res[0][j] = 0;
        }
        for (int i=1; i<=A.size(); i++) {
            for (int j=0; j<=99; j++) {
                res[i][j] = Integer.MAX_VALUE;
                int lowerRange = Math.max(0, j-target);
                int upperRange = Math.min(99, j+target);
                for (int p=lowerRange; p<=upperRange; p++) {
                    res[i][j] = Math.min(res[i][j], res[i-1][p]+Math.abs(j-A.get(i-1)));
                }
            }
        }
        int result = Integer.MAX_VALUE;
        for (int j=0; j<=99; j++) {
            result = Math.min(result, res[A.size()][j]);
        }
        return result;
    }
}

```

---

## @@ 找出有向图中的弱联通分量

请找出有向图中弱联通分量的数目。图中的每个节点包含其邻居的 1 个标签和1 个列表。 （一个有向图中的相连节点指的是一个包含 2 个通过直接边沿路径相连的顶点的子图。）

样例

给定图:

    A----->B  C
     \     |  |
      \    |  |
       \   |  |
        \  v  v
         ->D  E <- F

返回 {A,B,D}, {C,E,F}. 图中有 2 个相连要素，即{A,B,D} 和 {C,E,F} 。

挑战

将原素升序排列。

**题解**

Union Find

```java
/**
 * Definition for Directed graph.
 * class DirectedGraphNode {
 *     int label;
 *     ArrayList<DirectedGraphNode> neighbors;
 *     DirectedGraphNode(int x) { label = x; neighbors = new ArrayList<DirectedGraphNode>(); }
 * };
 */
public class Solution {
    /**
     * @param nodes a array of Directed graph node
     * @return a connected set of a directed graph
     */
    public List<List<Integer>> connectedSet2(ArrayList<DirectedGraphNode> nodes) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        for(DirectedGraphNode node : nodes){
            for(DirectedGraphNode n : node.neighbors){
                int fa = find(map, node.label);
                int ch = find(map, n.label);
                map.put(fa, ch);
            }
        }
        HashMap<Integer, ArrayList<Integer>> record = new HashMap<Integer, ArrayList<Integer>>();

        for(DirectedGraphNode node : nodes){
            int val = find(map, node.label);
            if(!record.containsKey(val)){
                record.put(val, new ArrayList<Integer>());
            }
            record.get(val).add(node.label);
        }

        for(int key : record.keySet()){
            ArrayList<Integer> sub = new ArrayList<Integer>();
            sub.addAll(record.get(key));
            res.add(sub);
        }
        return res;

    }

    private int find(HashMap<Integer, Integer> map, int v){
        if(!map.containsKey(v)){
            map.put(v, v);
            return v;
        }
        while(map.get(v) != v) v = map.get(v);
        return v;
    }
}

```

---

## @@ 加油站

在一条环路上有 N 个加油站，其中第 i 个加油站有汽油gas[i]，并且从第 i 个加油站前往第 i+1个加油站需要消耗汽油cost[i]。

你有一辆油箱容量无限大的汽车，现在要从某一个加油站出发绕环路一周，一开始油箱为空。

求可环绕环路一周时出发的加油站的编号，若不存在环绕一周的方案，则返回-1。

样例

现在有4个加油站，汽油量gas[i]=[1, 1, 3, 1]，环路旅行时消耗的汽油量cost[i]=[2, 2, 1, 1]。则出发的加油站的编号为2。

注意

数据保证答案唯一。

挑战

O(n)时间和O(1)额外空间

**题解**

1. 从i开始，j是当前station的指针，sum += gas[j] – cost[j] （从j站加了油，再算上从i开始走到j剩的油，走到j+1站还能剩下多少油）
2. 如果sum < 0，说明从i开始是不行的。那能不能从i..j中间的某个位置开始呢？既然i出发到i+1是可行的， 又i~j是不可行的， 从而发现i+1~ j是不可行的。
3. 以此类推i+2~j， i+3~j，i+4~j 。。。。等等都是不可行的
4. 所以一旦sum<0，index就赋成j + 1，sum归零。
5. 最后total表示能不能走一圈。

以上做法，其实是贪心的思想：

也就是说brute force的解是 ： 一个一个来考虑， 每一个绕一圈， 但是 实际上 我们发现 i - j不可行 直接index就跳到j+1， 这样周而复始，很快就是绕一圈 就得到解了。

```java
public class Solution {
    /**
     * @param gas: an array of integers
     * @param cost: an array of integers
     * @return: an integer
     */
    public int canCompleteCircuit(int[] gas, int[] cost) {
        if (gas == null || cost == null || gas.length == 0 || cost.length == 0) {
            // Bug 0: should not return false;
            return -1;
        }

        int total = 0;
        int sum = 0;

        int startIndex = 0;

        int len = gas.length;
        for (int i = 0; i < len; i++) {
            int dif = gas[i] - cost[i];
            sum += dif;

            if (sum < 0) {
                // Means that from 0 to this gas station, none of them can be the solution.
                startIndex = i + 1; // Begin from the next station.
                sum = 0; // reset the sum.
            }

            total += dif;
        }

        if (total < 0) {
            return -1;
        }

        return startIndex;
    }
}

```

---

## @@ 克隆图

克隆一张无向图，图中的每个节点包含一个label和一个列表neighbors

LintCode Online Judge的无向图序列化：

图节点有唯一的label。

使用#作为一个分隔符，分隔节点的label和每个相邻节点neighbors。比如，序列化图{0,1,2#1,2#2,2}共有三个节点,因此包含两个个分隔符#。

1. 第一个节点label为0，存在边从节点0链接到节点1和节点2
2. 第二个节点label为1，存在边从节点1连接到节点2
3. 第三个节点label为2，存在边从节点2连接到节点2(本身),从而形成自环。

我们能看到如下的图：

       1
      / \
     /   \
    0 --- 2
         / \
         \_/

**题解**

使用BFS来解决此问题。用一个Queue来记录遍历的节点，遍历原图，并且把复制过的节点与原节点放在MAP中防止重复访问。

图的遍历有两种方式，BFS和DFS

这里使用BFS来解本题，BFS需要使用queue来保存neighbors

但这里有个问题，在clone一个节点时我们需要clone它的neighbors，而邻居节点有的已经存在，有的未存在，如何进行区分？

这里我们使用Map来进行区分，Map的key值为原来的node，value为新clone的node，当发现一个node未在map中时说明这个node还未被clone，

将它clone后放入queue中处理neighbors。

使用Map的主要意义在于充当BFS中Visited数组，它也可以去环问题，例如A--B有条边，当处理完A的邻居node，然后处理B节点邻居node时发现A已经处理过了

处理就结束，不会出现死循环。

queue中放置的节点都是未处理neighbors的节点。

```java
/**
 * Definition for undirected graph.
 * class UndirectedGraphNode {
 *     int label;
 *     ArrayList<UndirectedGraphNode> neighbors;
 *     UndirectedGraphNode(int x) { label = x; neighbors = new ArrayList<UndirectedGraphNode>(); }
 * };
 */
public class Solution {
    /**
     * @param node: A undirected graph node
     * @return: A undirected graph node
     */
    public UndirectedGraphNode cloneGraph(UndirectedGraphNode node) {
        if (node == null) {
            return null;
        }

        UndirectedGraphNode root = null;

        // store the nodes which are cloned.
        HashMap<UndirectedGraphNode, UndirectedGraphNode> map =
            new HashMap<UndirectedGraphNode, UndirectedGraphNode>();

        Queue<UndirectedGraphNode> q = new LinkedList<UndirectedGraphNode>();

        q.offer(node);
        UndirectedGraphNode rootCopy = new UndirectedGraphNode(node.label);

        // 别忘记这一行啊。orz..
        map.put(node, rootCopy);

        // BFS the graph.
        while (!q.isEmpty()) {
            UndirectedGraphNode cur = q.poll();
            UndirectedGraphNode curCopy = map.get(cur);

            // bfs all the childern node.
            for (UndirectedGraphNode child: cur.neighbors) {
                // the node has already been copied. Just connect it and don't need to copy.
                if (map.containsKey(child)) {
                    curCopy.neighbors.add(map.get(child));
                    continue;
                }

                // put all the children into the queue.
                q.offer(child);

                // create a new child and add it to the parent.
                UndirectedGraphNode childCopy = new UndirectedGraphNode(child.label);
                curCopy.neighbors.add(childCopy);

                // Link the new node to the old map.
                map.put(child, childCopy);
            }
        }

        return rootCopy;
    }
}

```

---

## @@ 堆化

给出一个整数数组，堆化操作就是把它变成一个最小堆数组。

对于堆数组A，A[0]是堆的根，并对于每个A[i]，A [i * 2 + 1]是A[i]的左儿子并且A[i * 2 + 2]是A[i]的右儿子。

样例

给出 [3,2,1,4,5]，返回[1,2,3,4,5] 或者任何一个合法的堆数组

挑战

O(n)的时间复杂度完成堆化

说明

什么是堆？

+ 堆是一种数据结构，它通常有三种方法：push， pop 和 top。其中，“push”添加新的元素进入堆，“pop”删除堆中最小/最大元素，“top”返回堆中最小/最大元素。

什么是堆化？

+ 把一个无序整数数组变成一个堆数组。如果是最小堆，每个元素A[i]，我们将得到A[i * 2 + 1] >= A[i]和A[i  * 2 + 2] >= A[i]

如果有很多种堆化的结果？

+ 返回其中任何一个。

**题解**

Heapify的基本思路就是：Given an array of N values, a heap containing those values can be built by simply “sifting” each internal node down to its proper location：

1. start with the last internal node
2. swap the current internal node with its smaller child, if necessary
3. then follow the swapped node down
4. continue until all internal nodes are done

```java
public class Solution {
    /**
     * @param A: Given an integer array
     * @return: void
     */
    public void heapify(int[] A) {
        int start = A.length/2;
        for (int i=start;i>=0;i--)
            shiftDown(i, A);
    }

    private void shiftDown(int ind, int[] A){
        int size = A.length;
        int left = ind*2+1;
        int right = ind*2+2;
        while (left<size || right<size){
            int leftVal = (left<size) ? A[left] : Integer.MAX_VALUE;
            int rightVal = (right<size) ? A[right] : Integer.MAX_VALUE;
            int next = (leftVal<=rightVal) ? left : right;
            if (A[ind]<A[next]) break;
            else {
                swap(A, ind,next);
                ind = next;
                left = ind*2+1;
                right = ind*2+2;
            }
        }
    }

    private void swap(int[] A, int x, int y){
        int temp = A[x];
        A[x] = A[y];
        A[y] = temp;
    }
}

```

---

## @@ 重哈希

哈希表容量的大小在一开始是不确定的。如果哈希表存储的元素太多（如超过容量的十分之一），我们应该将哈希表容量扩大一倍，并将所有的哈希值重新安排。假设你有如下一哈希表：

size=3, capacity=4

    [null, 21, 14, null]
           ↓    ↓
           9   null
           ↓
          null

哈希函数为：

    int hashcode(int key, int capacity) {
        return key % capacity;
    }

这里有三个数字9，14，21，其中21和9共享同一个位置因为它们有相同的哈希值1(21 % 4 = 9 % 4 = 1)。我们将它们存储在同一个链表中。

重建哈希表，将容量扩大一倍，我们将会得到：

size=3, capacity=8

    index:   0    1    2    3     4    5    6   7
    hash : [null, 9, null, null, null, 21, 14, null]

给定一个哈希表，返回重哈希后的哈希表。

样例

给出 [null, 21->9->null, 14->null, null]

返回 [null, 9->null, null, null, null, 21->null, 14->null, null]

注意
哈希表中负整数的下标位置可以通过下列方式计算：

+ C++/Java：如果你直接计算-4 % 3，你会得到-1，你可以应用函数：a % b = (a % b + b) % b得到一个非负整数。
+ Python：你可以直接用-1 % 3，你可以自动得到2。

**题解**

```java
/**
 * Definition for ListNode
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    /**
     * @param hashTable: A list of The first node of linked list
     * @return: A list of The first node of linked list which have twice size
     */
    public ListNode[] rehashing(ListNode[] hashTable) {
        int size = hashTable.length;
        if (size==0) return null;
        int newSize = 2*size;
        ListNode[] newTable = new ListNode[newSize];
        Arrays.fill(newTable,null);

        for (int i=0;i<size;i++){
            ListNode cur = hashTable[i];
            while (cur!=null){
                ListNode temp = cur;
                cur = cur.next;
                //Calculate the new position for temp.
                int val = (temp.val % newSize + newSize) % newSize;
                if (newTable[val]==null){
                    newTable[val]=temp;
                    temp.next = null;
                } else {
                    ListNode p = newTable[val];
                    while (p.next!=null) p = p.next;
                    p.next = temp;
                    temp.next = null;
                }
            }
        }

        return newTable;
    }
};


```

---

## @@ 拓扑排序

给定一个有向图，图节点的拓扑排序被定义为：

+ 对于每条有向边A--> B，则A必须排在B之前　　
+ 拓扑排序的第一个节点可以是任何在图中没有其他节点指向它的节点　　

找到给定图的任一拓扑排序

挑战

能否分别用BFS和DFS完成？

**题解**

A basica method is recording the pre nodes of every node, then find out a node without pre node in each iteration and delete this node from unvisited set.

DFS: use a recursive method, randomly pick up an unmakred node, before adding it into result list, recursively visite all its neighbors and add its neighbors into list first. In this way, we guarantee that all the nodes belong to some node's post nodes will be added to the result list first.

Thoughts:

1. For each node in the graph, construct a map with node as key, and number of parent nodes as value
2. Looping through left nodes and see if its indegree is 0: if so, remove the node from graph and add it to result; also its neighbors indegree--

A problem while implementing #2 is ConcurrentModificatoinException that I tried to remove the node from map while looping through it. A work around is looping through remaining nodes from graph and remove it from graph directly. Entries in map are never removed.

```java
/**
 * Definition for Directed graph.
 * class DirectedGraphNode {
 *     int label;
 *     ArrayList<DirectedGraphNode> neighbors;
 *     DirectedGraphNode(int x) { label = x; neighbors = new ArrayList<DirectedGraphNode>(); }
 * };
 */
public class Solution {
    /**
     * @param graph: A list of Directed graph node
     * @return: Any topological order for the given graph.
     */
    public ArrayList<DirectedGraphNode> topSort(ArrayList<DirectedGraphNode> graph) {
        ArrayList<DirectedGraphNode> res = new ArrayList<DirectedGraphNode>();
        if (graph.size()==0) return res;

        //Construct hash map.
        Map<DirectedGraphNode, Set<DirectedGraphNode>> map = new HashMap<DirectedGraphNode, Set<DirectedGraphNode>>();
        for (DirectedGraphNode node: graph){
            Set<DirectedGraphNode> set = new HashSet<DirectedGraphNode>();
            map.put(node,set);
        }
        for (DirectedGraphNode node : graph)
            for (DirectedGraphNode temp: node.neighbors)
                map.get(temp).add(node);

        //Construct topological order sequence.
        int len = graph.size();
        while (graph.size()>0) {
            int index = 0;
            while (index<graph.size()){
                DirectedGraphNode node = graph.get(index);
                if (map.get(node).size()==0){
                    graph.remove(node);
                    res.add(node);
                    for (DirectedGraphNode temp: graph)
                        if (map.get(temp).contains(node))
                            map.get(temp).remove(node);
                } else index++;
            }
        }
        return res;
    }
}

```

---

## @@ 背包问题 II

给出n个物品的体积A[i]和其价值V[i]，将他们装入一个大小为m的背包，最多能装入的总价值有多大？

样例

对于物品体积[2, 3, 5, 7]和对应的价值[1, 5, 2, 4], 假设背包大小为10的话，最大能够装入的价值为9。

注意

A[i], V[i], n, m均为整数。你不能将物品进行切分。你所挑选的物品总体积需要小于等于给定的m。

**题解**

这道题还是跟Backpack有大不一样之处

用子问题定义状态：即f[i][v]表示前 i 件物品恰放入一个容量为 j 的背包可以获得的最大价值。则其状态转移方程便是：

f[i][j] = max{f[i-1][j], j>=A[i-1]? f[i-1][j-A[i-1]]+V[i-1] : 0}

```java
public class Solution {
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A & V: Given n items with size A[i] and value V[i]
     * @return: The maximum value
     */
    public int backPackII(int m, int[] A, int V[]) {
        int[][] res = new int[A.length+1][m+1];
        res[0][0] = 0;
        for (int i=1; i<=A.length; i++) {
            for (int j=0; j<=m; j++) {
                if (j - A[i-1] < 0)
                    res[i][j] = res[i-1][j];
                if (j - A[i-1] >= 0) {
                    res[i][j] = Math.max(res[i-1][j], res[i-1][j-A[i-1]]+V[i-1]);
                }
            }
        }

        return res[A.length][m];
    }
}

```

---

## @@ 最长连续序列

给定一个未排序的整数数组，找出最长连续序列的长度。

样例

给出数组[100, 4, 200, 1, 3, 2]，这个最长的连续序列是 [1, 2, 3, 4]，返回所求长度 4

说明

要求你的算法复杂度为O(n)

**题解**

我们可以把所有的数字放在hashset中，来一个数字后，取出HashSet中的某一元素x，找x-1,x-2....x+1,x+2...是否也在set里。

```java
public class Solution {
    /**
     * @param nums: A list of integers
     * @return an integer
     */
    public int longestConsecutive(int[] num) {
        if (num == null) {
            return 0;
        }

        HashSet<Integer> set = new HashSet<Integer>();
        for (int i: num) {
            set.add(i);
        }

        int max = 0;
        for (int i: num) {
            int cnt = 1;
            set.remove(i);

            int tmp = i - 1;
            while (set.contains(tmp)) {
                set.remove(tmp);
                cnt++;
                tmp--;
            }

            tmp = i + 1;
            while (set.contains(tmp)) {
                set.remove(tmp);
                cnt++;
                tmp++;
            }

            max = Math.max(max, cnt);
        }

        return max;
    }
}

```

---

## @@ 单词搜索

给出一个二维的字母板和一个单词，寻找字母板网格中是否存在这个单词。

单词可以由按顺序的相邻单元的字母组成，其中相邻单元指的是水平或者垂直方向相邻。每个单元中的字母最多只能使用一次。

样例
给出board =

    [
      "ABCE",
      "SFCS",
      "ADEE"
    ]

word = "ABCCED"， ->返回 true,

word = "SEE"，-> 返回 true,

word = "ABCB"， -> 返回 false.

**题解**

1. Locate the first char and start the recursive search
2. Backtracking. Set and unset the visited flag.

```java
public class Solution {
    /**
     * @param board: A list of lists of character
     * @param word: A string
     * @return: A boolean
     */
    public boolean exist(char[][] board, String word) {
        if (board==null || board.length==0) return false;
        boolean visited[][] = new boolean[board.length][board[0].length];
        for (int i=0; i < board.length; i++){
            for (int j=0; j < board[0].length; j++){
                if (search(word, 0, board, i, j, visited)) {
                    return true;
                }
            }
        }
        return false;
    }

    public boolean search(String word, int index, char[][] board, int i, int j, boolean[][] visited){
        if (i<0 || j<0 || i==board.length || j==board[0].length || visited[i][j]==true) return false;
        visited[i][j] = true;
        boolean result = false;
        if (board[i][j]==word.charAt(index)){
            if (index == word.length()-1) return true;
            //save the result here instead of just return the result, as we need to unset the visited matrix before return
            result = search(word, index+1, board, i-1, j, visited) ||
                            search(word, index+1, board, i+1, j, visited) ||
                            search(word, index+1, board, i, j-1, visited) ||
                            search(word, index+1, board, i, j+1, visited);
        }
        visited[i][j] = false;
        return result;
    }
}

```

---


## ---- 未做完 ----


## @ 统计比给定整数小的数的个数

给定一个整数数组 （下标由 0 到 n-1，其中 n 表示数组的规模，数值范围由 0 到 10000），以及一个 查询列表。对于每一个查询，将会给你一个整数，请你返回该数组中小于给定整数的元素的数量。

样例

对于数组 [1,2,7,8,5] ，查询 [1,8,5]，返回 [0,4,2]

注意

在做此题前，最好先完成 线段树的构造 and 线段树查询 II 这两道题目。

挑战

可否用一下三种方法完成以上题目。

1. 仅用循环方法
2. 分类搜索 和 二进制搜索
3. 构建 线段树 和 搜索

**题解**

```java


```

---


## @ 区间最小数

给定一个整数数组（下标由 0 到 n-1，其中 n 表示数组的规模），以及一个查询列表。每一个查询列表有两个整数 [start, end]。 对于每个查询，计算出数组中从下标 start 到 end 之间的数的最小值，并返回在结果列表中。

样例

对于数组 [1,2,7,8,5]， 查询 [(1,2),(0,4),(2,4)]，返回 [2,1,5]

注意

在做此题前，建议先完成以下三道题 线段树的构造， 线段树的查询 及 线段树的修改。

挑战

每次查询在O(logN)的时间内完成

**题解**

```java

```

---


## @ 连续子数组求和 II

给定一个整数数组，请找出一个连续的旋转子数组，使得该子数组的和最大。输出答案时，请分别返回第一个数字和最后一个数字的序号。（如果两个相同的答案，请返回其中任意一个）

样例

给定 [3, 1, -100, -3, 4], 返回 [4,1].

**题解**

使用一个Stack就可以完成计算，非常简单。只需要从左往右结合，每遇到一个运算符号，就将前面两个数字弹出并且计算，然后再push回去。

全部计算完成后，再将结果弹出即可。

```java
public class Solution {
    /**
     * @param A an integer array
     * @return  A list of integers includes the index of the first number and the index of the last number
     */
    public ArrayList<Integer> continuousSubarraySumII(int[] A) {
        Pair regular = continuousSubarraySum(A);
        int maxWrap = 0;

        for(int i = 0; i < A.length; i++){
            maxWrap += A[i];
            A[i] = -A[i];
        }
        Pair wrap = continuousSubarraySum(A);
        maxWrap = maxWrap + wrap.maxValue;
        ArrayList<Integer> temp = new ArrayList<Integer>();
        temp.add(wrap.idxs.get(1) + 1);
        temp.add(wrap.idxs.get(0) - 1);
        return maxWrap > regular.maxValue ?  temp : regular.idxs;


    }


    private Pair continuousSubarraySum(int[] A) {
        // Write your code here

        int curSum = A[0], maxSum = Integer.MIN_VALUE;
        int start = 0, end = 0;
        ArrayList<Integer> res = new ArrayList<Integer>();
        res.add(0);
        res.add(0);
        for(int i = 1; i < A.length; i++){
            if(maxSum < curSum){
                res.set(0, start);
                res.set(1, i-1);
                maxSum = curSum;
            }
            if(curSum < 0){
                curSum = 0;
                start = i;
                end = i;
            }
            curSum += A[i];

        }

        if(maxSum < curSum){
            res.set(0, start);
            res.set(1, A.length - 1);
        }
        return new Pair(maxSum, res);
    }

    class Pair{
        int maxValue;
        ArrayList<Integer> idxs;
        public Pair(int maxValue, ArrayList<Integer> idxs){
            this.maxValue = maxValue;
            this.idxs = idxs;

        }
    }
}


```

---

## @ nuts 和 bolts 的问题

给定一组 n 个不同大小的 nuts 和 n 个不同大小的 bolts。nuts 和 bolts 一一匹配。 不允许将 nut 之间互相比较，也不允许将 bolt 之间互相比较。也就是说，只许将 nut 与 bolt 进行比较， 或将 bolt 与 nut 进行比较。请比较 nut 与 bolt 的大小。

样例

Nuts 用一个整数数组表示 nuts [] = {1, 5, 8, 2}. Bolts 也用一个整数数组表示 bolts[] = {3, 6, 7, 9}. 我们将提供一个比较函数，以比较 nut 与 bolt 的大小。 将 nuts 进行升序排序，使得 nuts 与 bolts 位置对等。

**题解**

```java

```

---


## ---- 困难题 ----


