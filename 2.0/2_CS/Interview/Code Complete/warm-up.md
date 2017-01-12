# 前期热身

## 重点细节

1. 准备好自我介绍，因为面试官往往没时间看你简历，或者一边听你自我介绍一边看简历，要让他们感到对 CS 的热爱，对工作的向往和对自己以往经历的自豪。要提的点应该包括：
    + 为什么是这个公司
    + 为什么是这个职位
    + 为什么是我
2. 交流非常非常重要，锻炼自己边说边写的能力，一面理清思路，一面让面试官了解自己在干什么
3. 放轻松，保持自信，说话大声点流利点
4. 在函数之前写几句文档
5. 一开始 validate input
6. 在合适的地方加注释
7. 面试完之后立即发 Thank you letter

## 技术面试的流程模板

1. 明确题意：通过与面试官交流明确需要解答的问题。这部分主要为了让自己放松心态，并且给面试官留下你具有良好团队意识和交流能力的印象。
2. 描述大体思路：描述你打算用什么算法，什么数据结构。主要是为了让面试官了解你的思维过程，如果你给出的解答与他想要的答案偏差太多，可以及时纠正。同时，描述思路也给了你自己思考的机会。
3. 实现算法：先处理边界条件。对于重要的算法模块，加一些注释或者与面试官进行交流。目的是让面试官始终了解你在做什么，算法框架是什么。
4. 跑一个测试：用一个测试用例(test case)走一遍你写的程序。目的在于和面试官一起确保你的算法是有效的，可以在过程中及时发现并纠正自己的错误。同时，给面试官留下你有写单元测试习惯的良好印象。
5. 描述算法复杂度，回答面试官的问题

## 总体策略

1. 越好的公司越要放到最后面试。因为你每面试一次，尤其是 onsite，基本上会都有新的感悟，都会发现自己之前准备上的不足，而这个过程本身就是一种提高，所以说基本上是越面越强的。
2. 投简历也要抓住时机不要错过机会：许多大公司招new grad都是在某一特定时间内，过了这段招满了就不招了。今年的例子比如微软思科雅虎。这三家公司我都没拿到面试。不过好在flg都是全年招人的。

## 简历怎么投

1. 推荐顺序是内推 > 直接找recruiter > 网申，非常不建议网申（小公司除外，初期我们还是需要投一些小公司练手的，海投的途径我主要用过以下几个，indeed，Linkedin，jobvite），虽然不是所有网申都石沉大海，但是网申的效率远比内推或者直接找recruiter联系低得多，直接找recruiter是个很不错的途径。
2. 如何找内推或者recruiter的联系方式？内推基本有两种途径找，一是找自己的学长学姐，无论是之前就认识还是在LinkedIn上现加的，一般客气一点人家还是愿意内推的，毕竟大家出来混都不容易。二是去各大论坛找内推帖，绝大多数的内推帖都还是很靠谱的，至于如何搜，“site:论坛域名 公司名+内推”屡试不爽。
3. recruiter的联系方式也有两种途径，一是一般来说周围会有一些正在面或者已经面过这一公司的同学，面试过程中会有一些recruiter联系过他们，把这些recruiter的邮箱要过来就好。二是去LinkedIn上搜。

## 过来人经验

1. Cracking coding interview是本好书,不过不必要做好几遍，把关键的几章自己写一遍就好了，如果面了一段时间，发现自己那一块不好，可以重点突击
2. 面试以考代练的效果还是很好的
3. 口语很重要，从我的观察来看，身边口语好的人通常能拿到更过的offer
4. Google很慢，而且一催就挂，不要拖太晚面google，否则人家觉得你的deadline太早会把你拒掉。
5. 有人在做leetcode,我自己做了一下觉得挺难,一般公司考不了那么难得题
6. 如果很想要一个offer，寄得给recruiter写thank you letter和follow up letter。 我samsung
return offer, Epic, Apple的offer都是follow up+ thank you very much出来的。
7. Apple很少给new grad发interview, 我的面试就是refer出来的
8. GPA貌似没人看，3.5以上绝对够用，没到3.5的同学也照样拿到好的offer，不要为了GPA选水课，几乎每个面试都会过简历，没有有技术含量的project会是硬伤

## Interview Preparation Grid

针对每个 project，列出以下几个方面的相关总结关键词，一定要是**特别精炼的短语**，不要长篇大论的句子：

+ Challenges
+ Mistakes/Failures
+ Enjoyed
+ Leadership
+ Conflicts
+ What You'd Do Differently

### 细致准备重点项目

两三个 project 要重点准备，除了上面提到的方面，还需要能够细致介绍：

+ Technical decisions
+ Choices of technologies(tradeoff)

## 常见面试问题

> Tell me about yourself

可以按照如下的方式组织准备

1. **Current Role [Headline Only]**: I'm a graduate student in Carnegie Mellon University majored in Electrical and Computer Engineering.
2. **College**: I majored in Software Engineering for my undergraduate and had a 6-month internship in Microsoft.
3. **Current Role [Details]**: Learning both the software and the hardware, I know how to write great code on different platforms, especially computer vision and machine learning.
4. **Outside of Work**: Outside of work, I've been working on mobile app development. One of my app named League of Legends Wiki has over 700K downloads with an average rating of 4.5 out of 5.
5. **Wrap Up**: I'm looking for a full time job as I'll get my master degree next year and your company caught my eye. I've always been interested in creating something new so I'd like to talk more with you about the xxx position in your company.

注意见缝插针描述自己的闪光点，让人感兴趣和印象深刻。

> What are your weaknesses

回答技巧：实话实话，不要装逼。点明缺点之后重点强调自己是如何克服的。

个人参考答案：Sometimes, I may lose focus on the whole project while plunge into very detailed problems. It's not bad to spend more time finding the best solution. But it may be better to finish the most critical part first. As it is, I'll draw the whole design on paper and put it just in front of the monitor so that I can easily find out what I should focus on.

## 问面试官的问题

大概有三类问题

### Genuine Questions

跟公司，工作有关的问题，例如

1. What brought you to this company?
2. What has been most challenging for you?
3. Do you have program managers? If there is a conflicts between developer and managers, how do you solve it?

### Insightful Questions

这类问题通常需要对公司有比较深入的研究，例如

1. I noticed that you use technology X. How do you handle problem Y?
2. Why did this product choose to use technology X over technology Y?

### Passion Questions

展现激情和学习兴趣

1. I'm very interested in machine learning, and I'd love to learn more about it. What opportunities are there at this company to learn about this?
2. I'm not familiar with technology X, but it sounds like a very interesting solution. Could you tell me a bit more about how it works?

## 回答问题技巧

+ 不要过多涉及细节，而是用数据对比或者面试官能听懂的内容来介绍
+ 多说 I 而不是 We，说自己扮演的角色和所做的工作
+ 结构式问题回答

### Nugget First

开门见山，先用一句话概括，然后再逐步推进到细节部分

### S.A.R. (Situation, Action, Result)

+ outline the situation
+ explain the actions you took
+ describe the result

**Action 部分是最需要着力的地方，逻辑清晰，分点叙述，主要不要涉及过多细节**。

精雕细琢故事部分，字里行间体现出自己的一些特质，如：Initiative/Leadership, Empathy, Compassion, Humility, Teamwork/Helpfulness


