
### Python中声明exception的方法

问题 [链接](http://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python)

在python2.6中定义异常得到警告

    >>> class MyError(Exception):
    ...     def __init__(self, message):
    ...         self.message = message
    ...
    >>> MyError("foo")
    _sandbox.py:3: DeprecationWarning: BaseException.message has been deprecated as of Python 2.6

问题很长，大意如标题

回答

或许我理解错了，但是为什么不这样做

    class MyException(Exception):
        pass
如果要重写什么，例如传递额外参数，可以这么做

    class ValidationError(Exception):
        def __init__(self, message, Errors):

            # Call the base class constructor with the parameters it needs
            Exception.__init__(self, message)

            # Now for your custom code...
            self.Errors = Errors

你可以通过第二个参数传递error 字典, 之后通过e.Errors获取

### 如何人为地抛出一个异常

问题 [链接](http://stackoverflow.com/questions/2052390/how-do-i-manually-throw-raise-an-exception-in-python)

pythonic

    raise Exception("I know python!")

更多可参考 [文档](http://docs.python.org/2/reference/simple_stmts.html#the-raise-statement)

### 如何一行内处理多个异常

问题 [链接](http://stackoverflow.com/questions/6470428/catch-multiple-exceptions-in-one-line-except-block)

我知道可以这么做

    try:
        # do something that may fail
    except:
        # do this if ANYTHING goes wrong
也可以

    try:
        # do something that may fail
    except IDontLikeYourFaceException:
        # put on makeup or smile
    except YouAreTooShortException:
        # stand on a ladder

如果想在一行里处理多个异常的话

    try:
        # do something that may fail
    except IDontLIkeYouException, YouAreBeingMeanException: #没生效
    except Exception, e: #捕获了所有
        # say please
答案

    # as在python2.6,python2.7中仍然可以使用
    except (IDontLIkeYouException, YouAreBeingMeanException) as e:
        pass

### Python assert最佳实践

问题 [链接](http://stackoverflow.com/questions/944592/best-practice-for-python-assert)

有没有代码实例使用assert作为独立代码，而不是仅用来debug

    assert x >= 0, 'x is less than zero'

    类似
    if x < 0:
        raise Exception, 'x is less than zero'

    有什么方法，可以设定一个规则就像 if x \< 0 抛出错误但是不是通过try/except/finally检查的

搞晕了：

    原文 Also, is there any way to set a business rule like if x \< 0 raise error that is always checked without the try/except/finally so, if at anytime throughout the code x is less than 0 an error is raised, like if you set assert x < 0 at the start of a function, anywhere within the function where x becomes less then 0 an exception is raised?

回答1

Assert仅用在，测试那些从不发生的情况！目的是让程序尽早失败

Exception用在，那些可以明确知道会发生的错误，并且建议总是创建自己的异常类


例如，你写一个函数从配置文件中读取配置放入字典，文件格式不正确抛出一个ConfigurationSyntaxError,同时你可以assert返回值非None

在你的例子中，如果x是通过用户接口或外部传递设置的，最好使用exception

如果x仅是同一个程序的内部代码，使用assert

回答2

这个函数是为了能够当x小于0的时候，原子性的抛出一个异常。你可以使用[class descriptors](https://docs.python.org/2/reference/datamodel.html#implementing-descriptors)有一个例子：

    class ZeroException(Exception):
        pass

    class variable(object):
        def __init__(self, value=0):
            self.__x = value

        def __set__(self, obj, value):
            if value < 0:
                raise ZeroException('x is less than zero')

            self.__x  = value

        def __get__(self, obj, objType):
            return self.__x

    class MyClass(object):
        x = variable()

    >>> m = MyClass()
    >>> m.x = 10
    >>> m.x -= 20
    Traceback (most recent call last):
       File "<stdin>", line 1, in <module>
       File "my.py", line 7, in __set__
          raise ZeroException('x is less than zero')
    ZeroException: x is less than zero

### 如何打印到stderr

问题 [链接](http://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python)

经常这么干

    import sys
    sys.stderr.write('spam\n')

    print >> sys.stderr, 'spam'

    from __future__ import print_function
    print('spam', file=sys.stderr)

但是不够pythonic, 有没有更好的方法?

回答

我发现这种方式是最短/灵活/可扩展/可读的做法

    from __future__ import print_function

    def warning(*objs):
        print("WARNING: ", *objs, file=sys.stderr)



