  

## Pylint 是什么

Pylint 是一个 Python 代码分析工具，它分析 Python 代码中的错误，查找不符合代码风格标准（Pylint 默认使用的代码风格是 PEP
8，具体信息，请参阅参考资料）和有潜在问题的代码。目前 Pylint 的最新版本是 pylint-0.18.1。

  * Pylint 是一个 Python 工具，除了平常代码分析工具的作用之外，它提供了更多的功能：如检查一行代码的长度，变量名是否符合命名标准，一个声明过的接口是否被真正实现等等。
  * Pylint 的一个很大的好处是它的高可配置性，高可定制性，并且可以很容易写小插件来添加功能。
  * 如果运行两次 Pylint，它会同时显示出当前和上次的运行结果，从而可以看出代码质量是否得到了改进。
  * 目前在 eclipse 的 [pydev](http://pydev.sourceforge.net/) 插件中也集成了 Pylint。

* * *

[回页首](http://www.ibm.com/developerworks/cn/linux/l-cn-
pylint/?S_TACT=105AGX52&S_CMP=tec-csdn#ibm-pcon)

## Pylint 具体介绍

### Pylint 的安装

Pylint 可以用于所有高于或者等于 2.2 的 Python 版本兼容。需要 [logilab-
astng](http://www.logilab.org/project/logilab-astng)（version >= 0.14）和
[logilab-common](http://www.logilab.org/project/logilab-common)（version >=
0.13）的包（具体信息，请参阅 参考资料），如果是 Python 版本低于 2.3，那么它还需要 optik 包（本文接下来的示例暂不考虑这种情况）。

**Pylint 所用到的所有的包的下载地址**

logilab-astng 的最新包下载：<http://www.logilab.org/856/>

logilab-common 的最新包下载：<http://www.logilab.org/848/>

optik 的包下载：<http://optik.sourceforge.net/>

Pylint 的最新包下载：<http://www.logilab.org/project/pylint>

**Pylint 在 Linux 上的安装**

1\. 在 Linux 上，首先安装 Python 的包（高于版本 2.2），并在环境变量 $PATH 中添加 Python 可执行文件的路径。

2\. 下载 Pylint、logilab-astng (version >= 0.14) 和 logilab-common (version >=
0.13) 的包 , 使用 `tar zxvf *.tar.gz`解压缩这些包。

3\. 依次进入 logilab-astng、logilab-common 和 Pylint 解开的文件夹中，运行命令 `Python setup.py
install`来安装。

4\. 安装完成后，就可以通过 `pylint [options] module_or_package`来调用 Pylint 了。

**Pylint 在 Windows 上的安装**

1\. 安装 Python 的包（高于版本 2.2），右键单击桌面上的我的电脑图标，选择属性，高级，环境变量，在 $PATH 中添加 Python
的安装路径，如 C:\Python26\。

2\. 使用解压缩工具解压缩所有的包。

3\. 打开命令行窗口，使用 `cd`依次进入 logilab-astng、logilab-common 和 Pylint 解开的文件夹中，运行命令
`python setup.py install`来安装。

4\. 安装完成后，在 Python 的安装路径下出现一个 Scripts 文件夹，里面包含一些 bat 脚本，如 pylint.bat 等。

5\. 为了使调用 pylint.bat 的时候不需要输入完整路径，在 Python 的安装目录下创建 pylint.bat
的重定向文件，这是一个纯文本文件 pylint.bat，里面包含 pylint.bat
的实际路径，如：C:\Python26\Scripts\pylint.bat。

6\. 安装完成后，可以通过 `pylint [options] module_or_package`来调用 Pylint 了。

### Pylint 的调用

##### 清单 1. Pylint 的调用命令

    
    
     pylint [options] module_or_package

使用 Pylint 对一个模块 module.py 进行代码检查：

  * 1\. 进入这个模块所在的文件夹，运行 `pylint [options] module.py`  
这种调用方式是一直可以工作的，因为当前的工作目录会被自动加入 Python 的路径中。

  * 2\. 不进入模块所在的文件夹，运行 `pylint [options] directory/module.py`  
这种调用方式当如下条件满足的时候是可以工作的：directory 是个 Python 包 ( 比如包含一个 __init__.py 文件 )，或者
directory 被加入了 Python 的路径中。

使用 Pylint 对一个包 pakage 进行代码检查：

  * 1\. 进入这个包所在文件夹，运行 `pylint [options] pakage。`  
这种调用方式是一直可以工作的，因为当前的工作目录会被自动加入 Python 的路径中。

  * 2\. 不进入包所在的文件夹，运行 `pylint [options] directory/ pakage。`  
这种情况下当如下条件满足的时候是可以工作的：directory 被加入了 Python 的路径中。比如在 Linux 上，`export
PYTHONPATH=$PYTHONPATH: directory。`

此外，对于安装了 tkinter 包的机器，可以使用命令 `pylint-gui`打开一个简单的 GUI 界面，在这里输入模块或者包的名字 ( 规则同命令行
), 点击 **Run**，Pylint 的输出会在 GUI 中显示。

### Pylint 的常用命令行参数

  * `-h``,``\--help`

显示所有帮助信息。

  * `\--generate-rcfile`

可以使用 pylint --generate-rcfile 来生成一个配置文件示例。可以使用重定向把这个配置文件保存下来用做以后使用。也可以在前面加上其它选
项，使这些选项的值被包含在这个产生的配置文件里。如：`pylint --persistent=n --generate-rcfile >
pylint.conf`，查看 pylint.conf，可以看到 persistent=no，而不再是其默认值 yes。

  * `\--rcfile=<file>`

指定一个配置文件。把使用的配置放在配置文件中，这样不仅规范了自己代码，也可以方便地和别人共享这些规范。

  * `-i <y_or_n>, --include-ids=<y_or_n>`

在输出中包含 message 的 id, 然后通过 `pylint --help-msg=<msg-
id>`来查看这个错误的详细信息，这样可以具体地定位错误。

  * `-r <y_or_n>, --reports=<y_or_n>`

默认是 y, 表示 Pylint 的输出中除了包含源代码分析部分，也包含报告部分。

  * `\--files-output=<y_or_n>`

将每个 module /package 的 message 输出到一个以 pylint_module/package. [txt|html]
命名的文件中，如果有 report 的话，输出到名为 pylint_global.[txt|html] 的文件中。默认是输出到屏幕上不输出到文件里。

  * `-f <format>, --output-format=<format>`

设置输出格式。可以选择的格式有 text, parseable, colorized, msvs (visual studio) 和 html,
默认的输出格式是 text。

  * `\--disable-msg=``<msg ids>`

禁止指定 id 的 message. 比如说输出中包含了 W0402 这个 warning 的 message, 如果不希望它在输出中出现，可以使用
`\--disable-msg= W0402`

### Pylint 的输出

Pylint`的默认输出格式是原始文`本（raw text）格式 `，可以通过 -f <format>，--output-format=<format>
来指定别的输出格式如`html`等等。在`Pylint`的输出中有如下两个部分：源代码分析部分``和报告部分。`

**源代码分析部分：**

对于每一个 Python 模块，Pylint 的结果中首先显示一些"*"字符 , 后面紧跟模块的名字，然后是一系列的 message, message
的格式如下：

    
    
     MESSAGE_TYPE: LINE_NUM:[OBJECT:] MESSAGE

MESSAGE_TYPE 有如下几种：

(C) 惯例。违反了编码风格标准

(R) 重构。写得非常糟糕的代码。

(W) 警告。某些 Python 特定的问题。

(E) 错误。很可能是代码中的错误。

(F) 致命错误。阻止 Pylint 进一步运行的错误。

##### 清单 2. Pylint 中的 utils 模块的输出结果

    
    
     ************* Module utils 
     C: 88:Message: Missing docstring 
     R: 88:Message: Too few public methods (0/2) 
     C:183:MessagesHandlerMixIn._cat_ids: Missing docstring 
     R:183:MessagesHandlerMixIn._cat_ids: Method could be a function 
     R:282:MessagesHandlerMixIn.list_messages: Too many branches (14/12)

**报告部分：**

在源代码分析结束后面，会有一系列的报告，每个报告关注于项目的某些方面，如每种类别的 message
的数目，模块的依赖关系等等。具体来说，报告中会包含如下的方面：

  * 检查的 module 的个数。
  * 对于每个 module, 错误和警告在其中所占的百分比。比如有两个 module A 和 B, 如果一共检查出来 4 个错误，1 个错误是在 A 中，3 个错误是在 B 中，那么 A 的错误的百分比是 25%, B 的错误的百分比是 75%。
  * 错误，警告的总数量。

* * *

[回页首](http://www.ibm.com/developerworks/cn/linux/l-cn-
pylint/?S_TACT=105AGX52&S_CMP=tec-csdn#ibm-pcon)

## 使用 Pylint 分析 Python 代码的具体示例

下面是一个从 xml 文件中读取一些值并显示出来的一段 Python 代码 dw.py，代码如下：

##### 清单 3. 源码

    
    
    import string 
     #!/usr/bin/env python 
    
     import xml.dom.minidom 
    
     xmlDom=xml.dom.minidom.parse("identity.xml") 
     organizations = xmlDom.getElementsByTagName('DW') 
     for org in organizations: 
    	 products = org.getElementsByTagName('linux') 
        for product in products: 
            print 'ID: ' + product.getAttribute('id') 
            print 'Name: ' + product.getAttribute('name') 
            print 'Word Count: ' + product.getAttribute('count')

##### 清单 4. identity.xml 的内容

    
    
     <IBM> 
            <DW> 
                    <linux id="100" name="python" count="3000" /> 
            </DW> 
     </IBM>

这时候使用 Pylint 的结果（这是从 html 格式的输出中拷贝的）为：

##### 清单 5. Pylint 的分析结果

    
    
     ************* Module dw 
     C:1:Missing docstring 
     C:5:Operator not preceded by a space xmlDom=xml.dom.minidom.parse("identity.xml") ^ 
     C:5:Invalid name "xmlDom" (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$) 
     C:6:Invalid name "organizations" (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$) 
    
     Report 部分省略

输出中第一部分是源代码分析，第二部分是报告。输出结果中有这么多信息，从哪里开始分析呢？首先使用如下的步骤来分析代码：

1\. 因为输出结果太长，所以可以先不让它输出报告部分，先根据源代码分析部分来找出代码中的问题。使用选项 `"--reports=n"``。`

2\. 使用选项 `"--include-ids=y"`。可以获取到源代码分析部分每条信息的 ID。

##### 清单 6. 使用 pylint --reports=n --include-ids=y dw.py 的结果

    
    
    ************* Module dw 
    C0111: 1: Missing docstring 
    C0322: 5: Operator not preceded by a space xmlDom=xml.dom.minidom.parse("identity.xml") ^ 
    C0103: 5: Invalid name "xmlDom" (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$) 
    C0103: 6: Invalid name "organizations" (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)

每个信息前面都会加上一个 id, 如果不理解这个信息的意思，可以通过 `pylint --help-msg=id`来查看。

##### 清单 7. 使用 pylint --help-msg= C0111 的结果

    
    
     C0111: *Missing docstring* 
      Used when a module, function, class or method has no docstring. Some special 
     methods like __init__ doesn't necessary require a docstring. 
     This message belongs to the basic checker.

3\. 开始分析每个源代码中的问题。从上面知道，第一个问题的原因是缺少 `docstring`，在代码中增加 `docstring`, 修改后的代码如下：

##### 清单 8. 增加 docstring 修改后的源码

    
    
     #!/usr/bin/env python 
    
    """This script parse the content of a xml file"""
    
     import xml.dom.minidom 
    
     xmlDom=xml.dom.minidom.parse("identity.xml") 
     organizations = xmlDom.getElementsByTagName('DW') 
     for org in organizations: 
        products = org.getElementsByTagName('linux') 
        for product in products: 
            print 'ID: ' + product.getAttribute('id') 
            print 'Name: ' + product.getAttribute('name') 
            print 'Word Count: ' + product.getAttribute('count')

重新运行 `pylint --reports=n --include-ids=y dw.py`，结果为：

##### 清单 9. 运行结果

    
    
     ************* Module dw 
     C0322:  7: Operator not preceded by a space 
     xmlDom=xml.dom.minidom.parse("identity.xml") 
          ^ 
     C0103:  7: Invalid name "xmlDom" (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$) 
     C0103:  8: Invalid name "organizations" (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)

可以看到源代码中的第一个问题已被解决。

4\. 关于第二个 C0322 的问题，这里的分析结果说明得比较清楚，是代码第七行中的等号运算符两边没有空格。我们在这里加上空格，重新运行 `pylint
--reports=n --include-ids=y dw.py`，结果为：

##### 清单 10. 运行结果

    
    
     ************* Module dw 
     C0103:  7: Invalid name "xmlDom" (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$) 
     C0103:  8: Invalid name "organizations" (should match (([A-Z_][A-Z0-9_]*)|(__.*__))$)

5\. 可以看到现在问题只剩下 C0103 了。这里的意思是变量命名规则应该符合后面正则表达式的规定。Pylint
定义了一系列针对变量，函数，类等的名字的命名规则。实际中我们不一定要使用这样的命名规则，我们可以定义使用正则表达式定义自己的命名规则，比如使用选项
`\--const-rgx='[a-z_][a-z0-9_]{2,30}$'`，我们将变量 `xmlDom`改为 `xmldom`, 代码如下：

##### 清单 11. 将变量 xmlDom 改为 xmldom 后的源码

    
    
     #!/usr/bin/env python 
    
    """This script parse the content of a xml file"""
    
     import xml.dom.minidom 
    
     xmldom = xml.dom.minidom.parse("identity.xml") 
     organizations = xmldom.getElementsByTagName('DW') 
     for org in organizations: 
        products = org.getElementsByTagName('linux') 
        for product in products: 
            print 'ID: ' + product.getAttribute('id') 
            print 'Name: ' + product.getAttribute('name') 
            print 'Word Count: ' + product.getAttribute('count')

运行 `pylint --reports=n --include-ids=y --const-rgx='[a-z_][a-z0-9_]{2,30}$'
dw.py`，结果中就没有任何问题了。

6\. 如果希望一个组里的人都使用这些统一的规则，来规范一个部门的代码风格。比如说大家都使用 `\--const-
rgx='[a-z_][a-z0-9_]{2,30}$'`作为命名规则，那么一个比较便捷的方法是使用配置文件。

使用 `pylint --generate-rcfile > pylint.conf`来生成一个示例配置文件，然后编辑其中的 `\--const-
rgx`选项。或者也可以直接 `pylint --const-rgx='[a-z_][a-z0-9_]{2,30}$' --generate-rcfile
> pylint.conf`，这样生成的配置文件中 `\--const-rgx`选项直接就是 `'[a-z_][a-z0-9_]{2,30}$'`了。

以后运行 Pylint 的时候指定配置文件：`pylint --rcfile=pylint.conf dw.py`

这样 Pylint 就会按照配置文件
`pylint.conf`中的选项来指定参数。在一个部门中，大家可以共同使用同一个配置文件，这样就可以保持一致的代码风格。

7\. 如果把 report 部分加上，即不使用 `\--reports=``n，可以看到报告部分的内容`。

* * *

[回页首](http://www.ibm.com/developerworks/cn/linux/l-cn-
pylint/?S_TACT=105AGX52&S_CMP=tec-csdn#ibm-pcon)

## 结束语

本文通过详细的理论介绍和简单易懂的实例全面介绍了 Python 代码分析工具 Pylint。相信读者看完后一定可以轻松地将 Pylint
运用到自己的开发工程中。

  

