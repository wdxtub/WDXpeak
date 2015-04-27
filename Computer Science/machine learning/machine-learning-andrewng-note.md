# Machine Learning

<!-- MarkdownTOC -->

- Prerequists
- Machine Learning Definition
- Lecture 2: Linear Regression, Gradient Descent and Normal Equations
- Lecture 3: Locally weighted regression(loess), logistic regression

<!-- /MarkdownTOC -->


## Prerequists

+ basic knowledge of computer science
+ queues, stacks, binary trees
+ basic probability and statistics
+ basic linear algebra

## Machine Learning Definition

Arthur Samuel(1959): Field of study that gives computers the ability to learn without being explicitly programmed.

Tom Mitchell(1998): Well-posed Learning Problem: A computer program is said to learn from experience E with respect to some task T and some performance measure P, if its performance on T, as measured by P, improves with experience E.

四个大类

+ Supervised Learning
    + 回归，连续
    + 分类，离散(0, 1 分类)
+ Learning Theory
+ Unsupervised Learning
+ Reinforcement Learning
    + reward function

## Lecture 2: Linear Regression, Gradient Descent and Normal Equations

梯度下降方法有时候依赖于参数初始值，α 是 learning rate

batch 与 stochastic

对于大数据集，用随机的方法不一定能很快收敛

最小化问题

tr A 矩阵 A 对角线元素之和

## Lecture 3: Locally weighted regression(loess), logistic regression

也许可以做到完美拟合，但是很容易过拟合

underfitting 与 overfitting

parametric learning algorithm 找寻固定参数的最佳值

non-paramatric learning algorithm 参数的数量随着样本数量的增加而增加

在想要知道的点的估计值附近的区域选择点来进行LR(线性回归)，使用权重函数保证离指定点近的样本点权重较大，而远的较小

perceptron algorithm
