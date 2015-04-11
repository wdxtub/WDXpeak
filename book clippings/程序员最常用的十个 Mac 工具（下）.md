![](_resources/程序员最常用的十个 Mac 工具（下）image0.jpg)

截至到现在，我一共收获了两千多个干货，微信服务器也回复了两千多根劈柴，我想大家这次一定满足了吧！

经此一役，我终于认识到了大伙对干货的渴求就像干柴渴望烈火、沙漠遭遇绿洲，放心吧，我一定会继续努力的！以后的文章将只有 「Linux 内核编程」、「iOS 和
OS X中的 Block 和 GCD」、「进程、轻量级进程和线程的那点事儿」、「ARC 的自我觉醒」、「文件系统的沧海桑田」等等……等等，请各位留意阅读！

今天继续介绍剩下的七种武器：

#### Vim

文本编辑器同样是程序员最喜爱的开发工具之一，我个人偏爱
Vim。Vim号称编辑器之神，可以脱离鼠标全键盘操作，良好的插件体系几乎适配各类编程语言，使用起来充满推背的速度感，如果你是个赛车迷，你会喜欢上这款软件的。

回复「vim」，查看我之前写的 Vim 系列。

其他可选工具：Emacs、TextMate、Sublime Text等。

#### Xcode、JetBrains 系列和 Eclipse 系列

IDE 是图形化的集成开发工具，具备精准的词法分析、编程提示、调试等功能，功能之繁复用户自知，如果做工业级编程和团队协作的话，推荐使用 IDE。

在这里给大家推荐如下几个工具：  
1、Xcode，Mac 上优秀的集成开发工具，几乎所有的 Mac App 和 iOS App 都由此而生，免费软件。  
无论你是 写 Java 的还是写 Python，用了 Mac 一定要安装 Xcode，为什么？我准备写一篇「更有效率的
XCode」说一下这个事情，当然，这样的内容没那么干，如果各位不同意就算了。

2、JetBrains 系列，产品线丰富，几乎都是精品，Java、Python、Ruby、Php、Objective-C、Web 等一应俱全，收费，还挺贵。

3、Eclipse 系列，通过插件方式几乎支持所有的常用编程语言，免费。

#### Homebrew 和 Cask

Homebrew 是 OS X 的包管理工具，Ruby 社区的作品，功能类似 Ubuntu 下的apt-get。使用 Homebrew 可以非常容易的安装
OS X 中没有包含的 Unix 工具包和语言包，比如 wget，node，lua，rabbitmq，nginx 等。当然，我们得首先安装
Homebrew，安装脚本如下：

`ruby -e "$(curl -fsSL https://raw.github.com/Homebrew/homebrew/go/install)"`

一段类似黑客帝国里的脚本过去之后，Homebrew 就装好了。尝试一下安装命令行下载工具 wget：  
brew install wget  
一段类似黑客帝国里的脚本过去之后，wget 就装好了。

* * *

那有没有工具可以用类似的方式安装Chrome 浏览器、离线迅雷、虾米、QQ 呢？答案是肯定的，程序员无所不能，他们开发了Homebrew-
Cask用来一键安装应用软件，有了 Cask，再也不用手动下载软件包 DMG，打开，拖进应用程序文件夹了，一切都可以交给程序去做。

安装 Cast：  
`brew tap phinze/homebrew-cask && brew install brew-cask`

用法：  
brew cask search 列出所有可以被安装的软件  
brew cask search xx 查找所有和 xx 相关的应用  
brew cask info xx 查看xx应用的信息  
brew cask uninstall xx 卸载 xx

尝试一下吧。

#### Git

Git 是一款分布式版本控制和软件配置管理软件，类似 SVN 和 CVS，是 Linus 的第二个惊世之作。关于 Linus 和 Git 的故事，我们会在
Linus 系列里描述，这里就不细聊了。

Git 是目前主流的版本管理工具，基于 Git 构建的 Github 网站则是这个星球上最大的开源集散地。还在使用 SVN 和 CVS
的童靴，该换换脑筋了。

回复「git」，你将获得一份Git 简明教程。

图形化的 Git 工具推荐：GitHub、SourceTree。

#### VisualDiff

对于程序员来说，文件比较也属必备工具，OS X 中提供了原生的比较工具 FileMerge，不过这个工具对非 ASCII 内容的文件支持非常不好，推荐
VisualDiffer。VisualDiffer
支持文件和文件夹比较、文件过滤、多重比较模式、颜色标注等，操作简单，响应迅速，实乃程序员居家旅行之必备工具。收费软件，可以直接从 AppStore 下载。

另外，习惯命令行操作的朋友，直接使用 diff 和 vimdiff，也是不错的选择。

#### xScope

xScope 是一款强大的辅助设计工具，可以精确度量屏幕上的 UI 元素，尤其适合全栈工程师。  
xScope 可以方便的取得屏幕上任意位置的颜色，可以动态智能监测元素边界并显示距离，可以针对移动设备和各种浏览器设定屏幕尺寸，可以设定屏幕辅助线，放大屏幕
等。如果你不想事事求人，xScope是个不错的选择。收费软件。

#### Pixelmator

Pixelmator 号称 Mac 上的精简版 PhotoShop，设计更为人性化，适合非专业人士使用，不是平面设计人员也可以作出非常专业的图像设计。像我这
样的老程序员，也开始时不时设计个物件，让团队里的美工 MM 为之侧目。收费软件。

推荐一个Podcast视频教程：http://www.pixelmator.com/tutorials/itunes/

* * *

内容暂时告一段落吧，关于程序员用 Mac 的内容才刚刚开始，干货还在后面等着……

由于今天的内容干的冒烟，我为不喜欢干货的童靴准备了一个故事，回复「story」阅读……没有好奇心的就不用回复了。

记住今天的三个关键字：vim，git 和 story，再加一个吧：微社区。

觉得文章有价值，随手转发朋友圈，有转发才有未来。

[阅读原文](http://mp.weixin.qq.com/s?__biz=MjM5ODQ2MDIyMA==&mid=100351098&idx=1&sn
=6c67d2d78d331e90d4c9adbf2d9350cf&scene=1#rd)

