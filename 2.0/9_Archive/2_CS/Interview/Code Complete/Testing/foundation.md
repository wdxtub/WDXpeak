# Testing 

在面试软件开发的过程中，面试官可能也会询问关于软件开发流程以及测试方法相关的问题。在大多数互联网公司，许多部门不一定配有专门的QA(Quality Assurance)，在这种情况下，程序员本身需要对自己开发的模块和系统进行测试。另一方面，程序员在开发过程中测试自己的程序也是非常好的习惯，这样可以确保开发效率。基于上述原因，面试软件开发职位但遇到测试相关的问题并不少见。本章节总结了一些常见的测试相关问题及解题方法，并且在“工具箱”部分列举了测试相关的常见概念。如果需要面试测试相关的专门职位，建议查阅更多相关资料。

## 测试现实世界的物体、软件或函数

三者并无本质的差别，问题的核心均在于：测试对象在不同的输入下，能否实现预计的功能，提供恰当的输出。 一般情况下，总是需要考虑以下几个方面，以全面测试对象对于不同类型输入的"效果"：

(1) 常规情况(Normal cases)

输入不同类型的合法数据，主要用以判断对象的功能性：在给定输入的情况下能否给出期望的输出，由此判断功能的实现是否正确。比如，测试银行账户的转账功能：假设账户中有1000元，可以输入100，2000等并判断余额及转出钱数是否符合期望。

(2) 极端情况(Extreme cases)

测试一些边界条件或极端情况。所谓的极端情况包括多用户或多线程情况下频繁地访问／更新数据。比如，继续测试银行账户的转账功能：假设账户中有1000元，可以测试边界条件，取出1000元等。或者测试极端情况，假设用户开了多个页面，并在每个页面上几乎同时都尝试转出1000元，或者用户通过ATM机和手机APP同时进行转账操作等。

(3) 非法情况(Invalid case)

主要测试用户输入非法数据时系统不会崩溃，并且能够给出恰当的反馈。比如，测试银行账户的转账功能：当用户输入大于账户余额的数字时，或者当接收人账户错误时，系统能否给出错误提示等。

## 故障排除(Troubleshooting)

另一大类的常见问题是给出一个有问题的测试现象，让面试者判断问题出现在哪里。对于这类问题，首先考虑测试对象由生成，到运行，到产生最终结果的完整流程，其次判断每一步执行了什么，需要依赖哪些参数，该步骤的异常是否会导致最终的测试现象，并且考虑如何验证自己的判断。 例如，测试用户无法访问你开发的网站。首先考虑主要流程，简述如下：用户连接到网络，发送HTTP请求到网站，网站发送数据包给用户，用户浏览器显示页面。在此例中，每一步都有可能导致无法访问网站的情况，具体描述如下：

(1) 用户连接到网络：这一步用户需要获得有效的IP，获取访问互联网的权限。需要依赖用户的网卡是否工作正常，是否能够被分配到有效的IP，是否能够从路由器或者服务器获得互联网访问权限等等。检验方式可以是：可以打开终端用ping命令，尝试建立与大型网站的连接。或者直接用浏览器尝试访问其他大型网站。如果不能建立与其他网站的连接，则网络接入有问题。

(2) 发送HTTP请求到网站：用户首先会通过DNS获取服务器地址，然后发送HTTP请求到对应的IP。需要依赖用户能否正确获取网站IP地址。检验方式可以是：在用户端利用抓包软件，例如WireShark，tcpdump等，观察是否有HTTP请求发送到网站服务器。如果没有发送HTTP请求或目的地IP有问题，则DNS可能有错。

(3) 网站发送数据包给用户：这一步需要网站接收到HTTP请求，并且将对应数据传回给用户。需要依赖网站能否收到HTTP请求以及对于HTTP请求的处理是否正确。检验方式可以是：在服务器端通过log判断是否有新用户接入，接入请求的处理是否正确，以及发送给用户的数据是什么。如果网站没有收到请求，则服务器端的网络可能有问题。如果服务器无法处理HTTP请求或抛出异常，则服务器的实现可能有问题。

(4) 用户浏览器显示页面： 这一步需要用户接收到网站发回的数据，浏览器解析数据并显示页面。需要依赖于用户能否收到数据，以及收到的数据是否能够被浏览器正确解析及显示。检验方式可以是：在用户端利用抓包软件，观察是否有来自服务器的数据。一般来说，如果用户用的是商用浏览器，即能够正确解析数据。故如果能收到服务器数据但是不能正常显示，我们可以认为服务器的数据有问题。

## 工具箱

### GNU调试器命令

1. Compile with GDB support: gcc -g prog.c -o prog.x;
2. Start debugging: gdb prog.x , (gdb) run;
3.  Handle breakpoints: (gdb) break prog.c: 6 or (gdb) break my_func; if, continue, step, next; delete;
4. Watch variable: (gdb) `print my_var`, (gdb) `watch my_var`, (gdb) x (address of var);
5. Other utilities: (gdb) backtrace, (gdb) finish.

### 测试的方法

**AB Testing**

AB测试是一种对比测试方案。测试人员对于不同用户随机生成两种方案，例如，某些用户看到的网页按钮是圆形的，其他用户看到的网页按钮是方形的。通过用户对于不同测试方案的反应，来决定最终部署哪种方案。具体请参考：
http://en.wikipedia.org/wiki/A/B_testing

**Black Box Testing**

黑箱测试主要用于测试程序的功能，而不是内部结构或运作。测试者秩序知道输入以及对应的输出，就可以生成测试数据。黑箱测试的目的在于快速检测程序的功能性。特别地，黑箱测试还应该包括非法的输入数据，以确保程序不会崩溃。

White Box Testing
与黑箱测试相对，白箱测试主要用于测试程序的内部结构或运作。测试人员需要从程序设计的角度生成测试案例：输入测试数据并验证程序按照既定的流程执行。

### 工业界测试流程

**Unit Test**

优良的软件设计强调模块化，即模块之间通过API进行交互，每个模块负责实现相对独立的功能。单元测试的目的在于对于每个模块设计相应的测试数据，用以检验模块的功能。通常，单元测试采用黑箱测试，通过运行脚本完成。测试人员将测试数据输入脚本，将输出结果与期望的输出数据进行比较。单元测试不仅仅可以用于新模块的开发，还可以用于对于已有模块的更新，维护。对于模块的每次更改都应该运行相应的单元测试以确保功能的完整性。

**Alpha Test**

Alpha测试通常是阶段性开发完成后开始进行。主要是面向内部开发人员，在模拟环境中输入模拟的数据进行测试，以验证系统符合使用者以及设计者的需求。

**Beta Test**

当Alpha阶段完成后，可以进入由公众参与的beta测试阶段。Beta测试通常使用真实的运行环境，并且使用实际数据进行测试，以确认系统效率。测试的主要目的在于进一步测试及完善功能。

---

## What the Interviewer Is Looking For

+ Big Picture Understanding
+ Knowing How the Pieces Fit Together
+ Organization
+ Practicality

## Testing a Real World Object

1. Who will use it? And why?
2. What are the use cases?
3. What are the bounds of use?
4. What are the stress / failure conditions?
5. How would you perform the testing?

## Testing a Piece of Software

1. Are we doing Black Box Testing or White Box Tesing?
2. Who will use it? And why?
3. What are the use cases?
4. What are the bounds of use?
5. What are the stress conditions / failure conditions
6. What are the test cases? How would you perform the testing?

## Testing a Function

1. Define the test cases
	+ The normal case
	+ The extremes
	+ Nulls and "illegal" input
	+ Strange input
2. Define the expected result
3. Write test code

## Troubleshooting Questions

1. Understand the Scenario
2. Break Down the Problem
3. Create Specific, Manageable Tests


