# 论文修改意见

<!-- MarkdownTOC -->

- 一些答辩时可能提到的数据
- 需要修改的地方
- 修改意见原文
    - Review result 1
    - Overall evaluation of the thesis 1
    - Review result 2
    - Overall evaluation of the thesis 2
- Reminder

<!-- /MarkdownTOC -->

## 一些答辩时可能提到的数据

Knowledge Graph 数据

    Root 1 总分类
    Field 6 技术 地理 科学 社会
    Transition 9 人物 宗教 文化 生活
    Entity 581 户外 宠物 动物 资讯
    Leaf NA NA

笔记数据系统

    400 personal notes in 15 categories including technique, geography, root category, science, history, society, people, religion, culture, leisure, life, nature, society science, technology and nature science. 300 of them are used as the training data and the rest are test data.


## 需要修改的地方

+ (已完成)阐述数据来使结果更加可信(write more details about the example data used for the experiments (400 personal notes in 15 categories) to make the results more convincing.)
+ (已完成)引用时候的规整，要么全用`[]`要么全用`()` (The reference syntax is not uniform in this paper, for example, sometimes it uses [], sometimes it uses “(Ferguson, 1999; Khan, 1999),”. The author needs to clean it up.)
+ (已完成)论文对于其实现的两个系统（笔记系统和书籍推荐系统）的运行效果描述不够清晰。论文只是使用几个截图简单地给出了这两个系统的一些运行结果，读者无法判断这两个系统的功能到底有哪些，更无法判断个人知识图谱在系统到底其怎样的作用；
+ (已完成)论文对于其提出基于个人知识图谱的笔记分类算法和书籍推荐算法的实验设计及其结果分析还比较简单。论文应单列一章来比较详细地描述实验结果及其分析，而不是放在结论一章中（另外致谢和参考文献不需要章编号）。应对其使用的数据集及其权威性做清楚的论证。从表5-2和表5-3的结果看，作者提出的基于个人知识图谱的方法与相关方法相比也没有显著的不同。


## 修改意见原文

### Review result 1

This thesis has basically reached the requirements of Master of Engineering degree thesis level, and the defense can be carried out after the revision.

### Overall evaluation of the thesis 1

This research built an effective toolkit for personal information management that can perform information aggregation and find connections between different information. The toolkit can turn rich data into organized information and knowledge to reveal hidden links between information.

One contribution of the work is to use the Knowledge Graph to arrange all the information and find connections between the data. It also gives out recommendation using the information of current node and neighboring nodes. The Knowledge Graph is dynamically adaptive to understand the user’s habits and be more effective and accurate through learning the user’s behavior.

The background research is adequate, the quality of the research is innovative and the author had good understanding of the problems in this topic. The work had satisfied the basic requirements of MS research thesis.

The author should write more details about the example data used for the experiments (400 personal notes in 15 categories) to make the results more convincing.

The reference syntax is not uniform in this paper, for example, sometimes it uses [], sometimes it uses “(Ferguson, 1999; Khan, 1999),”. The author needs to clean it up.
Suggestions for revision:
The author should write more details about the example data used for the experiments (400 personal notes in 15 categories) to make the results more convincing.

The reference syntax is not uniform in this paper, for example, sometimes it uses [], sometimes it uses “(Ferguson, 1999; Khan, 1999),”. The author needs to clean it up.

### Review result 2

This thesis has reached the requirements on thesis of Master of Engineering, and the defense can be carried out.

### Overall evaluation of the thesis 2

知识表示与信息管理是计算机技术研究的热点领域之一，论文探讨一种基于知识图谱的个人信息管理方法，论文选题具有重要的理论意义和应用价值。

论文在介绍个人信息管理相关技术以及知识图谱基本概念的基础上，提出了一种通过构造个人知识谱图从而对个人信息进行提取、理解、分析和管理的个人信息管理方法，并构造了两个原型系统，笔记系统和书籍推荐系统作为案例来验证基于个人知识图谱的个人信息管理方法的可行性，给出了这两个系统的初步设计，并研究了其中基于个人知识图谱的笔记分类算法和书籍推荐算法，并做了初步的实验与相关的方法进行了比较。

论文反映作者较好地掌握了相关基础理论知识和相关技术，有一定的软件开发能力。论文撰写基本规范，组织结构基本合理，结论有一定可靠性。论文达到了工程硕士专业学位论文水平，可以参加答辩。

Suggestions for revision:

1. 论文对于其实现的两个系统（笔记系统和书籍推荐系统）的运行效果描述不够清晰。论文只是使用几个截图简单地给出了这两个系统的一些运行结果，读者无法判断这两个系统的功能到底有哪些，更无法判断个人知识图谱在系统到底其怎样的作用；

2. 论文对于其提出基于个人知识图谱的笔记分类算法和书籍推荐算法的实验设计及其结果分析还比较简单。论文应单列一章来比较详细地描述实验结果及其分析，而不是放在结论一章中（另外致谢和参考文献不需要章编号）。应对其使用的数据集及其权威性做清楚的论证。从表5-2和表5-3的结果看，作者提出的基于个人知识图谱的方法与相关方法相比也没有显著的不同。

## Reminder

1. Students should submit the thesis for defense to this e-mail before August 21.
2. The thesis defense will be in August 26.
