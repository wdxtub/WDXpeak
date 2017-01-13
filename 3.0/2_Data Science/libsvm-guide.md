# libSVM 使用指南

CMU 15 Fall 10601b 机器学习的期末作业是在 CIFAR-10 数据集上的图像分类，我们小组已经实现了 LR, NN, NB 等比较『朴素』的机器学习算法，对于如何实现 SVM 倒是一直没有什么思路。他山之石，可以攻玉，我打算从 libSVM 入手，看看能不能找到点思路。

## 一：下载编译安装

这三个统称『配置环境』，从[官网](http://www.csie.ntu.edu.tw/~cjlin/libsvm/index.html)下载，然后自己想办法编译（我是直接找别人编译好的），接着重命名避免和 matlab 自带的 svmtrain 重名。说明一下我用的版本是 3.20

> 在当前目录下会出现svmtrain.mexw64、svmpredict.mexw64（64位系统）或者svmtrain.mexw32、svmpredict.mexw32（32位系统）这两个文件，把文件名svmtrain和svmpredict相应改成libsvmtrain和libsvmpredict。
> 
> 这是因为Matlab中自带有SVM的工具箱，而且其函数名字就是svmtrain和svmpredict，和LIBSVM默认的名字一样，在实际使用的时候有时会产生一定的问题，比如想调用LIBSVM的变成了调用Matlab SVM。
> 
> 如果有进行重命名的，以后使用LIBSVM时一律使用libsvmtrain和libsvmpredict这两个名字进行调用。

## 二：原理

SVM 的原理这里不介绍，关键词：监督学习，二分类，核函数。这里提到是二分类，那么要如何扩展成多分类呢？比方说在我们的这个项目中，图片有十个类别，就要想办法把一个二分类的用到十分类上。比较基本的思路有两种，一对多(one-versus-rest)和一对一(one-versus-one)。

举个例子，一对多实际上是训练十个分类器，对于第一个分类器，类别 1 是一类，类别 2-10 是一类；对于第二个分类器，类别 2 是一类，类别 1 + 类别 3-10 是一类，这样就得到了十个分类器。预测的时候，分别用这十个分类器分类，然后将分类结果中出现最多的那个类别作为结果。

继续举例子，一对一的话实际要训练 $\frac{10\times9}{2}$ 个分类器，然后预测的时候需要跑所有的分类器，选出现最多的那个类别作为最终分类结果。

libSVM 是使用一对一的方式来实现的

## 三：使用

基本来说，因为不需要在意具体的实现，所以使用起来还是简单粗暴的

### 训练

如果数据准备好了的话，一句话就可以搞定。

```matlab
model = libsvmtrain(training_label_vector, training_instance_matrix [, 'libsvm_options']);
```

这个函数有三个参数，其中

+ `-training_label_vector`:训练样本的类标，如果有m个样本，就是m x 1的矩阵（类型必须为double）。这里可以是二分类和多分类，类标是（-1,1）、（1,2,3）或者其他任意用来表示不同的类别的数字，要转成double类型。
+ `-training_instance_matrix`:训练样本的特征，如果有m个样本，每个样本特征是n维，则为m x n的矩阵（类型必须为double）。
+ `-libsvm_options`:训练的参数，会专门开一章来介绍。

### 预测

如果有了训练出来的模型的话，一句话搞定。`libpredict` 函数用于对测试集的数据进行测试，还能对未知样本进行预测。

```matlab
[predicted_label, accuracy, decision_values/prob_estimates] 
　　　　= libsvmpredict(testing_label_vector, testing_instance_matrix, model [, 'libsvm_options']);
```

这个函数包括四个参数，其中

+ `-testing_label_vector`:测试样本的类标，如果有m个样本，就是m x 1的矩阵（类型必须为double）。如果类标未知，可以初始化为任意m x 1的double数组。
+ `-testing_instance_matrix`:测试样本的特征，如果有m个样本，每个样本特征是n维，则为m x n的矩阵（类型必须为double）。
+ `-model`:使用libsvmtrain返回的模型
+ `-libsvm_options`:预测的参数，与训练的参数形式一样。

## 四：参数

参数这一部分比较多，而且需要一定的理论基础，很多参数我都不大明白是干嘛的，所以我就先挑一些我懂的参数，然后剩下的就是文档里的大概翻译。所以下面的列表是有先后顺序的

+ `-s` svm类型：SVM设置类型（默认0，我就用默认的)
	+ 0 — C-SVC； 
	+ 1 – v-SVC； 
	+ 2 – one-class SVM； 
	+ 3 — e-SVR； 
	+ 4 — v-SVR
+ `-t` 核函数类型：核函数设置类型（默认2，据说2的效果也比较好，所以继续用2）
	+ 0 – 线性核函数：`u’v`
	+ 1 – 多项式核函数：`（r*u’v + coef0)^degree`
	+ 2 – RBF(径向基)核函数：`exp(-r|u-v|^2）`
	+ 3 – sigmoid核函数：`tanh(r*u’v + coef0)`
+ `-h` shrinking：是否使用启发式，0或1（默认1）
	+ 用 0 的话训练会快一些，
+ `-d` degree：核函数中的degree设置（针对多项式核函数）（默认3）
+ `-g` r(gamma）：核函数中的gamma函数设置（针对多项式/rbf/sigmoid核函数）（默认1/k，k为总类别数)
+ `-r` coef0：核函数中的coef0设置（针对多项式/sigmoid核函数）（（默认0)
+ `-c` cost：设置C-SVC，e -SVR和v-SVR的参数（损失函数）（默认1）
+ `-n` nu：设置v-SVC，一类SVM和v- SVR的参数（默认0.5）
+ `-p` p：设置e -SVR 中损失函数p的值（默认0.1）
+ `-m` cachesize：设置cache内存大小，以MB为单位（默认40）
+ `-e` eps：设置允许的终止判据（默认0.001）
+ `-wi` weight：设置第几类的参数C为weight*C (C-SVC中的C) （默认1）
+ `-v` n: n-fold交互检验模式，n为fold的个数，必须大于等于2

以上这些参数设置可以按照SVM的类型和核函数所支持的参数进行任意组合，如果设置的参数在函数或SVM类型中没有也不会产生影响，程序不会接受该参数；如果应有的参数设置不正确，参数将采用默认值。

## 五：返回数据模型

训练会返回一个结构体，预测会返回三个结果，这里分别说明一下

### 训练返回的内容

libsvmtrain函数返回训练好的SVM分类器模型，可以用来对未知的样本进行预测。这个模型是一个结构体，包含以下成员：

+ `-Parameters`: 一个5 x 1的矩阵，从上到下依次表示：
	+ `-s` SVM类型（默认0）；
	+ `-t` 核函数类型（默认2）
	+ `-d` 核函数中的degree设置(针对多项式核函数)(默认3)；
	+ `-g` 核函数中的r(gamma）函数设置(针对多项式/rbf/sigmoid核函数) (默认类别数目的倒数)；
	+ `-r` 核函数中的coef0设置(针对多项式/sigmoid核函数)((默认0)
+ `-nr_class`: 表示数据集中有多少类别，比如二分类时这个值即为2。
+ `-totalSV`: 表示支持向量的总数。
+ `-rho`: 决策函数wx+b中的常数项的相反数（-b）。
+ `-Label`: 表示数据集中类别的标签，比如二分类常见的1和-1。
+ `-ProbA`: 使用-b参数时用于概率估计的数值，否则为空。
+ `-ProbB`: 使用-b参数时用于概率估计的数值，否则为空。
+ `-nSV`: 表示每类样本的支持向量的数目，和Label的类别标签对应。如Label=[1; -1],nSV=[63; 67]，则标签为1的样本有63个支持向量，标签为-1的有67个。
+ `-sv_coef`: 表示每个支持向量在决策函数中的系数。
+ `-SVs`: 表示所有的支持向量，如果特征是n维的，支持向量一共有m个，则为m x n的稀疏矩阵。

另外，如果在训练中使用了-v参数进行交叉验证时，返回的不是一个模型，而是交叉验证的分类的正确率或者回归的均方根误差。

### 预测返回的内容

libsvmtrain函数有三个返回值，不需要的值在Matlab可以用~进行代替。

+ `-predicted_label`：第一个返回值，表示样本的预测类标号。
+ `-accuracy`：第二个返回值，一个3 x 1的数组，表示分类的正确率、回归的均方根误差、回归的平方相关系数。
+ -`decision_values/prob_estimates`：第三个返回值，一个矩阵包含决策的值或者概率估计。对于n个预测样本、k类的问题，如果指定“-b 1”参数，则n x k的矩阵，每一行表示这个样本分别属于每一个类别的概率；如果没有指定“-b 1”参数，则为n x k*(k-1)/2的矩阵，每一行表示k(k-1)/2个二分类SVM的预测结果。


## 六：读取或保存

**`libsvmread`函数可以读取以LIBSVM格式存储的数据文件。**

```matlab
[label_vector, instance_matrix] = libsvmread(‘data.txt’);
```

这个函数输入的是文件的名字，输出为样本的类标和对应的特征。

**`libsvmwrite`函数可以把Matlab的矩阵存储称为LIBSVM格式的文件。**

```matlab
libsvmwrite(‘data.txt’, label_vector, instance_matrix]
```

这个函数有三个输入，分别为保存的文件名、样本的类标和对应的特征（必须为double类型的稀疏矩阵）。

## 总结

总体来说训练时间还是很长的（怪电脑），尤其是随着分类的增多所需要的分类器会增长得更快，难以想象要分一百类会怎么样。不过 libSVM 在不同的平台下都有实现，哪怕想要在手机上实现最简单的机器学习，也都可以用这个包，还是非常方便的。

## 参考资料

[LIBSVM在Matlab下的使用](http://noalgo.info/363.html)


