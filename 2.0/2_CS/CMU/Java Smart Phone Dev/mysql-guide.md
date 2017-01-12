# MySQL 学习指南

第六次作业最难的部分在于配置环境和理解数据库的工作原理，配置好+明了原理，其实要写的东西就是比较按部就班的了。这个学习指南的目的是尽可能在最短的时间内帮助大家上手完成 18641 Project 1 Unit 6。大概分为：总体设计、环境配置、数据库原理以及相关实现细节。

## 总体设计

随着 Project 1 临近尾声，老师已经从打卡上班型变成了磨洋工型，无论是上课还是作业文档都走起了极简路线。这次的作业其实跟上一部分又没有太多关系了，什么 Tomcat 什么 Servlet 什么这个那个统统可以滚粗，根本毛都用不到。说到底其实就是在原来 server 的那个 project 里，写一个程序，和数据库连接，然后插入更新删除数据库中对应的条目即可。压根不需要启动什么 server，因为也没有任何 client 或者 servlet。

## 环境配置

我的环境是 Mac OS 10.11 El Capitan，然后 MySQL 的官网上连 10.10 的都没有，于是来[这里](http://dev.mysql.com/downloads/) 下载 `mysql-5.6.27-osx10.9-x86_64.dmg`

打开安装，完成之后在 System Preferences 里可以看到一个新的 MySQL 图标，然后在里面可以开启 MySQL

接着需要配置一下 root 密码

    cd /usr/local/mysql/bin
    ./mysqladmin -u root password 123456

这里 123456 就是设置的密码。然后会告诉你通过命令行搞密码不安全噢，不管，用自带的 client 连接数据库试试看

    ./mysql -u root -p
    123456

然后就可以看到命令行的界面了

    Welcome to the MySQL monitor.  Commands end with ; or \g.
    Your MySQL connection id is 73
    Server version: 5.6.27 MySQL Community Server (GPL)

    Copyright (c) 2000, 2015, Oracle and/or its affiliates. All rights reserved.

    Oracle is a registered trademark of Oracle Corporation and/or its
    affiliates. Other names may be trademarks of their respective
    owners.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

    mysql>

现在数据库正常运行了，我们需要知道怎么用 java 来操作数据库

Java 操作数据库需要用到 MySQL Community 提供的 Connector，反正就是一个封装好的连接器，俗称 jdbc，这里我用的是 `mysql-connector-java-5.1.37-bin.jar`

在 server 的文件夹下面新建一个 lib 文件夹，然后把这个 jar 放进去，再然后回到 eclipse 右键点击项目选择 properties 然后导入这个 jar 包。

在 main 函数中加入如下代码进行测试

```
String URL = "jdbc:mysql://localhost:3306";
String USER_NAME = "root";
String PASSWORD = "123456";

try{
    Connection connection = null;
    connection = DriverManager.getConnection(URL, USER_NAME, PASSWORD);
    if (connection != null){
        System.out.println("Connected to Database Successfully!");
    }

} catch (SQLException e) {
    // TODO Auto-generated catch block
    e.printStackTrace();
} finally {

}
```

没什么问题的话应该能看到数据库连接成功

## 数据库原理

了解一下各类范式即可，我是瞎设计的

## 实现细节

网上都有，略
