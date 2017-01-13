# 机器学习和计算机视觉相关的数学

<!-- MarkdownTOC -->

- 线性代数 (Linear Algebra)：
- 概率和统计 (Probability and Statistics)
- 分析 (Analysis)
- 拓扑 (Topology)
- 流形理论 (Manifold theory)

<!-- /MarkdownTOC -->


## 线性代数 (Linear Algebra)：

我想国内的大学生都会学过这门课程，但是，未必每一位老师都能贯彻它的精要。这门学科对于Learning是必备的基础，对它的透彻掌握是必不可少的。我在科大一年级的时候就学习了这门课，后来到了香港后，又重新把线性代数读了一遍，所读的是

**Introduction to Linear Algebra (3rd Ed.)  by Gilbert Strang**

这本书是MIT的线性代数课使用的教材，也是被很多其它大学选用的经典教材。它的难度适中，讲解清晰，重要的是对许多核心的概念讨论得比较透彻。我个人觉得，学习线性代数，最重要的不是去熟练矩阵运算和解方程的方法——这些在实际工作中MATLAB可以代劳，关键的是要深入理解几个基础而又重要的概念：子空间(Subspace)，正交(Orthogonality)，特征值和特征向量(Eigenvalues and eigenvectors)，和线性变换(Linear transform)。从我的角度看来，一本线代教科书的质量，就在于它能否给这些根本概念以足够的重视，能否把它们的联系讲清楚。Strang的这本书在这方面是做得很好的。

而且，这本书有个得天独厚的优势。书的作者长期在MIT讲授线性代数课(18.06)，[课程的video](http://ocw.mit.edu/OcwWeb/Mathematics/18-06Spring-2005/CourseHome/index.htm)在MIT的Open courseware网站上有提供。有时间的朋友可以一边看着名师授课的录像，一边对照课本学习或者复习。

## 概率和统计 (Probability and Statistics)

概率论和统计的入门教科书很多，我目前也没有特别的推荐。我在这里想介绍的是一本关于多元统计的基础教科书：

**Applied Multivariate Statistical Analysis_(5th Ed.)  by Richard A. Johnson and Dean W. Wichern**

这本书是我在刚接触向量统计的时候用于学习的，我在香港时做研究的基础就是从此打下了。实验室的一些同学也借用这本书学习向量统计。这本书没有特别追求数学上的深度，而是以通俗易懂的方式讲述主要的基本概念，读起来很舒服，内容也很实用。对于Linear regression, factor analysis, principal component analysis (PCA), and canonical component analysis (CCA)这些Learning中的基本方法也展开了初步的论述。

之后就可以进一步深入学习贝叶斯统计和Graphical models。一本理想的书是

**Introduction to Graphical Models (draft version).  by M. Jordan and C.Bishop.**

我不知道这本书是不是已经出版了（不要和Learning in Graphical Models混淆，那是个论文集，不适合初学）。这本书从基本的贝叶斯统计模型出发一直深入到复杂的统计网络的估计和推断，深入浅出，statistical learning的许多重要方面都在此书有清楚论述和详细讲解。MIT内部可以access，至于外面，好像也是有电子版的。

## 分析 (Analysis)

我想大家基本都在大学就学过微积分或者数学分析，深度和广度则随各个学校而异了。这个领域是很多学科的基础，值得推荐的教科书莫过于

**Principles of Mathematical Analysis, by Walter Rudin**

有点老，但是绝对经典，深入透彻。缺点就是比较艰深——这是Rudin的书的一贯风格，适合于有一定基础后回头去看。

在分析这个方向，接下来就是泛函分析(Functional Analysis)。

**Introductory Functional Analysis with Applications, by Erwin Kreyszig.**

适合作为泛函的基础教材，容易切入而不失全面。我特别喜欢它对于谱论和算子理论的特别关注，这对于做learning的研究是特别重要的。Rudin也有一本关于functional analysis的书，那本书在数学上可能更为深刻，但是不易于上手，所讲内容和learning的切合度不如此书。

在分析这个方向，还有一个重要的学科是测度理论(Measure theory)，但是我看过的书里面目前还没有感觉有特别值得介绍的。

## 拓扑 (Topology)

在我读过的基本拓扑书各有特色，但是综合而言，我最推崇：

**Topology (2nd Ed.)  by James Munkres**

这本书是Munkres教授长期执教MIT拓扑课的心血所凝。对于一般拓扑学(General
topology)有全面介绍，而对于代数拓扑(Algebraic topology)也有适度的探讨。此书不需要特别的数学知识就可以开始学习，由浅入深，从最基本的集合论概念（很多书不屑讲这个）到 Nagata-Smirnov Theorem和Tychonoff theorem等较深的定理（很多书避开了这个）都覆盖了。讲述方式思想性很强，对于很多定理，除了给出证明过程和引导你思考其背后的原理脉络，很多令人赞叹的亮点——我常读得忘却饥饿，不愿释手。很多习题很有水平。

## 流形理论 (Manifold theory)

对于拓扑和分析有一定把握时，方可开始学习流形理论，否则所学只能流于浮浅。我所使用的书是

**Introduction to Smooth Manifolds.  by John M. Lee**

虽然书名有introduction这个单词，但是实际上此书涉入很深，除了讲授了基本的manifold, tangent space, bundle, sub-manifold等，还探讨了诸如纲理论(Category theory)，德拉姆上同调(De Rham cohomology)和积分流形等一些比较高级的专题。对于李群和李代数也有相当多的讨论。行文通俗而又不失严谨，不过对某些记号方式需要熟悉一下。

虽然李群论是建基于平滑流形的概念之上，不过，也可能从矩阵出发直接学习李群和李代数——这种方法对于急需使用李群论解决问题的朋友可能更加实用。而且，对于一个问题从不同角度看待也利于加深理解。下面一本书就是这个方向的典范：

**Lie Groups, Lie Algebras, and Representations: An Elementary Introduction.  by Brian C. Hall**

此书从开始即从矩阵切入，从代数而非几何角度引入矩阵李群的概念。并通过定义运算的方式建立exponential mapping，并就此引入李代数。这种方式比起传统的通过“左不变向量场(Left-invariant vector field)“的方式定义李代数更容易为人所接受，也更容易揭示李代数的意义。最后，也有专门的论述把这种新的定义方式和传统方式联系起来。

---

感觉数学似乎总是不够的。这些日子为了解决research中的一些问题，又在图书馆捧起了数学的教科书。从大学到现在，课堂上学的和自学的数学其实不算少了，可是在研究的过程中总是发现需要补充新的数学知识。Learning和Vision都是很多种数学的交汇场。看着不同的理论体系的交汇，对于一个researcher来说，往往是非常exciting的enjoyable的事情。不过，这也代表着要充分了解这个领域并且取得有意义的进展是很艰苦的。记得在两年前的一次blog里面，提到过和learning有关的数学。今天看来，我对于数学在这个领域的作用有了新的思考。对于Learning的研究，

1、Linear Algebra (线性代数) 和 Statistics (统计学) 是最重要和不可缺少的。这代表了Machine Learning中最主流的两大类方法的基础。一种是以研究函数和变换为重点的代数方法，比如Dimension reduction，feature extraction，Kernel等，一种是以研究统计模型和样本分布为重点的统计方法，比如Graphical model, Information theoretical models等。它们侧重虽有不同，但是常常是共同使用的，对于代数方法，往往需要统计上的解释，对于统计模型，其具体计算则需要代数的帮助。以代数和统计为出发点，继续往深处走，我们会发现需要更多的数学。

2、Calculus (微积分)，只是数学分析体系的基础。其基础性作用不言而喻。Learning研究的大部分问题是在连续的度量空间进行的，无论代数还是统计，在研究优化问题的时候，对一个映射的微分或者梯度的分析总是不可避免。而在统计学中，Marginalization和积分更是密不可分——不过，以解析形式把积分导出来的情况则不多见。

3、Partial Differential Equation （偏微分方程，这主要用于描述动态过程，或者仿动态过程。这个学科在Vision中用得比Learning多，主要用于描述连续场的运动或者扩散过程。比如Level set, Optical flow都是这方面的典型例子。

4、Functional Analysis (泛函分析)，通俗地，可以理解为微积分从有限维空间到
无限维空间的拓展——当然了，它实际上远不止于此。在这个地方，函数以及其所作用的对象之间存在的对偶关系扮演了非常重要的角色。Learning发展至今，也在向无限维延伸——从研究有限维向量的问题到以无限维的函数为研究对象。Kernel Learning 和 Gaussian Process 是其中典型的例子——其中的核心概念都是Kernel。很多做Learning的人把Kernel简单理解为Kernel trick的运用，这就把kernel的意义严重弱化了。在泛函里面，Kernel (Inner Product)是建立整个博大的代数体系的根本，从metric, transform到spectrum都根源于此。

5、Measure Theory(测度理论)，这是和实分析关系非常密切的学科。但是测度理论并不限于此。从某种意义上说，Real Analysis可以从Lebesgue Measure（勒贝格测度）推演，不过其实还有很多别的测度体系——概率本身就是一种测度。测度理论对于Learning的意义是根本的，现代统计学整个就是建立在测度理论的基础之上——虽然初级的概率论教科书一般不这样引入。在看一些统计方面的文章的时候，你可能会发现，它们会把统计的公式改用测度来表达，这样做有两个好处：所有的推导和结论不用分别给连续分布和离散分布各自写一遍了，这两种东西都可以用同一的测度形式表达：连续分布的积分基于Lebesgue测度，离散分布的求和基于计数测度，而且还能推广到那种既不连续又不离散的分布中去（这种东西不是数学家的游戏，而是已经在实用的东西，在Dirchlet Process或者Pitman-Yor Process里面会经常看到)。而且，即使是连续积分，如果不是在欧氏空间进行，而是在更一般的拓扑空间（比如微分流形或者变换群），那么传统的黎曼积分（就是大学一年级在微积分课学的那种）就不work了，你可能需要它们的一些推广，比如Haar Measure或者 Lebesgue-Stieltjes积分。

6、Topology（拓扑学)，这是学术中很基础的学科。它一般不直接提供方法，但是它的很多概念和定理是其它数学分支的基石。看很多别的数学的时候，你会经常接触这样一些概念：Open set / Closed set，set basis，Hausdauf, continuous function，metric space, Cauchy sequence, neighborhood, compactness, connectivity。很多这些也许在大学一年级就学习过一些，当时是基于极限的概念获得的。如果，看过拓扑学之后，对这些概念的认识会有根本性的拓展。比如，连续函数，当时是由epison法定义的，就是无论取多小的正数epsilon，都存在xxx，使得xxx。这是需要一种metric去度量距离的，在general topology里面，对于连续函数的定义连坐标和距离都不需要——如果一个映射使得开集的原像是开集，它就是连续的——至于开集是基于集合论定义的，不是通常的开区间的意思。这只是最简单的例子。当然，我们研究learning也许不需要深究这些数学概念背后的公理体系，但是，打破原来定义的概念的局限在很多问题上是必须的——尤其是当你研究的东西它不是在欧氏空间里面的时候——正交矩阵，变换群，流形，概率分布的空间，都属于此。

7、Differential Manifold (微分流形)，通俗地说它研究的是平滑的曲面。一个直接的印象是它是不是可以用来fitting一个surface什么的——当然这算是一种应用，但是这是非常初步的。本质上说，微分流形研究的是平滑的拓扑结构。一个空间构成微分流形的基本要素是局部平滑：从拓扑学来理解，就是它的任意局部都同胚于欧氏空间，从解析的角度来看，就是相容的局部坐标系统。当然，在全局上，它不要求和欧氏空间同胚。它除了可以用于刻画集合上的平滑曲面外，更重要的意义在于，它可以用于研究很多重要的集合。一个n-维线性空间的全部k-维子空间

8、Lie Group Theory (李群论)，一般意义的群论在Learning中被运用的不是很多，群论在Learning中用得较多的是它的一个重要方向Lie group。定义在平滑流形上的群，并且其群运算是平滑的话，那么这就叫李群。因为Learning和编码不同，更多关注的是连续空间，因为Lie group在各种群中对于Learning特别重要。各种子空间，线性变换，非奇异矩阵都基于通常意义的矩阵乘法构成李群。在李群中的映射，变换
，度量，划分等等都对于Learning中代数方法的研究有重要指导意义。

9、Graph Theory（图论)，图，由于它在表述各种关系的强大能力以及优雅的理论，高效的算法，越来越受到Learning领域的欢迎。经典图论，在Learning中的一个最重要应用就是graphical models了，它被成功运用于分析统计网络的结构和规划统计推断的流程。Graphical model所取得的成功，图论可谓功不可没。在Vision里面，maxflow(graphcut)算法在图像分割，Stereo还有各种能量优化中也广受应用。另外一个重要的图论分支就是Algebraic graph theory (代数图论)，主要运用于图的谱分析，著名的应用包括Normalized Cut和Spectral Clustering。近年来在semi-supervised learning中受到特别关注。
