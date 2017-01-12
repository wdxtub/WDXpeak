Python/Django编程实践指南
=========================
####Python/Django代码风格
PEP8是Python官方推荐的代码风格指南标准。  

* 使用4个空格作为缩进
* 最外层函数和类使用两个空行分隔
* 类中的方法使用一个空行分隔

PEP8建议按如下三种方式分组导入包  
* 标准库导入
* 第三方相关包导入
* 本地应用或库导入

比如：一个Django项目，包导入看起来应该是：  

    #标准库
    from math import sqrt
    from os.path import abspath
    
    #Django导入
    from django.db import models
    from django.utils.translation import ugettext_lazy as _
    
    #第三方应用导入
    from django_extensions.db.models import TimeStampedModel
    
    #导入自己的应用
    from splits.models import BananaSplit

（当然这里的注释只是对本例的说明，实际代码中并不需要写这些注释）  


####使用相对导入
使用相对导入，更易于app的移植、重用、重命名。比如：下面的cones app，在view中使用硬编码使用cones 包，

    # cones/views.py
    # Hard coding of package name
    from django.views.generic import CreateView
    # DON’T DO THIS: Hardcoding of the 'cones' package
    from cones.models import WaffleCone
    from cones.forms import WaffleConeForm
    class WaffleConeCreateView(CreateView):
        model = WaffleCone
        form_class = WaffleConeForm 

* 现在假如你想在其他project重用这个cones app，但是刚好这个project中已经有一个叫cones 的app了，这样就会造成名字的冲突。  
* 如果想像把cones改名，你又得在多次更改cones。  

推荐的方式应该是：  

    # cones/views.py
    from django.views.generic import CreateView
    # Hard coding of the 'cones' package
    from .models import WaffleCone
    from .forms import WaffleConeForm
    class WaffleConeCreateView(CreateView):
        model = WaffleCone
        form_class = WaffleConeForm 


####避免使用 import  *
在99%的情况下都因该明确import具体的模块名字

    from django import forms
    from django.db import models
绝对不要这样干：  

    from django.form import *
    from django.db.models import *
不要这样做的原因是避免隐含的加载其他Python模块的locals把当前的模块的命名空间覆盖了。那样做可能导致不可预见性灾难。  

比如Django Froms 和 Django Models 包中都含有一个类叫CharField，隐含地加载两个库，Models库将覆盖Forms版本的CharField。  

#####Django风格
在URL pattern名字中使用下划线"_"而不是破折号"-"，注意只是指的是url()的name参数，而不是真正的URL地址，破折号在URL没问题。  
使用下划线而不是破折号在模版 block 名字中。  

####Python/Django最佳环境配置
本地测试环境和线上生产环境使用同样的数据库  
有些童鞋喜欢在本地用SQLite作为测试数据库，生产环境才使用正式的数据库如MySQL/PostgreSQL，然而不同的数据库有不同的数据类型和约束，很多问题一旦跑到线上问题就来了。  

#####使用Pip 和 Virtualenv
Pip 是 python 包安装管理工具，比easy_install更强大。  
Virtualenv是用来创建完全独立的、隔离的Python环境的工具，这就意味着你可以在A 项目中使用Django1.4，B项目中使用1.5成为可能，互不影响。Virtualenvwrapper如其名就像咖啡伴侣，它为virtualenv提供了更便捷的操作。  

使用virtualenv激活某个虚拟环境：  

    source ~/.virtualenvs/myproject/bin/activate
而使用virtualenvwrapper可以简单为：  

    workon myproject
####使用版本控制系统
Git 和 Mercurial 是 Django开发中最流行的版本控制工具，它不仅能使用你在本地有一份拷贝，而且还能使用代码托管服务用来备份，更重要的是可以多人协助编程。推荐大家使用 GitHub 或者 Bitbucket，后者可以建立免费的私有仓库。  

####Django项目代码布局
运行：  

    $ django-admin.py startproject mysite
    $ cd mysite
    $ django-admin.py startapp my_app

Django1.5的默认布局：  

    mysite/
        manage.py
        my_app/
            __init__.py
            models.py
            tests.py
            views.py
        mysite/
            __init__.py
            settings.py
            urls.py
            wsgi.py    

比较常用的一种布局格式是：  

    gongshare_project/   #<repository_root>/
        .gitignore
        Makefile
        docs/
        requirements.txt
        gongshare/          #<django_project_root>/
            manage.py
            media/
            products/
            profiles/
            ratings/
            static/
            templates/
            gongshare/      #<configuration_root>/
                __init__.py
                settings/
                urls.py
                wsgi.py

这是一个三层结构的布局：  
顶层是仓库根目录，它包含了第二层目录外还包括一些如：**README, doc/** 目录，**.gitignore** 、**requirements** 文件。  

第二层是django项目的根目录，这层是通过 django-admin.py startproject 命令生成的。这个目录包含了第三层目录外还有mdedia、static（css，js等）、templates（模版）目录和app目录（比如：profiles、ratings、products）  

第三层同样是通过django-admin.py startproject 生成，除了一个基础的URLConf（urls.py)外还有settings模块，settings模块方式不同环境下的项目配置文件。  


####配置文件和必要文件
* 所有配置文件都应该有版本控制。
* 遵循DRP原则
