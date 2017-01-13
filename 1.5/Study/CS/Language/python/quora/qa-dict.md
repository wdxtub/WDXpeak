
### 使用列表解析创建一个字典

问题 [链接](http://stackoverflow.com/questions/1747817/python-create-a-dictionary-with-list-comprehension)

python 2.6

    d = dict((key, value) for (key, value) in sequence)

python 2.7+ or 3, 使用 [字典解析语法](http://www.python.org/dev/peps/pep-0274/)

    d = {key: value for (key, value) in sequence}

### 使用"in"还是"has_key()"

问题 [链接](http://stackoverflow.com/questions/1323410/has-key-or-in)

    d = {'a': 1, 'b': 2}
    'a' in d
    True
    or:

    d = {'a': 1, 'b': 2}
    d.has_key('a')
    True

哪种更好

in更pythonic, 另外 has_key()在Python3.x中已经被移除

### 字典默认值

问题 [链接](http://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary)

和问题有点偏

    #获取时,如不存在，得到默认值
    d.get(key, 0)
    #设置时，若key不存在，设置默认值，已存在，返回已存在value
    d.setdefault(key, []).append(new_element)
    #初始即默认值
    from collections import defaultdict
    d = defaultdict(lambda: 0)
    #or d = defaultdict(int)


### 如何给字典添加一个值

问题 [链接](http://stackoverflow.com/questions/1024847/add-to-a-dictionary-in-python)


    #### Making a dictionary ####
    data = {}
    # OR #
    data = dict()

    #### Initially adding values ####
    data = {'a':1,'b':2,'c':3}
    # OR #
    data = dict(a=1, b=2, c=3)

    #### Inserting/Updating value ####
    data['a']=1  # updates if 'a' exists, else adds 'a'
    # OR #
    data.update({'a':1})
    # OR #
    data.update(dict(a=1))

    #### Merging 2 dictionaries ####
    data.update(data2)  # Where data2 is also a dict.

### 如何将字段转换成一个object，然后使用对象-属性的方式读取

问题 [链接](http://stackoverflow.com/questions/1305532/convert-python-dict-to-object)

有dict

    >>> d = {'a': 1, 'b': {'c': 2}, 'd': ["hi", {'foo': "bar"}]}}

想用这种方式访问

    >>> x = dict2obj(d)
    >>> x.a
    1
    >>> x.b.c
    2
    >>> x.d[1].foo
    bar

使用namedtuple

    >>> from collections import namedtuple
    >>> MyStruct = namedtuple('MyStruct', 'a b d')
    >>> s = MyStruct(a=1, b={'c': 2}, d=['hi'])
    >>> s
    MyStruct(a=1, b={'c': 2}, d=['hi'])
    >>> s.a
    1
    >>> s.b
    {'c': 2}
    >>> s.c
    >>> s.d
    ['hi']

使用类

    class Struct:
        def __init__(self, **entries):
            self.__dict__.update(entries)

    >>> args = {'a': 1, 'b': 2}
    >>> s = Struct(**args)
    >>> s
    <__main__.Struct instance at 0x01D6A738>
    >>> s.a
    1
    >>> s.b
    2

### 如何在单一表达式中合并两个Python字典

问题 [链接](http://stackoverflow.com/questions/38987/how-can-i-merge-union-two-python-dictionaries-in-a-single-expression)

    >>> x = {'a':1, 'b': 2}
    >>> y = {'b':10, 'c': 11}
    >>> z = x.update(y)
    >>> print z
    None
    >>> x
    {'a': 1, 'b': 10, 'c': 11}

我想要最终合并结果在z中，不是x，我要怎么做？

回答

这种情况下，可以使用

    z = dict(x.items() + y.items())

这个表达式将会实现你想要的，最终结果z，并且相同key的值，将会是y中key对应的值

    >>> x = {'a':1, 'b': 2}
    >>> y = {'b':10, 'c': 11}
    >>> z = dict(x.items() + y.items())
    >>> z
    {'a': 1, 'c': 11, 'b': 10}

如果在Python3中,会变得有些复杂

    >>> z = dict(list(x.items()) + list(y.items()))
    >>> z
    {'a': 1, 'c': 11, 'b': 10}

### 如何映射两个列表成为一个字典

问题 [链接](http://stackoverflow.com/questions/209840/map-two-lists-into-a-dictionary-in-python)

两个列表

    keys = ('name', 'age', 'food')
    values = ('Monty', 42, 'spam')
如何得到

    dict = {'name' : 'Monty', 'age' : 42, 'food' : 'spam'}

使用zip

    >>> keys = ['a', 'b', 'c']
    >>> values = [1, 2, 3]
    >>> dictionary = dict(zip(keys, values))
    >>> print dictionary
    {'a': 1, 'b': 2, 'c': 3}

### 排序一个列表中的所有dict，根据dict内值

问题 [链接](http://stackoverflow.com/questions/72899/in-python-how-do-i-sort-a-list-of-dictionaries-by-values-of-the-dictionary)

如何排序如下列表，根据name或age

    [{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]

简单的做法；

    newlist = sorted(list_to_be_sorted, key=lambda k: k['name'])

高效的做法

    from operator import itemgetter
    newlist = sorted(list_to_be_sorted, key=itemgetter('name'))

### 根据值排序一个字典

问题 [链接](http://stackoverflow.com/questions/613183/python-sort-a-dictionary-by-value)

    import operator
    x = {1: 2, 3: 4, 4:3, 2:1, 0:0}
    sorted_x = sorted(x.iteritems(), key=operator.itemgetter(1))
    #[(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
    #dict(sorted_x) == x

### 如何将自定义对象作为字典键值

问题 [链接](http://stackoverflow.com/questions/4901815/object-as-a-dictionary-key)

    class MyThing:
        def __init__(self,name,location,length):
            self.name = name
            self.location = location
            self.length = length

        def __hash__(self):
            return hash((self.name, self.location))

        def __eq__(self, other):
            return (self.name, self.location) == (other.name, other.location)

