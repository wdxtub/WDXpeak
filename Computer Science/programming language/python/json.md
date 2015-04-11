Python处理JSON
==================
####概念  
**序列化（Serialization）**：将对象的状态信息转换为可以存储或可以通过网络传输的过程，传输的格式可以是JSON、XML等。反序列化就是从存储区域（JSON，XML）读取反序列化对象的状态，重新创建该对象。   

**JSON（JavaScript Object Notation）**：一种轻量级数据交换格式，相对于XML而言更简单，也易于阅读和编写，机器也方便解析和生成，Json是JavaScript中的一个子集。  

Python2.6开始加入了JSON模块，无需另外下载，Python的Json模块序列化与反序列化的过程分别是 **encoding**和 **decoding**  

**encoding**：把一个Python对象编码转换成Json字符串  
**decoding**：把Json格式字符串解码转换成Python对象  
对于简单数据类型（string、unicode、int、float、list、tuple、dict），可以直接处理。  

#####json.dumps方法对简单数据类型encoding：  

    import json
    data = [{'a':"A",'b':(2,4),'c':3.0}]  #list对象
    print "DATA:",repr(data)
    
    data_string = json.dumps(data)
    print "JSON:",data_string

输出：  

    DATA: [{'a':'A','c':3.0,'b':(2,4)}] #python的dict类型的数据是没有顺序存储的
    JSON: [{"a":"A","c":3.0,"b":[2,4]}]  

JSON的输出结果与DATA很相似，除了一些微妙的变化，如python的元组类型变成了Json的数组，Python到Json的编码转换规则是：
![python2json](../resource/image/python2json.png)

#####json.loads方法处理简单数据类型的decoding（解码）转换  

    import json
    data = [{'a':"A",'b':(2,4),'c':3.0}]  #list对象
    
    data_string = json.dumps(data)
    print "ENCODED:",data_string

    decoded = json.loads(data_string)
    print "DECODED:",decoded

    print "ORIGINAL:",type(data[0]['b'])
    print "DECODED:",type(decoded[0]['b'])

输出:  

    ENCODED: [{"a": "A", "c": 3.0, "b": [2, 4]}]
    DECODED: [{u'a': u'A', u'c': 3.0, u'b': [2, 4]}]
    ORIGINAL: <type 'tuple'>
    DECODED: <type 'list'>

解码过程中，json的数组最终转换成了python的list，而不是最初的tuple类型，Json到Python的解码规则是：
![json2python](../resource/image/json2python.png)  

####json的人文关怀  
编码后的json格式字符串紧凑的输出，而且也没有顺序，因此`dumps`方法提供了一些可选的参数，让输出的格式提高可读性，如`sort_keys`是告诉编码器按照字典排序(a到z)输出。  

    import json
    
    data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
    print 'DATA:', repr(data)
    
    unsorted = json.dumps(data)
    print 'JSON:', json.dumps(data)
    print 'SORT:', json.dumps(data, sort_keys=True)

输出:  

    DATA: [{'a': 'A', 'c': 3.0, 'b': (2, 4)}]
    JSON: [{"a": "A", "c": 3.0, "b": [2, 4]}]
    SORT: [{"a": "A", "b": [2, 4], "c": 3.0}

`indent`参数根据数据格式缩进显示，读起来更加清晰: 

    import json
    
    data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
    print 'DATA:', repr(data)
    
    print 'NORMAL:', json.dumps(data, sort_keys=True)
    print 'INDENT:', json.dumps(data, sort_keys=True, indent=2)

输出:  

    DATA: [{'a': 'A', 'c': 3.0, 'b': (2, 4)}]
    NORMAL: [{"a": "A", "b": [2, 4], "c": 3.0}]
    INDENT: [
      {
        "a": "A",
        "b": [
          2,
          4
        ],
        "c": 3.0
      }
    ]

`separators`参数的作用是去掉`,`,`:`后面的空格，从上面的输出结果都能看到", :"后面都有个空格，这都是为了美化输出结果的作用，但是在我们传输数据的过程中，越精简越好，冗余的东西全部去掉，因此就可以加上separators参数：  

    import json
    
    data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
    print 'DATA:', repr(data)
    print 'repr(data)             :', len(repr(data))
    print 'dumps(data)            :', len(json.dumps(data))
    print 'dumps(data, indent=2)  :', len(json.dumps(data, indent=2))
    print 'dumps(data, separators):', len(json.dumps(data, separators=(',',':')))


输出：  

    DATA: [{'a': 'A', 'c': 3.0, 'b': (2, 4)}]
    repr(data)             : 35
    dumps(data)            : 35
    dumps(data, indent=2)  : 76
    dumps(data, separators): 29


`skipkeys`参数，在encoding过程中，dict对象的key只可以是string对象，如果是其他类型，那么在编码过程中就会抛出`ValueError`的异常。`skipkeys`可以跳过那些非string对象当作key的处理.

    import json
    
    data= [ { 'a':'A', 'b':(2, 4), 'c':3.0, ('d',):'D tuple' } ]
    
    try:
        print json.dumps(data)
    except (TypeError, ValueError) as err:
        print 'ERROR:', err
    print 
    print json.dumps(data, skipkeys=True)

输出:  
    
    ERROR: keys must be a string
    
    [{"a": "A", "c": 3.0, "b": [2, 4]}]



####让json支持自定义数据类型  
以上例子都是基于python的built-in类型的，对于自定义类型的数据结构，json模块默认是没法处理的，会抛出异常：`TypeError  xx is not JSON serializable`，此时你需要自定义一个转换函数:  

    import json  

    class MyObj(object):
        def __init__(self, s):
            self.s = s
        def __repr__(self):
            return '<MyObj(%s)>' % self.s

    obj = .MyObj('helloworld')
    
    try:
        print json.dumps(obj)
    except TypeError, err:
        print 'ERROR:', err
    
    #转换函数
    def convert_to_builtin_type(obj):
        print 'default(', repr(obj), ')'
        # 把MyObj对象转换成dict类型的对象
        d = { '__class__':obj.__class__.__name__, 
              '__module__':obj.__module__,
            }
        d.update(obj.__dict__)
        return d
    
    print json.dumps(obj, default=convert_to_builtin_type)

输出:  

    ERROR: <MyObj(helloworld)> is not JSON serializable
    default( <MyObj(helloworld)> )
    {"s": "hellworld", "__module__": "MyObj", "__class__": "__main__"} 
    #注意：这里的class和module根据你代码的所在文件位置不同而不同


相反，如果要把json decode 成python对象，同样也需要自定转换函数，传递给json.loads方法的`object_hook`参数：  

    #jsontest.py

    import json
    
    class MyObj(object):
    
        def __init__(self,s):
            self.s = s
    
        def __repr__(self):
    
            return "<MyObj(%s)>" % self.s
    
    def dict_to_object(d):
        if '__class__' in d:
            class_name = d.pop('__class__')
            module_name = d.pop('__module__')
            module = __import__(module_name)
    
            print "MODULE:",module
    
            class_ = getattr(module,class_name)
    
            print "CLASS",class_
    
            args = dict((key.encode('ascii'),value) for key,value in d.items())
    
            print 'INSTANCE ARGS:',args
    
            inst = class_(**args)
        else:
            inst = d
        return inst
    
    encoded_object = '[{"s":"helloworld","__module__":"jsontest","__class__":"MyObj"}]'
    
    myobj_instance = json.loads(encoded_object,object_hook=dict_to_object)
    print myobj_instance
    
输出：  

    MODULE: <module 'jsontest' from 'E:\Users\liuzhijun\workspace\python\jsontest.py'>
    CLASS <class 'jsontest.MyObj'>
    INSTANCE ARGS: {'s': u'helloworld'}
    [<MyObj(helloworld)>]
    MODULE: <module 'jsontest' from 'E:\Users\liuzhijun\workspace\python\jsontest.py'>
    CLASS <class 'jsontest.MyObj'>
    INSTANCE ARGS: {'s': u'helloworld'}
    [<MyObj(helloworld)>]


####使用Encoder与Decoder类实现json编码的转换  

**JSONEncoder**有一个迭代接口`iterencode(data)`，返回一系列编码的数据，他的好处是可以方便的把逐个数据写到文件或网络流中，而不需要一次性就把数据读入内存.  

    import json
    
    encoder = json.JSONEncoder()
    data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
    
    for part in encoder.iterencode(data):
        print 'PART:', part

输出：  

    PART: [
    PART: {
    PART: "a"
    PART: :
    PART: "A"
    PART: ,
    PART: "c"
    PART: :
    PART: 3.0
    PART: ,
    PART: "b"
    PART: :
    PART: [2
    PART: , 4
    PART: ]
    PART: }
    PART: ]


`encode`方法等价于`''.join(encoder.iterencode()`，而且预先会做些错误检查（比如非字符串作为dict的key），对于自定义的对象，我们只需从些JSONEncoder的`default()`方法，其实现方式与上面提及的函数`convet_to_builtin_type()`是类似的。  


    import json
    import json_myobj

    class MyObj(object):

        def __init__(self,s):
            self.s = s

        def __repr__(self):
            return "<MyObj(%s)>" % self.s
    
    class MyEncoder(json.JSONEncoder):
        
        def default(self, obj):
            print 'default(', repr(obj), ')'
            # Convert objects to a dictionary of their representation
            d = { '__class__':obj.__class__.__name__, 
                  '__module__':obj.__module__,
                  }
            d.update(obj.__dict__)
            return d
    
    obj = json_myobj.MyObj('helloworld')
    print obj
    print MyEncoder().encode(obj)

输出：  

    <MyObj(internal data)>
    default( <MyObj(internal data)> )
    {"s": "helloworld", "__module__": "Myobj", "__class__": "MyObj"}

从json对Python对象的转换:

    class MyDecoder(json.JSONDecoder):
        
        def __init__(self):
            json.JSONDecoder.__init__(self, object_hook=self.dict_to_object)
    
        def dict_to_object(self, d):
            if '__class__' in d:
                class_name = d.pop('__class__')
                module_name = d.pop('__module__')
                module = __import__(module_name)
                print 'MODULE:', module
                class_ = getattr(module, class_name)
                print 'CLASS:', class_
                args = dict( (key.encode('ascii'), value) for key, value in d.items())
                print 'INSTANCE ARGS:', args
                inst = class_(**args)
            else:
                inst = d
            return inst
    
    encoded_object = '[{"s": "helloworld", "__module__": "jsontest", "__class__": "MyObj"}]'
    
    myobj_instance = MyDecoder().decode(encoded_object)
    print myobj_instance

输出:

    MODULE: <module 'jsontest' from 'E:\Users\liuzhijun\workspace\python\jsontest.py'>
    CLASS: <class 'jsontest.MyObj'>
    INSTANCE ARGS: {'s': u'helloworld'}
    [<MyObj(helloworld)>]


####json格式字符串写入到文件流中  
上面的例子都是在内存中操作的，如果对于大数据，把他编码到一个类文件(file-like)中更合适，`load()`和`dump()`方法就可以实现这样的功能。

    import json
    import tempfile
    
    data = [ { 'a':'A', 'b':(2, 4), 'c':3.0 } ]
    
    f = tempfile.NamedTemporaryFile(mode='w+')
    json.dump(data, f)
    f.flush()
    
    print open(f.name, 'r').read()
    

输出：

    [{"a": "A", "c": 3.0, "b": [2, 4]}]

类似的：      

    import json
    import tempfile
    
    f = tempfile.NamedTemporaryFile(mode='w+')
    f.write('[{"a": "A", "c": 3.0, "b": [2, 4]}]')
    f.flush()
    f.seek(0)
    
    print json.load(f)

输出：  

    [{u'a': u'A', u'c': 3.0, u'b': [2, 4]}]


参考：  
http://docs.python.org/2/library/json.html  
http://www.cnblogs.com/coser/archive/2011/12/14/2287739.html  
http://pymotw.com/2/json/  









