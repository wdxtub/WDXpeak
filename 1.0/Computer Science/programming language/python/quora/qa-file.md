
### 如何判断一个文件是否存在

问题 [链接](http://stackoverflow.com/questions/82831/how-do-i-check-if-a-file-exists-using-python)

如何检查一个文件是否存在，不适用try:声明

    import os.path
    print os.path.isfile(fname)

    print os.path.exists(fname)


### 如何创建不存在的目录结构

问题 [链接](http://stackoverflow.com/questions/273192/python-best-way-to-create-directory-if-it-doesnt-exist-for-file-write)


    if not os.path.exists(directory):
        os.makedirs(directory)

需要注意的是，当目录在exists和makedirs两个函数调用之间被创建时，makedirs将抛出OSError

### 如何拷贝一个文件

问题 [链接](http://stackoverflow.com/questions/123198/how-do-i-copy-a-file-in-python)

[shutil](http://docs.python.org/2/library/shutil.html)模块

    copyfile(src, dst)

将src文件内容拷贝到dst，目标文件夹必须可写，否则将抛出IOError异常

如果目标文件已存在，将被覆盖

另外特殊文件，想字符文件，块设备文件，无法用这个方法进行拷贝

src/dst是字符串

### 逐行读文件去除换行符(perl chomp line)

问题 [链接](http://stackoverflow.com/questions/275018/how-can-i-remove-chomp-a-newline-in-python)
类似问题 [链接](http://stackoverflow.com/questions/761804/trimming-a-string-in-python)

读一个文件，如何获取每一行内容（不包括换行符）

比较pythonic的做法:

    >>> text = "line 1\nline 2\r\nline 3\nline 4"
    >>> text.splitlines()
    ['line 1', 'line 2', 'line 3', 'line 4']

用rstrip,(rstrip/lstrip/strip)

    #去除了空白+换行
    >>> 'test string \n'.rstrip()
    'test string'
    #只去换行
    >>> 'test string \n'.rstrip('\n')
    'test string '
    #更通用的做法，系统相关
    >>> import os, sys
    >>> sys.platform
    'linux2'
    >>> "foo\r\n".rstrip(os.linesep)
    'foo\r'

### 如何获取一个文件的创建和修改时间

问题 [链接](http://stackoverflow.com/questions/237079/how-to-get-file-creation-modification-date-times-in-python)

跨平台的获取文件创建及修改时间的方法

你有很多选择

使用[os.path.getmtime](http://docs.python.org/release/2.5.2/lib/module-os.path.html#l2h-2177)或者[os.path.getctime](http://docs.python.org/release/2.5.2/lib/module-os.path.html#l2h-2178)


    import os.path, time
    print "last modified: %s" % time.ctime(os.path.getmtime(file))
    print "created: %s" % time.ctime(os.path.getctime(file))

或者[os.stat](http://www.python.org/doc/2.5.2/lib/module-stat.html)

    import os, time
    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(file)
    print "last modified: %s" % time.ctime(mtime)

注意，ctime()并非指*nix系统中文件创建时间，而是这个节点数据的最后修改时间

### 如何将字符串转换为datetime

问题 [链接](http://stackoverflow.com/questions/466345/converting-string-into-datetime)

可以查看下time模块的[strptime](http://docs.python.org/2/library/time.html#time.strptime)方法，反向操作是[strftime](http://docs.python.org/2/library/time.html#time.strftime)

    from datetime import datetime
    date_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

[扩展文档](http://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior)

### 找到当前目录及文件所在目录

问题 [链接](http://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory)

查找当前目录使用os.getcwd()

查找某个文件的目录，使用, [os.path](http://docs.python.org/2/library/os.path.html)

    import os.path
    os.path.realpath(__file__)

### 如何找到一个目录下所有.txt文件

问题 [链接](http://stackoverflow.com/questions/3964681/find-all-files-in-directory-with-extension-txt-with-python)

使用[glob](http://docs.python.org/2/library/glob.html)

    import glob
    import os
    os.chdir("/mydir")
    for files in glob.glob("*.txt"):
        print files

使用os.listdir

    import os
    os.chdir("/mydir")
    for files in os.listdir("."):
        if files.endswith(".txt"):
            print files

或者遍历目录

    import os
    for r,d,f in os.walk("/mydir"):
        for files in f:
            if files.endswith(".txt"):
                print os.path.join(r,files)

### 读文件到列表中

问题 [链接](http://stackoverflow.com/questions/3277503/python-read-file-line-by-line-into-array)


    f = open('filename')
    lines = f.readlines()
    f.close()
    等价
    with open(fname) as f:
        content = f.readlines()

[文档](http://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files)

### 如何往文件中追加文本

问题 [链接](http://stackoverflow.com/questions/4706499/how-do-you-append-to-file-in-python)

    with open("test.txt", "a") as myfile:
        myfile.write("appended text")

可以使用'a'或'a+b' mode打开文件，见 [文档](http://docs.python.org/2/library/functions.html#open)

### 如何获取文件扩展名

问题 [链接](http://stackoverflow.com/questions/541390/extracting-extension-from-filename-in-python)

使用os.path.splitext方法：

    >>> import os
    >>> fileName, fileExtension = os.path.splitext('/path/to/somefile.ext')
    >>> fileName
    '/path/to/somefile'
    >>> fileExtension
    '.ext'

### 如何列出一个目录的所有文件

问题 [链接](http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python)

1.使用os.listdir(),得到目录下的所有文件和文件夹

    #只需要文件
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

2.os.walk()

    from os import walk

    f = []
    for (dirpath, dirnames, filenames) in walk(mypath):
        f.extend(filenames)
        break

3.glob

    import glob
    print glob.glob("/home/adam/*.txt")

重复问题 [链接](http://stackoverflow.com/questions/120656/directory-listing-in-python)

import os

    for dirname, dirnames, filenames in os.walk('.'):
        # print path to all subdirectories first.
        for subdirname in dirnames:
            print os.path.join(dirname, subdirname)

        # print path to all filenames.
        for filename in filenames:
            print os.path.join(dirname, filename)

### 如何从标准输入读取内容stdin

问题 [链接](http://stackoverflow.com/questions/1450393/how-do-you-read-from-stdin-in-python)


使用[fileinput](http://docs.python.org/2/library/fileinput.html)

    import fileinput
    for line in fileinput.input():
        pass

### 如何高效地获取文件行数

问题 [链接](http://stackoverflow.com/questions/845058/how-to-get-line-count-cheaply-in-python)


比较结果python2.6

    mapcount : 0.471799945831
    simplecount : 0.634400033951
    bufcount : 0.468800067902
    opcount : 0.602999973297

代码

    from __future__ import with_statement
    import time
    import mmap
    import random
    from collections import defaultdict

    def mapcount(filename):
        f = open(filename, "r+")
        buf = mmap.mmap(f.fileno(), 0)
        lines = 0
        readline = buf.readline
        while readline():
            lines += 1
        return lines

    def simplecount(filename):
        lines = 0
        for line in open(filename):
            lines += 1
        return lines

    def bufcount(filename):
        f = open(filename)
        lines = 0
        buf_size = 1024 * 1024
        read_f = f.read # loop optimization

        buf = read_f(buf_size)
        while buf:
            lines += buf.count('\n')
            buf = read_f(buf_size)

        return lines

    def opcount(fname):
        with open(fname) as f:
            for i, l in enumerate(f):
                pass
        return i + 1


    counts = defaultdict(list)

    for i in range(5):
        for func in [mapcount, simplecount, bufcount, opcount]:
            start_time = time.time()
            assert func("big_file.txt") == 1209138
            counts[func].append(time.time() - start_time)

    for key, vals in counts.items():
        print key.__name__, ":", sum(vals) / float(len(vals))


### Python如何实现mkdir -p功能


问题 [链接](http://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python)

    import os, errno

    def mkdir_p(path):
        try:
            os.makedirs(path)
        except OSError as exc: # Python >2.5
            if exc.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else: raise

