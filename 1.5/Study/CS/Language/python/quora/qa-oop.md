
### Python 'self' 解释

问题 [链接](http://stackoverflow.com/questions/2709821/python-self-explained)


self关键字的作用是什么？
我理解他用户在创建class时具体化实例，但我无法理解为何需要给每个方法加入self作为参数.

举例，在ruby中，我这么做:

    class myClass
        def myFunc(name)
            @name = name
        end
    end

我可以很好地理解，非常简单.但是在Python中，我需要去加入self:

    class myClass:
        def myFunc(self, name):
            self.name = name

有谁能解释下么？

使用self关键字的原因是，Python没有@语法用于引用实例属性.Python决定用一种方式声明方法:实例对象自动传递给属于它的方法,但不是接收自动化：方法的第一个参数是调用这个方法的实例对象本身.这使得方法整个同函数一致,并且由你自己决定真实的名（虽然self是约定，但当你使用其他名的时候，通常人们并不乐意接受）.self对于代码不是特殊的，只是另一个对象.

Python本来可以做一些用来区分真实的名字和属性的区别 —— 像Ruby有的特殊语法，或者像C++/Java的命令声明,或者其他可能的的语法 —— 但是Python没有这么做.Python致力于使事情变得明确简单，让事情是其本身，虽然并不是全部地方都这么做，但是实例属性是这么做的！这就是为什么给一个实例属性赋值时需要知道是给哪个实例赋值,并且，这就是为什么需要self

举例

    class Vector(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y
        def length(self):
            return math.sqrt(self.x ** 2 + self.y ** 2)

等价于

    def length_global(vector):
        return math.sqrt(vector.x ** 2 + vector.y ** 2)

另外

    v_instance.length()
    转为
    Vector.length(v_instance)
### 为什么Python的'private'方法并不是真正的私有方法

问题 [链接](http://stackoverflow.com/questions/70528/why-are-pythons-private-methods-not-actually-private)

Python允许我们创建'private' 函数：变量以两个下划线开头，像这样： *__myPrivateMethod()*.
但是，如何解释：

    >>> class MyClass:
    ...     def myPublicMethod(self):
    ...             print 'public method'
    ...     def __myPrivateMethod(self):
    ...             print 'this is private!!'
    ...
    >>> obj = MyClass()
    >>> obj.myPublicMethod()
    public method
    >>> obj.__myPrivateMethod()
    Traceback (most recent call last):
    File "", line 1, in
    AttributeError: MyClass instance has no attribute '__myPrivateMethod'
    >>> dir(obj)
    ['_MyClass__myPrivateMethod', '__doc__', '__module__', 'myPublicMethod']
    >>> obj._MyClass__myPrivateMethod()
    this is private!!


dir(obj) 和 obj._MyClass__myPrivateMethod()


回答

‘private'只是用作，确保子类不会意外覆写父类的私有方法和属性.不是为了保护外部意外访问而设计的！

例如:

    >>> class Foo(object):
    ...     def __init__(self):
    ...         self.__baz = 42
    ...     def foo(self):
    ...         print self.__baz
    ...
    >>> class Bar(Foo):
    ...     def __init__(self):
    ...         super(Bar, self).__init__()
    ...         self.__baz = 21
    ...     def bar(self):
    ...         print self.__baz
    ...
    >>> x = Bar()
    >>> x.foo()
    42
    >>> x.bar()
    21
    >>> print x.__dict__
    {'_Bar__baz': 21, '_Foo__baz': 42}

当然，这对于两个同名的类没有作用

另外，可以查看diveintopython的解释 [入口](http://www.faqs.org/docs/diveintopython/fileinfo_private.html#d0e11521)

### Python中类方法的作用是什么

问题 [链接](http://stackoverflow.com/questions/38238/what-are-class-methods-in-python-for)


我现在意识到，我不需要像我在使用java的static方法那样使用类方法，但是我不确定什么时候使用

谁能通过一个好的例子解释下Python中的类方法，至少有人能告诉我什么时候确实需要使用类方法


类方法用在：当你需要使用不属于任何明确实例的方法,但同时必须涉及类.有趣的是，你可以在子类中覆写，这在Java的static方法和Python的模块级别函数中是不可能做到的

如果你有一个MyClass, 并且一个模块级别函数操作MyClass(工厂，依赖注入桩等等), 声明一个类方法.然后这个类方法可以在子类中调用

### Python中 __new__ 和 __init__的用法

问题 [链接](http://stackoverflow.com/questions/674304/pythons-use-of-new-and-init)

我很疑惑，为何__init__总是在__new__之后调用

如下

    class A(object):
        _dict = dict()

        def __new__(cls):
            if 'key' in A._dict:
                print "EXISTS"
                return A._dict['key']
            else:
                print "NEW"
                return super(A, cls).__new__(cls)

        def __init__(self):
            print "INIT"
            A._dict['key'] = self
            print ""

    a1 = A()
    a2 = A()
    a3 = A()

输出

    NEW
    INIT

    EXISTS
    INIT

    EXISTS
    INIT

有木有人可以解释一下

来自 [链接](http://mail.python.org/pipermail/tutor/2008-April/061426.html)


使用__new__,当你需要控制一个实例的生成

使用__init__,当你需要控制一个实例的初始化

__new__是实例创建的第一步.最先被调用，并且负责返回类的一个新实例.

相反的,__init__不返回任何东西，只是负责在实例创建后进行初始化

通常情况下，你不必重写__new__除非你写一个子类继承不可变类型，例如str,int,unicode或tuple


你必须了解到，你尝试去做的用[Factory](http://en.wikipedia.org/wiki/Factory_object)可以很好地解决，并且是最好的解决方式.使用__new__不是一个简洁的处理方式,一个[factory例子](http://code.activestate.com/recipes/86900/)


### 如何获取一个实例的类名

问题 [链接](http://stackoverflow.com/questions/510972/getting-the-class-name-of-an-instance-in-python)

    x.__class__.__name__

### @staticmethod和@classmethod的区别

问题 [链接](http://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python)

staticmethod，静态方法在调用时，对类及实例一无所知

仅仅是获取传递过来的参数，没有隐含的第一个参数，在Python里基本上用处不大，你完全可以用一个模块函数替换它

classmethod, 在调用时，将会获取到其所在的类，或者类实例，作为其第一个参数

当你想将函数作为一个类工厂时，这非常有用: 第一个参数是类，你可以实例化出对应实例对象，甚至子类对象。

可以观察下 dict.fromkey(),是一个类方法，当子类调用时，返回子类的实例

    >>> class DictSubclass(dict):
    ...     def __repr__(self):
    ...         return "DictSubclass"
    ...
    >>> dict.fromkeys("abc")
    {'a': None, 'c': None, 'b': None}
    >>> DictSubclass.fromkeys("abc")
    DictSubclass
    >>>

###  如何定义静态方法(static method)

问题 [链接](http://stackoverflow.com/questions/735975/static-methods-in-python)

使用 [staticmethod](http://docs.python.org/2/library/functions.html#staticmethod)装饰器


    class MyClass(object):
        @staticmethod
        def the_static_method(x):
            print x
    MyClass.the_static_method(2) # outputs 2

### Python中的类变量(环境变量)

问题 [链接](http://stackoverflow.com/questions/68645/static-class-variables-in-python)

在类中定义的变量，不在方法定义中，成为类变量或静态变量

    >>> class MyClass:
    ...     i = 3
    ...
    >>> MyClass.i
    3

i是类级别的变量，但这里要和实例级别的变量i区分开

    >>> m = MyClass()
    >>> m.i = 4
    >>> MyClass.i, m.i
    >>> (3, 4)

这和C++/java完全不同，但和C#区别不大，C#不允许类实例获取静态变量

具体见 [what the Python tutorial has to say on the subject of classes and class objects](http://docs.python.org/2/tutorial/classes.html#SECTION0011320000000000000000)

另外，静态方法

    class C:
        @staticmethod
        def f(arg1, arg2, ...): ...

### 如何判断一个对象是否拥有某个属性

问题 [链接](http://stackoverflow.com/questions/610883/how-to-know-if-an-object-has-an-attribute-in-python)

    if hasattr(a, 'property'):
        a.property

两种风格

EAFP(easier to ask for forgiveness than permission)

LBYL(look before you leap)

相关内容
[EAFP vs LBYL (was Re: A little disappointed so far)](http://web.archive.org/web/20070929122422/http://mail.python.org/pipermail/python-list/2003-May/205182.html)
[EAFP vs. LBYL @Code Like a Pythonista: Idiomatic Python](http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#eafp-vs-lbyl)

    try:
        doStuff(a.property)
    except AttributeError:
        otherStuff()
    or

    if hasattr(a, 'property'):
        doStuff(a.property)
    else:
        otherStuff()

### Python中有没有简单优雅的方式定义单例类

问题 [链接](http://stackoverflow.com/questions/31875/is-there-a-simple-elegant-way-to-define-singletons-in-python)

我不认为有必要，一个拥有函数的模块（不是类）可以作为很好的单例使用，它的所有变量被绑定到这个模块，无论如何都不能被重复实例化

如果你确实想用一个类来实现，在python中不能创建私有类或私有构造函数,所以你不能隔离多个实例而仅仅通过自己的API来访问属性

我还是认为将函数放入模块，并将其作为一个单例来使用是最好的办法

### 理解Python的Super()和init方法

问题 [链接](http://stackoverflow.com/questions/576169/understanding-python-super-and-init-methods)

尝试着去理解super().从表面上看，两个子类都能正常创建.我只是好奇他们两者之间的不同点

    class Base(object):
        def __init__(self):
            print "Base created"

    class ChildA(Base):
        def __init__(self):
            Base.__init__(self)

    class ChildB(Base):
        def __init__(self):
            super(ChildB, self).__init__()

    print ChildA(),ChildB()

回答

Super让你避免明确地引用基类，这是一点。最大的优势是，当出现多重继承的时候，各种[有趣的情况](http://www.artima.com/weblogs/viewpost.jsp?thread=236275)就会出现。查看super[官方文档](http://docs.python.org/library/functions.html#super).

另外注意，在Python3.0中，可以使用super().__init__() 代替 super(ChildB, self).__init__().IMO略有优势.


### 在Python中，如何判断一个对象iterable?

问题 [链接](http://stackoverflow.com/questions/1952464/in-python-how-do-i-determine-if-an-object-is-iterable)

1. 检查__iter__对序列类型有效，但是对例如string，无效


        try:
            iterator = iter(theElement)
        except TypeError:
            # not iterable
        else:
            # iterable

        # for obj in iterator:
        #     pass

2. 使用collections

        import collections

        if isinstance(e, collections.Iterable):
            # e is iterable

### 构建一个基本的Python迭代器

问题[链接](http://stackoverflow.com/questions/19151/build-a-basic-python-iterator)

在Python中，迭代器对象遵循迭代器协议，这意味着它提供了两种方法: `__iter__()`和`next()`。`__iter__()`返回一个迭代器对象并且在循环开始时就隐式的被调用。`next()`方法返回下一个值，并在循环的每一次增量中被调用。当没有值需要返回时，`next()`引发一个StopIteration异常，这个异常被循环结构隐式的捕获从而停止迭代。

这有一个简单计数例子：

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

上述会打印出：

    3
    4
    5
    6
    7
    8

 这个用生成器写会更简单一些，下面是之前答案的翻写：

    def counter(low, high):
        current = low
        while current <= high:
            yield current
            current += 1

    for c in counter(3, 8):
        print c

打印出来的内容是一样的。在后台，生成器对象支持迭代器协议，大体上对Counter类做一些同样事情。

[Iterators and Simple Generators](http://www.ibm.com/developerworks/library/l-pycon.html)，David Mertz的这篇文章，是一篇对迭代器非常好的介绍。

### 在Python中，抽象类和接口有什么区别？

问题[链接](http://stackoverflow.com/questions/372042/difference-between-abstract-class-and-interface-in-python)

看看下面这个：

    class Abstract1(object):
        """Some description that tells you it's abstract,
        often listing the methods you're expected to supply."""
        def aMethod(self):
            raise NotImplementedError( "Should have implemented this" )

因为在Python中没有（也不需要）一个正式的接口协议，类Java的抽象类和接口的区别并不存在。如果有人尝试定义一个正式的接口，它其实也是一个抽象类。唯一的不同就是在文档注释的表述。

并且当你使用鸭子类型时，抽象类和接口的区别有点吹毛求疵了。

Java使用接口是因为它没有多重继承。

因为Python有多重继承，你可能还会看到类似这样的东西：

    class SomeAbstraction( object ):
        pass # lots of stuff - but missing something

    class Mixin1( object ):
        def something( self ):
            pass # one implementation

    class Mixin2( object ):
        def something( self ):
            pass # another

    class Concrete1( SomeAbstraction, Mixin1 ):
        pass

    class Concrete2( SomeAbstraction, Mixin2 ):
        pass

这是一种使用混合抽象超类去创建不相交的具体子类的方法。

### Python 的__slots__

问题[链接](http://stackoverflow.com/questions/472000/python-slots)

引用[Jacob Hallen](http://code.activestate.com/lists/python-list/531365/)：

`__slots__`的正确使用方法是保存对象的空间。取代使用允许任何时间给类添加属性的动态字典，有一种在创建之后不允许添加的静态结构。使用slots节省了给所有对象同一个字典的系统开销。有时候这是一个很有效的优化，但它也会变得毫无用处，前提是Python的解释器足够动态化，可以在确实需要为对象增加某些东西时只需要字典。

不幸的是，使用slots有一个副作用。他们通过一种方法改变了那些带有slots的对象的表现形式，使它们被古怪的控制者和细小的静态归类滥用。这很糟糕，因为古怪的控制者应该滥用元类，而细小的静态归类应该滥用生成器。但是从Python开始，只有这一种显著的方法了。

将CPython做的很聪明，聪明到可以不用`__slots__`保存空间，是一个主要的工作，这也就是为什么它不在P3k的更改列表中（到目前为止）。

### Python中，新式类和旧式类的区别

问题[链接](http://stackoverflow.com/questions/54867/what-is-the-difference-between-old-style-and-new-style-classes-in-python)

根据[https://docs.python.org/2/reference/datamodel.html#new-style-and-classic-classes](https://docs.python.org/2/reference/datamodel.html#new-style-and-classic-classeshttps://docs.python.org/2/reference/datamodel.html#new-style-and-classic-classes):

    Up to Python 2.1, old-style classes were the only flavour available to the user. The concept of (old-style) class is unrelated to the concept of type: if x is an instance of an old-style class, then x.__class__ designates the class of x, but type(x) is always <type 'instance'>. This reflects the fact that all old-style instances, independently of their class, are implemented with a single built-in type, called instance.

    New-style classes were introduced in Python 2.2 to unify classes and types. A new-style class neither more nor less than a user-defined type. If x is an instance of a new-style class, then type(x) is the same as x.__class__.

    The major motivation for introducing new-style classes is to provide a unified object model with a full meta-model. It also has a number of immediate benefits, like the ability to subclass most built-in types, or the introduction of "descriptors", which enable computed properties.

    For compatibility reasons, classes are still old-style by default. New-style classes are created by specifying another new-style class (i.e. a type) as a parent class, or the "top-level type" object if no other parent is needed. The behaviour of new-style classes differs from that of old-style classes in a number of important details in addition to what type returns. Some of these changes are fundamental to the new object model, like the way special methods are invoked. Others are "fixes" that could not be implemented before for compatibility concerns, like the method resolution order in case of multiple inheritance.

    Python 3 only has new-style classes. No matter if you subclass from object or not, classes are new-style in Python 3. It is however recommended that you still subclass from object.

### Python中，@property和设置-获取哪一个更好

问题[链接](http://stackoverflow.com/questions/6618002/python-property-versus-getters-and-setters)

用属性更好，这也是他们存在的原因。

原因是在Python中，所有属性都是公共的。名字由单下划线或双下划线开始的，只不过是一个警告，表示这个属性的值在只是一个执行细节，在未来的版本中可能不会保持一致。他并没有阻止你去获取或者设置这个属性。因此，标准的属性访问途径便是是公认最好的，Pythonic的。

属性的优点是他们和访问属性的语法上保持一致，所以你可以在不改变客户端的情况下把属性从一个改变成另一个值。你甚至可以有一个不再生产环境版本的类用来保存属性，不用改变代码就可以使用它们（用来debug或者上下文代码）。同时，你不需要为所有东西写获取和设置因为在之后你可能需要更好的控制。

### 在Python中，链式调用父类构造器

问题[链接](http://stackoverflow.com/questions/904036/chain-calling-parent-constructors-in-python)

你正在做的事情，确实是值得推荐的（对于Python 2.x来说）

是否把类明确的传递给`super`是一个风格而不是功能上的问题。把类明确的传递给`super`符合Python哲学的“明了胜于晦涩”。

### Python中，一个对象前面带单下划线和双下划线的含义

问题[链接](http://stackoverflow.com/questions/1301346/the-meaning-of-a-single-and-a-double-underscore-before-an-object-name-in-python)

单下划线

在一个类中，单下划线开头的单纯为了告诉其他程序员，这些属性或者方法意味着私有的。然而，这些属性或者方法本身并没什么特别的。

引述[PEP-8](http://www.python.org/dev/peps/pep-0008/)：

    _single_leading_underscore: weak "internal use" indicator. E.g. from M import * does not import objects whose name starts with an underscore.

双下划线

来自[Python文档](http://docs.python.org/tutorial/classes.html#private-variables-and-class-local-references)：

    Any identifier of the form __spam (at least two leading underscores, at most one trailing underscore) is textually replaced with _classname__spam, where classname is the current class name with leading underscore(s) stripped. This mangling is done without regard to the syntactic position of the identifier, so it can be used to define class-private instance and class variables, methods, variables stored in globals, and even variables stored in instances. private to this class on instances of other classes.

同一页还有一个警告：

    Name mangling is intended to give classes an easy way to define “private” instance variables and methods, without having to worry about instance variables defined by derived classes, or mucking with instance variables by code outside the class. Note that the mangling rules are designed mostly to avoid accidents; it still is possible for a determined soul to access or modify a variable that is considered private.

举例

    >>> class MyClass():
    ...     def __init__(self):
    ...             self.__superprivate = "Hello"
    ...             self._semiprivate = ", world!"
    ...
    >>> mc = MyClass()
    >>> print mc.__superprivate
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: myClass instance has no attribute '__superprivate'
    >>> print mc._semiprivate
    , world!
    >>> print mc.__dict__
    {'_MyClass__superprivate': 'Hello', '_semiprivate': ', world!'}

### 在一个已存在的对象里，加一个方法

问题[链接](http://stackoverflow.com/questions/972/adding-a-method-to-an-existing-object)

在Python中，函数和约束方法还是有一些区别。

    >> def foo():
    ...     print "foo"
    ...
    >>> class A:
    ...     def bar( self ):
    ...         print "bar"
    ...
    >>> a = A()
    >>> foo
    <function foo at 0x00A98D70>
    >>> a.bar
    <bound method A.bar of <__main__.A instance at 0x00A9BC88>>
    >>>

约束方法被约束到一个实例上，当方法调用时这个实例会被当做第一个参数传入。

在类（与实例相反）中，那些作为属性的可调用者仍然能是有限制的，尽管，你可以随时修改这个类的定义。

    >>> def fooFighters( self ):
    ...     print "fooFighters"
    ...
    >>> A.fooFighters = fooFighters
    >>> a2 = A()
    >>> a2.fooFighters
    <bound method A.fooFighters of <__main__.A instance at 0x00A9BEB8>>
    >>> a2.fooFighters()
    fooFighters

这样之前定义的实例也回随着更新（只要他们没有重写这个属性）：

    >>> a.fooFighters()
    fooFighters

问题出现在当你想把一个方法固定在某一个实例时：

    >>> def barFighters( self ):
    ...     print "barFighters"
    ...
    >>> a.barFighters = barFighters
    >>> a.barFighters()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: barFighters() takes exactly 1 argument (0 given)

当你想直接固定到一个实例上时，函数不是自动约束的:

    >>> a.barFighters
    <function barFighters at 0x00A98EF0>

为了绑定它，我盟可以用[types模块中的方法类函数](http://docs.python.org/library/types.html?highlight=methodtype#module-types):

    >>> import types
    >>> a.barFighters = types.MethodType( barFighters, a )
    >>> a.barFighters
    <bound method ?.barFighters of <__main__.A instance at 0x00A9BC88>>
    >>> a.barFighters()
    barFighters

这时候，类的其他实例不会受到影响：

    >>> a2.barFighters()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AttributeError: A instance has no attribute 'barFighters'

更多的信息，可以在阅读[descriptors](http://users.rcn.com/python/download/Descriptor.htm)和[metaclass](http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html)以及[programming](http://www.gnosis.cx/publish/programming/metaclass_2.html)中发现。

### 在Python中，metaclass是什么

问题[链接](http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python/6581949#6581949)

**类对象**

在理解metaclass之前，你需要掌握Python中的类。而且Python的类的设计，非常的特别，借鉴了Smalltalk语言。

大多数语言中，类只是一段代码用来描述如何生产一个对象。在Python中也有几分这个意思：

    >>> class ObjectCreator(object):
    ...       pass
    ...

    >>> my_object = ObjectCreator()
    >>> print(my_object)
    <__main__.ObjectCreator object at 0x8974f2c>

但是Python中的类不仅仅如此。类，也是对象。

对，对象。

当你使用`class`这个关键字时，Python执行它并创造一个对象，示例：

    >>> class ObjectCreator(object):
    ...       pass
    ...

在内存中创建了一个对象名字是"ObjectCreator"。

这个对象（类）有能力创造对象（实例），这也是为什么它是类。

但它仍然是一个类，因此：

 - 你可以把它当做一个变量

 - 你可以复制它

 - 你可以给它添加属性

 - 你可以把它当成一个函数的参数

举例：

    >>> print(ObjectCreator) # you can print a class because it's an object
    <class '__main__.ObjectCreator'>
    >>> def echo(o):
    ...       print(o)
    ...
    >>> echo(ObjectCreator) # you can pass a class as a parameter
    <class '__main__.ObjectCreator'>
    >>> print(hasattr(ObjectCreator, 'new_attribute'))
    False
    >>> ObjectCreator.new_attribute = 'foo' # you can add attributes to a class
    >>> print(hasattr(ObjectCreator, 'new_attribute'))
    True
    >>> print(ObjectCreator.new_attribute)
    foo
    >>> ObjectCreatorMirror = ObjectCreator # you can assign a class to a variable
    >>> print(ObjectCreatorMirror.new_attribute)
    foo
    >>> print(ObjectCreatorMirror())
    <__main__.ObjectCreator object at 0x8997b4c>

动态创建类

类就是对象，你可以快速创建它，像任何其他对象一样。

首先，你可以在一个函数里创建一个类，用`class`:

    >>> def choose_class(name):
    ...     if name == 'foo':
    ...         class Foo(object):
    ...             pass
    ...         return Foo # return the class, not an instance
    ...     else:
    ...         class Bar(object):
    ...             pass
    ...         return Bar
    ...
    >>> MyClass = choose_class('foo')
    >>> print(MyClass) # the function returns a class, not an instance
    <class '__main__.Foo'>
    >>> print(MyClass()) # you can create an object from this class
    <__main__.Foo object at 0x89c6d4c>

但是它不是很动态，你仍然需要手写你的类。

既然类是对象，他们一定可以被什么东西生成。

当你使用`class`关键字时，Python自动创建了这个对象，但是像Python中的其他东西一样，它给你了一个方法手动实现。

还记得`type`函数吗。一个让你知道对象类型的古老的函数：

    >>> print(type(1))
    <type 'int'>
    >>> print(type("1"))
    <type 'str'>
    >>> print(type(ObjectCreator))
    <type 'type'>
    >>> print(type(ObjectCreator()))
    <class '__main__.ObjectCreator'>

哦，`type`有另外一种完全不同的功能，它也可以迅速创建类。`type`可以把类的描述作为参数，并返回一个类。

（我知道同一个函数根据你传入的值有两种不同的用法是很蠢的，但是它是Python中的一种向后兼容的问题）

`type`这样工作：

    type(name of the class,
         tuple of the parent class (for inheritance, can be empty),
         dictionary containing attributes names and values)

举个例子

    >>> class MyShinyClass(object):
    ...       pass

可以通过这种方法手动生成：

    >>> MyShinyClass = type('MyShinyClass', (), {}) # returns a class object
    >>> print(MyShinyClass)
    <class '__main__.MyShinyClass'>
    >>> print(MyShinyClass()) # create an instance with the class
    <__main__.MyShinyClass object at 0x8997cec>

你可能会注意到我们使用"MyShinyClass"做为类的名字并且作为变量并且作为类的参考。他们可以不同，但是没有必要把事情搞复杂。

`type`接受一个字典，定义一个类的参数，所以：

    >>> class Foo(object):
    ...       bar = True

可以理解成：

    >>> Foo = type('Foo', (), {'bar':True})

并且可以当成一个普通类来使用：

    >>> print(Foo)
    <class '__main__.Foo'>
    >>> print(Foo.bar)
    True
    >>> f = Foo()
    >>> print(f)
    <__main__.Foo object at 0x8a9b84c>
    >>> print(f.bar)
    True

当然，你可以继承它，所以：

    >>>   class FooChild(Foo):
    ...         pass

可以是：

    >>> FooChild = type('FooChild', (Foo,), {})
    >>> print(FooChild)
    <class '__main__.FooChild'>
    >>> print(FooChild.bar) # bar is inherited from Foo
    True

最后你可能想要在你的类里添加方法。只要适当的定义一个函数，然后把它标记为属性。

    >>> def echo_bar(self):
    ...       print(self.bar)
    ...
    >>> FooChild = type('FooChild', (Foo,), {'echo_bar': echo_bar})
    >>> hasattr(Foo, 'echo_bar')
    False
    >>> hasattr(FooChild, 'echo_bar')
    True
    >>> my_foo = FooChild()
    >>> my_foo.echo_bar()
    True

可以回顾一下：在Python中，类就是对象，你可以动态的创造一个类。

这就是当你使用`class`关键字时Python做的事情，使用metaclass时，也是一样的。

**什么是metaclass（最终版本）**

Metaclass是创建类的原料。

你定义类就是为了创建对象，对不对？

但是我们知道Python类本身就是对象。

所以，这些对象就是metaclass创建的。他们是类的类，你可以这样表述：

    MyClass = MetaClass()
    MyObject = MyClass()

刚才你看到了`type`允许你做类似这样的事情：

    MyClass = type('MyClass', (), {})

这是因为`type`这个函数实际上是一个metaclass。`type`就是metaclass -- Python用来在后台创造一切类。

现在你知道为什么这个东西他喵的写成小写的，而不是`Type`了吧。

嗯，我想同样的问题可能发生在用来创造字符串对象的`str`这个类上，`int`是创造整数对象的类，`type`是用来创造类对象的类。

通过查看`__class__`参数验证。

所有的东西，我是说所有，在Python中都是对象。包括整数，字符串，函数，类。他们全是对象。他们全都由一个类创造而来：

    >>> age = 35
    >>> age.__class__
    <type 'int'>
    >>> name = 'bob'
    >>> name.__class__
    <type 'str'>
    >>> def foo(): pass
    >>> foo.__class__
    <type 'function'>
    >>> class Bar(object): pass
    >>> b = Bar()
    >>> b.__class__
    <class '__main__.Bar'>

现在，看看所有的`__class__`的`__class__`是什么？

    >>> age.__class__.__class__
    <type 'type'>
    >>> name.__class__.__class__
    <type 'type'>
    >>> foo.__class__.__class__
    <type 'type'>
    >>> b.__class__.__class__
    <type 'type'>

所以，metaclass就是用来创造类对象的原料。

如果你想，你可以把他叫做类工厂。

`type`是Python使用的内建的metaclass，当然，你可以创造你自己的metaclass。

**`__metaclass__`属性**

你可以给你写的类添加一个`__metaclass__`属性:

    class Foo(object):
      __metaclass__ = something...
      [...]

如果你这样做，Python会使用metaclass创建`Foo`这个类。

小心点，这很复杂。

你先写了`class Foo(object)`，但是现在在内存中，还没有创建这个类对象`Foo`。

Python会在类的定义时，检查`__metaclass__`。如果找到了，Python就用它创造一个类对象`Foo`。如果没有，就用`type`创造类。

多读几次。

当你这样：

    class Foo(Bar):
      pass

Python会做下面这些事情：

`Foo`里面有`__metaclass__`这个属性吗？

如果有，在内存中创建一个类对象（我是说一个类对象，与我同在）通过使用`__metaclass__`创建一个同样的名字`Foo`。

如果Python找不到`__metaclass__`，它会在模块层找这个`__metaclass__`，试图通过同样的方式。（但是仅对于那些没有继承任何东西的类，基本上都是旧式类）

之后，如果哪都找不到`__metaclass__`，就使用`Bar`（第一层父类）自带的metaclass（有可能就是缺省的`type`）来创建类对象。

注意，这里的`__metaclass__`不会被继承，父类的会被继承(`Bar.__class__`)。如果`Bar`使用一个用`type`（而不是`type.__new__()`）创建`Bar`本身的`__metaclass__`属性，那么子类不会继承这个行为。

现在一个大问题出现了，你可以在`__metaclass__`里面放什么呢？

答案是：一些可以创建类的东西。

然而什么可以创建类的呢？`type`或者是它的任何子类，或者使用它的东西。

**惯用的metaclass **

一个metaclass的主要目的就是当一个类创建的时候，自动的改变它。

你通常对接口做这些事情，比如你想要创建一个符合当前上下文的类。

试想一个愚蠢的例子，你决定让你的模块里的所有类的所有属性都用大写。有几种方法可以实现，其中一种是在模块层使用`__metaclass__`。

通过这种方法，该模块的所有类在创建时都会使用这个metaclass，而我们只需要告诉metaclass把所有属性都变成大写。

幸运的是，`__metaclass__`可以通过任何方式调用，不需要一个正规的类（我知道，有些名字里带着class的东西不一定是类，想想看吧，它很有用）。

所以我们通过一个函数，从简单的例子开始：

    # the metaclass will automatically get passed the same argument
    # that you usually pass to `type`
    def upper_attr(future_class_name, future_class_parents, future_class_attr):
      """
        Return a class object, with the list of its attribute turned
        into uppercase.
      """

      # pick up any attribute that doesn't start with '__' and uppercase it
      uppercase_attr = {}
      for name, val in future_class_attr.items():
          if not name.startswith('__'):
              uppercase_attr[name.upper()] = val
          else:
              uppercase_attr[name] = val

      # let `type` do the class creation
      return type(future_class_name, future_class_parents, uppercase_attr)

    __metaclass__ = upper_attr # this will affect all classes in the module

    class Foo(): # global __metaclass__ won't work with "object" though
      # but we can define __metaclass__ here instead to affect only this class
      # and this will work with "object" children
      bar = 'bip'

    print(hasattr(Foo, 'bar'))
    # Out: False
    print(hasattr(Foo, 'BAR'))
    # Out: True

    f = Foo()
    print(f.BAR)
    # Out: 'bip'

现在，我们做同样的事情，但是对metaclass使用真正的类：

    # remember that `type` is actually a class like `str` and `int`
    # so you can inherit from it
    class UpperAttrMetaclass(type):
        # __new__ is the method called before __init__
        # it's the method that creates the object and returns it
        # while __init__ just initializes the object passed as parameter
        # you rarely use __new__, except when you want to control how the object
        # is created.
        # here the created object is the class, and we want to customize it
        # so we override __new__
        # you can do some stuff in __init__ too if you wish
        # some advanced use involves overriding __call__ as well, but we won't
        # see this
        def __new__(upperattr_metaclass, future_class_name,
                    future_class_parents, future_class_attr):

            uppercase_attr = {}
            for name, val in future_class_attr.items():
                if not name.startswith('__'):
                    uppercase_attr[name.upper()] = val
                else:
                    uppercase_attr[name] = val

            return type(future_class_name, future_class_parents, uppercase_attr)

但是这并不符合面向对象的思想。我们直接调用`type`，不重写或者调用父类的`__new__`方法。试一下：

    class UpperAttrMetaclass(type):

        def __new__(upperattr_metaclass, future_class_name,
                    future_class_parents, future_class_attr):

            uppercase_attr = {}
            for name, val in future_class_attr.items():
                if not name.startswith('__'):
                    uppercase_attr[name.upper()] = val
                else:
                    uppercase_attr[name] = val

            # reuse the type.__new__ method
            # this is basic OOP, nothing magic in there
            return type.__new__(upperattr_metaclass, future_class_name,
                                future_class_parents, uppercase_attr)

你可能会主要到多余的参数`upperattr_metaclass`。它没什么特殊的：一个方法总是接受当前的实例作为第一个参数。就像你在普通的方法中使用`self`。

当然，我这里使用这么长的名字是为了更清楚，但是像`self`一样，所有参数有惯用的名字。所以一个真正的生产环境的metaclass看起来可能是这样：

    class UpperAttrMetaclass(type):

        def __new__(cls, clsname, bases, dct):

            uppercase_attr = {}
            for name, val in dct.items():
                if not name.startswith('__'):
                    uppercase_attr[name.upper()] = val
                else:
                    uppercase_attr[name] = val

            return type.__new__(cls, clsname, bases, uppercase_attr)

我们可以通过使用`super`简化继承，让它更清晰。（因此，你可以拥有metaclasses，继承metaclass，继承type）

    class UpperAttrMetaclass(type):

        def __new__(cls, clsname, bases, dct):

            uppercase_attr = {}
            for name, val in dct.items():
                if not name.startswith('__'):
                    uppercase_attr[name.upper()] = val
                else:
                    uppercase_attr[name] = val

            return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)

差不多就这样，metaclass真没什么更多的内容了。

使用metaclass的代码非常复杂的背后原因不是metaclass本身，而是你把metaclass用在了那些自我实现，多重继承的东西上，比如`__dict__`等等。

总之，metaclass有特殊的技巧实现黑魔法，当然包括复杂的东西。但是对他们自己来说，他们很简单：

 - 拦截一个类的创建

 - 装饰一个类

 - 返回装饰过的类

**为什么使用metaclass替代函数**

既然`__metaclass__`可以接受任何调用，为什么你还要使用明显更复杂的类呢？

有几个原因：

 - 目的更明确。当你看到`UpperAttrMetaclass(type)`的时候就，你知道接下去会发生什么

 - 你可以使用面向对象，metaclass可以继承metaclass，重写父类的方法，Metaclass也可以使用metaclass。

 - 你可以更好的组织你的代码结构。不要像上面的例子哪样琐碎的使用metaclass。对某些东西来说它通常是复杂的。创造几个方法并把它们整合到一个类里是很有用的，可以让代码更易读。

 - 关联使用`__new__`，`__init__`，和`__call__`。它们允许你做不同的东西，尽管你可以把它们都做在`__new__`里面，有些人用`__init__`更舒服。

 - 这些都叫metaclass，靠，它们肯定很有意义。

**你他喵为什么会使用metaclass**

现在有一个大问题，为什么使用这种倾向于引起不清晰的错误的特性？

通常你不会这样：

    Metaclass的99%的使用者都不必担心它的深度魔法。如果你不知道你是否需要它们，就别用（那些需要它们的人知道为何用它们，而且不需要解释）

*Python Guru Tim Peters*

metaclass的主要作用就是创造一个接口。典型的用法就是Django ORM。

它允许你这样定义这些东西：

    class Person(models.Model):
        name = models.CharField(max_length=30)
        age = models.IntegerField()

但是你这样用：

    guy = Person(name='bob', age='35')
    print(guy.age)

它不会返回一个`IntegerField`对象。它会返回一个`int`，甚至能直接从数据库里拿。

这可能是由于`models.Model`为它定义了`__metaclass__`，使用一些魔法方法，让你可以定义一些可以做复杂的事情的简单声明关联数据库。

Django让一些复杂的事情看起来很简单，通过暴露一个简单的接口，使用metaclass，重构了接口的代码让真正的行为在幕后执行。

**结语**

首先你知道类是对象而且可以创建实例。

实际上，类本身也是实例，是metaclass的实例。

    >>> class Foo(object): pass
    >>> id(Foo)
    142630324

所有的东西都是对象，在Python中，它们不是一个类的实例，就是metaclass的实例。

除了`type`。

`type`是它自己的metaclass。这些东西在纯净的Python环境下是看不到的，他们在执行层做了一些交互来实现。

第二，metaclass是复杂的。你不需要在每一个简单的类里使用它。你可以用两种不同的方法来改变一个类：

 - [monkey patching](http://en.wikipedia.org/wiki/Monkey_patch)

 - 类的装饰器

99%的当你需要改变一个类的时刻，你需要用这些东西。

但是99%的时间里，你不根本不需要改变一个类。

### Python的"最小惊奇"：多重默认参数

问题[链接](http://stackoverflow.com/questions/1132941/least-astonishment-in-python-the-mutable-default-argument)

实际上，这不是一个设计瑕疵，而且不它不是因为内部或者表现问题。

它单纯是来自Python中，函数是第一梯队的对象的事实，而且不仅仅是一段代码。

从这个角度，你会发现它很明智：一个函数是一个对象取决于它的定义；默认参数是一种类似丛书数据，而且它们的状态可能从一次到另一次的调用过程中发生改变-和在其他对象中一样。

不管怎样，Effbot在[Default Parameter Values in Python](http://effbot.org/zone/default-values.htm)中对这种表现有一个很好的解释。

我发现它很干净，我强烈推荐阅读以下，并且对函数对象是如何工作的掌握更多知识。