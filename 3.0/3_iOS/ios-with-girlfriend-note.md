# 给女朋友的 iOS 开发教程学习笔记

这是来自网络的一个视频教程，以一个完整项目为实战，感觉应该还是不错的，地址在[这里](https://www.youtube.com/watch?v=LEQpV9znZsk)。

基本会覆盖以下内容：

+ Design
+ Network
+ API
+ Xcode 7
+ Swift
+ UICollectionView
+ UIImageView
+ Cocoapods
+ UIButton
+ UIKit Animation
+ Core Animation
+ Git

## 1 Design

+ Font
	+ 适应不同风格的技巧：换字体，居中，全大写，加粗，根据表达的意思来更改设计，更改颜色
+ Elements: 多个元素如何组织
	+ 一起居中，靠近，更改背景来切换感觉，用布局来表现逻辑关系，非主题透明度
	+ 英文可以改成大写减少可读性凸现主体
	+ 边距，线条宽度，是否填充
+ Detail
	+ 无谓的圆角，卡片式设计，文字细节斟酌，操作的融合
	+ 打破常规，沉浸式体验，阴影
+ Color
	+ 颜色对比，圆角按钮，线条按钮，更改字体，实心线条，情绪设计
	+ 主题色：渐变，去掉边框，情感

问自己几个问题

+ 我要通过这个设计表达什么情感？
+ 我要通过这个设计强调什么？
+ 我能不能做一些突破？
+ 如何可以更加雕琢设计？

## 2 Design An App

+ Architecture
	+ Tabbar: Apple Music, 微博, iBooks, Medium
		+ 各个部分没有太紧密的逻辑关系
		+ 简化上下文关系
		+ 生产力，高效
		+ 用户容易理解
	+ Slide Menu: VOUN, ThunderSpace HD, Inbox by Gmail, Uber
		+ Unicorn，最核心的功能只有一个
		+ Immediate，可以快速完成操作
	+ Slider: Kickstarter, Tinder, Sooshi
		+ Focus
	+ Waterfall: Twitter, Instagram, Freeshot, Flipboard
		+ Timeline
		+ Efficiency
		+ Just repeating 简单动作重复，让人上瘾
+ Design and Purpose
	+ 开始阶段
		+ Trust 如何让用户相信，愿意去用
		+ Marketing 用户可能会因为应用漂亮而口碑传播
		+ Identity 让人记住，有辨识度
	+ 发展阶段
		+ Productivity
		+ Function 与产品的定位有关
			+ Category 定位
			+ Character 给人的感觉
			+ Design is not just what it looks like and feels like. Design is how it works. --- Steve Jobs
	+ User Interface
		+ Consistency 一致性
			+ Font Style
			+ Layout
			+ Elements
			+ Color
			+ Interaction 
		+ Custom
			+ Along with your function
			+ Unique experience
			+ Journey of soul 

## 3 Design Interface

Sketch 的使用教程

+ `a`: 打开不同设备不同尺寸模板
+ 按住 `shift` 可以得到正圆形/正方形/正多边形
+ 可以点击 `edit` 来编辑多边形
+ 可以给不同的元素弄成一个 group 方便管理
+ 等比例缩放用 `scale` 工具
+ 注意渐变的使用
+ 可以用 rectangle + radius 来做圆角按钮
+ Avenir 字体很漂亮
+ Mask 功能

其他的都可以自己慢慢摸索，不算特别难，设计部分需要慢慢学习，这里就是大概了解工具怎么用

## 4 Code Swift

前面说了很多编程历史，照这样看来我也可以怒吹一波，接下来是利用 Playground 带大家入门，很基础，其实看我的学习笔记也是可以的

## 5 Code Swift Advance

讲的是面向对象的内容，还是可以看我的学习笔记

## 6 Meet iOS APP

比较基础，这里记录一下大概的步骤

+ 创建一个 Single View Application
+ Debug View Hierarchy 可以把 app 界面立体分解，一个层级结构
+ View Hierarchy 是一个好东西，很清晰展现布局
+ Xcode 基本的使用指导，界面与功能
+ 在 build 到真机的时候会有问题(swift 才会出问题)
	+ Library not loaded: @rpath/libswiftCore.dylib
	+ 最重要的一步，要下载一个[证书](http://developer.apple.com/certificationauthority/AppleWWDRCA.cer)
	+ 安装之后重新 clean build 一下就好了
+ 在 storyboard 中的 custom class 选择关联的 `view controller`
	+ 类似于安卓中 `findviewbyID`
+ `UIViewController` 自带一个 `UIView`
	+ 可以在 `viewDidLoad()` 中对 `view` 变量进行操作
	+ 如：`view.backgroundColor = UIColor.greenColor()`
+ 按住 `option` 键指向函数或者变量可以查看帮助
+ 添加控件可以直接拖拽，然后通过在 `Alignment` 里添加 `Horizantally` 和 `Vertically` 两个约束来让某一个控件居中
+ 给 button 添加动作，切换视图 `show assistant editor`
+ 左键单击 button 并按住 ctrl，从 storyboard 拖一条线到代码中，就可以生成对应执行操作的代码(注意要选择 Action 而不是 outlet，outlet 相当于是连接控件的变量)
+ 插入图片需要对宽度和高度进行约束
+ 图片资源添加到 Assets 里

## 7 AutoLayout

+ 代码布局比较灵活
+ AutoLayout 可能是未来的趋势
+ 添加图片之后，如果没有限定高度和宽度，虚拟的黄线是实际显示的大小
+ 有冲突的时候可以选择不同的解决办法
	+ update frames 是通过修改控件来解决冲突
	+ update constrains 是通过修改约束来解决冲突
	+ reset to suggested constrain 是让 Xcode 自己搞定
	+ 一般我们选第一个
+ 在有了第一个元素之后，添加之后的元素，可以利用类似安卓中 relative layout 的机制来进行绑定
	+ 点击要绑定(还没有任何约束)的控件，按住 ctrl 用鼠标拖一个箭头到被绑定的控件(已有设定好的约束)上
	+ 如果出现红线，表示绑定的条件还不充分，Xcode 无法决定其具体位置
+ command + 方向键可以旋转屏幕，来测试不同方向下的效果
+ 合理利用不同类型的约束来完成界面相互依存逻辑的配置，注意这里也可以用一些设计模式来保证不会随便就出冲突，重点在于确定页面上最重要的元素，或者直接可以用隐藏的占位控件来做约束的 base

## 8 UITableView

+ 一个 `UITableView` 控件是由一个 `TableViewWrapperView` 和 许多 `TableViewCell` 组成的
+ 不会把所有的行都显示出来，而是通过一个重用机制，假设有 N 行，那么会在上下各多生成一行，共 N+2 行
+ 另一个概念是 Sections，方便组织不同类别的数据
+ `UITableView` 将由 Controller 提供数据和指定交互动作，具体是通过两个 protocol 指定的(`UITableViewDataSource` - data, `UITableViewDelegate` - interaction)
+ `UITableViewDataSource`
	+ `numberOfSectionsInTableView`
	+ `numberOfRowsInSection`
	+ `cellForRowAtIndexPath`
	+ ...
+ `UITableViewDelegate`
	+ `heightForRowAtIndexPath`
	+ `didSelectRowAtIndexPath`
	+ `willDisplayCell`
	+ ...
+ 如果想在代码中操作对应的控件，需要先按住 ctrl 拖一个 outlet 关系到代码中
+ 至于是 update frame 还是 update constrain 需要灵活一点根据需要来，没有一刀切的东西
+ `TableView` 通过 `TableViewCell` 的 identifier 来找到对应的 cell
+ `indexPath.row` 确定是第几行
+ 选择 TableView 所在的 View Controller 然后拖一条线到新建的另一个 View Controller 上，连接类型选择 Show，然后给对应的 Segue 命名
+ 用 `performSegueWithIdentifier`，然后传入刚才给 segue 命名的 identifier
+ 重写 `prepareForSegue` 方法来准备传入的数据
+ 强制转换中使用 `as!` 进行检查
+ 记得要把 `delegate` 和 `datasource` 都进行绑定，不然并不会执行对应的操作



