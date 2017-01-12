# Python

收集的一些 python 的面试资料

## ExtendList

What will be the output of the code below? Explain your answer.

```python
def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3

```

How would you modify the definition of extendList to produce the presumably desired behavior?

### Solution

The output of the above code will be:

```
list1 = [10, 'a']
list2 = [123]
list3 = [10, 'a']
```

Many will mistakenly expect list1 to be equal to [10] and list3 to be equal to ['a'], thinking that the list argument will be set to its default value of [] each time extendList is called.

However, what actually happens is that the new default list is created only once when the function is defined, and that same list is then used subsequently whenever extendList is invoked without a list argument being specified. This is because expressions in default arguments are calculated when the function is defined, not when it’s called.

list1 and list3 are therefore operating on the same default list, whereas list2 is operating on a separate list that it created (by passing its own empty list as the value for the list parameter).

The definition of the extendList function could be modified as follows, though, to always begin a new list when no list argument is specified, which is more likely to have been the desired behavior:

```python
def extendList(val, list=None):
    if list is None:
        list = []
    list.append(val)
    return list
```

With this revised implementation, the output would be:

```
list1 = [10]
list2 = [123]
list3 = ['a']
```

## late binding

What will be the output of the code below? Explain your answer.

```python
def multipliers():
    return [lambda x : i * x for i in range(4)]
    
print [m(2) for m in multipliers()]
```

How would you modify the definition of multipliers to produce the presumably desired behavior?

### Solution

The output of the above code will be [6, 6, 6, 6] (not [0, 2, 4, 6]).

The reason for this is that Python’s closures are late binding. This means that the values of variables used in closures are looked up at the time the inner function is called. So as a result, when any of the functions returned by multipliers() are called, the value of i is looked up in the surrounding scope at that time. By then, regardless of which of the returned functions is called, the for loop has completed and i is left with its final value of 3. Therefore, every returned function multiplies the value it is passed by 3, so since a value of 2 is passed in the above code, they all return a value of 6 (i.e., 3 x 2).

(Incidentally, as pointed out in The Hitchhiker’s Guide to Python, there is a somewhat widespread misconception that this has something to do with lambdas, which is not the case. Functions created with a lambda expression are in no way special and the same behavior is exhibited by functions created using an ordinary def.)

Below are a few examples of ways to circumvent this issue.

One solution would be use a Python generator as follows:

```python
def multipliers():
     for i in range(4): yield lambda x : i * x 
```

Another solution is to create a closure that binds immediately to its arguments by using a default argument. For example:

```python
def multipliers():
    return [lambda x, i=i : i * x for i in range(4)]
```

Or alternatively, you can use the functools.partial function:

```python
from functools import partial
from operator import mul

def multipliers():
    return [partial(mul, i) for i in range(4)]
```

## class variables

What will be the output of the code below? Explain your answer.

```python
class Parent(object):
    x = 1

class Child1(Parent):
    pass

class Child2(Parent):
    pass

print Parent.x, Child1.x, Child2.x
Child1.x = 2
print Parent.x, Child1.x, Child2.x
Parent.x = 3
print Parent.x, Child1.x, Child2.x
```

### Solution

The output of the above code will be:

```
1 1 1
1 2 1
3 2 3
```

What confuses or surprises many about this is that the last line of output is 3 2 3 rather than 3 2 1. Why does changing the value of Parent.x also change the value of Child2.x, but at the same time not change the value of Child1.x?

The key to the answer is that, in Python, class variables are internally handled as dictionaries. If a variable name is not found in the dictionary of the current class, the class hierarchy (i.e., its parent classes) are searched until the referenced variable name is found (if the referenced variable name is not found in the class itself or anywhere in its hierarchy, an AttributeError occurs).

Therefore, setting x = 1 in the Parent class makes the class variable x (with a value of 1) referenceable in that class and any of its children. That’s why the first print statement outputs 1 1 1.

Subsequently, if any of its child classes overrides that value (for example, when we execute the statement Child1.x = 2), then the value is changed in that child only. That’s why the second print statement outputs 1 2 1.

Finally, if the value is then changed in the Parent (for example, when we execute the statement Parent.x = 3), that change is reflected also by any children that have not yet overridden the value (which in this case would be Child2). That’s why the third print statement outputs 3 2 3.

## python 2 / 3

What will be the output of the code below in Python 2? Explain your answer.

```python
def div1(x,y):
    print "%s/%s = %s" % (x, y, x/y)
    
def div2(x,y):
    print "%s//%s = %s" % (x, y, x//y)

div1(5,2)
div1(5.,2)
div2(5,2)
div2(5.,2.)
```

Also, how would the answer differ in Python 3 (assuming, of course, that the above print statements were converted to Python 3 syntax)?

### Solution

In Python 2, the output of the above code will be:

```
5/2 = 2
5.0/2 = 2.5
5//2 = 2
5.0//2.0 = 2.0
```

By default, Python 2 automatically performs integer arithmetic if both operands are integers. As a result, 5/2 yields 2, while 5./2 yields 2.5.

Note that you can override this behavior in Python 2 by adding the following import:

```python
from __future__ import division 
```

Also note that the “double-slash” (//) operator will always perform integer division, regardless of the operand types. That’s why 5.0//2.0 yields 2.0 even in Python 2.

Python 3, however, does not have this behavior; i.e., it does not perform integer arithmetic if both operands are integers. Therefore, in Python 3, the output will be as follows:

```
5/2 = 2.5
5.0/2 = 2.5
5//2 = 2
5.0//2.0 = 2.0
```

## IndexError

What will be the output of the code below?

```python
list = ['a', 'b', 'c', 'd', 'e']
print list[10:]
```

### Solution

The above code will output [], and will not result in an IndexError.

As one would expect, attempting to access a member of a list using an index that exceeds the number of members (e.g., attempting to access list[10] in the list above) results in an IndexError. However, attempting to access a slice of a list at a starting index that exceeds the number of members in the list will not result in an IndexError and will simply return an empty list.

What makes this a particularly nasty gotcha is that it can lead to bugs that are really hard to track down since no error is raised at runtime.

## List Tricks

Consider the following code snippet:

```
1. list = [ [ ] ] * 5
2. list  # output?
3. list[0].append(10)
4. list  # output?
5. list[1].append(20)
6. list  # output?
7. list.append(30)
8. list  # output?
```
 
What will be the ouput of lines 2, 4, 6, and 8? Explain your answer.

### Solution

The output will be as follows:

```
[[], [], [], [], []]
[[10], [10], [10], [10], [10]]
[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]]
[[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30]
```

Here’s why:

The first line of output is presumably intuitive and easy to understand; i.e., list = [ [ ] ] * 5 simply creates a list of 5 lists.

However, the key thing to understand here is that the statement list = [ [ ] ] * 5 does NOT create a list containing 5 distinct lists; rather, it creates a a list of 5 references to the same list. With this understanding, we can better understand the rest of the output.

list[0].append(10) appends 10 to the first list. But since all 5 lists refer to the same list, the output is: [[10], [10], [10], [10], [10]].

Similarly, list[1].append(20) appends 20 to the second list. But again, since all 5 lists refer to the same list, the output is now: [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20]].

In contrast, list.append(30) is appending an entirely new element to the “outer” list, which therefore yields the output: [[10, 20], [10, 20], [10, 20], [10, 20], [10, 20], 30].

## Selection

Given a list of N numbers, use a single list comprehension to produce a new list that only contains those values that are:
(a) even numbers, and
(b) from elements in the original list that had even indices

For example, if list[2] contains a value that is even, that value should be included in the new list, since it is also at an even index (i.e., 2) in the original list. However, if list[3] contains an even number, that number should not be included in the new list since it is at an odd index (i.e., 3) in the original list.

### Solution

A simple solution to this problem would be as follows

	[x for x in list[::2] if x%2 == 0]
For example, given the following list:

```
#        0   1   2   3    4    5    6    7    8
list = [ 1 , 3 , 5 , 8 , 10 , 13 , 18 , 36 , 78 ]
```

the list comprehension [x for x in list[::2] if x%2 == 0] will evaluate to:

	[10, 18, 78]

The expression works by first taking the numbers that are at the even indices, and then filtering out all the odd numbers.

## Subclass of dictionary

Given the following subclass of dictionary:

```python
class DefaultDict(dict):
    def __missing__(self, key):
        return []
```

Will the code below work? Why or why not?

```python
d = DefaultDict()
d['florp'] = 127
```

### Solution

Yes, it will work. With this implementation of the DefaultDict class, whenever a key is missing, the instance of the dictionary will automatically be instantiated with a list.

---

## == 和 is 的区别

Python 中的对象包括3要素，id(唯一标示), type(类型), value(值)

is 用来判断，a 对象是否是 b 对象，用id来判断

== 用来判断 a 对象的值是否与 b的值相同

## 说说你对zen of python的理解，你有什么办法看到它?

Python之禅,Python秉承一种独特的简洁和可读行高的语法，以及高度一致的编程模式，符合“大脑思维习惯”，使Python易于学习、理解和记忆。Python同时采用了一条极简主义的设计理念，了解完整的Python哲学理念，可以在任何一个Python交互解释器中键入import this命令，这是Python隐藏的一个彩蛋:描绘了一系列Python设计原则。如今已是Python社区内流行的行话"EIBTI"，明了胜于晦涩这条规则的简称. 在Python的思维方式中，明了胜于晦涩，简洁胜于复杂。

```python
>>> import this    
The Zen of Python, by Tim Peters    
    
Beautiful is better than ugly.    
Explicit is better than implicit.    
Simple is better than complex.    
Complex is better than complicated.    
Flat is better than nested.    
Sparse is better than dense.    
Readability counts.    
Special cases aren't special enough to break the rules.    
Although practicality beats purity.    
Errors should never pass silently.    
Unless explicitly silenced.    
In the face of ambiguity, refuse the temptation to guess.    
There should be one-- and preferably only one --obvious way to do it.    
Although that way may not be obvious at first unless you're Dutch.    
Now is better than never.    
Although never is often better than *right* now.    
If the implementation is hard to explain, it's a bad idea.    
If the implementation is easy to explain, it may be a good idea.    
Namespaces are one honking great idea -- let's do more of those!  
```

## 说说你对pythonic的看法，尝试解决下面的小问题

简洁，明了，严谨，灵活

```python
#交换两个变量值    
a,b = b,a    
    
#去掉list中的重复元素    
old_list = [1,1,1,3,4]    
new_list = list(set(old_list))    
    
#翻转一个字符串    
s = 'abcde'    
ss = s[::-1]    
    
#用两个元素之间有对应关系的list构造一个dict    
names = ['jianpx', 'yue']    
ages = [23, 40]    
m = dict(zip(names,ages))    
    
#将数量较多的字符串相连，如何效率较高，为什么    
fruits = ['apple', 'banana']    
result = ''.join(fruits)    
    
#python字符串效率问题之一就是在连接字符串的时候使用‘+’号，例如 s = ‘s1’ + ‘s2’ + ‘s3’ + ...+’sN’，总共将N个字符串连接起来， 但是使用+号的话，python需要申请N-1次内存空间， 然后进行字符串拷贝。原因是字符串对象PyStringObject在python当中是不可变 对象，所以每当需要合并两个字符串的时候，就要重新申请一个新的内存空间 （大小为两个字符串长度之和）来给这个合并之后的新字符串，然后进行拷贝。 所以用+号效率非常低。建议在连接字符串的时候使用字符串本身的方法 join（list），这个方法能提高效率，原因是它只是申请了一次内存空间， 因为它可以遍历list中的元素计算出总共需要申请的内存空间的大小，一次申请完。  
```

## 你调试python代码的方法有哪些?

+ 具体IDE都有调试，比如:IDLE, Eclipse+Pydev都可以设置断点调试。   
+ pdb模块也可以做调试。  
+ 还有PyChecker和Pylint  
+ PyChecker是一个python代码的静态分析工具，它可以帮助查找python代码的bug, 会对代码的复杂度和格式提出警告    

## 什么是GIL?

什么是GIL(Global Interpreter Lock)全局解释器锁? 简单地说就是:  

每一个interpreter进程,只能同时仅有一个线程来执行, 获得相关的锁, 存取相关的资源. 那么很容易就会发现,如果一个interpreter进程只能有一个线程来执行,多线程的并发则成为不可能, 即使这几个线程之间不存在资源的竞争.

从理论上讲,我们要尽可能地使程序更加并行, 能够充分利用多核的功能.  

## 对比一下dict中items与iteritems?

```python
>>> D = {'a':1,'b':2,'c':3,'d':4}    
>>> D.items()                       #一次性取出所有    
[('a', 1), ('c', 3), ('b', 2), ('d', 4)]    
>>> D.iteritems()                   #迭代对象，每次取出一个。用for循环遍历出来；    
<dictionary-itemiterator object at 0x00000000026243B8>    
>>> for i in D.iteritems():    
...   print i,    
...    
('a', 1) ('c', 3) ('b', 2) ('d', 4)    
>>> for k,v in D.iteritems():    
...   print k,    
...    
a c b d    
```

总结:   

1. 一般iteritems()迭代的办法比items()要快，特别是数据库比较大时。  
2. 在Python3中一般取消前者函数  

## 是否遇到过python的模块间循环引用的问题，如何避免它?

这是代码结构设计的问题，模块依赖和类依赖  
如果老是觉得碰到循环引用，很可能是模块的分界线划错地方了。可能是把应该在一起的东西硬拆开了，可能是某些职责放错地方了，可能是应该抽象的东西没抽象  
总之微观代码规范可能并不能帮到太多，重要的是更宏观的划分模块的经验技巧，推荐uml，脑图，白板等等图形化的工具先梳理清楚整个系统的总体结构和职责分工  
  
采取办法，从设计模式上来规避这个问题，比如: 
 
1. 使用 “__all__” 白名单开放接口  
2. 尽量避免 import  

## 有用过with statement吗？它的好处是什么？

```python
>>> with open('text.txt') as myfile:    
...   while True:    
...     line = myfile.readline()    
...     if not line:    
...       break    
...     print line,    
    
# with语句使用所谓的上下文管理器对代码块进行包装，允许上下文管理器实现一些设置和清理操作。    
# 例如：文件可以作为上下文管理器使用，它们可以关闭自身作为清理的一部分。    
# NOTE：在PYTHON2.5中，需要使用from __future__ import with_statement进行with语句的导入   
```

## 用Python生成指定长度的斐波那契数列

```python
def fibs(x):  
    result = [0, 1]  
    for index in range(x-2):  
        result.append(result[-2]+result[-1])  
    return result  
  
if __name__=='__main__':  
    num = input('Enter one number: ')  
    print fibs(num)  
```

## Python里如何生产随机数

```python
>>> import random  
>>> random.random()  
0.29495314937268713  
>>> random.randint(1,11)  
8  
>>> random.choice(range(11))  
3  
```

## Python里如何反序的迭代一个序列

如果是一个list, 最快的解决方案是：  
  
```python
list.reverse()  
try:  
    for x in list:  
        “do something with x”  
finally:  
    list.reverse()  
  
如果不是list, 最通用但是稍慢的解决方案是：  
for i in range(len(sequence)-1, -1, -1):  
x = sequence[i] 
```

## Python中如何定义一个函数

```python
def func(arg, *args, **kwagrs):   #普通函数  
    func_body  
    return   
  
lambda x: x **2                   #匿名函数 
```

## Python匹配HTML tag的时候，`<.*>`和`<.*?>`有什么区别

```python
import re  
s = ‘<html><head><title>Title</title>’  
print(re.match(‘<.*>’, s).group())  
  
会返回一个匹配<html><head><title>Title</title>而不是<html>  
  
而  
  
import re  
s = ‘<html><head><title>Title</title>’  
print(re.match(‘<.*?>’, s).group())  
  
则会返回<html>  
  
<.*>这种匹配称作贪心匹配 <.*?>称作非贪心匹配 
```

## Python里面search()和match()的区别

```python
>>> import re  
>>> re.match(r'python','Programing Python, should be pythonic')  
>>> obj1 = re.match(r'python','Programing Python, should be pythonic')  #返回None  
>>> obj2 = re.search(r'python','Programing Python, should be pythonic') #找到pythonic  
>>> obj2.group()  
'python'  
#re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；  
#re.search匹配整个字符串，直到找到一个匹配。  
```

## Python程序中文输出问题怎么解决

在Python3中，对中文进行了全面的支持，但在Python2.x中需要进行相关的设置才能使用中文。否则会出现乱码。
  
Python默认采取的ASCII编码，字母、标点和其他字符只使用一个字节来表示，但对于中文字符来说，一个字节满足不了需求。  

为了能在计算机中表示所有的中文字符，中文编码采用两个字节表示。如果中文编码和ASCII混合使用的话，就会导致解码错误，从而才生乱码。  

解决办法:  

+ 交互式命令中：一般不会出现乱码，无需做处理   
+ py脚本文件中：跨字符集必须做设置，否则乱码  

1.首先在开头一句添加:  

```
# coding = utf-8    
# 或    
# coding = UTF-8    
# 或    
# -*- coding: utf-8 -*-   
```

2.其次需将文件保存为UTF-8的格式！  
3.最后: s.decode('utf-8').encode('gbk') 
 
## 什么是lambda函数

函数使用:  

1. 代码块重复，这时候必须考虑到函数，降低程序的冗余度  
2. 代码块复杂，这时候必须考虑到函数，降低程序的复杂度  
3. 
Python有两种函数,一种是def定义，一种是lambda函数()  

当程序代码很短，且该函数只使用一次，为了程序的简洁，及节省变量内存占用空间，引入了匿名函数这个概念  

```python
>>> nums = range(2,20)  
>>> for i in nums:  
        nums = filter(lambda x:x==i or x % i,nums)  
>>> nums  
[2, 3, 5, 7, 11, 13, 17, 19]  
```
 
## 请写出一段Python代码实现删除一个list里面的重复元素

```python
>>> L1 = [4,1,3,2,3,5,1]  
>>> L2 = []  
>>> [L2.append(i) for i in L1 if i not in L2]  
>>> print L2  
[4, 1, 3, 2, 5]  
```

## Python是如何进行类型转换的

```python
>>> int('1234')                   # 将数字型字符串转为整形  
1234  
>>> float(12)                     # 将整形或数字字符转为浮点型  
12.0  
>>> str(98)                       # 将其他类型转为字符串型  
'98'  
>>> list('abcd')                  # 将其他类型转为列表类型  
['a', 'b', 'c', 'd']  
>>> dict.fromkeys(['name','age']) # 将其他类型转为字典类型  
{'age': None, 'name': None}  
>>> tuple([1, 2, 3, 4])           # 将其他类型转为元祖类型  
(1, 2, 3, 4)  
```

详细转换总结如下:

函数 |描述  
:--:|:--:
int(x [,base])          | 将x转换为一个整数  
long(x [,base] )        | 将x转换为一个长整数  
float(x)                | 将x转换到一个浮点数  
complex(real [,imag])   | 创建一个复数  
str(x)                  | 将对象 x 转换为字符串  
repr(x)                 | 将对象 x 转换为表达式字符串  
eval(str)               | 用来计算在字符串中的有效Python表达式,并返回一个对象  
tuple(s)                | 将序列 s 转换为一个元组  
list(s)                 | 将序列 s 转换为一个列表  
set(s)                  | 转换为可变集合  
dict(d)                 | 创建一个字典。d 必须是一个序列 (key,value)元组。  
frozenset(s)            | 转换为不可变集合  
chr(x)                  | 将一个整数转换为一个字符  
unichr(x)               | 将一个整数转换为Unicode字符  
ord(x)                  | 将一个字符转换为它的整数值  
hex(x)                  | 将一个整数转换为一个十六进制字符串  
oct(x)                  | 将一个整数转换为一个八进制字符串  

## 如何知道一个Python对象的类型

```python
>>> type([]);type('');type(0);type({});type(0.0);type((1,))  
<type 'list'>  
<type 'str'>  
<type 'int'>  
<type 'dict'>  
<type 'float'>  
<type 'tuple'>  
```

## Python里面如何拷贝一个对象

```python
切片S[:]  # 注不能应用于字典  
深浅拷贝  # 能应用于所有序列和字典  
```

1. 浅拷贝D.copy()方法  
2. 深拷贝deepcopy(D)方法  

## Python中pass语句的作用是什么

pass语句什么也不做,一般作为占位符或者创建占位程序  

## 写一段程序逐行读入一个文本文件，并在屏幕上打印出来

```python
f = open(filename)    
while True:    
    line = f.readline()    
    if not line: break    
    print(line)    
f.close()   
``` 

## 如何用Python删除一个文件

```python
import os  
os.remove(filename)  
```

## Python代码得到列表list的交集与差集

```python
>>> list1 = [1, 3, 4, 6]  
>>> list2 = [1, 2, 3, 4]  
>>> [i for i in list1 if i not in list2]  
[6]  
>>> [i for i in list1 if i in list2]  
[1, 3, 4]  
```

## Python是如何进行内存管理的
python内部使用引用计数，来保持追踪内存中的对象，Python内部记录了对象有多少个引用，即引用计数，当对象被创建时就创建了一个引用计数，当对象不再需要时，这个对象的引用计数为0时，它被垃圾回收。所有这些都是自动完成，不需要像C一样，人工干预，从而提高了程序员的效率和程序的健壮性。  

## 介绍一下Python下range()函数的用法

```python
>>> range(10)  
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  
>>> range(1, 10)  
[1, 2, 3, 4, 5, 6, 7, 8, 9]  
>>> range(0, 9, 2)  
[0, 2, 4, 6, 8]  
>>> range(99,0,-10)  
[99, 89, 79, 69, 59, 49, 39, 29, 19, 9]  
```

相区别的是xrange(),每次只取出一个迭代对象，如果是数据量比较大时，效率较高  

在Python3中，没有xrange()函数，其功能放在了range()函数上  

## Python异常处理


程序中出现异常情况时就需要异常处理。比如当你打开一个不存在的文件时。当你的程序中有一些无效的语句时，Python会提示你有错误存在。下面是一个拼写错误的例子，print写成了Print  

下面是异常最常见的几种角色  

```
1. 错误处理  
>>>可以在程序代码中捕捉和相应错误，或者忽略已发生的异常。  
>>>如果忽略错误，PYTHON默认的异常处理行为将启动:停止程序，打印错误信息。  
>>>如果不想启动这种默认行为，就用try语句来捕捉异常并从异常中恢复。  
2. 事件通知  
>>>异常也可用于发出有效状态的信号，而不需在程序间传递结果标志位。或者刻意对其进行测试  
3. 特殊情况处理  
>>>有时，发生了某种很罕见的情况，很难调整代码区处理。通常会在异常处理中处理，从而省去应对特殊情况的代码  
4. 终止行为  
>>>try/finally语句可确保一定会进行需要的结束运算，无论程序是否有异常  
5. 非常规控制流程 
``` 

## 介绍一下Python中的filter方法

filter就像map,reduce,apply,zip等都是内置函数，用C语言实现，具有速度快，功能强大等  
  
优点。  

用于过滤与函数func()不匹配的值, 类似于SQL中select value != 'a'  

相当于一个迭代器，调用一个布尔函数func来迭代seq中的每个元素，返回一个是bool_seq返回为True的序列  

```
>>>第一个参数: function or None, 函数或None  
>>>第二个参数: sequence,序列  
```

## 介绍一下except的用法和作用

```python
try/except:          捕捉由PYTHON自身或写程序过程中引发的异常并恢复  
except:              捕捉所有其他异常  
except name:         只捕捉特定的异常  
except name, value:  捕捉异常及格外的数据(实例)  
except (name1,name2) 捕捉列出来的异常  
except (name1,name2),value: 捕捉任何列出的异常，并取得额外数据  
else:                如果没有引发异常就运行  
finally:             总是会运行此处代码 
```
 
## 如何用Python来进行查询和替换一个文本字符串

```python
>>> words = 'Python is a very funny language!'  
>>> words.find('Python')             # 返回的为0或正数时，为其索引号  
0  
>>> words.find('is')  
7  
>>> words.find('dafa')               # 返回-1表示查找失败  
-1  
>>> words.replace('Python', 'Perl')  # replace()替换  
'Perl is a very funny language!' 
```
 
## Python如何copy一个文件

```python
import shutil  
shutil.copyfile('a.py', 'copy_a.py') 
```
 
## Python判断当前用户是否是root

```python
import os  
if os.getuid() != 0:    # root账号的uid=0  
    print os.getuid()  
    print 'Should run as root account'  
else:  
    print 'Hello, Root!' 
```
 
## 用Python写一个for循环的例子

for循环可以遍历序列(列表，字符串，元祖),range()及迭代对象，如xrange()  

```python
names = ['Alice', 'Betty', 'Fred', 'Tom']  
for index, name in enumerate(names):  
    print 'index:',index,'=>', name  
  
# 输出结果    
index: 0 => Alice  
index: 1 => Betty  
index: 2 => Fred  
index: 3 => Tom  
```

## 介绍一下Python中webbrowser的用法

+ webbrowser模块提供了一个高级接口来显示基于Web的文档，大部分情况下只需要简单的调用open()方法。  
+ webbrowser定义了如下的异常：exception webbrowser.Error, 当浏览器控件发生错误是会抛出这个异常  
  
webbrowser有以下方法：  
  
	webbrowser.open(url[, new=0[, autoraise=1]])  
  
这个方法是在默认的浏览器中显示url, 如果new = 0, 那么url会在同一个浏览器窗口下打开，如果new = 1, 会打开一个新的窗口，如果new = 2, 会打开一个新的tab, 如果autoraise ＝ true, 窗口会自动增长。  
  
	webbrowser.open_new(url)  

在默认浏览器中打开一个新的窗口来显示url, 否则，在仅有的浏览器窗口中打开url  
  
	webbrowser.open_new_tab(url)  

在默认浏览器中当开一个新的tab来显示url, 否则跟open_new()一样  
  
	webbrowser.get([name]) 

根据name返回一个浏览器对象，如果name为空，则返回默认的浏览器  
  
	webbrowser.register(name, construtor[, instance])  

注册一个名字为name的浏览器，如果这个浏览器类型被注册就可以用get()方法来获取。  

## 默写尽可能多的str对象的方法

方法 | 描述    
:--:|:--:   
S.capitalize()                   |  返回首字母大写的字符串的副本    
S.center(width[,fillchar])       |  返回一个长度为max(len(S),width),S居中，两侧fillchar填充    
S.count(sub[,start[,end]])       | 计算子字符串sub的出现次数，可将搜索范围限制为S[start:end]    
S.decode([encoding[,error]])     | 返回使用给定编码方式的字符串的解码版本，由error指定错误处理方式    
S.endswith(suffix[start[,end]])  | 检查S是否以suffix结尾，可给定[start:end]来选择匹配的范围    
S.expandtabs([tabsize])          | 返回字符串的副本，其中tab字符会使用空格进行扩展，可选择tabsize    
S.find(sun[,start[,end]])        | 返回子字符串sub的第一个索引，不存在则为-1,可选择搜索范围    
S.index(sub[,start[,end]])       | 返回子字符串sub的第一个索引，不存在则引发ValueError异常.    
S.isalnum()                      | 检查字符串是否由字母或数字字符组成    
S.isalpha()                      | 检查字符串是否由字母字符组成    
S.isdigit()                      | 检查字符串是否由数字字符组成    
S.islower()                      | 检查字符串是否由小写字母组成    
S.isspace()                      | 检查字符串是否由空格组成    
S.istitle()                      | 检查字符串时候首字母大写    
S.isupper()                      | 检查字符串是否由大写字母组成    
S.join(sequence)                 | 返回其中sequence的字符串元素由S连接的字符串    
S.ljust(width[,fillchar])        | 返回S副本左对齐的字符串,长度max(len(S),W),右侧fillchar填充    
S.lower()                        | 返回所有字符串都为小写的副本    
S.lstrip([char])                 | 向左移除所有char，默认移除(空格,tab,\n)    
S.partition(seq)                 | 在字符串中搜索seq并返回    
S.replace(old,new[,max])         | 将new替换olad,最多可替换max次    
S.rfind(sub[,start[,end]])       | 返回sub所在的最后一个索引，不存在则为-1,可定搜索范围S[start:end]    
S.rindex(sub[,start[,end]])      | 返回sub所在的最后一个索引，不存在则会引发ValueError异常。    
S.rjust(width[,fillchar])        | 返回S副本右对齐的字符串,长度max(len(S),W),左侧fillchar填充    
S.rpartition(seq)                | 同Partition,但从右侧开始查找    
S.rstip([char])                  | 向右移除所有char，默认移除(空格,tab,\n)    
S.rsplit(sep[,maxsplit])         | 同split,但是使用maxsplit时是从右往左进行计数    
S.split(sep[,maxsplit])          | 使用sep做为分割符,可使用maxsplit指定最大切分数    
S.zfill(width)                   | 在S的左侧以0填充width个字符    
S.upper()                        | 返回S的副本，所有字符大写    
S.splitlines([keepends])         | 返回S中所有行的列表，可选择是否包括换行符    
S.startswith(prefix[,start[,end]]) | 检查S是否以prefix开始，可用[start,end]来定义范围    
S.strip([chars])                 | 移除所有字符串中含chars的字符，默认移除(空格，tab,\n)    
S.swapcase()                     | 返回S的副本，所有大小写交换    
S.title()                        | 返回S的副本，所有单词以大写字母开头    
S.translate(table[,deletechars]) | 返回S的副本，所有字符都使用table进行的转换，可选择删除出现在deletechars中的所有字符    

## 现在有一个dict对象adict,里面包含了一百万个元素,查找其中的某个元素的平均需要多少次比较

O(1)  哈希字典，快速查找，键值映射，键唯一!  

## 有一个list对象alist，里面的所有元素都是字符串，编写一个函数对它实现一个大小写无关的排序

```python
words = ['This','is','a','dog','!']  
words.sort(key=lambda x:x.lower())  
print words  
#输出结果  
>>>   
['!', 'a', 'dog', 'is', 'This']  
```

## 有一个排好序地list对象alist，查找其中是否有某元素a

```python
alist = ['a','s','d','f']  
  
try:  
    alist.index('a')  
    print 'Find it.'  
except ValueError:  
    print 'Not Found.'  
 ```
 
## 请用Python写一个获取用户输入数字，并根据数字大小输出不同信息的脚本

```python
num = input('Enter number: ')  
  
if num > 100:  
    print 'The number is over 100'  
elif 0 < num <= 100:  
    print 'The number is between 0~100'  
elif num < 0:  
    print 'The number is negative.'  
else:  
    print 'Not a number'  
```

## 打乱一个排好序的list对象alist

```python
# random模块中的shuffle(洗牌函数)  
import random  
alist = [1, 2, 3, 4]  
random.shuffle(alist)     
print alist 
```
 
## 有二维的list对象alist，假定其中的所有元素都具有相同的长度，写一段程序根据元素的第二个元素排序

```python
def sort_lists(lists, sord, idx):  
    if sord == 'desc':  
        lists.sort(key=lambda x:x[idx], reverse=True)  
    else:  
        lists.sort(key=lambda x:x[idx])  
    return lists  
lists = [['cd','ab'],['ef','ac']]  
sort_lists(lists,'desc',1)  
print lists  
  
# 输出结果  
>>>   
[['ef', 'ac'], ['cd', 'ab']]  
```

## inspect模块有什么用

inspect模块提供了一系列函数用于帮助使用自省。  
  
检查对象类型  

```
is{module|class|function|method|builtin}(obj): 检查对象是否为模块、类、函数、方法、内建函数或方法。  
isroutine(obj): 用于检查对象是否为函数、方法、内建函数或方法等等可调用类型。  
```

获取对象信息  

```
getmembers(object[, predicate])
这个方法是dir()的扩展版，它会将dir()找到的名字对应的属性一并返回。  

getmodule(object)
它返回object的定义所在的模块对象。  

get{file|sourcefile}(object)
获取object的定义所在的模块的文件名|源代码文件名（如果没有则返回None）。  

get{source|sourcelines}(object)
获取object的定义的源代码，以字符串|字符串列表返回。  

getargspec(func)
仅用于方法，获取方法声明的参数，返回元组，分别是(普通参数名的列表, *参数名, **参数名, 默认值元组)。  
```
 
## Python处理命令行参数示例代码

```python
# 最简单、最原始的方法就是手动解析了  
import sys  
for arg in sys.argv[1:]:  
    print(arg) 
```    
  
## 介绍一下Python getopt模块

```python
# getopt模块是原来的命令行选项解析器，支持UNIX函数getopt()建立的约定。  
# 它会解析一个参数序列，如sys.argv，并返回一个元祖序列和一个非选项参数序列。  
# 目前支持的选项语法包括短格式和长格式选项：-a, -bval, -b val, --noarg, --witharg=val, --witharg val。  
# 如果只是简单的命令行解析，getopt还是不错的选择。一个例子如下  
  
import sys  
import getopt  
  
try:  
    options, remainder = getopt.getopt(sys.argv[1:], 'o:v', ['output=', 'verbose', 'version=',])  
except getopt.GetoptError as err:  
    print 'ERROR:', err  
    sys.exit(1)  
```

总结下getopt的特点：

1. getopt是从前到后解析 
2. getopt不检查额外参数的合法性，需要自行检查
3. 短命令行和长命令行是分开解析的

## 有一个长度是101的数组，存在1~100的数字，有一个是重复的，拿重复的找出来

```python
# Python中，主要是拿count(i) ==2的找出来即可，再利用列表推导式  
>>> l = [1, 2, 3, 4, 2]  
>>> tmp = []  
>>> [tmp.append(i) for i in l if l.count(i) == 2]  
[None, None]  
>>> tmp  
[2, 2]  
>>> set(tmp)  
set([2])  
```

## set是在哪个版本成为build-in types的？举例说明,并说明为什么当时选择了set这种数据结构

python的set和其他语言类似, 是一个无序不重复元素集, 基本功能包括关系测试和消除重复元素. 集合对象还支持union(联合), intersection(交), difference(差)和sysmmetric difference(对称差集)等数学运算.  
  
sets 支持 x in set, len(set),和 for x in set。作为一个无序的集合，sets不记录元素位置或者插入点。因此，sets不支持 indexing, slicing, 或其它类序列（sequence-like）的操作。  
  
  
下面来点简单的小例子说明。  

```python
>>> x = set('spam')  
>>> y = set(['h','a','m'])  
>>> x, y  
(set(['a', 'p', 's', 'm']), set(['a', 'h', 'm']))  
```

再来些小应用。  

```python  
>>> x & y # 交集  
set(['a', 'm'])  
  
>>> x | y # 并集  
set(['a', 'p', 's', 'h', 'm'])  
  
>>> x - y # 差集  
set(['p', 's'])  
```

去除海量列表里重复元素，用hash来解决也行，只不过感觉在性能上不是很高，用set解决还是很不错的，示例如下：  
  
```python
>>> a = [11,22,33,44,11,22]  
>>> b = set(a)  
>>> b  
set([33, 11, 44, 22])  
>>> c = [i for i in b]  
>>> c  
[33, 11, 44, 22]  
```

### 集合   
   
集合用于包含一组无序的对象。要创建集合，可使用set()函数并像下面这样提供一系列的项：  

```python
s = set([3,5,9,10])      #创建一个数值集合  
t = set("Hello")         #创建一个唯一字符的集合  
```

与列表和元组不同，集合是无序的，也无法通过数字进行索引。此外，集合中的元素不能重复。例如，如果检查前面代码中t集合的值，结果会是：  
  
```python  
>>> t  
set(['H', 'e', 'l', 'o'])  
注意只出现了一个'l'。  
```

集合支持一系列标准操作，包括并集、交集、差集和对称差集，例如：  

```python
a = t | s          # t 和 s的并集  
b = t & s          # t 和 s的交集  
c = t – s         # 求差集（项在t中，但不在s中）  
d = t ^ s          # 对称差集（项在t或s中，但不会同时出现在二者中）  
```

基本操作：  

```python
t.add('x')            # 添加一项  
s.update([10,37,42])  # 在s中添加多项  
```

## Python如何实现单例模式

```python
#-*- encoding=utf-8 -*-  
print '----------------------方法1--------------------------'  
#方法1,实现__new__方法  
#并在将一个类的实例绑定到类变量_instance上,  
#如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回  
#如果cls._instance不为None,直接返回cls._instance  
class Singleton(object):  
    def __new__(cls, *args, **kw):  
        if not hasattr(cls, '_instance'):  
            orig = super(Singleton, cls)  
            cls._instance = orig.__new__(cls, *args, **kw)  
        return cls._instance  
  
class MyClass(Singleton):  
    a = 1  
  
one = MyClass()  
two = MyClass()  
  
two.a = 3  
print one.a  
#3  
#one和two完全相同,可以用id(), ==, is检测  
print id(one)  
#29097904  
print id(two)  
#29097904  
print one == two  
#True  
print one is two  
#True  
  
print '----------------------方法2--------------------------'  
#方法2,共享属性;所谓单例就是所有引用(实例、对象)拥有相同的状态(属性)和行为(方法)  
#同一个类的所有实例天然拥有相同的行为(方法),  
#只需要保证同一个类的所有实例具有相同的状态(属性)即可  
#所有实例共享属性的最简单最直接的方法就是__dict__属性指向(引用)同一个字典(dict)  
#可参看:http://code.activestate.com/recipes/66531/  
class Borg(object):  
    _state = {}  
    def __new__(cls, *args, **kw):  
        ob = super(Borg, cls).__new__(cls, *args, **kw)  
        ob.__dict__ = cls._state  
        return ob  
  
class MyClass2(Borg):  
    a = 1  
  
one = MyClass2()  
two = MyClass2()  
  
#one和two是两个不同的对象,id, ==, is对比结果可看出  
two.a = 3  
print one.a  
#3  
print id(one)  
#28873680  
print id(two)  
#28873712  
print one == two  
#False  
print one is two  
#False  
#但是one和two具有相同的（同一个__dict__属性）,见:  
print id(one.__dict__)  
#30104000  
print id(two.__dict__)  
#30104000  
  
print '----------------------方法3--------------------------'  
#方法3:本质上是方法1的升级（或者说高级）版  
#使用__metaclass__（元类）的高级python用法  
class Singleton2(type):  
    def __init__(cls, name, bases, dict):  
        super(Singleton2, cls).__init__(name, bases, dict)  
        cls._instance = None  
    def __call__(cls, *args, **kw):  
        if cls._instance is None:  
            cls._instance = super(Singleton2, cls).__call__(*args, **kw)  
        return cls._instance  
  
class MyClass3(object):  
    __metaclass__ = Singleton2  
  
one = MyClass3()  
two = MyClass3()  
  
two.a = 3  
print one.a  
#3  
print id(one)  
#31495472  
print id(two)  
#31495472  
print one == two  
#True  
print one is two  
#True  
  
print '----------------------方法4--------------------------'  
#方法4:也是方法1的升级（高级）版本,  
#使用装饰器(decorator),  
#这是一种更pythonic,更elegant的方法,  
#单例类本身根本不知道自己是单例的,因为他本身(自己的代码)并不是单例的  
def singleton(cls, *args, **kw):  
    instances = {}  
    def _singleton():  
        if cls not in instances:  
            instances[cls] = cls(*args, **kw)  
        return instances[cls]  
    return _singleton  
 
@singleton  
class MyClass4(object):  
    a = 1  
    def __init__(self, x=0):  
        self.x = x  
  
one = MyClass4()  
two = MyClass4()  
  
two.a = 3  
print one.a  
#3  
print id(one)  
#29660784  
print id(two)  
#29660784  
print one == two  
#True  
print one is two  
#True  
one.x = 1  
print one.x  
#1  
print two.x  
#1  
```

## 如何用Python来发送邮件

```python
# 可以使用smtplib标准库。  
# 以下代码可以在支持SMTP监听器的服务器上执行。  
  
import sys, smtplib  
  
fromaddr = raw_input("From: ")  
toaddrs  = raw_input("To: ").split(',')  
print("Enter message, end with ^D:")  
msg = ''  
while 1:  
    line = sys.stdin.readline()  
    if not line:  
        break  
msg += line  
  
# 发送邮件部分  
server = smtplib.SMTP('localhost')  
server.sendmail(fromaddr, toaddrs, msg)  
server.quit()  
【题目:055】| Python自动连接ssh的代码
#!/usr/bin/env python  
  
#import the need library.  
import pxssh  
  
#machine details  
hostname = ''  
username = ''  
password = ''  
  
#command we want to send  
command = 'ls -lart'  
  
#function to connect  
def connect(hostname, username, password, release):  
    try:  
        s = pxssh.pxssh()  
        s.login(hostname, username, password, release)  
        print s  
        return s  
    except Exception, e:  
        print "[-] Error Connecting: " + str(e)  
  
#func to send a command  
def send_command(ssh_session, command):  
    ssh_session.sendline(command)  
    ssh_session.prompt()  
    print ssh_session.before  
  
#main()  
if __name__ == "__main__":  
    session = connect(hostname, username, password)  
    send_command(session, command)  
```

或者用pexpect模块

```python
#!/usr/bin/env python  
  
import pexpect  
  
def ssh_cmd(ip, passwd, cmd):  
    ret = -1  
    ssh = pexpect.spawn('ssh root@%s "%s"' % (ip, cmd))  
    try:  
        i = ssh.expect(['password:', 'continue connecting (yes/no)?'], timeout=5)  
        if i == 0 :  
            ssh.sendline(passwd)  
        elif i == 1:  
            ssh.sendline('yes\n')  
            ssh.expect('password: ')  
            ssh.sendline(passwd)  
        ssh.sendline(cmd)  
        res = ssh.read()  
        print res  
        ret = 0  
    except pexpect.EOF:  
        print "EOF"  
        ssh.close()  
        ret = -1  
    except pexpect.TIMEOUT:  
        print "TIMEOUT"  
        ssh.close()  
        ret = -2  
    return ret  
  
#main()  
if __name__ == "__main__":  
    ssh_cmd('127.0.0.1', 'password', 'ls -lart')  
 ```
 
## 介绍一下Python Date Time方面的类

```python
一.time模块  
time模块提供各种操作时间的函数  
一般有两种表示时间的方式:  
第一种: 是时间戳的方式(相对于1970.1.1 00:00:00以秒计算的偏移量),时间戳是惟一的  
第二种: 以数组的形式表示即(struct_time),共有九个元素，分别表示，同一个时间戳的struct_time会因为时区不同而不同  
  
二.datetime模块  
Python提供了多个内置模块用于操作日期时间，像calendar，time，datetime。time模块。  
相比于time模块，datetime模块的接口则更直观、更容易调用。  
datetime模块定义了下面这几个类：  
datetime.date：表示日期的类。常用的属性有year, month, day；  
datetime.time：表示时间的类。常用的属性有hour, minute, second, microsecond；  
datetime.datetime：表示日期时间。  
datetime.timedelta：表示时间间隔，即两个时间点之间的长度。  
datetime.tzinfo：与时区有关的相关信息。  
datetime中，表示日期时间的是一个datetime对象  
datetime中提供了strftime方法，可以将一个datetime型日期转换成字符串
```
  
## 写一个简单的Python socket编程

服务器端程序:

```python
# FileName: server.py  
  
import socket  
  
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.bind(('localhost', 8001))  
  
sock.listen(5)  
while True:  
    conn, addr = sock.accept()  
    try:  
        conn.settimeout(5)  
        buff = conn.recv(1024)  
        if buff == '1':  
            conn.send('Hello, Client...')  
        else:  
            conn.send('Please, Go Out...')  
    except socket.timeout:  
        print 'Socket Time Out...'  
    finally:  
        conn.close()  
```

客户端程序:

```python
# FileName: client.py  
import socket  
import time  
  
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
sock.connect(('localhost', 8001))  
time.sleep(2)  
sock.send('1')  
print sock.recv(1024)  
sock.close() 
```
 
在终端运行server.py，然后运行clien.py，会在终端打印“Hello, Client..."。
如果更改client.py的sock.send('1')为其它值在终端会打印“Please, Go Out...”。
更改time.sleep(2)为大于5的数值， 服务器将会超时。

## 解释一下python的and-or语法

0 and ＊ 不需要再考虑＊是0还是1，结果是0  
1 and ＊ 需要考虑＊是0还是1来决定结果。  
  
1 or ＊ 不需要考虑后面的＊，结果为1  
0 or ＊ 需要考虑后面的＊来决定结果  
  
这个语法看起来类似于 C 语言中的 bool ? a : b 表达式。整个表达式从左到右进行演算，所以先进行 and 表达式的演算。 1 and 'first' 演算值为 'first'，然后 'first' or 'second' 的演算值为 'first'。  
  
0 and 'first' 演算值为 False，然后 0 or 'second' 演算值为 'second'。  
  
and-or主要是用来模仿 三目运算符 bool?a:b的，即当表达式bool为真，则取a否则取b。  
  
and-or 技巧，bool and a or b 表达式，当 a 在布尔上下文中的值为假时，不会像 C 语言表达式 bool ? a : b 那样工作。

  
## Python里关于“堆”这种数据结构的模块是哪个？“堆”有什么优点和缺点

这个真没有！
 
## 实现一个stack

```python
class Stack :  
    def __init__( self ):  
        ''''' Creates an empty stack. '''  
        self._items = list()  
          
    def isEmpty(self):  
        ''''' Returns True if the stack is empty or False otherwise. '''  
        return len(self) == 0  
  
    def __len__(self):  
        ''''' Returns the number of items in the stack. '''  
        return len(self._items)  
     
    def peek(self):  
       ''''' Returns the top item on the stack without removing it. '''  
       assert not self.isEmpty(), "Cannot peek at an empty stack"  
       return self._items[-1]  
  
    def pop(self):  
        ''''' Removes and returns the top item on the stack. '''  
        assert not self.isEmpty(), "Cannot pop from an empty stack"  
        return self._items.pop()  
     
    def push(self,item):  
        ''''' Push an item onto the top of the stack. '''  
        self._items.append( item )  
  ```
  
## 编写一个简单的ini文件解释器

db_config.ini

```
[baseconf]
host=127.0.0.1
port=3306
user=root
password=root
db_name=evaluting_sys
[concurrent]
processor=20
```

示例代码

```python
import sys,os
import ConfigParser
def test(config_file_path):
    cf = ConfigParser.ConfigParser()
    cf.read(config_file_path)

    s = cf.sections()
    print 'section:', s

    o = cf.options("baseconf")
    print 'options:', o

    v = cf.items("baseconf")
    print 'db:', v

    db_host = cf.get("baseconf", "host")
    db_port = cf.getint("baseconf", "port")
    db_user = cf.get("baseconf", "user")
    db_pwd = cf.get("baseconf", "password")

    print db_host, db_port, db_user, db_pwd

    cf.set("baseconf", "db_pass", "123456")
    cf.write(open("config_file_path", "w"))
if __name__ == "__main__":
    test("../conf/db_config.ini")
```

## Tuple 和 List 的转换

函数tuple(seq)可以把所有可迭代的(iterable)序列转换成一个tuple, 元素不变，排序也不变。

例如，tuple([1,2,3])返回(1,2,3), tuple(‘abc’)返回(‘a’.'b’,'c’).如果参数已经是一个tuple的话，函数不做任何拷贝而直接返回原来的对象，所以在不确定对象是不是tuple的时候来调用tuple()函数也不是很耗费的。

函数list(seq)可以把所有的序列和可迭代的对象转换成一个list,元素不变，排序也不变。

例如 list([1,2,3])返回(1,2,3), list(‘abc’)返回['a', 'b', 'c']。如果参数是一个list, 她会像set[:]一样做一个拷贝

## python下多线程的限制以及多进程中传递参数的方式

python多线程有个全局解释器锁（global interpreter lock），这个锁的意思是任一时间只能有一个线程使用解释器，跟单cpu跑多个程序一个意思，大家都是轮着用的，这叫“并发”，不是“并行”。

多进程间共享数据，可以使用 multiprocessing.Value 和 multiprocessing.Array

## Python是如何进行内存管理的？

Python引用了一个内存池(memory pool)机制，即Pymalloc机制(malloc:n.分配内存)，用于管理对小块内存的申请和释放

内存池（memory pool）的概念：

当创建大量消耗小内存的对象时，频繁调用new/malloc会导致大量的内存碎片，致使效率降低。内存池的概念就是预先在内存中申请一定数量的，大小相等 的内存块留作备用，当有新的内存需求时，就先从内存池中分配内存给这个需求，不够了之后再申请新的内存。这样做最显著的优势就是能够减少内存碎片，提升效率。

内存池的实现方式有很多，性能和适用范围也不一样。 

python中的内存管理机制——Pymalloc：
　　
python中的内存管理机制都有两套实现，一套是针对小对象，就是大小小于256bits时,pymalloc会在内存池中申请内存空间；当大于256bits，则会直接执行new/malloc的行为来申请内存空间。

关于释放内存方面，当一个对象的引用计数变为0时，python就会调用它的析构函数。在析构时，也采用了内存池机制，从内存池来的内存会被归还到内存池中，以避免频繁地释放动作。

## 什么是lambda函数？它有什么好处?

lambda 函数是一个可以接收任意多个参数(包括可选参数)并且返回单个表达式值的函数。 lambda 函数不能包含命令，它们所包含的表达式不能超过一个。不要试图向lambda 函数中塞入太多的东西；如果你需要更复杂的东西，应该定义一个普通函数，然后想让它多长就多长。

## 列表与元组的区别是什么.分别在什么情况下使用

列表中的项目应该包括在方括号中，你可以添加、删除或是搜索列表中的项目。由于你可以增加或删除项目，所以列表是可变的数据类型，即这种类型是可以被改变的。

元组和列表十分类似，但是元组是不可变的.也就是说你不能修改元组。元组通过圆括号中用逗号分割的项目定义。元组通常用在使语句或用户定义的函数能够安全地采用一组值的时候，即被使用的元组的值不会改变。

## 字典

键值对的集合(map)字典是以大括号“{}”包围的数据集合。

与列表区别：字典是无序的，在字典中通过键来访问成员。字典是可变的，可以包含任何其他类型。

## 说明os,sys模块不同，并列举常用的模块方法？

官方解释：

os： This module provides a portable way of using operating system dependent functionality.

翻译：提供一种方便的使用操作系统函数的方法。

sys：This module provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.

翻译：提供访问由解释器使用或维护的变量和在与解释器交互使用到的函数。

