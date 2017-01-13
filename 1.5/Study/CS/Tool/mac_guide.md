# Mac 指南

<!-- MarkdownTOC -->

- 清除 PRAM (只适用于英特尔的苹果电脑)
- 清除PMU (iMac不适用)
- 显示/隐藏 隐藏文件
- 想接收最新开发者版本，在Terminal输入：
- 想接收最新公测版版本，在Terminal输入：
- 停止接收开发者或公测版，只接收正式版推送方法，在Terminal输入：
- 应用推荐

<!-- /MarkdownTOC -->

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
