### 如何结束退出一个python脚本

问题 [链接](http://stackoverflow.com/questions/73663/terminating-a-python-script)

    import sys
    sys.exit()

### foo is None 和 foo == None的区别

问题 [链接](http://stackoverflow.com/questions/26595/is-there-any-difference-between-foo-is-none-and-foo-none)

    if foo is None: pass
    if foo == None: pass

如果比较相同的对象实例，is总是返回True
而 == 最终取决于 "__eq__()"

    >>> class foo(object):
        def __eq__(self, other):
            return True

    >>> f = foo()
    >>> f == None
    True
    >>> f is None
    False

    >>> list1 = [1, 2, 3]
    >>> list2 = [1, 2, 3]
    >>> list1==list2
    True
    >>> list1 is list2
    False

另外

    (ob1 is ob2) 等价于 (id(ob1) == id(ob2))



### 如何在循环中获取下标

问题 [链接](http://stackoverflow.com/questions/522563/accessing-the-index-in-python-for-loops)

使用enumerate

    for idx, val in enumerate(ints):
        print idx, val

### python中如何将一行长代码切成多行

问题 [链接](http://stackoverflow.com/questions/53162/how-can-i-do-a-line-break-line-continuation-in-python)

例如：

    e = 'a' + 'b' + 'c' + 'd'
    变成
    e = 'a' + 'b' +
        'c' + 'd'

括号中，可以直接换行

    a = dostuff(blahblah1, blahblah2, blahblah3, blahblah4, blahblah5,
                blahblah6, blahblah7)


非括号你可以这么做

    a = '1' + '2' + '3' + \
        '4' + '5'
    或者
    a = ('1' + '2' + '3' +
        '4' + '5')

可以查看下代码风格： [style guide](http://www.python.org/dev/peps/pep-0008/)
推荐是后一种，但某些个别情况下，加入括号会导致错误

### 为何1 in [1,0] == True执行结果是False

问题 [链接](http://stackoverflow.com/questions/9284350/why-does-1-in-1-0-true-evaluate-to-false)

有如下

    >>> 1 in [1,0]             # This is expected
    True
    >>> 1 in [1,0] == True     # This is strange
    False
    >>> (1 in [1,0]) == True   # This is what I wanted it to be
    True
    >>> 1 in ([1,0] == True)   # But it's not just a precedence issue!
                               # It did not raise an exception on the second example.

    Traceback (most recent call last):
      File "<pyshell#4>", line 1, in <module>
          1 in ([1,0] == True)
          TypeError: argument of type 'bool' is not iterable

这里python使用了比较运算符链

    1 in [1,0] == True

将被转为

    (1 in [1, 0]) and ([1, 0] == True)

很显然是false的

同样的

    a < b < c

会被转为

    (a < b) and (b < c) # b不会被解析两次

[具体文档](http://docs.python.org/2/reference/expressions.html#not-in)

### Python中的switch替代语法

问题 [链接](http://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python)

python中没有switch，有什么推荐的处理方法么

使用字典:

    def f(x):
        return {
            'a': 1,
            'b': 2,
        }.get(x, 9)

Python Cookbook中的几种方式

[Readable switch construction without lambdas or dictionaries](http://code.activestate.com/recipes/410692/)

[Exception-based Switch-Case](http://code.activestate.com/recipes/410695/)

[Using a Dictionary in place of a 'switch' statement](http://code.activestate.com/recipes/181064/)


### 使用 'if x is not None' 还是'if not x is None'

问题 [链接](http://stackoverflow.com/questions/2710940/python-if-x-is-not-none-or-if-not-x-is-none)

我总想着使用 'if not x is None' 会更加简明

但是google的Python风格指南使用的却是 'if x is not None'

性能上没有什么区别，他们编译成相同的字节码

    Python 2.6.2 (r262:71600, Apr 15 2009, 07:20:39)
    >>> import dis
    >>> def f(x):
    ...    return x is not None
    ...
    >>> dis.dis(f)
    2           0 LOAD_FAST                0 (x)
                3 LOAD_CONST               0 (None)
                6 COMPARE_OP               9 (is not)
                9 RETURN_VALUE
    >>> def g(x):
    ...   return not x is None
    ...
    >>> dis.dis(g)
    2           0 LOAD_FAST                0 (x)
                3 LOAD_CONST               0 (None)
                6 COMPARE_OP               9 (is not)
                9 RETURN_VALUE

在风格上，我尽量避免 'not x is y' 这种形式，虽然编译器会认为和 'not (x is y)'一样，但是读代码的人或许会误解为 '(not x) is y'

如果写作 'x is not y' 就不会有歧义

最佳实践

    if x is not None:
        # Do something about x

### 在非创建全局变量的地方使用全局变量

问题 [链接](http://stackoverflow.com/questions/423379/using-global-variables-in-a-function-other-than-the-one-that-created-them)

如果我在一个函数中创建了全局变量，如何在另一个函数中使用？

回答：

你可以在给全局变量赋值的函数中声明 global

    globvar = 0

    def set_globvar_to_one():
        global globvar    # Needed to modify global copy of globvar
        globvar = 1

    def print_globvar():
        print globvar     # No need for global declaration to read value of globvar

    set_globvar_to_one()
    print_globvar()       # Prints 1

我猜想这么做的原因是，全局变量很危险，Python想要确保你真的知道你要对一个全局的变量进行操作

如果你想知道如何在模块间使用全局变量，查看其他回答

### 如何检测一个变量是否存在

问题 [链接](http://stackoverflow.com/questions/843277/how-do-i-check-if-a-variable-exists-in-python)

我想检测一个变量是否存在，我现在是这么做的

    try:
        myVar
    except NameError:
        # Doint smth

存在其他不是使用exception的方式么？

回答


检测本地变量

    if 'myVar' in locals():
        # myVar exists.

检测全局变量

    if 'myVar' in globals():
        # myVar exists.

检测一个对象是否包含某个属性

    if hasattr(obj, 'attr_name'):
        # obj.attr_name exists.

### Python中是否存在三元运算符

问题 [链接](http://stackoverflow.com/questions/394809/does-python-have-a-ternary-conditional-operator)

三元运算在Python2.5中被加入

    a if test else b

使用

    >>> 'true' if True else 'false'
    'true'
    >>> 'true' if False else 'false'
    'false'

官方文档：

[Conditional expressions](https://docs.python.org/3/reference/expressions.html#conditional-expressions)

[Is there an equivalent of C’s ”?:” ternary operator?](https://docs.python.org/3.3/faq/programming.html#is-there-an-equivalent-of-c-s-ternary-operator)


### Python中的do-while

问题 [链接](http://stackoverflow.com/questions/743164/do-while-loop-in-python)

实现方法

    while True:
        stuff()
        if fail_condition:
            break

或者

    stuff()
    while not fail_condition:
        stuff()

### 相对于range() 应该更倾向于实用xrange()?

问题 [链接](http://stackoverflow.com/questions/135041/should-you-always-favor-xrange-over-range) 

why or why not?

就性能而言, 特别是当你迭代一个大的range, xrange()更优. 但是, 有一些情况下range()更优

- 在Python3中, range() 等价于 python2.x的 xrange(), 而xrange()不存在了.(如果你的代码将在2和3下运行, 不能使用xrange)

- range()在某些情况下更快, 例如, 多次重复遍历同一个序列. 

- xrange()并不适用于所有情况, 例如, 不支持slices以及任意的list方法


### 在Python中，“i += x”和“i = i + x”什么时候不等

问题[链接](http://stackoverflow.com/questions/15376509/when-is-i-x-different-from-i-i-x-in-python)

这完全取决于i这个对象。

`+=`调用了[`__iadd__`方法](https://docs.python.org/2/reference/datamodel.html#object.__iadd__)（如果存在—不存在就退一步调用`__add__`），然而`+`调用[`__add__`方法]（https://docs.python.org/2/reference/datamodel.html#object.__add__)^1

从一个API的角度，`__iadd__`期望被使用在恰当的位置修改易变的对象（返回的对象也是转变后的），而`__add__`应该返回某些东西的一个新的实例。对于不可变对象，两种方法都返回新的实例，但`__iadd__`会把新的实例放在和旧实例名字相同的命名空间里。这就是为什么

    i = 1
    i += 1

看上去增量`i`，实际上，你得到了一个新的数值，并且转移到了`i`的最上面—丢掉了旧的数值的引用。在这种情况下，`i += 1`和`i = i + 1`是完全一样的。但是，对于大多数可变对象，这是完全不同的：

一个具体的例子：

    a = [1, 2, 3]
    b = a
    b += [1, 2, 3]
    print a  #[1, 2, 3, 1, 2, 3]
    print b  #[1, 2, 3, 1, 2, 3]

对比一下：

    a = [1, 2, 3]
    b = a
    b = b + [1, 2, 3]
    print a #[1, 2, 3]
    print b #[1, 2, 3, 1, 2, 3]

注意第一个例子，从`b`和`a`代表相同的对象开始，当我对`b`使用`+=`，实际上它改变了`b`（`a`看起来也改变了- -毕竟他们代表同一个列表）。但是在第二个例子里，当我进行`b = b + [1, 2, 3]`操作时，b被引用并且和一个新的列表`[1, 2, 3]`联系了起来。之后在b的命名空间保存了这个关联的列表- -不考虑b之前的序列。