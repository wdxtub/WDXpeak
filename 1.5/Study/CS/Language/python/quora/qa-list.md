### 序列的切片操作

问题 [链接](http://stackoverflow.com/questions/509211/the-python-slice-notation)

It's pretty simple really:
很简单:

    a[start:end] # start 到 end-1
    a[start:]    # start 到 末尾
    a[:end]      # 0 到 end-1
    a[:]         # 整个列表的拷贝

还有一个step变量，控制步长,可在上面语法中使用

    a[start:end:step] # start through not past end, by step


注意，左闭右开

其他特点，开始或结束下标可能是负数，表示从序列末尾开始计算而非从头开始计算,所以

    a[-1]    # 最后一个元素
    a[-2:]   # 最后两个元素
    a[:-2]   # 除了最后两个元素

Python对程序员很友好，如果序列中存在的元素数量少于你要的，例如，你请求 a[:-2] 但是a只有一个元素，你会得到一个空列表，而不是一个错误.有时候你或许希望返回的是一个错误，所以你必须知道这点
### 判断一个列表为空得最佳实践

问题 [链接](http://stackoverflow.com/questions/53513/python-what-is-the-best-way-to-check-if-a-list-is-empty)

答案:

    if not a:
        print "List is empty"
    #不要用len(a)来判断

### 如何合并两个列表

问题 [链接](http://stackoverflow.com/questions/1720421/merge-two-lists-in-python)

    listone = [1,2,3]
    listtwo = [4,5,6]
    #outcome we expect: mergedlist == [1, 2, 3, 4, 5, 6]

1.不考虑顺序（原来问题不是很明确）

    listone + listtwo
    #linstone.extend(listtwo)也行，就是会修改listone

2.考虑顺序做些处理

    >>> listone = [1,2,3]
    >>> listtwo = [4,5,6]
    >>> import itertools
    >>> for item in itertools.chain(listone, listtwo):
    ...     print item
    ...
    1
    2
    3
    4
    5
    6

### 如何获取一个列表的长度

问题 [链接](http://stackoverflow.com/questions/518021/getting-the-length-of-an-array-in-python)

python中是不是只有这种方法可以获取长度？语法很奇怪

    arr.__len__()

应该使用这种方式

    mylist = [1,2,3,4,5]
    len(mylist)

这样做法，不需要对每个容器都定义一个.length()方法，你可以使用len()检查所有实现了__len__()方法的对象

### Python中如何复制一个列表

问题 [链接](http://stackoverflow.com/questions/2612802/how-to-clone-a-list-in-python)

可以用切片的方法

    new_list = old_list[:]

可以使用list()函数

    new_list = list(old_list)

可以使用copy.copy(),比list()稍慢，因为它首先去查询old_list的数据类型

    import copy
    new_list = copy.copy(old_list)

如果列表中包含对象，可以使用copy.deepcopy(), 所有方法中最慢，但有时候无法避免

    import copy
    new_list = copy.deepcopy(old_list)

例子：

    import copy

    class Foo(object):
        def __init__(self, val):
             self.val = val

        def __repr__(self):
            return str(self.val)

    foo = Foo(1)

    a = ['foo', foo]
    b = a[:]
    c = list(a)
    d = copy.copy(a)
    e = copy.deepcopy(a)

    # edit orignal list and instance
    a.append('baz')
    foo.val = 5

    print "original: %r\n slice: %r\n list(): %r\n copy: %r\n deepcopy: %r" \
           % (a, b, c, d, e)

结果:

    original: ['foo', 5, 'baz']
    slice: ['foo', 5]
    list(): ['foo', 5]
    copy: ['foo', 5]
    deepcopy: ['foo', 1]

效率简单比较

    10.59 - copy.deepcopy(old_list)
    10.16 - pure python Copy() method copying classes with deepcopy
    1.488 - pure python Copy() method not copying classes (only dicts/lists/tuples)
    0.325 - for item in old_list: new_list.append(item)
    0.217 - [i for i in old_list] (a list comprehension)
    0.186 - copy.copy(old_list)
    0.075 - list(old_list)
    0.053 - new_list = []; new_list.extend(old_list)
    0.039 - old_list[:] (list slicing)

### 列表的append和extend的区别

问题 [链接](http://stackoverflow.com/questions/252703/python-append-vs-extend)

    >>> x = [1, 2]
    >>> x.append(3)
    >>> x
    [1, 2, 3]
    >>> x.append([4,5])
    >>> x
    [1, 2, 3, [4, 5]]
    >>>
    >>> x = [1, 2, 3]
    >>> x.extend([4, 5])
    >>> x
    [1, 2, 3, 4, 5]

### 如何随机地从列表中抽取变量

问题 [链接](http://stackoverflow.com/questions/306400/how-do-i-randomly-select-an-item-from-a-list-using-python)

    foo = ['a', 'b', 'c', 'd', 'e']
    from random import choice
    print choice(foo)

### 如何利用下标从列表中删除一个元素

问题 [链接](http://stackoverflow.com/questions/627435/how-to-remove-an-element-from-a-list-by-index-in-python)

1.del

    In [9]: a = range(10)
    In [10]: a
    Out[10]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    In [11]: del a[-1]
    In [12]: a
    Out[12]: [0, 1, 2, 3, 4, 5, 6, 7, 8]

2.pop

    a = ['a', 'b', 'c', 'd']
    a.pop(1)
    # now a is ['a', 'c', 'd']

    a = ['a', 'b', 'c', 'd']
    a.pop()
    # now a is ['a', 'b', 'c']

### 获取列表的最后一个元素

问题 [链接](http://stackoverflow.com/questions/930397/how-to-get-the-last-element-of-a-list)

囧

    result = l[-1]
    result = l.pop()

### 如何将一个列表切分成若干个长度相同的子序列

问题 [链接](http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python)

想要得到这样的效果

    l = range(1, 1000)
    print chunks(l, 10) -> [ [ 1..10 ], [ 11..20 ], .., [ 991..999 ] ]

使用yield:

    def chunks(l, n):
        """ Yield successive n-sized chunks from l.
        """
        for i in xrange(0, len(l), n):
            yield l[i:i+n]
    list(chunks(range(10, 75), 10))

直接处理

    def chunks(l, n):
        return [l[i:i+n] for i in range(0, len(l), n)]

### 如何删除一个list中重复的值同时保证原有顺序

问题 [链接](http://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-in-python-whilst-preserving-order)

我是这么做的额

    def uniq(input):
    output = []
    for x in input:
        if x not in output:
        output.append(x)
    return output

有什么更好的方法？

你可以在这里找到一些可用的方法 [入口](http://www.peterbe.com/plog/uniqifiers-benchmark)

最快的一个

    def f7(seq):
        seen = set()
        seen_add = seen.add
        return [ x for x in seq if x not in seen and not seen_add(x)]

如果你需要在同一个数据集中多次是哦那个这个方法，或许你可以使用ordered set处理 http://code.activestate.com/recipes/528878/

插入，删除和归属判断复杂度都是O(1)

### 如何在遍历一个list时删除某些元素

问题 [链接](http://stackoverflow.com/questions/1207406/remove-items-from-a-list-while-iterating-in-python)

使用列表解析

    somelist = [x for x in somelist if determine(x)]

上面那个操作将产生一个全新的somelist对象，而失去了对原有somelist对象的引用

    #在原有对象上进行修改
    somelist[:] = [x for x in somelist if determine(x)]

使用itertools

    from itertools import ifilterfalse
    somelist[:] = list(ifilterfalse(determine, somelist))

### 如何获取list中包含某个元素所在的下标

问题 [链接](http://stackoverflow.com/questions/176918/in-python-how-do-i-find-the-index-of-an-item-given-a-list-containing-it)


    >>> ["foo","bar","baz"].index('bar')
    1

参照 [文档](http://docs.python.org/2/tutorial/datastructures.html#more-on-lists)

### 如何扁平一个二维数组

问题 [链接](http://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python)

    l = [[1,2,3],[4,5,6], [7], [8,9]]
    变为[1, 2, 3, 4, 5, 6, 4, 5, 6, 7, 8, 9]

列表解析

    [item for sublist in l for item in sublist]

itertools

    >>> import itertools
    >>> list2d = [[1,2,3],[4,5,6], [7], [8,9]]
    >>> merged = list(itertools.chain(*list2d))

    # python >= 2.6
    >>> import itertools
    >>> list2d = [[1,2,3],[4,5,6], [7], [8,9]]
    >>> merged = list(itertools.chain.from_iterable(list2d))

sum

    sum(l, [])


### 列表解析和map

问题 [链接](http://stackoverflow.com/questions/1247486/python-list-comprehension-vs-map)

更喜欢使用map()而不是列表解析的原因是什么？


在某些情况下，map性能更高一些(当你不是为了某些目的而使用lambda，而是在map和列表解析中使用相同函数).

列表解析在另一些情况下性能更好，并且大多数pythonistas认为这样更简洁直接

使用相同函数，略微优势

    $ python -mtimeit -s'xs=range(10)' 'map(hex, xs)'
    100000 loops, best of 3: 4.86 usec per loop
    $ python -mtimeit -s'xs=range(10)' '[hex(x) for x in xs]'
    100000 loops, best of 3: 5.58 usec per loop

相反情况，使用lambda

    $ python -mtimeit -s'xs=range(10)' 'map(lambda x: x+2, xs)'
    100000 loops, best of 3: 4.24 usec per loop
    $ python -mtimeit -s'xs=range(10)' '[x+2 for x in xs]'
    100000 loops, best of 3: 2.32 usec per loop

### 列表和元组有什么区别

问题[链接](http://stackoverflow.com/questions/626759/whats-the-difference-between-list-and-tuples)

除了元组是不可变的之外，还有一个语义的区别去控制它们的使用。元组是各种结构类型混杂的（比如，它们的入口有不同的含义），列表则是一致的序列。元组有结构，列表有顺序。

根据这种据别，刻意让代码更为明确和易理解。

用页数和行数来定义一本书中的位置的例子：

    my_location = (42, 11)  # page number, line number

然后你可以在一个字典里把这个当做键保存位置的记录。然而列表可以用来存储多点定位。通常会想添加或移除一个列表中的某个定位，所以列表是可变的。另一方面，为了保持行数的完好无损，而改变页书的值似乎说不通，这很可能会给你一个新的定位。而且，可能有很完美的解决办法用来处理正确的行数（而不是替换所有的元组）

这一点，有很多有趣的文章，比如[”Python Tuples are Not Just Constant Lists”](http://jtauber.com/blog/2006/04/15/python_tuples_are_not_just_constant_lists/) or [“Understanding tuples vs. lists in Python”](http://news.e-scribe.com/397)。Python官方文档也[提到了](https://docs.python.org/2/tutorial/datastructures.html#tuples-and-sequences)（“元组是不可变对象，并且用于包含哪些混杂的序列…”)。

在一个动态类型语言比如haskell，元组通常有不同的类型，并且元组的长度必须是固定的。在列表中值必须是同一种类型，值长度不需要固定。所以区别很明显。

最后，Python中还有一个[nametuple](https://docs.python.org/dev/library/collections.html#collections.namedtuple)，合理表示一个元组已经有的结构。这些突出的想法明确了元组是类和实例的一种轻型的替换。

### Python 2.7里[...]是什么？

问题[链接](http://stackoverflow.com/questions/17160162/what-is-in-python-2-7)

它意味着你在它的内部创建了一个无限嵌套的不能打印的列表。`p`包含一个包含`p`的`p`...等等。`[...]`就是一种让你知道问题的标记，为了通告信息，它不能被而代表。看一下@6502的答案，那些展示了发生什么的优秀的图片。

现在，关于之后你编辑的三个问题：

* 这个[答案](http://stackoverflow.com/questions/7674685/whats-exactly-happening-in-infinite-nested-lists/7680125#7680125)看上去已经覆盖它了

* Ignacio的[链接](http://www.csse.monash.edu.au/~lloyd/tildeFP/1993ACJ/)描述了一些可能的用法

* 这更像是一种数据结构设计的话题而不是编程语言，所以很不幸，你不能在Python的官方文档找到任何参考

