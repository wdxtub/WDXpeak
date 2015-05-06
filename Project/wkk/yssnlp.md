# YSSNLP 会议笔记

找一些可以参考的方向来做毕业设计

<!-- MarkdownTOC -->

- 慕课：自然语言处理的一个新舞台
- 移动互联网时代自然语言的创新
	- NLP 2.0 研发策略
	- 自然语言处理的基本问题

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

_周明, MSRA_

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
	+ 当前句子NLP -\> 考虑历史 -\> 考虑时间地点设备 -\> 考虑使用人

**统计自然语言处理**

θ* = argmaxθ SOME.CRITERION(W,S,θ)

θ = argmaxθ SOME.CRITERION(W,S,θ)

+ 建模：计算预测结果的概率或者得分的方法
	+ P(W|S) = Pθ(W|S)
+ 训练：利用训练数据估计所用模型的参数权值
	+ θ* = argmaxθ SOME.CRITERION(W,S,θ)
+ 预测：对输入数据求一个最佳概率或者得分的结果
	+ W* = argmaxWPθ(W|S)
+ 上下文模型：考虑时间地点人物历史
	+ W* = argmaxWPθ(W|S, Location, Entity, History)