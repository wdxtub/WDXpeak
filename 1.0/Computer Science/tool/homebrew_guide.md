Mac OS X是基于Unix的操作系统，可以安装大部分为Unix/Linux开发的软件。然而，如果只是以使用为目的，对每个软件都进行手工编译不是很方便，也不利于管理已安装的软件，于是出现了类似于Linux中APT、Yum等类似的软件包管理系统，其中最著名的有MacPorts、Fink、Homebrew等。

我曾经是MacPorts的使用者，但了解Homebrew之后，立即“弃暗投明”了。其实MacPorts也是一个很不错的解决方案，除了一个实在让我头疼的特性。MacPorts有个原则，对于软件包之间的依赖，都在MacPorts内部解决（/opt/local），无论系统本身是否包含了需要的库，都不会加以利用。这使得MacPorts过分的庞大臃肿，导致系统出现大量软件包的冗余，占用不小的磁盘空间，同时稍大型一点的软件编译时间都会难以忍受。

而Homebrew的原则恰恰相反，它尽可能地利用系统自带的各种库，使得软件包的编译时间大为缩短；同时由于几乎不会造成冗余，软件包的管理也清晰、灵活了许多。Homebrew的另一个特点是使用Ruby定义软件包安装配置（叫做formula），定制非常简单。

至于Fink，由于并未安装使用过，不加讨论。（从互联网上的消息看，Fink由于维护人手的问题，软件包的更新不是很及时。）于我而言，Homebrew已经足够完善，除非发现重大的问题或者出现新的具有突破性的竞争对手，否则我没兴趣折腾别的软件包管理系统了。


Homebrew的安装非常简单，在终端程序中输入以下命令即可。

    ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"

由于Homebrew的安装地址可能变化，请到官方网站查看最新的安装方法。

安装过程需要输入root口令。

### Homebrew的使用

Homebrew的可执行命令是brew，其基本使用方法如下（以wget为例）。

+ 查找软件包 brew search wget
+ 安装软件包 brew install wget
+ 列出已安装的软件包 brew list
+ 删除软件包 brew remove wget
+ 查看软件包信息 brew info wget
+ 列出软件包的依赖关系 brew deps wget
+ 更新 brew update
+ 列出过时的软件包（已安装但不是最新版本）brew outdated
+ 更新过时的软件包（全部或指定）brew upgrade 或 brew upgrade wget
