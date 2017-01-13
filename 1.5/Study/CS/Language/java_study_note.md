# Java 精要

<!-- MarkdownTOC -->

- 第1章 Java程序设计概述
    - 1.1 Java程序设计平台
    - 1.2 Java“白皮书”的关键术语
    - 1.3 Java Applet与Internet
    - 1.4 Java发展简史
    - 1.5 关于Java的常见误解
- 第2章 Java程序设计环境
- 第3章 Java基本的程序设计结构
    - 3.1 一个简单的Java应用程序
    - 3.2 注释
    - 3.3 数据类型
        - 3.3.1 整型
        - 3.3.2 浮点类型
        - 3.3.3 char类型
        - 3.3.4 boolean类型
    - 3.4 变量
        - 3.4.1 变量初始化
        - 3.4.2 常量
    - 3.5 运算符
        - 3.5.1 自增运算符与自减运算符
        - 3.5.2 关系运算符与boolean运算符
        - 3.5.3 位运算符
        - 3.5.4 科学函数与常量
        - 3.5.5 数值类型之间的转换
        - 3.5.6 强制类型转换
        - 3.5.7 括号与运算符级别
        - 3.5.8 枚举类型
    - 3.6 字符串
        - 3.6.1 子串
        - 3.6.2 拼接
        - 3.6.3 不可变字符串
        - 3.6.4 检测字符串是否相等
        - 3.6.5 代码点与代码单元
        - 3.6.6 字符串API
        - 3.6.7 阅读联机API文档
        - 3.6.8 构建字符串
    - 3.7 输入输出
        - 3.7.1 读取输入
        - 3.7.2 格式化输出
        - 3.7.3 文件输入与输出
    - 3.8 控制流程
    - 3.8.1 块作用域
        - 3.8.2 条件语句
        - 3.8.3 循环
        - 3.8.4 确定循环
        - 3.8.5 多重选择：switch语句
        - 3.8.6 中断控制流程语句
    - 3.9 大数值
    - 3.10 数组
        - 3.10.1 For each循环
        - 3.10.2 数组初始化以及匿名数组
        - 3.10.3 数组拷贝
        - 3.10.4 命令行参数
        - 3.10.5 数组排序
        - 3.10.6 多维数组
        - 3.10.7 不规则数组
- 第4章 对象与类
    - 4.1 面向对象程序设计概述
        - 4.1.1 类
        - 4.1.2 对象
        - 4.1.3 识别类
        - 4.1.4 类之间的关系
        - 4.2 使用现有类
        - 4.2.2 Java类库中的GregorianCalendar类
        - 4.2.3 更改器方法与访问器方法
    - 4.3 用户自定义类
        - 4.3.1 一个最简单的类
        - 4.3.2 多个源文件的使用
        - 4.3.3 解析类
        - 4.3.4 从构造器开始
        - 4.3.5 隐式参数与显式参数
        - 4.3.6 封装的优点
        - 4.3.7 基于类的访问权限
        - 4.3.8 私有方法
        - 4.3.9 Final实例域
    - 4.4 静态域与静态方法
        - 4.4.1 静态域
        - 4.4.2 静态常量
        - 4.4.3 静态方法
        - 4.4.4 Factory方法
        - 4.4.5 Main方法
    - 4.5 方法参数
    - 4.6 对象构造
        - 4.6.1 重载
        - 4.6.2 默认域初始化
        - 4.6.3 默认构造器
        - 4.6.4 显式域初始化
        - 4.6.5 参数名
        - 4.6.6 调用另一个构造器
        - 4.6.7 初始化块
        - 4.6.8 对象析构与finalize方法
    - 4.7 包
        - 4.7.1 类的导入
        - 4.7.2 静态导入
        - 4.7.3 将类放入包中
        - 4.7.4 包作用域
    - 4.8 类路径
    - 4.9 文档注释
        - 4.9.1 注释的插入
        - 4.9.2 类注释
        - 4.9.3 方法注释
        - 4.9.4 域注释
        - 4.9.5 通用注释
        - 4.9.6 包的概述注释
        - 4.9.7 注释的抽取
    - 4.10 类的设计技巧
- 第5章 继承
    - 5.1 类、超类和子类
        - 5.1.1 继承层次
        - 5.1.2 多态
        - 5.1.3 动态绑定
        - 5.1.4 阻止继承：final类和方法
        - 5.1.5 强制类型转换
        - 5.1.6 抽象类
        - 5.1.7 受保护访问
    - 5.2 Object：所有类的超类
        - 5.2.1 Equals方法
        - 5.2.2 相等测试与继承
        - 5.2.3 HashCode方法
        - 5.2.4 ToString方法
    - 5.3 泛型数组列表
        - 5.3.1 访问数组列表元素
    - 5.4 对象包装器与自动打包
    - 5.5 参数数量可变的方法
    - 5.6 枚举类
    - 5.7 反射
- 附录1 C++注释
- 附录2 Java注释与警告

<!-- /MarkdownTOC -->


## 第1章 Java程序设计概述

简要地介绍一下Java语言的发展历史。

### 1.1 Java程序设计平台

Java并不只是一种语言，Java是一个完整的平台，有一个庞大的库，其中包含了很多可重用的代码和一个提供诸如安全性、跨操作系统的可一直性以及自动垃圾收集等服务的执行环境。

### 1.2 Java“白皮书”的关键术语

感兴趣的话可以参见[这里](http://java.sun.com/docs/white/langenv/)

**简单性**

人们希望构建一个无需社脑的专业训练就可以进行编程的系统，并且要符合当今的标准惯例。Java提出了C++中许多很少使用、难以理解、易混淆的特性。在目前看来，这些特性带来的麻烦远远多于其带来的好处。

`Java语法是C++语法的一个“纯净”版本`。没有头文件、指针运算、结构、联合、操作符重载、虚基类等等。

简单的另一个方面是小。Java的目标之一是支持开发能够在小型机器上独立运行的软件。

**面向对象**

面向对象设计是一种程序设计技术。它将重点放在数据(即对象)和对象的接口上。具体来说，就是关注的是要做出什么，而不是用什么做出来。在本质上，Java的面向对象能力与C++是一样的。

Java与C++的主要不同点在于`多继承`，在Java中，取而代之的是简单的接口概念，以及Java的`元类(metaclass)`模型。

**网络技能**

Java又一个拓展的例程库，用于处理像HTTP和FTP这类的TCP/IP协议。Java应用程序能够通过URL打开和访问网络上的对象，其边界程度就好像访问本地文件一样。

**健壮性**

Java的设计目标之一在于使得Java编写的程序具有多方面的可靠性。Java和C++的最大不同在于Java采用的指针模型可以消除重写内存和损坏数据的可能性。

Java编译器能够检测许多在其他语言中仅在运行时刻才能够检测出来的问题。

**安全性**

一开始Java就设计成能够防范各种袭击，其中包括

1. 运行时堆栈溢出。如，蠕虫等病毒常用的袭击手段。
2. 在子集的处理空间之外破坏内存
3. 未经授权读写文件。

**体系结构中立**

编译器生成一个体系结构中立的目标文件格式，这是一种编译过的代码，只要有Java运行时系统，就可以在许多处理器上运行。Java编译器通过生成与特定的计算机体系结构无关的字节码指令来实现这一特性。精心设计的字节码不仅可以很容易地在任何机器上解释执行，而且还可以迅速地翻译成本地机器的代码。

解释字节码肯定会比全速地运行机器指令慢很多，但是虚拟机有一个选项，可以将使用最贫乏的字节码序列翻译成机器码，这一过程被称为即时编译。这一策略已经证明十分有效。

**可移植性**

与C和C++不同，Java规范中没有“依赖具体实现”的地方，数据类型具有固定的大小，这消除了代码移植时令人头痛的主要问题。

**解释型**

Java解释器可已在任何移植了解释器的机器上执行Java字节码。由于链接是一个增值而简便的过程，所以开发过程也变得更加快捷

**高性能**

尽管对解释后的字节码性能已经比较满意，但在有些场合下却需要更加高效的性能。字节码可以(在运行时刻)快速地翻译成运行这个应用程序的特定CPU的机器码。

**多线程**

多线程可以带来更好的交互响应和实时行为。在不同的机器上，只是调用多线程的代码完全相同；Java把多线程的实现交给了底层的操作系统或线程库来完成。多线程编译的简单性是Java称为颇具魅力的服务器端开发语言的主要原因之一。

**动态性**

Java与C或C++相比更加具有动态性。它能够适应不断发展的环境。库中可以自由地添加新方法和实例变量，而对客户端却没有任何影响。在Java中找出运行时类型信息十分简单。

### 1.3 Java Applet与Internet

这里的想法很简单：用户从Internet下载Java字节码，并在子集的机器上运行。在网页中运行Java程序称为applet。为了使用applet，需要启用Java的Web浏览器执行字节码。由于Sun公司负责发放Java源代码的许可证，并坚持不允许对语言和基本类库的结构做出任何修改，因此，Java的applet应该可以运星在任何启用Java的浏览器上，并且无论何时访问包含applet的网页，都会得到程序的最终版本。

现在，当需要在浏览器中显示动态效果时，大多数网页都直接使用JavaScript或Flash。

### 1.4 Java发展简史

+ 1991年，由Patrick Naughton及其伙伴James Gosling带领的Sun公司的工程师小组想要设计一种小型的计算机语言，主要用于像有限电视转换盒这种设备。这种语言的关键是不能与任何特定的体系结构捆绑在一起，这个项目被命名为“Green”。
+ 代码短小、紧凑且与平台无关，这些要求促使开发团队联想起很早以前的一种模型，某些Pascal的实现曾经在早期的PC上尝试过这种模型。
+ 不过，Sun公司的人都具有UNIX的应用背景。因此，所开发的语言以C++为基础，而不是Pascal。Gosling把这种语言称为“Oak”。Sun公司的人后来发现Oak是一种已有的计算机语言的名字，于是将其改名为Java。
+ 1992年，Green项目发布了它的第一个产品，称之为“*7”，具有非常智能的远程控制，但是Sun公司对生产这个产品没有兴趣。
+ Green项目(这时换了一个新名字──“Fist Person”公司)整个1993年和1994年上半年都在苦苦寻求其技术的买家。但是，一个也没有。1994年First Person公司解散了。
+ 1994年中期，Java语言的开发者意识到它们能够建立一个最酷的浏览器。在1995年5月23日的SunWorld展示后，引发了人们延续至今的对Java的狂热追逐。
+ 1996年初，Sun发布了Java的第1个版本。Java1.1弥补了其中的大多部分明显的缺陷。
+ 1998年，Sun发布了Java1.2，后改名为“Java2标准版软件开发工具箱1.2版”。
+ 除了标准版之外，还有两个其他的版本，一个是用于手机等嵌入式设备的“微型版”，另一个是用于服务器端处理的“企业版”。
+ 标准版的1.3和1.4版本对最初的Java 2版本做出了某些改进，拓展了标准类库，提高系统性能。
+ 5.0版是自1.1版依赖第一个对Java语言做出重大改进的版本。
+ 版本6(没有后缀.0)与2006年末发布。这个版本没有对语言方面再进行改进，而是改进了其他性能，并增强了类库。

### 1.5 关于Java的常见误解

> Java是HTML的拓展。

Java是一种程序设计语言；HTML是一种描述网页结构的方式。

> 使用XML，就不需要Java。

Java是一种程序设计语言；XML是一种描述数据的方式。可以使用任何一种程序设计语言处理XML数据。

> Java是一种非常容易学习的程序设计语言。

像Java这种功能强大的语言大都不太容易学习。

>Java将成为适用于所有平台的通用性编程语言。

很多在桌面计算机上已经工作良好的应用程序，通常是用C或C++编写的，用Java重写一次似乎对于用户来说没有什么特别的好处。

> Java只不过是另外一种程序设计语言。

程序设计语言的成功更多地取决于其支撑系统的能力，而不是优美的语法。Java的成功源于其类库能够让人们轻松地完成原本有一定难度的事情

> 现在有了C#，Java过时了。

C#借鉴了Java许多好的思想，例如：清晰的语言结构、虚拟机和垃圾收集器。最重要的是安全性和平台无关性。但是从求职广告判定，Java仍然是大多数开发者选择的语言。

> Java有专利，应该避免使用。

Sun声称Java未来的版本将在General Public License下可用。Linux使用的是同一个开放源代码许可。开放源代码会使Java的生存期延长很多年。

> Java是解释型的，因此对于关键的应用程序速度太慢了。

Java所写的代码某些程度上其运行速度与C++相差无几。Java有一些C++没有的额外开销。但是，硬件的发展很快的。

> 所有的Java程序都是在网页中运行的。

所有的Java applet都在网页浏览器中运行的。然而，大多数Java程序是运行在Web浏览器之外的独立应用程序。

> Java程序是主要的安全风险。

相当可笑，不解释。

> JavaScript是Java的简易版。

JavaScript是一种在网页中使用的脚本语言。JavaScript的语言类似Java，除此之外，两者无任何关系。额，名字有点像。
更多可查阅[Java FAQ(Java Frequently Question)](http://www.apl.jhu.edu/~hall/java/FAQs-and-Tutorials.html)


## 第2章 Java程序设计环境

详情可参见各种搭建Java开发设计环境的教程，故不赘述。

## 第3章 Java基本的程序设计结构

### 3.1 一个简单的Java应用程序

```java
public class FirstSample{
    public static void main(String[] args){
        System.out.println(“Hello! I’m wdxtub”);
    }
}
```

这就是一个最简单的Java应用程序，但是所有的Java应用程序都具有这种结构。

Java对`大小写敏感`。关键字`public`称为`访问修饰符(access modifier)`，用于控制程序的其他部分对这段代码的访问级别。

`类`是构建所有Java应用程序和applet的构建块。Java应用程序中的全部内容都必须放置在类中。关键字class后面紧跟类名。Java中定义类名的规则很宽松。名字必须以`字母开头`，后面可以跟字母和数字的任意组合。长度基本上没有限制。但是不能使用Java的保留字。

源代码的文件名必须与公有类的名字相同，并用`.java`作为扩展名。

运行编译程序时，Java 虚拟机将从指定类中的`main`方法开始执行，并且`main`方法必须声明为`public`。


### 3.2 注释

三种方法：

1. `//` 单行的注释，内容从 // 开始到本行结尾
2. `/*...*/` 长篇的注释
3. `/**...*/` 用于自动生成文档

### 3.3 数据类型

Java是一种强类型语言。这就意味着必须为每一个变量声明一种类型。Java中一共有8种基本类型(primitive type)。其中4种整型，2种浮点类型，1种char型，1种boolean类型。

#### 3.3.1 整型

表示没有小数部分的数值，可以是复数。分别为`int(4字节)`，`short(2字节)`，`long(8字节)`，`byte(1字节)`。

由于Java程序必须保证在所有机器都能得到相同的运行结果，所以每一种数据类型的取值范围必须固定。

#### 3.3.2 浮点类型

浮点类型用于表示有小数部分的数值。分别是`float(4字节，有效位数6～7位)`，`double(8字节，有效位数15位)`。

`double`表示这种类型的数值精度是`float`的两倍。绝大部分程序都采用`double`类型。`float`类型的数值有一个后缀F，没有`后缀F`的浮点数值默认为`double`类型。

三个特殊的浮点数值：

+ 正无穷大
+ 负无穷大
+ NaN(不是一个数字，Not a Number)

#### 3.3.3 char类型

`char`类型用于表示单个字符。通常用来表示字符常量。

**我们强烈建议不要在程序中使用char类型，除非确实需要对UTF-16代码单元进行操作。最好将需要处理的字符串用抽象数据类型表示。**

#### 3.3.4 boolean类型

`boolean(布尔)`类型有两个值：`false`和`true`，用来判定逻辑条件。整型和布尔值之间不能进行相互转换。

### 3.4 变量

每一个变量属于一种类型(type)。声明变量时，变量所属的类型位于变量名之前，每个声明以分号结束。

可以在一行中声明多个变量，不过不提倡使用这种风格。逐一声明每一个变量可以提高程序的可读性。

#### 3.4.1 变量初始化

声明一个变量之后，必须用赋值语句对变量进行显式的初始化，千万不要使用未被初始化的变量。可以将声明放在代码中的任何地方，变量的声明应尽可能地靠近变量第一次使用的地方。

#### 3.4.2 常量

利用关键字final声明常量，表示这个变量只能被赋值一次。一旦被赋值后就不能再更改了。习惯上，常量名使用大写。
若希望某个常量可以在一个类中的多个方法中使用，通常将这些常量称为类常量，使用static final设置。

类常量的定义位于main方法的外部，所以在同一个类的其他方法中也可以使用这个常量。

### 3.5 运算符

Java程序设计语言承认了最优性能与理想结果之间存在的冲突，并给予了改进。在默认情况下，虚拟机设计者允许中间结果采用拓展的精度。但对于strictfp关键字标记的方法必须使用严格的浮点计算来产生理想的结果。

#### 3.5.1 自增运算符与自减运算符

前缀方式`先进行加一或减一`的运算，后缀方式则使用变量原来的值。

建议不要在其他表达式的内部使用++，使人迷惑，产生bug。

#### 3.5.2 关系运算符与boolean运算符

其中`==`，`!=`，`<`，`>`，`<=`，`>=`，`||`，`&&`均与C++一致。

#### 3.5.3 位运算符

+ &(与)，|(或)，^(异或)，-(非)
+ `>>`和`<<`运算符进行右移或左移操作，屏蔽某些位。
+ `>>>`运算符用0填充高位；`>>`运算符用符号填充高位，没有`<<<`运算符。

#### 3.5.4 科学函数与常量

在Math类中，包含各种的数学函数。若得到一个完全可预测的结果比运行速度更重要的话，就应该使用StrictMath类。

#### 3.5.5 数值类型之间的转换

整型转换为float或double型很有可能损失精度。

#### 3.5.6 强制类型转换

在圆括号中给出想要转换的目标类型，后面紧跟待转换的变量名，如

    double x = 9.998;
    int nx = (int)x;

若想进行四舍五入计算，使用Math.round方法。

#### 3.5.7 括号与运算符级别

与正常情况下一致。少数结合性是从右向左的。

#### 3.5.8 枚举类型

枚举类型包括有限个命名的值。

如 `enum Size{SMALL,MEDIUM,LARGE,EXTRA_LARGE}`。

### 3.6 字符串

Java字符串就是Unicode字符序列。

#### 3.6.1 子串

String类的substring方法可以从一个较大的字符串提取一个子串，容易计算子串长度，语句：`s.substring(a,b)`，长度即为`b-a`。

#### 3.6.2 拼接

允许使用`+`号连接(拼接)两个字符串。

#### 3.6.3 不可变字符串

`String`类没有提供用于修改字符串的方法，所以在Java文档中将String类对象称为`不可变字符串`。

不可变字符又一个优点：编译器可以让`字符串共享`。Java的设计者认为共享带来的高效率远远胜过于提取。

#### 3.6.4 检测字符串是否相等

使用`equals`方法检测两个字符串是否相等。`s.equals(t)`，若 `s` 与 `t` 相等，则返回`true`，否则返回`false`。`s` 和 `t` 可以是字符串变量也可以是字符串常量，如`”Hello”.equals(greeting)`。

如果向不区分大小写，使用`equalsIgnoreCase`方法。

一定不能使用 `==` 运算符检测两个字符串是否相等！这个运算符只能够确定两个字符是否放置在同一个位置上。

#### 3.6.5 代码点与代码单元

大多数的常用Unicode字符使用一个代码单元就可以表示，而辅助字符则需要一对代码来表示。

`s.charAt(n)`将返回位置 `n` 的代码单元，`n`介于`0～s.length()-1`之间。对于那些一对代码单元表示的字符，就会出现问题。而`codePointAt`可以解决这个问题。

#### 3.6.6 字符串API

Java中的String类包含了50多个方法并且绝大多数都很有用。

**java.lang.string**

+ `char charAt( int index )`
    + 返回给定位置的代码单元。除非对底层的代码单元感兴趣，否则不需要调用这个方法。
+ `int codePointAt( int index )`
    + 返回从给定位置开始或结束的代码点。
+ `int offsetByCodePoints( int startIndex, int cpCount )`
    + 返回从 startIndex 代码点开始，位移 cpCount 后的代码点索引。
+ `int compareTo( String other )`
    + 按照字典顺序，如果字符串位于other之前，返回一个负数；位于other之后，返回一个正数；如果两个字符串相等，返回0。
+ `boolean endsWith( String suffix )`
    + 如果字符串以suffix结尾，返回true。
+ `boolean equals( Object other )`
    + 如果字符串以other相等，返回true。
+ `boolean equalsIgnoreCase( String other )`
    + 如果字符串与other相等(忽略大小写)，返回true。
+ `int indexOf( String str )`
+ `int indexOf( String, int fromIndex )`
+ `int indexOf( int cp )`
+ `int indexOf( int cp, int fromIndex )`
    + 返回与字符串str或代码点cp匹配的第一个子串的开始位置。这个位置从索引0或fromIndex开始计算。如果在原始串中不存在str，返回-1。
+ `int lastIndexOf( String str )`
+ `int lastIndexOf( String str, int  fromIndex )`
+ `int lastIndexOf( int cp )`
+ `int lastIndexOf( int cp, int fromIndex )`
    + 返回与字符串str或代码点cp匹配的最后一个子串的开始位置。这个位置从原始串尾端或fromIndex开始计算。
+ `int length()`
    + 返回字符串的长度。
+ `int codePointCount( int startIndex, int endIndex)`
    + 返回startIndex和endIndex-1之间的代码点数量。没有配成对的代用字符将计入代码点。
+ `String replace(CharSequence oldString, CharSequence newString)`
    + 返回一个新字符串。这个字符串用newString代替原始字符串中的所有oldString。可以用String或StringBuilder对象作为CharSequence参数。
+ `boolean startsWith( String prefix )`
    + 如果字符串以prefix字符串开始，返回true。
+ `String substring( int beginIndex )`
+ `String substring( int beginIndex, int  endIndex )`
    + 返回一个新字符串。这个字符串包含原始字符串中从beginIndex到串尾或endIndex-1的所有代码点。
+ `String toLowerCase()`
    + 返回一个新字符串，这个字符串将原始字符串中的所有大写字母改成了小写字母。
+ `String toUpperCase()`
    + 返回一个新字符串，这个字符串将原始字符串中的所有小写字母改成了大写字母。
+ `String trim()`
    + 返回一个新字符串。这个字符串将山除了原始字符串头部和尾部的空格。

#### 3.6.7 阅读联机API文档

学会使用在线API文档十分重要，从中可以查阅到标准库类中的所有类和方法。

#### 3.6.8 构建字符串

如果需要用许多小段的字符串构建一个字符串，那么应该按照下列步骤进行。首先，构建一个空的字符串构建器：

    StringBuilder builder = new StringBuilder();

当每次需要添加一部分内容时，就调用append方法。

    builder.append(ch); // appends a single character
    builder.append(str);    // appends a string

**java.lang.StringBuilder**

+ `StringBuilder()`
    + 构造一个空的字符串构建器。
+ `int length()`
    + 返回构建器或缓冲器中的代码单元数量。
+ `StringBuilder append( String str )`
    + 追加一个字符串并返回this。
+ `StringBuilder append( char c )`
    + 追加一个代码单元并返回this。
+ `StringBuilder appendCodePoint( int cp )`
    + 追加一个代码点，并将其转换为一个或两个代码单元并返回this。
+ `void setCharAt( int i,char c )`
    + 将第 i 个代码单元设置为 c。
+ `StringBuilder insert( int offset,String str )`
    + 在offset位置插入一个字符串并返回this。
+ `StringBuilder insert( int offset,Char c )`
    + 在offset位置插入一个代码单元并返回this。
+ `StringBuilder delete( int startIndex,int endIndex )`
    + 删除偏移量从startIndex到-endIndex-1的代码单元并返回this。
+ `String toString()`
    + 返回一个与构建器或缓冲器内容相同的字符串。

### 3.7 输入输出

#### 3.7.1 读取输入

要想通过控制台进行输入，首先需要构造一个`Scanner`对象，并与“标准输入流”`System.in`关联。

    Scanner in = new Scanner(System.in);

现在就可以使用`Scanner`类的各种方法实现输入操作。例如可以用`nextLine`方法将输入一行(包括输入行中有空格的情况)，若想读取一个单词(以空格作为分隔符)，就调用next方法；想读取一个整数，就调用`nextInt`方法；想读取一个浮点数，就调用`nextDouble`方法。

    String name = in.nextLine();
    String firstName = in.next();
    int age = in.nextInt();
    double salary = in.nextDouble();

最后在程序最开始加上 `import java.util.*;`

当使用的类不是定义在基本`java.lang`包中时，一定要使用`import`指示将相应的包加载进来。

**java.util.Scanner**

+ `Scanner( InputStream in)`
    + 用给定的输入流创建一个Scanner对象。
+ `String nextLine()`
    + 读取输入的下一行内容。
+ `String next()`
    + 读取输入的下一个单词(以空格作为分隔符)
+ `int nextInt()`
+ `double nextDouble()`
    + 读取并转换下一个表示整数或浮点数的字符序列。
+ `boolean hasNext()`
    + 检测输入中是否还有其他单词。
+ `boolean hasNextInt()`
+ `boolean hasNextDouble()`
    + 检测是否还有表示整数或浮点数的下一个字符序列。
+ `Scanner( File f )`
    + 构造一个从给定文件读取数据的Scanner。
+ `Scanner( String data)`
    + 构造一个从给定字符串读取数据的Scanner。

**java.util.System**

+ `static Console console()`
    + 如果有可能进行交互操作，就通过控制台窗口为交互的用户返回一个Console对象，否则返回null。

**java.io.Console**

+ `static char[] readPassword( String prompt, Object...args )`
+ `static String readLine( String prompt, Object...args)`
    + 显示字符串prompt并且读取用户输入，直到输入行结束。args参数可以用来提供输入格式。

#### 3.7.2 格式化输出

沿用了C语言库函数中的printf方法，另外还可以给出控制格式化输出的各种标志

可以采用一个格式化的字符串指出要被格式化的参数索引。紧跟在%后面，并以$终止。还可以选择使用<标志。它指示前面格式说明中的参数将再次使用。

#### 3.7.3 文件输入与输出

要想对文件进行读取，就需要一个用`File`对象构造一个`Scanner`对象，例如：`Scanner in = new Scanner(new File(“myfile.txt”));`

如果文件名中包含反斜杠符号，就要记住在每个反斜杠之前再价一个额外的反斜杠：`“c:\\mydirectory\\myfile.txt”`。

要想写入文件，就需要构造一个`PrintWriter`对象。在构造器中，主需要提供文件名：`PrintWriter out = new PrintWriter(“myfile.txt”);`

可以向输出到`System.out`一样使用`print`、`pinrtln`以及`printf`命令。

**java.io.PrintWriter**

`PrintWriter( File f)`
构造一个将数据写入给定文件的PrintWriter。
`PrintWriter( String fileName )`
构造一个将数据写入文件的PrintWriter。文件名由参数指定。

**java.io.File**

`File( String fileName )`

用给定的文件名，构造一个描述文件的File对象。注意这个文件当前不必存在。

### 3.8 控制流程

Java使用条件语句和循环结构确定控制流程。

### 3.8.1 块作用域

块确定了变量的作用域。一个块可以嵌套在另一个块中。不能在嵌套的两个块中声明同名的变量。

#### 3.8.2 条件语句

#### 3.8.3 循环

以上两章与C++无异，故略去。

#### 3.8.4 确定循环

尽管Java允许在for循环的各个部分放置任何表达式，但有一条不成文的规则：for语句的三个部分应该对同一个计数器变量进行初始化、检测和更新。

#### 3.8.5 多重选择：switch语句

有可能出发多个`case`分支。如果在`case`分支语句的末尾没有`break`语句，那么就会接着执行下一个`case`分支语句。这种情况相当危险，常常会引发错误。为此，尽量不要使用`switch`语句。

当在`switch`语句中使用枚举常量时，不必在每个标签中指明枚举名，可以由`switch`的表达式确定。例如：

    Size sz = {SMALL,LARGE,...}
    switch (sz){
        case SMALL: // no need to use Size.SMALL
        ...
        break;
    }

#### 3.8.6 中断控制流程语句

无限制地使用goto语句确实是导致错误的根源，但偶尔地使用goto跳出循环是有益处的，Java中增加了一条带标签的break以支持这种跳出。

请注意，标签必须放在希望跳出的最外层循环之前，必须紧跟一个冒号。如下所示：

    int n;
    read_data:
    while(...){ // this loop statement is tagged with the label
        ...
        for(...){ // this inner loop is not labeled
            if(...) break read_data; // break out of read_data loop
        }
    }
    // this statement is executed immediately after the labeled break

    if(....){.....}

即可以直接跳出所标记的循环，继续执行下面的语句。

带标签的continue将跳到与标签匹配的循环首部。

### 3.9 大数值

如果基本的整数和浮点数精度不能够满足需求，那么可以使用`java.math`包中的两个很有用的类：`BigInterger`(任意精度的整数运算)和`BigDecimal`(任意精度的浮点数运算)。

使用静态的`valueOf`方法可以将普通的数值转换为大数值：

    BigInterger a = BigInteger.valueOf(100);

但是不能使用算数运算符，有专门的运算方法。

**java.math.BigInterger**

+ `BigInteger add( BigInteger other )`
+ `BigInteger subtract( BigInteger other)`
+ `BigInteger multiply( BigInteger other)`
+ `BigInteger divide( BigInteger other)`
+ `BigInteger mod( BigInteger other)`
    + 返回这个大整数和另一个大整数other的和、差、积、商和余数。
+ `int compareTo( BigInteger other )`
    + 如果这个大整数和另一个大整数other相等，返回0；如果这个大整数小于另一个大整数，返回负数；大于的话，返回正数。
+ `static BigInteger valueOf(long x)`
    + 返回值等于x的大整数。

**java.math.BiDecimal**

+ `BigDecimal add( BigDecimal other )`
+ `BigDecimal subtract( BigDecimal other)`
+ `BigDecimal multiply( BigDecimal other)`
+ `BigDecimal divide( BigDecimal other, RoundingMode mode)`
    + 返回这个大实数和另一个大实数other的和、差、积、商和余数。要想计算商，必须给出舍入方式(rounding mode)。RoundingMode.HALF_UP是四舍五入方式，其他的舍入方式参见API文档。
+ `int compareTo( BigDecimal other )`
    + 如果这个大实数和另一个大实数other相等，返回0；如果这个大实数小于另一个大实数，返回负数；大于的话，返回正数。
+ `static BigDecimal valueOf( long x)`
+ `static BigDecimal valueOf( long x, int scale)`
    + 返回值等于x或x/10scale的一个大实数。

### 3.10 数组

应该使用`new`运算符创建数组：`int[] a = new int[100];`

要想获得数组中的元素个数，可以使用`array.length`。

一旦创建了数组，就不能再改变它的大小。如果经常需要在运行过程中拓展数组的大小，就应该使用另一种数据结构─数组列表(array list)。

#### 3.10.1 For each循环

Java SE 5.0增加了一种功能很强的循环结构，可以用来一次处理数组中的每个元素(其他类型的元素集合亦可)而不必为指定下标值而分心。

语句格式为：`for( variable : collection ) statement`    例如：

    for( int element : a )
        System.out.println( element );

就可以打印数组a的每一个元素。

有个更加简单的方式打印数组中的所有值，即利用Arrays类的toString方法。调用`Arrays.toString(a)`，返回一个包含数组元素的字符串，这些元素被放置在括号内，并用逗号分隔。

#### 3.10.2 数组初始化以及匿名数组

提供一种创建数组对象并同时赋予初始值的简化书写形式，如：

    int[] smallPrimes = { 2, 3, 5, 6};

使用这种语句时就不用调用`new`。

还可以初始化一个匿名的数组：`new int[]{ 11, 12, 14, 15};` 这种表示法将创建一个新数组并利用括号中提供的值进行初始化，数组的大小就是初始值的个数。使用这种语法形式可已在不创建新变量的情况下重新初始化一个数组。例如：`smallPrimes = new int[]{ 11, 12, 14, 15};`

#### 3.10.3 数组拷贝

允许将一个数组变量拷贝给另一个数组变量。这是，两个变量就引用同一个数组：`int[] luckyNumbers = smallPrimes;`

如果希望将一个数组的所有值拷贝到一个新的数组中，就要使用`Arrays`类的`copyOf`方法：`int[] copiedLuckyNumbers = Arrays.copyOf( luckyNumbers, luckyNumbers.length );`

第二个参数是新数组的长度。这个方法通常用来增加数组的大小：`luckyNumbers = Arrays.copyOf( luckyNumbers, 2 * luckyNumbers.length);`

如果数组元素是数值型，那么多余的元素将被赋值为`0`；如果数组元素是是布尔型，则将赋值为`false`。如果长度小于原始数组的长度，则只拷贝最前面的数据元素。

在Java SE 6之前，用`System`类的`arraycopy`方法将一个数组的元素拷贝到另一个数组中。调用这个方法的格式为：

    System.arraycopy( from, fromIndex, to, toIndex, count);

数组`to`必须有足够的空间存放拷贝的元素。意思为，从`from`数组的下标为`fromIndex`元素开始，拷贝`count`个元素到`to`数组，从`to`数组的下标为`toIndex`的元素开始变成被拷贝过来的元素。

#### 3.10.4 命令行参数

`main`方法接受命令行参数。

#### 3.10.5 数组排序

可以使用Arrays类中的sort方法对数值型数组进行排序：

    int[] a = new int[1000];
    ...

`Arrays.sort(a);` 这个方法使用了优化的快速排序算法，效率是比较高的。

**java.util.Arrays**

+ `static String toString( type[] a )`
    + 返回包含a中数据元素的字符串，这些数据元素被放在括号内，并用逗号分隔。
+ `static type copyOf( type[] a, int length )`
+ `static type copyOf( type[] a, int start, int end )`
    + 返回与a类型相同的一个数组，其长度为length或者 end-start，数组元素为a的值。
+ `static void sort( type[] a )`
    + 采用优化的快速排序算法对数组进行排序。
+ `static int binarySearch( type[] a, type v)`
+ `static int binarySearch( type[] a, int start, int end, type v )`
    + 采用二分搜索法查找值v。如果查找成功，则返回相应的下标值；否则，返回一个负数值r。-r-1是为保持a有序v应插入的位置。
+ `static void fill( type[] a, type v )`
    + 将数组的所有数据元素值设置为v。
+ `static boolean equals( type[] a, type[] b)`
    + 如果两个数组大小相同，并且下标相同的元素都对应相等，返回true。
+ `static int hashCode( type[] a )`
    + 计算数组a的散列码。可以是int、long、short、char、byte、boolean、float或double的数组。

**java.lang.System**

+ `static void arraycopy( Object from, int fromIndex, Object to, int toIndex, int count )`
    + 将第一个数组中的元素拷贝到第二个数组中。

#### 3.10.6 多维数组

使用`new`进行初始化：`balances = new double[NSIZE][MSIZE];`

或者是：`int[][] magicSquare = {{16, 3, 2, 13},{5, 10, 11,8}};`

一旦数组被初始化，就可以利用两个方括号访问每个元素。

`for each`循环语句不能自动处理二维数组的每一个元素。它是按照行，也就是一维数组处理的。要想访问二维数组a的所有元素，需要使用两个嵌套的循环：

    for( double[] row: a )
        for( double value : row )
            do something with value

想要快速打印一个二维数组的数据元素列表，可以调用：`System.out.println( Arrays.deepToString(a));`

#### 3.10.7 不规则数组

可以方便地构造一个“不规则”数组。

## 第4章 对象与类

### 4.1 面向对象程序设计概述

数据被放在第一位，然后再考虑操作数据的算法。

#### 4.1.1 类

`类(class)`是构造对象的模板或蓝图。由类`构造(construct)`对象的过程称为创建类的`实例(instance)`。

`封装(encapsulation，有时称为数据隐藏)`是与对象功能有关的一个重要概念。对象中的数据称为`实例域(instance fields)`，操纵数据的过程称为`方法(method)`。对于每个特定的类实例(对象)都有一组特定的实例域值。这些值的集合就是这个对象的当前`状态(state)`。无论何时，只要向对象发送一个消息，它的状态就有可能发生改变。

封装的关键在于绝对不能让类中的方法直接地访问其他类的实例域。程序仅通过对象的方法与对象数据进行交互。

在对于一个已有的类扩展时，这个扩展后的新类具有所拓展的类的全部属性和方法。在新类中，只需要提供哪些仅适用于这个类的新方法和数据域就可以了。

#### 4.1.2 对象

要想使用OOP，一定要清楚对象的三个主要特性：

1. 对象的行为(behavior)──可以对对象施加哪些操作，或可以对对象施加哪些方法？
2. 对象的状态(state)──当施加那些方法时，对象如何响应？
3. 对象标识(identity)──如何辨别具有相同行为与状态的不同对象？

此外，每个对象都保存着描述当前特征的信息。这就是对象的状态。对象的状态可能会随着时间而发生改变，但这种改变不会是自发的。

对象的状态并不能完全描述一个对象。每个对象都有一个唯一的身份(identity)。需要注意，作为一个类的实例，每个对象的标识永远是不同的，状态常常也存在着差异。对象的这些关键特性在彼此之间相互影响着。

#### 4.1.3 识别类

识别类的简单规则是在分析问题的过程中寻找名词，而方法对应动词。在创建类的时候，哪些名词和动词是重要的完全取决于个人的开发经验。

#### 4.1.4 类之间的关系

在类之间最常见的关系有

+ 依赖(“uses-a”)
+ 聚合(“has-a”)
+ 继承(“is-a”)

`依赖(dependence)`，是一种最明显的、最常见的关系。如果一个类的方法操纵另一个类的对象，我们就说一个类依赖于另一个类。应该尽可能将相互依赖的类减至最少，即类之间的耦合度最小。

`聚合(aggregation)`，是一种具体且易于理解的关系。集合意味着类A的对象包含类B的对象。

`继承(inheritance)`，是一种表示特殊与一般的关系。一般而言，如果类A扩展类B，类A不但包含从类B继承的方法，还会拥有一些额外的功能。

#### 4.2 使用现有类

要想使用对象，就必须首先构造对象，并指定其初状态。然后，对对象施加方法。在Java程序设计语言中，使用`构造器(constructor)`构造新实例。

构造器的名字应与类名相同，并且使用`new`操作符进行构造；也可以将这个对象传递给一个方法；另外`Date`类中有一个`toString`方法，返回日期的字符串描述，如下

    new Date(); // 被初始化为当前的日期和时间
    System.out.println(new Date());
    String s = new Date().toString();

如果希望构造的对象可以多次使用，就要把对象放在一个变量中：

    Date birthday = new Date();

可以让一个变量引用一个已存在的变量：`Date deadline = birthday; `则这两个变量引用同一个对象。

一个对象变量并没有实际包含一个对象，而仅仅引用一个对象。在Java中，任何对象变量的值都是对存储在另外一个地方的一个对象的引用。new操作符的返回值也是一个引用。可以显式地将对象变量设置为`null`，表明这个对象变量目前没有任何引用对象：`deadline = null;`变量不会自动初始化为`null`，而必须通过调用`new`或将它们设置为`null`进行初始化。

#### 4.2.2 Java类库中的GregorianCalendar类

Date类只提供了少量的方法用来比较两个时间点。例如`before`和`after`方法分别表示一个时间点是否早于另一个时间点，或者晚于另一个时间点。

    if( today.before(birthday) )
        System.out.println(“Still time to shop for a gift.”);

`GregorianCalendar`类所包含的方法比`Date`类多得多，并且封装了实例域。

#### 4.2.3 更改器方法与访问器方法

对实例域作出修改的方法被称为`更改器方法(mutator method)`，仅访问实例域而不进行修改的方法称为`访问器方法(accessor method)`。

通常的习惯是在访问器方法前面加上前缀`get`，在更改器方法前面加上前缀`set`。

**java.util.GregorianCalendar**

+ `GregorianCalendar()`
    + 构造一个日历对象，用来表示默认地区、默认时区的当前时间。
+ `GregorianCalendar( int year, int month, int day )`
+ `GregorianCalendar( int year, int month, int day, int hour, int minutes, int seconds )`
    + 用给定的日期和时间构造一个Gregorian日历对象。
+ `int get( int field )`
    + 返回给定区域的值
+ `void set( int field, int value )`
+ `void set( int year, int month, int day )`
+ `void set( int year, int month, int day, int hour, int minutes, int seconds )`
    + 将日期域和时间域设置为新值。
+ `void add( int field, int amount)`
    + 对给定的时间域增加指定数量的时间。
+ `int getFistDayOfWeek()`
    + 获得当前用户所在地区，一个星期中的第一天。
+ `void setTime( Date time )`
    + 将日历设置为指定的时间点。
+ `Date getTime()`
    + 获得这个日历对象当前值所表达的时间点

**java.text.DateFormatSymbols**

+ `String[] getShortWeekdays()`
+ `String[] getShortMonths()`
+ `String[] getWeekdays()`
+ `String[] getMonths()`
    + 获得当前地区的星期几或月份的名称。利用Calendar的星期和月份常量作为数组索引值。

### 4.3 用户自定义类

复杂应用程序需要各种`主力类(workhorse class)`。通常这些类没有main方法，而却有自定义的实例域和实例方法。要想创建一个完整的程序，应该将若干类组合在一起，其中只有一个类有main方法。

#### 4.3.1 一个最简单的类

在Java的类中最简单的类定义形式为：

    class ClassName{
        constructor1
        constructor2
        …
        Method1
        Method2
        …
        Field1
        Field2
    …
    }

文件名必须与`public`类的名字相匹配。在一个文件中，只能有一个公有类，但可以有任意数目的非公有类。

#### 4.3.2 多个源文件的使用

如果习惯于将每一个类存在一个单独的源文件中，将可以有两种编译源程序的方法。

一种是使用通配符调用编译器，即`*`代表不定的字符串。另一种是只对含有公有类的文件进行`javac`操作，如果在这里使用了某个类，那么会自动搜索这个类的源文件，进行编译。

可以认为Java编译器内置了`make`功能。

#### 4.3.3 解析类

关键字`public`意味着任何类的任何方法都可以调用这些方法。关键字`private`确保只有该类自身的方法能够访问这些实例域，而其他类的方法不能够读取这些域。

#### 4.3.4 从构造器开始

构造器与类同名，将实例域初始化为所希望的状态。构造器总是伴随着new操作符的执行被调用，而不能对一个已经存在的对象调用构造器来达到重新设置实例域的目的。

#### 4.3.5 隐式参数与显式参数

方法用于操作对象以及存取它们的实例域。例如，方法：

    public void raiseSalary( double byPercent ){
        double raise = salary * byPercent / 100;
        salary += raise;
    }

将调用这个方法的对象的`salary`实例域设置为新值，看看下面这个调用：`number007.raiseSalary(5);` 它的结果将`number007.salary`域的值增加5%。`raiseSalary`方法有两个参数。第一个参数被称为`隐式(implicit)`参数，是出现在方法名前的类对象。第二个参数位于方法名后面括号中的数值，这是一个`显式(explicit)`参数。
在每个方法中，关键字`this`表示隐式参数。如果需要的话，可以用下列方式编写`raiseSalary`方法：

    public void raiseSalary( double by Percent ){
        double raise = this.salary * byPercent / 100;
        this.salary += raise;
    }

有些程序员更偏爱这样的风格，因为这样可以将实例域与局部变量明显区分开来。

#### 4.3.6 封装的优点

封装应提供下面三项内容：

1. 一个私有的数据域
2. 一个公有的域访问器
3. 一个公有的域更改器方法

这样做有如下的好处：

+ 可以改变内部实现，除了该类的方法之外，不会影响其他代码。
+ 更改器方法可以执行错误检查，然而直接对域进行赋值将不会进行这些处理。

#### 4.3.7 基于类的访问权限

一个方法可以访问所属类的所有对象的私有数据，而不仅限于访问隐式参数的私有特性。C++也有同样的原则。

#### 4.3.8 私有方法

尽管绝大多数方法都被设计为公有的，但在某些特殊情况下，也可能设计为私有的。

#### 4.3.9 Final实例域

可以将实例域定义为`final`。构建对象时必须初始化这样的域。也就是说，必须确保在每一个构造器执行之后，这个域的值被设置，并且在后面的操作中，不能够再对它进行修改。

`final`修饰符大都应用于`基本数据(primitive)`类型域，或`不可变类(immutable)`的域。对于可变的类，使用`final`修饰符可能会造成混乱。

### 4.4 静态域与静态方法

#### 4.4.1 静态域

如果将域定义为`static`，每个类中只有一个这样的域。它属于类，而不属于任何独立的对象。

#### 4.4.2 静态常量

静态变量使用得比较少，但静态常量却使用得比较多。例如，在`Math`类中定义一个静态常量：`public static final double PI = 3.1415926;`在程序中，可以用`Math.PI`的形式获得这个常量。

另一个多次使用的静态常量是`System.out`。

#### 4.4.3 静态方法

静态方法是一种不能向对象实施操作的方法。例如，Math类的pow方法就是一个静态方法。表达式`Math.pow(x,a);`计算`X^a`。在运算时，不使用任何`Math`的对象，即没有隐式的参数。因为静态方法不能操作对象，所以不能在静态方法中访问实例域。但是，静态方法可以访问自身类中的静态域。

#### 4.4.4 Factory方法

静态方法的一种常见用途。相当于创建实例对象的new。即把创建对象的过程抽象封装出来，可以创建不同名字和返回类型的对象，并且使程序的扩展性和安全性更强。

#### 4.4.5 Main方法

`main`方法部队任何对象进行操作。事实上，在启动程序时还没有任何一个对象。静态的main方法将执行并创建程序所需要的对象。

### 4.5 方法参数

Java程序设计语言总是采用值调用。也就是说，方法得到的是所有参数值的一个拷贝，特别是，方法不能修改传递给它的任何参数变量的内容。

把对象引用作为参数可以改变对象参数状态，因为方法得到的是对象引用的拷贝，对象引用和它的拷贝引用的是同一个对象，所以在对其拷贝进行了更改之后，原来的对象引用也会发生变化。

Java程序设计语言对对象采用的不是引用调用，实际上，对象引用进行的是值传递，传递的值是一个拷贝的对象引用并且和原来的对象引用指向的是同一个对象，也因为如此，对这个拷贝的对象引用进行修改，也会对原来的对象产生影响。

### 4.6 对象构造

#### 4.6.1 重载

如果多个方法有相同的名字、不同的参数，便产生了重载。编译器通过用各个方法给出的参数类型与特定方法调用所使用的值类型进行匹配来判断选择对应的方法。如果编译器找不到匹配的参数，或者找出多个可能的匹配，就会产生编译时错误(此过程称为重载解析(overloading resolution))。

#### 4.6.2 默认域初始化

如果在构造器中没有显式地给域赋予初值，那么就会被自动地赋为默认值：数值为0、布尔值为false、对象引用为null。这是很不好的习惯。

#### 4.6.3 默认构造器

如果在编写一个类时没有编写构造器，那么系统就会提供一个默认构造器。这个默认构造器将所有的实例域设置为默认值。

如果类中提供了至少一个构造器，但是没有提供默认的构造器，则在构造对象时如果没有提供构造函数参数就会被视为不合法。

#### 4.6.4 显式域初始化

由于类的构造器方法可以重载，所以可以采用多种形式设置类的实例域的初始状态。确保不管怎样调用构造器，每个实例域都可以被设置为一个有意义的初值。这是一种很好的设计习惯。

可以在类定义中，直接将一个值赋给任何域。当一个类的所有构造器都希望把相同的值赋给某个特定的实例域时，这种方式特别有用。

初始值不一定是常量。可以调用方法对域进行初始化。

#### 4.6.5 参数名

编写很小的构造器时，常常用单个字符命名：

    public Employee( String n, double s){
        name = n;
        salary = s;
    }

这样的话，就只有阅读代码才能了解参数n和s的含义，所以可以用aName和aSalary来代替，这样就可以一眼看出参数的含义。

还有一种常用的技巧，原理如下：参数变量用同样的名字将实例域屏蔽起来，再利用this隐式参数(即被构造的对象)访问实例域：

    public Employee( String name, double salary){
        this.name = name;
        this.salary = salary;
    }

#### 4.6.6 调用另一个构造器

关键字`this`引用方法的隐式参数。然而这个关键字还有另外一个含义。

如果构造器的第一个语句形如this(...)，这个构造器将调用同一个类的另一个构造器，例子如下：

    public Employee(double s){
        // calls Employee( String, double )
        this( “Employee #” + nextId, s);
        nextId++;
    }

当调用new Employee(6000)时，会调用Employee(String,double)构造器。采用这种方式使用this关键字非常有用，这样对公共的构造器代码部分只编写一次即可。

#### 4.6.7 初始化块

除了在构造器中设置值和在声明中赋值，Java还有第三种机制，称为`初始化块(initialization block)`。在一个类的声明中可以包含多个代码块。只要构造类的对象，这些块就会被执行。例如：

    class Employee{
        public Employee( String n, double s ){
            name = n;
            salary = s;
        }

        public Employee(){
            name = “”;
            salary = 0;
        }
        ........
        private static int nextId;
        private int id;
        private String name;
        private double salary;
        ........
        // object initialization block
        {
            id = nextId;
            nextId++;
        }
    }

在这个例子中，无论使用哪个构造器构造对象，id域都在对象初始化块(最后的一段)中被初始化。首先运行初始化块，然后才运行构造器的主体部分。这种机制不是必须的，也不常见。建议将初始化块放在域定义之后。

**java.util.Random**

+ `Random()`
    + 构造一个新的随机数生成器。
+ `int nextInt( int n )`
    + 返回一个0~n-1之间的随机数。

#### 4.6.8 对象析构与finalize方法

有些面向对象的程序设计语言，特别是C++，有显式的析构器方法，其中反之一些当对象不在使用时需要执行的清理代码。在析构器中，最常见的操作是回收分配格对象的存储空间。由于Java有自动的垃圾回收器，不需要人工回收内存，所以Java不支持析构器。

当然，某些对象使用了内存之外的其他资源，例如，文件或使用了系统资源的另一个句柄。在这种情况下，当资源不再需要时，将其回收和再利用将显得十分重要。

可以为任何一个类添加finalize方法。finalize方法将在垃圾回收器清除对象之前调用。在实际应用中，不要依赖于使用finalize方法回收任何短缺的资源，这是因为很难知道这个方法什么时候才能够调用。

如果某个资源需要在使用后立即被关闭，那么就需要人工来管理。可以应用一个类似`dispose`或`close`的方法完成相应的清理操作。如果一个类使用了这样的方法，使用完毕一定要记得调用它。

### 4.7 包

Java允许使用包(package)将类组织起来。借助于包可以方便地组织自己的代码，并将自己的代码与别人提供的代码库分开管理。

标准的Java类库分布在多个包中，包括`java.lang`、`java.util`、`java.net`等。标准的Java包具有一个层次结构，所有标准的Java包都在java和javax包层次中。

使用包的主要原因是确保类名的唯一性。Sun公司建议将公司的因特网域名以逆序的形式作为包名，并且不同的项目使用不同的子包。若域名为www.wdx.cn，则包的名字就叫做 cn.wdx。

从编译器的角度来看，嵌套的包之间没有任何关系，每一个都拥有独立的类集合。

#### 4.7.1 类的导入

一个类可以使用所属包中的所有类，以及其他包中的公有类(public class)。可以使用两种方式访问包中的公有类。第一种就是每个类名前添加完整包名。另一种是使用import语句，可以用import语句导入一个特定的类或者整个包。import语句应位于源文件的顶部(但位于package语句后面)。

还可以使用`星号(*)`导入一个包：`import java.util.*`

若两个不同包中有相同的类名，则可以添加特定的`import`语句来解决：`import java.util.Date;`若有冲突的类名都要用，则在每个类名的前面加上完整的包名。

#### 4.7.2 静态导入

从Java SE 5.0开始，import语句可以导入静态方法和静态域的功能。例如：`import static java.lang.System.*;`就可以使用`System`类的静态方法和静态域，而不必加类名前缀：

    out.println(“GoodBye!My friend!”);  // i.e,System.out
    exit(0);    // i.e., System.exit

静态导入的两个最实际的应用：

1. 算数函数：如果对Math类使用静态导入，就可以采用更加自然的方式使用静态导入：`sqrt( pow( x, 2 ) + pow( y, 2 ))`
2. 笨重的常量：如果需要使用大量带有冗长名字的常量，就应该使用静态导入，例如`calendar`类。

#### 4.7.3 将类放入包中

要想将一个类放入包中，就必须将包的名字放在源文件的开头，包中定义类的代码之前：`package cn.wdx;`

如果没有在源文件中放置package语句，这个源文件中的类就被放置在一个默认包中(default package)。默认包是一个没有名字的包。

#### 4.7.4 包作用域

标记为`public`的部分可以被任意的类使用；标记为`private`的部分只能被定义它们的类使用。如果没有指定`public`或`private`，这个部分(类、方法或变量)可以被同一个包中的所有方法访问。

可以通过`包密封(package sealing)`机制来解决将各种包混杂在一起的问题。如果将一个包密封起来，就不能再向这个包添加类了。

### 4.8 类路径

类文件也可以存储在`JAR(Java归档)`文件中，JAR文件使用ZIP格式组织文件和子目录。
为了能使类能够被多个程序共享，需要做到下面几点：

+ 把类放到一个目录中。
+ 将JAR文件放在一个目录中
+ 设置类路径(class path)。类路径是所有包含类文件的路径的集合。

### 4.9 文档注释

如果在源代码中添加以专用的界定符/**开始的注释，那么可以很容易地生成一个看上去具有专业水准的文档。

#### 4.9.1 注释的插入

javadoc实用程序(utility)从下面几个特性中抽取信息：

+ 包
+ 公有类与接口
+ 公有的和受保护的方法
+ 公有的和受保护的域

应该为上面几部分编写注释。注释应该放置在所描述的特性的前面。注释以`/**`开始，并以`*/`结束。

每个`/**...*/`文档注释在标记之后紧跟着自由格式文本(free-form text)。标记由@开始，如`@author`或`@param`。

自由格式文本的第一句应该是一个概要性的句子。`javadoc`实用程序自动地将这些句子抽取出来形成概要页。

在自由格式文本中，可以使用HTML修饰符，例如，用于强调的`<em>...</em>`、用于设置等宽“打字机”字体的`<code>...</code>`、用于着重强调的`<strong>...</strong>`以及包含图像的`<img...>`等。不过一定不要使用`<h1>`或`<hr>`，因为它们会与文档的格式产生冲突。

#### 4.9.2 类注释

类注释必须放在import语句之后，类定义之前。例子如下：

    /**
     * A <code>Card</code> object represents a playing card,such
     * as “Queen of Hearts”. A card has a suit (Diamond, Heart,
     * Spade or Club) and a value ( 1 = Ace, 2....10,11 = Jack,
     * 12 = Queen, 13 = King).
     */
    public class Card{
        .....
    }

#### 4.9.3 方法注释

每一个方法在注释是必须放在所描述的方法之前。除了通用标记之外，还可以使用下面的标记：

    @param variable description

这个标记将对当前方法的`param(参数)`部分添加一个条目。这个描述可以占据多行，并可以使用HTML标记。一个方法的所有`@param`标记必须放在一起。

    @return description

这个标记将对当前方法添加`return(返回)`部分。这个描述可以跨越多行，并可以使用HTML标记。

    @throws class description

这个标记将添加一个注释，用于表示这个方法有可能抛出异常。

#### 4.9.4 域注释

只需要对公有域(通常指的是静态常量)建立文档。例如：

    /**
     *  The “Hearts” card suit
     */
    public static final int HEARTS = 1;

#### 4.9.5 通用注释

用于类文档的注释

    @author name

这个标记将产生一个“author”(作者)条目。可以使用多个@author标记，每个标记对应一个作者。

    @version text

这个标记将产生一个“version”(版本)条目。这里的text可以是对当前版本的任何描述。
用于所有文档的注释

    @since text

这个标记将产生一个“since”(始于)条目。这里的text可以是对引入特性的版本描述，例如`@since version 1.3.3`。

    @deprecated text

这个标记将对类、方法或变量添加一个不再使用的注释。text中给出了取代的建议。

    @see reference

这个标记将在“see also”部分增加一个超级链接。它可以用于类中，也可以用于方法中。这里的reference可以选择下列情形之一：

+ 第一种情况最常见，只要提供类、方法或变量的名字，`javadoc`就在文档中插入一个超链接。例如，`@see cn.wdx.HelloWorld#text()` 就会建立一个链接到`cn.wdx.HelloWorld`类的`text`方法的超链接。注意要用“#”分隔类名与方法名，或类名与变量名。
+ 如果在`@see`标记后面有一个`<`字符，就需要指定一个超链接。如果在`@see`标记后面有一个双引号字符，文本就会显示在`see also`部分。
+ 可以为一个特性添加多个`@see`标记，但必须将它们放在一起。

#### 4.9.6 包的概述注释

想要产生包注释，就需要在每一个包目录中添加一个单独的文件，可以有如下两个选择：

1. 提供一个以package.html命名的HTML文件。在标记`<BODY>...</BODY>`之间的所有文本都会被抽取出来。
2. 提供一个以`package-info.java`命名的Java文件。这个文件必须包含一个初始的以`/**和*/`界定的`Javadoc`注释，跟随在一个包语句之后。它不应该包含更多的代码或注释。

还可以为所有的源文件提供一个概述性的注释。

这个注释被放置在一个名为`overview.html`的文件中，这个文件位于包含所有源文件的父目录中。标记`<BODY>...</BODY>`之间的所有文本都会被抽取出来。

#### 4.9.7 注释的抽取

详见javadoc的文档。

### 4.10 类的设计技巧

+ 一定将数据设计为私有
+ 一定要对数据初始化
+ 不要在类中使用过多的基本数据类型。
+ 不是所有的域都需要独立的域访问器和域更改器。
+ 使用标准格式进行类的定义。

采用下列顺序书写类的内容：

+ 公有访问特性部分
+ 包作用域访问特性部分
+ 私有访问特性部分

在每一部分中应该按照下列顺序列出

+ 实例方法
+ 静态方法
+ 实例域
+ 静态域

将职责过多的类进行分解

类名和方法名要能够体现它们的职责

## 第5章 继承

### 5.1 类、超类和子类

“is-a”关系是继承的一个明显特征，关键字extends表示继承。例如：

    class Manager extends Employee{
        .... // Manager类继承了Employee类
    }

关键字`extends`表明正在构造的新类派生于一个已存在的类。已存在的类被称为`超类(superclass)`、`基类(base class)`或`父类(parent class)`；新类被称为`子类(subclass)`、`派生类(derived class)`或`孩子类(child class)`。超类和子类是Java程序员最常用的两个术语。

在通过扩展超类定义子类的时候，仅需要指出子类与超类的不同之处。因此在设计类的时候，应该将通用的方法放在超类中，而将具有特殊用途的方法放在子类中。

若超类中的某些方法对于子类中并不适用，就需要提供一个新的方法来`覆盖(override)`超类中的这个方法。但如果在这个新的方法中需要调用超类中的同名方法的时候，可以用`super`来调用，例如：

    public double getSalary(){
        double baseSalary = super.getSalary();
        return baseSalary + bonus;
    }

在子类中可以增加域、增加方法或覆盖超类的方法，然而绝不能删除继承的任何域和方法。
super在构造器中用来调用超类的构造器，例如：

    public Manager( String n, double s, int year ){
        super( n, s, year );
        bonus = 0;
    }

如果子类的构造器没有显式地调用超类的构造器，则将自动地调用超类默认的构造器。如果超类没有不带参数的构造器，并且在子类的构造器中又没有显式地调用超类的其他构造器，则Java编译器将报告错误。

#### 5.1.1 继承层次

继承并不仅限于一个层次，由一个公共超类派生出来的所有类的集合被称为`继承层次(inheritance hierarchy)`。在继承层次中，从某个特定的类到其祖先的路径被称为该类的`继承链(inheritance chain)`。

通常，一个祖先类可以拥有多个子孙继承链。Java不支持多继承。

#### 5.1.2 多态

有一个用来判断是否应该设计为继承关系的简单规则，这就是`is-a`规则，它表明子类的每个对象也是超类的对象。

`is-a`规则的另一种表述方式是置换法则。它表明程序中出现超类对象的任何地方都可以用子类对象置换。

在Java程序设计语言中，对象变量是多态的。一个超类变量既可以引用一个超类对象，也可以引用一个此超类的任何一个子类的对象。然而，不能将一个超类的引用赋给子类变量。

#### 5.1.3 动态绑定

弄清调用对象方法的执行过程十分重要。下面是调用过程的描述：

编译器查看对象的声明类型和方法名。假设调用`x.f(param)`，且隐式参数`x`声明为C类的对象。编译器将会一一列举所有`C`类中名为`f`的方法和其他超类中访问属性为`public`且名为`f`的方法。

至此，编译器已获得所有可能被调用的候选方法。

接下来，编译器查看调用方法时提供的参数类型。如果在所有名为`f`的方法中存在一个与提供的参数类型完全匹配，就选择这个方法。这个过程被称为`重载解析(overloading resolution)`。如果编译器没有找到与参数类型匹配的方法，或者发现经过类型转换后有多个方法与之匹配，就会报告一个错误。

至此，编译器已获得需要调用的方法名字和参数类型。

如果是`private`方法、`static`方法、`final`方法或者构造器，那么编译器可以准确地知道应该调用哪个方法，这种调用方式称为静态绑定(static binding)。与此对应的是，调用的方法依赖于隐式参数的实际类型，并且在运行时实现动态绑定。

当程序运行，并且采用动态绑定调用方法时，虚拟机一定调用与`x`所引用对象的实际类型最合适的那个类的方法。

每次调用方法都要进行搜索，时间开销相当大。因此，虚拟机预先为每个类创建了一个方法表(method table)，与C++中的VTABLE类似，其中列出了所有方法的签名和实际调用的方法。实际调用时查找此表即可。

动态绑定有一个非常重要的特性：无需对现存的代码进行修改，就可以对程序进行扩展。

#### 5.1.4 阻止继承：final类和方法

不允许扩展的类被称为`final`类。如果在定义类的时候使用了`final`修饰符就表明这个类是final类。可以阻止人们定义其子类，如：

    final class Executive extends Manager{...}

类中的方法也可以被声明为final如果这样做，子类就不能覆盖这个方法(`final`类中的所有方法自动成为`final`方法)。如：`public final int getValue()`

将方法或类声明为final的意义在于：确保它们不会在子类中改变语义。

#### 5.1.5 强制类型转换

对象引用的转换语法与数值表达式的类型转换类似，仅需要用一对圆括号将目标类名括起来，并放置在需要转换的对象引用之前就可以了。

在进行类型转换之前，先查看以下是否能够成功地转换。可以简单地使用instanceof运算符实现，如：

    if( staff[1] instanceof Manager){
        boss = (Manager) staff[1];
        ......
    }

综上所述，有两个原则：

1. 只能在继承层次内进行类型转换。
2. 在超类传唤成子类之前，应该使用`instanceof`检查。

一般情况下，应该尽量少用类型转换和`instanceof`运算符。

#### 5.1.6 抽象类

如果自下而上仰视类的继承层次结构，位于上层的类更具有通用性，甚至可能更加抽象。从某种角度看，祖先类更加通用，人们只将它作为派生其他类的基类，而不作为想使用的特定实例类。

使用`abstract`关键字来声明抽象类。

    public abstract String getDescription();
    // no implementation required

为了提高程序的清晰读，包含一个或多个抽象方法的类本身必须被声明为抽象的。除了抽象方法之外，抽象类还可以包含具体数据和具体方法。

抽象方法充当占位的角色，它们的具体实现在子类中。扩展抽象类可以有两种选择。一种是在子类中定义部分抽象方法或抽象方法也不定义，这样就必须将子类也标记为抽象类；另一种是定义全部的抽象方法，这样一来，子类就不是抽象的了。

类即使不含抽象方法，也可以将类声明为抽象类。

抽象类不能被实例化，即不能创建抽象类的对象。但是可以定义一个抽象类的对象变量，但是它只能引用非抽象子类的对象。

#### 5.1.7 受保护访问

+ 仅对本类可见──private。
+ 对所有类可见──public。
+ 对本包和所有子类可见──protected。
+ 对本包可见──默认。

Java中的protected概念要比C++中的安全性差。

### 5.2 Object：所有类的超类

`Object`类是Java中所有类的最终祖先，在Java中每个类都是由它扩展而来的。如果没有明确地指出超类，`Object`就被认为是这个类的超类。

可以使用`Object`类型的变量引用任何类型的对象。当然，`Object`类型的变量只能用于作为各种值的通用持有者。要想对其中的内容进行具体的操作，还需要清楚对象的原始类型，并进行相应的类型转换。

在Java中，只有`基本类型(primitive types)`不是对象。

#### 5.2.1 Equals方法

`Object`类中的`equals`方法用于检测一个对象是否等于另一个对象。在`Object`类中，这个方法将判断两个对象是否具有相同的引用。

#### 5.2.2 相等测试与继承

Java语言规范要求equals方法具有下面的特性：

+ 自反性：对于任何非空引用`x`，`x.equals(x)`应该返回`true`。
+ 对称性：对于任何引用`x`和`y`，当且仅当`y.equals(x)`返回`true`，`x.equals(y)`也应该返回`true`。
+ 传递性：对于任何引用`x`、`y`和`z`，如果`x.equals(y)`返回`true`，`y.equals(z)`返回`true`，`x.equals(z)`也应该返回`true`。
+ 一致性：如果`x`和`y`引用的对象没有发生变化，反复调用`x.equals(y)`应该返回同样的结果。
+ 对于任意非空引用`x`，`x.equals(null)`应该返回`false`。

可以从两个截然不同的情况看待getClass的使用：

1. 如果子类能够拥有子集的相等概念，则对称性需求将强制采用getClass进行检测。
2. 如果由超类决定相等的概念，那么就可以使用instanceof进行检测，这样就可以在不同子类对象之间进行相等的比较。

下面给出编写一个完美的equals方法的建议：

+ 显式参数命名为`otherObject`，稍后需要将它转换称另一个叫做`other`的变量。
+ 检测`this`与`otherObject`是否引用同一个对象：`if( this == otherObject ) return true;`
+ 检测`otherObject`是否为`null`，如果为`null`，返回`false`。`if( otherObject == null ) return false;`
+ 比较`this`与`otherObject`是否属于同一个类。
+ 如果`equals`语义在每个子类中有所改变，就使用`getClass`检测：`if (getClass() != otherObject.getClass()) return false;`
+ 如果所有的子类拥有统一的语义，就使用`instanceof`检测：`if( ! ( otherObject instanceof ClassName )) return false;`
+ 将`otherObject`转换相应的类型变量：`ClassName other = ( ClassName )otherObject;`

现在开始对所有需要比较的域进行比较。使用 `==` 比较基本类型域，使用`equals`比较对象域。如果所有都匹配，就返回`true`，否则返回`false`

    return field1 == other.field1
        && field2.equals(other.field2)
        && ...;

如果在子类中重新定义`equals`，就要在其中包含调用`super.equals(other)`。

#### 5.2.3 HashCode方法

`散列码(hash code)`是由对象导出的一个整型值，是没有规律的。可以用做来判断对象是否相等。

**java.lang.Object**

+ `int hashCode()`
    + 返回对象的散列码。散列码可以是任意的整数，包括正数或负数。两个相等的对象要求返回相等的散列码。
+ `Class getClass()`
    + 返回包含对象信息的类对象。Java提供了类运行时的描述，被封装在Class类中。
+ `boolean equals( Object otherObject )`
    + 比较两个对象是否相等，如果两个对象指向同一块存储区域，方法放回true；否则方法返回false。在自定义类中，应该覆盖这个方法。
+ `String toString()`
    + 返回描述该对象值的字符串。在自定义类中，应该覆盖这个方法。
+ `Object clone()`
    + 创建一个对象的副本。Java运行时系统将为新实例分配存储空间，并将当前的对象复制到这块存储区域中。

**java.lang.Class**

+ `String getName()`
    + 返回这个类的名字。
+ `Class getSuperclass()`
    + 以Class对象的形式返回这个类的超类信息。

#### 5.2.4 ToString方法

在`Object`中还有一个重要的方法，就是`toString`方法，它用于返回表示对象值的字符串。绝大多数的`toString`方法都遵循这样的格式：类的名字，随后是一对方括号括起来的域值。

如果`x`是任意一个对象，并调用`System.out.println(x)`; 就会直接调用`x.toString()`，并打印输出得到的字符串。

### 5.3 泛型数组列表

在Java SE 5.0中，`ArrayList`是一个采用`类型参数(type parameter)`的`泛型类(generic class)`。为了指定数组列表保存的元素对象类型，需要用一对尖括号将类名括起来加在后面。下面声明和构造一个保存`Employee`对象的数组列表：

    ArrayList<Employee> staff = new ArrayList<Employee>();

使用`add`方法可以将元素添加到数组列表中。如果调用`add`且内部数组已经满了，数组列表就将自动地创建一个更大的数组，并将所有的对象从较小的数组中拷贝到较大的数组中。

如果已经清楚或能够估计出数组可能存储的元素数量，就可以在填充数组之前调用`ensureCapacity`方法：

    staff.ensureCapacity(100);

这个方法调用将分配一个包含100个对象的内部数组。然后调用100次add，而不用重新分配空间。

**java.util.ArrayList<T>**

+ `ArrayList<T>`
    + 构造一个空数组列表
+ `ArrayList<T>(int initialCapacity)`
    + 用指定容量initialCapacity构造一个空数组列表
+ `boolean add(T obj)`
    + 在数组列表的尾端添加一个元素obj。永远返回true。
+ `int size()`
    + 返回存储在数组列表中的当前元素数量。(这个值将小于或等于数组列表的容量)
+ `void ensureCapacity(int capacity)`
    + 确保数组列表在不重新分配存储空间的情况下就能够保存给定数量的元素。
+ `void trimToSize()`
    + 将数组列表的存储容量削减到当前尺寸。
+ `void set( int index, T obj )`
    + 设置数组列表指定位置的元素值，此操作将覆盖这个位置的原有内容。
+ `T get( int index )`
    + 获得指定位置的元素值。
+ `void add( int index, T obj )`
    + 向后移动元素，以便插入元素。
+ `T remove( int index )`
    + 删除一个元素并将后面的元素向前移动。被删除的元素由返回值返回。

#### 5.3.1 访问数组列表元素

数组列表自动扩展容量的便利增加了访问元素语法的复杂程度。使用`get`和`set`方法实现访问或改变数组元素的操作。例如：

    staff.set(i,harry);
    Employee e = staff.get(i);

使用`add`方法为数组添加新元素，而不要使用`set`方法，它只能替换数组中已经存在的元素内容。

也可以使用`for each`循环对数组列表遍历：

    for(Employee e : staff)
        do something with e

请注意下面的变化：

+ 不必指出数组的大小。
+ 使用`add`将任意多的元素添加到数组中。
+ 使用`size()`替代`length`计算元素的数目。
+ 使用`a.get(i)`替代`a[i]`访问元素。

### 5.4 对象包装器与自动打包

有时，需要将int这样的基本类型转换为对象。所有的基本类型都有一个与之对应的类。例如，Integer类对应基本类型int。通常，这些类称为包装器(wrapper)。对象包装器类是不可变的，即一旦构造了包装器，就不允许更改包装在其中的值。对象包装器类还是final，因此不能定义它们的子类。

假设想定义一个整型数组列表。而尖括号中的类型参数不允许是基本类型，也就是说，不允许写成`ArrayList<int>`。这里就用到了`Integer`对象包装器类。我们可以声明一个`Integer`对象的数组列表。

    ArrayList<Integer> list = new ArrayList<Integer>();

Java SE 5.0的另一个改进之处是更加便于添加或获得数组元素。

`list.add(3);` 将自动变成 `list.add(new Integer(3));`

这种变换被称为`自动打包(autoboxing)`。

相反的，当将一个`Integer`对象赋给一个`int`值时，会自动地拆包。包含在包装器中的内容不会改变。不能使用这些使用这些包装器类创建修改数值参数的方法。如果想要修改参数值的方法，就要使用`持有者(holder)`类型。

最后强调以下，打包和拆包是**编译器**认可的，而不是虚拟机。

**java.lang.Integer**

+ `int intValue()`
    + 以int的形式返回Integer对象的值。
+ `static String toString( int i )`
    + 以一个新String对象的形式返回给定数值 i 的十进制表示。
+ `static String toString( int i, int radix )`
    + 返回数值 i 的基于给定radix参数进制的表示。
+ `static int parseInt( String s )`
+ `static int parseInt( String s, int radix )`
    + 返回字符串 s 表示的整型数值，给定字符串表示的十进制的整数，或者是radix参数进制的整数。
+ `static Integer valueOf( String s )`
+ `static Integer valueOf( String s, int radix )`
    + 返回用 s 表示的整型数值进行初始化后的一个新Integer对象，给定字符串表示的是十进制的整数，或者是radix参数进制的整数。

**java.text.NumberFormat**

+ `Number parse( String s )`
    + 返回数字值，假设给定的String表示了一个数值。

### 5.5 参数数量可变的方法

可以用省略号...表明这个方法可以接收任意数量的对象。例如

    public static double max( double... values){
        double largest = Double.MIN_VALUE;
        for( double v : values) if (v > largest ) largest = v;
        return largest;
    }

### 5.6 枚举类

    public enum Size{ SMALL, MEDIUM, LARGE, EXTRA_LARGE };

实际上，这个声明定义的类型是一个类，它刚好有4个实例，在此尽量不要构造新对象。如果需要的话，可以在枚举类型中添加一些构造器、方法和域。当然构造器只是在构造枚举常量的时候被调用。

每个枚举类型都有一个静态的`values`方法，它将返回一个包含全部枚举值的数组。

**java.lang.Enum<E>**

+ `static Enum valueOf( Class enumClass, String name )`
    + 返回指定名字、给定类的枚举常量。
+ `String toString()`
    + 返回枚举常量名。
+ `int ordinal()`
    + 返回枚举常量在enum声明中的位置，位置从 0 开始计数。
+ `int compareTo(E other)`
    + 如果枚举常量出现在other之前，则返回一个负值；如果this == other，则返回 0；否则，返回正值。枚举常量的出现次序在enum声明中给出。

### 5.7 反射

`反射库(reflection library)`提供了一个非常丰富且精心设计的工具集，以便能编写能够动态操纵Java代码的程序。使用反射，Java可以支持Visual Basic用户习惯使用的工具。特别是在设计或运行中添加新类时，能够快速地应用开发工具动态地查询新添加类的能力。

能够分析类能力的程序被称为反射(reflective)。反射机制的功能极其强大。可以用反射机制：

+ 在运行中分析类的能力。
+ 在运行中查看对象，例如，编写一个toString方法供所有类使用。
+ 实现数组的操作代码。
+ 利用Method对象，这个对象很像C++中的函数指针。
+ 反射是一种功能强大且复杂的机制。使用它的主要对象是工具构造者。

## 附录1 C++注释

> Java的类与C++的类

Java中的所有函数都属于某个类的方法(标准术语称其为方法，而不是成员函数)。因此，Java中的所有函数都必须有一个外壳类并且`main`方法必须是静态的。如果`main`方法正确退出，那么Java应用程序的退出代码为0，如果想要在终止程序的时候返回其他代码，那就需要调用`System.exit`方法。

> Java的整型与C++的整型

+ 在C和C++中，int表示的整型与目标机器相关。Java没有任何无符号类型(unsigned type)。
+ boolean值的不同
+ 在C++中，数值或指针可以代替boolean值。0相当于false，非0值相当于true。在Java中就不行。

> 变量的声明与定义

C和C++中变量的声明与定义是不同的。在Java中，不区分变量的声明与定义。

> const

`const`是Java的保留关键字，但目前并未使用，必须用`final`定义常量。

> 移位操作

在C和C++中无法确定 `>>` 操作执行的是算数移位(扩展符号位)，还是逻辑移位(高位填0)。实际上在C和C++中，`>>` 运算符实际上是只为非负数定义的。Java消除了这种含糊性。

> boolean的强制类型转换

不要在boolean类型与任何数值类型之间进行强制类型转换，这样可能防止发生错误。

> 逗号运算符？

与C和C++不同，Java不使用逗号运算符，不过可以在for语句中用逗号隔开表达式列表。

> Java中的字符串

与C++不同，Java字符串更加像char*指针，自动的垃圾回收也可以避免内存泄露。

> 流程结构

Java的控制流程功能结构与C和C++的控制流程结构一样，只有很少的例外情况。没有goto语句，但break语句可以带标签，可以利用它实现从内层循环跳出的目的。还有一种变形的for循环，类似于C#中的foreach循环。

> 嵌套的块

在C++中，可以在嵌套的块中重定义一个变量。在内层定义的变量会覆盖在外层定义的变量。这样，有可能导致程序设计错误，因此在Java中不允许这样做。

> 运算符重载

与C++不同，Java没有提供运算符重载功能。Java语言的设计者确实为字符串的连接重载了+运算符，但是没有重载其他运算符，也没有给Java程序员自己重载运算符的权利。

> Java数组与C++数组

Java数组与C++数组在堆栈上有很大不同，但基本上与分配在堆(heap)上的数组指针一样。Java中的[]运算符被预定义为检查数组边界，而且没有指针运算，不能通过数组名加1来得到数组的下一个元素。

> Java对象变量

在C++中没有空引用，并且引用不能被赋值。我们可以将Java的对象看作C++的对象指针。在Java中指针问题不再困扰。如果使用一个没有初始化的指针，系统就会产生一个运行时错误，而不是随机的结果。垃圾收集器会处理内存管理问题。

> 更改器和访问器

在C++中，带有const后缀的方法是访问器方法；默认为更改器方法。Java中，访问器方法与更改器方法语法上没有明显的区别。

> Java的构造器

Java构造器的工作方式与C++一样。但是，要记住所有的Java对象都是在堆中构造的，构造器总是伴随着new操作符一起使用。C++程序员最容易犯得作物就是忘记new操作符。

> Java的内部定义

在C++中，通常在类的外面定义方法，如果在类的内部定义方法，这个方法就自动成为内联方法。在Java中，所有的方法都必须在类的内部定义，但并不表示它们是内联方法。

> static的不同含义

Java中的静态域与静态方法在功能上与C++相同。但是语法却有不同。C中static有三种含义：

+ 表示退出一个块后依然存在的局部变量。
+ 不能被其他文件访问的全局变量和函数。
+ 属于类且不属于类对象的变量和函数。这个含义与Java相同。

> 值调用和引用调用

C++有值调用和引用调用，用`&`符号标记，可以实现修改它们的引用参数的目的。而Java则不行，Java只有值调用。

> 初始化

在C++中，不能直接初始化实例域。所有的域必须在构造器中设置。但是，有一个特殊的初始化器列表语法。C++使用这种特殊的语法来调用域构造器。在Java中没有这种必要，因为对象没有子对象，只有指向其他对象的指针。

> 构造器

在Java中，this引用等价于C++的this指针。但是，在C++中，一个构造器不能调用另一个构造器。在C++中，必须将抽取初的公共初始代码编写成一个独立的方法。
> `#include与import`

这两者并没有共同之处。在C++中，必须使用#include将外部特性的声明加载近来，因为C++编译器无法查看任何文件的内部，除了正在编译的文件以及在头文件中明确包含的文件。Java编译器可以查看其他文件的内部。

在Java中，通过显式地给出包名，就可以不使用import；而在C++中，无法避免使用#include。

在C++中，与包机制类似的是命名空间(namespace)。在Java中，package与import语句类似C++中的namespace和using指令(directive)。

> Java的继承和C++的继承

Java与C++定义继承类的方式十分相似。Java用关键字extends代替了C++的冒号(:)。在Java中，所有的继承都是公有继承，而没有C++中的私有继承和保护继承。

> 调用超类及虚拟方法

在Java中使用关键字super调用超类的方法，而在C++中则采用超类名加上::操作符的形式。

在Java中，不需要将方法声明为虚拟方法。动态绑定是默认的处理方式。如果不希望让一个方法具有虚拟特性，可以将它标记为final。

> 根类

C++中没有类似Java中Object的根类，不过每个指针都可以转换成`void*`。

## 附录2 Java注释与警告

+ `System.out`中的`println`方法输出后自动换行，而`print`方法不换行。
+ `/*...*/`注释不能嵌套。
+ Java有一个能够表示任意精度的算数包，通常称为“大数值”(big number)，并不是一种新的类型，而是一个Java对象。
+ 在JDK5.0中，可以使用十六进制表示浮点数值，使用p表示指数，尾数采用十六进制，指数采用十进制。指数的基数是2。
+ 浮点数值不适用于禁止出现舍入误差的金融计算中。
+ `&` 和 `|` 运算符应用于布尔值，得到的结果也是布尔值，不按“短路”方式计算。
+ 如果试图将一个数值从一种类型强制转换为另一种类型，而又超出了目标类型的表示范围，就会成为一个完全不同的值。

因为输入是可见的，所有Scanner类不适用于从控制台读取密码。Java SE 6特别引入了Console类实现这个目的。要想读取一个密码，可以采用下列代码

    Console cons = System.console();
    String username = cons.readLine(“User name: ”);
    char[] passwd = cons.readPassword(“Password: ”);

为了安全起见，返回的密码存放在一维字符数组中，而不是字符串中。在对密码进行处理后，应该马上用一个填充值覆盖数组元素。采用Console对象处理输入不如采用Scanner对象方便。

+ 可以构造一个带有字符串参数的Scanner，但这个Scanner将字符串解释为数据，而不是文件名。
+ 在循环中，检测两个浮点数是否相等需要格外小心。
+ 可以使用下面两种形式声明数组：`int[] a;` 或 `int a[];` 大多数Java应用程序员喜欢第一种。
+ 在Java中允许数组长度为0。数组长度为0与null不同。
+ 类的方法在前面，域在后面这种风格有易于促使人们更加关注接口的概念，削减对实现的注意。
+ 不要在构造器中定义与实例域重名的局部变量。
+ 注意不要编写返回引用可变对象的访问器方法，这样会破坏封装性！如果需要返回一个可变对象的引用，应该首先对它进行克隆(clone)。
+ 在绝大多数的面型对象程序设计语言中，静态域被称为类域。术语`static`只是沿用了C++的叫法，并无实际意义。
+ 可以使用对象调用静态方法。不过这种方式很容易造成混淆，建议使用类名来调用静态方法。
+ 每一个类可以有一个`main`方法。这是一个常用于对类进行单元测试的技巧。
+ Java允许重载任何方法。因此，要完整地描述一个方法，需要指出方法名以及参数类型。这叫做方法的签名(signature)。返回类型不是方法签名的一部分。
+ 如果文档中有到其他文件的链接，例如，图像文件(用户界面的组建的图表或图像等)，就应该将这些文件放到子目录`doc-files`中。`javadoc`实用程序将从源目录拷贝这些目录中及其中的文件到文档目录中。在联接种需要使用`doc-files`目录，例如：`<img src=“doc-files/uml.png” alt = “UML diagram”>`。
+ 注释时没必要在每一行开始用星号`*`，大部分IDE会自动添加星号`*`。
+ 关键字`this`有两个用途：一是引用隐式参数，二是调用该类其他的构造器。同样，`super`关键字也有两个用途：一是调用超类的方法，二是调用超类的构造器。
+ 在覆盖一个方法时，子类方法不能低于超类方法的可见性。特别是，如果超类方法是`public`，子类方法一定要声明为`public`。
+ 域也可以被声明为`final`，一旦如此，构造对象之后就不允许修改其值了。不过如果将一个类声明为`final`，只有其中的方法自动称为`final`，而不包括域。
+ 强烈建议为自定义的每一个类增加`toString`方法。这样做不仅自己受益，而且所有使用这个类的程序员也会受益匪浅。
