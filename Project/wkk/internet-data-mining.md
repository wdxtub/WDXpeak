# 互联网数据挖掘

万小军 http://www.icst.pku.edu.cn/lcwm

<!-- MarkdownTOC -->

- 数据挖掘概述与关联规则挖掘
    - 数据挖掘流程
    - 数据挖掘任务
    - 分类定义
    - 聚类定义
    - 关联规则挖掘：定义
    - 摘要

<!-- /MarkdownTOC -->

## 数据挖掘概述与关联规则挖掘

数据挖掘从多学科领域发展而来：Statistics/AI, Machine Learning, Pattern Recognition, Database systems

### 数据挖掘流程

**Data** -Selection-> **Target data** -Preprocessing-> **Preprocessed data** -Transformation-> **Transformed data** -Data mining-> **Patterns** -Interpretation/evaluatoin-> **Knowledge**

### 数据挖掘任务

+ 预测型(Prediction Methods): 基于一些变量预测其他变量的未知值或未来值
    + 分类 Classification
    + 回归 Regression
    + 偏差检测 Deviation Detection
+ 描述型(Description Methods): 发现描述数据的人们可解释的模式
    + 聚类 Clustering
    + 关联规则挖掘 Association Rule Discovery
    + 摘要 Summarization

### 分类定义

+ 给定一个样例集合(训练集)
    + 每个样例包含一个属性集合，其中一个属性是类标记/类号
+ 基于训练集构建一个模型，该模型将类标记属性看作是其它属性值的一个函数
+ 目标：对心的样例尽可能准确地赋予标记
    + 基于一个测试集来评估模型的准确性

Training Set -> Learn Classifier -> Model <- Test set

### 聚类定义

+ 给定一个数据点集合，每个数据点具有一组属性，数据点之间能进行相似度度量，聚类目标为找到若干类簇：
    + 同一类簇中的数据点相似
    + 不同类簇中的数据点不相似
+ 相似度度量准则
    + 欧氏距离
    + 其他面向特定问题的准则：余弦准则

应用：文档聚类

+ 目标：发现文档类簇，统一类簇中文档相似(基于重要词语)
+ 方法：识别每篇文档中的重要词语，基于文档相似性进行聚类

### 关联规则挖掘：定义

+ 给定一个记录集合，每个记录包含若干项
    + 产生依赖规则，可以基于某些项的出现预测一个项的出现

应用：市场营销

+ 假如发现一条规则
+ {面包圈..} -> {薯片}
+ 可以帮助提高薯片的销量

### 摘要

为数据集进行总结，提供一个简洁/紧凑的表示，包括可视化与报表生成
