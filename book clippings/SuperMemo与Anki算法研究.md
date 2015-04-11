SuperMemo 是一个著名的记忆辅助工具，但是其算法太过学院派。SM的早期的算法是开源的，一点也不神秘<http://www.supermemo.com
/english/algsm11.htm> 。（这里指的主要是2003年之前的算法，后面近10年的算法更新已经不公开思路了）

  

其中的体系大概是这样

  

**Historic note: earlier releases of the algorithm**

  

Although the presented algorithm may seem complex, you should find it easier
and more natural once you understand the evolution of individual concepts such
as E-Factor, matrix of optimum intervals, optimum factors, and forgetting
curves.

  * **1985** \- Paper-and-pencil version of SuperMemo is formulated ([Algorithm SM-0](http://www.supermemo.com/english/ol/beginning.htm#Algorithm)). Repetitions of whole pages of material proceed along a fixed table of intervals. See also: [Using SuperMemo without a computer](http://www.supermemo.com/articles/paper.htm)
  * **1987** - [First computer implementation](http://www.supermemo.com/articles/soft/sm2.htm) makes it possible to divide material into individual items. Items are classified into difficulty categories by means of [E-Factor](http://www.supermemo.com/english/ol/sm2.htm#E-Factor). Each difficulty category has its own optimum spacing of repetitions ([Algorithm SM-2](http://www.supermemo.com/english/ol/sm2.htm))
  * **1989** \- SuperMemo 4 was able to modify the function of optimum intervals depending on the student's performance ([Algorithm SM-4](http://www.supermemo.com/english/ol/sm4.htm))
  * **1989** \- SuperMemo 5 replaced the matrix of optimum intervals with the matrix of optimal factors (an optimum factor is the ratio between successive intervals). This approach accelerated the modification of the function of optimum intervals ([Algorithm SM-5](http://www.supermemo.com/english/ol/sm5.htm))
  * **1991** - [SuperMemo 6](http://www.supermemo.com/articles/soft/sm6.htm) derived optimal factors from forgetting curves plotted for each entry of the matrix of optimum factors. This could dramatically speed up the convergence of the function of optimum intervals to its ultimate value ([Algorithm SM-6](http://www.supermemo.com/english/ol/sm6.htm))
  * **1995** - [SuperMemo 8 Pre-Release 1](http://www.supermemo.com/articles/soft/sm8.htm) capitalized on data collected by users of[SuperMemo 6](http://www.supermemo.com/articles/soft/sm6.htm) and [SuperMemo 7](http://www.supermemo.com/articles/soft/sm7.htm) and added a number of improvements that strengthened the theoretical validity of the function of optimum intervals and made it possibility to accelerate its modification, esp. in early stages of learning ([Algorithm SM-8](http://www.supermemo.com/english/algsm8.htm#Algorithm%20SM-8)). New concepts include:
    * replacing E-factors with absolute difficulty factors: [A-Factors](http://www.supermemo.com/english/algsm8.htm#A-Factor)
    * fast approximation of A-Factors from the [FirstGrade-vs.-A-Factor correlation graph](http://www.supermemo.com/english/algsm8.htm#G-AF%20graph) and [ForgettingIndex-Grade graph](http://www.supermemo.com/english/algsm8.htm#G-FI%20graph)
    * real-time adjustment of the matrix of optimal factors based on introducing D-Factors and power approximation of the decline of optimum factors

SM12+: 神经网络

  

2005年之前的算法甚至不考虑推迟复习的情况，需要用户每天学习，这样即使算法非常精准，但是用户只要有几天推迟整个算法就乱掉了。现在网络上说基于SM算法的基本
上都是说的2005年之前的算法，因为之前的算法比较公开，但是算法是不实用的，一款软件没有理由需要每天使用。这一点也是我非常想要改进的地方，其实SuperMe
mo已经有了解决方案，但是无奈不开源了，只能自己捣鼓

  

我认为良好的算法应该是：

1.基于时间间隔和记忆质量反馈；

2.记忆辅助工具需要做的是对碎片时间优化，用户可以随时学习

3.允许用户推迟记忆时间，而不是用自己的 day to day 算法安排进度

  

2005年之后SM看到了推迟补偿的重要性，加入了一些对推迟的考虑。但是SM的核心还是计算时间，而没有考虑用户的时间是碎片化的，多复习几遍会死吗，为什么非要计
算的那么“准”。与其用神经网络，机器学习计算精准的补偿推迟单词的复习时间，不如做个可以让人可以跨平台，简单可以忍受的客户端。聪明反被聪明误；

  

反馈选项太多，SM的算法需要接受5个级别的复习质量： “In order to calculate the new value of an
E-Factor, the student has to assess the quality of his response to the
question asked during the repetition of an item (my SuperMemo programs use the
0-5 grade scale - the range determined by the ergonomics of using the numeric
key-pad).”

  

复习一个单词的时候你要打分：好，很好，一般，不好，很不好；我一直困扰的是好和很好有什么太大的区别？一个人真能作出5个等级的自省吗？
反正我一般不能区分“好”和“很好”，所以算法的输入是不可靠的。

  

一款软件不应改让人为难，去打1-5的分数，而应改要么0要么1，首先让人好做判断，而不是困扰。所以算法应该有能力把用户的0和1映射成1-5个回忆质量等级，而不
是把问题抛给用户。

  

* * *

  

Mnemosyne 函数与SuperMemo非常相似，换句话说，它会问你一个问题，你按照自己的掌握程度用0-5来标注，然后软件就会自动帮你规划。也就是说，你
不需要决定什么时候复习，程序会根据你之前的表现来决定。当你给越来越多的卡片评分后，程序会更加了解你需要多长的时间间隔来复习。一方面来说，你需要相信这个算法；
另一方面来说，如果你不相信这个算法，那么为啥要用这个软件？

  

当你在anki中记忆错误一个卡片时，它会在10到20分钟后给你出示这个卡片（默认状态下，这换个可以通过选项改变）。相反，Mnemosyne和supermem
o把所有这些记忆错误的卡片放到最后，使你先看完今天该看的卡片，然后才进行复述工作。毫无疑问，anki的方法的意图是很好的，而且对于一些人来说也是很高效的。但
我更适应把所有错误的卡片放到最后的方式来复述。对于anki来说，我喜欢的复述方式就很难实现，使用anki时，我不得不把电脑的时间调回几百分钟来得到熟悉的卡片
，这样的复述方式确实是有争议的。因此，对于anki这个软件，你在复述错误一个卡片时，可以记个高分让它不再重复，或是由软件决定它的出现。

  

anki的算法设定复述的时间表是按小时来的，而不是按天来。在mnemosyne和supermemo中，他们是按天来的，这样做的原因是睡眠。复述是按睡眠的周期
来的。这个是有很多研究结果支持的。如果你作个这样的体验（译者：我这里理解的不是很好）   ，在24小时中任何时间作记忆，做完后，记忆不会随着时间而继续保留。

  

惟一一个我对anki欣赏的地方（这也是让我震惊的事情，anki是记忆复述软件中唯一具有这个功能的）是它包括了一个“编辑－撤销”的功能。这样如果你对一个卡片的
评分错了，你能重新修正。虽然这个功能在所有的软件中是一个很普通的功能，但是mnemosyne和super memo却没有。

  

* * *

Anki的算法原来是基于SuperMemo
SM5算法的。但是Anki默认的在用户回答回答卡片之前就预测下次出现间隔的做法暴露出了SM5算法的某些基本的问题。SM2与其之后的算法的主要区别在于：

  * SM2算法使用你在某张卡片上的表现来确定这张卡片下次出现的时间
  * SM3及之后的算法使用你在某张卡片上的表现来确定这张卡片以及与其相似的卡片下次出现的时间

理论上来说，最新的算法会得到更加准确的时间间隔，因为确定间隔的因素从一张卡片变成了一组卡片。如果你一直坚持学习并且所有的卡片的难度都类似，这个算法就非常好。
然而，一旦出现不一致的地方（比方说每天学习时间不一样，卡片的难度不一样），那么SM3+就很可能对下次出现的时间做出不正确的预估——要么总是出现，要么总不出现
。

  

在评估了各种选择之后，Anki的作者决定使用由SM2算法派生出来的近似优化间隔。SM2的方法是可预测并且对于用户来说更加直观，但是SM3+则隐藏了这些细节（
而算法是会出错的）

  

Anki的算法基于SM2，但是在下列方面有不同：

  * SM2定义的初始间隔是1天，然后就是6天。但是在Anki中，这个时间是可以自定义的。Anki知道在你能记住一张新卡片之前可能需要多次的查看，所以那些一开始的记忆错误并不意味着你会在接下来的几天里总是要看到那些卡片。也就是说，学习阶段的表现并不会影响到记忆阶段。
  * 对于每张卡片，Anki给出的评级是4种，而不是SM2中的六种，并且只有一个选项是fail的情况。之所以这样做，是因为记忆错误的总体来说一定是占少数的，那么更重要的是区分
  * 回答卡片的时间超出预计也会被考虑在这张卡片下次出现的间隔计算中，也就是说，那些你记得但是回答晚的，会有一定的出现频率的提高。
  * 与SM2相似，Anki的failure 按键会把卡片的出现间隔重设为默认，但是用户可以让其回到过往的某一状态而不是完全回到起点。同时你也可以在第二天再看那些没有记住的卡片，而不是当天。
  * 如果选择了已经记住这个状态，不仅仅会增加ease factor，还会增加下一次出现的时间间隔，这样的策略会比SM2更加激进一些
  * 在学习某张卡片的阶段时连续的failure不会让卡片的ease factor进一步降低。标准的SM算法一个备遭诟病的地方就是连续错误会让某张卡片掉入“短间隔地狱”，反复出现。在Anki中，这种问题得到了有效解决

（这里提出了学习阶段和记忆阶段，这个很有启发性，如果在算法中检测出来，也是很重要的）

  

SM2算法表现很好，这是大家公认的，但是无论从理论还是实践上来说，SM5优于SM2是毋庸置疑的。SM2算法中卡片显示的间隔时间仅由其难度决定，这只是heur
istic formula的一个近似。

  

SM2算法简单粗暴，直接利用与一个叫E-factor的参数相乘来得到显示的间隔时间。相比之下，SM5算法会手机用户的数据并且据此调整优化间隔时间，也就是说它
会自动适应不同的人，而SM6算法在这方面走得更远。

  

所有的SuperMemo算法都会根据不同的难度进行分类，SM2中每个分类有固定的时间间隔，而在SM5中每一类虽然也有这样的间隔，但是可以根据用户的表现进行对
应的调整。

  

保持一致性因此在SM5中会比SM2中更重要，因为不一致不仅仅会影响一个条目，也会产生连锁反应，导致出现错误的调整。但是随着使用次数的增加，SM5及之后的算法
会有更加准确的间隔时间预测

  

卡片的难度不一样的确会影响到实际算法的应用，直到在SM8算法中引入了A-Factors才得以解决。

  

由于现在对于记忆的了解依然不完整，那么自适应模型总是要优于固定模型的。SM2 < SM5 < SM8

  

E-factor, A-factor, RF matrix, matrix smoothing, stability, collection.

* * *

  

SuperMemo 2算法

  

1987年12月使用Turbo Pascal 3.0 / IBM PC编写完成，主要是在以下两个方面增强SuperMemo算法：

  1. 把优化的过程应用到可能的最小单位（之前的算法的单位是item组成的page）
  2. 根据item的不同的难度等级来进行区分

观察到复习的时间间隔接近于某个常数，所以决定使用以下公式

  

I(1):=1

I(2):=6

for n>2 I(n):=I(n-1)*EF

  

其中

  

I(n) - inter-repetition interval after the n-th repetition (in days)

EF - easiness factor, 表示记忆某个item的难度，后面称为E-Factor

  

E-Factor的范围是1.1~2.5，其中1.1是最难，2.5是最简单。当一个新的item进入SuperMemo数据库时，它的E-
Factor为2.5。在不断重复的过程中，这个值将会不断减少。因此一个单词记忆的时候用户的记忆度越低，那么它的E-Factor就会下降越多。（注意！Supe
rMemo的机制，实际上是认为，一个item入库的时候用户已经是记住的，这与背单词不一样，千万注意！另一种做法是一开始默认用户都不会，也就是初始值为1.1，
然后在不断学习的过程中递增这个数值）

  

后来发现E-Factor不应该低于1.3。如果低于这个数值，那么就以恼人的频率出现，看起来是公式有内在的缺陷，所以保证E-
Factor不低于1.3就成了下一步改进的方向。

  

为了得到新的E-Factor，就需要引入用户对于问题回答的评价，也就是0-5的评分机制，新的公式为：

  

EF’:=f(EF,q)

  

其中

  

EF’ - E-Factor的新值

EF - E-Factor的旧值

q - 评价的分数

f - 用来计算EF’的函数

  

f函数原来比较复杂，经过多方考虑和改进之后，最后的形式是这样的

  

EF’:=EF-0.8+0.28*q-0.02*q*q （画一下函数图像）

  

而原来的公式是：

  

EF’:=EF+(0.1-(5-q)*(0.08+(5-q)*0.02))

  

注意当q=4时，E-Factor将不会改变

  

现在的问题是选项太多，六种！太夸张，能接受的至多是三种，然后根据反应时间自动细分成六种，可是反应时间，在跑步的时候，是非常难以界定的，这就有了问题，需要斟酌

  

**Algorithm SM-2 used in the computer-based variant of the SuperMemo method and involving the calculation of easiness factors for particular items:**

  1. Split the knowledge into smallest possible items.
  2. With all items associate an E-Factor equal to 2.5.
  3. Repeat items using the following intervals:  
**I(1):=1**  
**I(2):=6**  
**for n>2: I(n):=I(n-1)*EF**  
where:  
I(n) - inter-repetition interval after the n-th repetition (in days),  
EF - E-Factor of a given item  
If interval is a fraction, round it up to the nearest integer.

  4. After each repetition assess the quality of repetition response in 0-5 grade scale:  
5 - perfect response  
4 - correct response after a hesitation  
3 - correct response recalled with serious difficulty  
2 - incorrect response; where the correct one seemed easy to recall  
1 - incorrect response; the correct one remembered  
0 - complete blackout.

  5. After each repetition modify the E-Factor of the recently repeated item according to the formula:  
**EF':=EF+(0.1-(5-q)*(0.08+(5-q)*0.02))**  
where:  
EF' - new value of the E-Factor,  
EF - old value of the E-Factor,  
q - quality of the response in the 0-5 grade scale.  
If EF is less than 1.3 then let EF be 1.3.

  6. If the quality response was lower than 3 then start repetitions for the item from the beginning without changing the E-Factor (i.e. use intervals I(1), I(2) etc. as if the item was memorized anew).
  7. After each repetition session of a given day repeat again all items that scored below four in the quality assessment. Continue the repetitions until all of these items score at least four.

对于寻找E-Factor的优化过程被证明是有效的，在程序中你总是能找到一个选项来显示E-Factor的分布（后面称为E-
Distribution）。E-Distribution的形状需要大概几个月的时间来建立。

  

* * *

SuperMemo 4算法

  

SM2算法最被人诟病的地方就是那个充满着magic
number的优化公式（也就是求出EF’的那个公式）。虽然在实践中已经被证明很有效，但是在理论上没有被证明是有效的

  

Particular entries of the matrix of optimal intervals (later called the OI
matrix) where taken from the formulas used in the Algorithm SM-2.

  

As a consequence, SuperMemo 4 was intended to yield an ultimate definition of
the function of optimal intervals.

  

**Algorithm SM-4 used in SuperMemo 4.0:**

  * Split the knowledge into smallest possible items
  * With all items associate an E-Factor equal to 2.5
  * Tabulate the OI matrix for various repetition numbers and E-Factor categories (see Fig. 3.2)_[similar matrix can be viewed as the Optimum Interval matrix in__[SuperMemo 98](http://www.supermemo.com/articles/soft/sm9.htm)__ with _**[Tools](http://www.supermemo.com/help/tools.htm)**** : Statistics : ****[Analysis](http://www.supermemo.com/help/analysis.htm)**** : Matrices : Intervals**_]_
  * Use the following repetition spacing to obtain the initial OI matrix:  
OI(1,EF):=1  
OI(2,EF):=6  
for n>2 OI(n,EF):=OI(n-1,EF)*EF  
where:  
OI(n,EF) - optimal inter-repetition interval after the n-th repetition (in
days) for items with E-Factor equal EF,

  * Use the OI matrix to determine inter-repetition intervals:  
I(n,EF):=OI(n,EF)  
where:  
I(n,EF) - the n-th inter-repetition interval for an item whose E-Factor equals
EF (in days),  
OI(n,EF) - the entry of the OI matrix corresponding to the n-th repetition and
the E-Factor EF

  * After each repetition estimate the quality of the repetition response in the 0-5 grade scale (cf. [Algorithm SM-2](http://www.supermemo.com/english/ol/sm2.htm)).
  * After each repetition modify the E-Factor of the recently repeated item according to the formula:  
EF':=EF+(0.1-(5-q)*(0.08+(5-q)*0.02))  
where:  
EF' - new value of the E-Factor,  
EF - old value of the E-Factor,  
q - quality of the response in the 0-5 grade scale.  
If EF is less than 1.3 then let EF be 1.3.

  * After each repetition modify the relevant entry of the OI matrix.
  * An exemplary formula could look as follows (the actual formula used in SuperMemo 4 was more intricate):  
OI':=_interval+interval_*(1-1/EF)/2*(0.25*q-1)

  * OI'':=(1-_fraction_)*OI+_fraction_*OI'
  * where:  
OI'' - new value of the OI entry,  
OI' - auxiliary value of the OI entry used in calculations,  
OI - old value of the OI entry,  
_interval_ - interval used before the considered repetition (i.e. the last
used interval for the given item),

  * _fraction_ - any number between 0 and 1 (the greater it is the faster the changes of the OI matrix),
  * EF - E-Factor of the repeated item,  
q - quality of the response in the 0-5 grade scale.  
Note that for q=4 the OI does not change and that for q=5 the OI increases 4
times less than it decreases for q=0.  
Note also that the maximum change of the OI equals (I(n)-I(n-1))/2 in terms of
the repetition spacing used in [Algorithm
SM-2](http://www.supermemo.com/english/ol/sm2.htm) (i.e. (OI-OI/EF)/2).

  * 8\. If the quality response was lower than 3 then start repetitions for the item from the beginning without changing the E-Factor.
  * 9\. After each repetition session of a given day repeat again all the items that scored below four in the quality assessment. Continue the repetitions until all of these items score at least four

As it was mentioned earlier, the Algorithm SM-4 was implemented in SuperMemo 4
and was used between March 9, 1989 and October 17, 1989. **Although the main
concept of modifying the function of optimal intervals seemed to be a major
step forward, the implementation of the algorithm was a failure**. The basic
insufficiency of the algorithm appeared to result from formulas applied in
modification of the OI matrix.

  

  

