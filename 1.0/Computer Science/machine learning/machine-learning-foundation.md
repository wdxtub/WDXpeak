# 机器学习基石 学习笔记

Hsuan-Tien Lin htlin@csie.ntu.edu.tw

<!-- MarkdownTOC -->

- Roadmap
- Lecture 1 The Learning Problem
    - 从学习到机器学习
    - Machine Learning
        - 三个关键
    - 学习问题
- Lecture 2 Learn to Answer Yes/No
    - select g from H
    - Perceptron Learning Algorithm
    - Cyclic PLA
    - Linear Separability 线性可分
    - PLA Fact: W~t~ Gets More Aligned with W~f~
    - PLA Fact: W~t~ Does Not Grow Too
    - 一个习题
    - More about PLA
    - Learning with **Noisy Data**
    - Pocket Algorithm
- Lecture 3: Types of Learning
    - Different Output Space
    - Different Label
    - Different Protocol
    - Different Input Space
- Lecture 4: Feasibility of Learning
    - Hoeffding's Inequality
    - Connect to Learning
- Lecture 5: Training versus Testing
    - Two Central Questions
    - Trade-off on M
    - Where Did M Come From
    - How Many Lines Are There?
    - Effective Number of Lines
    - Dichotomies: Mini-hypothesis
    - Growth Function
        - Growth Function for Positive Rays
        - Growth Fucntion for Positive Intervals
        - Growth Function for Convex Sets
    - The Four Growth Functions
        - Break Point of H
- Lecture 6: Theory of Generalization
    - Restriction of Break Point
    - Bounding Function
    - BAD Bound for General H
        - Step 1: Replace E~out~ by E~in~'
        - Step 2: Decompose H by Kind
        - Step 3: Use Hoeffding without Replacement
    - Vapnik-Chervonenkis (VC) bound:
- Lecture 7: The VC Dimension
    - More on Vapnik-Chervonenkis(VC) Bound
    - VC Dimension
    - VC Dimension and Learning
    - 2D PLA Revisited
    - VC Dimension of Perceptrons
    - 证明 d~vc~ >= d+1
    - 证明 d~vc~ <= d+1
    - Degrees of Freedom
    - VC Bound Rephrase: Penalty for Model Complexity
    - THE VC Message
    - VC Bound Rephrase: Sample Complexity
    - Looseness of VC Bound
- Lecture 8: Noise and Error
    - Target Distribution P(y|x)
    - Error Measure
    - Two Important Pointwise Error Measures
    - Choice of Error Measure
    - Weighted Classification
    - Minimizing E~in~ for Weighted Classification
- Lecture 9: Linear Regression
    - The Error Measure
    - Matrix Form of E~in~(w)
    - The Gradient ▽E~in~(w)
    - Optimal Linear Regression Weights
    - Linear Regression Algorithm
    - Is Linear Regression a 'Learning Algorithm'?
    - Benefit of Analytic Solution: 'Simpler-than-VC' Guarantee
    - Geometric View of **Hat Matrix**
    - The Learning Curve
    - Linear Classification vs. Linear Regression
- Lecture 10: Logistic Regression
    - Logistic Function
    - Three Linear Models
    - Likelihood
    - Cross-Entropy Error
    - Minimizing E~in~(w)
    - Iterative Optimization
    - Choice of η
    - Putting Everything Together
- Lecture 11: Linear Models for Classification
    - Linear Models Revisited
    - Error-Functions Revisited
    - Theoretical Implication of Upper Bound
    - Two Iterative Optimization Schemes
    - Stochastic Gradient Descent (SGD)
    - Multiclass Classification
    - One-Versus-All (OVA) Decomposition
    - One-versus-one(OVO) Decomposition
- Lecture 12: Nonlinear Transformation
    - Circular Separable
    - Linear Hypothesis in Z-Space
    - The Nonlinear Transform Steps
    - Computation/Storage Price
    - Model Complexity Price
    - polynomial Transform Revisited
- Lecture 13: Hazard of Overfitting
    - Case Study
    - Learning Curves Revisited
    - A Detailed Experiment
- Lecture 14: Regularization
    - Matrix Form of Regularized Regression Problem
    - The Lagrange Multiplier
    - Augmented Error
    - The Result
    - Legendre Polynomials
    - Regularization and VC Theory
    - Another View of Augmented Error
    - General Regularizers Ω(w)
    - L2 and L1 Regularizer
    - The Optimal λ
- Lecture 15: Validation
    - Comparison between E~in~ and E~test~
    - The Dilemma about K
    - Leave-One-Out Cross Validation
    - Disadvantages of Leave-One-Out Estimate
    - V-fold Cross Validation
    - Final Words on Validation
- Lecture 16: Three Learning Principles
    - Occam's Razor
    - Simple Model
    - Sampling Bias
    - Visual Data Snooping
    - Dealing with Data Snooping
    - Power of Three

<!-- /MarkdownTOC -->


## Roadmap

+ Lecture 1: The Learning Problem
    * _A_ takes _D_ and _H_ to get _g_
+ Lecture 2: Learning to Answer Yes/No
    * Perceptron Hypothesis Set
    * Perceptron Learning Algorithm, PLA
    * Guarantee of PLA
    * Non-Separable Data
+ Lecture 3: Types of Learning
    + Learning with Different Output Space y
        + [classification],[regression], structured
    + Learning with Different Data Lable y~n~
        + [supervised], un/semi-supervised, reinforcement
    + Learning with Different Protocol f -> (x~n~,y~n~)
        + [batch], online, active
    + Learning with Different Input Space X
        + [concrete], raw, abstract
+ Lecture 4: Feasibility of Learning
    + Learning is Impossible?
    + Probability to the Rescue
    + Connection to Learning
    + Connection to Real Learning
+ Lecture 5: Training versus Testing
    + Recap and Preview
        + two questions: E~out~(g) ≈ E~in~(g), and E~in~(g) ≈ 0
    + Effective Number of Lines
        + at most 14 through the eye of 4 inputs
    + Effective Number of Hypothesis
        + at most m~H~(N) through the eye of N inputs
    + Break Point
        + when m~H~(N) becomes 'non-exponential'
+ Lecture 6: Theory of Generalization
    + Restriction of Break Point
        + break point 'breaks' consequent points
    + Bounding Function: Basic Cases
        + B(N, k) bounds m~H~(N) with break point k
    + Bounding Function: Inductive Cases
        + B(N, k) is poly(N)
    + A Pictorial Proof
        + m~H~(N) can replace M with a few changes
+ Lecture 7: The VC Dimension
    + Definition of VC Dimension
        + maximum non-break point
    + VC Dimension of
        + d~vc~(H) = d + 1
    + Physical Intuition of VC Dimension
        + d~vc~ ≈ #free parameters
    + Interpreting VC Dimension
        + loosely: model complexity & sample complexity
+ Lecture 8: Noise and Error
    + Noise and Probability Target
        + can replace f(x) by P(y|x)
    + Error Measure
        + affect 'ideal' target
    + Algorithmic Error Measure
        + user-dependent -> plausible or friendly
    + Weighted Classification
        + easily done by virtual 'example copying'
+ Lecture 9: Linear Regression
    + Linear Regression Problem
        + use hyperplanes to approximate real values
    + Linear Regression Algorithm
        + analytic solution with pseudo-inverse
    + Generalization Issue
        + E~out~ - E~in~ ≈ 2(d+1)/N on average
    + Linear Regression for Binary Classification
        + 0/1 error <= squared error
+ Lecture 10: Logistic Regression
    + Logistic Regression Problem
        + P(+1|x) as target and θ(w^T^x) as hypothesis
    + Logistic Regression Error
        + cross-entropy(negative log likelihood)
    + Gradient of Logistic Regression Error
        + θ-weighted sum of data vectors
    + Gradient Descent
        + roll downhill by -▽E~in~(w)
+ Lecture 11: Linear Models for Classification
    + Linear Models for Binary Classification
        + three models useful in different ways
    + Stochastic Gradient Descent
        + follow negative stochastic gradient
    + Multiclass via Logistic Regression
        + predict with maximum estimated P(k|x)
    + Multiclass via Binary Classification
        + predict the tournament champion
+ Lecture 12: Nonlinear Transformation
    + Quadratic Hypothesis
        + linear hypothesis on quadratic-transformed data
    + Nonlinear Transform
        + happy linear modeling after Z = ø(X)
    + Price of Nonlinear Transform
        + computation/storage/[model complexity]
    + Structured Hypothesis Sets
        + linear/simpler model first
+ Lecture 13: Hazard of Overfitting
    + What is Overfitting
        + lower E~in~ but higher E~out~
    + The Role of Noise and Data Size
        + overfitting 'easily' happens!
    + Deterministic Noise
        + what H cannot capture acts like noise
    + Dealing with Overfitting
        + data cleaning/pruning/hinting, and more
+ Lecture 14: Regularization
    + Regularized Hypothesis Set
        + original H + constraint
    + Weight Decay Regularization
        + add (λ/N)w^T^w in E~aug~
    + Regularization and VC Theory
        + regularization decreases d~EFF~
    + General Regularizers
        + target-dependent, [plausible], or [friendly]
+ Lecture 15: Validation
    + Model Selection Problem
        + dangerous by E~in~ and dishonest by E~test~
    + Validation
        + select with E~val~(D~train~) while returning A~m*~(D)
    + Leave-One-Out Cross Validation
        + huge computation for almost unbiased estimate
    + V-Fold Cross Validation
        + reasonable computation and performance
+ Lecture 16: Three Learning Principles
    + Occam's Razor
        + simple, simple, simple!
    + Sampling Bias
        + match test scenario as much as possible
    + Data Snooping
        + any use of data is 'contamination'
    + Power of Three
        + relatives, bounds, models, tools, principles

## Lecture 1 The Learning Problem

从基础学习 what every machine learning user should know

+ When Can Machines Learn? illustrative + technical
+ Why Can Machines Learn? theoretical + illustrative
+ How Can Machines Learn? technical + practical
+ How Can Machines Learn Better? practical + theorietical

知其然也知其所以然

### 从学习到机器学习

+ 学习的过程：observations -> **learning** -> skill
+ 机器学习的过程：data -> **ML** -> skill(improved performance measure)
+ skill: improve some **performance measure**

### Machine Learning

+ improving some perormance mearsure with experience computed from data
+ an alternative route to build complicated systems

#### 三个关键

+ exists some 'underlying pattern' to be learned, so performance measure can be improved. 要有东西可学
+ but no programmable definition, so 'ML' is needed
+ somehow there is data about the pattern. 要有大量数据


### 学习问题

+ 输入 x
+ 输出 y
+ 目标函数 target function f: X->Y
+ data D={(x~1~,y~1~),(x~2~,y~2~),...,(x~n~,y~n~)}
+ 机器学习可能得到的假设 g:X->Y
+ {(x~n~, y~n~)} from f -> ML -> g

 ![learning flow](./_resources/mlf1.jpg)

+ f 我们不知道
+ g 越接近 f 越好
+ A takes D and H to get g
+ related to DM, AI and Stats

## Lecture 2 Learn to Answer Yes/No

+ 每一个样本的数据可以看成一个向量，可以给每一个向量计算出一个加权得分，每一个维度有一个权重。
+ 把 threshold 收进公式中，可以得到一个统一的表达，最后的得分等于两个向量相乘
+ ![mlf2](./_resources/mlf2.jpg)
+ perceptrons <-> linear(binary) classifiers 线性分类器

### select g from H

* H = all possible perceptrons, g = ? 从这么多可能的线之中，选出一条最好的，最能区分数据的
* 先要求 g 和 f 在已有数据上结果最接近, g(x~n~) = f(x~n~) = y~n~
* 难点在于，H 很大，有无数种可能的线(分类器)
* 从第一条线 g~0~ 开始，不断进行修正，可以认为是一开始的权重向量 w~0~

### Perceptron Learning Algorithm

* For t = 0, 1, ... 这里 t 是轮数，因为会迭代很多次
* 找到 w~t~ 的一个分类错误的点(x~n(t)~, y~n(t)~), 即 sign(w~t~^T^x~n(t)~) 不等于 y~n(t)~
* 试着去改正这个错误 w~t+1~ <- w~t~ + y~n(t)~x~n(t)~ until no more mistakes
* 返回最后得到的 w 为 g, 这个 w 称为 w~pla~

### Cyclic PLA

* For t = 0,1,...
* find the next mistake of wt called (x~n(t)~, y~n(t)~), aka sign(w~t~^T^x~n(t)~) 不等于 y~n(t)~
* correct the mistake by w~t+1~ <- w~t~ + y~n(t)~x~n(t)~
* until a full cycle of not encountering mistakes
* 可以采用标准的遍历，或者也可以是预先计算好的随机顺序

### Linear Separability 线性可分

* if PLA halts, (necessary condition) D allows some w(一条用来区分的线) to make no mistake
* 有一条线可以区分数据，即有解，有解的时候 PLA 算法才会停

### PLA Fact: W~t~ Gets More Aligned with W~f~

+ 线性可分，则存在一条完美的直线 W~f~(即目标函数) 使得 y~n~ = sign(W~f~^T^ x~n~)
+ 也就是 y~n~ 的符号，与 W~f~^T^ 和 x~n~ 的乘积(也就是 x~n~ 到直线 W~f~ 的距离)的符号，一定是相同的
+ ![mlf3](./_resources/mlf3.jpg)
+ W~t~ 为当前次迭代的直线，找出一个错误的点，然后做更新
+ 通过不等式可以得到，下一次迭代得到的直线，会更加接近于完美的直线 W~f~ ，因为乘积越来越大了(但是乘积还需要考虑向量的长度，这里说的是角度，下面就是说长度)

### PLA Fact: W~t~ Does Not Grow Too

+ W~t~ changed only when mistake
+ 也就是只有在 sign(W~t~^T^ x~n(t)~) 不等于 y~n(t)~ 也就是 y~n(t)~w~t^T^x~n(t)~ <= 0
+ ![mlf4](./_resources/mlf4.jpg)
+ 平方之后来看长度的公式，蓝色部分通过上面的推导可知是小于等于零的
+ y~n~ 是正负 1，所以下一次迭代的向量的长度的增长是有限的，最多增长 x~n~^2^ 那么多(也就是长度最大的向量)
+ 然后推导出来 w~t~ 确实是越来越靠近 w~f~ 的

### 一个习题

+ ![mlf5](./_resources/mlf5.jpg)
+ 具体怎么推导的呢，研究了半个多小时终于弄清楚了，如下
+ W~f~ 是理论上完美的那条线，w~t~ 是第 t 次迭代得到的那条线，而因为这两条线最好结果就是完全平行，所以有
    + (W~f~^T^ / || W~f~ ||) * (w~t~ / || w~t~ ||) 的最大值为 1 (`eq1`)
+ 由前面 PPT 得到的两个公式：
    + W~f~^T^w~t+1~ >= W~f~^T^w~t~ + min~n~y~n~W~f~^T^x~n~ (`eq2`)
    + w~t+1~^2^ <= w~t~^2^ + max(n)x~n~^2^ (`eq3`)
+ 因为是迭代 T 次，把 `eq2` 和 `eq3` 代入到 `eq1` 中
    + W~f~^T^w~t~ / || w~f~ || 这部分就是条件里的 p，因为迭代 T 次，所以分子变成 T·p
    + 分子是 || w~t~ ||，根据 `eq3` 可知迭代 T 次后为 √(T·R^2^)
+ 又因为 `eq1` 的最大值为1，可以求出 T 的范围，得到答案

### More about PLA

+ Guarantee: as long as **linear separable** and **correct by mistake**
    + inner product of w~f and w~t grows fast; length of w~t grows slowly
    + PLA 'lines' are more and more align with W~f~ -> halts
+ Pros
    + Simple to implement, fast, works in any dimensin d
+ Cons
    + **'Assumes' linear separable D** to halt(property unknown in advance)
    + Not fully sure **how long halting takes**(p depends on W~f~) -though practically fast
+ What if D not linear separable?

### Learning with **Noisy Data**

+ ![mlf6](./_resources/mlf6.jpg)
+ Line with Noise Tolerance
    + ![mlf7](./_resources/mlf7.jpg)
    + 在看到的数据中，找犯错误最少的一条(但是这是一个很难的问题)

### Pocket Algorithm

+ modify PLA algorithm (black lines) by **keeping best weights in pocket**
+ ![mlf8](./_resources/mlf8.jpg)
+ 例题时间
+ ![mlf9](./_resources/mlf9.jpg)

## Lecture 3: Types of Learning

### Different Output Space

+ 二元分类与多元分类
+ 例子：Patient Recovery Prediction Problem
    + binary classification: patient features -> sick or not
    + multiclass classification: patient features -> which type of cancer
    + regression(回归分析)
        + patient features -> how many days before recovery
        + compnay data -> stock price
        + climate data -> temperature
+ 统计上有很多工具也可以放到机器学习里来用
+ Structured Learning
    + Sequence Tagging Problem 词性标注
    + protein data -> protein folding
    + speech data -> speech parse tree

### Different Label

+ 监督式学习
    + ![mlf10](./_resources/mlf10.jpg)
+ 非监督式学习
    + ![mlf11](./_resources/mlf11.jpg)
+ 其他一些非监督式学习
    + ![mlf12](./_resources/mlf12.jpg)
    + diverse, with possibly very different performance goals
+ 半监督式学习
    + 只提供有限信息，只标记一部分，蓝色的是没有标记的，其他颜色是标记出来的
    + ![mlf13](./_resources/mlf13.jpg)
    + leverage unlabeled data to avoid 'expensive' labeling

### Different Protocol

+ Reinforcement Learning
    + 惩罚错误判断，鼓励正确判断
    + learn with **partial/implicit information**(often sequentially)
+ Batch Learning 填鸭式教育
    + ![mlf14](./_resources/mlf14.jpg)
    + batch learning: **a very common protocol**
+ Online 老师教书
    + hypothesis 'improves' through receiving data instances sequentially
    + PLA can be easily adapted ton online protocol
    + reinforcement learning is often done online
+ Active Learning
    + ![mlf15](./_resources/mlf15.jpg)

### Different Input Space

+ Concrete features: the 'easy' ones for ML
+ Raw features -> meaning of digit(比方说笔迹识别，把图像转换成数字化的信息，可以是对称性或者密度，或者直接转化成二维数组，越抽象，对于机器来说就越困难)
    + often need human or machines to **convert to concrete ones**
    + 要么是人工来做，要么就是 deep learning 自动来做
+ Abstract features: **no** physical meaning, even harder for ML
    + 比方说评分预测问题(KDDCup 2011)
    + need **feature conversion**/extraction/construction

## Lecture 4: Feasibility of Learning

+ Inferring Something Unknown
    + diificult to infer **unknown target f outside D** in learning
    + 抽样调查
+ **Hoeffding's Inequality**
    + 只是给出一个比较高的上限
    + probably approximately correct(PAC)

### Hoeffding's Inequality

用一个从罐子里取玻璃球作为例子，有两种玻璃球：橙色和绿色。假设：

    橙色的概率为 u
    则绿色的概率为 1-u
    但 u 具体是多少我们不知道

然后我们从中取出 `N` 个样本：

    橙色的比例为 v
    则绿色的比例为 1-v
    这时我们是知道 v 具体是多少的

> Does **in-sample v** say anything about out-of-sample u?

+ Possibly not: sample can be mostly green while bin is mostly orange
+ Probably yes: in-sample v likely **close to** unknown u

> Formally, what does v say about u?

    u = orange probability in bin
    v = orange fraction in sample

![mlf16](./_resources/mlf16.jpg)

抽样数量足够大的时候，抽样得到的概率 v 和实际概率 u 相差的概率会很小(Heoffding's Inequality)

The statement `v = u` is **probably approximately correct**(PAC)

根据上面的公式我们知道，其实要知道抽样得到的概率 v 和实际概率 u 相差多少，只跟误差和抽样的数量有关。

If **large N**, can **probably** infer unknown u by known v

### Connect to Learning

瓶中的情况 | 对应到 Learning
--- | ---
unknown orange prob. u | fixed hypothesis h(x) ? target f(x)
marble in bin | x 在 X 中
orange | h is wrong -> h(x) 不等于 f(x) aka orange
green | h is right -> h(x) 等于 f(x) aka green
size-N sample from bin | check h on D = {(x~n~, y~n~)} 这里 y~n~ 就是 f(x~n~)

![mlf17](./_resources/mlf17.jpg)

![mlf18](./_resources/mlf18.jpg)

E~out~(h) 对应于 总体概率 u，E~in~(h) 对应于抽样概率 v

![mlf19](./_resources/mlf19.jpg)

Does not depend on E~out~(h),**no need to know E~out~(h)**

E~in~(h) = E~out~(h) is **probably approximately correct**(PAC)

![mlf20](./_resources/mlf20.jpg)

**BAD** sample: **E~in~ and E~out~ far away**

can get **worse** when involving 'choice'

Hoeffding 保证的是出现 Bad Sample 的机会不会很大

![mlf21](./_resources/mlf21.jpg)

什么意思呢？如果hypothesis set是有有限种选择，训练样本够多，那么不管学习算法A怎么选择，样本的判别结果都会与总体的一致。那么，如果学习算法设计为寻找样本中错误率最小的，那么刚刚的推论PAC就能保证选出来的g与f是约等于的。

也就是说，当有 M 个 hypothesis 的时候，对应的误差也会变大，但是依然可以找到一个情况，此时

E~in~(g) = E~out~(g) is **PAC, regardless of A**

Most reasonable A(like PLA/pocket): pick the h~m with **lowest E~in~(h~m~) as g

![mlf22](./_resources/mlf22.jpg)

不过仍然有一个遗留问题，刚刚的推论是在hypothesis set有限的前提下，那类似于PLA的hypothesis set是无穷的又如何呢？不用紧张，以后会证明这个问题。现在至少在有限的情形下证明了，这是一个很好的出发点。

## Lecture 5: Training versus Testing

![mlf23](./_resources/mlf23.jpg)

### Two Central Questions

![mlf24](./_resources/mlf24.jpg)

+ Can we make sure that E~out~(g) is close enough to E~in~(g)
+ Can we make E~in~(g) small enough?

### Trade-off on M

M 也就是 hypothesis 的集合，对于不同的值，对于上面两个问题有两个不同的解答

Small M | Large M
--- | ---
Yes! P[BAD] <= 2·M·exp(...) | No! P[BAD] <= 2·M·exp(...)
No! too few choices | Yes!, many choices

这样就两难了，M 小的时候，可以保证 E~out~(g) 和 E~in~(g) 足够接近，但是不能保证 E~in~(g) 足够小；M 大的时候则是相反的情况。如何选择正确的 M 呢？尤其是 M 可能是无限多的情况怎么办呢？

现在的情况就是这个公式和 M 有关

![mlf25](./_resources/mlf25.jpg)

所以想办法能不能把可能无限大的 M，弄成有限的数量 m~H

![mlf26](./_resources/mlf26.jpg)

### Where Did M Come From

![mlf27](./_resources/mlf27.jpg)

之前的讨论中，我们直接把概率的 or 转化为概率的相加，因为我们假设这些 BAD case 不大可能会重叠，但是当 M 很大的时候，这种做法(Uniform Bound)就不行了。为什么呢？

因为假如 h~1 很接近于 h~2~,则 E~out~(h~1~) 会很接近 E~out~(h~2~)，并且很有可能 E~in~(h~1~) = E~in~(h~2~)

Union bound **over-estimating** 很多重复的也被计算进去了。那么对于这种情况，如果我们能 group similar hypothesis by **kind**，就可以减少误差。

### How Many Lines Are There?

考虑平面上所有的线 H = {all lines in R^2^}

+ How many lines? 无限多条
+ How many **kinds of** lines if viewd from one input vector x~1?
    + 两种，一种划分 x~1 是圈，另一种划分 x~1 是叉
    + 2 kinds: h~1~-like(x~1~) = o or h~2~-like(x~1~) = x

如果从两个点的角度来看呢？有 4 种线，x~1 和 x~2 的组合可能是：oo, xx, xo, ox

三个点的情况下呢？通常情况下有 8 种线，x~1~, x~2~, x~3~ 的组合可能是：ooo, xxx, oox, xxo, oxo, xox, oxx, xoo

但是如果三点共线的话，就只有 6 种线了。

四个点的情况下呢？至多只有 14 种线了。(指的是线性可分的线的种类的数量)

### Effective Number of Lines

maximum kinds of lines with respect to N inputs x~1~, x~2~, ..., x~N~ -> **effective number of lines** 可能的有效划分的线种类数量

![mlf28](./_resources/mlf28.jpg)

这里用 `effective(N)` 代替了原来的 `M`，如果 `effective(N)` 远小于 2^N 的话，那么就可能解决无穷条线的问题了

### Dichotomies: Mini-hypothesis

![mlf29](./_resources/mlf29.jpg)

用 Dichotomies Set 的大小来代替 M，但是现在会依赖于不同点的选取，需要做进一步的修改

### Growth Function

![mlf30](./_resources/mlf30.jpg)

注意这里这个 m~H~(N) 是重要的符号

#### Growth Function for Positive Rays

![mlf31](./_resources/mlf31.jpg)

N+1

#### Growth Fucntion for Positive Intervals

![mlf32](./_resources/mlf32.jpg)

0.5N^2 + 0.5N + 1

#### Growth Function for Convex Sets

![mlf33](./_resources/mlf33.jpg)

![mlf34](./_resources/mlf34.jpg)

### The Four Growth Functions

![mlf35](./_resources/mlf35.jpg)

#### Break Point of H

指的是增长函数中第一个有希望的点(也就是增长趋势放缓的点)，比方说之前三个点我们可以做出 8 种线，但是四个点的时候却不能做出 16 种线，所以 4 就是一个 break point。

![mlf36](./_resources/mlf36.jpg)

## Lecture 6: Theory of Generalization

E~out~ ≈ E~in~ possible if **m~H~(N) breaks somewhere** and **N large enough**

growth function m~H~(N): max number of dichotomies

![mlf37](./_resources/mlf37.jpg)

### Restriction of Break Point

what 'must be true' when **minimum break point** k = 2

+ N = 1: every m~H~(N) = 2 by definition
+ N = 2: every m~H~(N) < 4 by definition (so **maximum possible = 3)
+ N = 3: **maximum possible = 4 远小于 2^3^**

既然如此，换一个角度来考虑的话那么更General的情况是：如果现在已知minimum break point k = 2，在样本量N不同的情况下对应的Dichotomies大小又是如何的状况呢？k = 2这里的意义就是说任意的两个样本点都无法被shatter到（shatter到的意思：n个样本点的2^n个情形都能出现，这里就是指2个样本点的4种情形都能出现）。

break point k **restricts maximum possible m~H~(N) a lot** for N > k

idea: m~H~(N) <= **maximum possible m~H~(N) given k** <= poly(N) N 的多项式时间

m~H~(N)跟我们实际上的 hypothesis set 有关，我们不如来算一下 m~H~(N)在有某一个break point的前提下，到底能产生多少种可能性。如果最多的可能性，也即 m~H~(N)的最大值也是一个多项式的话，那么就可以放心大胆的说 m~H~(N)也是多项式的。进而，如果能将这个多项式的 m~H~(N) 成功地放进我们原来的 Hoeffding 不等式的话，也许我们就可以说在PLA这样的无穷 hypothesis set 上的 Learning 是做得到的。

### Bounding Function

**bounding function B(N, k)**: maximum possible m~H~(N) when break point = k

+ combinatorial quantity: maximum number of length-N vectors with (o, x) while **no shatter any length-k** subvectors
+ irrelevant of the details of H.

new goal: B(N, k) <= poly(N)?

B(N, k) <= B(N-1, k) + B(N-1, k-1)

now we have **upper bound** of bounding function

![mlf38](./_resources/mlf38.jpg)

+ simple induction using **boundary and inductive formula**
+ for fixed k, B(N, k) upper bounded by poly(N) -> **m~H~(N) is poly(N) if break point exists
+ `<=` can be `=` actually

### BAD Bound for General H

![mlf39](./_resources/mlf39.jpg)

具体的证明主要分以下几步

#### Step 1: Replace E~out~ by E~in~'

![mlf40](./_resources/mlf40.jpg)

第一步，想办法将式子中的 E~out~(h) 替换掉。hypothesis set只要有一个 h 发生坏事情，也就是 E~in~(h) 与 E~out~(h) 差别很大，我们就说这个训练数据 D 不是好的数据，我们希望坏数据 D 发生的概率不要太高。

+ E~in~(h) finitely many, E~out~(h) infinitely many
+ How? sample **verification set D'** of size N to calculate E~in~'
+ BAD h of E~in~ - E~out~ 可以大概近似于 BAD h of E~in~ - E~in~'

这样一来 evil E~out~ removed by verification with **ghost data**

#### Step 2: Decompose H by Kind

想办法将 Hypothesis set 换成某一个 h。如下图所示，现在在乎的所有和 BAD 有关的只是 E~in~(h) 和 E~in~(h)' 来决定了。也就是说，如果 h 在 D 与 D’ 上做出一样的 dichotomy 的话，那么 E~in~(h) 和 E~in~(h)' 就会长一样。所以我只要把所有的 hypothesis set 分成 |H(x1, x2…, x’1, x’2…)| 这么多类就好，也就是在这 2N 个点上有多少种 Dichotomies 就好了。这样的话最多最多有 m~H~(2N) 种，把每一种抓一个代表出来我们就可以使用 union bound 了。

![mlf41](./_resources/mlf41.jpg)

![mlf42](./_resources/mlf42.jpg)

use m~H~(2N) to calculate BAD-overlap properly

#### Step 3: Use Hoeffding without Replacement

![mlf43](./_resources/mlf43.jpg)

![mlf44](./_resources/mlf44.jpg)

use **Hoeffding** after zooming to fixed h

现在我们已经是固定的 h，想知道两次 sampling 的差别。就好像我们先有 2N 个样本的例子，我们抓 N 个出来然后比较剩下的 N 个；或者说我们抓 N 个出来，比较它跟所有 2N 个的平均是多少。如果想要 E~in~(h) 和 E~in~(h)' 相差 alpha 的话，那么 E~in~(h) 与所有人的平均需要相差 alpha/2。那怎么知道 E~in~(h) 与所有 2N 的差别呢？没错，就是使用 Hoeffding 不等式来解决，只不错这次罐子变得更小，变得有限的 2N 个了。

### Vapnik-Chervonenkis (VC) bound:

![mlf45](./_resources/mlf45.jpg)

## Lecture 7: The VC Dimension

if **finite d~vc~**, **large N**, and **low E~in~**

如果成长函数在 k 处有 break point，那么这个成长函数会被一个上限函数所限制，这个上限函数又会被某个多项式限制，这个多项式是 k-1 次方

![mlf46](./_resources/mlf46.jpg)

![mlf47](./_resources/mlf47.jpg)

### More on Vapnik-Chervonenkis(VC) Bound

![mlf48](./_resources/mlf48.jpg)

![mlf49](./_resources/mlf49.jpg)

### VC Dimension

the formal name of **maximum non-**break point

![mlf50](./_resources/mlf50.jpg)

+ N <= d~vc~ -> H can shatter some N inputs
+ k > d~vc~ -> k is a break point for H

if N >= 2, d~vc~ >= 2, m~H~(N) <= N 的 d~vc~ 次方

![mlf51](./_resources/mlf51.jpg)

good: **finite d~vc~**

### VC Dimension and Learning

**finite d~vc~ -> g will generalize E~out~(g) ≈ E~in~(g)**

+ regardless of learning algorithm A
+ regardless of input distribution P
+ regardless of target function f

![mlf52](./_resources/mlf52.jpg)

### 2D PLA Revisited

如果现在 2D 里面我们的数据是 **linearly separable D**，那么 **PLA can converge**，也就是说，当迭代次数 T 足够大的时候，我们可以找到一条线，这条线把所有 data 正确分类，也就是 **E~in~(g)=0**。

如果这些 data 是从某个分布中(具体是什么分布不重要)以及某个target function得来的，即 **with x~n~ ~ P and y~n~ = f(x~n~)**，我们有很大的机会说他们的 E~in~(g) 和 E~out~(g) 是很接近的，因为我们知道了 d~vc~ 是有限的。当 N 很大的时候，可以知道 **E~out~(g) ≈ E~in~(g)**

![mlf53](./_resources/mlf53.jpg)

那么问题来了: general PLA for x with **more than 2 features** 怎么办呢

### VC Dimension of Perceptrons

+ 1D perceptro (pos/neg rays): d~vc~ = 2
+ 2D perceptrons: d~vc~ = 3
    + 如何证明的呢？
    + 三个点的情况下，我们找到一种方式可以shatter，于是 d~vc~ >= 3
    + 四个点的情况下，我们发现所有方式都不可以shatter，于是 d~vc~ <= 3
    + 于是 d~vc~ = 3
+ d-D perceptrons: d~vc~ ? d+1 如何证明呢

### 证明 d~vc~ >= d+1

**一个习题**

![mlf54](./_resources/mlf54.jpg)

There are **some d+1 inputs** we can shatter

![mlf55](./_resources/mlf55.jpg)

注意：X **invertible**

怎么样可以保证 shatter 呢，对于任何一组输入 y，存在这样的 w 保证 Xw 的符号等于 y

![mlf56](./_resources/mlf56.jpg)

'special' X can be shattered -> d~vc~ >= d+1

### 证明 d~vc~ <= d+1

**一个习题**

![mlf57](./_resources/mlf57.jpg)

要证明所有可能性都不行。

linear dependence **restricts dichotomy**

![mlf58](./_resources/mlf58.jpg)

'general' X no-shatter -> d~vc~ <= d+1

### Degrees of Freedom

+ hypothesis parameters w = (w~0~, w~1~,..., w~d~): creates degrees of freedom
+ hypothesis quantity M = |H|: 'analog' degrees of freedom
+ hypothesis 'power' d~vc~ = d+1: **effective 'binary' degrees of freedom**

物理意义是 hypothesis set 在做二元分类的时候有多少自由度(就是有多少可控的参数)

我们发现，d+1 实际上就是perceptron 的维度，所以 VC dimension 就和 perceptron 的维度联系起来了。hypothesis set 是由 d+1 维的 w 来表示的，而这些 w 可以代表着 hypothesis 的自由度 degrees of freedom。所以 VC dimension 的物理意义就是 effective ‘binary’ degrees of freedom，hypothesis set 在作二元分类的状况下到底有多少的自由度。同时也就象征着 powerfulness of H，到底能够产生多少的dichotomies。

d~vc~(H): powerfullness of H

![mlf59](./_resources/mlf59.jpg)

practical rule of thumb: **d~vc~ ≈ #free parameters(but not always)**

**using the right d~vc~ (or H) is important**

### VC Bound Rephrase: Penalty for Model Complexity

VC dimension的一种意义是表征着 model complexity。

![mlf60](./_resources/mlf60.jpg)

坏事情发生的机会很小，也就是好事情发生的机会很大

![mlf61](./_resources/mlf61.jpg)

信赖区间，一般比较在意右边的部分，考虑最坏情况。

根号里面的部分是 penalty for **model complexity** Ω(N, H, δ)

### THE VC Message

![mlf62](./_resources/mlf62.jpg)

**powerful H** not always good

### VC Bound Rephrase: Sample Complexity

VC bound还有另外的一种含义：Sample Complexity样本复杂度。

![mlf63](./_resources/mlf63.jpg)

prictical rule of thumb: **N ≈ 10d~vc~ often enough!**

### Looseness of VC Bound

![mlf64](./_resources/mlf64.jpg)

**philosophical message** of VC bound important for improving ML

## Lecture 8: Noise and Error

learning can happen with **target distribution P(y|x)** and **low E~in~ w.r.t. err**

噪声是容易出现的，人工标记错误；同一个数据不同人工标记不同；训练数据收集可能不精准等等原因。那么在有噪声的时候，我们之前推导的 VC bound 是否仍然能作用的很好？

回想一下，VC bound 的核心：我们不知道一个罐子里有多少橘色的弹珠，不过我们抓一把出来就可以估计橘色的弹珠有多少，这些橘色的弹珠就是我们犯错误的地方。噪声的影响就是特别的弹珠，弹珠的颜色不是固定的，譬如弹珠40%是橘色的，60%的时候是绿色的。那这时候我们如何知道罐子大致的橘色的比例是多少呢。

![mlf65](./_resources/mlf65.jpg)

### Target Distribution P(y|x)

也就是说，只要我们的每个训练数据 y 来自某一个 joint distribution P(y|x)，我们在训练的时候和测试的时候都符合 P(y|x)，那么这个 VC bound 的大架构还是有效的。P(y|x) 通常叫做 **target distribution**，对于每一个 x 可以做一个它最理想的预测 **mini-target** 是什么。它告诉我们最理想的预测 **ideal mini-target** 是什么，另外不理想的就是 noise 。例如 P(o|x) = 0.7, P(x|x) = 0.3，也就是说现在拿了一颗弹珠它是圈圈概率是0.7，请问你是要猜圈圈还是要猜叉叉。当然最好猜它是圈圈，那么错误率就是0.3。

那么之前固定的 target f 可以认为是目前 target distribution 的一种特例，这时候P(y|x) = 1 for y = f(x)也就是完全没有噪声。使用 target distribution 的时候和之前是用 target function 的时候基本上没有什么太大的不一样。

所以回头来看，我们 Learning 的目标分为两个部分了 predict **ideal mini-target(w.r.t. P(y|x))** on **often-seen inputs(w.r.t. P(x))**，一个是原先的 P(x)，它告诉我们哪些点是重要的常常会被抽样到也就是在 E~in~(h) 里经常出现；另外一个是 P(y|x)，它告诉我们最理想的 mini-target 是什么。在常见的点上的预测要做的表现好，这就是 machine learning 做的事情。

![mlf66](./_resources/mlf66.jpg)

新的流程，区别在于左上角不再是一个固定的 target function 而是一个 target distribution，要保证训练和测试的数据都是从同一个分布产生的。

VC still works.

### Error Measure

final hypothesis g ≈ f

如何衡量 g 跟 f 是长的很像的呢？之前使用的是 E~out~(g)，有三个特性：**out of sample** 衡量的是还没有看过或者是未来抽样出来的x，**point-wise** 可以在每一个x上个别衡量，最后做抽样的平均就可以了，**classification** 二元分类考虑的就是对或者不对。实际上有很多的错误衡量的方式，不过为了简单起见大部分的主要集中在 point-wise 的方式。

![mlf67](./_resources/mlf67.jpg)

![mlf68](./_resources/mlf68.jpg)

### Two Important Pointwise Error Measures

![mlf69](./_resources/mlf69.jpg)

那有哪些 Point-wise 的错误衡量方式呢？0/1 error 通常用在分类上，分对还是分错；平方的 error 通常用在回归分析，计算错误的距离。未来会讲更多不同错误衡量方式。不同的错误衡量方式，会影响到最理想的 mini-target，也就是最好的 f 会长什么样。

VC 理论对于很多不同的 hypothesis set 还有很多不同的错误衡量方式来说都会 work。也就是说，不管是 classification 还是 regression，不只是0/1的错误衡量，都能得到类似的 VC bound。详细的数学推导太过于繁复，大家没有必要都走过一遍。

0/1 找最大概率的那个；平方 找加权平均值

于是新的 Learning Flow 会加上 Error Message 的部分

![mlf70](./_resources/mlf70.jpg)

**一个习题**

![mlf71](./_resources/mlf71.jpg)

### Choice of Error Measure

这些错误的衡量到底哪里来的呢？想象一个指纹分类系统，分类器可能会犯两种错误：false accept，应该要说不可以用，但是分类器说可以用；false reject，明明应该可以用，但是分类器说不可以用。其实也就是我们在分类中常说的 false positive 和 false negative，只是台湾和大陆的叫法不同而已。对于这两种错误的类型，之前的 0/1 error penalizes both types equally。然而，在实际应用中，两种错误带来的影响可能很不一样。

![mlf72](./_resources/mlf72.jpg)

但是很多时候错误衡量的具体权重是不太能确定的，所以在设计算法的时候常常要采用替代的方式。一种替代方式是找一些有意义的错误衡量，例如之前 Pocket PLA 在进行 0/1 分类时如果分不对就认为是噪声，想办法让噪声最小也就是 0/1 error 最小(NP hard问题之前有提到)。以及以后会讲到的距离平方的方式，想办法高斯噪声最小；另外一种替代方式会更 friendly，例如很容易求出解，或者凸优化的目标函数等。

![mlf73](./_resources/mlf73.jpg)

### Weighted Classification

不同的错误有不同的惩罚

![mlf74](./_resources/mlf74.jpg)

weighted classification: **different 'weight' for different (x, y)**

### Minimizing E~in~ for Weighted Classification

目标还是让 E~in~^w^(h) 越小越好

![mlf75](./_resources/mlf75.jpg)

![mlf76](./_resources/mlf76.jpg)

一种比较机械的方式就是，在训练开始前，我们将{(x,y) | y=-1} 的数据复制1000倍之后再开始学习，后面的步骤与传统的 pocket 方法一模一样。然而，从效率、计算资源的角度考虑，通常不会真的将 y=-1 的数据拷贝 1000 倍，实际中一般采用”virtual copying”。

![mlf77](./_resources/mlf77.jpg)

只要保证：randomly check -1 example mistakes with 1000 times more probability。也就是说，pocket 随机访问-1错误点的几率在概率上要比非权重PLA算法时访问-1错误点的几率高了1000倍。

systematic route(called 'reduction') can be applied to many other algorithm

**一个习题**

![mlf78](./_resources/mlf78.jpg)

总之，我们选择好适合特定应用的error measure: err，然后在训练时力求最小化err，即，我们要让最后的预测发生错误的可能性最小（错误测量值最小），这样的学习是有效的。

## Lecture 9: Linear Regression

![mlf102](./_resources/mlf102.jpg)

例如，信用卡额度预测问题：特征是用户的信息（年龄，性别，年薪，当前债务，…），我们要预测可以给该客户多大的信用额度。 这样的问题就是回归问题。目标值 y 是实数空间 R。线性回归的假设 hypothesis 是 h(x) = w^T^x

For x = (x~0~, x~1~, x~2~,..., x~d~) 'features of customer', approximate the **desired credit limit** with a **weighted** sum:

![mlf79](./_resources/mlf79.jpg)

怎么理解？向量 x 就代表客户的不同信息，然后通过这个 hypothesis，也就是不同的权重向量 w，相乘得到一个实数

h(x): like **perceptron**, but without the **sign**

**linear regression**: find lines/hyperplanes with small **residuals**

### The Error Measure

![mlf80](./_resources/mlf80.jpg)

这里之所以可以直接用 w 代替 h，因为每个不同的 hypothesis 实际上就是对应不同的权重

所以现在的问题就是最小化 E~in~(w)

### Matrix Form of E~in~(w)

![mlf81](./_resources/mlf81.jpg)

然后就可以得到下面的式子：

![mlf82](./_resources/mlf82.jpg)

这是一个连续可微凸函数，要找到最低点，表示不管到哪个方向都没有办法更低，也就是对应点的梯度(在每个方向上做偏微分)为零

![mlf83](./_resources/mlf83.jpg)

找到一个 W~LIN~,在各个方向偏微分为零

### The Gradient ▽E~in~(w)

![mlf84](./_resources/mlf84.jpg)

假设我们的 w 是一维的，那么上面的式子就变成了一个一元二次方程，求微分就很简单，对 w 求导即可。如果 w 是一个向量，那么就可以按照如下的方式来进行对梯度的求解(其实和一维的情况很像)

![mlf85](./_resources/mlf85.jpg)

所以整个式子是这么写：

▽E~in~(w) = 2/N * (X^T^Xw - X^T^y)

### Optimal Linear Regression Weights

task: find W~LIN~ such that ▽E~in~(w) = 2/N * (X^T^Xw - X^T^y) = 0

![mlf86](./_resources/mlf86.jpg)

如果 X^T^X 可逆的话，那么问题很简单(有唯一解)，可以直接求出 W~LIN~，并且大部分情况可能是如此。如果不可逆的话，就有很多组解，但是依然可以找到 pseudo-inverse，因此找到 W~LIN~

![mlf87](./_resources/mlf87.jpg)

实际上，无论哪种情况，我们都可以很容易得到结果。因为许多现成的机器学习/数学库帮我们处理好了这个问题，只要我们直接调用相应的计算函数即可。有些库中把这种广义求逆矩阵运算成为 pseudo-inverse。

### Linear Regression Algorithm

![mlf88](./_resources/mlf88.jpg)

有比较好的 pseudo-inverse 的话，这个算法非常简单有效

**一个习题**

![mlf89](./_resources/mlf89.jpg)

### Is Linear Regression a 'Learning Algorithm'?

![mlf90](./_resources/mlf90.jpg)

从某些角度来说，不算是，但是从某些角度来说，也是学习的算法

![mlf91](./_resources/mlf91.jpg)

if E~out~(W~LIN~) is good, learning 'happened'!

### Benefit of Analytic Solution: 'Simpler-than-VC' Guarantee

![mlf92](./_resources/mlf92.jpg)

接下来，我们试图求一下E~in~，E~out~ 的平均范围，会比求解VC bound更为简单。

### Geometric View of **Hat Matrix**

![mlf93](./_resources/mlf93.jpg)

N 维的空间里，y 是在 N 维空间里的向量，那么我要做预测也就是y^hat^ = Xw~LIN~，w 做的事情就是把 X 的每一个 column 作线性组合，X 的每一个 column 也是一个N维的向量。也就是说，X 拿出每个 column 可以展开成在 N 维度里面一个小的空间，然后 y^hat^ 会在这个空间里面。Linear Regression 要做什么？希望y与y^hat^的差别越小越好，也就是 y – y^hat^ 垂直于这个小空间的时候。所以，H 这个矩阵的作用就是把任何一个向量 y 投影到 X 所展开的那个空间里；I-H 的作用就是求解任何一个向量 y 对于 X 所展开的空间的余数。

trace(I-H) 对角线上的值加起来是多少。trace(I – H)的物理意义：我们原来有一个n个自由度的向量，现在我们将其投影到d+1维的空间（因为X有d+1个向量展开），然后取余数，剩下的自由度最多就是N – (d + 1)。

![mlf94](./_resources/mlf94.jpg)

注意到 E~in~ 算的是y – y^hat^，即垂直于平面的距离。而另一个角度来说，y 可以认为是真实的 f(X) + noise的向量，我们会发现将 noise 投影在平面上求解的垂直于平面的距离实际上也就是 y – y^hat^。也就是说，我们现在要求解的 E~in~ 其实就是把I – H 这个线性的变换用在 noise 上面。于是就可以得到E~in~的平均范围，E~out~ 平均范围的求解会相对复杂这里省略。

### The Learning Curve

![mlf95](./_resources/mlf95.jpg)

通过 E~in~ 和 E~out~ 的式子通常就，可以画出一个图通常叫做学习曲线。所以，所谓的 generalization error 也就是 E~in~ 与 E~out~ 的差距，平均来说就是 2(d+1)/N。如果还记得的话，在有 d+1 个自由度时，VC bound最坏情况下是 d+1。所以 Linear regression的 学习真的已经发生了。

linear regression (LinReg): learning 'happened'!

**一个习题**

H: projection y to y^hat^

![mlf96](./_resources/mlf96.jpg)

### Linear Classification vs. Linear Regression

![mlf97](./_resources/mlf97.jpg)

![mlf98](./_resources/mlf98.jpg)

那能否直接用 Linear regression 来解分类问题就好？听起来有点道理。

![mlf99](./_resources/mlf99.jpg)

之所以能够通过线程回归的方法来进行二值分类，是由于回归的 squared error 是分类的 0/1 error 的上界(平方的错误一定比0/1的错误大)

![mlf100](./_resources/mlf100.jpg)

用一个宽松一点但是更好算的限制来简化。

我们通过优化 squared error，一定程度上也能得到不错的分类结果；或者，更好的选择是，将回归方法得到的 w 作为二值分类模型的初始 w 值。

W~LIN~: useful baseline classifier, or as initial PLA/pocket vector 用作一开始的 w~0~，就可以加速 PLA/pocket 的运算

**一个习题**

![mlf101](./_resources/mlf101.jpg)

## Lecture 10: Logistic Regression

**gradient descent** on **cross-entropy error** to get good **logistic hypothesis**

有一组病人的数据，我们需要预测他们在一段时间后患上心脏病的“可能性”，就是我们要考虑的问题。通过二值分类，我们仅仅能够预测病人是否会患上心脏病，不同于此的是，现在我们还关心患病的可能性，即 f(x) = P(+1|x)，取值范围是区间 [0,1]。

然而，我们能够获取的训练数据却与二值分类完全一样，x 是病人的基本属性，y 是 +1(患心脏病)或 -1（没有患心脏病）。输入数据并没有告诉我们有关“概率” 的信息。在二值分类中，我们通过 w*x 得到一个 ”score” 后，通过取符号运算 sign 来预测 y 是 +1 或 -1。而对于当前问题，我们如过能够将这个 score 映射到[0,1] 区间，问题似乎就迎刃而解了。

same data as hard binary classification, different **target function**

我们手上的数据可以看成是我们想要资料的有噪声的版本，在噪声的基础上我们来找到最接近真实的情况

![mlf103](./_resources/mlf103.jpg)

同样是根据权重算出一个分数，但是会通过另一个函数θ 来把这个分数映射到0到1的区间

### Logistic Function

![mlf104](./_resources/mlf104.jpg)

平滑可微 S 形函数

![mlf105](./_resources/mlf105.jpg)

**一个习题**

![mlf106](./_resources/mlf106.jpg)

### Three Linear Models

linear scoring functions: s = w^T^x

![mlf107](./_resources/mlf107.jpg)

how to define **E~in~(w) for logistic regression**?

### Likelihood

在机器学习假设中，数据集 D 是由 f 产生的，我们可以按照这个思路，考虑 f 和假设 h 生成训练数据 D 的概率是多少？首先要产生 x~1~，概率是 P(x~1~)，然后产生 y~1~，概率是 P(y~1~ | x~1~)。

![mlf108](./_resources/mlf108.jpg)

这里可以对 P(o|x~1~) P(x|x~2~) ...进行代换，变成下面的形式

![mlf109](./_resources/mlf109.jpg)

如何想要 h 与 f 很接近的话，那么 h 产生数据 D 的可能性与 f 真正产生这些数据的可能性就会很接近，训练数据的客观存在的，显然越有可能生成该数据集的假设越好。也就是 h 产生数据 D 的可能性是最高的。

![mlf110](./_resources/mlf110.jpg)

logistic hypothesis有一个数学上的特性：1 - h(x) = h(-x)。所以 likelihood(h) 就可以化简为如下图所示，其中灰色的 P(x) 是一系列的常数。所以，likelihood(logistic h) 正比于如下的连乘。

![mlf111](./_resources/mlf111.jpg)

利用上面的特性替换之后：

![mlf112](./_resources/mlf112.jpg)

### Cross-Entropy Error

把上面的公式用 w 和 θ 代入之后，可以得到下面的公式

![mlf113](./_resources/mlf113.jpg)

前面有 h(x) = θ(w^T^x)

但是这里是连乘，不是特别好处理，我们这里取对数，就可以把连乘变成连加

![mlf114](./_resources/mlf114.jpg)

之前我们都做的是最小化，所以增加一个负号，变成最小化，然后在除以一个 N，做一个常数的 scaling

![mlf115](./_resources/mlf115.jpg)

把 θ 具体代入到上面的公式，就可以得到

![mlf116](./_resources/mlf116.jpg)

err(w, x, y) = ln(1 + exp(-ywx)) **cross-entropy error**

是一个 point-wise 的 error function

**一个习题**

![mlf117](./_resources/mlf117.jpg)

### Minimizing E~in~(w)

![mlf118](./_resources/mlf118.jpg)

我们已经推导完了E~in~(w)，接下来的事情就是想办法找到 w 使得E~in~(w)是最小的。幸运的是，LR 的这个函数是 convex 的。求解最小值就是找到谷底梯度为0的地方。

![mlf119](./_resources/mlf119.jpg)

第一步就是求梯度 ▽E~in~(w)

![mlf120](./_resources/mlf120.jpg)

一步一步求解偏微分，微积分连锁率。这个是其中一个 component 的推导，然后对于整体来说，可以写成如下形式：用 x~n~ 代替 x~n,i~

![mlf121](./_resources/mlf121.jpg)

到这一步我们想要的就是让这个梯度为零

![mlf122](./_resources/mlf122.jpg)

可以把梯度看成是一个以 θ 为权重的 y~n~x~n~ 的加权平均

![mlf123](./_resources/mlf123.jpg)

梯度什么时候是 0？第一个可能是所有的 θ 都是零，也就是说 y~n~w^T^x~n~ 要接近正无限大；但是正常来说更多的是 weighted sum = 0，non-linear equation of w

这是一个困难的问题

想要上式等于零，一种情况是sigmoid 项恒为0，也就是所有的 ywx >> 0，这时要求数据时线性可分的（不能有噪音）。否则，需要迭代优化。回忆一下之前revised PLA求解超平面直观的优化方法：

![mlf124](./_resources/mlf124.jpg)

![mlf125](./_resources/mlf125.jpg)

**一个习题**

![mlf126](./_resources/mlf126.jpg)

最小，代表 w 在 当前的 xy 上是错的，犯错的得到的权重特别大，梯度某种角度也代表了犯错在哪里。

### Iterative Optimization

![mlf127](./_resources/mlf127.jpg)

梯度下降法是最经典、最常见的优化方法之一。要寻找目标函数曲线的波谷，采用贪心法：想象一个小人站在半山腰，他朝哪个方向跨一步，可以使他距离谷底更近（位置更低），就朝这个方向前进。这个方向可以通过微分得到。选择足够小的一段曲线，可以将这段看做直线段，那么有

![mlf128](./_resources/mlf128.jpg)

这样就把一个非线性的优化问题利用泰勒展开，变成了一个线性的问题，在η够小的时候。

![mlf129](./_resources/mlf129.jpg)

所以，我们真正要要求解的是 v 乘上梯度如何才能越小越好。也就是 v 与梯度是完全的相反方向。想象一下：如果一条直线的斜率 k>0，说明向右是上升的方向，应该向左走；反之，斜率 k<0，向右走。

gradient descent: a simple & popular optimization tool

### Choice of η

![mlf130](./_resources/mlf130.jpg)

η better be **monotonic of** || ▽E~in~(w~t~) ||

解决的方向问题，步幅η也很重要。步子太小的话，速度太慢；过大的话，容易发生抖动，可能到不了谷底。显然，距离谷底较远（位置较高）时，步幅大些比较好；接近谷底时，步幅小些比较好（以免跨过界）。距离谷底的远近可以通过梯度（斜率）的数值大小间接反映，接近谷底时，坡度会减小。因此，我们希望步幅与梯度数值大小正相关。原式子可以改写为：

![mlf131](./_resources/mlf131.jpg)

### Putting Everything Together

![mlf132](./_resources/mlf132.jpg)

similar time complexity to **pocket** per iteration

**一个习题**

![mlf133](./_resources/mlf133.jpg)

看前面的公式一个一个代入，最后后面是一样的，系数是 0.1 * θ(0) = 0.1 * 0.5 = 0.05，所以选第三个答案

## Lecture 11: Linear Models for Classification

### Linear Models Revisited

linear scoring functions: s = w^T^x

![mlf134](./_resources/mlf134.jpg)

can linear regression or logistic regression **help linear classification**?

### Error-Functions Revisited

![mlf135](./_resources/mlf135.jpg)

为了更方便地比较三个 model，对其 error function 做一定处理。接下来我们要做的事情就是看看这些 Error Function 跟 ys 的关系，在此之前我们先看看ys 的物理意义：y 代表正确与否 correctness，s 代表正确或错误的程度 score。

![mlf136](./_resources/mlf136.jpg)

**Visulaizing Error Functions**

通过曲线来比较三个error function （注意：为了让Logistic Error Function 完全压在 0/1 的 Error Function 上，一般 cross-entropy 变为以2为底的 scaled cross-entropy），这样很容易通过比较三个 error function 来得到分类的 0/1 error 的上界。

![mlf137](./_resources/mlf137.jpg)

### Theoretical Implication of Upper Bound

![mlf138](./_resources/mlf138.jpg)

**Regression for Classification**

![mlf139](./_resources/mlf139.jpg)

线性分类(PLA)、线性回归、逻辑回归的优缺点比较：

+ PLA
    + 优点：在数据线性可分时高效且准确。
    + 缺点：只有在数据线性可分时才可行，否则需要借助POCKET 算法（没有理论保证）。
+ 线性回归
    + 优点：最简单的优化（直接利用矩阵运算工具）
    + 缺点：y*s 的值较大时，与0/1 error 相差较大(loose bound)。
+ 逻辑回归
    + 优点：比较容易优化（梯度下降）
    + 缺点：y*s 是非常小的负数时，与0/1 error 相差较大。

实际中，逻辑回归用于分类的效果优于线性回归的方法和 POCKET 算法。线性回归得到的结果w 有时作为其他几种算法的初值。

**一个习题**

![mlf140](./_resources/mlf140.jpg)

不 scale 之前有一部分是在 err 1/0 曲线之下的

### Two Iterative Optimization Schemes

![mlf141](./_resources/mlf141.jpg)

每一轮迭代，logistic regression 的复杂度比 PLA 大很多(因为每次都要过一遍所有的点)，所以有没有一个办法，能降低复杂度呢？

### Stochastic Gradient Descent (SGD)

传统的随机梯度下降更新方法如下。每次更新都需要遍历所有data，当数据量太大或者一次无法获取全部数据时，这种方法并不可行。

![mlf142](./_resources/mlf142.jpg)

我们希望用更高效的方法解决这个问题，基本思路是：只通过一个随机选取的数据(xn,yn) 来获取“梯度”，以此对 w 进行更新。这种优化方法叫做随机梯度下降。

![mlf143](./_resources/mlf143.jpg)

利用期望值的性质，在减少计算量的同时，保持比较高的正确率

stochastic gradient = true gradient + zero-mean 'noise' directions

![mlf144](./_resources/mlf144.jpg)

这种方法在统计上的意义是：进行足够多的更新后，平均的随机梯度与平均的真实梯度近似相等。

![mlf145](./_resources/mlf145.jpg)

注意：在这种优化方法中，一般设定一个足够大的迭代次数，算法执行这么多的次数时我们就认为已经收敛（防止不收敛的情况），η经验上的取值在0.1附近会比较合适。

**一个习题**

![mlf146](./_resources/mlf146.jpg)

### Multiclass Classification

One Class at a Time

![mlf148](./_resources/mlf148.jpg)

这方法有一个问题，就是用简单的二值分类，在交叉和没有覆盖到的区域，会有冲突，所以最要用 Soft 的方式，也就是用概率来表示。

![mlf147](./_resources/mlf147.jpg)

与二值分类不同的是，我们如何将这些Model延伸来做多类别的分类。一种直观的解决方法是将其转化为多轮的二值分类问题：任意选择一个类作为+1，其他类都看做-1，在此条件下对原数据进行训练，得到w；经过多轮训练之后，得到多个 w，如下图得到四个分类器，每个都是一个概率的分类器。

可以看到下面的是一个概率，w~[k]~^T^ 表示第 k 个分类器，其实连 θ 都不用考虑(因为是单调的)，直接比较大小即可

### One-Versus-All (OVA) Decomposition

![mlf149](./_resources/mlf149.jpg)

对于某个x，在有些时候4个分类器中只会有1个分类器说x就是它的类别；不过对于中间区域的点，4个分类器似乎都会说不是它们的类别，那该如何分类呢？这个时候，就将其分到可能性最大的那个类（例如逻辑回归对于x 属于某个类会有一个概率估计）。如果目标类别是k 个类标签，我们需要k 轮训练，得到k 个w。这种方法叫做One-Versus-All (OVA)。

它的最大缺点是，目标类很多时，每轮训练面对的数据往往非常不平衡(unbalanced)，因为每次训练都是当前类别的概率与其他K-1个类别的概率比较，会严重影响训练准确性。multinomial (‘coupled’) logistic regression 考虑了这个问题，感兴趣的话自学下吧。

**一个习题**

![mlf150](./_resources/mlf150.jpg)

注意这个过程可以很容易并行

### One-versus-one(OVO) Decomposition

既然这样，One-Versus-All 会出现 Unbalanced 的情况，那么有一种方法叫做 One-Versus-One(OVO)尝试解决这个问题。

基本方法：每轮训练时，任取两个类别，一个作为+1，另一个作为-1，其他类别的数据不考虑，这样，同样用二值分类的方法进行训练；目标类有k个时，需要 `k*(k-1)/2` 轮训练，得到 `k*(k-1)/2` 个分类器。

**Multiclass Prediction: Combine Pairwise Classifiers**

![mlf151](./_resources/mlf151.jpg)

预测：对于某个x，用训练得到的 `k*(k-1)/2` 个分类器分别对其进行预测，哪个类别被预测的次数最多，就把它作为最终结果。即通过“循环赛”的方式来决定哪个“类”是冠军。

![mlf152](./_resources/mlf152.jpg)

显然，这种方法的优点是每轮训练面对更少、更平衡的数据，而且可以用任意二值分类方法进行训练；缺点是需要的轮数太多(k*(k-1)/2)，占用更多的存储空间，而且预测也更慢。

OVA 和 OVO 方法的思想都很简单，可以作为以后面对多值分类问题时的备选方案，并且可以为我们提供解决问题的思路。

**一个习题**

![mlf153](./_resources/mlf153.jpg)

10 个类别，需要 `10*(10-1)/2 = 45` 个分类器，然后因为每个分类器只需要 2N/10 份的资料，所以一次计算的消耗是 N/5 的三次方，相乘之后就是第二个答案

## Lecture 12: Nonlinear Transformation

![mlf154](./_resources/mlf154.jpg)

二元分类视觉上像切一条线，数学上来说就是用输入 x 乘上某个向量 w 然后得到一个分数 s，这种模型很有好处，复杂度可控(d~vc~限制)，但是有限制，可能有些数据，没办法用线来切开。

how to **break the limit** of linear hypothesis?

### Circular Separable

![mlf155](./_resources/mlf155.jpg)

re-derive **Circular**-PLA, **Circular**-Regression

x~1~ 与 x~2~ 就是某个输入的横纵坐标(这里只考虑二维情况)

对于上面的例子，我们可以假设分类器是一个圆心在原点的正圆，圆内的点被分为+1，圆外的被分为-1，于是有：

![mlf156](./_resources/mlf156.jpg)

在上面的式子中，将 (0.6, -1, -1) 看做向量 w，将(1, x1^2, x2^2) 看做向量z，这个形式和传统的线性假设很像。可以这样理解，原来的 x-空间的点都映射到了 z-空间，这样，在 x-空间中线性不可分的数据，在 z-空间中变得线性可分；然后，我们在新的 z-空间中进行线性假设。

### Linear Hypothesis in Z-Space

![mlf157](./_resources/mlf157.jpg)

![mlf158](./_resources/mlf158.jpg)

在数学上，通过参数 w 的取值不同，上面的假设可以得到正圆、椭圆、双曲线、常数分类器，它们的中心都必须在原点。如果想要得到跟一般的二次曲线，如圆心不在原点的圆、斜的椭圆、抛物线等，则需要更一般的二次假设。

![mlf159](./_resources/mlf159.jpg)

具体参数 w 的产生，就是把空间转换函数的不同变量的不同次数项一个一个对应写下来。可以参考上图的例子。

对于找个通用的模型来说，直线可以看成是一个退化的特例

**一个习题**

![mlf160](./_resources/mlf160.jpg)

### The Nonlinear Transform Steps

Good Quadratic Hypothesis

![mlf161](./_resources/mlf161.jpg)

具体步骤如下：

![mlf162](./_resources/mlf162.jpg)

![mlf163](./_resources/mlf163.jpg)

也就是说，在操作上实际上不是往左边的箭头，而是往右边的箭头。往右边的箭头告诉我x-空间的每一个点都可以映射到z-空间，然后我等z-空间的线性分类告诉我分类结果。

如上的流程里面有两个比较关键可以选择的事情：如何做feature transform；选择怎样的linear model。这里的非线性转换其实也是特征转换(feature transform)，在特征工程里很常见。Feature transform 看起来很强大，就像打开了潘多拉的盒子，我们突然一下子可以做更多更多的事情了。不过听起来这么强大，到底有没有什么代价呢？且听下回分解。

not new, not just polynomial:

raw(pixels) (**domain knowledge**)-> **concrete(intensity, symmetry)**

**一个习题**

![mlf164](./_resources/mlf164.jpg)

### Computation/Storage Price

所谓”有得必有失“，将特征转换到高次空间，我们需要付出学习代价（更高的模型复杂度）。x-空间的数据转换到z-空间之后，新的假设中的参数数量也比传统线性假设多了许多：

![mlf165](./_resources/mlf165.jpg)

Q large -> **difficult to compute/store**

### Model Complexity Price

![mlf166](./_resources/mlf166.jpg)

Q large -> **large d~vc~**

那么如何选择呢？

![mlf167](./_resources/mlf167.jpg)

在两个关键问题上没有办法兼得

根据之前分析过的，VC dimension 约等于自由变量(参数)的数量，所以新假设的 d~vc~ 急速变大，也就是模型复杂大大大增加。回顾机器学习前几讲的内容，我们可以有效学习的条件是

1. E~in~(g) 约等于 E~out~(g)
2. E~in~(g) 足够小。

当模型很简单时，d~vc~ 很小，我们更容易满足（1）而不容易满足（2）；反之，模型很复杂时，d~vc~ 很大），更容易满足（2）而不容易满足（1）。看来选择合适复杂度的 model 非常 trick。

careful about **your brain's model complexity**

观察是不可靠的，依靠的是人的学习，已经受主观影响了，所以

![mlf168](./_resources/mlf168.jpg)

**一个习题**

![mlf169](./_resources/mlf169.jpg)

(d+2)x(d+1)/2 - 1

注意这里把一个实数空间映射到了一个50次的多项式，因此复杂度增加到了一千多维，这就会带来很高的计算代价

### polynomial Transform Revisited

前面我们分析的非线性转换都是多项式转换(polynomial transform)。我们将二次假设记为 H~2~，k次假设记为 H~k~。显然，高次假设的模型复杂度更高。如下图所示，低次假设的模型是包含在高次假设的模型里面的。当Hypothesis之间有这样的互相包含的关系的时候，我们将它叫做hypothesis set的一个结构。

![mlf170](./_resources/mlf170.jpg)

也就是说，高次假设对数据拟合得更充分，E~in~ 更小；然而，由于付出的模型复杂度代价逐渐增加，E~out~ 并不是一直随着 E~in~ 减小。

所以并不是高维度就好，而是应该找到一个折中。

![mlf171](./_resources/mlf171.jpg)

实际工作中，通常采用的方法是：先通过最简单的模型（线性模型）去学习数据，如果 E~in~ 很小了，那么我们就认为得到了很有效的模型；否则，转而进行更高次的假设，一旦获得满意的 E~in~ 就停止学习（不再进行更高次的学习）。

![mlf172](./_resources/mlf172.jpg)

总结为一句话：**linear/simpler model first**! simple, efficient, **safe**, and **workable**!

**一个习题**

![mlf173](./_resources/mlf173.jpg)

## Lecture 13: Hazard of Overfitting

overfitting happens with **excessive power**, **stochastic/deterministic noise**, and **limited data**

Bad Generalization

![mlf174](./_resources/mlf174.jpg)

这是什么意思呢，假设我们在一个二次空间里有五个点，如果我们想要找到的拟合函数是二次多项的话，可以看做是真实的值加上一些小小的噪声(也就是有一些 E~in~ 但并不大)。当然我们也可以用上面的方法把他们转到四次多项式上，那么五个点，四次多项式，有唯一解并且保证了 E~in~(g) = 0，可是与此同时，我们可以看到这条四次多项式和target函数差距很大，E~out~(g) 会非常大。

bad generalization: **low E~in~, high E~out~**

![mlf175](./_resources/mlf175.jpg)

**overfitting**: low**er** E~in~, high**er** E~out~

简单的说就是这样一种学习现象：VC dimension 太大的时候，E~in~ 很小，E~out~ 却很大。而另外一方面，E~in~ 和 E~out~ 都很大的情况叫做 Under-fitting。这是机器学习中两种常见的问题。这里的fitting指的就是 E~in~ 。上图中，竖直的虚线左侧是”underfitting”, 左侧是”overfitting”。

发生overfitting 的主要原因是：使用过于复杂的模型(d~vc~ 很大)；数据噪音；有限的训练数据。

用开车来比喻的话

![mlf176](./_resources/mlf176.jpg)

**一个习题**

![mlf177](./_resources/mlf177.jpg)

### Case Study

两组数据，一组由一个十次多项式生成，带噪声；另一组由一个五十次多项式生成，不带噪声；然后我们用二次和十次多项式去拟合，来看看结果如何

![mlf178](./_resources/mlf178.jpg)

overfitting from g~2~ to g~10~? **both yes**

可以看到在 E~in~ 部分，g~2~ 要比 g~10~ 大，毕竟是十次多项式；可以要比 E~out~ 的时候，g~10~ 就变得太大了，发生了 overfitting

如上图所示，我们可以分别从噪声与 Data Size 的角度理解地简单些：

有噪音时，更复杂的模型会尽量去覆盖噪音点，即对数据过拟合！这样，即使训练误差E~in~ 很小(接近于零)，由于没有描绘真实的数据趋势，E~out~ 反而会更大。即噪音严重误导了我们的假设。

还有一种情况，如果数据是由我们不知道的某个非常非常复杂的模型产生的，实际上有限的数据很难去“代表”这个复杂模型曲线。我们采用不恰当的假设去尽量拟合这些数据，效果一样会很差，因为部分数据对于我们不恰当的复杂假设就像是“噪音”，误导我们进行过拟合。

如下面的例子，假设数据是由50次幂的曲线产生的（下图右边，without噪声），与其通过10次幂的假设曲线去拟合它们，还不如采用简单的2次幂曲线来描绘它的趋势。

![mlf179](./_resources/mlf179.jpg)

以退为进 philosophy: **concession** for **advantage**

### Learning Curves Revisited

![mlf180](./_resources/mlf180.jpg)

在样本数量比较小的时候，低次项多项式反而效果会更好。没有太多数据的话，不妨直接用简单的 hypothesis

在没有 noise 的情况下，情况依然是二次的比较好

![mlf181](./_resources/mlf181.jpg)

当你要学习的东西是很复杂的时候，其实这个复杂度本身就是 noise，因为无论二次还是十次都没办法完全拟合

**一个习题**

![mlf182](./_resources/mlf182.jpg)

### A Detailed Experiment

什么时候需要小心 overfit 会发生

我们在 target function 上加一个高斯噪声，然后来研究不同的噪声强度对于 overfitting 的影响

![mlf183](./_resources/mlf183.jpg)

某个次方的多项式叫做 Q~f~ 比如说十次多项式就是 Q~10~

![mlf184](./_resources/mlf184.jpg)

红色表示非常 overfit，蓝色表示没有多少 overfit，

![mlf185](./_resources/mlf185.jpg)

可见，数据规模一定时，随机噪音越大，或者确定性噪音越大（即目标函数越复杂），越容易发生overfitting。总之，容易导致overfitting 的因素是：数据过少；随机噪音过多；确定性噪音过多；假设过于复杂(excessive power)。

对于最后一点解释一下，右边这个图与左边的图有一些小小的不一样：靠下部分说明好像 Q~f~ 往小的方向走的时候也会有overfit的现象出现。大家知道我们 overfit 的衡量方式是 E~out~(g~10~) – E~out~(g~2~)，当 target function 是10次多项式以下的时候，那么学习器 g~10~ 就太强了。

overfitting 'easily' happens

![mlf186](./_resources/mlf186.jpg)

如果我们的假设空间不包含真正的目标函数f(X)（未知的），那么无论如何 H 无法描述f(X) 的全部特征。这时就会发生确定性噪音。它与随机噪音是不同的。例如，目标函数是50次的多项式，而hypothesis是10次多项式的话，一定找个target function有某些地方是没办法被任何一个hypothesis所描述的。我们可以类比的理解它：在计算机中随机数实际上是“伪随机数”，是通过某个复杂的伪随机数算法产生的，因为它对于一般的程序都是杂乱无章的，我们可以把伪随机数当做随机数来使用。确定性噪音的哲学思想与之类似。

philosophy: when teaching a kid, perhaps better not to use examples from a complicated target function

**一个习题**

![mlf187](./_resources/mlf187.jpg)

对应导致过拟合发生的几种条件，我们可以想办法来避免过拟合。

![mlf188](./_resources/mlf188.jpg)

all very **practical** techniques to combat overfitting

假设过于复杂(excessive d~vc~) => start from simple model

随机噪音 => 数据清洗(Data Cleaning/Pruning)：将错误的label 纠正或者删除错误的数据。possibly helps, but **effect varies**

数据规模太小 => 收集更多数据，或根据某种规律“伪造”更多数据（Data hinting）：例如，在数字识别的学习中，将已有的数字通过平移、旋转等，变换出更多的数据。

正规化(regularization) 也是限制模型复杂度的方法，在下一讲介绍。其他解决过拟合的方法在后面几讲介绍。

**一个习题**

![mlf189](./_resources/mlf189.jpg)

要保证对称性，跟 target 函数一致

## Lecture 14: Regularization

minimizes **augmented error**, where the added **regularizer** effectively **limits model complexity**

发生 Overfitting 的一个重要原因可能是假设过于复杂了，我们希望在假设上做出让步，用稍简单的模型来学习，避免 Overfitting。例如，原来的假设空间是10次曲线，很容易对数据过拟合；我们希望它变得简单些，比如 w 向量只保持三个分量（其他分量为零）。

![mlf190](./_resources/mlf190.jpg)

![mlf191](./_resources/mlf191.jpg)

step back = **constrain**

也就是 Hypothesis Set 需要从高阶 step back 到低阶，例如从从10次多项式 H~10~ 走回到2次多项式 H~2~，如下图左所示。实际上就是代表在原来的Learning问题上加上一些限制Constraint。

![mlf192](./_resources/mlf192.jpg)

如果现在将左图的限制放松一些，如下右图所示。

![mlf193](./_resources/mlf193.jpg)

boolean operation 的最优化是困难的(上图右边的 s.t. 部分，那个类似方括号的操作)

可是，右上图中的优化问题是 NP-Hard 的。如果对 w 进行更soft/smooth 的约束，可以使其更容易优化。我们将此时的假设空间记为H(C)，这是“正则化的Hypothesis Set”。如果我们能够顺利地解决下图的最佳化问题，找出一个好的 w~REG~ 的话，那么就是regularized hypothesis。

![mlf194](./_resources/mlf194.jpg)

把一个离散的替换成一个连续的，方便优化

**一个习题**

![mlf195](./_resources/mlf195.jpg)

前面可以知道向量 w~q~^2^ 的和要小于 H(C) 中的 C，答案三不符合这个条件

### Matrix Form of Regularized Regression Problem

![mlf196](./_resources/mlf196.jpg)

把回归问题写成矩阵的形式

### The Lagrange Multiplier

那如何求解这个优化问题呢？先来看看我们新加入的这个限制对优化问题造成了怎样的影响。原来没有限制的时候，只需要让目标函数沿着梯度的反方向一路滚下去知道梯度=0。那加入了限制之后，也就是说w需要在一个红色的球里滚动，如下图所示。可以想象，大部分的时候我们需要的解都是在球的边界附近，只要梯度与w不是平行的，目标函数就仍然可以向谷底滚一点点，可以得到一个更好的解。也就是说，最优的结果是梯度与 w~REG~是平行的。

![mlf197](./_resources/mlf197.jpg)

w~lin~: 做 linear regression 的解

我们现在要做的是在一定限制里求解，所以解必须在圆圈里。在边缘的带点只能在垂直于球的法向量的方向上滚。如果梯度的反方向和 w 不平行，那么在可以滚的方向上会有一个分量，就可以沿着允许的方向滚。

直到 ▽E~in~(w~REG~) 和 w~REG~ 平行，才算是找到了最优解

也就是满足最下面的公式(拉格朗日参数 λ)

### Augmented Error

![mlf198](./_resources/mlf198.jpg)

**ridge regression**

minimizing **unconstrained E~aug~** effectively minimizes some **C-constrained** E~in~

![mlf199](./_resources/mlf199.jpg)

我们要求解的话，就要找出 w~REG~，然后看看有没有一个相对应的 λ，让这两个向量是平行的。观察下面这个式子发现，梯度是原来 E~in~ 的微分，只要对 w~REG~ 做积分，那么就可以得到原来的目标函数的等价形式。

求梯度等于零，实际上就是找原函数的最小值在哪里

加上的这一项通常叫做regularizer。如果给定了 λ (λ>=0，因为它代表两个向量长度的比值而 λ = 0则就代表无限制的原问题)，那么就可以通过解这个优化问题得到 w~REG~。也就是说，我们不再需要去求解之前的那个 constrained C 的优化问题了，对于使用者来说，指定 C 与指定 λ 来说没有什么区别。

也就是原来的条件成为了目标函数的一部分了

### The Result

![mlf200](./_resources/mlf200.jpg)

一点点的 regularization 也会有很好的效果

总之，λ 越大，希望的 w 越短越好(因为在最小化问题中相当于在惩罚长的 w)，对应的常数 C 越小，模型越倾向于选择更小的 w 向量。这种正规化成为 weight-decay regularization，它对于线性模型以及进行了非线性转换的线性假设都是有效的。

### Legendre Polynomials

另外补充一下，虽然 regularization 可以跟任何的transform做搭配，课件中的实验为了结果更明显一些，其实在transform的时候加入了一点小技巧。naive 多项式的transform有一些小小的缺点：如果|x| <= 1，高次 x^Q^ 是很小的数字，要想它在hypothesis中发挥影响力则需要很大的 w，这就与 regularization 目的（将w压到很小）背道而驰。也就是说 regularization 会过度地惩罚了高次的 x^Q^ ，这里用的技巧就叫做 legendre polynomials，如下图所示。

![mlf201](./_resources/mlf201.jpg)

找一些互相垂直的基底，用原来的多项式做垂直化(系数会有一些改变，补偿呗过分惩罚的高次项分数)，效果会更好

**一个习题**

![mlf202](./_resources/mlf202.jpg)

+ λ = 0则就代表无限制的原问题
+ C 很大，表示条件很宽松，也包含了线性回归的解

### Regularization and VC Theory

![mlf203](./_resources/mlf203.jpg)

根据 VC Bound 理论，E~in~ 与 E~out~ 的差距是模型的复杂度。也就是说，假设越复杂（d~vc~ 越大），E~out~ 与 E~in~ 相差就越大，违背了我们学习的意愿。

### Another View of Augmented Error

![mlf204](./_resources/mlf204.jpg)

E~aug~ 跟 VC 其实有一些异同，E~aug~ 新加入的那项可以认为是某个单一 hypothesis 有多复杂；而 VC 则表示整个hypothesis set有多复杂。也许，E~aug~ 是一个比原来的 E~in~ 的更好的代理。

minimizing E~aug~:

+ (heuristically) operating with the better proxy;
+ (technically) enjoying flexibility of whole H

![mlf205](./_resources/mlf205.jpg)

对于某个复杂的假设空间 H，d~vc~ 可能很大；通过正规化，原假设空间变为正规化的假设空间 H(C)。与 H 相比，H(C) 是受正规化的“约束”的，因此实际上 H(C) 没有 H 那么大，也就是说 H(C) 的 VC维比 原 H 的VC维要小，也就是 Effective VC Dimension。因此，E~out~ 与 E~in~ 的差距变小。

不仅考虑了 Hypothesis set，也考虑了算法怎么做选择，就可以得到一个更优化的 VC Dimension

**一个习题**

![mlf206](./_resources/mlf206.jpg)

### General Regularizers Ω(w)

want: constrait in the **'direction' of target function**

刚刚讲到的regularizer都集中在weight decay上面，那如果想要换更一般的regularizer呢。指导我们更好地设计正规项的原则：最好能告诉target function在哪一个方向。

![mlf207](./_resources/mlf207.jpg)

+ target-dependent(symmetry)：如果知道target function的特性，也许可以放进去。例如如果想要的是比较接近偶次方函数，加上的regularizer就是让奇次方的w越小越好。
+ plausible(sparsity)：有说服力的，例如比较平滑或者简单的regularizer。因为regularization主要是为了解决overfitting
+ friendly(optimize)：方便优化求解。

当然，就算选择了一个不太好的regularizer，还有lamda = 0的保护，最差就是不用它而已。

regularizer 和 error measure 的方向很像，三个不同的面向

**机器学习是一门非常重实践的学科，要多写代码**

### L2 and L1 Regularizer

![mlf208](./_resources/mlf208.jpg)

那接下来来看一下L2与L1的regularizer。L2非常的平滑，也易于求解。那L1的特点呢？它也是convex的，不过不是处处可微。不过L1的解常常会是sparse的，也就是w中会有很多的0，因为它的解常常会发生在顶点处。

**L1 useful if needing sparse solution**

### The Optimal λ

![mlf209](./_resources/mlf209.jpg)

那 λ 应该如何选择？λ 当然不是越大越好！选择合适的 λ 也很重要，它收到随机噪音和确定性噪音的影响，噪音越大，需要的 λ 越大。那具体要如何选择呢？且听下回分解。

**一个习题**

![mlf210](./_resources/mlf210.jpg)

## Lecture 15: Validation

(crossly) reserve **validation data** to simulate testing procedure for **model selection**

机器学习的每个模型都有各式各样的参数。即使只是对于二元分类，学习算法上可以选择PLA，LR等；很多学习算法都是iterative的，需要决定迭代次数；可能需要决定每一次迭代走多大，例如梯度下降；或者有很多的transform，例如线性、二次等；同时 regularizer 又有很多的选择 L1/L2；再来 regularizer 到底要加多强的 λ。况且这些选择是组合起来的，那么我们怎么做出正确的选择？

![mlf211](./_resources/mlf211.jpg)

in addition to your **favorite** combination, may need to try other combinations to get a good **g**

![mlf212](./_resources/mlf212.jpg)

把模型选择问题一般化一下，就是如下的定义：有 M 个模型，每个模型有其对应的 Hypothesis set 以及学习算法A，希望选出某一个模型得到的g，它的 E~out~(g) 是最小的。但是 E~out~ 不知道，无法以其作为标准。

![mlf213](./_resources/mlf213.jpg)

根据 E~in~(g) 最小来选择模型也是行不通的。一方面容易造成 overfitting；另一方面，假设有两个模型PK：算法 A~1~ 在 H~1~ 上让 E~in~ 最小；算法 A~2~ 在 H~2~ 上让 E~in~ 最小。最后选出来的 g 的效果是在 H~1~∪H~2~ 上让 E~in~ 最小，也就说额外增加了model complexity，容易造成bad generalization。

**selecting by E~in~ is dangerous**

![mlf214](./_resources/mlf214.jpg)

通过测试数据来选择模型是自欺欺人的。如果能找到一些测试数据，来看看哪一个模型的表现更好就选择哪个。如果用这样的方式，可以得到Hoeffding的理论保证如下图。看起来很棒，可是问题是我们找不到测试数据，测试数据就像考卷，不可能说考试之前就发下来的。

**selecting by E~test~ is infeasible and cheating**

### Comparison between E~in~ and E~test~

![mlf215](./_resources/mlf215.jpg)

那，将这两者结合一下：把训练数据留一部分下来作为测试数据，用其他的训练数据来训练模型，然后用测试数据来测试模型的表现好坏。这是legal cheating。

**一个习题**

![mlf216](./_resources/mlf216.jpg)

根据上面的分析，原来的训练数据分割出一部分作为测试数据，也被叫做validation set。同样，也会有 Hoeffding 不等式的保证。

![mlf217](./_resources/mlf217.jpg)

为了和原来的 E~out~ 作比较，我们知道更多的训练数据一般来说会有更好的 E~out~。所以很大程度上来说也就有如下的保证。

![mlf218](./_resources/mlf218.jpg)

先把数据切成两个部分，训练集和测试集，用训练集训练出最好的模型，再把所有的数据放到最好的模型上训练，这样就可以找到用更多数据训练出来的最佳模型(不是 g^-^ 了)

![mlf219](./_resources/mlf219.jpg)

我们来看看 validation 有没有用，横轴是 validatoin set 的大小，纵轴是 Expected E~out~(越低越好)，如果用 in-sample 会得到的那条横线；如果作弊用 E~test~ 会得到最下面的虚线；如果只用训练集，那么会得到 g^-^；如果选出最佳之后再用全部的数据集，会得到 g。

我们可以看到用 g 的时候，实际上是很有用的。但是 g^-^ 有时候比用 E~in~ 还糟糕，为什么呢？因为当测试集太大，训练集就会太小，效果就不好

### The Dilemma about K

![mlf220](./_resources/mlf220.jpg)

那 Validation Set 的大小 K 应该如何选择？选择的 K 应该尽可能地让这三个 Error 约等式成立。通常情况下，K 取 N/5。

![mlf221](./_resources/mlf221.jpg)

注意到加入Validation的方式花的时间比原来25N^2要来的小，因为训练模型的数据更少了。

### Leave-One-Out Cross Validation

考虑一个极端的情形，取非常小的K = 1。小的K可以让 E~out~(g) 与 E~out~(g-)非常接近，不过之前那个约等式右边希望 E~out~(g-) 与 E~val~(g-)接近就很难满足了。那我们来看看能不能克服这个问题。

![mlf222](./_resources/mlf222.jpg)

e~n~ 表示取第 n 笔数据作为 validation data，所得到的 E~val~(g-)。e~n~ 到底能不能告诉我们 E~out~(g)有多好呢？一个 e~n~ 当然不行，那把每笔数据都作为一次 validation data 然后平均起来，选择平均 Error 最小的作为最后的g，这样的方式叫做 cross validation。

E~loocv~(H, A) ≈ E~out~(g)

![mlf223](./_resources/mlf223.jpg)

那 Leave-one-out Cross Validation 有何理论保证呢？或者它能不能告诉我们最在乎的事情 E~out~(g)有多好。假设有一个算法和1000笔数据拿来做 Leave-one-out Cross Validation，然后对各式各样的1000笔数据来做取一个平均。证明跟 E~out~(N-1)的平均值是可以连接的。因为 E~out~(g-) 与 E~out~(g) 几乎是一样的，前者是1000笔数据做出来的，后者是999笔数据做出来的。

e~n~前面的符号表示期望值

所以，我们得到了一个几乎完全没有偏见的针对 E~out~(g)的衡量方式。也就是说，Leave-one-out Cross Validation在选择模型上会比 E~in~ 来的更有效。

**一个习题**

![mlf224](./_resources/mlf224.jpg)

### Disadvantages of Leave-One-Out Estimate

![mlf225](./_resources/mlf225.jpg)

很明显，一方面，Leave-One-Out Cross Validation大大增加了计算的复杂度，实际应用上上可能不太行；另一方面，对于二元分类来说，分类结果在0与1之间跳动，Leave-One-Out求一个平均值。对这个平均值来说，这些0与1的跳动是很大的，希望用平均的方式把这些很大的跳动消掉，其实还是不太容易。

这两个问题使得这个方法在实际上并不是特别常用

### V-fold Cross Validation

how to **decrease computation need** for cross validation?

![mlf226](./_resources/mlf226.jpg)

practical rule of thumb: V = 10

为了降低计算复杂度，将训练资料分为V份，取其中V-1做训练，另外1份做validation。这种方式通常叫做V-fold Cross Validation，实际上V通常取10。

### Final Words on Validation

**Selecting Validation Tool**

+ **V-Fold** generally preferred over single validation if computation allows
+ **5-Fold or 10-Fold** generally works well: not necessary to trade V-Fold with Leave-One-Out

**Nature of Validation**

+ all training models: select among hypotheses
+ all validation schemes: select among finalists
+ all testing methods: just evaluate

validation still more optimistic than testing

do not fool yourself and others, **report test result**, not **best validation result**

Traning 就像初赛，各个模型都从 Hypothesis Set 中选出最合适的h；Validation就像复赛，从多种模型的scheme中选出一个最优的。这两步都是在进行模型选择，之后的testing methods都只是在对模型进行estimate了。也因为Validation还是在做选择，只要做选择就会有数据的污染等等，所以Validation仍然比testing要乐观。对于模型来说，testing的表现才是真正要看重的，而不是最好的validation的表现。

**一个习题**

![mlf227](./_resources/mlf227.jpg)

## Lecture 16: Three Learning Principles

### Occam's Razor

> An explanation of the data should be made as simple as possible, but no simpler.

> Entities must not be muliplied beyond necessity. -- William of Occam

**Occam's razor** for trimming down unnecessary explanation

The simplest model that fits the data is aslo the most plausible

它的哲学意义蛮有名的，比喻剃掉过分的解释。在机器学习里面的意思就是：对训练数据最简单的解释就是最好的。那么问题来了，什么叫做简单的模型和解释；以及为什么确定简单的就是最好的？

曾今定义过 simple hypothesis：看起来很简单，例如一个大大的圆而不是弯弯曲曲的曲线；只需要少数的参数，圆心和半径就能确定这个 hypothesis长什么样子。也曾今定义过 simple model(也就是Hypothesis Set)：有效的hypothesis数量不是很多，成长函数长的很慢。

### Simple Model

![mlf228](./_resources/mlf228.jpg)

simple: **small hypothesis/model complexity

**Simple is Better**

![mlf229](./_resources/mlf229.jpg)

那为什么简单是好的呢？直觉的解释如下：想象有一个简单的model，同时给你一堆随机产生的没什么规律的训练数据。这时候你的 model 只有很小的机会能够找到 E~in~ 是0，杂乱的训练数据导致大部分的时候都没办法分开。那反过来说，如果今天有一组训练数据用你的 simple model 可以分开，这表明了你的数据是有显著性的，是有规律的数据。而用复杂的模型，则是达不到这样的效果的。

direct action: **linear first**

always ask whether **data over-modeled**

所以根据这个锦囊妙计出发，先试线性的模型；选择模型之前永远要想一想是否尽可能地用了最简单的模型。

**一个习题**

![mlf230](./_resources/mlf230.jpg)

### Sampling Bias

抽样有偏差的时候，学习算法产生的结果也会有偏差，这样的情形叫做Sampling bias。VC理论里的一个假设就是：训练数据与测试数据来自于同一个分布。不然的话，学习可能没办法做的很好。那怎么办呢？

实用的建议：了解你的测试环境，让你的训练环境跟测试环境尽可能地接近。举例来说，如果测试环境是last user records，也就是时间轴上靠后的使用者资料，那么训练的时候应该要想办法对时间轴上靠后的数据的权重加强一下。或者，做validation的时候也选择late user records靠后的用户资料。

If the data is sampled in a biased way, learning will produce a similarly biased outcome.

techincal explanation: data from P~1~(x, y) but test under P~2~ ≠ P~1~: **VC fails**

philosophical explanation: study Math but test English: no strong test guarantee

'minor' VC assumption: data and testing **both iid from P**

**一个习题**

![mlf231](./_resources/mlf231.jpg)

### Visual Data Snooping

第三个锦囊妙计就是不要偷看数据。例如之前我们通过观察数据发现圆圈可能是一个好的hypothesis，这其实忽略了人脑的VC dimension。当然实际情况下，偷看资料可能经常发生，不只有使用眼睛的方式。

学习中使用数据的任何过程，都是间接地让你偷看到数据。偷看到数据的表现以后，在下决策去做任何的一件事都要想到，这个数据已经因为你的决策选择过程而多出了很多的model complexity而污染。

所以，在实际操作中，要谨慎地处理Data Snooping这件事情。要做到完全不偷看数据很难，一个折中的方式是做validation。另外，在实际操作中如果要做什么决定的时候尽量避免用数据来做决定，要先把domain knowledge变成feature放进去而不是看完数据再放专业知识进去。然后，要时刻存着怀疑之心，时刻要有一个感觉经过多少过程得到这些结果，结果到底可能被污染的多严重。

If a data set has affected any step in the learning process, its ability to assess the outcome has been compromised.

### Dealing with Data Snooping

+ truth - **very hard to avoid**, unless being extremely honest
+ extremely honest: **lock your test data in same**
+ less honest: **reserve validation and use cautiously**

+ be blind: avoid **making modeling decision by data**
+ be suspicious: interpret research results (including your onw) by proper **feeling of contamination**

careful balance between **data driven modeling(snooping)** and **validation (no-snooping)**

**一个习题**

![mlf232](./_resources/mlf232.jpg)

### Power of Three

Three Related Fields

![mlf233](./_resources/mlf233.jpg)

Three Theoretical Bounds

![mlf234](./_resources/mlf234.jpg)

Three Linear Models

![mlf235](./_resources/mlf235.jpg)

Three Key Tools

![mlf236](./_resources/mlf236.jpg)

Three Learning Principles

![mlf237](./_resources/mlf237.jpg)

三个相关的领域：

+ Data Mining：从大量的数据里找出一些有兴趣的特性。它跟ML是高度相关的。
+ Artificial Intelligence：想让机器做一些有智慧的事情。ML是实现AI的一种方法。
+ Statistics：从数据里做一些推论的动作。是ML的工具。

三个理论保证：

+ Hoeffding不等式：针对单个hypothesis的抽样
+ Multi-Bin Hoeffding：针对M个hypothesis
+ VC Bound：针对整个hypothesis set。

三个模型：

+ PLA/Pocket：二元分类
+ Linear regression：线性回归，公式解
+ Logistic regression：分类概率

三个重要工具：

+ Feature Transform：通过映射到高维空间，将E_in变小。
+ Regularization：反其道而行，想让VC Dimension变小一点，但是可能E_in会变大一些。
+ Validation：留下干净的数据来做模型的选择。

三个锦囊妙计：

+ Occam’s Razer：simple is good。
+ Sampling Bias：training matches testing。
+ Data Snooping：honesty is best policy。

Three Future Directions

![mlf238](./_resources/mlf238.jpg)

未来的学习方向：将在后续的机器学习技法课程中讲解。一个是更多不一样的转换方式，不止有多项式的转换；一个是更多的正则化的方式；再来就是不是那么多的Label，譬如说要做无监督的学习应该要如何来做等等。

