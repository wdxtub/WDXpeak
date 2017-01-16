# Ansible 指南

最近在接入公司各个研发部门的日志，方便统一管理和分析，但是一台一台机子配置的话实在非常刀耕火种，所以还是要学习一下自动化运维工具。考虑到我对轻量级工具的偏爱，Ansible 就成了当仁不让的选择。

---

## 介绍

Ansible 基于 Python [paramiko](http://www.paramiko.org/) 开发，是一个简单的运维管理工具，用来自动化部署应用、配置、编排任务等，可以通过 SSH 或 ZeroMQ 连接主机

五个部分组成

+ Ansible: 核心
+ Modules: 核心模块与自定义模块
+ Plugins: 各类插件
+ Playbooks: 多任务配置文件，由 Ansible 自动执行
+ Inventory: 管理主机的清单

架构简单、依赖少，只要有 ssh 便可以工作；学习曲线平滑，上手比较容易；模块丰富，满足需求


## 安装

默认使用 SSH 协议管理节点，要求 Python 2.7。

Ubuntu 安装

```

## 优化

性能问题优化：

+ 开启 ssh 参数, pipelining 和 control persist
+ 优化 playbook，除去非必要模块，减少远程依赖
+ callback 模块异步化，Ansible 自身会等 callback 结束之后才执行后续命令，这点可以大大降低高并发时的耗时
+ 将需要网络传输的操作，如安装软件报、拉取 docker 镜像等，内置到镜像中

## 参考链接

+ [paramiko](http://www.paramiko.org/)
+ [Ansible入门](https://www.gitbook.com/book/ansible-book/ansible-first-book/details)
+ [Ansible中文权威指南](http://ansible-tran.readthedocs.io/en/latest/)
+ [Ansible 简易教程](https://blog.goquxiao.com/posts/2015/09/01/ansible-simple-tutorial/)
+ [Ansible 快速入门](http://cn.soulmachine.me/blog/20140127/)


