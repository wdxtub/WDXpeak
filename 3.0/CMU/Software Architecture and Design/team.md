# Team Project

## 总体要求

练习各种各样的 pattern

作业围绕这个学期学习的五个主要方面：

+ Concepts of software architecture
+ design/reengineer various views of software architecture 
+ architectural styles (macro patterns)
+ design patterns (micro patterns)
+ ATAM to analyze existing architecture and make recommendations

在一个实际的稍微大型一点的项目中来具体实践，最终制品是：

+ a revised ATAM document adding recommendations on design patterns (earlier you have had recommendations on architectural styles and various architectural view diagrams)
+ implemented recommended design patterns and architectural styles seamlessly integrated in the previous students' project.

使用 Scrum，一共有 4 个 sprints，每次 1 到 2 周。具体的时间线为(Week 12 - Week 16)

+ Week 1 (Sprint 1: deadline: 4/8 Friday midnight)
    + set up docker-supported project environment with previous students' projects;
    + study existing design and code and recommend design patterns that should, could, or will be good to be implemented in this project.
    + After Sprint 1, TAs will summarize all design patterns / architectural styles that must be implemented in the team projects and publish to Blackboard.
+ Week 2 (Sprint 2: deadline: 4/15 Friday midnight)
    + Implement at least 4 recommended design patterns/architectural styles (one person one); demo to TAs (each group 1 hour)
+ Week 3 (Sprint 3: deadline: 4/22 Friday midnight)
    + Implement at least 8 recommended design patterns/architectural styles (one person two); demo to TAs (eachgroup 1 hour)
+ Week 4 (Sprint 4: deadline: 4/29 Friday midnight)
    + Implement all rest recommended design patterns/architectural styles;
    + give final group presentation; (template will be published soon)
    + demo to TAs (each group 1 hour)
 
Final deliverables (deadline: 5/6 Friday midnight PDT)

+ revised final presentation ppt;
+ final project technical report; (template will be published soon)


## 1st Sprint 

1. Form a group with 2 teams. Please state the group formation in the following [shared google doc file](https://docs.google.com/spreadsheets/d/1i7Tsn_QPZwvmmfWlbyfvKjP8_WpkdwcQmDDJuS7dmWs/edit#gid=0)
2. Each team will study the last semester team's document, design, and code, and summarize a document to recommend design patterns that (1) are used, (2) should be used, and (3) could be used, as part of the ATAM document.
3. Study docker technique and install and run the last semester team's work on local machine (in your submission, please mark whether this is done).

### 分工

队伍信息

+ Team 13(Da Wang, Jinhong Chen, Shaoyi Hu, Lei Yu, Yu Zheng)
+ Team 15(Shurui Li, Yang Shi, Yidi Liu, Ning Wang)

任务列表

+ 文档
    + 设计部分（结合代码，代码在[这里](https://drive.google.com/file/d/0Bxmu64h_VZzkNlRTVGR0QUUtWlU/view?usp=sharing)）
        + !!已使用的设计模式 ([4.5])
        + !!应该使用的设计模式 ([4.5]，根据需求分析)
        + !!能够使用的设计模式 ([4.5]，结合前面的分析)
        + 具体的分析需要结合 sensitivity, risk, tradeoff（就是之前 ATAM 的套路）
        + 分工就按照前端和后端，每组完成前端/后端的三个分析（也就是已使用/应该使用/能够使用）
            + 前端部分
            + 后端部分
    + Business ([挂起]初稿，需改进)
    + Mission ([挂起]初稿，需改进)
+ 设计
    + Utility Tree ([挂起]初稿，需改进)
    + Scenario Generation and Prioritization ([挂起]初稿，需改进)
    + Architectural style analysis and recommendations ([挂起]初稿，需改进)
    + Risks and non-risks ([挂起]初稿，需改进)
    + Analyze Architectural Approaches ([挂起]初稿，需改进)
+ 代码
    + docker 的安装与配置 ([已完成]，Team 13)


## 以下这部分可不看

TAs have created a new Docker image with the project code you will be working on with. The image tag is: `cmusvsc/apachecmda:1.1`

TMUX is installed for your convenience.

We also updated the tutorial with step by step instructions of using docker for this project at the [link](https://docs.google.com/document/d/15InmPSNxm3Wjm1GAIh4_ilVy4rPkYBY1dxcbK7BFmQc/edit?usp=sharing)

