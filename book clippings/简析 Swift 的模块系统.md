![](_resources/简析 Swift 的模块系统image0.jpg)

Swift 中模块是什么？当写下 Swift 中一句 import Cocoa 的时候到底做了什么？官方 iBook 很含糊只是提了半页不到。

  

本文解决如下问题：

1\. 介绍 Swift 中两种可 import 的模块

2\. 如何用 Swift 写一个可被其他 Swift 代码使用的模块

3\. 分析 Swift 的标准库实现方式

  

**第一部分 Clang 模块（系统模块）**

Clang 模块是来自系统底层的模块，一般是 C/ObjC 的头文件。原始 API 通过它们暴露给 Swift ，编译时需要链接到对应的 Library。

  

例如 UIKit、Foundation 模块，从这些模块 dump 出的定义来看，几乎是完全自动生成的。当然， Foundation 模块更像是自动生成
\+ 人工扩展（我是说其中的隐式类型转换定义、对 Swift 对象的扩展等，以及 @availability 禁用掉部分函数。）。相关函数声明可以从我的
Github andelf/Defines-Swift 获得。

  

我可不觉得这些定义全部都是官方生成后给封装进去的。所以在整个 Xcode-6 beta2 目录树里进行了探索。

  

在 Xcode 目录寻找相关信息，最后目标锁定到了一个特殊的文件名 module.map。

  

原来这个文件叫 Module map(这个名字还真是缺乏想象力)，属于 llvm 的 Module 系统。本来是用来颠覆传统的 C/C++/Objc 中的
#include 和 #import。最早在 2012 年 11 月的 LLVM DevMeeting 中由 Apple 的 Doug Gregor
提出。相关内容 CSDN 也有文章介绍，不过是直译版，没有提出自己见解。

  

**关于 llvm Module 系统**

2012 年提出概念，所以其实这个东西已经很早就实现了。简单说就是用树形的结构化描述来取代以往的平坦式 #include，例如传统的 #include
<stdio.h> 现在变成了 import std.io;，逼格更高。主要好处有：

1\. 语义上完整描述了一个框架的作用。

2\. 提高编译时可扩展性，只编译或 include 一次。避免头文件多次引用，只解析一次头文件甚至不需要解析（类似预编译头文件）。

3\. 减少碎片化，每个 module 只处理一次，环境的变化不会导致不一致。

4\. 对工具友好，工具（语言编译器）可以获取更多关于 module 的信息，比如链接库，比如语言是 C++ 还是 C。

5\. 等等。

  

所以这么好的一个东西， Apple 作为 llvm 的主力，在它的下一代语言中采用几乎是一定的。

  

算了，我是个半路出家的，之前没接触过 iOS / MacOSX 开发，其实 2013 年的 WWDC， Apple 为 Objective-C 加入的
@import 语法就是它。可以认为，这是第一次这个 Module 系统得到应用。

  

**module.map 文件**

module.map 文件就是对一个框架，一个库的所有头文件的结构化描述。通过这个描述，桥接了新语言特性和老的头文件。默认文件名是
module.modulemap，module.map 其实是为了兼容老标准，不过现在 Xcode 里的还都是这个文件名，相信以后会改成新名字。

  

文件的内容以 Module Map Language 描述，大概语法我从 llvm 官方文档摘录一段，大家体会一下：

module MyLib {

explicit module A {

header "A.h"

export *

}

explicit module B {

header "B.h"

export *

}

}

  

类似上面的语法，描述了 MyLib、MyLib.A、MyLib.B 这样的模块结构。

  

官方文档中有更多相关内容，可以描述框架，描述系统头文件，控制导出的范围，描述依赖关系，链接参数等等。这里不多叙述，举个 libcurl 的例子：

module curl[system] [extern_c] {

header "/usr/include/curl/curl.h"

link "curl"

export *

}

  

将此 module.map 文件放入任意文件夹，通过 Xcode 选项或者命令行参数，添加路径到 import search path （swift 的
-I 参数）。然后就可以在 Swift 代码里直接通过 import curl 导入所有的接口函数、结构体、常量等，(实测，发现
curl_easy_setopt 无法自动导入，看起来是声明语法太复杂导致）。

  

甚至可以直接从 swift repl 调用，体验脚本语言解释器般的快感（因为我们已经指定了链接到 curl 库）。

  

Xcode 选项位于 Build Settings 下面的 Swift Compiler – Search Paths 。添加路劲即可。

  

再举个复杂点的 SDL2.framework 的例子，看看如何实现树形的模块结构，这个需要把 module.map 放到 .framework 目录里

framework moduleSDL2 [system] {

umbrella header "SDL.h"

link -framework SDL2

module Version {

header "SDL_version.h"

export *

}

module Event {

header "SDL_events.h"

export *

}

// ....

export *

module * {

export *

}

}

  

**小结**

Swift 的 C 模块（也是它的标准库部分）完全就是 llvm 的 Module 系统，在 import search path 的所有
module.map 中的模块都可以被识别，唯一缺点可能是如果有过于复杂用到太多高级 C 或者黑暗 C 语法的函数，无法很好识别，相信以后的版本会有所改善。

  

所以当有人问 Swift 到底有多少标准库的时候，答案就是，基本上系统里所有的 Objective-C 和 C 头文件都可以调用。

  

自 iOS 7 时代，这些头文件就已经被组织为 Module 了，包括标准 C 库 Darwin.C。同样因为 Module 系统来自于传统的
C/C++/Objc 头文件，所以 Swift 虽然可以有 import ModA.ModB.ModC 的语句，但是整个模块函数名字空间还是平坦的。

  

一些有意思的模块可以探索探索，比如 simd，比如 Python（没错是的，直接调用 Python 解释器）等。

  

另外 Swift 的 -module-cache-path 参数可以控制这类模块预编译头的存放位置（ .pcm 文件： pre compiled
module）。

  

Xcode 项目的 Build Settings ， Apple LLVM 6.0 – Language – Modules 有项目对 Module
支持的相关选项，默认是打开的。

  

**第二部分 Swift 模块**

说完了系统模块，该说 Swift 模块了。 Swift 自身的这个系统还是很赞的。

  

本节介绍怎样用 Swift 创建一个可 import 的模块。

  

**几个文件类型**

先清楚几个文件类型。假设 ModName.swift 是我们的 Swift 源码文件。

  

*ModName.swiftmodule Swift 的模块文件，有了它，才能 import;

* ModName.swiftdoc保存了从源码获得的文档注释（文档注释以 /// 开头）;

*libswiftModName.dylib 动态链接库;

*libswiftModName.a 静态链接库;

  

TODO: 目前有个疑问就是 .swiftmodule 和链接库到底什么时候用哪个，以及具体作用。

  

**.swift 源码文件**

先明确一个概念，一个 .swift 文件执行是从它的第一条非声明语句（表达式、控制结构）开始的，同时包括声明中的赋值部分（对应为 mov 指令或者 lea
指令），所有这些语句，构成了该 .swift 文件的 top_level_code() 函数。

  

而所有的声明，包括结构体、类、枚举及其方法，都不属于 top_level_code()
代码部分，其中的代码逻辑，包含在其他区域，top_level_code() 可以直接调用他们。

  

程序的入口是隐含的一个 main(argc, argv) 函数，该函数执行逻辑是设置全局变量 C_ARGC C_ARGV，然后调用
top_level_code()。

  

不是所有的 .swift 文件都可以作为模块，目前看，任何包含表达式语句和控制控制的 .swift 文件都不可以作为模块。正常情况下模块可以包含全局变量(v
ar)、全局常量(let)、结构体(struct)、类(class)、枚举(enum)、协议(protocol)、扩展(extension)、函数(func
)、以及全局属性(var { get set })。这里的全局，指的是定义在 top level 。

  

这里说的表达式指 expression ，语句指 statement ，声明指 declaration 。可能和有些人对相关概念的定义不同。实际上我特无奈有
些人纠结于概念问题，而不是问题本身，本来翻译过来的舶来品就有可能有误差，当你明白那指的是什么的时候，就可以了。

  

**模块编译方法**

这里先以命令行操作为例，

xcrun swift -sdk$(xcrun --show-sdk-path --sdk macosx) ModName.swift -emit-
library -emit-module-module-name ModName -v -o libswiftModName.dylib -module-
link-name swiftModName

  

执行后获得 ModName.swiftdoc、ModName.swiftmodule、libswiftModName.dylib.

  

这三个文件就可以表示一个可 import 的 Swift 模块。目前看起来 dylib 是必须得有的，否则链接过程报错。实际感觉 .swiftmodule
文件所包含的信息还需要继续挖掘挖掘。

  

多个源码文件直接依次传递所有文件名即可。

  

静态链接库 .a 目前还没有找到方法， -Xlinker -static 会报错。

  

**命令行参数解释**

相关命令行参数：

-module-name<value> ：Name of the module to build 模块名；

  

-emit-library： 编译为链接库文件；

  

-emit-module-path<path> ：Emit an importable module to 编译模块到路径（全路径，包含文件名）；

  

-emit-module Emitan importable module；

  

-module-link-name<value> Library to link against when using this module 该模块的链接库名，就是 libswiftModName.dylib，这个信息会直接写入到 .swiftmodule；

  

**使用模块**

使用模块就很简单了，记住两个参数：

-I 表示 import search path ，前面介绍过，保证 .swiftmodule 文件可以在 import search path 找到（这点很类似 module.map 文件，找得到这个就可以 import 可以编译）；

  

-L 表示链接库搜索路径，保证 .dylib 文件可以在其中找到，如果已经在系统链接库目录中，就不需要这个参数。

  

例如：

xcrun swift -sdk$(xcrun --show-sdk-path --sdk macosx) mymodtest.swift -I. -L.

  

此时表示所有 module 文件都在当前目录。

  

这两个选项都可以在 Xcode 中指定，所以如果你有小伙伴编译好的 module 想在你的项目里用是完全 ok 的。

  

**For Xcode**

很不幸，没能在 Xcode 中找到编译模块的相关方法。等我发现如何搞定的时候我会补上这个坑。

  

不过在任何含 Swift 项目的编译过程中， .swiftmodule 文件总是伴随着 .o 文件传递。

  

**第三部分瞎分析 .swiftmodule 文件**

简单分析下一个 .swiftmodule 所包含的信息。

  

**Foundation**

这里先以标准库的 Foundation.swiftmodule 下手。

  

用 hexdump 查看发现它包含所有导出符号，以及 mangled name 。还有个文件列表，表示它是从哪些文件获得的（可以是 .swift 也可以是
.swiftmodule ）。

  

用 strings 列出内容，发现 Foundation 库有如下特征:

...

Foundation

LLVM 3.5svn

/SourceCache/compiler_KLONDIKE/compiler_KLONDIKE-600.0.34.4.8/src/tools/swift/
stdlib/objc/Foundation/Foundation.swift

/SourceCache/compiler_KLONDIKE/compiler_KLONDIKE-600.0.34.4.8/src/tools/swift/
stdlib/objc/Foundation/KVO.swift

/SourceCache/compiler_KLONDIKE/compiler_KLONDIKE-600.0.34.4.8/src/tools/swift/
stdlib/objc/Foundation/NSStringAPI.swift

CoreFoundation

Foundation

Swift

swiftFoundation

...

  

可以大胆猜测对应下：

-module-name =>Foundation

编译环境 => LLVM 3.5svn

源文件列表 => …

依赖列表 => CoreFoundation, Foundation, Swift

-module-link-name=> swiftFoundation

  

我由此猜测， Foundation 的确是只有少量 Swift 代码做桥接。然后通过 Clang 模块将剩下工作交到底层。

  

分析其他类似模块也得到相同结果。

  

**Swift 标准库**

接下来有点好奇标准库 Swift 是怎么实现的。得到如下结果。

  

节选重要部分到我的 Gist

  

里面有些很有意思的信息，有兴趣的同学可以去看看。

  

依赖模块 SwiftShims 是一个 module.map 定义的模块，桥接的部分头文件。源文件有相关信息和注释。大致意思是用来实现几个底层接口对象，比如
NSRange 邓。

  

其中-module-link-name 是 swift_stdlib_core。

  

**结论**

LLVM Module 作为 Apple 提出的特性，已经被 Swift
完全采用，直接在它基础上建立了自己的模块系统。我相信它会影响到我们处理第三方库的方式方法。相信不久就会有相关工具基于它来管理依赖关系，比如老的
cocoapods4 可以加入新特性。

  

用 Swift 写模块目前并没有很好的 IDE 支持，所以不是很方便。基于猜测验证，上面的方法可以实现在 Swift 里 import Swift
模块，方法和结果看起来完全和官方模块相同。

  

Swift 的标准库完全是上面两种模块的结合体，用 Swift 模块封装 Clang
模块。这就解决了文章一开始提出的问题：为什么标准库大部分看起来是自动生成代码，少部分又好像是人工写的接口代码。

\------------------------------------------------------------

如果这篇文章对您或您的朋友有所帮助，您可以点击右上角的更多按钮 ![](_resources/简析 Swift 的模块系统image1.jpg)

分享给您的朋友们~ ![](_resources/简析 Swift 的模块系统image2.jpg)

CocoaChina是全球最大的苹果开发中文社区，它的官方微信每日定时推送各种精彩的研发教程资源和工具，介绍app推广营销经验，最新企业招聘和外包信息，以及
Cocos2d引擎、Cocos Studio开发工具包的最新动态及培训信息。关注微信可以第一时间了解最新产品和服务动态！

请搜索微信号“CocoaChina”关注我们 ![](_resources/简析 Swift 的模块系统image3.jpg)

  

[阅读原文](http://mp.weixin.qq.com/s?__biz=MjM5OTM0MzIwMQ==&mid=200773823&idx=1&sn
=42df903f79099d5519a262438f639ebf&scene=0#rd)

