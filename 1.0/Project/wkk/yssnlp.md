# YSSNLP 会议笔记

找一些可以参考的方向来做毕业设计

<!-- MarkdownTOC -->

- 慕课：自然语言处理的一个新舞台
- 移动互联网时代自然语言的创新
    - NLP 2.0 研发策略
    - 自然语言处理的基本问题
    - 自然语言处理的延伸
    - 多智能处理
- 阿里巴巴大数据实践只自然语言处理
    - 知识图谱
    - 用户标签挖掘
- 互联网+ 背景下的 NLP+
    - MLF Algorithms and Features
- 一种结构化数据标注方法：部分标注与原子任务
- 面向大规模开放域知识库问答系统

<!-- /MarkdownTOC -->


## 慕课：自然语言处理的一个新舞台

_孙茂松, 清华, sms@tsinghua.edu.cn_

+ 2012 MOOC 元年

相关研究研究方向

+ Automated scoring/evaluation for written student responses
	+ Content analysis for scoring/assessment
	+ Analysis of the structure of argumentation
	+ Grammatical error detection and correction
	+ Discourse and stylistic analysis
	+ Plagiarism detection
	+ Machine translation for assessment, instruction and curriculum development
	+ Detection of non-literal language (e.g., metaphor)
	+ Sentiment analysis
	+ Non-traditional genres (beyond essay scoring)
+ Intelligent Tutoring (IT) and Game-based assessment that incorporates NLP
	+ Dialogue systems in education
	+ Hypothesis formation and testing
	+ Multi-modal communication between students and computers
	+ Generation of tutorial responses
	+ **Knowledge representation in learning systems**
	+ **Concept visualization in learning systems**
+ Learner cognition
	+ Assessment of learners’ language and cognitive skill levels
	+ Systems that detect and adapt to learners’ cognitive or emotional states
	+ Tools for learners with special needs
+ Use of corpora in educational tools
	+ Data mining of learner and other corpora for tool building
	+ Annotation standards and schemas / annotator agreement
+ Tools and applications for classroom teachers and/or test developers
	+ NLP tools for second and foreign language learners
	+ Semantic-based access to instructional materials to identify appropriate texts
	+ **Tools that automatically generate test questions**
	+ Processing of and access to lecture materials across topics and genres
	+ Adaptation of instructional text to individual learners’ grade levels
	+ Tools for text-based curriculum development
	+ E-learning tools for personalized course content
	+ Language-based educational games

学科交叉研究

+ 语言信息处理
+ 机器学习
+ 人机交互
+ 教育学
+ 认知心理学
+ 计算教育学

重要分支：支持大规模在线教育的自然语言处理

## 移动互联网时代自然语言的创新

_周明, MSRA, mingzhou@mircosoft.com_

### NLP 2.0 研发策略

点对点的创新 + 把互联网当作研究平台 + 快速实施 + 跨学科合作

方向 | 组件 | 组件 | 组件 | 组件 | 组件
--- | --- | --- | --- | --- | ---
贡献 | 重要算法 | 原型 | 数字生活/工作产品 | 商业模式 | 人才
合作 | 多学科交叉 | 校企合作 | 跨部门合作 | 市场/营销 | 生态系统
市场 | 用户行为分析 | 市场分析 | 商业模式 | 用户服务 | 未来判断
互联网 | **网络挖掘** | **知识获取** | **模型训练** | 快速实施 | 用户反馈
NLP技术 | **分词/词性** | **句法语义分析** | 机器翻译 | **信息抽取** | **问答系统**

### 自然语言处理的基本问题

+ 汉字信息处理
	+ 字形、字库、编码、排版、显示、打印
+ 中文理解
	+ 分词、词性、句法、语义、篇章、分类、知识库、聚类、检索、问答、文摘、生成、对话、词典、辅助教学、语音识别和合成、OCR、辅助阅读和写作
+ 跨语言信息处理
	+ 在线词典、机器翻译、语音翻译、第二外语学习、跨语言检索、跨语言文摘、跨语言问答、跨语言知识库翻译和合成

### 自然语言处理的延伸

+ 与文化结合
	+ 对联、诗词、歌词、猜谜、文字游戏、书法、易经
+ 多媒体结合
	+ 文字-画/音乐转换、文字与画匹配、地图、漫画、音乐制作
+ 手势识别
	+ 手语/盲文的处理、识别、合成与翻译
+ 智能设备控制
	+ 手机助手、机器人、智能汽车、智能家居
+ 大数据
	+ 各类数据的搜集、加工、存储、索引、服务、更新、数据采集、挖掘、分析预测和商业智能
+ 电子商务
	+ 卖家工作站、云客服、导购助手、客服系统、广告、推荐
+ 其他应用
	+ 舆情分析、信息安全、医疗、教育、银行、金融等

**语音/口语语言处理**

+ 语音自然语言处理
+ 标点的恢复
+ 文本正则化处理

**Context-Aware 自然语言处理**

+ 上下文有关的理解
	+ 冬天能穿多少穿多少 vs 夏天能穿多少穿多少
	+ 单身的来由：原来是喜欢一个人 vs 现在是喜欢一个人
	+ 剩女产生的原因：一是谁都看不上 vs 一是谁都看不上
+ 句子、篇章、上下文感知
	+ Input: 当前句子和以前的 n-1 句子
	+ Output: 当前句子的翻译
	+ 当前句子NLP -> 考虑历史 -> 考虑时间地点设备 -> 考虑使用人

**统计自然语言处理**

+ 建模：计算预测结果的概率或者得分的方法
	+ P(W|S) = Pθ(W|S)
+ 训练：利用训练数据估计所用模型的参数权值
	+ θ* = argmaxθ SOME.CRITERION(W,S,θ)
+ 预测：对输入数据求一个最佳概率或者得分的结果
	+ W* = argmaxWPθ(W|S)
+ 上下文模型：考虑时间地点人物历史
	+ W* = argmaxWPθ(W|S, Location, Entity, History)

### 多智能处理

+ 数据智能
	+ 大规模、多样化、新鲜的数据
	+ 云计算基础设施
	+ 机器学习
	+ 数据驱动的系统
+ 知识智能
	+ 知识库、词典、规则、推理
	+ 知识驱动的系统
+ 社会智能
	+ 网页锚文本
	+ 各种用户标签
	+ 用户日志
	+ 用户反馈
	+ 社区问答
	+ 社会关系网络
	+ 人类计算

**知识库及建立**

Knowledge Base | # of KB Entity | # of KB Triple
---|---|---
微软、谷歌、百度、搜狗 | 未公开 | 未公开
Freebase [Jan. 2013] | 22M | 100M
Yago [Jan. 2013] | 10M | 120M
DBpedia [Jan. 2013] | 3.77M | 430M

+ 知识来源
    + 结构化数据：IMDB, Facebook, LinkedIn
    + 半结构化数据：网页表格、维基百科
    + 无结构化的数据：网页文档
+ 知识抽取技术
    + 自动生成 wrapper，譬如从网页中爬
    + 词汇模板 (Hearst Patterns)
    + 基于分布的相似度计算语义相似词
    + Bootstrapping，用一些种子，生成模板，再爬
    + 人工检查和校正

**社会智能挖掘**

+ Tweet
    + Spam filter, Classification, Tweet quality, Entity extraciton, Sentiment analysis
+ User
    + Zombie fans detection, User profile, Social impact index, Expert finding, Yellow page of users
+ Tweet collection
    + Clustering, Topic detection, Event extraction, Summarization, Social search

## 阿里巴巴大数据实践只自然语言处理

+ 深度学习
    + DNN, CNN, RNN, W2V, RBM, DBN
+ 分词、词性标注、命名实体识别、句法分析、N-gram、语义分析、情感分析
+ Map Reduce, MPI, Parameter Server
+ CPU集群(云梯), GPU 集群

典型应用分享

+ 知识图谱
+ 全网用户兴趣挖掘

### 知识图谱

+ 知识库(核心)
    + 基础数据库
        + 词库：同反多义词、相关词、上下位
        + 句库：实体描述、句法分析、情感语句
        + 度量库：重要度、相似度、词间关系
    + RDF 数据库
        + 实体库：品牌、产品、商品、买家、卖家
        + 属性库：单独属性、列举属性、关联属性
+ 信息抽取(输入)
    + 数据融合：度量、对齐、冲突消解、缺失补齐、简单推理
    + 结构化数据挖掘、半结构化数据挖掘、非结构化数据挖掘、热点
+ 数据处理(输入)
    + 数据监控、数据抓取、数据筛选、数据标注
    + 内网数据、外网数据

### 用户标签挖掘

+ 用户画像
+ 基于特征识别的用户分类
+ 用户单日兴趣标签
+ 用户短期兴趣标签
+ 用户长期兴趣标签

## 互联网+ 背景下的 NLP+

_汤步洲, tangbuzhou@gmail.com_

### MLF Algorithms and Features

+ ML Algorithms
    + Conditional Random Fields (CRFs)
    + Support Vector Machines (SSVMs)
+ Features
    + Bag-of-word
    + Syntactic information (e.g., POS)
    + Document structure (e.g., sections)
    + Domain knowledge(e.g., dictionaries)
    + Word representations (i.e., Brown Clustering)

## 一种结构化数据标注方法：部分标注与原子任务

partial annotation and atomic task

_李正华, 苏州大学 hlt.suda.edu.cn_

目前 NLP 的瓶颈

+ 传统标记数据年代久远
+ 需要面向网络文本，标注一定规模的评价和训练数据

近期工作

+ 依存句法
    + Google Web Treebank(Petrov and McDonald, 2012)
    + Twitter (Kong et al., 2014)
    + Weibo (Wang et al., 2014)
    + 哈工大 6 万句传统领域依存树库(LDC)
    + 哈工大数据堂合作标注的 5 万句微博依存树库
+ 分词词性
    + CIPS-SIGHAN 2012 微博分词评测
    + NLPCC 2015 微博分词词性标注评测任务

标注数据需要回答的一些问题

+ 标注哪些数据，如何选择
+ 如何制定标注规范
+ 如何标注，如何设计标注任务
+ 结构化数据标注质量如何保证
+ 标注后，如何和传统数据一起训练

## 面向大规模开放域知识库问答系统

问答系统分类：

+ IR-based QA: 基于关键词匹配 + 信息抽取，仍然是基于浅层语义分析
+ Community QA: 依赖于网民贡献，问答过程仍然依赖于关键词检索技术
+ KB-based QA: Knowledge Graph

知识库问答关键问题

+ 自然语言问句改写为结构化查询语句
    + 基本步骤：Which software has been developed by organizations founded in California, USA?
    + 短语检测：software, developed by, organizations, founded in, California
    + 资源映射：dbo:Software, dbr:developer, dbo:Company, dbr:foundationPlace, dbo:California
    + 语义组合：<dbo:Sotware, dbr:develper, dbo:Compnay>, <dbo:Company, dbr:foundationPlace, dbo:California>
    + 查询生成： SELECT DISTINCT ?url WHERE { <condition1>, <condition2>, ...}
+ 大规模开放域知识图谱带来的挑战
    + 大规模、开放域
        + 实体链接 Entity Mention
        + 关系发现 Relation Pattern
            + 看做一个分类问题
            + 需要 NLP 工具分析词性、句法等
            + 错误累积、语言依赖
            + 需要标注数据
            + 大规模开放域知识库下难以获得充足标注
        + 传统方法：同义词词典、人工关系模板
    + 自然语言问句表达多样、富含歧义
        + 短语切分歧义，资源映射，组合歧义
        + 如何消除歧义？
        + Joint Disambiguation using Markov Logic Network
    + 知识库多源异构
        + 很多场景下，单单只用一个知识库的信息不能完全回答用户的问题
        + 例如：谁出演了《变形金刚》并且和《Monkey Business》的演唱者结婚了
        + 电影知识库、音乐知识库、人物知识库都用到了
        + 先对齐再问答
            + 对齐有错误的话，错误会积累传递
            + 知识库是快速迭代更新的，对于问题的回答并不需要知识库中所有节点的对齐，只需要触发一个子图
        + 联合模型
            + 知识库对齐的结果影响问句分析
            + 问句的分析结果对于知识库对齐有影响
        + Joint Inference
            + 问句语义解析
            + 知识库对齐
            + Integer Linear Programming
+ 更多挑战
    + 不完备：需要知识推理
+ 知识推理
    + 逻辑推理
        + 人工规则不适用
        + 自动学习高阶规则性能差
    + 基于表示学习的知识推理
        + 推理过程 -> 相似度计算
+ 知识库表示学习
    + 学习实体、类别、关系的向量表示
    + 难点：一对多、多对一、多对多、可反关系

