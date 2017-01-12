# Python 快速上手指南

<!-- MarkdownTOC -->

- 原始数据类型和操作符
- 变量和集合
- 控制流程
- 函数
- 类
- 模块

<!-- /MarkdownTOC -->


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
+ Python 2.7 之后，大括号可以用来表示集合：`filled_set = {1, 2, 2, 3, 4}` -> `{1 2 3 4`
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
