

### 应该在学习Python3之前学习Python2，还是直接学习Python3

问题 [链接](http://stackoverflow.com/questions/170921/should-i-learn-python-2-before-3-or-start-directly-from-python-3)

你可以从python2开始，2和3主要的语法格式和风格相同

3要替代2不是短时间内能完成的，将会是一个很长的过程，所以学习Python2并没有什么坏处

我建议你关注下2和3的不同之处  [This slides gives you a quick introduction of the changes in Python 2 and 3](http://stackoverflow.com/questions/170921/should-i-learn-python-2-before-3-or-start-directly-from-python-3)





### 在virtualenv中如何使用不同的python版本

问题 [链接](http://stackoverflow.com/questions/1534210/use-different-python-version-with-virtualenv)

在创建virtualenv实例时，使用-p选项

    virtualenv -p /usr/bin/python2.6 <path/to/new/virtualenv/>

### 如何离开virtualenv

问题 [链接](http://stackoverflow.com/questions/990754/how-to-leave-a-python-virtualenv)

使用virtualenv时

    me@mymachine:~$ workon env1
    (env1)me@mymachine:~$ workon env2
    (env2)me@mymachine:~$ workon env1
    (env1)me@mymachine:~$

如何退出某个环境

    $ deactivate

### Python中什么项目结构更好

问题 [链接](http://stackoverflow.com/questions/193161/what-is-the-best-project-structure-for-a-python-application)

假设你要开发一个较大的客户端程序(非web端),如何组织项目目录和递归？


不要太在意这个.按你高兴的方式组织就行.Python项目很简单，所以没有那么多愚蠢的规则

    /scripts or /bin  命令行脚本
    /tests 测试
    /lib C-语言包
    /doc 文档
    /apidoc api文档

并且顶层目录包含README和Config

难以抉择的是，是否使用/src树. /src,/lib,/bin在Python中没有明显的区别，和Java/c不同

因为顶层/src文件夹显得没有什么实际意义，你的顶层目录可以是程序顶层架构的目录

    /foo
    /bar
    /baz

我建议将这些文件放入到"模块名"的目录中，这样，如果你在写一个应用叫做quux, /quux目录将包含所有这些东西

你可以在PYTHONPATH中加入 /path/to/quux/foo,这样你可以QUUX.foo中重用模块


另一个回答

    Project/
    |-- bin/
    |   |-- project
    |
    |-- project/
    |   |-- test/
    |   |   |-- __init__.py
    |   |   |-- test_main.py
    |   |
    |   |-- __init__.py
    |   |-- main.py
    |
    |-- setup.py
    |-- README


### 在Python中使用Counter错误

问题 [链接](http://stackoverflow.com/questions/13311094/counter-in-collections-module-python)

当使用Counter时，出现异常

    AttributeError: 'module' object has no attribute 'Counter'

    from collections import Counter
    ImportError: cannot import name Counter

原因：

版本问题，Counter在 python2.7中才被加入到这个模块，你可能使用了Python2.6或更老的版本

可以看下 [文档](http://docs.python.org/2/library/collections.html#collections.Counter)

如果要在 Python2.6或2.5版本使用，可以看 [这里](http://code.activestate.com/recipes/576611-counter-class/)


### 在Python中如何连接mysql数据库

问题 [链接](http://stackoverflow.com/questions/372885/how-do-i-connect-to-a-mysql-database-in-python)

首先，安装mysqldb

然后

    #!/usr/bin/python
    import MySQLdb

    db = MySQLdb.connect(host="localhost", # your host, usually localhost
                         user="john", # your username
                          passwd="megajonhy", # your password
                          db="jonhydb") # name of the data base

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    # Use all the SQL you like
    cur.execute("SELECT * FROM YOUR_TABLE_NAME")

    # print all the first cell of all the rows
    for row in cur.fetchall() :
        print row[0]

### Python框架flask和bottle有什么区别

问题 [链接](http://stackoverflow.com/questions/4941145/python-flask-vs-bottle)

区别：flask基于其他现有的存在很长一段时间的技术像Werkzeug和Jinja2，它没有尝试去重复发明轮子

另外一方面，Bottle，试图用一个文件解决一切.

我想去合并他们，但是Bottle的开发者貌似对偏离“一个文件”的处理方式不是很感兴趣

关于可扩展性： 可以使用其他模板引擎，例如Flask-Genshi使用了mako模板

Flask, Werkzeug and Jinja2 的开发者亲自回答的...碉堡了，翻译不是很准确


### 如何测试一个python脚本的性能

问题 [链接](http://stackoverflow.com/questions/582336/how-can-you-profile-a-python-script)


引入

    import cProfile
    cProfile.run('foo()')

执行脚本

    python -m cProfile myscript.py

结果

    1007 function calls in 0.061 CPU seconds

    Ordered by: standard name
    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.061    0.061 <string>:1(<module>)
    1000    0.051    0.000    0.051    0.000 euler048.py:2(<lambda>)
        1    0.005    0.005    0.061    0.061 euler048.py:2(<module>)
        1    0.000    0.000    0.061    0.061 {execfile}
        1    0.002    0.002    0.053    0.053 {map}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler objects}
        1    0.000    0.000    0.000    0.000 {range}
        1    0.003    0.003    0.003    0.003 {sum}

一个PyCon演讲 [入口](http://blip.tv/pycon-us-videos-2009-2010-2011/introduction-to-python-profiling-1966784)


### 如何获取5分钟之后的unix时间戳

问题 [链接](http://stackoverflow.com/questions/2775864/python-create-unix-timestamp-five-minutes-in-the-future)

使用 [calendar.timegm](http://docs.python.org/3.3/library/calendar.html#calendar.timegm)

    future = datetime.datetime.now() + datetime.timedelta(minutes = 5)
    return calendar.timegm(future.utctimetuple())

strftime的%s在windows中无法使用



### 在python中如何调用外部命令?

问题 [链接](http://stackoverflow.com/questions/89228/calling-an-external-command-in-python) 

Look at the subprocess module in the stdlib:

可以看下标准库中的 [subprocess](http://docs.python.org/library/subprocess.html)

    from subprocess import call
    call(["ls", "-l"])

subprocess相对于system的好处是, 更灵活

但是 quick/dirty/one time scripts, os.system is enough

### 用Python在终端打印出有颜色的文字?

问题[链接](http://stackoverflow.com/questions/287871/print-in-terminal-with-colors-using-python)

某种程度上这取决于你使用的平台。通常的方法是用ANSI转义序列。举个简单的例子，这有一些来自[blender build scripts](https://svn.blender.org/svnroot/bf-blender/trunk/blender/build_files/scons/tools/bcolors.py)的代码：

    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'

为了使用上面那种代码，你应该这样做：

    print bcolors.WARNING + "Warning: No active frommets remain. Continue?"
          + bcolors.ENDC

这在unixes包括OS X，linux和windows(为你提供[enable ansi.sys](http://support.microsoft.com/kb/101875))上会生效。有ansi代码来设置颜色，移动光标，做更多事情。

如果你想了解更为复杂的内容（这听上去好像你正在写一款游戏），你应该深入“cursor”这个没款，它会为你处理很多复杂的部分。[Python Curses HowTO](https://docs.python.org/2/howto/curses.html)是一篇很好的介绍。

如果你是用的不是ASCII（或者说你没有用PC)，你面对诸如ascii字符低于127，’#’，‘@’可能是你得到空格的最好的赌注。如果你确定你的终端使用IBM [extended ascii character set](http://telecom.tbi.net/asc-ibm.html)，你将会有更多的选择，字符176，字符177，字符178，和字符219代表”空格字符”。

一些流行的基于文本的程序，比如”Dwarf Fortress”，仿照文本的模式做成了图形模式，使用传统PC的字体图片。你可以在[Dwarf Frotress Wiki](http://dwarffortresswiki.org/DF2014:Tilesets)找一些这种点阵图看看（[user-made tilesets](http://dwarffortresswiki.org/Tileset_repository)）。

[Text Mode Demo Contest](http://en.wikipedia.org/wiki/TMDC)有更多把图片处理成文本的源码。

嗯...我想这个问题被我扯远了。尽管我现在纠结着去做一款基于文本的史诗冒险游戏。在有颜色的文本这方面，祝你好运。

### 我该如何保护我的Python代码

Python作为字节码编译的解释型语言，是很难封闭的。几遍你使用一种exe包比如[py2exe](http://py2exe.org/)，可执行文件的结构依然是清晰可见的，而且Python的字节编码是非常易懂的。

通常是这样，你必须要想出一个折衷的办法。保护代码究竟重不重要。里面是不是有很私密的东西(比如银行的对称加密秘钥），或者你是一个偏执狂。选择一门可以让你更快速开发优秀产品的语言，对于你的奇特想法从现实主义考虑一下它的价值。

如果你确定使用要强制授权保证安全，可以写一个小的C拓展，那么这个授权检验就会变得很难逆转（但不是完全不可能）。然后把你的大批代码放进Python。

### 首选的Python单元测试框架

问题[链接](http://stackoverflow.com/questions/191673/preferred-python-unit-testing-framework)

`nose`实际上不是一个单元测试的框架。它是一个测试的执行器，并且是最好的一款。它可以运行通过`pyUnit`，`py.test`和`doctest`创建的测试。

我首选的单元测试框架是pyUnit。它和其他xUnit框架一样，而且可以让没有Python基础的人很好上手。而且它对Eclipse/PyDev提供非常好的支持。

在`py.test`中，我发现了很多层级的安装/卸载混淆在一起。我还发现它生成了很多非常无组织和难阅读的单元测试。

`doctest`对于简单的东西来说还好，但是它很有限，不能真正的用来测试复杂和交互的代码。

### Python的单元测试放在哪？

问题[链接](http://stackoverflow.com/questions/61151/where-do-the-python-unit-tests-go)

对于一个文件`module.py`来说，单元测试通常叫做`test_module.py`，遵循Python的命名规则。

在以下几种地方放置`test_module.py`都是可以接受的：

1. 和`module.py`放在同一个文件夹。

2. 在`../tests/test_module.py`（与代码文件夹的同级）

3. 在`tests/test_module.py` （在代码文件夹下的同层）

我倾向第一种方法，它可以更直观的被找到并且引入。不管你在使用什么样的开发系统，你都可以轻松的配置并找到以`test_`开头的文件。实际上，方便查找的缺省的单元测试模型是`test*.py`。

### distribute, distutils, setuptools和distutils2的区别

问题[链接](http://stackoverflow.com/questions/6344076/differences-between-distribute-distutils-setuptools-and-distutils2)

到2014年9月，所有其他回答的时间都超过一年了。当你寻求Python打包的建议时，记得看一下发布的日期，而且不要相信过时的信息。

这篇搭建在Readthedocs的文章[Python Packaging User Guide](http://stackoverflow.com/questions/6344076/differences-between-distribute-distutils-setuptools-and-distutils2)值得一读。每一页都有一个最近时间展示，所以你可以检查最新的手册，而且它相当的全面。Python 3.4的官方文档已经从信任的角度把这个链接加进来了。

工具的总结：

这里有一个2014年9月份的Python打包总结：

* **Distutils** is still the standard tool for packaging in Python. It is included in the standard library (Python 2 and Python 3.0 to 3.4). It is useful for simple Python distributions, but lacks features. It introduces the distutils Python package that can be imported in your setup.py script.

* **Setuptools** was developed to overcome Distutils' limitations, and is not included in the standard library. It introduced a command-line utility called easy_install. It also introduced the setuptools Python package that can be imported in your setup.py script, and the pkg_resources Python package that can be imported in your code to locate data files installed with a distribution. One of its gotchas is that it monkey-patches the distutils Python package. It should work well with pip. The latest version was released in August 2014.

* **Distribute** was a fork of Setuptools. It shared the same namespace, so if you had Distribute installed, import setuptools would actually import the package distributed with Distribute. Distribute was merged back into Setuptools 0.7, so you don't need to use Distribute any more. In fact, the version on Pypi is just a compatibility layer that installs Setuptools.

* **Distutils2** was an attempt to take the best of Distutils, Setuptools and Distribute and become the standard tool included in Python's standard library. The idea was that Distutils2 would be distributed for old Python versions, and that Distutils2 would be renamed to packaging for Python 3.3, which would include it in its standard library. These plans did not go as intended, however, and currently, Distutils2 is an abandoned project. The latest release was in March 2012, and its Pypi home page has finally been updated to reflect its death.

* **Distlib** is a tool that aims to implement a subset of the previous tools' functionality, but only functionality that is very well-defined in accepted PEPs. It should hopefully be included eventually in the Python standard library. It is still being developed and is not recommended for end-users yet.

* **Bento** is a packaging solution designed to replace Distutils, Setuptools, Distribute and Distutils2, written from the ground up. Its primary developer is also a core developer of numpy/scipy, so he's familiar with non-simple use-cases for packaging systems. Its first commit was in October 2009, and the latest commit as of writing was in August 2014, although the authors are not updating its Pypi page correspondingly. It's in active development but it is not mature yet, and it is not as widely known as Setuptools yet.

推荐：

所以综上所述，排除所有这些选项，我回推荐 **Setuptools**，除非你的需求非常基础，那么你可能只需要 Distutils。Setuptools在Virtualenv和Pip上的表现非常好，我强烈推荐。

作为一个边注，我建议使用Virtualenv1.10或者更高的版本，因为对Python2或3来说，它是第一个识别Setuptools/Distribute并合并的版本。
