# Mac 指南

## 关闭 rootles

开机按住Command＋R，进入恢复模式，打开terminal，键入：

csrutil disable

回车，重新启动即可。要重新恢复，只需将disable改为enabl

## 重建 Mail 索引

当邮箱出现问题时，您可能会看到提醒信息说“邮件”需要通过重新索引邮件来修复邮箱。

在其他时候，您可能想要自己重新索引邮件，例如，使用“主题”、“收件人”或“发件人”搜索邮箱时未返回正确结果时。

如果“邮件”已打开，请退出它。

在“User/资源库/Mail/V3/MailData”中，删除任何以“Envelope Index”开头的文件，如 Envelope Index 或 Envelope Index-shm。

默认情况下，您的“资源库”个人文件夹处于隐藏状态。若要显示它，请选取 Finder >“前往文件夹”，然后输入“~/资源库”。

打开“邮件”。

“邮件”将创建新 Envelope Index 文件。此过程可能需要几分钟，取决于“邮件”要重新索引的邮件数量。

## 清除 PRAM (只适用于英特尔的苹果电脑)

这个方法不是根本的解决方法，但是可以除去一些不必要的开机设置。因而也节省了时间。方法是：重启你的电脑，同时按下 command + option + p + r 直到听到3 到4 声启动铃响之后松手。


## 清除PMU (iMac不适用)

对于Macbook, Macbook Pro用户，方法是：

1. 确保Macbook关闭.
2. 去掉电源适配器和电池.
3. 按下电源开关并保持5 秒钟，放开.
4. 接上电源适配器和电池.
5. 打开电源开关.

## 显示/隐藏 隐藏文件

    defaults write com.apple.finder AppleShowAllFiles -bool true
    defaults write com.apple.finder AppleShowAllFiles -bool false

## 想接收最新开发者版本，在Terminal输入：

    sudo defaults write /Library/Preferences/com.apple.SoftwareUpdate CatalogURL https://swscan.apple.com/content/catalogs/others/index-10.10seed-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog.gz

## 想接收最新公测版版本，在Terminal输入：

    sudo defaults write /Library/Preferences/com.apple.SoftwareUpdate CatalogURL https://swscan.apple.com/content/catalogs/others/index-10.10beta-10.10-10.9-mountainlion-lion-snowleopard-leopard.merged-1.sucatalog.gz

## 停止接收开发者或公测版，只接收正式版推送方法，在Terminal输入：

    sudo softwareupdate --clear-catalog

## 应用推荐

付费软件：

+ 1Password：密码管理；
+ BetterZip2：解压缩；
+ MacHider：文件隐藏(最新版是Hider2)
+ Parallels Desktop：虚拟机
+ CleanMyMac 2：垃圾清理
+ dash：文档管理
+ 马克飞象：印象笔记第三方插件
+ eeder2(feedly)：文章订阅
+ Mind Preview：思维导图软件

免费软件：

+ Alferd：提高效率的神器
+ MPlayerX：视频播放器，播放各种格式视频
+ 印象笔记：云笔记软件
+ iTerm2：命令行终端
+ Pocket：稍后读软件
+ SiteSucker：网站备份工具
+ LICEcap：截取GIF动态图
+ ImageAlpha(Pngyu)：png图片压缩

命令行工具：

+ Homebrew：包管理神器

下面列出这些购买建议：

+ 建议尽量选择冰点价格或打折促销时购入，可以选择mou.li这样的团购代购服务；
+ 部分软件开发商会有官方团购打折；
+ 家庭装促销包授权适合家里人一起使用；
+ 关注和参与个人或集体组织的团购活动；
+ 选择购买Mac App Store的版本通常升级后续版本会 Free；
+ 部分 Apps 只有Mac App Store 版会有iCloud同步功能；
+ 如果官方有非沙盒版，建议不要选择Mac App Store的阉割版，购入原版；


