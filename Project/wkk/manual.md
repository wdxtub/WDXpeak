# 基本功能使用指南


<!-- MarkdownTOC -->

- 导入Kindle书摘
- 导入Evernote笔记

<!-- /MarkdownTOC -->



## 导入Kindle书摘

+ `kindle.py`、`Notes文件夹`和`Import文件夹`在同一层级
+ 执行 `python kindle.py` 就可以自动生成对应书摘，并导入到`Notes/kindle文件夹`中

## 导入Evernote笔记

+ 先导出Evernote中的指定笔记本，选择html格式，会得到一个文件夹
+ 把整个文件夹放入到`Import文件夹`中
+ `python evernote.py`即可
+ 图片会自动重命名好
