# 功能开发方向

首先要明确的是这是一个 本地的 基于markdown文法的 致力于构建个人知识网络的应用。那么需要的功能大致如下：

+ 流程
    * 收集(人工收集 RSS提取 Wiki抓取 新闻抓取)
    * 完善(人工完善 Inbox 类别检测 关键词提取 标签生成)
    * 整理(人工整理 语义分析 主题归类 笔记链接)
    * 总结(个人知识库构建 人工配制或自动生成)
+ Markdown 相关
    * 生成目录
    * 生成 epub/pdf/html
    * 定制 css
    * 支持数学公式
    * 支持多种文法扩展
+ 笔记系统 相关
    * 网页内容(wiki, books)转换为 markdown 格式
    * 不同笔记间的超链接
    * 主题笔记(knowledge 也就是一个主题里汇聚了相关笔记链接及信息的核心笔记)
    * 话题提取(关注的话题，每天自动更新对应的数据如RSS 微博 博客等等)
    * 自动标签
    * 自动关键词(TF-IDF与余弦相似性)
    * 找到类似/相关笔记
    * 基于约定而非数据库
    * 分区与类别(Inbox, Knowledge)的自动设定
    * !!笔记自动评分
    * 从 Evernote 导入笔记
    * 邮件推送
+ 实现细节
    * 中英文分词(NLTK, Jieba, 斯坦福中文分类器)
    * 词性标注(NLTK)
    * 文本分类(NLTK)
    * 本地网站界面(flask)
    * 电子书管理
    * 项目网站搭建
+ 高级功能
    * 根据笔记主题自动更新最新资讯(RSS Wiki News)
    * 根据笔记主题推荐书籍(Douban Amazon)
        - 评论内容的感情倾向和关键词提取
    * 知识结构图谱展示
    * 机器翻译的词对齐技术，自动提取关键词(比如「文件」、「使命召唤」，映射到「Windows」、「游戏」这些更适合做关键词的词上)
    * 笔记聚合
        - 按类目特征，拉取这个类目下的评论，进行分词，统计词频；
        - 对词进行聚类，包含常用的LDA，结合本体库，将词进行归类和分类，建立语料库；（分类是最重要的一步，比如服装类目下学院风、淑女、熟女、休闲等都会归为款式这类）
        - 属性情感搭配，建立属性词和情感词的连接关系，判断分句的情感；
        - 属性词+情感词转换到属性类的情感，对句子进行位置标记；
        - 将属性情感和位置标记结果build到搜索中，便于根据标签反向检索内容。
    * 多文本摘要技术 新闻聚合+提取关键句子
    * 电子书核心主题抽取
+ 书单
    * 数学之美
    * 统计自然语言处理基础
    * 统计学习方法 李航（自然语言处理和机器学习不同，机器学习依靠的更多是严谨的数学知识以及推倒，去创造一个又一个机器学习算法。而自然语言处理是把那些机器学习大牛们创造出来的东西当Tool使用。所以入门也只是需要涉猎而已，把每个模型原理看看）
    * 中文信息处理丛书：统计自然语言处理（第2版）宗成庆
    * 自然语言处理综论（Speech and Language Processing: An Introduction to Natural Language Processing, Computational Linguistics and Speech Recognition）
    * 机器学习实战哈林顿 (Peter Harrington)
    * Python自然语言处理
    * !!集体智慧编程
+ 工具包
    * pattern - simpler to get started than NLTK
    * chardet - character encoding detection
    * pyenchant - easy access to dictionaries
    * scikit-learn - has support for text classification
    * unidecode - because ascii is much easier to deal with
+ 工具
    * [CRF++](http://crfpp.googlecode.com/svn/trunk/doc/index.html)
    * [GIZA](https://code.google.com/p/giza-pp/)
    * [Word2Vec](https://code.google.com/p/word2vec/)
    * 词向量（ Distributed Representation）
    * 基本架构 分词=>词性标注=>Parser
    * 虽然这三模型可能学起来比较难，但是Tool用起来是轻松加愉快。Giza++是训练Translation Model的实现，CRF可以用到各种的序列标注问题上（例如分词，命名实体识别），Word2Vec，可以把一个词变成一个向量，如果两个词的上下文比较相似，则两个词的向量比较相似。
