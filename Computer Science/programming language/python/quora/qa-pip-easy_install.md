
### 如何使用 pip 更新所有包

问题 [链接](http://stackoverflow.com/questions/2720014/upgrading-all-packages-with-pip)

如何使用pip更新python的所有包

没有内置的标志可以实现

但是你可以这么做

    pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs pip install -U

### 如何删除Python easy_install安装的包

问题 [链接](http://stackoverflow.com/questions/1231688/how-do-i-remove-packages-installed-with-pythons-easy-install)

[pip](https://pypi.python.org/pypi/pip/), setuptools/easy_install的另一种选择，提供uninstall命令

首先，移除依赖

    $ easy_install -m [PACKAGE]

然后，手动删除egg文件

    $ rm -rf .../python2.X/site-packages/[PACKAGE].egg

### 如何获取Python的site-packages目录位置

问题 [链接](http://stackoverflow.com/questions/122327/how-do-i-find-the-location-of-my-python-site-packages-directory)

参考 [How to Install Django" documentation](http://docs.djangoproject.com/en/dev/topics/install/#remove-any-old-versions-of-django)

可以在shell中执行

    python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())"

更好的可读性

    from distutils.sysconfig import get_python_lib
    print(get_python_lib())

### setup.py安装后如何卸载

问题 [链接](http://stackoverflow.com/questions/1550226/python-setup-py-uninstall)


使用下面命令安装的包如何卸载

    python setup.py install

手工删除的话

    python setup.py install --record files.txt
    cat files.txt | xargs rm -rf

### 如何获取安装的python模块列表

问题 [链接](http://stackoverflow.com/questions/739993/get-a-list-of-installed-python-modules)

    >>> help('modules')

### 为什么要使用pip而不是easy_install

问题 [链接](http://stackoverflow.com/questions/3220404/why-use-pip-over-easy-install)

有一条推文

    Don't use easy_install, unless you like stabbing yourself in the face. Use pip.

Pip简介

    All packages are downloaded before installation. Partially-completed installation doesn’t occur as a result.
    Care is taken to present useful output on the console.
    The reasons for actions are kept track of. For instance, if a package is being installed, pip keeps track of why that package was required.
    Error messages should be useful.
    The code is relatively concise and cohesive, making it easier to use programmatically.
    Packages don’t have to be installed as egg archives, they can be installed flat (while keeping the egg metadata).
    Native support for other version control systems (Git, Mercurial and Bazaar)
    Uninstallation of packages.
    Simple to define fixed sets of requirements and reliably reproduce a set of packages.

其他原因：

    Another—as of yet unmentioned—reason for favoring pip is because it is the new hotness and will continue to be used in the future.

    pip提供unstall命令
    如果中途安装失败，pip will leave you in a clean state.

### 如何在正确使用pip，virtualenv，distribute构建Python环境

问题[链接](http://stackoverflow.com/questions/4324558/whats-the-proper-way-to-install-pip-virtualenv-and-distribute-for-python)

你可以不向Python本身添加任何东西。

你不需要sudo或者任何权限。

你不需要编辑任何文件。

在自引导的虚拟环境里安装virtualenv。通过这个虚拟环境，它可以创建更多。自从virtualenv搭载了pip和distribute，你就可以从其中一个获得所有东西。

1. 下载virtualenv:
    http://pypi.python.org/pypi/virtualenv
    https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.9.tar.gz(实际上最好下载最新的版本!)
2. 解压源码
3. 用解压好的源文件创建一个干净的虚拟环境。选择正确的命令，虚拟环境会自带pip和distribute。
4. 在virtualenv中安装virtualenv
5. 使用第一个自建的环境去创建更多！

有一个bash的简单例子：

    # Select current version of virtualenv:
    VERSION=1.6.4
    # Name your first "bootstrap" environment:
    INITIAL_ENV=py-env0
    # Options for your first environment:
    ENV_OPTS='--no-site-packages --distribute'
    # Set to whatever python interpreter you want for your first environment:
    PYTHON=$(which python)
    URL_BASE=http://pypi.python.org/packages/source/v/virtualenv

    # --- Real work starts here ---
    curl -O $URL_BASE/virtualenv-$VERSION.tar.gz
    tar xzf virtualenv-$VERSION.tar.gz
    # Create the first "bootstrap" environment.
    $PYTHON virtualenv-$VERSION/virtualenv.py $ENV_OPTS $INITIAL_ENV
    # Don't need this anymore.
    rm -rf virtualenv-$VERSION
    # Install virtualenv into the environment.
    $INITIAL_ENV/bin/pip install virtualenv-$VERSION.tar.gz

现在你可以用你的自引导环境去创建更多：

    # Create a second environment from the first:
    $INITIAL_ENV/bin/virtualenv --no-site-packages --distribute py-env1
    # Create more:
    $INITIAL_ENV/bin/virtualenv py-env2

疯狂吧！

更新

`—no-site-packages` and`—distribute`现在是默认的了（运行`virtualenv -h`）所以你可以通过`python virtualenv.py bootstrap`或者`python3 virtualenv.py bootstrap`安装你的引导。
