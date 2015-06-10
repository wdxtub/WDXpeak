# Personal Information Management based on Knowledge Graph

Da Wang, A.Prof. Chengying Gao

<!-- MarkdownTOC -->

- 中文概述
- 注意
- Abstract
- 摘要
- Chapter 1 Introduction
    - 1.1 Background
    - 1.2 Objectives
    - 1.3 Related Works
    - 1.4 Contribution
    - 1.5 Structure of this Thesis
- Chapter 2 Personal Knowledge Graph
    - 2.1 Introduction
    - 2.2 Knowledge Representation
        - 2.2.1 Entity Representation
        - 2.2.2 Relation Representation
        - 2.2.3 Resource Description Framework
    - 2.3 Building Knowledge Graph
        - 2.3.1 Complex System Theory
        - 2.3.2 Layer Model for Personal Knowledge Graph
        - 2.3.3 Search Strategy and Data Format
    - 2.4 Results
- Chapter 3 Note System
    - 3.1 Introduction
    - 3.2 Data Management
    - 3.3 Web UI
    - 3.4 Integrated with Knowledge Graph
        - 3.4.1 Note Labeling
        - 3.4.2 Tag Extraction
        - 3.4.3 Inverted Index
        - 3.4.3 Note Classification
        - 3.4.4 Similar Notes
    - 3.5 Results
- Chapter 4 Recommender System
    - 4.1 Introduction
        - Model-based Collaborative Filtering
    - 4.2 Data Acquisition and Parsing
    - 4.3 Integrated with Knowledge Graph
    - 4.4 Connected to Note System
- Chapter 5 Conclusion
    - 5.1 Comparison on Note System
    - 5.2 Comparison on Recommender System
    - 5.3 Future Work
- Bibliography
- Appendix A
- Acknowledgements

<!-- /MarkdownTOC -->



## 中文概述

高老师好，

前段时间因为要出国体检，顺德退宿还有各种同学聚会的缘故耽误了一点时间，这两天才终于把论文整理出来了，格式基本就是按照老师给我的论文参考来写，老师说要多一些数据对比，所以也花了比较多时间进行数据准备和不同方法的测试。考虑到英文看起来比较折腾，这里以提纲的方式大概整理每一章的内容，方便老师查看。

第一章 概述

1. 背景：个人信息管理系统的发展过程以及在互联网时代的新发展，引出知识图谱的概念
2. 目标：简要描述个人信息关系系统的大致目标：通过三大类应用的组合行程信息获取处理理解的闭环，方便用户进行知识转化
3. 相关工作：具体的文献综述，包括知识管理，自然语言处理以及知识图谱等相关的论文
4. 贡献：把原本比较大型的知识图谱应用在个人信息管理中，模仿互联网的知识体系结构，无需人为干预
5. 论文的结构：简要介绍每一部分的内容

第二章 知识图谱

1. 介绍：知识图谱的基本介绍以及现状
2. 知识表示：从哲学角度出发，引入到计算机领域的知识表示技术，包括实体表示，关系表示等相关概念
3. 构造知识图谱：受现有的知识图谱系统启发，基于复杂系统理论，提出了一种个人知识图谱的五层模型，利用维基百科的数据进行类别分类以及节点关系的构造
4. 结果：通过现有数据构造的个人知识图谱，约六百个节点，以及可视化图形

第三章 笔记系统

1. 介绍：现有笔记系统的优点及不足，主要以印象笔记为分析对象
2. 数据管理：利用纯文本以及 Markdown 文法来支持复杂格式的表示，利用文件夹来进行类别管理
3. 用户界面：基于 Python 以及网络框架 Flask 构造的网页客户端，可以进行搜索或以类别进行访问，以及支持一些其他的功能
4. 与知识图谱集成：介绍数据标注，标签提取，倒排索引，文本分类，查找相似笔记等相关技术的具体算法和使用
5. 结果：最终得到的比较完整的笔记应用

第四章 推荐系统

1. 介绍：推荐系统的相关介绍，包括推荐问题的定义以及常用方法，以及常见问题和评测指标
2. 数据获取：如何从豆瓣抓取数据并转换成 json 格式，并进行标签提取
3. 与知识图谱集成：与笔记系统类似，进行数据标注以及特征排名，针对不同类别书籍的评分差异以及可能的作弊情况进行评分标准化的处理
4. 与笔记系统连接：以知识图谱为轴把笔记和书籍信息通过基于知识图谱的推荐系统链接到一起

第五章 结论

1. 总体总结
2. 测试数据，测试方法和评测指标
3. 笔记系统的相关数据对比（kNN, SVM, F1, 训练时间和分类时间)
4. 推荐系统的相关数据对比(准确率，召回率，F1，新颖度，覆盖度，多样性)
5. 不足及未来工作

后面就是致谢和参考文献

麻烦老师了，我听说的最新消息好像是最后七月底才需要交论文，所以最近也会慢慢一边修改代码一边改进论文，争取做出满意的结果。


## 注意

+ 有些地方可能要配图
+ 不断慢慢补充吧，把中文资料大概都翻译过去
+ 公式之类的就把其他论文的搬过去，应该没有问题
+ 算法步骤图
+ 表格
+ 剩下的逐步完善

## Abstract

This paper presents an effective toolkit for personal information management(PIM). The development of this toolkit is based on the idea that new information retrieval methods and natural language processing methods can help people extract useful information when facing the information explosion/chaos/overload. With a automatic and unified information processing pipeline, this toolkit focuses on improving the effectiveness of three main PIM processes: get/retrieve, understand/analyze and connect/organize.

keywords:

## 摘要

关键词：

## Chapter 1 Introduction

### 1.1 Background

With the development of Internet and Information Technology, the problem of Information Explosion has arisen, that is, Rich Data and Poor Information. Nowadays it is easy for almost everyone to get all kinds of data from newspaper, television as well as social networks but the problem is: how can we turn those data into information and transform them into knowledge.

Personal Information Management(PIM) is the focus of many scholars in the area of Personal Knowledge Management(PKM) and it is the process to capture or locate knowledge as defined by Seufert et al.(2003). The data is transformed to information and vice versa in this process and it mainly deals with the past knowledge, as argued by Russell Ackoff (1989). Knowledge conversion is in the form of explicit knowledge (from one media, e.g. hard copy to another media, e.g. electronic copy), and is the combination process as suggested by Nonaka and Takeuchi (1995).

The PIM is the foundation of PKM, where individuals are able to create their own knowledge database for immediate or future use in this process. The required skills / competences in PIM are retrieving, evaluating and organizing, which are the skills playing significant roles in capture / locate knowledge.

As it is, we must answer one of the most important question about PIM, that is, how to arrange the information. The idea of Knowledge Graph is one of the options to be the rules for information management. However, nowadays most techniques used on knowledge graph focus on information retrieval but not for information management. They focus on identifying identities from the web sources and find connections between them. They treat this problem in a large scale and make it impossible to apply it on personal information management. This paper presents a method to build a simplified knowledge graph to finish the information management task such as text classification and information recommendation.

Nowadays the most famous product close to PIM is Evernote, a note application that can be used in almost every platform. But it can only meet the needs of getting/retrieving and arranging information. When it comes to understand and connect the information, it becomes useless as few natural language processing techniques are integrated in it.

So we need a tool to help us understand what our notes are and find connection between our notes as well as the other information in the Internet. That is to say, it is a tool that can figure out what areas we are focusing on and help us arrange those information based on its understanding a.k.a. the Knowledge Graph.

### 1.2 Objectives

The goal of this work is to present an system for a full circle in the fields of personal information management including getting, understanding, connecting and sharing information as well as knowledge. Based on the Knowledge Graph, a note system and a book recommendation system are built in order to test the efficiency and accuracy of the usage of the Knowledge Graph. Also, a web-based user interface and several import/export toolkits are built to help user browse their personal information and collect other information on mobile devices. All the source code in this work are open sourced.

### 1.3 Related Works

As the personal information management system consists of three main parts, that is, Personal Knowledge Management, Natural Language Processing and Recommender System, different works are presented by many scholars.

For personal knowledge management across computer and internet tools and technologies, Ismail and Ahmad [2] suggested four main processes: get/retrieve, understand/analyze, share/ publish, and connect (GUSC). The concepts are based on different reviews by Grundspenkis [3], Jarche [4], [5], Martin [6], Avery et al. [7], Pettenati et al. [8], and Razmerita et al. [9].

The PKM processes consist of four main tasks:

+ Get/Retrieve knowledge: online search, RSS feed, wikipedia, twitter, facebook, etc
+ Understand/Analyze knowledge: automatic summarization, relationship extraction, sentiment analysis, etc
+ Share knowledge: blog, RSS, wiki, twitter, facebook, etc
+ Connect to other Knowledge: similar notes/information, related books, etc

They have such a huge goal and want to build a complete and complex system to cover every part of the PIM/PKM process which makes the whole system too large to use for common user in daily life.

For natural language processing, the main problem is that most works are based on English.   In order to handle Chinese, some extra works are needed such as word segmentation [10]. Also, analyzing text is also an important task. TextRank [11], Automatic Summarization [12], Sentence Extraction [13] and Multi-Document Summarization [14] are some of the useful techniques. Most of them are integrated in powerful NLP toolkit such as NLTK [15].

Knowledge Graph is one of the most advanced and undergoing research fields nowadays, different companies have their own applications based on it, [16] [17] [18]. Also, many knowledge bases are built based on the concepts of ontology: Freebase [19], DBpedia [20], XPLORE [21] and WordNet [22]. For Knowledge Graphs in Chinese language, the most famous works are HowNet [23] and SSCO [24].

There are also many research on recommender system. Google [25] [26], Amazon [27] and Netflix [28] [29] are two of the most famous companies that widely use the recommender system in their product. Most recommender systems are based on the following mechanisms: LFM [30], SVD [31], context-aware recommendation [32], information aggregation [33], top-n recommendation [34] and knowledge-based recommendation [35] [36].

### 1.4 Contribution

In my work, based on Knowledge Graph, I build an effective toolkit for personal information management that can perform information aggregation and find connections between different information in order to help people turn rich data into rich information and knowledge. With the assists of the system, people can focus on the information itself as most of the data is filtered and hidden links between information are revealed.

The system consists of the following components:

+ A directory-based Note System using Markdown syntax powered by flask
+ A book recommendation System finding related books according to user’s notes
+ A personal Knowledge Graph generated from the internet data and user notes
+ Import/Export toolkits for connecting different devices and share in different ways

The novelty of the present work, compared to the previous ones, is that it use the Knowledge Graph to arrange all the information. With this graph data structure, it is more natural to find connection and give out recommendation using the information of current node and neighboring nodes. Also, as the knowledge graph is dynamic, it can learn to understand the user’s habits and be more effective and accurate if the user keeps on using it for some time.

And the philosophy in building the Knowledge Graph is to simulate the structure of knowledge generated by billions of people around the world which can be regarded as a self-organized complex system. No human-defined rules are used in building the knowledge graph so there are no fixed categories in this graph. As it is, it is highly flexible to change from time to time without further modification.

### 1.5 Structure of this Thesis

This thesis is divided into four main chapters.

Chapter 2 describes the basis concepts of knowledge representation and the construction procedure of the knowledge graph. Finally, some rendering result of the knowledge graph are put at the end of this chapter.

Chapter 3 is about the design and implementation of the note system. It contains how I arrange the data and display them in a web-based user interface. Also an introduction about how to extract the features and classifying text according to them will be given as well as how to find the similar notes based on knowledge graph.

Chapter 4 is about the design and implementation of the book recommendation system. The following introduction will be in this part: how to get the book information, how to extract features and attach them to different node in the knowledge graph, and how to build the recommender system based on knowledge graph.

Chapter 5 is the conclusion part which contains the comparison result of the text classification, related note discovery and book recommendation among different methods. The results shows that the method presented in this paper has better performance in finishing these tasks.

Appendix A is a brief user guide in installing and using the system.

## Chapter 2 Personal Knowledge Graph

### 2.1 Introduction

Knowledge Graph is a kind of semi-structured data set to represent and store human knowledge. In common sense the information center of knowledge graph is entity (or object) and each of them has several meta information including ontology, attribute, relationship and description.

So far, the knowledge graph databases built by human (Wikipedia, Freebase), in quality, coverage rate and precision rate, are much better than any other auto generated knowledge graph databases (NELL [37]￼￼, OpenIE [38], DeepDive [39]).

There are three types of information structures on the Internet: Structured, Semi-Structured and Plain text. The structured data has high degree of confidence but in small scale. The semi-structured data is not as accurate as structured data but there are more resources of them. Most data on the Internet are in plain text form. It is difficult to extract knowledge from them because of complexity and variety. We usually get knowledge from the structured and semi-structured data using record identification, pattern learning and attribute value extraction.

Most Knowledge Graph systems are treated as a basic component in searching engines such as Google, Baidu and SoSo. Their goals are to build a big complex graph containing as much knowledge as possible which in the meantime makes it impossible to apply it on personal usage.

In order to build the Personal Knowledge Graph, we need to find a way to model the knowledge of the world in an abstract way so that we will not be stuck in finding as much knowledge material as possible, instead we can focus on building the best structure of the  personal knowledge graph.

### 2.2 Knowledge Representation

We still don’t have a clear definition on what knowledge is and how to represent them. However, as the development of artificial intelligence as well as the Internet, we need a way to represent knowledge or at least, represent facts. That is to say, we must find a way to represent both entity and relationships.

#### 2.2.1 Entity Representation

概念三角形的配图 [Ogden, Richards, 1923]

In philosophy, ontology is the philosophical study of the nature of being, becoming, existence or reality, as well as the basic categories of being and their relations.

In computer science, an ontology is a formal, explicit specification of a shared conceptualization [40]. Conceptualization means an abstract model of phenomena in the world by having identified the relevant concepts of those phenomena. Explicitness means the type of concepts used and the constraints on their use are explicitly defined. Formality means the fact that the ontology should be machine readable. And finally, the adjective word shared means that ontology should capture consensual knowledge accepted by the communities.

We usually use quintuple O = \{￼ C, R, F, A, I \} to represent entity.

C means the set of concepts. R means the relations between concepts and instances. F represent functions, that is to say, the nth element of one relation is decided by the value of the other n-1 elements. A means axioms, usually used for knowledge reasoning and I means instances.

#### 2.2.2 Relation Representation

For different kinds of knowledge base, they have different strategies in representing the relationships between entities. They are Ontology, Taxonomy and Folksonomy.

Ontology uses tree structure and nodes from different layers have strict IsA relationship, for example, Human activities -> leisure activities -> sports -> golf. Because of the simplicity in relationships, it is easy for knowledge reasoning. However, the simple relationships between different layers limit the ability of representing complex relationships among concepts.

Taxonomy also uses tree structure but the nodes from different layers don’t need to be strict IsA relationship, instead, they are hypernym-hyponym relationship. For example: Places -> Milky Way Galaxy -> Solar Systems -> Inner Planets -> Earth -> Asia -> China -> Guangdong -> Guangzhou. Based on this kind of representation, taxonomy can represent complex concepts but this also make knowledge reasoning even more difficult and can’t avoid the redundancy of concepts.

Folksonomy is a user-defined tagging classification without layers. It is very flexible but as the lack of layers, it is difficult to represent the IsA or HasA relationship between different entities. Also, as the labels are generated by human, they may not be accurate or organized which makes knowledge reasoning tougher.

Most knowledge resources from the Internet(Wikipedia, Baidu Baike, Hudong Baike) uses the combination of Taxonomy and Folksonomy. But they can not cover all the relationships and the problem of redundancy as well as the lack of connections between the labels are problems that the scholars must solved.

#### 2.2.3 Resource Description Framework

Based on the concepts mentioned in the previous chapter, resource description framework, RDF, is invented to represent knowledge in computer science [41]. RDF represent entity in a simplified way using tetrad O = \{￼ C, I, T, P \}.

The data format of RDF includes Resource, Property and Statement. Resource means using URI to identify a resource uniquely and one resource usually stands for one thing. Property is a special kind of resource which is used for describing the relations between resources. Statement is a triad consisted of three kinds of resources: `ref:subject`, `rdf:predicate` and `ref:object`.

With the help of RDF, we can mapping the world knowledge from string to structured syntax description. And entities can be the concept model and the basis of logic reasoning. According to the specific needs, knowledge graph can be adjusted to describe different layers and granularities of abstraction of conception.

### 2.3 Building Knowledge Graph

There are some attempts in Chinese knowledge base construction. Hownet [42] and HNC [43] use complex topic model to build Knowledge graph. They all need huge human resources and can only model a small fields of knowledge. The description method for different subjects are also different which makes it impossible to extend to a large scale.

As it is, we must find a way to automatically construct ontologies and build corresponding knowledge graph. With the help of SSCO [24], in this work I build the knowledge graph based on Wikipedia. Although the contents of Wikipedia are not really machine interpretable, they contain much structured knowledge. Redirection pages, category systems, and InfoBox modules are excellent corpora for ontology learning.

However, most good-quality items in Wikipedia are in English. For Chinese language, we still do not have a large enough structured encyclopedias as good as English Wikipedia. Although we can find another two large Chinese encyclopedias called Baidu-Baike (http://baike.baidu.com/, a collaborative Web-based Chinese encyclopedia) and Hudong-Baike (http://www.hudong.com/, the world’s largest Chinese encyclopedia), their structures are not as good as Wikipedia for mapping pages into ontological form.

Also, the characteristics of the Chinese language are much different from English which determines that many techniques working on English [44] [45] can hardly be used in Chinese language. So I need a novel way to overcome the difficulties in building knowledge graph in Chinese.

#### 2.3.1 Complex System Theory

After observing the Internet world using webpage crawler, I found out that the webpages (or information) can be treated as a complex system which means that we can use the features of the complex system to simplify the acquisition of knowledge from the internet. Most knowledge from the internet contain lots of noises but with the help of the feedback of the system itself, most noises will be filtered away so we don’t have to spend plenty of time washing and cleaning our data.

A complex system is a damped, driven system  whose total energy exceeds the threshold for it to perform according to classical mechanics but does not reach the threshold for the system to exhibit properties according to chaos theory.

Complex adaptive systems (CAS) are special cases of complex systems. The reason for its complexity is that they are diverse and made up of multiple interconnected elements. It is adaptive in that they have the ability to change and learn from experience. We can see complex adaptive systems in our daily life such as the stock market, social insect, ant/bee colonies, the ecosystem, the immune system as well as any other systems consists of simple elements but when treated as a whole showing great complexity. Many large-scale online systems, such as collaborative tagging and social bookmarking system can be regarded as complex adaptive systems.

As it is, it is possible to build the knowledge graph based on complex system theory using the material generated from millions of people on the internet to build a complex adaptive system. It naturally has the magic mechanism of complex system. That is to say, consisting of dynamic network of multiplicity, it will be open and nested, have a memory and may produce emergent phenomena as well as feedback loops.

However, we still need some order to build the knowledge graph so as to have a clear view of the whole system while in the same time utilize the useful features of the complex system as much as possible.

#### 2.3.2 Layer Model for Personal Knowledge Graph

In order to build the knowledge graph with both the advantages of complex adaptive system as well as the clearness of the tree structure that normally used to represent knowledge graph, I design a five-layer model to represent the personal knowledge graph.

The first layer is the Root Layer which contains only one node called the root node. The root node is the parent node for every other nodes in the knowledge graph.

The second layer is the Field Layer. The nodes in this layer only have one parent node, the root node. That is to say, every node in this layer represents a specific knowledge field such as biology, society, history, technology and science, etc.

The third layer is the Transition Layer. The nodes in this layer can only have several parent nodes which are from the first and the second layer. It is called the transition layer because this is the last layer that has the strict node hierarchy. That is to say, any nodes beneath this layer will not have a clear definition of parent or child node.

The fourth layer is the Entity Layer. The nodes in this layer can only have several parent nodes which are from the second or third layer. There is no node hierarchy in this layer. That is to say, it can be treated as a complex adaptive system that are characterized by a high degree of adaptive capacity, giving them resilience in the face of perturbation.

The fifth layer is the Base Layer. In fact, nodes in this layer are the same as the node in the fourth layer except for one thing: they don’t have any other child nodes. This layer can be regarded as a trick in implementation so that when the system search the nodes in this layer, it knows that it is the end of the route and find other searching path.

#### 2.3.3 Search Strategy and Data Format

Using the category index page (http://zh.wikipedia.org/wiki/Wikipedia:%E5%88%86%E9%A1%9E%E7%B4%A2%E5%BC%95) as the root page, with the help of Scrapy(An open source and collaborative framework for extracting the data you need from websites in a fast, simple, yet extensible way), I can easily build the nodes in the first and second layer.

Each node in the second layer has its own classification page (for example Chinese History: http://zh.wikipedia.org/wiki/Category:%E4%B8%AD%E5%9B%BD%E5%8E%86%E5%8F%B2). Using Information from the webpage and pre-defined matching pattern, the system can build the nodes in the third layer accordingly.

In addition to this, for some items in the wikipedia, there are detailed structured table for the whole fields or areas. We also use this kind of information to find connections between different nodes.

这里要各种插图

In the end, with all the pages, nodes and connections we get from the internet, we store the nodes of the knowledge graph in a specific data format shown as followed:

这里是具体的数据结构，第一行是什么第二行是什么之类的

The system will load all the nodes and build the whole knowledge graph when initializing. The nodes in the second and the third layer will be the candidates for text classification (will be further introduced in Chapter 3) and the nodes in the fourth and fifth layer are used for knowledge reasoning and probability accumulation. Different keywords are from different nodes, the probabilities of these nodes will be transfer to their parent node thus the system can determine the category based on probability.

### 2.4 Results

For testing the efficiency of the design, I build a knowledge graph with 597 nodes and 651 edges. The detailed number of nodes in different layers are shown as followed:

插表格，每个 layer 的 node 数量

We can also visualized the graph with NetworkX (a Python language software package for the creation, manipulation, and study of the structure, dynamics, and function of complex networks). The big red circle is the root node and the blue ones represent the nodes in second layer. The green and small red ones are nodes from the third and fourth layer. The nodes in the fifth layer, as they are only a tricky representation in implementation, are not shown in the following figure.

插图

Now we have a complete knowledge graph and can test its performance using different kinds of applications. It is not as big as the complex system from big companies but has the same high level structure so that even though it is a simplified model, we can still have good performance on applications based on this personal knowledge graph

## Chapter 3 Note System

### 3.1 Introduction

The first application I built is a note system based on the personal knowledge graph. Similar to the famous cross-platform application Evernote, it provides basic note taking feature as well as other smart functions that Evernote doesn’t have such as import/export toolkit and automatic classification based on knowledge graph.

Evernote is one of the best note applications in the world. It support different devices from computer to mobile phone and arrange the notes with notebooks and tags. Several kinds of information can be attached with the note such as where and when you create the note, what is the last update time of this note and the historical version of the note. Each note can has its own attachment and share with other people with one click. What’s more, it is very convenient to import notes from the websites, wechat as well as email.

However, with all these advantages mentioned above, there are several disadvantages about Evernote, especially for programmers, they are:

1. We need the Evernote app to visit and edit our notes. If there is no Evernote application, you can not even see your note.
2. It is difficult to backup to the cloud service when the Internet is not available.
3. The editor of Evernote is not based on plain text, the format can only be used in the application itself.
4. Even though it provides exporting function, the formats of the document is limited. For example, it is difficult to send your note to your kindle.
5. Notes are notes, not knowledge. The algorithm in Evernote to find connections among notes are not smart enough which makes it more difficult to help people build their own knowledge framework.

The note system presented in this paper solve the above problems that make it inconvenient to use Evernote in a simple and elegant way. The system is built on python and plain text which makes it easy to support multiple platform without much effort. Each note is store in a text file and use directory to represent the concept of notebooks. That is to say, you can arrange your notes just put them in the same folder to tell the system that they are in the same notebook. Using this mechanism makes it clear even without the note system. User can visit their notes in any platform that has a file explorer. With the help of the python programmer community, importing, exporting, conversion can be easy tasks for everyone. After mapping the notes to the personal knowledge graph, the system can connect and extend the notes automatically to help user get deeper understanding about the notes.

### 3.2 Data Management

Most note system choose to use database as the storage method. However, as different platforms have different version of database (even the same database may act differently in mobile devices and computers). It is not a good choice to store everything in a database. Instead, the system presented in this paper with arrange notes and other data in plain text files along with directory. These are the basic components for any operating systems which makes sure that the system can work well even in a brand new machine without any installation or configuration.

The settings of the note system will be stored in a json file which tells the system where to find the notes and where to put the temporary files. For each note, you can just use it as normal plain text file or using the Markdown syntax (a markup language with plain text formatting syntax designed so that it can be converted to HTML and many other formats using a tool by the same name). Many websites support this format such as Github(http://www.github.com) and Quora(http://www.quaro.com).

这里插入一张对比图

Using this folder-based plain text mechanism, user can easily integrate the note system with different services provided by different Internet companies such as Dropbox(http://www.dropbox.com) and Github.

### 3.3 Web UI

As is mentioned above, the note application is implemented with python and flask, using direct mapping from folders to notebooks and files to notes. Anyone who knows how to use file explorer in any operating system can use it without learning effort.

Flask is a micro framework for Python based on Werkzeug, Jinja2 and good intentions. It is high flexible so that different features can be added to the system when needed without difficulties.

几个界面的图

It supports a simple directory structure of HTML, Markdown, txt, and pdf notes and any other files which may need to be referenced. It is also possible for users to have an easier way of searching through and browsing those files through either the command line or a simple web interface.

Here are the features that the note system supported:

+ Supports GitHub-Flavored Markdown
+ Supports MathJax syntax
+ Supports references to images and other files, and will automatically update those references if the files are moved
+ Full-text search (across html, txt, markdown, and even pdf files)
+ A rich text editor (in-browser) for dumping in web clippings (external images are automatically saved locally)
+ The rich text editor can convert and save HTML notes into Markdown
+ Auto-recompiling of Markdown notes and updating of whatever browser is viewing the note (i.e. live-ish previews)
+ Serves a browsable site of all your notes
+ Complete command-line interface
+ Export notes as portable presentations

### 3.4 Integrated with Knowledge Graph

Now that we have a completed note system, it is the time to integrate it with the personal knowledge graph described in Chapter 2. Personal Knowledge Graph can be treated as a kind of user profile as the weights between different nodes will change with the addition of notes.

In order to avoid the cold start problem in many machine learning system, some labeling work must be done before the integrating process can be finished. After that, the system will use algorithms based on entropy theory to extract the keywords of each note or use the bag of words model with the topic modeling method. With all the preparation work ready, the system will build the inverted index to accelerate the searching speed and use Naive Bayes method to finish the note classification task.

#### 3.4.1 Note Labeling

As the complex adaptive theory mentioned above, it is not a difficult task to label all the notes as the user just need to identify the related field of the notes and the system will learn the probabilities of them.

标注程序的图

Using the labeling program the user can label each note with ease. And after building the initial database of the personal notes, the system can classify the notes automatically.

#### 3.4.2 Tag Extraction

Before extracting keywords (or tags) from the note, as the target language in the system is Chinese, the first we need to do is word segmentation (Chinese characters don’t have space between words). The system uses word figure scanning method based on prefix dictionary to generate the directed acyclic graph(DAG) of all possibilities for the characters in a sentence that can form a word. Dynamic programming is also used here to find the route with the maximum probability and find the longest segmentation combination of words based on the frequencies of the words. For new or rare words that are not included in the dictionary (out of vocabulary word), the system use a Hidden Markov Model with Viterbi algorithm [46] which makes it possible to form new words based on probabilities.

After going through the pre-processing pipeline for Chinese, we can use the TextRank algorithm to extract tags from user’s notes. TextRank is a Graph-based ranking algorithm that uses the global information recursively drawn from the whole graph to decide the importance of each vertex in a graph. Inspired by the famous PageRank algorithm from Google, a graph-based ranking model can be treated as a voting or recommendation problem. That is to say, the connections between vertices have the same effect of voting. If a specific vertex has a large number of votes (many other vertices are connected to it), it is a natural way to regard it as an important vertex.

Now that we have those more important vertices, the importance of the vertex also affect how important the vote itself is. The vote from a more important vertex will have a higher value to represent its corresponding importance. After taking into account this information, we can have the whole ranking model to find the keywords of the notes.

For the implementation, after word segmentation, the system will separate the text into sentences based on a trained model. Base on the trained model and the results from word segmentation, the system will build a sparse matrix of words and the count it appears in each sentence. After that TFIDF method is applied for the normalization of each word while tf means the term frequency which represents how frequent a term occurs in a document and idf means inverse doc frequency which represents how important a word is.

With the TFIDF value it is possible to construct the similarity matrix between sentences and use PageRank algorithm to score the sentences in graph. Noted that the algorithm ranks the sentences with underlying assumption that “summary sentences“ are similar to most other sentences.

The last step is handling the stop words. In computing, stop words are words which are filtered out before or after processing of natural language data. Those words that normally used but without any contribution to the meaning of the sentences can be regarded as the stop words. As the task of tag extraction is to find the keywords of a document, thus we must exclude those words to find the real tags.

这里要装逼弄一堆公式 TFIDF TEXTRANK 中文分词 的公式，弄到word中时从论文里找

#### 3.4.3 Inverted Index

After finishing the first two stages of the processing pipeline (note labeling and tag extraction), the system will build inverted index for the notes and the tags so as to accelerate the speed to find the corresponding tags in a specific note.

In computer science, an inverted index is an index data structure storing a mapping from content, such as words or numbers, to its locations in a document or a set of documents. Extra time and space are need while adding new notes to the system, but with little cost inverted index makes fast full text searches possible [47]. Here is an example:

Given the texts
T[0] = "it is what it is"
T[1] = "what is it"
T[2] = "it is a banana"

we have the following inverted file index (where the integers in the set notation brackets refer to the indexes (or keys) of the text symbols, T[0], T[1] etc.):

"a":      {2}
"banana": {2}
"is":     {0, 1, 2}
"it":     {0, 1, 2}
"what":   {0, 1}

The inverted index data structure is a central component of a typical search engine indexing algorithm. A goal of a search engine implementation is to optimize the speed of the query: find the documents where word X occurs. Once a forward index is developed, which stores lists of words per document, it is next inverted to develop an inverted index. Querying the forward index would require sequential iteration through each document and to each word to verify a matching document. The time, memory, and processing resources to perform such a query are not always technically realistic. Instead of listing the words per document in the forward index, the inverted index data structure is developed which lists the documents per word [48].

The inverted index file in my system is as followed:

这里展示一下具体的文件内容

After building the inverted index for the user’s note, the system can now finish the task of classifying the note automatically base on Naive Bayes method.

#### 3.4.3 Note Classification

This is the most important part of the note system as it use the knowledge graph to help user classify and organize their notes. The system will automatically analyze the text in the note and find one or several proper categories for the note using Naive Bayes method.

In machine learning, Naive Bayes classifiers are a family of simple probabilistic classifiers based on applying Bayes' theorem with strong (naive) independence assumptions between the features. For text classification, that is to say the probability of the appearance of one word will not affect the appearance of the other words. This is a strong independence assumptions as in natural language there will always be some poly-words, collocations, institutional utterance and phrasal unites that violate assumption. However, for most case the Naive Bayes classifier can provide good enough performance as noisy may be one of the fixed property of the world.

Naive Bayes is one of the most famous and easy to implement algorithm and has been studied extensively since 1950s. At first, it was introduced in some text retrieval community in the early 1960s [49] and becomes one of the most popular (or baseline) method for text classification. Text classification is the kind of problem of judging which category one document may belong to using word frequencies as the features. As the notes from the users are highly organized format data, with appropriate preprocessing the Naive Bayes method is competitive with more advanced methods such as support vector machines [50][51].

In addition to this, Naive Bayes classifiers are highly scalable requiring a number of parameters linear in the number of variables (features/predictors) in a learning problem. Maximum-likelihood training can be done by evaluating a closed-form expression, which takes linear time, rather than by expensive iterative approximation as used for many other types of classifiers.

**Probabilistic model **

这里要装逼弄一堆公式，参考维基百科，配合好参考文献

Abstractly, naive Bayes is a conditional probability model: given a problem instance to be classified, represented by a vector  representing some n features (dependent variables), it assigns to this instance probabilities

for each of k possible outcomes or classes.[7]
The problem with the above formulation is that if the number of features n is large or if a feature can take on a large number of values, then basing such a model on probability tables is infeasible. We therefore reformulate the model to make it more tractable. Using Bayes' theorem, the conditional probability can be decomposed as

In plain English, using Bayesian probability terminology, the above equation can be written as

In practice, there is interest only in the numerator of that fraction, because the denominator does not depend on  and the values of the features are given, so that the denominator is effectively constant. The numerator is equivalent to the joint probability model

which can be rewritten as follows, using the chain rule for repeated applications of the definition of conditional probability:

Now the "naive" conditional independence assumptions come into play: assume that each feature  is conditionally independent of every other feature  for , given the category . This means that

and so on, for . Thus, the joint model can be expressed as

This means that under the above independence assumptions, the conditional distribution over the class variable  is:

where the evidence  is a scaling factor dependent only on , that is, a constant if the values of the feature variables are known.
Constructing a classifier from the probability model
The discussion so far has derived the independent feature model, that is, the naive Bayes probability model. The naive Bayes classifier combines this model with a decision rule. One common rule is to pick the hypothesis that is most probable; this is known as the maximum a posteriori or MAP decision rule. The corresponding classifier, a Bayes classifier, is the function that assigns a class label  for some k as follows:

**Text Classification**

Here is a worked example of naive Bayesian classification to the text classification problem. Consider the problem of classifying documents by their content, for example into science and society note (This is a simplified binary classification problem as an example, for multiple choice classification we just need more options to find it probabilities). Imagine that documents are drawn from a number of classes of documents which can be modeled as sets of words where the (independent) probability that the i-th word of a given document occurs in a document from class C can be written as

接下来是一堆公式，搬到word 的时候再弄

(For this treatment, we simplify things further by assuming that words are randomly distributed in the document - that is, words are not dependent on the length of the document, position within the document with relation to other words, or other document-context.)
Then the probability that a given document D contains all of the words , given a class C, is

The question that we desire to answer is: "what is the probability that a given document D belongs to a given class C?" In other words, what is ?
Now by definition

and

Bayes' theorem manipulates these into a statement of probability in terms of likelihood.

Assume for the moment that there are only two mutually exclusive classes, S and ¬S (e.g. spam and not spam), such that every element (email) is in either one or the other;

and

Using the Bayesian result above, we can write:


Dividing one by the other gives:

Which can be re-factored as:

Thus, the probability ratio p(S | D) / p(¬S | D) can be expressed in terms of a series of likelihood ratios. The actual probability p(S | D) can be easily computed from log (p(S | D) / p(¬S | D)) based on the observation that p(S | D) + p(¬S | D) = 1.
Taking the logarithm of all these ratios, we have:

(This technique of "log-likelihood ratios" is a common technique in statistics. In the case of two mutually exclusive alternatives (such as this example), the conversion of a log-likelihood ratio to a probability takes the form of a sigmoid curve: see logit for details.)

Finally, the document can be classified as follows. It is society if  (i.e., ), otherwise it is science.

Using this kind of method we can finish the automatic text classification task.

#### 3.4.4 Similar Notes

After classifying user’s notes, another important task is to find the connections between different notes. Usually we use TFIDF method and a distance measure to calculate the similarity between two notes and tell the user which ones are the similar notes. This kind of method is easy to implement but has two major problems. One is that two notes may have some shared words but their meanings are totally different, especially when one Chinese word can have completely different meanings in different context. The other is that two notes may not have any shared words but their meanings are highly related.

With the help of personal knowledge graph, it is possible for the system to solve the above problems with ease.

After initialing the personal knowledge graph, when loaded in all the user’s note, each node in the knowledge graph will has its own word list to show that this word may be highly related to a specific node. If we want to find the similar note for note A, first we need to extract the keywords from note A and check their positions in the personal knowledge graph. When calculating the similarity between note A and note B, we turn the comparison of strings into checking the degree of connection between two sub-graphs generated by note A and note B. As it is, many flow networks algorithms can be applied to find their similarity such as Dinic’s algorithm [52], push–relabel maximum flow algorithm [53] and Karger's algorithm [54]. These are all closed-form problems and can be computed fast.

### 3.5 Results

Now we have a directory-based note system using Markdown syntax and integrate it with personal knowledge graph and using Naive Bayes method to support better performance on text classification and similar note discovery. As it is a machine learning method the more notes added to the system the better performance it will get (some labeling work are needed to be the training data). In next chapter there will be another application based on the knowledge graph and the note system to connect personal knowledge to the internet data source.

## Chapter 4 Recommender System

### 4.1 Introduction

Chris Anderson wrote in his book “The Long Tail" that we are leaving the age of information and entering the age of recommendation. The Web is leaving the era of search and entering one of discovery. Search is what you do when you're looking for something. Discovery is when something wonderful that you didn't know existed, or din't know how to ask for, finds you.

This is also one of the most important stages in build the full circle of learning. There are so much information on the Internet and how can we find those knowledge we don’t even know it is important? That comes to the recommender problem:

+ Estimate a **utility function** that **automatically predicts** how a user will like an item.
+ Based on: Past behavior, Relations to tother users, Item similarity, Context
+ Let `C` be set of all users and let `S` be set of all possible recommendable items
+ Let `u` be a utility function measuring the usefulness of item `s` to user `c`, i.e., `u: C x S -> R`, where `R` is a totally ordered set
+ For each user `c` in `C`, we want to choose items `s` in `S` that maximize `u`

![rs1](./_resources/rs1.jpg)

**Approaches to Recommendation**

Offline: Learning Process, Model/Clusters

Online: Decision Process, Recommended Items

+ Collaborative filtering(CF): Recommend items based only on the users past behavior
    + **User-based**: Find similar users to me and recommend what they liked
    + **Item-based**: Find similar items to those that I have previously liked
+ Content-based: Recommend based on item features
+ Personalized Learning to Rank: Treat recommendation as a ranking problem
+ Demographic: Recommend based on user features
+ Social recommendations(trust-based)
+ Hybrid: Combine any of the above

**Serendipity**

+ Unsought finding
+ Don't recommend items the user already knows or **would have found anyway**
+ Expand the user's taste into neighboring areas by improving the obvious
+ Collaborative filtering can offer controllable serendipity(e.g. controlling how many neighbors to use in the recommendation)

**The CF Ingredients**

+ List of `m` Users and a list of `n` Items
+ Each user has a `list of items` with associated `opinion`
    + Explicit opinion - a rating score
    + Sometimes the rating is implicitly - purchase records or listen to tracks
+ `Active user` for whom the CF prediction task is performed
+ `Metric` for measuring `similarity between users`
+ Method for selecting a subset of `neighbors`
+ Method for `predicting a rating` for items not currently rated by the active user


**Pros & Cons**

+ Pros:
    + Requires `minimal knowledge` engineering efforts
    + Users and products are symbols without any internal structure or characteristics
    + Produces good-enough results in most cases
+ Cons:
    + Requires a large number of `reliable` user feedback data to bootstrap
    + Requires products to be standardized (users should have bought `exactly` the same product)
    + Assumes that `prior behavior determines current behavior` without taking into account contextual knowledge(session-level)

**Sparsity Problem**

+ Typically: large product sets, user ratins for a small percentage of them
+ Standard CF must have a number of users comparable to one tenth of the size of the product catalogue
+ Methods of dimensionality reduction
    + Matrix Factorization
    + Clustering
    + Projection(PCA ...)

**Scalability Problem**

+ Nearest neighbor algorithms require computations that grows with both the number of customers and products
+ With millions of customers and products a web-based recommender can suffer serious scalability problems
+ The worst case complexity is O(mn)(`m` customers and `n` product)
+ But in practice the complexity is O(m+n) since for each customer only a small number of products are considered
+ Some clustering techniques like K-means can help

**Performance Implications**

+ User-based CF - similarity between users is dynamic, precomputing user neighborhood can lead to poor predictions
+ Item-based CF - similarity between items is static
+ Enables precomputing of item-time similarity => prediction process involves only a table lookup for the similarity values & computation of the weighted sum

##### Model-based Collaborative Filtering

+ Use the entire user-item database to generate a prediction
+ Usage of statistical techniques to find the neighbors - e.g. nearest-neighbor
+ First develop a model of user
+ Type of model:
    + Probabilistic (e.g. Bayesian Network)
    + Clustering
    + Rule-based approaches (e.g. Association Rules)
    + Classification
    + Regression
    + LDA

**Classifiers**

+ Classifiers are general computational models trained using positive and negative examples
+ They may take in inputs
    + Vector of item features
    + Preferences of customers
    + Relations among item
+ E.g. Logistic Regression, Bayesian Networks, Support Vector Machines, Decision Trees, etc.
+ Pros
    + Versatile
    + Can be combined with other methods to improve accuracy of recommendations
+ Cons
    + Need a relevant training set
    + May overfit(Regularization)

+ Cold Start: There needs to be enough other users already in the system to find a match. New items need to get enough ratings
+ Popularity Bias: Hard to recommend items to someone with unique tastes
    + Tends to recommend popular items(items from the tail do not get so much data)

Seven hybridization techniques:
    •   Weighted: The score of different recommendation components are combined numerically.
    •   Switching: The system chooses among recommendation components and applies the selected one.
    •   Mixed: Recommendations from different recommenders are presented together.
    •   Feature Combination: Features derived from different knowledge sources are combined together and given to a single recommendation algorithm.
    •   Feature Augmentation: One recommendation technique is used to compute a feature or set of features, which is then part of the input to the next technique.
    •   Cascade: Recommenders are given strict priority, with the lower priority ones breaking ties in the scoring of the higher ones.
    •   Meta-level: One recommendation technique is applied and produces some sort of model, which is then the input used by the next technique.[27]

Robin Burke , Hybrid Web Recommender Systems, pp. 377-408, The Adaptive Web, Peter Brusilovsky, Alfred Kobsa, Wolfgang Nejdl (Ed.), Lecture Notes in Computer Science, Springer-Verlag, Berlin, Germany, Lecture Notes in Computer Science, Vol. 4321, May 2007, 978-3-540-72078-2.

### 4.2 Data Acquisition and Parsing

Scrapy, Book information, 描述一下数据结构(用那个复杂的)，然后处理成tag，类似于与note

### 4.3 Integrated with Knowledge Graph

根据标签和自带的分类信息来链接到各个节点上，根据评分和人数之类的信息(不同评分的分布)来进行打分

这里需要扯一个评分公式

分析一下一些特殊值

### 4.4 Connected to Note System

如何利用 knowledge graph 把结合 note 来进行 book 推荐

similarity computation

## Chapter 5 Conclusion

This is a novel attempt to apply a small part of knowledge graph from the internet for personal information management. Though lots of human labeling efforts are needed, its high accuracy and structured information arranging method can help people turn notes into knowledge. It is a plain-text based system so that it is easy to implement on different platforms to create a complete information management environment.

Now we have a web-based GUI to present all the notes mapping from specific local folder supporting markdown/pdf/image/math equations. As time limited the knowledge graph and the information management tool is separated from this GUI and work as a command-line-tool.

For text classification, based on LibLinear, we get a precision rate about 79.4% and greatly reduce the amount of computing time compared with naive bayes and svm method. However as the training/testing data is small, it may represent personal interests but can not be applied to predict other language material from the web or other people.

For book recommendation, based on knowledge graph, the recommended items for are highly related to the text itself and can give detailed recommendation reason.

### 5.1 Comparison on Note System

数据对比

### 5.2 Comparison on Recommender System

数据对比

### 5.3 Future Work

扯淡

## Bibliography

[1] Schmitt, U., 2013. Managing Personal Knowledge to make a Difference, 27th British Academy of Management Conference Proceedings (BAM), Sep 10–12, 2013, Liverpool, UK, 978–0–9549608–6–5.
[2] S. Ismail, M. S. Ahmad, “Emergence of Social Intelligence in Social Network: A Quantitative Analysis for Agent-mediated PKM Processes”, in Proc. of the ICIMu 2011 Conference, Malaysia, 2011.
[3] J. Grundspenkis, “Agent based approach for organization and personal knowledge modelling: Knowledge management perspective”, Journal of Intelligent Manufacturing, vol. 18, 2007, pp 451-457.
[4] H. Jarche, “PKM in 2010”, Life in Perpetual Beta. 2010. [5] H. Jarche, “Sense-Making with PKM”, Life in Perpetual Beta. 2009. [6] J. Martin, “Personal Knowledge Management”, Managing Knowledge:
Case Studies in Innovation. Edmonton: Spotted Cow Press. 2000. [7] S. Avery, R. Brooks, J. Brown, P. Dorsey, M. O’ Connor, “Personal knowledge management: framework for integration and partnerships”, in Proc. of the Association of Small Computer Users in Education Conference, 2001, pp. 29-39. [8] M. C. Pettenati, E. Cigognini, J. Mangione, E. Guerin, “Using social
software for personal knowledge management in formal online learning”, Turkish Online Journal of Distance Education, vol. 8, 2007, pp. 52-65.
[9] L. Razmerita, K. Kirchner, F. Sudzina, “Personal knowledge management: The role of Web 2.0 tools for managing knowledge at individual and organisational levels”, Online Information Review, vol. 33, 2009, pp. 1021-1039.
[10] “Chinese word segmentation as character tagging,” pp. 1–19, May 2003.
[11] Mihalcea, Rada, and Paul Tarau. "TextRank: Bringing order into texts." Association for Computational Linguistics, 2004.
[12] A. Nenkova, “Automatic Summarization,” FNT in Information Retrieval, vol. 5, no. 2, pp. 103–233, 2011.
[13] “Graph-based Ranking Algorithms for Sentence Extraction, Applied to Text Summarization,” pp. 1–4, Mar. 2015.
[14] J. Goldstein, V. Mittal, J. Carbonell, and M. Kantrowitz, “Multi-Document Summarization By Sentence Extraction,” pp. 1–9, Aug. 2002.
[15] Bird, Steven. "NLTK: the natural language toolkit." Proceedings of the COLING/ACL on Interactive presentation sessions. Association for Computational Linguistics, 2006.
[16] “Ontology Reasoning for the Semantic Web and Its Application to Knowledge Graph,” pp. 1–53, Oct. 2014.
[17] “Building, Maintaining, and Using Knowledge Bases: A Report from the Trenches,” pp. 1–12, Apr. 2013.
[18] “NLP Techniques in Knowledge Graph,” pp. 1–39, Oct. 2013.
[19] Bollacker, Kurt, et al. "Freebase: a collaboratively created graph database for structuring human knowledge." Proceedings of the 2008 ACM SIGMOD international conference on Management of data. ACM, 2008.
[20] Auer, Sören, et al. Dbpedia: A nucleus for a web of open data. Springer Berlin Heidelberg, 2007.
[21] Wang, Zhigang, et al. "XLore: A Large-scale English-Chinese Bilingual Knowledge Graph." International Semantic Web Conference (Posters & Demos). Vol. 1035. 2013.
[22] Miller, George A. "WordNet: a lexical database for English." Communications of the ACM 38.11 (1995): 39-41.
[23] Carpuat, Marine, et al. "Creating a bilingual ontology: A corpus-based approach for aligning WordNet and HowNet." Proceedings of the 1st Global WordNet Conference. 2002.
[24] Hu, Fanghuai, Zhiqing Shao, and Tong Ruan. "Self-supervised chinese ontology learning from online encyclopedias." The Scientific World Journal 2014 (2014).
[25] Das, Abhinandan S., et al. "Google news personalization: scalable online collaborative filtering." Proceedings of the 16th international conference on World Wide Web. ACM, 2007.
[26] Liu, Jiahui, Peter Dolan, and Elin Rønby Pedersen. "Personalized news recommendation based on click behavior." Proceedings of the 15th international conference on Intelligent user interfaces. ACM, 2010.
[27] Sarwar, Badrul, et al. "Item-based collaborative filtering recommendation algorithms." Proceedings of the 10th international conference on World Wide Web. ACM, 2001.
[28] Zhou, Yunhong, et al. "Large-scale parallel collaborative filtering for the netflix prize." Algorithmic Aspects in Information and Management. Springer Berlin Heidelberg, 2008. 337-348.
[29] Salakhutdinov, Ruslan, Andriy Mnih, and Geoffrey Hinton. "Restricted Boltzmann machines for collaborative filtering." Proceedings of the 24th international conference on Machine learning. ACM, 2007.
[30] Koren, Yehuda. "Factorization meets the neighborhood: a multifaceted collaborative filtering model." Proceedings of the 14th ACM SIGKDD international conference on Knowledge discovery and data mining. ACM, 2008.
[31] Koren, Yehuda. "Collaborative filtering with temporal dynamics."Communications of the ACM 53.4 (2010): 89-97.
[32] Adomavicius, Gediminas, and Alexander Tuzhilin. "Context-aware recommender systems." Recommender systems handbook. Springer US, 2011. 217-253.
[33] Garcia-Molina, Hector, Georgia Koutrika, and Aditya Parameswaran. "Information seeking: convergence of search, recommendations, and advertising." Communications of the ACM 54.11 (2011): 121-130.
[34] Cremonesi, Paolo, Yehuda Koren, and Roberto Turrin. "Performance of recommender algorithms on top-n recommendation tasks." Proceedings of the fourth ACM conference on Recommender systems. ACM, 2010.
[35] Trewin, Shari. "Knowledge-based recommender systems." Encyclopedia of Library and Information Science: Volume 69-Supplement 32 (2000): 180.
[36] Liang, Ting-Peng, et al. "A semantic-expansion approach to personalized knowledge recommendation." Decision Support Systems 45.3 (2008): 401-412.
[37] Carlson, Andrew, et al. "Toward an Architecture for Never-Ending Language Learning." AAAI. Vol. 5. 2010.
[38] Etzioni, Oren, et al. "Open information extraction from the web."Communications of the ACM 51.12 (2008): 68-74.
[39] Niu, Feng, et al. "DeepDive: Web-scale Knowledge-base Construction using Statistical Learning and Inference." VLDS 12 (2012): 25-28.
[40] Gruber, Thomas R. "A translation approach to portable ontology specifications."Knowledge acquisition 5.2 (1993): 199-220.
[41] Klyne, Graham, and Jeremy J. Carroll. "Resource description framework (RDF): Concepts and abstract syntax." (2006).
[42] Zhou, Q., and S. Y. Feng. "Build a relation network representation for How-Net."Proceedings of the 2000 International Conference on Multilingual Information Processing, Urumqi, China. 2000.
[43] Huang, Zengyang. "The Hierarchical Network of Concepts theory." (1998).
[44] Cheng, Xiao, and Dan Roth. "Relational inference for wikification." Urbana 51 (2013): 61801.
[45] A. Gal, G. Modica, H. Jamil, and A. A. Eyal, “Automatic Ontology Matching Using Application Semantics ,” pp. 1–12, Mar. 2005.
[46] Zhang, Hua-Ping, et al. "HHMM-based Chinese lexical analyzer ICTCLAS."Proceedings of the second SIGHAN workshop on Chinese language processing-Volume 17. Association for Computational Linguistics, 2003.
[47] Knuth, D. E. (1997) [1973]. "6.5. Retrieval on Secondary Keys". The Art of Computer Programming (Third ed.). Reading, Massachusetts: Addison-Wesley. ISBN 0-201-89685-0.
[48] Zobel, Justin; Moffat, Alistair; Ramamohanarao, Kotagiri (December 1998). "Inverted files versus signature files for text indexing". ACM Transactions on Database Systems(New York: Association for Computing Machinery) 23 (4): pp. 453–490. doi:10.1145/296854.277632.
[49] Russell, Stuart; Norvig, Peter (2003) [1995]. Artificial Intelligence: A Modern Approach (2nd ed.). Prentice Hall. ISBN 978-0137903955.
[50] Rennie, J.; Shih, L.; Teevan, J.; Karger, D. (2003). Tackling the poor assumptions of Naive Bayes classifiers. ICML.
[51] Suykens, Johan AK, and Joos Vandewalle. "Least squares support vector machine classifiers." Neural processing letters 9.3 (1999): 293-300.
[52] Yefim Dinitz (1970). "Algorithm for solution of a problem of maximum flow in a network with power estimation" (PDF). Doklady Akademii nauk SSSR11: 1277–1280.
[53] Goldberg, A V; Tarjan, R E (1986). "A new approach to the maximum flow problem". Proceedings of the eighteenth annual ACM symposium on Theory of computing - STOC '86. p. 136.
[54] Karger, David (1993). "Global Min-cuts in RNC and Other Ramifications of a Simple Mincut Algorithm". Proc. 4th Annual ACM-SIAM Symposium on Discrete Algorithms.
[55]
[56]
[57]
[58]
[59]
[60]
[61]
[62]
[63]
[64]
[65]



[9] Bird, Steven. "NLTK: the natural language toolkit." Proceedings of the COLING/ACL on Interactive presentation sessions. Association for Computational Linguistics, 2006.

[10] Y. G. P. D. Y. Z. Guandong Xu, “SemRec: A Semantic Enhancement Framework for Tag based Recommendation,” pp. 1–6, Jun. 2011.

## Appendix A

## Acknowledgements
