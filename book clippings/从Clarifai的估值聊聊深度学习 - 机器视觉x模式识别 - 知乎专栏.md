  

# 从Clarifai的估值聊聊深度学习

[ ![](%E4%BB%8EClarifai%E7%9A%84%E4%BC%B0%E5%80%BC%E8%81%8A%E8%81%8A%E6%B7%B1%
E5%BA%A6%E5%AD%A6%E4%B9%A0%20-%20%E6%9C%BA%E5%99%A8%E8%A7%86%E8%A7%89x%E6%A8%A
1%E5%BC%8F%E8%AF%86%E5%88%AB%20-%20%E7%9F%A5%E4%B9%8E%E4%B8%93%E6%A0%8F.resour
ces/e3a7c0c55_xs.jpg)Filestorm](http://www.zhihu.com/people/filestorm) · 3 个月前

[转载请注明出处]

前几天和 Ayden
[@叶瀚中](http://www.zhihu.com/people/a92a37fdefffe9f8c0d84cb5b885e408) 聊天时，提到了
[www.clarifai.com__](http://zhuanlan.zhihu.com/www.clarifai.com) 这家公司。

此前，我已经从各方消息中听说过创始人Matt Zeiler最近打算卖公司。甚至还和朋友打赌说这个公司能不能以$5M出手。

先说结论：

**这个公司的水准在13年称得上世界第一 。但是这并不能给该公司以世界级的价值。**  

  
Clarifai创始人Matt Zeiler 是 New York University (NYU) Rob
Fergus教授门下的学生。要知道，从上个世纪开始，NYU就一直是neural computation的重镇。现在Deep
net的前身ConvNet，就是出自 NYU 的 Yann LeCun教授组。  
Matt在PhD期间，还曾经在Google跟Jeff Dean实习过。不知道有没有学到什么独门绝技。总之，2013年Image Net
Challenge以来，他在Computer vision圈子就非常出名了。  
  
讲到这里就不得不提Image Net Challenge。以前的Computer
vision的数据集都非常小，最多不过几百类，几万张图，这带来一个问题——我们无法设计特别复杂的计算视觉模型。否则模型的复杂度太高，数据量太少，就会有
[Overfitting__](https://en.wikipedia.org/wiki/Overfitting) 的问题。  
  
2012年，华人教授李菲菲牵头搞了一个**巨大**的数据库 [ImageNet__](http://www.image-
net.org/)。到今天为止，Image Net上已经有了14,197,122张图片了。对每张图片，由人来手工记录图片中物体的名字，并向业界宣布，同学们，
如果你们谁开发出来了新的物体识别算法，就在我家的数据库上试试吧。  
  
于是2012年，就有了这个LSVRC - Large Scale Visual Recognition Challenge.
最终比赛结果在2012年底的NIPS会议上公布。  
  
当时，大多数的研究小组还都在用传统computer vision算法的时候，多伦多大学的Hinton祭出deep net这样一个大杀器。差距是这样的：  
第一名Deepnet的错误率是0.16422  
第二名日本东京大学的错误率是0.2617  
第三名牛津大学的错误率是0.2679  
  
如果我们仔细看看第二名和第三名的实现，会发现大家使用的技术框架非常接近，都是local descriptor + feature
compression这套。而在这套实现上，二者的差距几乎是可以忽略的——都完全不是deep net的对手。  
具体结果参见：[ImageNet Large Scale Visual Recognition Competition 2012
(ILSVRC2012)__](http://www.image-net.org/challenges/LSVRC/2012/results.html)  
  
说来也巧，我恰好也参加了NIPS
12，亲身感受了这在后来看来的历史时刻。Hinton当时放话说：“如果你没有参加前面十几年的NIPS，没关系，因为直到今年，Deep net才真正work了
”。虽然deepnet取得了如此瞩目的成绩，但是就在当时，还是有大量与会教授表示不愿意接受deepnet。这里面指的“不愿意”分几个层次  
1\. Deepnet很可能是某种形式的overfitting，因为它里面有6000万个参数。  
2\. Deepnet作为一个黑盒子，不可解释。所以对cv的贡献非常有限  
3\. Deepnet只能解决物体识别这一个问题，而物体检测、分割等经典问题还需要其他人的努力。  
  
在1%的性能提升都可以称之为“major contribution”的时代，被一个和最近10年computer vision，尤其是object recog
nition领域的进展几乎没有交集的方法，超过了10个百分点，这也难怪大家纷纷表示不承认也不接受deepnet的革命。但是，洪水的闸门已经打开。。。  
  
  
  
一年后，新一轮的Large Scale Visual Recognition Challenge又开始了，这时候我们不难发现，Deep
net的计算框架已经一统江湖了：  
[ImageNet Large Scale Visual Recognition Competition 2013
(ILSVRC2013)__](http://www.image-net.org/challenges/LSVRC/2013/results.php)  
  
其中Matt Zeiler ([http://Clarifai.com__](http://clarifai.com/))
的算法排名第一，在不用额外训练数据的情况下，跑到了error rate 0.1174这样的成绩。  
这个成绩是这样解读的：  
任选一张图片，扔给算法，算法返回5个结果。如果5个结果中，有一个猜对了物体类别，就算正确。换言之，如果允许猜5次，Clarifai已经有接近90%的准确率了
。这里的物体类别包括了英语中两万多个名词，几乎涵盖了各大类别。  
  
  
但是，2013年和2012年的情况又有很大不同。  
  
  
排名第二的新加坡国立大学的误差，是0.129，第三名ZF的误差是0.133，这都与Clarifai非常接近。再也无法出现Hinton组独步江湖的场面了。  
  
  
今年的结果还没出来，要等到12月份的NIPS 2014啦。我听到过一些小道消息，在LSVRC 12的训练集（因为测试集保密，所以线下研究的时候，大家都会辟出
一部分训练集做测试），某公司已经能跑到10%以内的误差了。当然Clarifai也没闲着，在他主页上已经更新了准确率到10.7%了。  
  
  
  
那么Deepnet的难点在什么地方呢？从最近CVPR 14的情况来看，圈子在这个方面作出的改进，几乎见不到什么质的飞跃。调整deepnet在大多数时候变成了
一门实验科学：一方面，对2012年原作的修改太大，会导致识别率惨不忍睹，另一方面，很少有人能有Stefan
Mallat那样的数学功底能从理论层面分析deep learning到底在干什么。但是，由于图片的数据量实在太大，站在工程角度上，如何能够在几周甚至几天内完
成几百万甚至上千万图片的训练，就是一个非常非常技术的活儿了。  
  
  
在工程实现方面，deepnet开山paper的一作Alex Krizhevsky已经开源了他的代码 [https://code.google.com/p
/cuda-convnet/...__](https://code.google.com/p/cuda-convnet/)
，并且又另起了一个convnet2的项目 [https://code.google.com/p/cuda-
convnet2/...__](https://code.google.com/p/cuda-convnet2/)。  
  
必须提到的，是UC-Berkeley Trevor Darrel的贾扬清，把他写的deepnet开源了。[https://github.com/BVLC/c
affe__](https://github.com/BVLC/caffe) 这个功能很全面，性能很高的deep
net，不断被大量的开发者完善。目前来看，它是最有希望成为deep
net通用架构的一个基础框架。目前，基于Caffe的识别误差，已经降到0.131了——非常接近Matt
Zeiler的结果。但是要注意，这些结果几乎都是开源的。  
  
换言之，一群有过几年cv经验的初创小团队，基本都可以超过Hinton 2012年的世界纪录，与2013年Matt Zeiler的纪录非常接近。这简直让我想起
战争之王检阅娃娃兵的片段：一个本科生训练出来的deepnet，和一个有30年经验的大学教授训练出来的deepnet，其实并没有区别。  
  
  

有这么个传说，真假待考，权当八卦说说吧。当年Hinton组在NIPS 12会场上，就被各家公司争相竞购。Hinton带着Google/MS/Baidu等公司
的负责人，找了间屋子说我们团队竞拍，每次加价一百万。后来嫌一百万太慢，改加价两百万。再后来的故事，大家就都知道了。。。

但是[http://Clarifai.com__](http://clarifai.com/)的估价和Hinton组被收购的故事又有所不同。一方面，Hint
on本人是当今世界上最杰出（哪怕是2012年deepnet火爆之前）的machine learning研究者，20多年前back propagation也是
他的杰作，而且deepnet的正宗首创效应也不可忽视。另一方面，deepnet席卷整个cv圈子带来的各种效应（比如开源），可能也是大家所始料不及的。

  

最后，一方面，我希望[http://Clarifai.com__](http://clarifai.com/)能被收购，引起更多对cv的关注。另一方面也希望
学术圈能尽快找准方向，尽早结束实验报告为主的探索期，能够真正从本质上解释这个伟大的理论究竟为什么work。

__分享

__举报

__99 赞 __

[ ![](%E4%BB%8EClarifai%E7%9A%84%E4%BC%B0%E5%80%BC%E8%81%8A%E8%81%8A%E6%B7%B1%
E5%BA%A6%E5%AD%A6%E4%B9%A0%20-%20%E6%9C%BA%E5%99%A8%E8%A7%86%E8%A7%89x%E6%A8%A
1%E5%BC%8F%E8%AF%86%E5%88%AB%20-%20%E7%9F%A5%E4%B9%8E%E4%B8%93%E6%A0%8F.resour
ces/da8e974dc_xs.jpg) 吴次仁](http://www.zhihu.com/people/wu-ci-ren-17)[ ![](%E4%
BB%8EClarifai%E7%9A%84%E4%BC%B0%E5%80%BC%E8%81%8A%E8%81%8A%E6%B7%B1%E5%BA%A6%E
5%AD%A6%E4%B9%A0%20-%20%E6%9C%BA%E5%99%A8%E8%A7%86%E8%A7%89x%E6%A8%A1%E5%BC%8F
%E8%AF%86%E5%88%AB%20-%20%E7%9F%A5%E4%B9%8E%E4%B8%93%E6%A0%8F.resources/4b019a
2fa_xs.jpg) 宁潇](http://www.zhihu.com/people/zhu-xiao-17)[ ![](%E4%BB%8EClarifa
i%E7%9A%84%E4%BC%B0%E5%80%BC%E8%81%8A%E8%81%8A%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B
9%A0%20-%20%E6%9C%BA%E5%99%A8%E8%A7%86%E8%A7%89x%E6%A8%A1%E5%BC%8F%E8%AF%86%E5
%88%AB%20-%20%E7%9F%A5%E4%B9%8E%E4%B8%93%E6%A0%8F.resources/da8e974dc_xs.jpg)
Qiang Hao](http://www.zhihu.com/people/qiang-hao-97)[ ![](%E4%BB%8EClarifai%E7
%9A%84%E4%BC%B0%E5%80%BC%E8%81%8A%E8%81%8A%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0
%20-%20%E6%9C%BA%E5%99%A8%E8%A7%86%E8%A7%89x%E6%A8%A1%E5%BC%8F%E8%AF%86%E5%88%
AB%20-%20%E7%9F%A5%E4%B9%8E%E4%B8%93%E6%A0%8F.resources/d063c8df0_xs.jpg)
王丰](http://www.zhihu.com/people/wdwind)[ ![](%E4%BB%8EClarifai%E7%9A%84%E4%BC%
B0%E5%80%BC%E8%81%8A%E8%81%8A%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%20-%20%E6%9C
%BA%E5%99%A8%E8%A7%86%E8%A7%89x%E6%A8%A1%E5%BC%8F%E8%AF%86%E5%88%AB%20-%20%E7%
9F%A5%E4%B9%8E%E4%B8%93%E6%A0%8F.resources/da2a56294_xs.jpg) huzhi
zhang](http://www.zhihu.com/people/huzhi-zhang) __

[ __ **Brave New World - 欢迎提问** ](http://zhuanlan.zhihu.com/cvprnet/19821288)
[ __ **visual saliency与benchmark tricks**
](http://zhuanlan.zhihu.com/cvprnet/19821399)

__17 条评论

  * [ ![](%E4%BB%8EClarifai%E7%9A%84%E4%BC%B0%E5%80%BC%E8%81%8A%E8%81%8A%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%20-%20%E6%9C%BA%E5%99%A8%E8%A7%86%E8%A7%89x%E6%A8%A1%E5%BC%8F%E8%AF%86%E5%88%AB%20-%20%E7%9F%A5%E4%B9%8E%E4%B8%93%E6%A0%8F.resources/da8e974dc_l.jpg) ](http://www.zhihu.com/people/yin-pei-jie-47)

[尹沛劼](http://www.zhihu.com/people/yin-pei-jie-47)

对最后的深度学习的本质很感兴趣，但是几乎看不到paper讨论这些(印象中Lecun还是Bengio有paper讨论过预训练的意义)。
有没有哪些组或者paper在关注这个领域？

3 个月前 __回复 __赞 __举报

  * [ ![](%E4%BB%8EClarifai%E7%9A%84%E4%BC%B0%E5%80%BC%E8%81%8A%E8%81%8A%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%20-%20%E6%9C%BA%E5%99%A8%E8%A7%86%E8%A7%89x%E6%A8%A1%E5%BC%8F%E8%AF%86%E5%88%AB%20-%20%E7%9F%A5%E4%B9%8E%E4%B8%93%E6%A0%8F.resources/55d68481b_l.jpg) ](http://www.zhihu.com/people/dennyx)

[DennyX](http://www.zhihu.com/people/dennyx)

这公司才两年吧，为了办公司都提前毕业了。。

3 个月前 __回复 __赞 __举报

  * [ ![](%E4%BB%8EClarifai%E7%9A%84%E4%BC%B0%E5%80%BC%E8%81%8A%E8%81%8A%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%20-%20%E6%9C%BA%E5%99%A8%E8%A7%86%E8%A7%89x%E6%A8%A1%E5%BC%8F%E8%AF%86%E5%88%AB%20-%20%E7%9F%A5%E4%B9%8E%E4%B8%93%E6%A0%8F.resources/4cf2223ae_l.jpg) ](http://www.zhihu.com/people/xiaoyu-shi-31)

[xiaoyu shi](http://www.zhihu.com/people/xiaoyu-shi-31)

我倒是觉得，CNN有点半学习半搜索的意思。真正需要庞大的数据量来支撑最后的性能的，只有搜索。真正意义上的识别和学习不应该是基于这么庞大的数据量的。就像Ng说
的，我们教小孩子认识苹果，是不会让他认几千个的

3 个月前 2 赞 __回复 __赞 __举报

  * [ ![](%E4%BB%8EClarifai%E7%9A%84%E4%BC%B0%E5%80%BC%E8%81%8A%E8%81%8A%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%20-%20%E6%9C%BA%E5%99%A8%E8%A7%86%E8%A7%89x%E6%A8%A1%E5%BC%8F%E8%AF%86%E5%88%AB%20-%20%E7%9F%A5%E4%B9%8E%E4%B8%93%E6%A0%8F.resources/e3a7c0c55_l.jpg) ](http://www.zhihu.com/people/filestorm)

[Filestorm](http://www.zhihu.com/people/filestorm)（作者） 回复
[DennyX](http://www.zhihu.com/people/dennyx)

不用两年，成立第一天就是奔着人才的。毕竟有Hinton叫价的故事在先。最近Matt在四处联系买家。

3 个月前 __回复 __赞 __举报

  * [ ![](%E4%BB%8EClarifai%E7%9A%84%E4%BC%B0%E5%80%BC%E8%81%8A%E8%81%8A%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%20-%20%E6%9C%BA%E5%99%A8%E8%A7%86%E8%A7%89x%E6%A8%A1%E5%BC%8F%E8%AF%86%E5%88%AB%20-%20%E7%9F%A5%E4%B9%8E%E4%B8%93%E6%A0%8F.resources/cd61c0771_l.jpg) ](http://www.zhihu.com/people/alan-huang)

[ALAN Huang](http://www.zhihu.com/people/alan-huang)

写的很好。不过ConvNet在这个数据集overfitting 并不一定。 从定义上讲，如果在测试集合上仍能保持很高的正确率，就不算。
况且200*200的图片有四万像素，6000万参数即使都是像素也只有1500张图，每个类别也才一两张而已。

3 个月前 __回复 __赞 __举报

  * [ ![](%E4%BB%8EClarifai%E7%9A%84%E4%BC%B0%E5%80%BC%E8%81%8A%E8%81%8A%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%20-%20%E6%9C%BA%E5%99%A8%E8%A7%86%E8%A7%89x%E6%A8%A1%E5%BC%8F%E8%AF%86%E5%88%AB%20-%20%E7%9F%A5%E4%B9%8E%E4%B8%93%E6%A0%8F.resources/da8e974dc_l.jpg) ](http://www.zhihu.com/people/andy-wong)

[Andy Wong](http://www.zhihu.com/people/andy-wong)

清华大牛再现江湖

3 个月前 __回复 __赞 __举报

  * [ ![](%E4%BB%8EClarifai%E7%9A%84%E4%BC%B0%E5%80%BC%E8%81%8A%E8%81%8A%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%20-%20%E6%9C%BA%E5%99%A8%E8%A7%86%E8%A7%89x%E6%A8%A1%E5%BC%8F%E8%AF%86%E5%88%AB%20-%20%E7%9F%A5%E4%B9%8E%E4%B8%93%E6%A0%8F.resources/e3a7c0c55_l.jpg) ](http://www.zhihu.com/people/filestorm)

[Filestorm](http://www.zhihu.com/people/filestorm)（作者） 回复 [xiaoyu
shi](http://www.zhihu.com/people/xiaoyu-shi-31)

你可以看下 Intriguing properties of neural networks 这篇。里面介绍了很多有趣的现象。。。

3 个月前 __回复 __赞 __举报

  * [ ![](%E4%BB%8EClarifai%E7%9A%84%E4%BC%B0%E5%80%BC%E8%81%8A%E8%81%8A%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%20-%20%E6%9C%BA%E5%99%A8%E8%A7%86%E8%A7%89x%E6%A8%A1%E5%BC%8F%E8%AF%86%E5%88%AB%20-%20%E7%9F%A5%E4%B9%8E%E4%B8%93%E6%A0%8F.resources/e3a7c0c55_l.jpg) ](http://www.zhihu.com/people/filestorm)

[Filestorm](http://www.zhihu.com/people/filestorm)（作者） 回复 [ALAN
Huang](http://www.zhihu.com/people/alan-huang)

到底是不是其实谁也不知道。。。比如我问：所有图片的流形的维度是多少？ 只是在deepnet刚问世的时候，不少反对派大佬都是这个态度，要么是嫌imageNet
本身有bisa，要么是批评6000万个参数太多，这些反对意见总结一下，都是一句话，overfitting嫌疑很重！ 但是话说回来，overfitting
the model of the world好像也不是件坏事 ;)

3 个月前 __回复 __赞 __举报

  * [ ![](%E4%BB%8EClarifai%E7%9A%84%E4%BC%B0%E5%80%BC%E8%81%8A%E8%81%8A%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%20-%20%E6%9C%BA%E5%99%A8%E8%A7%86%E8%A7%89x%E6%A8%A1%E5%BC%8F%E8%AF%86%E5%88%AB%20-%20%E7%9F%A5%E4%B9%8E%E4%B8%93%E6%A0%8F.resources/da8e974dc_l.jpg) ](http://www.zhihu.com/people/xing-yu-16-40)

[星宇](http://www.zhihu.com/people/xing-yu-16-40)

Hinton带着Google/MS/Baidu等公司的负责人去竞价，后面的故事是什么呢？

3 个月前 __回复 __赞 __举报

  * [ ![](%E4%BB%8EClarifai%E7%9A%84%E4%BC%B0%E5%80%BC%E8%81%8A%E8%81%8A%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%20-%20%E6%9C%BA%E5%99%A8%E8%A7%86%E8%A7%89x%E6%A8%A1%E5%BC%8F%E8%AF%86%E5%88%AB%20-%20%E7%9F%A5%E4%B9%8E%E4%B8%93%E6%A0%8F.resources/0173bebdc_l.jpg) ](http://www.zhihu.com/people/shi-jia-xin-75)

[石佳欣](http://www.zhihu.com/people/shi-jia-xin-75)

[@常铖](http://www.zhihu.com/people/e94cfb9c1539ab067a245876ef24d6d0)

3 个月前 __回复 __赞 __举报

  * [ ![](%E4%BB%8EClarifai%E7%9A%84%E4%BC%B0%E5%80%BC%E8%81%8A%E8%81%8A%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%20-%20%E6%9C%BA%E5%99%A8%E8%A7%86%E8%A7%89x%E6%A8%A1%E5%BC%8F%E8%AF%86%E5%88%AB%20-%20%E7%9F%A5%E4%B9%8E%E4%B8%93%E6%A0%8F.resources/a551ebd82_l.jpg) ](http://www.zhihu.com/people/xiaojidan)

[xiaojidan](http://www.zhihu.com/people/xiaojidan)

厉害， 不知道大神可以指导下，如何开展深入学习？

3 个月前 __回复 __赞 __举报

  * [ ![](%E4%BB%8EClarifai%E7%9A%84%E4%BC%B0%E5%80%BC%E8%81%8A%E8%81%8A%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%20-%20%E6%9C%BA%E5%99%A8%E8%A7%86%E8%A7%89x%E6%A8%A1%E5%BC%8F%E8%AF%86%E5%88%AB%20-%20%E7%9F%A5%E4%B9%8E%E4%B8%93%E6%A0%8F.resources/da8e974dc_l.jpg) ](http://www.zhihu.com/people/andy-wong)

[Andy Wong](http://www.zhihu.com/people/andy-wong) 回复
[Filestorm](http://www.zhihu.com/people/filestorm)（作者）

sorry，没表述清楚。我是指贾杨青，和我们实验室postdoc在清华是labmates。不过楼主的背景也很牛啊 嘿嘿

3 个月前 __回复 __赞 __举报

  * [ ![](%E4%BB%8EClarifai%E7%9A%84%E4%BC%B0%E5%80%BC%E8%81%8A%E8%81%8A%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%20-%20%E6%9C%BA%E5%99%A8%E8%A7%86%E8%A7%89x%E6%A8%A1%E5%BC%8F%E8%AF%86%E5%88%AB%20-%20%E7%9F%A5%E4%B9%8E%E4%B8%93%E6%A0%8F.resources/e3a7c0c55_l.jpg) ](http://www.zhihu.com/people/filestorm)

[Filestorm](http://www.zhihu.com/people/filestorm)（作者） 回复 [Andy
Wong](http://www.zhihu.com/people/andy-wong)

额，露怯了。。。jyq的model已经是很多地方的标配了，这才是真正的大牛。。。我赶紧退让。。。

3 个月前 __回复 __赞 __举报

  * [ ![](%E4%BB%8EClarifai%E7%9A%84%E4%BC%B0%E5%80%BC%E8%81%8A%E8%81%8A%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%20-%20%E6%9C%BA%E5%99%A8%E8%A7%86%E8%A7%89x%E6%A8%A1%E5%BC%8F%E8%AF%86%E5%88%AB%20-%20%E7%9F%A5%E4%B9%8E%E4%B8%93%E6%A0%8F.resources/f82acfea0_l.jpg) ](http://www.zhihu.com/people/location-xyy)

[FogLikelihood](http://www.zhihu.com/people/location-xyy)

Caffe真心不错。挺重要的一点是，caffe的卷积实现不依赖hand tuned cuda code.
而是直接构造在cublas上。这意味着每一次driver和硬件升级，几乎都能带来线性的性能提升。而且其代码结构清晰简洁，非常易于扩展。对比起来cuda
covnet改起来真是无语凝噎。

3 个月前 1 赞 __回复 __赞 __举报

  * [ ![](%E4%BB%8EClarifai%E7%9A%84%E4%BC%B0%E5%80%BC%E8%81%8A%E8%81%8A%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%20-%20%E6%9C%BA%E5%99%A8%E8%A7%86%E8%A7%89x%E6%A8%A1%E5%BC%8F%E8%AF%86%E5%88%AB%20-%20%E7%9F%A5%E4%B9%8E%E4%B8%93%E6%A0%8F.resources/da8e974dc_l.jpg) ](http://www.zhihu.com/people/xingxing-1111111)

[圣行](http://www.zhihu.com/people/xingxing-1111111)

“一群有过几年cv经验的初创小团队，基本都可以超过Hinton 2012年的世界纪录，与2013年Matt Zeiler的纪录非常接近。这简直让我想起战争之
王检阅娃娃兵的片段：一个本科生训练出来的deepnet，和一个有30年经验的大学教授训练出来的deepnet，其实并没有区别。”  
  
会用dl的人越来越多，全世界有几个大牛真正理解deepnet？

2 个月前 __回复 __赞 __举报

  * [ ![](%E4%BB%8EClarifai%E7%9A%84%E4%BC%B0%E5%80%BC%E8%81%8A%E8%81%8A%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%20-%20%E6%9C%BA%E5%99%A8%E8%A7%86%E8%A7%89x%E6%A8%A1%E5%BC%8F%E8%AF%86%E5%88%AB%20-%20%E7%9F%A5%E4%B9%8E%E4%B8%93%E6%A0%8F.resources/e3a7c0c55_l.jpg) ](http://www.zhihu.com/people/filestorm)

[Filestorm](http://www.zhihu.com/people/filestorm)（作者） 回复
[圣行](http://www.zhihu.com/people/xingxing-1111111)

有志摘取”理解deepnet桂冠“的人，会把好的ImageNet成绩当做信号，而非终点。  
  
在这两年的大环境下，能做到这一点还发得出paper为你我读到的，怕是不多。

2 个月前 __回复 __赞 __举报

  * [ ![](%E4%BB%8EClarifai%E7%9A%84%E4%BC%B0%E5%80%BC%E8%81%8A%E8%81%8A%E6%B7%B1%E5%BA%A6%E5%AD%A6%E4%B9%A0%20-%20%E6%9C%BA%E5%99%A8%E8%A7%86%E8%A7%89x%E6%A8%A1%E5%BC%8F%E8%AF%86%E5%88%AB%20-%20%E7%9F%A5%E4%B9%8E%E4%B8%93%E6%A0%8F.resources/da8e974dc_l.jpg) ](http://www.zhihu.com/people/wu-bin-28)

[吴斌](http://www.zhihu.com/people/wu-bin-28)

请教一下，在Google的“Building High-level Features Using Large Scale Unsupervised
Learning”论文中提到。他们使用Deep
Net基于ImageNet的2011数据集，1400多万数据，22000多分类，识别精度（accuracies）是15.8%。
怎么比较这个结果与LSVRC2012的结果（错误率是0.16422）？
换句话说，给算法5次机会，是否合理，怎么评价这两组测试结果？（给读者的印象，他们的差距实在是很大。）

15 天前 __回复 __赞 __举报

![](%E4%BB%8EClarifai%E7%9A%84%E4%BC%B0%E5%80%BC%E8%81%8A%E8%81%8A%E6%B7%B1%E5
%BA%A6%E5%AD%A6%E4%B9%A0%20-%20%E6%9C%BA%E5%99%A8%E8%A7%86%E8%A7%89x%E6%A8%A1%
E5%BC%8F%E8%AF%86%E5%88%AB%20-%20%E7%9F%A5%E4%B9%8E%E4%B8%93%E6%A0%8F.resource
s/ff7a681a0_l.jpg)

写下你的评论…

  

