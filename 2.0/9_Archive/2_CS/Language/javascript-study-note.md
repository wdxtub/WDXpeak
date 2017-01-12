# Javascript 学习指南

学一个新语言还是找经典书籍来看比较靠谱，虽然看起来慢，但是其实会更快，因为遇到问题的时候脑子里会有大概的解决思路，网上的教程的确是可以快速入门，但是大概瞄了一下总觉得少了点逻辑关联。对于 JavaScript 来说，《JavaScript 权威指南》作为圣经，我觉得是比较正确的打开方式，这里主要是学习这本书的一些笔记。

既然是笔记，也就意味着只是全书内容的一小部分，查漏补缺可以，但是如果真的要系统学习，还是找一本书安心来看比较好。

## JavaScript 概述

面向 Web 的动态的弱类型的编程语言，非常适合面向对象和函数式编程。调试的话一可以在 html 文件中嵌入并用浏览器打开，而可以直接使用浏览器自带的调试功能进行测试(Chrome, Firefox等)

比方说在 Chrome 中打开 developing tools，然后选择 Console 这个 tab，就可以编写代码测试了

以下是 JavaScript 语言的一个快速概览，包含基本的 JavaScript 用法，当然后面也会具体介绍，这里主要是给大家一个基本的概念和感觉。

变量通过 `var` 关键字声明，所有在双斜线 `//` 后面的内容都是注释

```javascript
var x; // 声明一个变量
x = 0; // 通过等号给变量赋值
```

JavaScript 支持多种数据类型

```javascript
x = 1; // 数字
x = 0.01; // 整数和实数共用一种数据类型
x = "Hello wdx"; // 这里双引号和单引号都可以用来表示字符串
x = true; // 布尔值，另一个是 false
x = null; // 表示空值
x= undefined; // 和 null 非常类似
```

JavaScript 中两个非常重要的数据类型是对象和数组。对象是名/值对的集合，或字符串到值映射的集合，通过 `.` 或者 `[]` 来访问对象属性，例如

```javascript
var book = {
	topic: "JavaScript",
	fat = true
};

book.topic // 返回 "JavaScript"
book["fat"] // 返回 true
book.author = "wdx"; // 通过赋值创建一个新对象
book.contents = {}; // 用 {} 创建一个空对象，它没有属性
```

JavaScript 也支持数组，数组和对象中都可以包含另一个数组与对象。通过方括号和花括号定义对象的方式叫做初始化表达式(initializer expression)。

```javascript
var primes = [2, 3, 5, 7];
primes[0] // 返回 2
primes.length // 返回长度 4
primes[4] = 9; // 通过赋值来添加新元素

var empty=[]; // 新建空数组
empty.length // 返回 0

// 嵌套包含
var points = [
	{x:0, y:0},
	{x:1, y:1}
];

var data = {
	trial1: [[1, 2],[3, 4]],
	trial2: [[2, 3],[4, 5]]
}
```

JavaScript 中常见的运算符 (operator)

```javascript
// +, -, *, / 比较常见，和其他语言用法一致
"3" + "2" // 加号还可以用作字符串连接，返回 "32"

// ++, --, +=, -=, *=, /= 这些简便运算符也都是有的

// 判断关系: ==, !=, <, <= ,> ,>=
"two" == "three" // false 两个字符串不相等
"two" > "three" // true "tw" 在字母表中的索引大于 "th"
false == (x > y) // true: false 和 false 相等
```

函数、方法和控制语句会在接下来的章节中具体介绍

### 客户端 JavaScript

这里主要需要弄明白的内容是：

+ 如何让 JavaScript 在 Web 浏览器中运行起来
+ Web 浏览器端脚本技术以及重要的全局函数
+ 通过脚本来操纵 HTML 文档内容
+ 操纵 HTML 中定义 Web 内容的元素
+ 如何使用 JavaScript 来进行 CSS 样式操作
+ 通过事件处理程序(event handler)来定义文档的行为
+ jQuery 库定义了一套灵巧易用的 API，用来操控文档内容、样式和行为。利用 `$()` 函数

## JavaScript 语言核心

### 词法结构

一些要点

+ JavaScript 程序是用 Unicode 字符集编写的
+ 大小写敏感
+ JavaScript 会忽略 token 间的空格和换行符
+ 注释方式 `//` 或者 `/* */`，后者可以跨行，但不能嵌套
+ 直接量(literal) 是程序中直接使用的数据值
+ 变量名必须以字母、下划线或者美元符号开始，后面可以是字母数字下划线美元符号
+ 保留字: break, delete, function, return, typeof, case, do, if, switch, var, catch, else, in, this, void, continue, false, instanceof, throw, while, debugger, finally, new, true, with, default, for, null, try
+ ECMAScript 5 的保留关键字: class, const, enum, export, extends, import, super
+ ECMAScript 3 将 Java 的所有关键字都列为保留字，为了实现兼容，请尽可能避免使用: abstract, double, goto, native, static, boolean, enum, implements, package, super, byte, export, import, private, synchronized, char, extends, int, protected, throws, class, final, interface, public, transient, const, float, long, short, volatile
+ JavaScript 预定能很多全局变量和函数，应当避免使用它们作为变量名和函数名: arguments, encodeURI, Infinity, Number, RegExp, Array, encodeURIComponent, isFinite, Object, String, Boolean, Error, isNaN, parseFloat, SyntaxError, Date, eval, JSON, parseInt, TypeError, decodeURI, EvalError, Math, RangeError, undefined, decodeURIComponent, Function, NaN, ReferenceError, URIError
+ 每一种特定的 JavaScript 运行环境都有自己的一个全局属性列表
+ 虽然句末的分号不是必须的，但是为了美观和避免奇怪的错误，还是加上为好

### 类型、值和变量

一些要点

+ 数据类型分为两类：原始类型(primitive type) 和对象类型(object type)
+ 原始类型包括数字、字符串和布尔值
+ null 和 undefined 是特殊的原始值，通常分别代表了各自特殊类型的唯一的成员
+ 对象是属性(property)的集合
+ 另一种特殊对象是函数。函数是具有与它相关联的可执行代码的对象
+ JavaScript 解释器有自己的内存管理机制，可以自动对内存进行垃圾回收(garbage collection)
+ JavaScript 的类型还可以分为可变(mutable)类型和不可变(immutable)类型。对象和数组属于可变类型，数字布尔值null和undefined属于不可变类型
+ JavaScript 的变量是无类型的 (untyped)，采用词法作用域(lexical scoping)，不在任何函数内声明的变量就是全局变量

#### 数字

+ 不区分整数值和浮点数值，统一用浮点数值表示
+ 十六进制用 `0x` 或 `0X` 为前缀
+ 八进制最好就不要用了，在 ECMAScript 6 的严格模式下是不允许的
+ 简洁的语法: [digits][.digits][(E|e)[(+|-)]digits]
	+ 6.02e23
	+ 1.4738223E-32

**算数运算**

`+ - * / %` 和其他语言一致

```javascript
Math.pow(2, 53)  // 9007199254740992: 2 的 53 次幂
Math.round(.6)   // 1.0: 四舍五入
Math.ceil(.6)    // 1.0: 向上去整
Math.floor(.6)   // 0.0: 向下求整
Math.abs(-5)     // 5: 求绝对值
Math.max(x,y,z)  // 返回最大值
Math.min(x,y,z)  // 返回最小值
Math.random()    // 生成一个 0-1.0 的伪随机数
Math.PI          // 圆周率
Math.E           // 自然对数
Math.sqrt(3)     // 3 的平方根
Math.pow(3, 1/3) // 3 的立方根
Math.sin(0)      // 三角函数: Math.cos, Math.atan 等
Math.log(10)     // 10 为底的自然对数
Math.log(100)/Math.LN10 // 10 为底 100 的对数
Math.log(512)/Math.LN2  // 2 为底 512 的对数
Math.exp(3)      // e 的三次幂  
```

算术运算在溢出、下溢或被零整除时不会报错，而是会用 `Infinity`, `-Infinity` 表示。负零值和正零值是相等的，除了作为除数的时候

```javascript
var zero = 0
var negz = -0
zero === negz // true
1/zero === 1/negz // false
```

日期和时间用 `Date` 类表示，日期对象不是基本数据类型，下面是一个简单的例子

```javascript
var then = new Date(2011, 8, 11); // 2011 年 9 月 11 日
var later = new Date(2011, 8, 11, 11, 11, 11); // 加上了时间
var now = new Date(); // 当前日期时间
var elapsed = now - then; // 计算时间间隔的毫秒数
later.getFullYear(); // 2011
later.getMonth(); // 8: 从 0 开始计数的月份
later.getDate(); // 11: 从 1 开始计数的天数
later.getDay(); // 得到星期几
later.getHours(); // 时间
later.getUTCHours(); // 使用 UTC 表示小时的时间，基于时区
```

#### 文本

+ 字符串是一组由 16 位值组成的不可变的有序序列，每个字符通常来自于 Unicode 字符集
+ 转义字符 `\`
+ `\o` NUL 字符
+ `\b` 退格符
+ `\t` 水平制表符
+ `\n` 换行符
+ `\v` 垂直制表符
+ `\f` 换页符
+ `\r` 回车符
+ `\"` 双引号
+ `\'` 单引号或撇号
+ `\\` 反斜线
+ `\xXX` 两位十六进制数 XX 指定的 Latin-1 字符
+ `\uXXXX` 四位十六进制数 XXXX 指定的 Unicode 字符

字符串的其他一些方法，注意字符串本身是不会被改变的，所以都是会返回一个新的字符串。在 ECMAScript 5 中也可以直接用方括号索引指定位置

```javascript
var s = "Hello, wdx"
s.length             // 长度
s.charAt(0)          // 获取第一个字符
s.charAt(s.length-1) // 获取最后一个字符
s.substring(1,4)     // 获取第 2-4 个字符
s.slice(1,4)         // 同上
s.slice(-3)          // 获取最后 3 个字符
s.indexOf("l")       // 字符 l 第一次出现的位置
s.lastIndexOf("l")   // 字符 l 最后一次出现的位置
s.indexOf("l",3)     // 字符 l 在位置 3 之后首次出现的位置
s.split(" ")         // 用空格分割成子串
s.replace("h", "H")  // 字符替换
s.toUpperCase()      // 变成大写
```

使用 `RegExp()` 构造函数可以使用正则表达式，两条斜线之间的文本构成了一个正则表达式直接量，例如：`/[1-9][0-9]*/`

#### 布尔值

true 和 false

#### null 和 undefined

可以将 null 认为是一个特殊的对象值(进行 typeof 运算会返回 object)，含义是『非对象』

用未定义值(undefined)来表示更深层次的空值，表示变量没有初始化

#### 全局对象

+ JavaScript 程序可以直接使用
+ 包括
	+ 全局属性: undefined, Infinity, NaN
	+ 全局函数: isNaN(), parseInt(), eval()
	+ 构造函数: Date(), RegExp(), String(), Object(), Array()
	+ 全局对象: Math, JSON 

#### 包装对象

类似于 Java 中的 Integer 与 Character 类 

#### 不可变的原始值和可变的对象引用

类似于 Java 中的传值与传引用的区别

#### 类型转换

== 运算符在判断两个值相等时会做类型转换

=== 运算符不会做类型转换

### 表达式和运算符

基本来说和 Java, Cpp, Python 等没有太大的区别，这里只提一些要点：

+ 用关键词 new 来新建对象，如果构造函数不需要参数，那么可以省略空圆括号对
+ `~` 按位求反
+ `&` 按位与
+ `|` 按位或
+ `^` 按位异或
+ `!` 逻辑非
+ `delete` 删除属性
+ `typeof` 检测类型
+ `<<` 左移位
+ `>>` 有符号右移
+ `>>>` 无符号右移
+ `instanceof` 测试对象类
+ `in` 测试属性是否存在
+ `===` 判断恒等
+ `!==` 判断非恒等

这里 `===` 和 `==` 比较容易混淆，简单的理解就是，前者需要各方面都相等，后者只需要值或者类型转换后的值相等即可

eval() 功能很强大，但是要慎用

### 语句

基本来说就是三个类别：条件，循环，跳转。直接给出几个例子，就很明白了

```javascript
// if ... else if ... else
if (condition){
	statements
}
else if (condition) {
	statements
}
else {
	statements
}

// switch
switch(expression){
	case val1:
		statements
		break;
	case val2:
		statements
		break;
	default:
		statements
		break;
}

// while
while (expression){
	statements
}

// do while
do{
	statements
} while(expression)


// for
for (initiale; test; increment){
	statement
}

// for in
for (variable in object){
	statement
}

// throw
throw expression
e.g
if (x < 0) thrw new Error("x can't be negative");

// try/catch/finally
try{
	statements
}
catch(e){
	statements
}
finally{
	statementss
}

// empty
empty; // 什么也不做，可以用作占位

```

+ 循环中可以使用 continue 与 break 来进行控制。
+ JavaScript 还支持标签，但是会使得代码比较乱，我不是很推荐用
+ 最好不要使用 with 语句，对性能影响很大，也很难优化
+ debugger 语句用于临时调试
+ `use strict` 严格模式执行指令(和语句还是有区别的)

#### 函数

用关键字 function 来定义函数

```javascript
function funcname([arg1 [, arg2 [..., argn]]]){
	statements
}

function hypotenuse(x, y){
	return Math.sqrt(x*x + y*y);
}
```

### 对象

+ 基本上和其他面向对象语言的类一致，
+ 删除属性使用 `delete` 关键字
+ 检测属性 `in`, `hasOwnProperty()`, `propertyIsEnumerable()` 来完成

#### 继承

面向对象的思路，看例子

```javascript
var o = {}
o.x = 1;
var p = inherit(o);
p.y = 2;
var q = inherit(p);
q.z = 3;
```

#### 枚举属性

具体在例子中

```javascript
for (p in o){
	if (!o.hasOwnProperty(p)) continue; // 跳过继承的属性
}
for (p in o){
	if (typeof o[p] === "function") continue; // 跳过方法
}
```

#### 序列化对象

基本都是用 JSON 来搞，这两个方法 `JSON.stringify()` 和 `JSON.parse()`

### 数组

整体思路和 python 非常类似

+ 方括号来进行声明初始化
+ 数组方法
	+ join(): 将所有元素转换为字符串并连接到一起，如果不指定分隔符，则默认用逗号
	+ reverse(): 颠倒元素顺序
	+ sort(): 排序，可以传入一个比较函数，例如
		+ `a.sort(function(a,b) {return b-a};`
	+ concat(): 创建并返回一个新数组，元素包括调用 concat() 的原始数组的元素和 concat() 的每个参数
	+ slice(): 返回数组片段，但是不修改数组本身
	+ splice(): 返回数组片度，并且会修改数组本身
		+ `var a = [1, 2, 3, 4, 5, 6, 7, 8];`
		+ `a.splice(4);` 返回 [5, 6, 7, 8]，a 变为 [1, 2, 3, 4]
	+ push(): 数组尾添加元素，并返回数组新的长度
	+ pop(): 删除最后一个元素，并返回这个元素
	+ push 和 pop 会修改并替换原数组，而不是生成新的数组
	+ unshift(): 数组头部添加元素，并返回新数组元素
	+ shift(): 删除第一个元素，并把之后的元素移过来补位，返回删除的元素
	+ toString(): 类似于默认的 join() 方法
+ ECMAScript 5 中的数组方法
	+ forEach()
	+ map()
	+ filter()
	+ every()
	+ some()
	+ reduce()
	+ reduceRight()
	+ indexOf()
	+ lasIndexOf()

## JavaScript 核心进阶

### 函数

### 类和模块

### 正则表达式的模式匹配 

### JavaScript 的子集和扩展

### 服务器端 JavaScript


