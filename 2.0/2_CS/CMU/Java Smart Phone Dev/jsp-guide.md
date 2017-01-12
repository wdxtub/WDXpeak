# JSP 学习指南

For Project 1 Unit 5 & 6

<!-- MarkdownTOC -->

- 开发环境搭建
	- Java
	- Tomcat
	- Eclipse
- 整体概念理解

<!-- /MarkdownTOC -->


## 开发环境搭建

Mac 10.11 El Capitan

### Java

系统已经不自带 Java，所以需要自己安装。这里比较简单，略。

### Tomcat

1. 下载 [Tomcat](http://tomcat.apache.org/)
2. 解压，并将文件夹命名为 Tomcat 并将文件夹移动到根目录/Library中，安装过程便完成了
3. `sudo chmod 755 /Library/Tomcat/bin/*.sh`
4. 进入 `/Library/Tomcat/bin/` 文件夹
	+ 开启服务器 `./startup.sh`
	+ 关闭服务器 `./shutdown.sh`
5. 开启服务器后访问 `localhost:8080` 应该就可以看到 Tomcat 的欢迎页面

### Eclipse

1. 首先确保已经做好之前的 Tomcat 安装和配置工作，Library 中 link 好了 Tomcat。
2. 确保 Eclipse 处于 Java EE 模式下，选中我们的项目，点选底部框中的 Servers 标签页，创建一个新 Server。
3. Apache -> Tomcat (v7.0) Server -> Next -> 设置 Tomcat 安装路径 -> 如有需要，设置 JRE 版本 -> Finish
4. 选择 new => other => Dynamic Web Project ,按要求填写项目信息，假如工程名字为Servlet，一直next，知道最后勾选添加web.xml,finish。

实现第一个servlet实例，New => Servlet ,输入如下代码

```java
 package servlet;

 import javax.servlet.http.HttpServlet;

 public class Hello extends HttpServlet {

	private static final long serialVersionUID = 1L;
	public void doGet(HttpServletRequest request, HttpServletResponse response)
	 		throws IOException, ServletException {
		response.setContentType("text/html");
		PrintWriter writer = response.getWriter();
		writer.println("Hello");
	}
 }
```

打开 WebContent -> WEB-INF -> web.xml, 增加servlet

```xml
<servlet>
  <servlet-name>HelloWorld</servlet-name>
  <servlet-class>servlet.HelloWorld</servlet-class>
</servlet>
<servlet-mapping>
	<servlet-name>HelloWorld</servlet-name>
	<url-pattern>/Hello</url-pattern>
</servlet-mapping>
```

其中 servlet-class 是确定的，而servlet-name则可以自己命名。

接下来可以运行了，不过要怎么做呢？很简单，选中工程，run as 选择server，然后打开浏览器输入 `127.0.0.1：8080/HelloWorld` or `127.0.0.1：8080/Hello`

这里注意 mapping 中的 servlet name 务必要和 servlet 中的 servlet name 一致

如果 server 无法启动，那么可以用以下方法解决

1. Clean project & server OR
2. Remove .snap file from this directory <workspace-directory>\.metadata\.plugins\org.eclipse.core.resources OR
3. Remove temp file from this directory <workspace-directory>\.metadata\.plugins\org.eclipse.wst.server.core

当然更多是要注意 console 中给出的错误信息来进行改正

## 整体概念理解

这一章的题目要求非常不清晰，给人的感觉是对着已经写好的代码，反推需要做的事情，这样带来的问题在于：刚拿到要求的时候简直连怎么开始都不知道。然后老师也非常科学的强行停课一周。所以都要靠自己了。

要完成这次的作业，首先需要理解的是我们最终需要什么东西：

1. 我们在上一章完成的 server 端
2. 我们在上一章完成的 client 端
3. 两个 servlet 用于实现上一章 client 端的部分功能

那么这些东西要怎么组织呢？首先意味着要运行这次的 project，我们需要两个 server，一个是上一章写的 server，用于保存所有的 model。另一个是用 Tomcat 搭建的本地 server，这个是给 servlet 跑的。然后 client 做什么呢？唯一的功能就是在启动我们上一章完成的 server 之后上传几个 car model 供我们的 servelt 获取和显示。

知道了这些之后，接下来需要理解的是 servlet 的工作模式。servlet 是什么这里不多说，简而言之就是服务器上跑的小程序。不同于我们原来的函数调用，Tomcat 的机制是：

1. 访问一个网址
2. 找到对应的 servlet
3. 执行 servlet 里的 `doGet()` 或者 `doPost()` （根据不同的传入调用模式）
4. 根据这两个方法中返回的 html 内容来展示页面。

所以我们要做一个页面来展示 car model 的信息的话：

1. 创建一个 servlet
2. 通过 `@WebServlet("/ConfigurePage")` 类似这样的修饰符来把一个 servlet 绑定到不同的 url 上
3. 访问对应 url 时相当于执行 servlet 中的 `doGet()` 函数

那么问题就来了，JSP 到底是干什么的。我的理解，JSP 其实是对显示内容的再次封装。为什么这么说，原则上看，其实我们可以把所有的输出内容(html)在 `doGet()` 中 `print` 出来，可是这样逻辑代码和输出样式混在一起，一不好改二不好看三不合理。所以就有了另一个办法——JSP。我们可以基本上用 html 代码来制作网页，在需要动态内容的地方插入 jsp 相关的标记符，然后显示的时候就交给 jsp 来处理数据和样式的显示。

具体的 jsp 语法这里略过，网上还是有不少教程的。知道了这些大概就可以完成这次的作业了。



