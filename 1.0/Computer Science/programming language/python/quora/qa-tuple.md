### Python中的命名元组是什么？

问题[链接](http://stackoverflow.com/questions/2970608/what-are-named-tuples-in-python)

命名元组基本上是一种易创建，轻量的对象类型。命名元组实例像值引用一样被对象引用或者使用基础的元组语法。他们可以像`struct`或者其他常用的记录类型一样被使用，除了他们是不可变的。他们在Python 2.6和Python 3.0中被加入。尽管有一个[在Python2.4中实现的秘诀](http://code.activestate.com/recipes/500261/)

举个例子，通常我们要顶一个点，用元组表示`(x, y)`。用代码写出来像下面这样：

    pt1 = (1.0, 5.0)
    pt2 = (2.5, 1.5)

    from math import sqrt
    line_length = sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)

使用命名元组可以更可读：

    from collections import namedtuple
    Point = namedtuple('Point', 'x y')
    pt1 = Point(1.0, 5.0)
    pt2 = Point(2.5, 1.5)

    from math import sqrt
    line_length = sqrt((pt1.x-pt2.x)**2 + (pt1.y-pt2.y)**2)

然而，命名元组仍然向下兼容普通的元组，所以下面的代码仍然有效：

    Point = namedtuple('Point', 'x y')
    pt1 = Point(1.0, 5.0)
    pt2 = Point(2.5, 1.5)

    from math import sqrt
    # use index referencing
    line_length = sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)
     # use tuple unpacking
    x1, y1 = pt1

因此，如果你认为对象标记可以让你的代码更Pythonic、更可读，那么请将所有的元组替换为命名元组。我个人已经开始使用命名元组去替代非常简单的值类型，尤其是那些要作为参数传入函数的东西。它让函数不用知道元组的包装内容，更加具有可读性。

长远点说，你还可以用命名元组替代不含方法的普通不可变类。你还可以把你的命名元组类型作为基类：

    class Point(namedtuple('Point', 'x y')):
        [...]

当然，作为元组，命名元组中的属性仍然是不可变的：

    >>> Point = namedtuple('Point', 'x y')
    >>> pt1 = Point(1.0, 5.0)
    >>> pt1.x = 2.0
    AttributeError: can't set attribute

如果你想改变这些值，你需要另一个类型。有一个方便的方法[mutable recordtypes](http://code.activestate.com/recipes/576555/)，它允许你把修改属性为新的值。

    >>> from rcdtype import *
    >>> Point = recordtype('Point', 'x y')
    >>> pt1 = Point(1.0, 5.0)
    >>> pt1 = Point(1.0, 5.0)
    >>> pt1.x = 2.0
    >>> print(pt1[0])
        2.0

我仍然不知道有任何”命名列表“的结构，可以让你添加新的区块。这种情况下你可能只是需要用一个字典。命名元组可以转化成字典，用`pt1._asdict()`可以返回`{'x': 1.0, 'y': 5.0}`而且升级为可以使用所有字典常用的函数。

已经标记过的，你应该[查看文档](https://docs.python.org/3/library/collections.html#collections.namedtuple)来获取更多搭建这些例子的信息。