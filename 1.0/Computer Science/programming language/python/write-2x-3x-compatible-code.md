编写兼容Python2.x与3.x代码
=====================
当我们正处于Python2.x到Python3.x的过渡期时，你可能想过是否可以在不修改任何代码的前提下能同时运行在Python2和3中。这看起来还真是一个合理的诉求，但如何开始呢？哪些Python2代码在3.x解释器执行时容易出状况呢？   
####print vs print()
如果你想的和我一样，你或许会说print语句，这是个很好的着手点，先简单展示一下，print在2.x中是一条语句，而在3.x中它是一个关键字或者是保留字。换句话说，因为这个变化涉及到语言的语法，你不可以使用在if语句中，Python仍然没有#ifdef 宏。下面尝试把括号里面的参数打印出来：  
    
    >>> print(“hello World!”)
    hello World!
很酷，这个在Python2和Python3中都可以运行，而且运行的效果是一样的，再来看看下面这段：  
    
    >>> print(10, 20) # python2
    (10,20)
此时，你并没有像前面那样幸运得到一样的结果，Python2中打印的是元组(tuple)，而在Python3中传递多个参数到print()里面时打印的是两个值：  
    
    >>> print(10, 20) # Python 3
    10 20
如果你思考得比较多的话，我们可以检查print是否是一个关键字，keyword模块包含一个关键字列表。print在3.x中不是关键字，可以简单验证一下：  
    
    >>> import keyword
    >>> ‘print’ in keyword.kwlist
    False
作为一名聪明的程序员，你可能在2.x中尝试的时候期待的结果是True，尽管这并没有错，但是为了达到Python3的效果，但你仍然会因为其他原因导致失败。  
    
    >>> import keyword
    >>> if ‘print’ in keyword.kwlist:
    ...    from __future__ import print_function
    ...
    File “”, line 2
    SyntaxError: from __future__ imports must occur at the beginning of the file

一种解决方案是使用一个函数，其功能类似于print，其中之一是sys.stdout.write()，另一个是distutils.log.warn()。不管出于什么原因，我们决定使用后者。“hello world”的例子看起来是这样的：  
    
    # python 2.x
    print ‘hello world’
    # python 3.x
    print(“hello world”)
下面的代码就可以在两个版本中通用：  
    
    # python2.x & 3.x 兼容
    from distutils.log import warn as printf
    printf(“hello world”)

为什么我们不用sys.stdout.write()呢，因为我们需要添加一个NEWLINE字符在字符串的结尾来兼容这种行为(python2.x中write方法不会换行)：  
    
    # Python 2.x & 3.x 兼容
    import sys
    sys.stdout.write(“hello World\n”)

####Import your way to a solution
一般情况情况下，import时没什么烦恼，只要正确的导入就行，但在下面代码中，我们想导入urlopen()函数，在Python2中，他同时存在与urllib2和urllib2中（我们使用后者），在Python3中，他被集成到了urllib.request中，而你的方案是要既能在2.x和3.x中正常工作：  
    
    try:
        from urllib2 import urlopen
    except ImportError:
        from urllib.request import urlopen

出于对内存的保护，也许你对iterator(Python3)版本的zip()更加有兴趣，在Python2中，iterator版本是itertools.izip()。这个函数在Python3中被重命名替换成了zip()。如果你使用迭代版本，导入语句也非常直白：  
    
    try:
        from itertools import izip as zip
    except ImportError:
        pass

另一个列子是看来来并不怎么优雅的StringIO类，在Python2中，纯Python版本是StringIO模块，意味着访问的时候是通过StringIO.StringIO，同样还有一个更为快速的C语言版本，位于cStringIO.StringIO，不过这取决你的Python安装版本，你可以优先使用cStringIO然后是StringIO（如果cStringIO不能用的话)。在Python3中，Unicode是默认的string类型，但是如果你做任何和网络相关的操作，很有可能你不得不用ASCII/字节字符串来操作，所以代替StringIO，你要io.BytesIO，为了达到你想要的，这个导入看起来有点丑：  
    
    try:
        from io import BytesIO as StringIO
    except ImportError:
        try:
            from cStringIO import StringIO
        except ImportError:
            from StringIO import StringIO

####Putting it all together
如果你运气好的话，上面那些就是你要准备做的全部，剩下的代码都比开始设置的地方更简单。如果你按照上面的方式导入了distutils.log.warn()[printf()],`url*urlopen()`,`*.StringIO`和一个标准的导入：`xml.etree.ElementTree`(2.5及更新的)，现在你就可以写一个非常简短短的解析器来展示从Google News服务中提供的头条故事（译注：当然首先得备一个梯子），只需八行代码：  
    
    g = urlopen(‘http://news.google.com/news?topic=h&output=rss’)
    f = StringIO(g.read())
    g.close()
    tree = xml.etree.ElementTree.parse(f)
    f.close()
    for elmt in tree.getiterator():
        if elmt.tag == ‘title’ and not \
            elmt.text.startswith(‘Top Stories’):
            printf(‘- %s’ % elmt.text)
这段脚本在2.x和3.x下面运行时，不需要做任何改动，运行效果完全一样，当然，如果你正在使用的是2.4或者更老的版本，你需要单独下载ElementTree。  
但是有时候感觉这些改变把你优雅的Python代码弄得一团糟，毕竟可读性才是最重要的，如果你要优先保证代码的整洁而且在不修改任何地方的前提下运行在两个版本的Python环境中，那么你可以看一下six包。  
six一个兼容库，它的主要任务是提供接口隐藏复杂的细节，你可以在[这里](http://packages.python.org/six)找到它。无论你是使用像six这样的库还是用自己的方法来做，我们希望这个简短的介绍可以让你开始考虑写的代码能够在2.x和3.x下同时运行。
