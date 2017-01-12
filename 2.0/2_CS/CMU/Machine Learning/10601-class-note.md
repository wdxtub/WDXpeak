# Machine Learning 课堂笔记

<!-- MarkdownTOC -->

- 课程信息
- 13 Oct. Tuesday
- 1 Sep. Tuesday
- 3 Sep. Wednesday
	- Density Estimation
	- Modeling Uncertainty with Probabilities
	- Maximum likelihood estimation, MLE
	- Maximum a priori estimation
- 8 Sep. Tuesday
	- Naive Bayes Classifier
	- Precision and Recall

<!-- /MarkdownTOC -->


## 课程信息

Recitation: 7:30-8:30 Thursday, Porter Hall 100

## 13 Oct. Tuesday

semi-supervised 可以看作是，先利用 labeled data 给 unlabeled data 做标记，然后根据这些标记来得出新的分离器。

Semi-supervised 的四个方法针对的是 ml 中不同的阶段，感觉需要经过大量实战才能培养出直觉找到最佳方法。但是半监督训练绝对是未来的方向，所谓四两拨千斤。

## 1 Sep. Tuesday

**Main Topics**

+ Supervised Learning
	+ Classifiers
		+ Naive Bayes, Logistic Regression, etc
		+ Extremely useful on many real tasks
	+ Non-linear classifiers
		+ Neural nets, decision trees, nearest-neighbor classifiers
	+ Regression
+ Unsupervised and semi-supervised learning
	+ k-means, mixture, SVC/PCA
+ Graphical models
	+ Bayes networks and Markov networks
	+ Hidden Markov models
+ Comparing and evaluating classifiers
	+ Overfitting, cross validation, bias-variance trade off
	+ Learning theory

**Conditional Probability**

Chain Rule

+ P(A^B) = P(A|B) P(B)
+ P(A^B^C) = P(A|B^C) P(B|C) P(C)

**Bayes Rule**

Write two expressions for P(A^B)

	P(A^B) = P(A|B)P(B)
	P(B^A) = P(B|A)P(A)

	P(A|B)P(B) = P(B|A)P(A)
	P(A|B)P(B) = P(B|A)P(A) / P(B)

P(A) - prior, P(A|B) - posterior 从 prior 到 posterior 的过程，B 可以看做是 evidence

## 3 Sep. Wednesday

+ P(B) = P(B A) + P(B \~A) - P(B|A)P(A) + P(B|\~A)P(\~A)
+ P(A|B^X) = P(B|A^X)P(A^X) / P(B^X)

P(θ|D) = P(D|θ)P(θ) / P(D)

+ P(θ|D) - posterior befilef on the unknown quantity after you see data D
+ P(D|θ) - liklihood: How likely is the observed data under the particular unknown quantity θ
+ P(θ) - prior belief on the unknown quantity befor you see data D
+ P(D) - much like a constant

Joint probability distribution - A functional mapping f: X-\>Y via probability distribution.

P(E) = 所有满足 E 条件的行的和

P(E1 | E2) = P(E1 ^ E2) / P(E2) = 所有满足 E1 和 E2 条件的行的和 / 所有满足 E2 条件的行的和

### Density Estimation

A Density Estimator learns a mapping from a set of attributes values to a Probability.

+ Input Attributes -\> Density Estimator -\> Probability
+ Input Attributes(x) -\> Classifier -\> Prediction of **categorical** output or class(one of y1, y2,..., yk)
+ Input Attributes -\> Regressor -\> Prediction of real-valued output(e.g. height)

为了分类一个属性 x，对于每个分类 y，求 p(x,y1), p(x,y2),...,p(x,yk)，然后挑选那个使 p 最大的 y 的分类返回

p 上的 `^` 符号表示这是一个 estimation

### Modeling Uncertainty with Probabilities

Y is a Boolean-value **randome variable** if

+ Y denotes an **event**
+ **there is uncertainty as to whether Y occurs**

Define P(Y|X) as "the fraction of possible worlds in which Y is true, given X"

Flips produce data set D with a(H) heads and a(T) tails

+ Flips are independent, identically distributed 1's and 0's (Bernoulli)
+ a(H) and a(T) are counts that sum these outcomes (Binomial)

P(D|θ) = P(a(H),a(T)|θ) = θ^(a(H)) \* (1-θ)^(a(T)) \* C(a(H), (a(H) + a(T))) \<- 因为次序不重要

### Maximum likelihood estimation, MLE

+ Data: Observed set D of a(H) Heads and a(T) Tails
+ Hypothesis: Binomial distributior
+ Learning θ is an optimization problem
+ MLE: Choose θ that maximizeds the probability of the observed data

^θ = argmax(θ) lnP(D|θ) = argmax(θ) lnθ^(a(H)) \* (1-θ)^(a(T))

要求 ^θ 的值，就要找上面式子的最值，如何求？对这个式子求导然后找极值点(导数为零)，并求出 θ

d/dθ ln P(D|θ) = 0 -\> ^θ(MLE) = a(H) / (a(H) + a(T))

也就是说，出现实验中可能的分部情况的最大可能的参数值，通过实验算出来的和我们通过直觉进行计算的是一致的（当然也有很多情况下是不一致的，这里一致是因为二项分布比较简单，这种不一致的情况实际上就是大多数人可能会根据直觉然后犯错误的地方，也就是了解概率的人咸鱼翻身的机会）

binomial 和 beta distribution 的区别在于未知的参数不一样。


### Maximum a priori estimation

**TODO**

## 8 Sep. Tuesday

### Naive Bayes Classifier

利用 Naive Bayes 可以减少一个参数（因为和是1，其中的一个可以用1-其他概率的和来代替）

Naive Bayes assumes

P(X1...Xn | Y) = P(Xi|Y) 的连乘

Two variables A, B are conditionally independent give C if

P(A,B|C) = P(A|C) \* P(B|C)

or

P(A|B,C) = P(A|B)

Using Chain rule

P(X1,X2|Y) = P(X1|X2,Y)P(X2|Y) = P(X1|Y)P(X2|Y)

利用 Naive Bayes 从原来的 (2^n-1)\*2 个参数降至 2n 个参数

### Precision and Recall

Precision = #(classified as positive AND positive in data) / #(classified as positive)

Recall = #(classified as positive AND positive in data) / #(positive in data)
