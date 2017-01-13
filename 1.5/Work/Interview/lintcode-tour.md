# LintCode 思路及个人想法

用 python 来进行解答

<!-- MarkdownTOC -->

- @ 要注意的知识点
- ---- 容易题 ----
- @ O(1)检测2的幂次
- @ x的平方根
- @ 不同的路径
- @ 不同的路径 II
- @ 两个字符串是变位词
- @ 两个链表的和
- @ 中位数
- @ 主元素
- @ 二分查找
- @ 二叉树的中序遍历
- @ 二叉树的前序遍历
- @ 二叉树的后序遍历
- @ 二叉树的最大深度
- @ 二叉树的最小深度
- @ 二进制中有多少个1
- @ 二进制求和
- @ 删除元素
- @ 删除排序数组中的重复数字
- @ 删除排序数组中的重复数字 II
- @ 删除排序链表中的重复元素
- @ 删除链表中倒数第n个节点
- @ 判断字符串是否没有重复字符
- @ 合并排序数组
- @ 合并排序数组 II
- @ 合并两个排序链表
- @ 合并区间
- @ 加一
- @ 哈希函数
- @ 颠倒整数
- @ 空格替换
- @ 斐波纳契数列
- @ 搜索二维矩阵
- @ 报数
- @ 恢复旋转排序数组
- @ 尾部的零
- @ 在O(1)时间复杂度删除链表节点
- @ 链表插入排序
- @ 链表划分
- @ 链表倒数第n个节点
- @ 翻转链表
- @ 翻转字符串
- @ 矩阵的之字型遍历
- @ 爬楼梯
- @ 比较字符串
- @ 有效的括号序列
- @ 最后一个单词的长度
- @ 旋转字符串
- @ 翻转二叉树
- @ 最长单词
- @ 落单的数
- @ 单例
- @ 奇偶分割数组
- @ 字符串查找
- @ 子数组之和(为零)
- @ 子数组之和(为 K)
- @ 最接近零的子数组和
- @ 数组剔除元素后的乘积
- ---- 未做完 ----
- @ 将整数A转换为B
- @ 排列序号
- @ 判断数独是否合法
- @ 分割回文串
- ---- 中等题 ----
- @ 最长公共子串
- ---- 困难题 ----

<!-- /MarkdownTOC -->

## @ 要注意的知识点

- lambda 表达式
- xrange
- 递归

## ---- 容易题 ----

这一部分是容易题

## @ O(1)检测2的幂次

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

## @ x的平方根

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

## @ 不同的路径

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

## @ 不同的路径 II

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

## @ 两个字符串是变位词

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

## @ 两个链表的和

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

## @ 中位数

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

## @ 主元素

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

## @ 二分查找

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

## @ 二叉树的中序遍历

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

## @ 二叉树的前序遍历

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

## @ 二叉树的后序遍历

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

## @ 二叉树的最大深度

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


## @ 二叉树的最小深度

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

## @ 二进制中有多少个1

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

## @ 二进制求和

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

## @ 删除元素

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

## @ 删除排序数组中的重复数字

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

## @ 删除排序数组中的重复数字 II

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

## @ 删除排序链表中的重复元素

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

## @ 删除链表中倒数第n个节点

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

## @ 判断字符串是否没有重复字符

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

## @ 合并排序数组

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

## @ 合并排序数组 II

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


## @ 合并两个排序链表

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

## @ 合并区间

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


## @ 加一

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


## @ 哈希函数

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

## @ 颠倒整数

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

## @ 空格替换

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

## @ 斐波纳契数列

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

## @ 搜索二维矩阵

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

## @ 报数

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

## @ 恢复旋转排序数组

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

## @ 尾部的零

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

## @ 在O(1)时间复杂度删除链表节点

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

## @ 链表插入排序

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

## @ 链表划分

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

## @ 链表倒数第n个节点

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

## @ 翻转链表

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

## @ 翻转字符串

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

## @ 矩阵的之字型遍历

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

## @ 爬楼梯

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

## @ 比较字符串

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

## @ 有效的括号序列

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

## @ 最后一个单词的长度

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

## @ 旋转字符串

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

## @ 翻转二叉树

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

## @ 最长单词

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

## @ 落单的数

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

## @ 单例

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

## @ 奇偶分割数组

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

## @ 字符串查找

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

## @ 子数组之和(为零)

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

## @ 子数组之和(为 K)

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

## @ 最接近零的子数组和

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

## @ 数组剔除元素后的乘积

给定一个整数数组A。

定义B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]， 计算B的时候请不要使用除法。

样例

    给出A=[1, 2, 3]，返回 B为[6, 3, 2]

**题解**

左右分治法

完全可以在最终返回结果result基础上原地计算左右两半部分的积。

```python

```

---


## ---- 未做完 ----




## @ 将整数A转换为B

如果要将整数A转换为B，需要改变多少个bit位？

样例

    如把31转换为14，需要改变2个bit位。
    (31)10=(11111)2
    (14)10=(01110)2

挑战

    你能想出几种方法？

**题解**



```python

```

---

## @ 排列序号

给出一个不含重复数字的排列，求这些数字的所有排列按字典序排序后该排列的编号。其中，编号从1开始。

样例

    例如，排列[1,2,4]是第1个排列。

**题解**



```python

```

---




## @ 判断数独是否合法

请判定一个数独是否有效。

该数独可能只填充了部分数字，其中缺少的数字用 . 表示。

注意

    一个合法的数独（仅部分填充）并不一定是可解的。我们仅需使填充的空格有效即可。

说明 什么是数独？

+ [英文版](http://sudoku.com.au/TheRules.aspx)
+ [中文版](http://baike.baidu.com/subview/961/10842669.htm)

**题解**



```python

```

---

## @ 分割回文串

给定一个字符串s，将s分割成一些子串，使每个子串都是回文串。

返回s所有可能的回文串分割方案。

样例

    给出 s = "aab"，返回

    [
     ["aa","b"],
     ["a","a","b"]
    ]

**题解**



```python

```

---


## ---- 中等题 ----

## @ 最长公共子串

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


## ---- 困难题 ----
