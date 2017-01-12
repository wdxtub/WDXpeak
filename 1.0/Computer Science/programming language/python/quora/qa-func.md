
### 如何获取一个函数的函数名字符串

问题 [链接](http://stackoverflow.com/questions/251464/how-to-get-the-function-name-as-string-in-python)

    my_function.__name__
    >>> import time
    >>> time.time.__name__
    'time'
### 用函数名字符串调用一个函数

问题 [链接](http://stackoverflow.com/questions/3061/calling-a-function-from-a-string-with-the-functions-name-in-python)

假设模块foo有函数bar:

    import foo
    methodToCall = getattr(foo, 'bar')
    result = methodToCall()

或者一行搞定

    result = getattr(foo, 'bar')()


### Python中**和*的作用

问题  [链接](http://stackoverflow.com/questions/36901/what-does-double-star-and-star-do-for-python-parameters)


*args和**kwargs允许函数拥有任意数量的参数，具体可以查看 [more on defining functions](http://docs.python.org/dev/tutorial/controlflow.html#more-on-defining-functions)

*args将函数所有参数转为序列

    In [1]: def foo(*args):
    ...:     for a in args:
    ...:         print a
    ...:
    ...:

    In [2]: foo(1)
    1


    In [4]: foo(1,2,3)
    1
    2
    3

**kwargs 将函数所有关键字参数转为一个字典

    In [5]: def bar(**kwargs):
    ...:     for a in kwargs:
    ...:         print a, kwargs[a]
    ...:
    ...:

    In [6]: bar(name="one", age=27)
    age 27
    name one

两种用法可以组合使用

    def foo(kind, *args, **kwargs):
        pass

*l的另一个用法是用于函数调用时的参数列表解包(unpack)

    In [9]: def foo(bar, lee):
    ...:     print bar, lee
    ...:
    ...:

    In [10]: l = [1,2]

    In [11]: foo(*l)
    1 2

在Python3.0中，可以将*l放在等号左边用于赋值  [Extended Iterable Unpacking](http://www.python.org/dev/peps/pep-3132/)

    first, *rest = [1,2,3,4]
    first, *l, last = [1,2,3,4]

### 在Python中使用\*\*kwargs的合适方法

问题 [链接](http://stackoverflow.com/questions/1098549/proper-way-to-use-kwargs-in-python)

当存在默认值的时候，如何合适的使用**kwargs?

kwargs返回一个字典，但是这是不是设置默认值的最佳方式？还是有其他方式？我只能将其作为一个字典接受，然后用get函数获取参数？

    class ExampleClass:
        def __init__(self, **kwargs):
            self.val = kwargs['val']
            self.val2 = kwargs.get('val2')

问题很简单，但是我没找到合适的解释。我见到人们用不同的方式实现，很难搞明白如何使用

回答

你可以用get函数给不在字典中的key传递一个默认值

    self.val2 = kwargs.get('val2',"default value")

但是，如果你计划给一个特别的参数赋默认值，为什么不在前一个位置使用命名参数？

    def __init__(self, val2="default value", **kwargs):

<<<<<<< HEAD
### 构造一个基本的Python迭代器

- 问题
[链接](http://stackoverflow.com/questions/19151/build-a-basic-python-iterator)
 
- 回答


python中的迭代器对象遵守迭代器协议,也就意味着python会提供两个方法:__iter__() 和 next().方法__iter__ 返回迭代器对象并且在循环开始时隐含调用.方法next()返回下一个值并且在每次循环中隐含调用.方法next()在没有任何值可返回时,抛出StopIteration异常.之后被循环构造器捕捉到而停止迭代.

下面是简单的计数器例子:
```python
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def next(self): # Python 3: def __next__(self)
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


for c in Counter(3, 8):
    print c
```
输出:
```python
3
4
5
6
7
8
```

使用生成器会更简单,包含了先前的回答:
```python
def counter(low, high):
    current = low
    while current <= high:
        yield current
        current += 1

for c in counter(3, 8):
    print c
```

输出是一样的.本质上说,生成器对象支持迭代协议并且大致完成和计数器类相同的事情.

David Mertz的文章, [Iterators and Simple Generators](http://www.ibm.com/developerworks/library/l-pycon.html),是一个非常不错的介绍.

### \*args和\*\*kwargs是什么
问题[链接](http://stackoverflow.com/questions/3394835/args-and-kwargs)

真正的语法是`*`和`**`，`*args`和`**kwargs`这两个名字只是约定俗成的，但并没有硬性的规定一定要使用它们。

当你不确定有多少个参数会被传进你的函数时，你可能会使用`*args`，也就是说它允许你给你的函数传递任意数量的参数，举个例子：

    >>> def print_everything(*args):
            for count, thing in enumerate(args):
    …           print ‘{0}. {1}’.format(count, thing)
    …
    >>> print_everthing(‘apple’, ‘banana’, ‘cabbage’)
    0. apple
    1. banana
    2. cabbage

类似的，`**kwargs`允许你处理那些你没有预先定义好的已命名参数

    >>> def table_everything(*args):
            for name, value in kwargs.items():
    …           print ‘{0} = {1}’.format(name, value)
    …
    >>> table_everthing(apple = ‘fruit’, cabbage = ‘vegetable’)
    cabbage = vegetable
    apple = fruit

你一样可以使用这些命名参数。明确的参数会优先获得值，剩下的都会传递给`*args`和`**kwargs`，命名参数排在参数列表前面，举个例子：

    def table_things(titlestring, **kwargs)

你可以同时使用它们，但是`*args`必须出现在`**kwargs`之前。

调用一个函数时也可以用`*`和`**`语法，举个例子：

    >>> def print_three_things(*args):
    …           print ‘a = {0}, b = {1}, c = {2}’.format(a, b , c)
    …
    >>> mylist = [‘aardvark’, ‘baboon’, ‘cat’]
    >>> print_three_things(*mylist)
    a = aardvark, b = baboon, c = cat

正如你看到的，它得到了一个list或者tuple，并解包这个list。通过这种方法，它将这些元素和函数中的参数匹配。当然，你可以同时在函数的定义和调用时使用`*`。


### 在Python中，如何干净、pythonic的实现一个复合构造函数

问题[链接](http://stackoverflow.com/questions/682504/what-is-a-clean-pythonic-way-to-have-multiple-constructors-in-python)

实际上 `None`比“魔法”值好多了：

    class Cheese():
        def __init__(self, num_holes = None):
            if (num_holes is None):
                …

现在如果你想完全自由地添加更多参数：

    class Cheese():
        def __init__(self, *args, **kwargs):
            #args -- tuple of anonymous arguments
            #kwargs -- dictionary of named arguments
            self.num_holes = kwargs.get('num_holes',random_holes())

为了更好的解释`*args`和`**kwargs`的概念（实际上你可以修改它们的名字）：

    def f(*args, **kwargs):
        print 'args: ', args, ' kwargs: ', kwargs

    >>> f('a')
    args:  ('a',)  kwargs:  {}
    >>> f(ar='a')
    args:  ()  kwargs:  {'ar': 'a'}
    >>> f(1,2,param=3)
    args:  (1, 2)  kwargs:  {'param': 3}

[http://docs.python.org/reference/expressions.html#calls](http://docs.python.org/reference/expressions.html#calls)

### Python参数中，\*\*和\*是干什么的

问题[链接](http://stackoverflow.com/questions/36901/what-does-double-star-and-star-do-for-python-parameters)

`*args`和`**args`是一种惯用的方法，允许不定数量的参数传入函数，在Python文档中有描述[more on defining functions](https://docs.python.org/dev/tutorial/controlflow.html#more-on-defining-functions)

`*args`会把所有的参数当做一个列表传递：

    In [1]: def foo(*args):
       ...:     for a in args:
       ...:         print a
       ...:
       ...:

    In [2]: foo(1)
    1


    In [4]: foo(1,2,3)
    1
    2
    3

`**kwargs`会把除了那些符合形参的参数作为一个字典传递：

    In [5]: def bar(**kwargs):
       ...:     for a in kwargs:
       ...:         print a, kwargs[a]
       ...:
       ...:

    In [6]: bar(name="one", age=27)
    age 27
    name one

这两种用法都可以混合进普通参数，允许传入一组固定的的和可变的参数：

    def foo(kind, *args, **kwargs):
        pass

另一种\*的用法就是在调用一个函数的时候解包参数列表

    In [9]: def foo(bar, lee):
       ...:     print bar, lee
       ...:
       ...:

    In [10]: l = [1,2]

    In [11]: foo(*l)
    1 2

在Python 3中，可以把\*用在一个待赋值对象的左边（[Extended Iterable Upacking](https://www.python.org/dev/peps/pep-3132/)）：

    first, *rest = [1, 2, 3, 4]
    first, *l, last = [1, 2, 3, 4]

### 为什么在Python的函数中，代码运行速度更快

问题[链接](http://stackoverflow.com/questions/11241523/why-does-python-code-run-faster-in-a-function)

你可能要问为什么在存储在本地变量的比全局变量运行速度更快。这是一个CPython执行细节。

记住Cpython在解释器运行时，是编译成字节编码的。当一个函数编译完成，本地变量就全部被存储在一个固定长度的数组中了（而不是字典）而且名字被指定了索引。这是合理的，因为你不能自动添加本地变量到你的函数中去。在指针中循环检索一个本地变量加入到列表中，并且计算琐碎的`PyObject`的增加。

不同的是全局查找（`LOAD_GLOBAL`），是一个涉及哈希查找的字典等等。顺带的，这就是为什么当你需要一个全局变量时，要说明`global i`。如果你曾经在一个范围内给一个变量赋值了，那么编译器会为它的入口发布一些`STORE_FAST`。除非你告诉它不要这样做。

顺便说一句，全局查找仍然是非常棒的。属性查找`foo.bar`是非常慢的。

### 如果把一个变量作为引用传入

问题[链接](http://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference)

问题出在[pass by assignment](https://docs.python.org/3/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference)。它背后的原理可以分为两部分：

    1、 传入的参数实际上是一个对象的引用（但是引用的是值）

    2、 有些数据类型是可变的的，有些不是

所以

 - 如果你向方法中传递了一个可变的对象，那么方法得到了这些对象的一个引用，只要你开心，就可以随意改变它。但是如果你在方法中重新定义了引用，外部是不知道的，所以当你改变了它，其他的引用仍然指向根对象。

 - 如果你向方法中传递了一个不可变对象，那么你不会重新定义外部的引用，你甚至不能改变对象。

我们做一些示例，让它们更清晰。

**列表-一种可变类型**

我们试着去修改传入方法中的列表：

    def try_to_change_list_contents(the_list):
        print 'got', the_list
        the_list.append('four')
        print 'changed to', the_list

    outer_list = ['one', 'two', 'three']

    print 'before, outer_list =', outer_list
    try_to_change_list_contents(outer_list)
    print 'after, outer_list =', outer_list

输出：

    before, outer_list = ['one', 'two', 'three']
    got ['one', 'two', 'three']
    changed to ['one', 'two', 'three', 'four']
    after, outer_list = ['one', 'two', 'three', 'four']

一个参数传入的是`outer_list`的一个引用，而不是它的复制，我们可以使用改变列表的方法去改变它，并且把改变反馈给其他的范围。

现在让我们看一下当我们试着改变这个作为参数传入的引用：

    def try_to_change_list_reference(the_list):
        print 'got', the_list
        the_list = ['and', 'we', 'can', 'not', 'lie']
        print 'set to', the_list

    outer_list = ['we', 'like', 'proper', 'English']

    print 'before, outer_list =', outer_list
    try_to_change_list_reference(outer_list)
    print 'after, outer_list =', outer_list

输出：

    before, outer_list = ['we', 'like', 'proper', 'English']
    got ['we', 'like', 'proper', 'English']
    set to ['and', 'we', 'can', 'not', 'lie']
    after, outer_list = ['we', 'like', 'proper', 'English']

`the_list`参数传递的是值，重新定义一个新的列表，对于方法外部的代码，没有任何影响。`the_list`只是`outer_list`的一个引用，我们让`the_list`指向了一个新的列表，但是我们没有办法修改`outer_list`的指向。

**字符串-不可变类型**

它是不可变的，所以我们没有办法改变字符串的内容。

我们试着改变一下引用。

    def try_to_change_string_reference(the_string):
        print 'got', the_string
        the_string = 'In a kingdom by the sea'
        print 'set to', the_string

    outer_string = 'It was many and many a year ago'

    print 'before, outer_string =', outer_string
    try_to_change_string_reference(outer_string)
    print 'after, outer_string =', outer_string

输出：

    before, outer_string = It was many and many a year ago
    got It was many and many a year ago
    set to In a kingdom by the sea
    after, outer_string = It was many and many a year ago

再一次，`the_string`参数通过值传递，定义一个新的字符串对于外部的代码是不起作用的。`the_string`是`outer_string`的一个引用的复制，我们把`the_string`指向了一个新的字符串。但是我们并没有改变`outer_string`的指向。

我希望这样说可以让事情看上去简单一些了。

编辑：被标记了，这并没有回答@David主要想问的问题。“有没有什么办法让我传入的值是真实的引用？“。回答一下。

**我们怎么避免这些？**

像@Andrea的我回答所展示的，你可以返回一个新的值。这不会改变传入的值，但是确实可以让你得到你想要输出的信息：

    def return_a_whole_new_string(the_string):
        new_string = something_to_do_with_the_old_string(the_string)
        return new_string

    # then you could call it like
    my_string = return_a_whole_new_string(my_string)

如果你确实想避免使用一个返回的值，你可以创建一个类承载你的值，并把他传入一个函数或者用一个已知的类，像列表一样：

    def use_a_wrapper_to_simulate_pass_by_reference(stuff_to_change):
        new_string = something_to_do_with_the_old_string(stuff_to_change[0])
        stuff_to_change[0] = new_string

    # then you could call it like
    wrapper = [my_string]
    use_a_wrapper_to_simulate_pass_by_reference(wrapper)

    do_something_with(wrapper[0])

虽然这样看起来有些笨重。
