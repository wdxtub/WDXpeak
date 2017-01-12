# Python Tips

## 字典推导(Dictionary comprehensions)和集合推导(Set comprehensions)

大多数的Python程序员都知道且使用过列表推导(list comprehensions)。如果你对list comprehensions概念不是很熟悉——一个list comprehension就是一个更简短、简洁的创建一个list的方法。

```python
>>> some_list = [1, 2, 3, 4, 5]

>>> another_list = [ x + 1 for x in some_list ]

>>> another_list
[2, 3, 4, 5, 6]
```

自从python 3.1 (甚至是Python 2.7)起，我们可以用同样的语法来创建集合和字典表：

```python
>>> # Set Comprehensions
>>> some_list = [1, 2, 3, 4, 5, 2, 5, 1, 4, 8]

>>> even_set = { x for x in some_list if x % 2 == 0 }

>>> even_set
set([8, 2, 4])

>>> # Dict Comprehensions

>>> d = { x: x % 2 == 0 for x in range(1, 11) }

>>> d
{1: False, 2: True, 3: False, 4: True, 5: False, 6: True, 7: False, 8: True, 9: False, 10: True}
```

在第一个例子里，我们以some_list为基础，创建了一个具有不重复元素的集合，而且集合里只包含偶数。而在字典表的例子里，我们创建了一个key是不重复的1到10之间的整数，value是布尔型，用来指示key是否是偶数。

这里另外一个值得注意的事情是集合的字面量表示法。我们可以简单的用这种方法创建一个集合：

```python
>>> my_set = {1, 2, 1, 2, 3, 4}

>>> my_set
set([1, 2, 3, 4])
```

而不需要使用内置函数set()。

## 计数时使用Counter计数对象。

这听起来显而易见，但经常被人忘记。对于大多数程序员来说，数一个东西是一项很常见的任务，而且在大多数情况下并不是很有挑战性的事情——这里有几种方法能更简单的完成这种任务。

Python的collections类库里有个内置的dict类的子类，是专门来干这种事情的：

```python
>>> from collections import Counter
>>> c = Counter('hello world')

>>> c
Counter({'l': 3, 'o': 2, ' ': 1, 'e': 1, 'd': 1, 'h': 1, 'r': 1, 'w': 1})

>>> c.most_common(2)
[('l', 3), ('o', 2)]
```

## 漂亮的打印出JSON

JSON是一种非常好的数据序列化的形式，被如今的各种API和web service大量的使用。使用python内置的json处理，可以使JSON串具有一定的可读性，但当遇到大型数据时，它表现成一个很长的、连续的一行时，人的肉眼就很难观看了。

为了能让JSON数据表现的更友好，我们可以使用indent参数来输出漂亮的JSON。当在控制台交互式编程或做日志时，这尤其有用：

```python
>>> import json

>>> print(json.dumps(data))  # No indention
{"status": "OK", "count": 2, "results": [{"age": 27, "name": "Oz", "lactose_intolerant": true}, {"age": 29, "name": "Joe", "lactose_intolerant": false}]}

>>> print(json.dumps(data, indent=2))  # With indention

{
  "status": "OK",
  "count": 2,
  "results": [

    {
      "age": 27,
      "name": "Oz",

      "lactose_intolerant": true
    },
    {
      "age": 29,

      "name": "Joe",
      "lactose_intolerant": false
    }
  ]

}
```

同样，使用内置的pprint模块，也可以让其它任何东西打印输出的更漂亮

## 拆箱

```python
>>> a, b, c = 1, 2, 3
>>> a, b, c
(1, 2, 3)
>>> a, b, c = [1, 2, 3]
>>> a, b, c
(1, 2, 3)
>>> a, b, c = (2 * i + 1 for i in range(3))
>>> a, b, c
(1, 3, 5)
>>> a, (b, c), d = [1, (2, 3), 4]
>>> a
1
>>> b
2
>>> c
3
>>> d
4
```

## 拆箱变量交换

```python
>>> a, b = 1, 2
>>> a, b = b, a
>>> a, b
(2, 1)
```

## 扩展拆箱（只兼容python3）

```python
>>> a, *b, c = [1, 2, 3, 4, 5]
>>> a
1
>>> b
[2, 3, 4]
>>> c
5
```

## 负数索引

```python
>>> a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a[-1]
10
>>> a[-3]
8
```

## 切割列表

```python
>>> a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a[2:8]
[2, 3, 4, 5, 6, 7]
```

## 负数索引切割列表

```python
>>> a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a[-4:-2]
[7, 8]
```

## 指定步长切割列表

```python
>>> a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a[::2]
[0, 2, 4, 6, 8, 10]
>>> a[::3]
[0, 3, 6, 9]
>>> a[2:8:2]
[2, 4, 6]
```

## 负数步长切割列表

```python
>>> a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a[::-1]
[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> a[::-2]
[10, 8, 6, 4, 2, 0]
```

## 列表切割赋值

```python
>>> a = [1, 2, 3, 4, 5]
>>> a[2:3] = [0, 0]
>>> a
[1, 2, 0, 0, 4, 5]
>>> a[1:1] = [8, 9]
>>> a
[1, 8, 9, 2, 0, 0, 4, 5]
>>> a[1:-1] = []
>>> a
[1, 5]
```

## 命名列表切割方式

```python
>>> a = [0, 1, 2, 3, 4, 5]
>>> LASTTHREE = slice(-3, None)
>>> LASTTHREE
slice(-3, None, None)
>>> a[LASTTHREE]
[3, 4, 5]
```

## 列表以及迭代器的压缩和解压缩

```python
>>> a = [1, 2, 3]
>>> b = ['a', 'b', 'c']
>>> z = zip(a, b)
>>> z
[(1, 'a'), (2, 'b'), (3, 'c')]
>>> zip(*z)
[(1, 2, 3), ('a', 'b', 'c')]
```

## 列表相邻元素压缩器

```python
>>> a = [1, 2, 3, 4, 5, 6]
>>> zip(*([iter(a)] * 2))
[(1, 2), (3, 4), (5, 6)]

>>> group_adjacent = lambda a, k: zip(*([iter(a)] * k))
>>> group_adjacent(a, 3)
[(1, 2, 3), (4, 5, 6)]
>>> group_adjacent(a, 2)
[(1, 2), (3, 4), (5, 6)]
>>> group_adjacent(a, 1)
[(1,), (2,), (3,), (4,), (5,), (6,)]

>>> zip(a[::2], a[1::2])
[(1, 2), (3, 4), (5, 6)]

>>> zip(a[::3], a[1::3], a[2::3])
[(1, 2, 3), (4, 5, 6)]

>>> group_adjacent = lambda a, k: zip(*(a[i::k] for i in range(k)))
>>> group_adjacent(a, 3)
[(1, 2, 3), (4, 5, 6)]
>>> group_adjacent(a, 2)
[(1, 2), (3, 4), (5, 6)]
>>> group_adjacent(a, 1)
[(1,), (2,), (3,), (4,), (5,), (6,)]
```

## 在列表中用压缩器和迭代器滑动取值窗口

```python
>>> def n_grams(a, n):
...     z = [iter(a[i:]) for i in range(n)]
...     return zip(*z)
...
>>> a = [1, 2, 3, 4, 5, 6]
>>> n_grams(a, 3)
[(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]
>>> n_grams(a, 2)
[(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
>>> n_grams(a, 4)
[(1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6)]
```

## 用压缩器反转字典

```python
>>> m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> m.items()
[('a', 1), ('c', 3), ('b', 2), ('d', 4)]
>>> zip(m.values(), m.keys())
[(1, 'a'), (3, 'c'), (2, 'b'), (4, 'd')]
>>> mi = dict(zip(m.values(), m.keys()))
>>> mi
{1: 'a', 2: 'b', 3: 'c', 4: 'd'}
```

## 列表展开

```python
>>> a = [[1, 2], [3, 4], [5, 6]]
>>> list(itertools.chain.from_iterable(a))
[1, 2, 3, 4, 5, 6]

>>> sum(a, [])
[1, 2, 3, 4, 5, 6]

>>> [x for l in a for x in l]
[1, 2, 3, 4, 5, 6]

>>> a = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
>>> [x for l1 in a for l2 in l1 for x in l2]
[1, 2, 3, 4, 5, 6, 7, 8]

>>> a = [1, 2, [3, 4], [[5, 6], [7, 8]]]
>>> flatten = lambda x: [y for l in x for y in flatten(l)] if type(x) is list else [x]
>>> flatten(a)
[1, 2, 3, 4, 5, 6, 7, 8]
```

## 生成器表达式

```python
>>> g = (x ** 2 for x in xrange(10))
>>> next(g)
0
>>> next(g)
1
>>> next(g)
4
>>> next(g)
9
>>> sum(x ** 3 for x in xrange(10))
2025
>>> sum(x ** 3 for x in xrange(10) if x % 3 == 1)
408
```

## 字典推导

```python
>>> m = {x: x ** 2 for x in range(5)}
>>> m
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

>>> m = {x: 'A' + str(x) for x in range(10)}
>>> m
{0: 'A0', 1: 'A1', 2: 'A2', 3: 'A3', 4: 'A4', 5: 'A5', 6: 'A6', 7: 'A7', 8: 'A8', 9: 'A9'}
```

## 用字典推导反转字典

```python
>>> m = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
>>> m
{'d': 4, 'a': 1, 'b': 2, 'c': 3}
>>> {v: k for k, v in m.items()}
{1: 'a', 2: 'b', 3: 'c', 4: 'd'}
```

## 命名元组

```python
>>> Point = collections.namedtuple('Point', ['x', 'y'])
>>> p = Point(x=1.0, y=2.0)
>>> p
Point(x=1.0, y=2.0)
>>> p.x
1.0
>>> p.y
2.0
```

## 继承命名元组

```python
>>> class Point(collections.namedtuple('PointBase', ['x', 'y'])):
...     __slots__ = ()
...     def __add__(self, other):
...             return Point(x=self.x + other.x, y=self.y + other.y)
...
>>> p = Point(x=1.0, y=2.0)
>>> q = Point(x=2.0, y=3.0)
>>> p + q
Point(x=3.0, y=5.0)
```

## 操作集合

```python
>>> A = {1, 2, 3, 3}
>>> A
set([1, 2, 3])
>>> B = {3, 4, 5, 6, 7}
>>> B
set([3, 4, 5, 6, 7])
>>> A | B
set([1, 2, 3, 4, 5, 6, 7])
>>> A & B
set([3])
>>> A - B
set([1, 2])
>>> B - A
set([4, 5, 6, 7])
>>> A ^ B
set([1, 2, 4, 5, 6, 7])
>>> (A ^ B) == ((A - B) | (B - A))
True
```

## 操作多重集合

```python
>>> A = collections.Counter([1, 2, 2])
>>> B = collections.Counter([2, 2, 3])
>>> A
Counter({2: 2, 1: 1})
>>> B
Counter({2: 2, 3: 1})
>>> A | B
Counter({2: 2, 1: 1, 3: 1})
>>> A & B
Counter({2: 2})
>>> A + B
Counter({2: 4, 1: 1, 3: 1})
>>> A - B
Counter({1: 1})
>>> B - A
Counter({3: 1})
```

## 统计在可迭代器中最常出现的元素

```python
>>> A = collections.Counter([1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7])
>>> A
Counter({3: 4, 1: 2, 2: 2, 4: 1, 5: 1, 6: 1, 7: 1})
>>> A.most_common(1)
[(3, 4)]
>>> A.most_common(3)
[(3, 4), (1, 2), (2, 2)]
```

## 两端都可操作的队列

```python
>>> Q = collections.deque()
>>> Q.append(1)
>>> Q.appendleft(2)
>>> Q.extend([3, 4])
>>> Q.extendleft([5, 6])
>>> Q
deque([6, 5, 2, 1, 3, 4])
>>> Q.pop()
4
>>> Q.popleft()
6
>>> Q
deque([5, 2, 1, 3])
>>> Q.rotate(3)
>>> Q
deque([2, 1, 3, 5])
>>> Q.rotate(-3)
>>> Q
deque([5, 2, 1, 3])
```

## 有最大长度的双端队列

```python
>>> last_three = collections.deque(maxlen=3)
>>> for i in xrange(10):
...     last_three.append(i)
...     print ', '.join(str(x) for x in last_three)
...
0
0, 1
0, 1, 2
1, 2, 3
2, 3, 4
3, 4, 5
4, 5, 6
5, 6, 7
6, 7, 8
7, 8, 9
```

## 可排序词典

```python
>>> m = dict((str(x), x) for x in range(10))
>>> print ', '.join(m.keys())
1, 0, 3, 2, 5, 4, 7, 6, 9, 8
>>> m = collections.OrderedDict((str(x), x) for x in range(10))
>>> print ', '.join(m.keys())
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
>>> m = collections.OrderedDict((str(x), x) for x in range(10, 0, -1))
>>> print ', '.join(m.keys())
10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

## 默认词典

```python
>>> m = dict()
>>> m['a']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'a'
>>>
>>> m = collections.defaultdict(int)
>>> m['a']
0
>>> m['b']
0
>>> m = collections.defaultdict(str)
>>> m['a']
''
>>> m['b'] += 'a'
>>> m['b']
'a'
>>> m = collections.defaultdict(lambda: '[default value]')
>>> m['a']
'[default value]'
>>> m['b']
'[default value]'
```

## 默认字典的简单树状表达

```python
>>> import json
>>> tree = lambda: collections.defaultdict(tree)
>>> root = tree()
>>> root['menu']['id'] = 'file'
>>> root['menu']['value'] = 'File'
>>> root['menu']['menuitems']['new']['value'] = 'New'
>>> root['menu']['menuitems']['new']['onclick'] = 'new();'
>>> root['menu']['menuitems']['open']['value'] = 'Open'
>>> root['menu']['menuitems']['open']['onclick'] = 'open();'
>>> root['menu']['menuitems']['close']['value'] = 'Close'
>>> root['menu']['menuitems']['close']['onclick'] = 'close();'
>>> print json.dumps(root, sort_keys=True, indent=4, separators=(',', ': '))
{
    "menu": {
        "id": "file",
        "menuitems": {
            "close": {
                "onclick": "close();",
                "value": "Close"
            },
            "new": {
                "onclick": "new();",
                "value": "New"
            },
            "open": {
                "onclick": "open();",
                "value": "Open"
            }
        },
        "value": "File"
    }
}
```

## 对象到唯一计数的映射

```python
>>> import itertools, collections
>>> value_to_numeric_map = collections.defaultdict(itertools.count().next)
>>> value_to_numeric_map['a']
0
>>> value_to_numeric_map['b']
1
>>> value_to_numeric_map['c']
2
>>> value_to_numeric_map['a']
0
>>> value_to_numeric_map['b']
1
```

## 最大和最小的几个列表元素

```python
>>> a = [random.randint(0, 100) for __ in xrange(100)]
>>> heapq.nsmallest(5, a)
[3, 3, 5, 6, 8]
>>> heapq.nlargest(5, a)
[100, 100, 99, 98, 98]
```

## 两个列表的笛卡尔积

```python
>>> for p in itertools.product([1, 2, 3], [4, 5]):
(1, 4)
(1, 5)
(2, 4)
(2, 5)
(3, 4)
(3, 5)
>>> for p in itertools.product([0, 1], repeat=4):
...     print ''.join(str(x) for x in p)
...
0000
0001
0010
0011
0100
0101
0110
0111
1000
1001
1010
1011
1100
1101
1110
1111
```

## 列表组合和列表元素替代组合

```python
>>> for c in itertools.combinations([1, 2, 3, 4, 5], 3):
...     print ''.join(str(x) for x in c)
...
123
124
125
134
135
145
234
235
245
345
>>> for c in itertools.combinations_with_replacement([1, 2, 3], 2):
...     print ''.join(str(x) for x in c)
...
11
12
13
22
23
33
```

## 列表元素排列组合

```python
>>> for p in itertools.permutations([1, 2, 3, 4]):
...     print ''.join(str(x) for x in p)
...
1234
1243
1324
1342
1423
1432
2134
2143
2314
2341
2413
2431
3124
3142
3214
3241
3412
3421
4123
4132
4213
4231
4312
4321
```

## 可链接迭代器

```python
>>> a = [1, 2, 3, 4]
>>> for p in itertools.chain(itertools.combinations(a, 2), itertools.combinations(a, 3)):
...     print p
...
(1, 2)
(1, 3)
(1, 4)
(2, 3)
(2, 4)
(3, 4)
(1, 2, 3)
(1, 2, 4)
(1, 3, 4)
(2, 3, 4)
>>> for subset in itertools.chain.from_iterable(itertools.combinations(a, n) for n in range(len(a) + 1))
...     print subset
...
()
(1,)
(2,)
(3,)
(4,)
(1, 2)
(1, 3)
(1, 4)
(2, 3)
(2, 4)
(3, 4)
(1, 2, 3)
(1, 2, 4)
(1, 3, 4)
(2, 3, 4)
(1, 2, 3, 4)
```

## 根据文件指定列类聚

```python
>>> import itertools
>>> with open('contactlenses.csv', 'r') as infile:
...     data = [line.strip().split(',') for line in infile]
...
>>> data = data[1:]
>>> def print_data(rows):
...     print '\n'.join('\t'.join('{: <16}'.format(s) for s in row) for row in rows)
...

>>> print_data(data)
young               myope                   no                      reduced                 none
young               myope                   no                      normal                  soft
young               myope                   yes                     reduced                 none
young               myope                   yes                     normal                  hard
young               hypermetrope            no                      reduced                 none
young               hypermetrope            no                      normal                  soft
young               hypermetrope            yes                     reduced                 none
young               hypermetrope            yes                     normal                  hard
pre-presbyopic      myope                   no                      reduced                 none
pre-presbyopic      myope                   no                      normal                  soft
pre-presbyopic      myope                   yes                     reduced                 none
pre-presbyopic      myope                   yes                     normal                  hard
pre-presbyopic      hypermetrope            no                      reduced                 none
pre-presbyopic      hypermetrope            no                      normal                  soft
pre-presbyopic      hypermetrope            yes                     reduced                 none
pre-presbyopic      hypermetrope            yes                     normal                  none
presbyopic          myope                   no                      reduced                 none
presbyopic          myope                   no                      normal                  none
presbyopic          myope                   yes                     reduced                 none
presbyopic          myope                   yes                     normal                  hard
presbyopic          hypermetrope            no                      reduced                 none
presbyopic          hypermetrope            no                      normal                  soft
presbyopic          hypermetrope            yes                     reduced                 none
presbyopic          hypermetrope            yes                     normal                  none

>>> data.sort(key=lambda r: r[-1])
>>> for value, group in itertools.groupby(data, lambda r: r[-1]):
...     print '-----------'
...     print 'Group: ' + value
...     print_data(group)
...
-----------
Group: hard
young               myope                   yes                     normal                  hard
young               hypermetrope            yes                     normal                  hard
pre-presbyopic      myope                   yes                     normal                  hard
presbyopic          myope                   yes                     normal                  hard
-----------
Group: none
young               myope                   no                      reduced                 none
young               myope                   yes                     reduced                 none
young               hypermetrope            no                      reduced                 none
young               hypermetrope            yes                     reduced                 none
pre-presbyopic      myope                   no                      reduced                 none
pre-presbyopic      myope                   yes                     reduced                 none
pre-presbyopic      hypermetrope            no                      reduced                 none
pre-presbyopic      hypermetrope            yes                     reduced                 none
pre-presbyopic      hypermetrope            yes                     normal                  none
presbyopic          myope                   no                      reduced                 none
presbyopic          myope                   no                      normal                  none
presbyopic          myope                   yes                     reduced                 none
presbyopic          hypermetrope            no                      reduced                 none
presbyopic          hypermetrope            yes                     reduced                 none
presbyopic          hypermetrope            yes                     normal                  none
-----------
Group: soft
young               myope                   no                      normal                  soft
young               hypermetrope            no                      normal                  soft
pre-presbyopic      myope                   no                      normal                  soft
pre-presbyopic      hypermetrope            no                      normal                  soft
presbyopic          hypermetrope            no                      normal   
```

## 正则表达式替换

目标: 将字符串line中的 overview.gif 替换成其他字符串

```python
>>> line = '<IMG ALIGN="middle" SRC=\'#\'" /span>
>>> mo=re.compile(r'(?<=SRC=)"([\w+\.]+)"',re.I)  

>>> mo.sub(r'"\1****"',line)  
'<IMG ALIGN="middle" SRC=\'#\'" /span>

>>> mo.sub(r'replace_str_\1',line)  
'<IMG ALIGN="middle" replace_str_overview.gif BORDER="0" ALT="">'< /span>

>>> mo.sub(r'"testetstset"',line)  
'<IMG ALIGN="middle" SRC=\'#\'" /span>
```

注意: 其中 \1 是匹配到的数据，可以通过这样的方式直接引用

## 遍历目录方法

在某些时候，我们需要遍历某个目录找出特定的文件列表，可以通过os.walk方法来遍历，非常方便

```python
import os
fileList = []
rootdir = "/data"
for root, subFolders, files in os.walk(rootdir):
if '.svn' in subFolders: subFolders.remove('.svn')  
# 排除特定目录
for file in files:
  if file.find(".t2t") != -1:
# 查找特定扩展名的文件
      file_dir_path = os.path.join(root,file)
      fileList.append(file_dir_path)  

print fileList
```

## 列表按列排序(list sort)

如果列表的每个元素都是一个元组(tuple),我们要根据元组的某列来排序的化，可参考如下方法

下面例子我们是根据元组的第2列和第3列数据来排序的,而且是倒序(reverse=True)

```python
>>> a = [('2011-03-17', '2.26', 6429600, '0.0'), ('2011-03-16', '2.26', 12036900, '-3.0'),
 ('2011-03-15', '2.33', 15615500,'-19.1')]
>>> print a[0][0]
2011-03-17
>>> b = sorted(a, key=lambda result: result[1],reverse=True)
>>> print b
[('2011-03-15', '2.33', 15615500, '-19.1'), ('2011-03-17', '2.26', 6429600, '0.0'),
('2011-03-16', '2.26', 12036900, '-3.0')]
>>> c = sorted(a, key=lambda result: result[2],reverse=True)
>>> print c
[('2011-03-15', '2.33', 15615500, '-19.1'), ('2011-03-16', '2.26', 12036900, '-3.0'),
('2011-03-17', '2.26', 6429600, '0.0')]
```

## 列表去重(list uniq)

有时候需要将list中重复的元素删除，就要使用如下方法

```python
>>> lst= [(1,'sss'),(2,'fsdf'),(1,'sss'),(3,'fd')]
>>> set(lst)
set([(2, 'fsdf'), (3, 'fd'), (1, 'sss')])
>>>
>>> lst = [1, 1, 3, 4, 4, 5, 6, 7, 6]
>>> set(lst)
set([1, 3, 4, 5, 6, 7])
```

## 字典排序(dict sort)

一般来说，我们都是根据字典的key来进行排序，但是我们如果想根据字典的value值来排序，就使用如下方法

```python
>>> from operator import itemgetter
>>> aa = {"a":"1","sss":"2","ffdf":'5',"ffff2":'3'}
>>> sort_aa = sorted(aa.items(),key=itemgetter(1))
>>> sort_aa
[('a', '1'), ('sss', '2'), ('ffff2', '3'), ('ffdf', '5')]
```

从上面的运行结果看到，按照字典的value值进行排序的

## 字典,列表,字符串互转

以下是生成数据库连接字符串,从字典转换到字符串

```python
>>> params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
>>> ["%s=%s" % (k, v) for k, v in params.items()]
['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
>>> ";".join(["%s=%s" % (k, v) for k, v in params.items()])
'server=mpilgrim;uid=sa;database=master;pwd=secret'
```

下面的例子 是将字符串转化为字典

```python
>>> a = 'server=mpilgrim;uid=sa;database=master;pwd=secret'
>>> aa = {}
>>> for i in a.split(';'):aa[i.split('=',1)[0]] = i.split('=',1)[1]
...
>>> aa
{'pwd': 'secret', 'database': 'master', 'uid': 'sa', 'server': 'mpilgrim'}
```

## 时间对象操作

将时间对象转换成字符串

```python
>>> import datetime
>>> datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
  '2011-01-20 14:05'
```

时间大小比较

```python
>>> import time
>>> t1 = time.strptime('2011-01-20 14:05',"%Y-%m-%d %H:%M")
>>> t2 = time.strptime('2011-01-20 16:05',"%Y-%m-%d %H:%M")
>>> t1 > t2
  False
>>> t1 < t2
  True
```

时间差值计算,计算8小时前的时间

```python
>>> datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
  '2011-01-20 15:02'
>>> (datetime.datetime.now() - datetime.timedelta(hours=8)).strftime("%Y-%m-%d %H:%M")
  '2011-01-20 07:03'
```

将字符串转换成时间对象

```python
>>> endtime=datetime.datetime.strptime('20100701',"%Y%m%d")
>>> type(endtime)
  <type 'datetime.datetime'>
>>> print endtime
  2010-07-01 00:00:00
```

将从 1970-01-01 00:00:00 UTC 到现在的秒数，格式化输出   

```python
>>> import time
>>> a = 1302153828
>>> time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(a))
  '2011-04-07 13:23:48'
```

## 命令行参数解析(getopt)

通常在编写一些日运维脚本时，需要根据不同的条件，输入不同的命令行选项来实现不同的功能 在Python中提供了getopt模块很好的实现了命令行参数的解析。请看如下程序:

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os,getopt
def usage():
print
'''''
Usage: analyse_stock.py [options...]
Options:
-e : Exchange Name
-c : User-Defined Category Name
-f : Read stock info from file and save to db
-d : delete from db by stock code
-n : stock name
-s : stock code
-h : this help info
test.py -s haha -n "HA Ha"
'''

try:
opts, args = getopt.getopt(sys.argv[1:],'he:c:f:d:n:s:')
except getopt.GetoptError:
usage()
sys.exit()
if len(opts) == 0:
usage()
sys.exit()  

for opt, arg in opts:
if opt in ('-h', '--help'):
  usage()
  sys.exit()
elif opt == '-d':
  print "del stock %s" % arg
elif opt == '-f':
  print "read file %s" % arg
elif opt == '-c':
  print "user-defined %s " % arg
elif opt == '-e':
  print "Exchange Name %s" % arg
elif opt == '-s':
  print "Stock code %s" % arg
elif opt == '-n':
  print "Stock name %s" % arg  

sys.exit()
```

## print 格式化输出

### 格式化输出字符串

截取字符串输出,下面例子将只输出字符串的前3个字母

```python
>>> str="abcdefg"
>>> print "%.3s" % str
  abc
```

按固定宽度输出，不足使用空格补全,下面例子输出宽度为10

```python
>>> str="abcdefg"
>>> print "%10s" % str
     abcdefg
```

截取字符串，按照固定宽度输出

```python
>>> str="abcdefg"
>>> print "%10.3s" % str
         abc
```

浮点类型数据位数保留

```python
>>> import fpformat
>>> a= 0.0030000000005
>>> b=fpformat.fix(a,6)
>>> print b
  0.003000
```

对浮点数四舍五入,主要使用到round函数

```python
>>> from decimal import *
>>> a ="2.26"
>>> b ="2.29"
>>> c = Decimal(a) - Decimal(b)
>>> print c
  -0.03
>>> c / Decimal(a) * 100
  Decimal('-1.327433628318584070796460177')
>>> Decimal(str(round(c / Decimal(a) * 100, 2)))
  Decimal('-1.33')
```

## 进制转换

有些时候需要作不同进制转换，可以参考下面的例子(%x 十六进制,%d 十进制,%o 八进制)

```python
>>> num = 10
>>> print "Hex = %x,Dec = %d,Oct = %o" %(num,num,num)
  Hex = a,Dec = 10,Oct = 12
```

## Python调用系统命令或者脚本

使用 os.system() 调用系统命令 , 程序中无法获得到输出和返回值

```python
>>> import os
>>> os.system('ls -l /proc/cpuinfo')
>>> os.system("ls -l /proc/cpuinfo")
  -r--r--r-- 1 root root 0  3月 29 16:53 /proc/cpuinfo
  0
```

使用 os.popen() 调用系统命令, 程序中可以获得命令输出，但是不能得到执行的返回值

```python
>>> out = os.popen("ls -l /proc/cpuinfo")
>>> print out.read()
  -r--r--r-- 1 root root 0  3月 29 16:59 /proc/cpuinfo  
```

使用 commands.getstatusoutput() 调用系统命令, 程序中可以获得命令输出和执行的返回值

```python
>>> import commands
>>> commands.getstatusoutput('ls /bin/ls')
  (0, '/bin/ls')
```

## Python 捕获用户 Ctrl+C ,Ctrl+D 事件

有些时候，需要在程序中捕获用户键盘事件，比如ctrl+c退出，这样可以更好的安全退出程序

```python
try:
    do_some_func()
except KeyboardInterrupt:
    print "User Press Ctrl+C,Exit"
except EOFError:
    print "User Press Ctrl+D,Exit"
```

## Python 读写文件

一次性读入文件到列表，速度较快，适用文件比较小的情况下

```python
track_file = "track_stock.conf"
fd = open(track_file)
content_list = fd.readlines()
fd.close()
for line in content_list:
    print line  
```

逐行读入，速度较慢,适用没有足够内存读取整个文件(文件太大)

```python
fd = open(file_path)
fd.seek(0)
title = fd.readline()
keyword = fd.readline()
uuid = fd.readline()
fd.close()  
```

写文件 write 与 writelines 的区别   

+ Fd.write(str) : 把str写到文件中，write()并不会在str后加上一个换行符
+ Fd.writelines(content) : 把content的内容全部写到文件中,原样写入，不会在每行后面加上任何东西

## 链式比较操作

    >>> x = 5
    >>> 1 < x < 10
    True
    >>> 10 < x < 20
    False
    >>> x < 10 < x*10 < 100
    True
    >>> 10 > x <= 9
    True
    >>> 5 == x > 4
    True

你可能认为它执行的过程先是：`1 < x`，返回`True`，然后再比较`True < 10`,当然这么做也是返回`True`,比较表达式`True < 10`,因为解释器会把`True`转换成`1`，`False`转换成`0`。但这里的链式比较解释器在内部并不是这样干的，它会把这种链式的比较操作转换成：`1 < x and x < 10`，不信你可以看看最后一个例子。

## 枚举

    >>> a = ['a', 'b', 'c', 'd', 'e']
    >>> for index, item in enumerate(a): print index, item
    ...
    0 a
    1 b
    2 c
    3 d
    4 e
    >>>

用enumerate包装一个可迭代对象,可以同时使用迭代项和索引，如果你不这么干的话，下面有一种比较麻烦的方法：  

    for i in range(len(a)):
        print i, a[i]

enumerate 还可以接收一个可选参数start，默认start等于0。`enumerate(list, start=1)`，这样index的起始值就是1  

## 生成器对象

    x=(n for n in foo if bar(n))  #foo是可迭代对象
    >>> type(x)
    <type 'generator'>

你可以把生成器对象赋值给x，意味着可以对x进行迭代操作：  

    for n in x:
        pass

它的好处就是不需要存储中间结果，也许你会使用（列表推倒式）：  

    x = [n for n in foo if bar(n)]
    >>> type(x)
    <type 'list'>

它比生成器对象能带来更快的速度。相对地，生成器更能节省内存开销，它的值是按需生成，不需要像列表推倒式一样把整个结果保存在内存中，同时它不能重新迭代，列表推倒式则不然。  

## iter()可接收callable参数

iter()内建函数接收的参数分为两种，第一种是：  

    iter(collection)---> iterator

参数collection必须是可迭代对象或者是序列 ，第二种是：  

    iter（callable， sentinel) --> iterator

callable函数会一直被调用，直到它的返回结果等于sentinel，例如：  

    def seek_next_line(f):
        #每次读一个字符，直到出现换行符就返回
        for c in iter(lambda: f.read(1),'\n'):  
            pass

## 小心可变的默认参数

    >>> def foo(x=[]):
    ...     x.append(1)
    ...     print x
    ...
    >>> foo()
    [1]
    >>> foo()
    [1, 1]
    >>> foo()
    [1, 1, 1]

取而代之的是你应该使用一个标记值表示“没有指定”来替换可变值,如：  

    >>> def foo(x=None):
    ...     if x is None:
    ...         x = []
    ...     x.append(1)
    ...     print x
    >>> foo()
    [1]
    >>> foo()
    [1]

## 发送值到生成器函数

    def mygen():
        """Yield 5 until something else is passed back via send()"""
        a = 5
        while True:
            f = (yield a) #yield a and possibly get f in return
            if f is not None:
                a = f  #store the new value

你可以：  

    >>> g = mygen()
    >>> g.next()
    5
    >>> g.next()
    5
    >>> g.send(7)  #we send this back to the generator
    7
    >>> g.next() #now it will yield 7 until we send something else
    7

## 如果你不喜欢使用空格缩进，那么可以使用C语言花括号{}定义函数：  

    >>> from __future__ import braces   #这里的braces 指的是：curly braces（花括号）
      File "<stdin>", line 1
    SyntaxError: not a chance

当然这仅仅是一个玩笑，想用花括号定义函数？没门。感兴趣的还可以了解下：  

    from __future__ import barry_as_FLUFL

不过这是python3里面的特性，http://www.python.org/dev/peps/pep-0401/  

## 切片操作中的步长参数

    a = [1,2,3,4,5]
    >>> a[::2]  # iterate over the whole list in 2-increments
    [1,3,5]

还有一个特例：`x[::-1]`，反转列表：  

    >>> a[::-1]
    [5,4,3,2,1]

有关反转，还有两个函数reverse、reversed，reverse是list对象的方法，没有返回值，而reversed是内建方法，可接收的参数包括tuple、string、list、unicode，以及用户自定义的类型，返回一个迭代器。  

    >>> l = range(5)
    >>> l
    [0, 1, 2, 3, 4]
    >>> l.reverse()
    >>> l
    [4, 3, 2, 1, 0]
    >>> l2 = reversed(l)
    >>> l2
    <listreverseiterator object at 0x99faeec>

## 装饰器

装饰器使一个函数或方法包装在另一个函数里头，可以在被包装的函数添加一些额外的功能，比如日志，还可以对参数、返回结果进行修改。装饰器有点类似Java中的AOP。下面这个例子是打印被装饰的函数里面的参数的装饰器，  

    >>> def print_args(function):
    >>>     def wrapper(*args, **kwargs):
    >>>         print 'Arguments:', args, kwargs
    >>>         return function(*args, **kwargs)
    >>>     return wrapper

    >>> @print_args
    >>> def write(text):
    >>>     print text

    >>> write('foo')
    Arguments: ('foo',) {}
    foo

@是语法糖，它等价于：  

    >>> write = print_args(write)
    >>> write('foo')
    arguments: ('foo',) {}
    foo

## for ... else语法

    for i in foo:
        if i == 0:
            break
    else:
        print("i was never 0")

else代码块只有在for循环正常结束后执行如果遇到break语句那么不会执行else语句块，等价于下面：  

    found = False
    for i in foo:
        if i == 0:
            found = True
            break
    if not found:
        print("i was never 0")

不过这种语法看起来怪怪地，让人感觉是else块是在for语句块没有执行的时候执行的，很容易让人去类比 if else 的语法，如果是把else换成finally或许更容易理解    

## 变量值交换

    >>> a = 10
    >>> b = 5
    >>> a, b
    (10, 5)

    >>> a, b = b, a
    >>> a, b
    (5, 10)

等号右边是一个创建元组的表达式，等号左边解压（没有引用的）元组分别赋给名称（变量）a和b。赋完值后因为没有被其他名字引用，因此被标记之后被垃圾收集器回收，而绑定到a和b的值已经被交换了。  

注意：多值赋值其实仅仅就是元组打包和序列解包的组合的过程  

## 可读的正则表达式

在Python中你可以把正则表达式分割成多行写，还可以写注释  

    >>> pattern = """
    ... ^                   # beginning of string
    ... M{0,4}              # thousands - 0 to 4 M's
    ... (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
    ...                     #            or 500-800 (D, followed by 0 to 3 C's)
    ... (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
    ...                     #        or 50-80 (L, followed by 0 to 3 X's)
    ... (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
    ...                     #        or 5-8 (V, followed by 0 to 3 I's)
    ... $                   # end of string
    ... """
    >>> re.search(pattern, 'M', re.VERBOSE)

## 函数参数解包(unpacking)

分别使用`*`和`**`解包列表和字典,这是一种非常实用的快捷方式,因为list,tuple,dict作为容器被广泛使用    

    def draw_point(x, y):
        # do some magic

    point_foo = (3, 4)
    point_bar = {'y': 3, 'x': 2}

    draw_point(*point_foo)
    draw_point(**point_bar)

## 动态地创建新类型

动态创建新类型虽不是实用功能,但了解一下也是有好处的  

    >>> NewType = type("NewType", (object,), {"x": "hello"})
    >>> n = NewType()
    >>> n.x
    "hello"

type的第一个参数就是类名,第二个参数是继承的父类,第三个参数是类的属性.它完全等同于:  

    >>> class NewType(object):
    >>>     x = "hello"
    >>> n = NewType()
    >>> n.x
    "hello"

## 上下文管理器与with语句

上下文管理器(context manager)用于规定某个对象的使用范围,进入或退出该范围时,特殊的操作会被执行(比如关闭连接,释放内存等等),语法是:`with... as ...`,该特性在python2.5引入的.

上下文管理器协议有两个方法组成`contextmanager.__enter__()`和`contextmanager.__exit__()`,任何实现了这两个方法的对象都称之为上下文管理器对象,比如文件对象就默认实现了该协议.

    with open('foo.txt', 'w') as f:
        f.write('hello!')

## 字典的get()方法

字典的get()方法用来替换d['key'],后者如果是遇到key不存在会有异常,如果使用的d.get('key'),key不存在时它返回的是None,你可以指定两个参数如:d.get('key',0)来用0取代返回的None  

    sum[value] = sum.get(value, 0) + 1

还有一个类似的方法`setdefault(key, value)`,如果字典中存在key,那么就直接返回d[key],否则设置d[key]=value,并返回该值.  

    >>> d = {'key':123}
    >>> d.setdefault('key',456)
    123
    >>> d['key']
    123
    >>> d.setdefault('key2',456)
    456
    >>> d['key2']
    456

collections.Counter是dict的子类,用来统计可哈稀对象,

    >>> cnt = Counter('helloworld')
    >>> cnt
    Counter({'l': 3, 'o': 2, 'e': 1, 'd': 1, 'h': 1, 'r': 1, 'w': 1})
    >>> cnt['l']
    3
    >>> cnt['x'] = 10
    >>> cnt.get('y')

## 描述符(Descriptors)

描述符是python的核心特新之一,当你使用`.`访问成员时,(如:x.y),python首先在实例字典中查找该成员,如果没有发现再从类字典中查找,如果这个对象实现了描述符(实现了`__get__,__set__,__delete__`),那么优先返回`__get__`方法的返回值.  

## 条件赋值

为什么python中没有类c语言的三目运算符,Guido van Rossum说过了,条件赋值更容易理解  

    x = 3 if (y == 1) else 2

这个表达式的意思就是:如果y等于那么就把3赋值给x,否则把2赋值给x, 条件中的括号是可选的,为了可读性可以考虑加上去.if else中的表达式可以是任何类型的,既可以函数,还可以类  

    (func1 if y == 1 else func2)(arg1, arg2)

如果y等于1,那么调用func1(arg1,arg2)否则调用func2(arg1,arg2)  

    x = (class1 if y == 1 else class2)(arg1, arg2)

class1,class2是两个类  

## 异常else语句块

    try:
       try_this(whatever)
    except SomeException, exception:
       #Handle exception
    else:
        # do something
    finally:
        #do something

else语句块会在没有异常的情况下执行,先于finally,它的好处就是你可以明确知道它会在没有异常的情况下执行,如果是把else语句块放在try语句块里面就达不到这种效果.  

## 原始数据类型和操作符

+ 布尔值也是基本的数据类型 `True` 和 `False`
+ 用 `not` 来取非
+ 字符串通过 `+` 号拼接，字符串可以被视为字符的列表
+ `%` 可以用来格式化字符串： `"%s can be %s" % ("strings", "interpolated")`
+ 也可以用 `format` 方法，这个更推荐：`"{0} can be {1}".format("strings", "formatted")`。也可以用变量名代替数字：`"{name} wants to eat {food}".format(name="Bob", food="lasagna")`
+ `None` 是对象，用 `is` 来比较：`"etc" is None`
+ `is` 可以用来比较对象的相等性，在比较原始的数据时没多少用，但是比较对象时必不可少

## 变量和集合

+ 列表用来保存序列：`li = []`，也可以直接初始化 `other_li = [4, 5, 6]`
+ 在列表末尾添加元素：`li.append(1)`
+ 访问最后一个元素：`li[-1]`
+ 拼接列表：`li.extend(other_li)`
+ 用 `in` 来返回元素是否在列表中
+ 返回列表长度：`len(li)`

---

+ 元组类似于列表，但是不可改变：`tuple = (1, 2, 3)`
+ 交换两个数字：`e, d = d, e`

---

+ 用字典来存储映射关系：`empty_dict = {}`
+ 字典初始化：`filled_dict = {"one": 1, "two": 2, "three": 3}`
+ 用中括号访问元素 `filled_dict["one"]`
+ 把所有的 key 保存在列表中 `filled_dict.keys()` -> `["three", "two", "one"]`
+ 把所有的 value 保存在列表中 `filled_dict.values()` 和 key 的顺序相同
+ 判断一个键是否存在 `"one" in filled_dict`
+ 用 get 方法来避免访问不存在的 key 时的 KeyError：`filled_dict.get("one")`，如果 key 不存在，则会返回一个 None

---

+ 集合存储无顺序的元素：`empty_set = set()`
+ Python 2.7 之后，大括号可以用来表示集合：`filled_set = {1, 2, 2, 3, 4}` -> `{1 2 3 4}`
+ 向集合添加元素：`filled_set.add(5)`
+ 用 `&` 来计算集合的交
+ `|` 并
+ `-` 差
+ `in` 判断元素是否在集合中

## 控制流程

+ `range(number)` 返回从 0 到 number 的列表
+ while 循环比较方便加条件

## 函数

+ 用 def 来新建函数
+ 通过 return 来返回值
+ 匿名函数：`(lambda x: x > 2)(3)`
+ 内置高阶函数 `map(add_10, [1, 2, 3])`

## 类

+ 继承：`class Human(object):` 继承了 object 类
+ 成员方法，参数要有 self：`def say(self, msg):`
+ 类方法由所有类的对象共享，这类方法在调用时，会把类本身传给第一个参数

例如

    @classmethod
    def get_species(cls):
        return cls.species

+ 静态方法是不需要类和对象的引用就可以调用的方法

例如

    @staticmethod
    def grunt():
        return "*grunt*"

## 模块

+ 导入其他模块：`import math`
+ 导入特定函数：`from math import ceil, floor`
+ 从模块中导入所有函数，不推荐使用：`from math import *`
+ 简写模块名：`import math as m`
+ 查看属性：`dir(math)`
