去年的Google大会上，Google带给我们一个小玩具——Android Studio，说它是玩具，是因为它确实比较菜，界面过时，操作不流畅，效率也不高，
但是现在，虽然版本还是0.6，甚至都没到1.0，但是我们可以发现亲儿子到底是亲儿子，现在的Android
Studio已经今非昔比，用了一段时间，简直爱不释手，我觉得，It's time to say goodbye eclipse！

  

本文将带领大家彻底的了解一下Android
Studio，注意：由于天朝的原因，我们的了解过程会比较曲折，但是最终大家会看见曙光，然后你就再也不想回到黑暗了！

  

首先，下载，官网地址：:https://developer.android.com/sdk/installing/studio.html#download想
想还是算了吧，等你打开都可以多敲几行代码了，大家可以去一些国内的分流网站上下载，大家尽情百度吧，这个还是不难的。

  

就是这货了！

  

安装我就不说了，都是程序员，没什么难的，但是有的人安装会出错：

  

大部分的启动失败基本都是由于JDK的环境变量问题，设置JDK的时候注意下把环境变量添加好就OK了。

  

**然后就是启动过程：**

  

![](_resources/Eclipse，到了说再见的时候了——AndroidStudio最全解析image0.jpg)

  

和Eclipse还是比较像的。

  

![](_resources/Eclipse，到了说再见的时候了——AndroidStudio最全解析image1.jpg)

  

选择New或者Import就可以开始我们的项目了，第一次创建的时候，要下载gradle的一些东西，会有些慢。

  

如果是在Eclipse里面的项目，我们可以导出为Android Studio格式，很方便的导入Android Studio开发。

  

![](_resources/Eclipse，到了说再见的时候了——AndroidStudio最全解析image2.jpg)

  

选择导出为 Gradle build file 就ok了。

  

Import的时候，Android Studio就可以自动识别了。

  

这个Gradle来头很大的，是Google用于智能化构建项目的构建集成工具，具体的使用大家可以百度之，总之一句话，他可以把一大串的编译命令用一行代码完成。

  

既然它这么牛逼，慢点就慢点吧。

  

![](_resources/Eclipse，到了说再见的时候了——AndroidStudio最全解析image3.jpg)

  

可以看见，内存使用率还是很优秀的，不像Eclipse那样动不动就上G了。

  

第一次配置好后，我们就可以进入启动界面了，这里我是导入的一个Eclipse项目来演示：

  

**大家先颤抖下吧：**

  

![](_resources/Eclipse，到了说再见的时候了——AndroidStudio最全解析image4.jpg)

  

是不是很优秀的赶脚！

  

不过这个还是来之不易的，首先我们来解决下面子问题：

  

其实默认的界面不是这个样子的，有点像Eclipse，反正就是白底的首先我们先变脸：

  

**点击设置：**

  

![](_resources/Eclipse，到了说再见的时候了——AndroidStudio最全解析image5.jpg)

  

就是那个小扳手，然后选择appearance

  

![](_resources/Eclipse，到了说再见的时候了——AndroidStudio最全解析image6.png)

  

选择Theme为Darcula，这个是程序员装逼也好、护眼也好。总之是不二选择。

  

然后为了解决下中文显示问题，我们需要设置下字体，建议微软雅黑，大小自己设置。

  

![](_resources/Eclipse，到了说再见的时候了——AndroidStudio最全解析image7.jpg)

  

**然后设置下编辑区的字体：**

  

![](_resources/Eclipse，到了说再见的时候了——AndroidStudio最全解析image8.png)

  

随便取个名字再save as一下就可以编辑了。

  

满足广大程序员的心声，我们还要设置一下东西，比如自动提示，不得不说，Android
Studio的自动提示功能非常之强大，但是，如果你要输入“String”，你输入“string”，这个是不会提示的，也就是大小写敏感的，不爽是吗？很简单：

  

![](_resources/Eclipse，到了说再见的时候了——AndroidStudio最全解析image9.png)

  

选择大小写不敏感就ok了！这样你想怎么提示就怎么提示了！

  

然后还有一点不爽，用惯了Eclipse的人会发现，鼠标悬停在程序上的时候，啥也没有了！嗯，对的，Android
Studio默认是没有鼠标悬浮提示的，要用快捷键ctrl+q，这个也有好处吧，比较配置太差的电脑不会卡死了。但是有些比较怀旧的就不肯了，OK，我们改：

  

![](_resources/Eclipse，到了说再见的时候了——AndroidStudio最全解析image10.png)

  

看见没，按照图上的勾选就OK了，熟悉的提示就出来了。

  

还有些其他的设置比如行号啊，tab数啊，什么格式啊，大家在Editor里面都能找到设置，比较简单，大家自力更生吧。

  

OK，我们脸变好了，下面给他赋予灵魂吧。

  

目前最新的版本是0.6，如果是前面的版本升级到0.6的，大家会惊奇的发现，新建一个pj都出错了！嗯，是的，比较坑爹是不是，我刚开始的时候也郁闷了，甚至都卸载
了N次。最后总结下如何修正这个问题：

  

一句话，这个问题是敏感词，大家都懂的，有钱的请使用VPN，有钱没钱的，都请修改host文件，具体可以参考我前面的文章：

  

天朝程序员的一声叹息——改hosts吧

  

然后我们打开SDK Manager，不出意外的话，大家是看不见下面的东西的，除非改了host，用了VPN，我在这里纠结了近2个小时，最后在各种资源的帮助下，
碰巧搞对了，在此分享下，但愿不要再被墙了！

  

![](_resources/Eclipse，到了说再见的时候了——AndroidStudio最全解析image11.png)

  

当然，要勾选force，这个大家都知道了

  

首先我们要升级build tool这个是导致错误的根源！

各种错误，比如：

  

error:1 0 plugin with id 'android' not found.

  

还有什么：

  

error:2 0.。。。。。。。。。。。。

  

![](_resources/Eclipse，到了说再见的时候了——AndroidStudio最全解析image12.jpg)

  

我们首先要升级下到19.1.0.

  

然后我们需要修改下项目中的

  

![](_resources/Eclipse，到了说再见的时候了——AndroidStudio最全解析image13.jpg)

将默认的19.0.3改成19.1.0再try aging就ok了

  

到此为止，基本上不会再出错了，如果出错请洗手洗脸，找个黄道吉日再试。

  

**下面我们来看看它狂帅酷霸拽的一些地方：**

  

![](_resources/Eclipse，到了说再见的时候了——AndroidStudio最全解析image14.png)

  

可以看见，比起Eclipse，它可谓是后现代化了，Google工程师花费大量时间，分析了各种代码编写规范，并在Android
Studio中以实现，一段代码如何写更好，一点便知，代码折叠功能，也让大家看的更赏心悦目。

  

代码提示功能更是越来越完善，这点是Eclipse不能比的。

  

下面我们要看看它最炫的地方了，实时的UI设计功能，大家都知道这次apple来了个playground，可以在编程的同时预览效果，感觉确实很牛逼的样子，我们A
ndroid程序员都要吓尿了，其实尿完了才发现，它真的是个playground，目前功能还只是让你玩的，还没有牛逼到我们想要的那种程度，不过确实要赞一个，如
果真能这样编程，估计Every One Is A Coder了。

  

这次的版本，UI设计越来越牛逼了，可以在编程的同时预览效果，当然只是xml的，不是实时编译运行预览，唉，希望这一天早点到来。

  

随便弄了个界面，不要喷我，谢谢：

  

![](_resources/Eclipse，到了说再见的时候了——AndroidStudio最全解析image15.jpg)

  

**design界面差不多，再看text界面：**

  

![](_resources/Eclipse，到了说再见的时候了——AndroidStudio最全解析image16.jpg)

  

真心的，现在做UI是不是方便多了，再也不用像个傻逼一样的不停切Tab来看效果了。

  

**再看一些常用功能：**

  

**新建：**

  

**为什么说它也牛逼呢，因为他可以根据你选择的地方来判断你要新建的类型，是java文件还是资源文件，同时提供各种模板：**

  

![](_resources/Eclipse，到了说再见的时候了——AndroidStudio最全解析image17.jpg)

![](_resources/Eclipse，到了说再见的时候了——AndroidStudio最全解析image18.png)

  

很方便有木有。

  

**再看新建工程：**

  

![](_resources/Eclipse，到了说再见的时候了——AndroidStudio最全解析image19.png)

![](_resources/Eclipse，到了说再见的时候了——AndroidStudio最全解析image21.png)

  

自动集成各种模板，方便+1有木有。

  

**再看新建的各种模板：**

  

![](_resources/Eclipse，到了说再见的时候了——AndroidStudio最全解析image21.png)

  

再回去用用Eclipse，你行吗，反正我是不行了。

  

![](_resources/Eclipse，到了说再见的时候了——AndroidStudio最全解析image22.png)

  

嗯，你没看错，这个不是Visual Studio，Android Studio也有这样的小提示了，很智能也很有效果，集成了Google大神们的汗水啊。

  

以上我们都看到的是一个Android的开发IDE，实际上，Google的野心并不限于此，他的目的是想把它打造成一个超越Visual
Studio,超越xCode的集成开发环境，在这里，可以很轻松的使用git、使用svn或者其它项目管理工具，同时Google还提供云服务：

  

![](_resources/Eclipse，到了说再见的时候了——AndroidStudio最全解析image23.png)

  

算了，这个就不说了，说多了都是泪，天朝的看看就行了。

  

**既然是集成环境，各种插件就不可少了：**

  

![](_resources/Eclipse，到了说再见的时候了——AndroidStudio最全解析image24.jpg)

  

大家可以看看，基本上Eclipse上有的插件，这里都有！

  

以上是我这段时间使用Android
Studio的一些所见所得，希望跟大家分享下，支持下Google的亲儿子，虽然他才0.6，但是可以预见，他的未来不可限量。

  

最后附上一些Android Studio的快捷键，当然，习惯了Eclipse的可以直接在设置的keymap中设置快捷键风格为Eclipse即可，看看，她就像
一个女生，不仅长的好看，学习又好，还知书达理，温柔善良，尊老爱幼。叫人怎能不心动呢！

  

**\----常用快捷键**

**  
**

1.Ctrl+E，可以显示最近编辑的文件列表

  

2.Shift+Click可以关闭文件

  

3.Ctrl+[或]可以跳到大括号的开头结尾

  

4.Ctrl+Shift+Backspace可以跳转到上次编辑的地方

  

5.Ctrl+F12，可以显示当前文件的结构

  

6.Ctrl+F7可以查询当前元素在当前文件中的引用，然后按F3可以选择

  

7.Ctrl+N，可以快速打开类

  

8.Ctrl+Shift+N，可以快速打开文件

  

9.Alt+Q可以看到当前方法的声明

  

10.Ctrl+W可以选择单词继而语句继而行继而函数

  

11.Alt+F1可以将正在编辑的元素在各个面板中定位

  

12.Ctrl+P，可以显示参数信息

  

13.Ctrl+Shift+Insert可以选择剪贴板内容并插入

  

14.Alt+Insert可以生成构造器/Getter/Setter等

  

15.Ctrl+Alt+V 可以引入变量。例如把括号内的SQL赋成一个变量

  

16.Ctrl+Alt+T可以把代码包在一块内，例如try/catch

  

17.Alt+Up and Alt+Down可在方法间快速移动

  

**\----不常用快捷键**

  

18.在一些地方按Alt+Enter可以得到一些Intention Action，例如将”==”改为”equals()”

  

19.Ctrl+Shift+Alt+N可以快速打开符号

  

20.Ctrl+Shift+Space在很多时候都能够给出Smart提示

  

21.Alt+F3可以快速寻找

  

22.Ctrl+/和Ctrl+Shift+/可以注释代码

  

23.Ctrl+Alt+B可以跳转到抽象方法的实现

  

24.Ctrl+O可以选择父类的方法进行重写

  

25.Ctrl+Q可以看JavaDoc

  

26.Ctrl+Alt+Space是类名自动完成

  

27.快速打开类/文件/符号时，可以使用通配符，也可以使用缩写

  

28.Live Templates! Ctrl+J

  

29.Ctrl+Shift+F7可以高亮当前元素在当前文件中的使用

  

30.Ctrl+Alt+Up /Ctrl+Alt+Down可以快速跳转搜索结果

  

31.Ctrl+Shift+J可以整合两行

  

32.Alt+F8是计算变量值

  

以上。

  

来自：eclipse_xu - CSDN博客

链接：http://blog.csdn.net/eclipsexys/article/details/30748339

  

—————————————————  

●本文编号422，以后想阅读这篇文章直接输入422即可。  

●本文分类“**工具**”、“**安卓开发**”，搜索分类名可以获得相关文章。

●输入m可以获取到全部文章目录

●输入r可以获取到热门文章推荐

●输入f可以获取到全部分类名称

—————————————————

**小猿个人微信：itcodemonkey 欢迎调戏**

**  
**

**推荐一个微信公众号：IT电商网，长按下面的微信号可以进行复制******

**itdianshang**

**  
**

**点击“阅读原文”可关注**

**  
**

![](_resources/Eclipse，到了说再见的时候了——AndroidStudio最全解析image25.)

阅读原文 举报

[阅读原文](http://mp.weixin.qq.com/s?__biz=MjM5NzA1MTcyMA==&mid=201677531&idx=2&sn
=8ae039835bce5e216de3f44d292dcfbf&scene=0#rd)

