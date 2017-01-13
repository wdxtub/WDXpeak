
### \_\_init\_\_.py是做什么用的

问题 [链接](http://stackoverflow.com/questions/448271/what-is-init-py-for)


这是包的一部分，[具体文档](http://docs.python.org/2/tutorial/modules.html#packages)

\_\_init\_\_.py让Python把目录当成包，

最简单的例子，\_\_init\_\_.py仅是一个空文件，但它可以一样执行包初始化代码或者设置\_\_all\_\_变量，后续说明

### 如何使用绝对路径import一个模块

问题 [链接](http://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path)


    import imp

    foo = imp.load_source('module.name', '/path/to/file.py')
    foo.MyClass()

###  获取Python模块文件的路径

问题 [链接](http://stackoverflow.com/questions/247770/retrieving-python-module-path)

如何才能获取一个模块其所在的路径

回答

    import a_module
    print a_module.__file__

获取其所在目录，可以

    import os
    path = os.path.dirname(amodule.__file__)

### 谁可以解释一下__all__么？


问题 [链接](http://stackoverflow.com/questions/44834/can-someone-explain-all-in-python)

该模块的公有对象列表

__all__指定了使用import module时，哪些对象会被import进来.其他不在列表里的不会被导入

    __all__ = ["foo", "bar"]

it's a list of public objects of that module -- it overrides the default of hiding everything that begins with an underscore

### 如何重新加载一个python模块

问题 [链接](http://stackoverflow.com/questions/437589/how-do-i-unload-reload-a-python-module)

使用reload内置函数

    reload(module_name)


    import foo

    while True:
        # Do some things.
        if is_changed(foo):
            foo = reload(foo)

### 在Python中，如何表示Enum(枚举)

问题[链接](http://stackoverflow.com/questions/36932/how-can-i-represent-an-enum-in-python)

Enums已经添加进了Python 3.4，详见PEP435。同时在pypi下被反向移植进了3.3，3.2，3.1，2.7，2.6，2.5和2.4。

通过`$ pip install enum34`来使用向下兼容的Enum，下载`enum`（没有数字）则会安装完全不同并且有冲突的版本。

    from enum imoprt Enum
    Animal = Enum(‘Animal’, ‘ant bee cat dog’)

等效的：
    
    class Animals(Enum):
        ant = 1
        bee = 2
        cat = 3
        dog = 4

在早期的版本中，实现枚举的一种方法是：

    def enum(**enums):
        return type(‘Enum’, (), enums)

使用起来像这样：

    >>> Numbers = enum(ONE=1, TWO=2, THREE='three')
    >>> Numbers.ONE
    1
    >>> Numbers.TWO
    2
    >>> Numbers.THREE
    'three'

也可以轻松的实现自动列举像下面这样：

    def enum(*squential, **named):
        enums = dict(zip(sequential, range(len(sequential))), **named)
        return type(‘Enum’, (), enums)

使用起来像这样：

    >>> Numbers = enum('ZERO', 'ONE', 'TWO')
    >>> Numbers.ZERO
    0
    >>> Numbers.ONE
    1

支持把值转换为名字，可以这样添加：

    def enum(*sequential, **named):
        enums = dict(zip(sequential, range(len(sequential))), **named)
        reverse = dict((value, key) for key, value in enums.iteritems())
        enums['reverse_mapping'] = reverse
        return type('Enum', (), enums)

这将会根据名字重写任何东西，但是对于渲染你打印出的枚举值很有效。如果反向映射不存在，它会抛出KeyError。看一个例子：

    >>> Numbers.reverse_mapping[‘three’]
    ’THREE’

### if __name__ == “__main__”做了什么？

问题[链接](http://stackoverflow.com/questions/419163/what-does-if-name-main-do)

稍微拓展一下Harley的答案...

当Python的解释器读一个源文件时，它执行了里面能找到的所有代码。在执行之前，它会定义少数几个变量。举个例子，如果Python解释器把该模块（即源文件）当做主程序运行，它就会把特殊的`__name__`变量的值设置为`“__main__”`。如果这个文件被其他模块引用，`__name__`就会被设置为其他模块的名字。

就你的脚本来说，我们假设把它当做主函数来执行，你可能会在命令行上这样用：

    python threading_example.py

设置好特殊变量之后，它会执行`import`声明并加载其他的模块。然后它会预估`def`的缩进，创建一个函数对象和一个指向函数对象的值叫做`myfunction`。之后它将读取`if`语句，确定`__name__`等于`”__main__”`后，执行缩进并展示。

这样做的主要原因是，有时候你写了一个可以直接执行的模块（一个`.py`文件），同时，它也可以被其他模块引用。通过执行主函数检查，你可以让你的代码只在作为主程序时执行，而在被其他模块引用或调用其中的函数时不执行。

[这页](http://ibiblio.org/g2swap/byteofpython/read/module-name.html)可以看到更多的细节。

### 通过相对路径引用一个模块

问题[链接](http://stackoverflow.com/questions/279237/import-a-module-from-a-relative-path)

假设你的两个文件夹都是真实的python包（都有`__init__.py`文件在里面），这里有一个可以安全的把相对路径模块包含进本地的脚本。

我假设你想这样做，因为你需要在脚本中包含一系列的模块。我在许多产品的生产环境和不同的情景下用过这个：调用其他文件夹下的脚本或者在不打开一个新的解释器的情况下在Python中执行。

    import os, sys, inspect
    # realpath() will make your script run, even if you symlink it :)
    cmd_folder = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile( inspect.currentframe() ))[0]))
    if cmd_folder not in sys.path:
        sys.path.insert(0, cmd_folder)

    # use this if you want to include modules from a subfolder
    cmd_subfolder=os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"subfolder")))
    if cmd_subfolder not in sys.path:
        sys.path.insert(0, cmd_subfolder)

    # Info:
    # cmd_folder = os.path.dirname(os.path.abspath(__file__)) # DO NOT USE__file__ !!!
    # __file__ fails if script is called in different ways on Windows
    # __file__ fails if someone does os.chdir() before
    # sys.argv[0] also fails because it doesn't not always contains the path

通过这个途径，确实迫使Python使用你的模块，而不用系统自带的那些。

但是注意。在`egg`文件中的模块会发生什么我确实不知道。可能会失败。如果你知道更好的解决办法请留言，我会花几个小时去改进它。

### Python中如何进行间接引用

问题[链接](http://stackoverflow.com/questions/72852/how-to-do-relative-imports-in-python)

看上去每个人都希望告诉你你该怎么做好过只回答这个问题。

问题在于你在运行一个作为`’__main__’`的模块，向解释器传递mod1.py作为一个参数。

来自[PEP 328](http://stackoverflow.com/questions/72852/how-to-do-relative-imports-in-python)：

    Relative imports use a module's __name__ attribute to determine that module's position in the package hierarchy. If the module's name does not contain any package information (e.g. it is set to '__main__') then relative imports are resolved as if the module were a top level module, regardless of where the module is actually located on the file system.

在Python 2.6中，他们添加了为主模块表现模块关系的功能，[PEP 366](https://www.python.org/dev/peps/pep-0366/)描述了这个功能。