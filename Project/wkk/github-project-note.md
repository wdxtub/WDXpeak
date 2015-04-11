# Github 上相关项目总结记录

## html2txt 转换指定网页为 markdown 文档

html2text is a Python script that converts a page of HTML into clean, easy-to-read plain ASCII text. Better yet, that ASCII also happens to be valid Markdown (a text-to-HTML format).

亲测可用，还比较简单，容易集成到项目中

### penlican 静态网站生成器

需要按照指定的方式进行编辑，具体还没有尝试，比较大型

Pelican is a static site generator, written in Python, that requires no database or server-side logic.

### grip 即时预览 markdown 文档

Preview GitHub Markdown files like Readme locally before committing them.

可以考虑使用渲染markdown的那部分代码

### Letterpress 小型的基于markdown的博客系统

Letterpress is a minimal, Markdown based blogging system written in Python.

支持的东西还比较全，可以考虑试试看

## mistune markdown渲染成html

The fastest markdown parser in pure Python, inspired by marked.

简单易用

### voldemort 简单的静态网站生成器

A simple static site generator using Jinja2 and Markdown templates.

看起来比较轻量

## rux 也是一个网站生成器

Micro & Fast static blog generator (markdown => html)

## ghmarkdown 可以即时也可以离线的 markdown 转 html

The complete command-line tool for GitHub-flavored markdown. It provides a convenient interface for the API provided by GitHub.

看用法和效果感觉还不错

## PyMarked markdown->html

A markdown parser and compiler, written in Python, translated from marked which written in javascrpt.

支持特性比较多

## mkdwiki2 把wiki页面转换成markdown

Write wiki in GitHub Flavored Markdown

感觉不错，可以有

## python-markdown2 功能超强大的转换器

markdown2: A fast and complete implementation of Markdown in Python

最多 star，感觉值得信赖

## snownlp 中文分词

SnowNLP是一个python写的类库，可以方便的处理中文文本内容，是受到了TextBlob的启发而写的，由于现在大部分的自然语言处理库基本都是针对英文的，于是写了一个方便处理中文的类库，并且和TextBlob不同的是，这里没有用NLTK，所有的算法都是自己实现的，并且自带了一些训练好的字典。注意本程序都是处理的unicode编码，所以使用时请自行decode成unicode。

很靠谱，可用

+ 中文分词（Character-Based Generative Model）
+ 词性标注（TnT 3-gram 隐马）
+ 情感分析（现在训练数据主要是买卖东西时的评价，所以对其他的一些可能效果不是很好，待解决）
+ 文本分类（Naive Bayes）
+ 转换成拼音（Trie树实现的最大匹配）
+ 繁体转简体（Trie树实现的最大匹配）
+ 提取文本关键词（TextRank算法）
+ 提取文本摘要（TextRank算法）
+ tf，idf
+ Tokenization（分割成句子）
+ 文本相似（BM25）
+ 支持python3（感谢erning）

## TextGrocery 另一个中文分词

TextGrocery是一个基于LibLinear和结巴分词的短文本分类工具，特点是高效易用，同时支持中文和英文语料。

## notes 最接近我想要的产品形式的project

## note 另一个很不错的project

## pynote 类似笔记管理

需要测试

## nomadic 这个很好！要试试

可以作为我的项目的基础




## pyspider 一个爬虫

A Powerful Spider(Web Crawler) System in Python. 
