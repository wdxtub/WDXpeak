# Python Study Note

## 基础知识

**1.使用glob模块可以用通配符的方式搜索某个目录下的特定文件，返回结果是一个list**

```python
import glob
flist=glob.glob('*.jpeg')
```

使用os.getcwd()可以得到当前目录，如果想切换到其他目录，可以使用os.chdir('str/to/path')，如果想执行Shell脚本，可以使用os.system('mkdir newfolder')。

对于日常文件和目录的管理, shutil模块提供了更便捷、更高层次的接口

```python
import shutil
shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')
```

使用PyCharm中，在一个Project中新建一个Directory和新建一个Package之后，IDE都会创建对应的目录，并添加默认的__init__.py文件，但是，两者还是不一样的。

如果在它们的目录下各新建一个python脚本测试输出os.getcwd()，如果是在Directory中得到的是Project的根目录’/Users/hujiawei/PycharmProjects/leetcodeoj’；如果是在Package中得到的是Package的根目录，如’/Users/hujiawei/PycharmProjects/leetcodeoj/pypackage’。

**2.如果要在代码中添加中文注释的话，最好在文档开头加上下面的编码声明语句。**

关于Python中的字符串编码可见廖雪峰的python教程。若代码打算用在国际化的环境中, 那么不要使用奇特的编码。Python 默认的 UTF-8, 或者甚至是简单的 ASCII 在任何情况下工作得最好。同样地，如果代码的读者或维护者只有很小的概率使用不同的语言，那么不要在标识符里使用非 ASCII 字符。

```
# coding=utf-8
或者
# -*- coding: utf-8 -*-
```

**3.关于Python中的变量**


在Python中，变量名类似`__xxx__`的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用`__name__`、`__score__`这样的变量名。

有些时候，你会看到以一个下划线开头的实例变量名(两个下划线开头的也一样算，其实任何以下划线开头的都算)，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。

双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问`__name`是因为Python解释器对外把`__name`变量改成了`_Student__name`，所以，仍然可以通过`_Student__name`来访问`__name`变量。但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把`__name`改成不同的变量名。

总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。

上面说的有点绕，下面我写了两个python脚本，大家可以对照看下哪些能够访问，哪些不能，不能的情况下如何操作变得可以访问(注释后面的yes和no表示能不能被访问)。

也就是说，默认呢，以一个下划线开始(不论结尾有没有下划线)的变量在外部都是可以直接访问的，但是不推荐这么做；以两个下划线开始和两个下划线结束的变量属于特殊变量，可以直接访问；而以两个下划线开始且结尾不是两个下划线(可以没有也可以有一个下划线)的变量属于私有变量，不能直接访问，虽然可以通过其他方式访问，但最好不要在外部访问。

文件APythonTestA.py

```python
# coding=utf-8

class ListNode:

    _class_field10 = 'node class field 1-0'
    _class_field11_ = 'node class field 1-1'
    _class_field12__ = 'node class field 1-2'

    __class_field20 = 'node class field 2-0'
    __class_field21_ = 'node class field 2-1'
    __class_field22__ = 'node class field 2-2'

    def __init__(self, x):
        self.val = x
        self.next = None

_class_field10 = 'node class field 1-0'
_class_field11_ = 'node class field 1-1'
_class_field12__ = 'node class field 1-2'

__class_field20 = 'node class field 2-0'
__class_field21_ = 'node class field 2-1'
__class_field22__ = 'node class field 2-2'
```

文件APythonTestB.py

```python
# coding=utf-8
__author__ = 'hujiawei'
__doc__ = 'for python test 2'

import APythonTestA

if __name__ == '__main__':
    print(dir(APythonTestA.ListNode))
    node = APythonTestA.ListNode(4)
    # print(node._ListNode__class_field20) #yes
    print(node._class_field10) #yes
    print(node._class_field11_) #yes
    print(node._class_field12__) #yes
    # print(node.__class_field20) #no
    print(node._ListNode__class_field20)#yes
    # print(node.__class_field21_) #no
    print(node._ListNode__class_field21_)#yes
    print(node.__class_field22__) #yes

    print(dir(APythonTestA))
    print(APythonTestA._class_field10) #yes
    print(APythonTestA._class_field11_) #yes
    print(APythonTestA._class_field12__) #yes
    print(APythonTestA.__class_field20) #yes
    print(APythonTestA.__class_field21_) #yes
    print(APythonTestA.__class_field22__) #yes

# ['_ListNode__class_field20', '_ListNode__class_field21_', '__class_field22__', '__doc__', '__init__', '__module__', '_class_field10', '_class_field11_', '_class_field12__']
# node class field 1-0
# node class field 1-1
# node class field 1-2
# node class field 2-0
# node class field 2-1
# node class field 2-2
# ['ListNode', '__builtins__', '__class_field20', '__class_field21_', '__class_field22__', '__doc__', '__file__', '__name__', '__package__', '_class_field10', '_class_field11_', '_class_field12__']
# node class field 1-0
# node class field 1-1
# node class field 1-2
# node class field 2-0
# node class field 2-1
# node class field 2-2
```

**4.关于Python中函数的参数，摘自廖雪峰的python教程**

Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，运行会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

`*args`是可变参数，args接收的是一个tuple；

`**kw`是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过`*args`传入：`func(*(1, 2, 3))；`

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过`**kw`传入：`func(**{'a': 1, 'b': 2})`。

使用`*args`和`**kw`是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

**5.关于Python的高级特性，参见廖雪峰的python教程**

切片，迭代，列表生成式，生成器

除非特殊的原因，应该经常在代码中使用生成器表达式。但除非是面对非常大的列表，否则是不会看出明显区别的。

使用生成器得到当前目录及其子目录中的所有文件的代码，下面代码来自伯乐在线-python高级编程技巧

```python
import os
def tree(top):
    #path,folder list,file list
    for path, names, fnames in os.walk(top):
        for fname in fnames:
            yield os.path.join(path, fname)

for name in tree(os.getcwd()):
    print name
```

另一个使用生成器的代码示例：

```python
num = [1, 4, -5, 10, -7, 2, 3, -1]

def square_generator(optional_parameter):
    return (x ** 2 for x in num if x > optional_parameter)

print square_generator(0)
# <generator object <genexpr> at 0x004E6418>

# Option I
for k in square_generator(0):
    print k
# 1, 16, 100, 4, 9

# Option II
g = list(square_generator(0))
print g
# [1, 16, 100, 4, 9]
```

**6.关于Python的函数式编程，参见廖雪峰的python教程，讲解得很好**

高阶函数(使用函数作为参数或者返回一个函数的函数称为高阶函数)，匿名函数(lambda)，装饰器(decorator)和偏函数

用来测试一个函数花费的运行时间的装饰器，当然你也可以使用其他的方式，比如Timer来得到运行时间。下面代码来自伯乐在线-python高级编程技巧

```python
def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

@timethis
def countdown(n):
    while n > 0:
        n -= 1
```

其中代码

```python
@timethis
def countdown(n):
```

就相当于：

```python
def countdown(n):
...
countdown = timethis(countdown)
```

装饰器除了可以使用函数实现，也可以使用类来实现。

对装饰器的类实现的唯一要求是它必须能如函数一般使用，也就是说它必须是可调用的。所以，如果想这么做这个类必须实现`__call__`方法。

```python
class decorator(object):

    def __init__(self, f):
        print("inside decorator.__init__()")
        f() # Prove that function definition has completed

    def __call__(self):
        print("inside decorator.__call__()")

@decorator
def function():
    print("inside function()")

print("Finished decorating function()")

function()

# inside decorator.__init__()
# inside function()
# Finished decorating function()
# inside decorator.__call__()
```

1. 语法糖@decorator相当于function=decorator(function)，在此调用decorator的`__init__`打印`inside decorator.__init__()`
2. 随后执行f()打印`inside function()`
3. 随后执行“print(“Finished decorating function()”)”
4. 最后再调用function函数时，由于使用装饰器包装，因此执行decorator的`__call__`打印 `inside decorator.__call__()`。

我觉得上面代码不是一般的使用方式，实际装饰器类应该是在`__init__`方法中设置好自己内部的函数f，然后在方法`__call__`中调用函数f，并包含一些其他的方法调用，大概如下：

```python
class decorator(object):

    def __init__(self, f):
        print("inside decorator.__init__()")
        # f() # Prove that function definition has completed
        self.f=f

    def __call__(self):
        print("inside decorator.__call__() begin")
        self.f()
        print("inside decorator.__call__() end")

@decorator
def function():
    print("inside function()")

print("Finished decorating function()")

function()

# inside decorator.__init__()
# Finished decorating function()
# inside decorator.__call__() begin
# inside function()
# inside decorator.__call__() end
```

再提供一个装饰器的例子，实现自顶向下的带备忘录的DP算法来解决斐波那契数列求值，来源于Python Algorithms- Mastering Basic Algorithms in the Python Language

```python
from functools import wraps

def memo(func):
    cache={}
    @wraps(func)
    def wrap(*args):
        if args not in cache:
            cache[args]=func(*args)
        return cache[args]
    return wrap

@memo
def fib(i):
    if i<2: return 1
    return fib(i-1)+fib(i-2)

print(fib(100))
```

**7.Python中的值传递和引用传递**

python函数传递的是对象的引用值，非传值或传引用。但是如果对象是不可变的，感觉和c语言中传值差不多。如果对象是可变的，感觉和c语言中传引用差不多。

运行下面的代码就清楚了

```python
def foo(a):
    print "传来是对象的引用对象地址为{0}".format(id(a))
    a = 3 #形式参数a是局部变量，a重新绑定到3这个对象。
    print "变量a新引用对象地址为{0}".format(id(a))
    # print a

x = 5
print "全局变量x引用的对象地址为{0}".format(id(x))
foo(x)
print "变量x新引用对象地址为{0}".format(id(x))
print x
#由于函数内部a绑定到新的对象，也就修改不了全局变量x引用的对象5
# 全局变量x引用的对象地址为140462615725816
# 传来是对象的引用对象地址为140462615725816
# 变量a新引用对象地址为140462615725864
# 变量x新引用对象地址为140462615725816
# 5


def foo(a):
    """在函数内部直接修改了同一个引用指向的对象。
    也就修改了实际参数传来的引用值指向的对象。
    """
    a.append("can change object")
    return a

lst = [1,2,3]
print foo(lst)
print lst
#[1, 2, 3, 'can change object']
#[1, 2, 3, 'can change object']


def foo(a):
    """实际参数传来一个对象[1,2,3]的引用，当时形式参数
    （局部变量a重新引用到新的对象，也就是说保存了新的对象）
    当然不能修改原来的对象了。
    """
    a = ["python","java"]
    return a

lst = [1,2,3]
for item in foo(lst):
    print item
print lst
# python
# java
```

**8.其他**

(1)Python中set([1,2,3])是一个set，{1,2,3,4,5}也是一个set，{1:2,2:4,3:6,4:8,5:10}是一个dict，而且空的{}是一个dict！

set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错。


## 数据结构

[Problem Solving with Python](http://interactivepython.org/courselib/static/pythonds/index.html)


## 开始之前

Pythonic 是一种编程风格，崇尚优雅、明确、简单

> 如果能用同一种方法来做一件事情，为什么要变来变去？

## 环境配置

先安装最新版本的 python，我用 2.x 的

    brew install python

然后再创建一个专用目录，比如叫做：~/.virtualenvs，用于保存python的开发环境信息。

    mkdir ~/.virtualenvs
    cd ~/.virtualenvs

接下来，通过pip包（类似于Ruby中的gem、R中的cran，Python中的包管理机制），安装Python虚拟环境库virtualenv

    pip install virtualenv

然后，假设我们要开发项目，创建一个该项目专用开发环境，假设命名为：myproject

    virtualenv myproject

创建成功之后，我们会发现，在我们上一步创建的~/python目录下面就多了一个myproject/bin/python的目录，相关第三方包等内容以后都回下载在这里。我们只需要激活该环境即可：

    source ~/.virtualenvs/myproject/bin/activate

这样所有的库依赖的环境就是这个单独的，而不影响本机

## 算术、字符串与变量

基本的加减乘数都支持，有以下几个需要注意一下

+ ** 阶乘
+ // 整除，丢弃小数点后面的值
+ 对整数长度没有限制
+ 浮点运算不是准确值
+ 浮点数可能会溢出
+ 一般而言优先使用整数而不是浮点数，更精确也不会溢出
+ 支持复数，1j表示-1的平方根

### 其他数学函数

+ ceil(x) 大于或等于 x 的整数
+ cos(x)
+ degrees(x) 弧度转换为度数
+ exp(x) e 的 x 次方
+ factorial(n) n 的阶乘
+ log(x) e 为底数 x 的对数
+ log(x, b)
+ pow(x, y) x 的 y 次方
+ radians(x) 度数转换为弧度
+ sin(x)
+ sqrt(x)
+ tan(x)

### 导入模块

以 math 模块为例子

    import math

这样的话，使用函数需要加上 math：`math.sqrt(5)`

或者可以

    from math import *

这样的话就无需加上 math: `sqrt(5)`

+ 使用第二种方式时如果有同名函数会被覆盖
+ 第一种方式更加安全

### 字符串

+ 单引号
+ 双引号
+ 三引号：多行字符串

字符串的长度：`len(s)`，返回的是一个整数。

字符串可以用 `+` 来进行拼接，如果需要重复拼接，可以使用 `*`，例如

    $  3 * 'hee' + 2 * "!"
    heeheehee!!

### 获取帮助

+ 导入模块后，可使用 `dir(m)` 列出模块的所有函数
+ 使用 `help(f)` 来查看帮助
+ 打印文档字符串 `print(math.tanh.__doc__`

### 类型转换

+ 整形/字符串->浮点 `float(x)`
+ 整形/浮点->字符串 `str(n)`
+ 浮点->整形 `int(x)`
+ 字符串->浮点/整形 `float(s)` or `int(s)`

### 变量

命名规则

+ 变量名长度不受限制
+ 第一个字符不能是数字
+ 区分大小写
+ 关键字保留

注意

+ 赋值时不复制，只是标记和重新标记既有值，因此效率很高
+ 数字和字符串是不可变的，看起来是在修改，其实是在创建拷贝
+ 可以多重赋值 `x, y, z = 1, 'two', 3.0`
    * 可以利用这个交换两个变量的值 `a, b = b, a`

## 编写程序

+ 输入字符串 `str = input('hint message')`
+ 删掉开头和结尾多余的空格 `.strip()`
+ 首字母大写 `.capitalize()`
+ 打印字符串会自动在字符串之间加空格 `print ('jack', 'ate', 'no', 'fat')`
+ 需要指定分隔符 `print ('jack', 'ate', 'no', 'fat', sep = '.')`
+ 默认会加一个换行，如果不需要的话 `print ('haha', end = '')`
+ 使用注释指出输入、处理和输出部分

### 流程控制

+ 逻辑运算符：not, and, or, ==
+ 布尔值：True, False
+ 短路求值

if/else

    if cond:
        true_block
    elif cond:
        another_block
    else:
        false_block

for

    for i in range(5, 10):
        print(i)
    $  5, 6, 7, 8, 9
    for i in range(10, 5, -1):
        print(i)
    $  10, 9, 8, 7, 6

while

    while i < 10:
        print(i)

+ 尽量使用 for 循环，仅在万不得已时才使用 while
+ 用 break 跳出循环，用 continue 跳过某一次循环(但建议尽量不要使用)

## 函数

+ 函数是一大块可重用的代码
+ 即使函数没有参数，也要加上圆括号
+ 函数外面声明的变量称为全局变量
+ 任何 Python 程序中通常都应该有一个 `main()` 函数，作为程序的起点
+ Python 不支持按值传递，全是按引用
+ 默认参数很方便 `def greeting(name, greeting = 'hello'`
+ **只在第一次调用时给默认参数赋值，在复杂的程序中这可能成为微妙 bug 的根源**

## 模块

+ 模块是一系列相关的函数和变量
+ 模块有自己的名称空间(不同的文件名就是不同的名称空间)
+ 复活节彩蛋 `import this`

## 字符串

+ 使用字符串索引以类似数组下标的方式访问字符串元素
+ 负数索引：从右往左表示，第一个数是 -1
+ 获取字符编码 `ord('a')`
+ 获取对应字符 `chr(97)`

一些转义字符

+ \\ 反斜杠
+ \' 单引号
+ \" 双引号
+ \n 换行
+ \r 回车
+ \t tab

### 字符串切片

    food = 'apple-pie'
    food[0:5]
    $  apple
    food[6:9]
    $  pie

+ 如果省略切片的起始索引，则默认为0，如果省略终止索引，则默认为末尾。
+ 同样可以使用负数，但是比较难懂

### 测试函数

下面都返回 True/False -> 布尔函数/谓词

+ s.endswith(t) 以字符串 t 结尾
+ s.startswith(t) 以字符串 t 打头
+ s.isalnum() 只包含字母或数字
+ s.isalpha() 只包含字母
+ s.isdecimal() 只包含十进制数字字符
+ s.isdigit() 只包含数字字符
+ s.isidentifier() 是合法的标识符
+ s.islower() 只包含小写字母
+ s.isnumeric() 只包含数字
+ s.isprintable() 只包含可打印字符
+ s.isspace() 只包含空白字符
+ s.istitle() 大小写符合头衔要求的字符串
+ s.isupper() 只包含大写字母
+ t in s 字符串 s 包含字符串 t

### 搜索函数

find 和 index 的差别在于没有找到字符串处理不同

+ s.find(t) 如果没有找到返回-1，找到则返回起始位置
+ s.rfind(t) 同上，从右往左搜索
+ s.index(t) 同上，找不到会引发 ValueError 异常
+ s.rindex(t) 同上，从右往左搜索

### 改变大小写的函数

注意这些都是创建并返回一个新的字符串

+ s.capitalize() 第一个字母改为大写
+ s.lower() 变小写
+ s.upper() 变大写
+ s.swapcase() 大写小写交换
+ s.title() 符合头衔的要求

### 设置格式的函数

用来美化字符串

+ s.center(n, ch) 一共 n 个字符，s 居中，两边用 ch 填充
+ s.ljust(n, ch) 一共 n 个字符，s 左边，右用 ch 填充
+ s.rjust(n, ch) 一共 n 个字符，s 右边，左用 ch 填充
+ s.format(vars) 类似于 printf 的输出
    * `'{0} likes {1}'.format('Jack', 'Rose')`

### 剥除函数

去掉多余字符的

+ s.strip(ch) 左右都去掉包含在ch中的字符
+ s.lstrip(ch) 左都去掉包含在ch中的字符
+ s.rstrip(ch) 右都去掉包含在ch中的字符

### 拆分函数

+ s.partition(t) 将 s 拆分成三个字符串(head, t, tail)
+ s.rpartition(t) 同上，从右边搜索
+ s.split(t) 以 t 为分隔符，返回列表
+ s.rsplit(t) 同上，从右边开始
+ s.splitlines 返回一个由 s 中的各行组成的列表

### 替换函数

同样也可以用来删除不要的子串

+ s.replace(old, new) 用 new 替换 old
+ s.expandtabs(n) 将 tab 替换成 n 个空格

### 其他函数

+ s.count(t) t 在 s 中出现的次数
+ s.encode() 设置 s 的编码
+ s.join(seq) 使用 s 将 seq 中的字符串连接成一个字符串
+ s.maketrans(old, new) 创建一个转换表
+ s.translate(table) 用指定转换表替换
+ s.zfill(width) 左边添加足够多的0，让字符串长度为 width

## 正则表达式

+ `?` -> 左边的字符是可选的
+ `|` -> 或者
+ `*` -> 0-无穷个
+ `+` -> 1-无穷个

    re.match(regex,s) 在 regex 与 s 不匹配时返回 None，否则返回一个特殊的正则表达式匹配对象

还有很多技巧，这里暂时不展开

## 数据结构

+ type 用来检查类型
+ 序列一共三种：字符串、元组和列表，都有如下特征
    * 最左索引为0
    * 最右索引为-1
    * 可以切片
    * 可以用 `+` 和 `*` 拼接，但类型要一样
    * len 计算包含的元素个数
    * x in s 检查 s 是否包含 x
+ 元组用圆括号括起，元素用逗号分隔，元组不可变
    * x in tup 检查是否是其中一个元组
    * len(tup) 个数
    * tup.count(x) x 出现次数
    * tup.index(x) 第一次出现的索引，若没有则 ValueError 异常
+ 列表用方括号括起，元素用逗号分隔，是可变的
    * 列表元素指向某个值，而不是包含它们
    * 列表的某个元素甚至可以指向这个列表本身！
    * s.append(x)
    * s.count(x)
    * s.extend(lst) 合并列表
    * s.index(x)
    * s.insert(i, x)
    * s.pop(i)
    * s.remove(x)
    * s.reverse() 是就地完成的，不需要额外的空间
    * s.sort() 升序排列，就地完成
    * 如果要降序，就 sort + reverse
+ 列表解析，特别的列表创建办法
    * $  `[n*n for n in range(1, 11)]`
    * $  `[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`
    * 一个常见的用途是用某种方式修改现有列表
    * $  `names = ['al', 'mei']`
    * $  `cap_names = [n.capitalize() for n in names]`
    * $  `['Al', 'Mei']`
    * 还可以用于剔除不想要的元素，比常规循环更简洁易读
    * $  `nums = [-1, 0, 1]`
    * $  `result = [n for n in nums if n > 0]`
    * $  `[1]`
+ 字典，存储键值对，可变，利用hash实现，key是唯一且不可变的，不能有两个相同的键值对
    * `color = {'red': 1, 'blue': 2}`
    * d.items()
    * d.keys()
    * d.values()
    * d.get(key)
    * d.pop(key)
    * d.popitem()
    * d.clear()
    * d.copy()
    * d.fromkeys(s, t) 创建一个新字典，key 来自 s, value 来自 t
    * d.setdefault(key, v) 如果 key 在字典中，返回其值，如果不在，返回 v 并添加这个键值对
    * d.update(e) 将 e 中的键值对添加到字典中
+ 集合，不重复的元素，只包含 key
    * set 可变或者不可变

## 输入输出

+ 字符串插入，类似于 C 语言
    * `print('value: %.2f' % x)`
+ 转换说明符
    * d 整数
    * o 八进制
    * x 小写十六
    * X 大写十六
    * e 小写科学
    * E 大写科学
    * F 浮点
    * s 字符串
    * % %字符
+ 命名替换可读性极佳
    * `My {pet} has {prob}.format(pet = 'dog', prob = 'fleas')`
+ 读写文件，r'filepath'可以用原始字符串而不用转义符号
+ 当前工作目录，如果没有指定的话，就是这个文件的所在位置
+ 检查文件和文件夹
    * os.getcwd() 当前工作目录
    * os.listdir(p) 返回列表，包含 p 中所有文件和文件夹
    * os.chdir(p) 设置当前目录
    * os.path.isfile(p)
    * os.path.isdir(p)
    * os.stat(fname) 文件信息

读取文本文件

    逐行读取文本文件
    def print_file(fname):
        f = open(fname, 'r')
        for line in f:
            print (line, end = '')
        f.close()

    整个读取文本文件
    def print_file(fname):
        f = open(fname, 'r')
        print(f.read())
        f.close()
    或者可以写成一行
    print(open(fname, 'r').read())

文件打开模式

+ r 读取
+ w 写入
+ a 文件末尾增加
+ b 二进制
+ t 文本模式
+ + 读写

写入文本文件

    def write_file():
        f = open('file.txt', 'w')
        f.write('Long long time ago.')

这里用 `w` 若已存在对应文件，则会删除源文件并新建，所以如果不想覆盖，先检查是否存在

将字符串插入到文件开头

    def insert_title(title, fname = 'file.txt'):
        f = open(fname, 'r+')
        temp = f.read()
        temp = title + '\n\n' + temp
        f.seek(0)
        f.write(temp)

处理二进制文件

    def is_gif(fname):
        f = open(fname, 'br')
        first4 = tuple(f.read(4))
        return first4 == (0x47, 0x49, 0x46, 0x38)
    gif 图像都以这四个字节开头

处理二进制文件方面，pickle 通常是一种方便得多的方式，可以让你轻松读写几乎任何数据结构

    def make_pickled_file():
        grades = {'alan' : [4, 8, 10, 10],
                  'tom'  : [7, 7, 7, 8]}
        outfile = open('grades.dat', 'wb')
        pickle.dump(grades, outfile)

    def get_pickled_data():
        infile = open('grades.dat','rb')
        grades = pickle.load(infile)
        return trades

## 异常处理

捕获异常，try 语句

    def get_age():
        while True:
            try:
                n = int(input('How old are you?'))
                return n
            except ValueError:
                print('Please enter an integer')
            except (TypeError, IOError):
                print('whatever i dont care)
            except:
                return 'error'
            finally:
                print('doing dirty work)

finally 代码块是肯定会执行的，所以通常用来善后。

with 语句会尽快完成工作，例如

    num = 1
    with open(fname, 'r') as f:
        for line in f:
            print (line)
            num = num + 1
    在 for 结束后会立即关闭文件

## 面向对象编程

### 类

    class Person:
        def __init__(self, name = '', age = 0):
            self._name = ''
            self._age = 0
        def __str__(self):
            print("Person('%s',%s)" % (self._name, self._age))

+ `__init__` 是初始化方法，创建对象时会自动调用，方法的第一个参数必须是 self，是一个指向自己本身的变量
+ `__str__` 用于生成对象的字符串表示
+ 在大多数类中，`__repr__` 与 `__str__` 相同

### Setter / Getter

    def set_age(self, age):
        if 0 < age <= 150:
            self._age = age

但这种方式明显比较麻烦，可以使用 `property decorator` 来解决这个问题

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if 0 < age <= 150:
            self._age = age

### 私有变量

虽然没有绝对意义上的私有变量，但是可以通过一些约定来尽可能避免，两个下划线

    self.__age
    若要直接访问
    p._Person__age

### 继承

    class Player(Person):
        pass

可以重写方法

### 多态

相同函数可以有不同的行为，与 c++ 的思想类似，不赘述

## Popular Package

+ PIL 图像处理
+ Django 类似 Ruby on Rails
+ Bottle 小型交互式网站框架
+ Pygame 2D 游戏
+ SciPy 科学计算
+ Twisted 网络编程库
+ PyPI 包索引


