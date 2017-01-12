# 基本功能使用指南


<!-- MarkdownTOC -->

- Nomadic 启动
- 安装指南
- 导入Kindle书摘
- 导入Evernote笔记

<!-- /MarkdownTOC -->

## Nomadic 启动

    nomadic-d

    nomadic browse

## 安装指南

安装 igraph 的时候在 mac 下直接 `pip install python-igraph` 会在编译 C core 的时候出问题，所以最好用 `homebrew` 事先安装好所有的依赖

    brew install homebrew/science/igraph
    pip install python-igraph

然后就可以了

安装 cairo 因为 mac 自带老版本，需要告知新版本位置

    export PKG_CONFIG_PATH=/usr/local/Cellar/cairo/1.14.0/lib/pkgconfig/:/opt/X11/lib/pkgconfig

    export PYTHON=/usr/local/opt/python/bin/python2.7

用 igraph 失败，改用 networkX



## 导入Kindle书摘

+ `kindle.py`、`Notes文件夹`和`Import文件夹`在同一层级
+ 执行 `python kindle.py` 就可以自动生成对应书摘，并导入到`Notes/kindle文件夹`中

## 导入Evernote笔记

+ 先导出Evernote中的指定笔记本，选择html格式，会得到一个文件夹
+ 把整个文件夹放入到`Import文件夹`中
+ `python evernote.py`即可
+ 图片会自动重命名好
