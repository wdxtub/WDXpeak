### 为什么是string.join(list)而不是list.join(string)

问题 [链接](http://stackoverflow.com/questions/493819/python-join-why-is-it-string-joinlist-instead-of-list-joinstring)

    my_list = ["Hello", "world"]
    print "-".join(my_list)
    #为什么不是 my_list.join("-") 。。。。这个....

答案：

因为所有可迭代对象都可以被连接，而不只是列表，但是连接者总是字符串

### 字符如何转为小写

问题 [链接](http://stackoverflow.com/questions/6797984/how-to-convert-string-to-lowercase-in-python)

    s = "Kilometer"
    print(s.lower())

### 字符串转为float/int

    >>> a = "545.2222"
    >>> float(a)
    545.2222
    >>> int(a)
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    ValueError: invalid literal for int() with base 10: '545.2222'
    >>> int(float(a))
    545
    >>> int('544')
    544

另一种，用 [ast](http://docs.python.org/2/library/ast.html#ast.literal_eval)模块


    >>> import ast
    >>> ast.literal_eval("545.2222")
    545.2222
    >>> ast.literal_eval("31")
    31


### 如何反向输出一个字符串

问题 [链接](http://stackoverflow.com/questions/931092/reverse-a-string-in-python)

做法

    >>> 'hello world'[::-1]
    'dlrow olleh'

### 如何随机生成大写字母和数字组成的字符串

    6U1S75
    4Z4UKK
    U911K4

解决

    import string, random
    ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(N))

### python中字符串的contains

问题 [链接](http://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-method)

python中字符串判断contains

使用in关键字

    if not "blah" in somestring: continue
    if "blah" not in somestring: continue

使用字符串的find/index  (注意index查找失败抛异常)

    s = "This be a string"
    if s.find("is") == -1:
        print "No 'is' here!"
    else:
        print "Found 'is' in the string."

### 如何判断一个字符串是数字

问题 [链接](http://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-in-python)

使用这种方法会不会十分丑陋和低效

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

使用这种方法并不丑陋和低效

使用isdigit(缺点，对非整数无能为力)

    a = "03523"
    a.isdigit()

### 字符串格式化 % vs format

问题 [链接](http://stackoverflow.com/questions/5082452/python-string-formatting-vs-format)

Python2.6中引入string.format()方法，语法和原先%操作符的字符串格式化差异较大

在什么情况下使用哪种更好?

以下的输出是一致的，有什么区别

    #!/usr/bin/python
    sub1 = "python string!"
    sub2 = "an arg"

    a = "i am a %s"%sub1
    b = "i am a {0}".format(sub1)

    c = "with %(kwarg)s!"%{'kwarg':sub2}
    d = "with {kwarg}!".format(kwarg=sub2)

    print a
    print b
    print c
    print d

.format 看起来更加强大，可以用在很多情况.

例如你可以在格式化时重用传入的参数,而你用%时无法做到这点

另一个比较讨厌的是，%只处理 一个变量或一个元组, 你或许会认为下面的语法是正确的

    "hi there %s" % name

但当name恰好是(1,2,3)时，会抛出TypeError异常.为了保证总是正确的，你必须这么写

    "hi there %s" % (name,)   # supply the single argument as a single-item tuple

这么写很丑陋， .format没有这些问题

什么时候不考虑使用.format

    你对.format知之甚少
    使用Python2.5

### 将一个字符串转为一个字典

问题 [链接](http://stackoverflow.com/questions/988228/converting-a-string-to-dictionary)

如何将字符串转成字典，不适用eval

    s = "{'muffin' : 'lolz', 'foo' : 'kitty'}"

从python2.6开始，你可以使用内建模块 ast.literal_eval

    >>> import ast
    >>> ast.literal_eval("{'muffin' : 'lolz', 'foo' : 'kitty'}")
    {'muffin': 'lolz', 'foo': 'kitty'}

这个做法比直接eval更安全
帮助文档

    >>> help(ast.literal_eval)
    Help on function literal_eval in module ast:

    literal_eval(node_or_string)
        Safely evaluate an expression node or a string containing a Python
        expression.  The string or node provided may only consist of the following
        Python literal structures: strings, numbers, tuples, lists, dicts, booleans,
        and None.

举例

    >>> eval("shutil.rmtree('mongo')")
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "<string>", line 1, in <module>
    File "/opt/Python-2.6.1/lib/python2.6/shutil.py", line 208, in rmtree
        onerror(os.listdir, path, sys.exc_info())
    File "/opt/Python-2.6.1/lib/python2.6/shutil.py", line 206, in rmtree
        names = os.listdir(path)
    OSError: [Errno 2] No such file or directory: 'mongo'
    >>> ast.literal_eval("shutil.rmtree('mongo')")
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "/opt/Python-2.6.1/lib/python2.6/ast.py", line 68, in literal_eval
        return _convert(node_or_string)
    File "/opt/Python-2.6.1/lib/python2.6/ast.py", line 67, in _convert
        raise ValueError('malformed string')
    ValueError: malformed string

### 如何获取一个字符的ASCII码

问题 [链接](http://stackoverflow.com/questions/227459/ascii-value-of-a-character-in-python)

    >>> ord('a')
    97
    >>> chr(97)
    'a'
    >>> chr(ord('a') + 3)
    'd'
    >>>

另外对于unicode

    >>> unichr(97)
    u'a'
    >>> unichr(1234)
    u'\u04d2'

### 如何使用不同分隔符切分字符串

问题 [链接](http://stackoverflow.com/questions/1059559/python-strings-split-with-multiple-separators)

使用re.split  [文档](http://docs.python.org/2/library/re.html#re.split)

    >>> re.split('\W+', 'Words, words, words.')
    ['Words', 'words', 'words', '']
    >>> re.split('(\W+)', 'Words, words, words.')
    ['Words', ', ', 'words', ', ', 'words', '.', '']
    >>> re.split('\W+', 'Words, words, words.', 1)
    ['Words', 'words, words.'])

或者匹配获取正确的 re.findall

    import re
    DATA = "Hey, you - what are you doing here!?"
    print re.findall(r"[\w']+", DATA)
    # Prints ['Hey', 'you', 'what', 'are', 'you', 'doing', 'here']

### 如何截掉空格（包括tab)

问题 [链接](http://stackoverflow.com/questions/1185524/how-to-trim-whitespace-including-tabs)

空白在字符串左右两边

    s = "  \t a string example\t  "
    s = s.strip()

空白在字符串右边

    s = s.rstrip()

左边

    s = s.lstrip()

另外你可以指定要截掉的字符作为参数

    s = s.strip(' \t\n\r')

### 如何截取一个字符串获得子串

问题 [链接](http://stackoverflow.com/questions/663171/is-there-a-way-to-substring-a-string-in-python)


    >>> x = "Hello World!"
    >>> x[2:]
    'llo World!'
    >>> x[:2]
    'He'
    >>> x[:-2]
    'Hello Worl'
    >>> x[-2:]
    'd!'
    >>> x[2:-2]
    'llo Worl'

python将这类操作称为切片，可以作用于序列类型，不仅仅是字符串

### python中用==比较字符串，is有时候会返回错误判断

问题 [链接](http://stackoverflow.com/questions/1504717/python-vs-is-comparing-strings-is-fails-sometimes-why)

is是身份测试，==是相等测试

    >>> a = 'pub'
    >>> b = ''.join(['p', 'u', 'b'])
    >>> a == b
    True
    >>> a is b
    False'

is 等价于 id(a) == id(b)

### 如何填充0到数字字符串中保证统一长度

问题 [链接](http://stackoverflow.com/questions/339007/python-nicest-way-to-pad-zeroes-to-string)

对于字符串

    >>> n = '4'
    >>> print n.zfill(3)
    >>> '004'

对于数字,[相关文档](http://docs.python.org/2/library/string.html#formatexamples)

    >>> n = 4
    >>> print '%03d' % n
    >>> 004
    >>> print "{0:03d}".format(4)  # python >= 2.6
    >>> 004
    >>> print("{0:03d}".format(4))  # python 3
    >>> 004

### 如何将字符串转换为datetime

字符串 -> time  [strptime](https://docs.python.org/2/library/time.html#time.strptime)

    >>> import time
    >>> time.strptime("30 Nov 00", "%d %b %y")   
    time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0,
                    tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)

time -> 字符串  [strftime](https://docs.python.org/2/library/time.html#time.strftime)

    >>> from time import gmtime, strftime
    >>> strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    'Thu, 28 Jun 2001 14:17:15 +0000'


### 如何将byte array转为string

问题 [链接](http://stackoverflow.com/questions/606191/convert-byte-array-to-python-string)

    >>> b"abcde"
    b'abcde'
    >>> b"abcde".decode("utf-8")
    'abcde'


