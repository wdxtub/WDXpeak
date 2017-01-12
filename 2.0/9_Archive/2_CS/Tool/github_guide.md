# Github 生活指南

<!-- MarkdownTOC -->

- 10 个功能
    - 1、拖拽Gist代码
    - 2、通过Web界面创建文件夹
    - 3、使用Git URL短地址
    - 4、文件查找
    - 5、使用Github Emoji
    - 6、使用Github命令行
    - 7、链接
    - 8、任务清单
    - 9、Map、 CSV 和 3D 渲染**
    - 10、Octodex
- Q: 如何追随大牛
- 在学习区刻意练习：借助GitStats进行项目统计

<!-- /MarkdownTOC -->


## 10 个功能

接触 github 以来，愈发喜欢这种简单明了自在掌控的生活，也有很多前辈给出了许多非常好的实践方法，在这里记录下来，成为极简主义生活的一部分。

Github 让全世界的开发人员、设计人员可以在一起工作交流。Github不仅提供大量开源项目、编程语言代码，他也发布过Windows 和 OS X桌面应用，可以让我们在工作中无缝集成Github 。

不过，有很多Github功能还是不为大多数人熟知，这里慧都控件网为大家收集了10个不可不知的Github功能。

### 1、拖拽Gist代码

Gist是 Github专有功能。可以让我们管理代码片段。当然，你还可以浏览并找到大量的各种语言的代码片段。Gist使用简单并且直观。不过，你知道吗，你可以直接添加代码文件？只需要将文件在 Gist拖拽，文件中的代码会立即被复制。这可节约不少时间。

### 2、通过Web界面创建文件夹

大多数人管理Github仓库是使用免费的Github应用程序。Github也创建了一个叫WebFlow的应用，可以让我们在web界面上管理内容。

### 3、使用Git URL短地址

就像我们在新浪微博分享照片文章一样。在Github也可以分享项目。不过分享的地址可能会超出微博的限制长度。

那么我们可以将网址缩短，使用Github的Git.io。Git.io将会缩短你的项目地址连接。也可以使用gitio命令，Git.io的命令行接口来缩短地址。

### 4、文件查找

处理新建文件，你还可以在任何存储库快速浏览这些文件。该功能不是太明显，需要快捷方式，在键盘上按"T"激活文件查找功能。在按上下键上下查找。当然，也可以输入文件名称来选择特定的文件 。

### 5、使用Github Emoji

Github也可以使用Emoji，我们可以在 the Emoji Cheat Sheet找到所有表情符号的代码。这些代码可以添加到各种项目的README.md文件中。

### 6、使用Github命令行

虽然大多数人喜欢使用GUI工作，不过还是有人喜欢 CLI (Command Line Interface)，对于这样的人，Github CLI就是最爱了。Github CLI 以 hub开始。它带来了可以使用git命令的其他命令。>>查看Hub

### 7、链接

有时候我们需要在自己的文件项目中分享或者输出特殊行。Github可以实现，我们只需要添加"#L "放在URL行号后面，请看图。

### 8、任务清单

Github 扩展了markdown来满足自己的需要，现在你可以在Github上添加一个复选框列表，使用 - [ ] or - [x]来表示一个检查项目。请注意,复选框只会出现在列表项中。"[ ]"必须以"‐"开始。

### 9、Map、 CSV 和 3D 渲染**

Gihub支持CSV，如果你有csv文件，Gihub会将这个文件渲染成交互式表格数据格式。你也可以搜索。除此之外，Gihub会以geoJSON格式渲染地图，STL extension渲染3D。

### 10、Octodex

本文最后一个但并不是最不重要的。你知道Github有各种版本的吉祥物——Octocat（章鱼猫）吗？Google有googledoodle，Github有Octocat。各式各样的Octocat是不是让你感觉很有爱？Labtocat、Femalecodertocat、Octoliberty、SpidertocatMegacat...你可以使用它们作为自己的头像

---

## Q: 如何追随大牛

**在学习区刻意练习。**

    修行之道：
    关注大师的言行，
    跟随大师的举动，
    和大师一并修行，
    领会大师的意境，
    成为真正的大师

具体的做法是在 Github 上：

+ watch、fork牛人们
+ 对他们的项目提交pull request
+ 主动给牛人们的项目写wiki或提交测试用例，或者问题
+ 还可以帮他们翻译中文

**牛人在哪里？**

+ GitHub上的代码库本身：尤其是：Explore、热门关注信息库两个栏目
+ GitHub官方推荐：GitHub自身的官方博客与GitHub员工们的个人博客推荐的项目与开发者
+ 各类社交媒体上提到的的GitHub库：尤其是Hacker News上提到的GitHub库。

关于学习的心理学研究，常常会谈到一个术语：元认知、元学习、元知识。是的，关于认知的认知、关于学习的学习、关于知识的知识，你对这些信息的偏好与熟练掌握，会让你在学习一门新东西时更加轻车熟路。对一手信息进行回溯，比如作者、创始人、最初文献出处，总是会让你更容易理解知识。


## 在学习区刻意练习：借助GitStats进行项目统计

借助于GitStats，我们能很好地统计自己的每个项目的工作量，从而看到工作进展。

用法如下，

    #复制GitStats项目到本地
    cd ~/dev
    git clone git://github.com/trybeee/GitStats.git
    python ~/dev/gitstats/git-stats /youproject public

这个给出的图表比较丑，将就看吧
