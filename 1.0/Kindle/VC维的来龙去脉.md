#VC维的来龙去脉

在台湾大学机器学习基石课程的基础上，我们简单聊聊“VC维的来龙去脉”。我们将解决以下问题：为什么某机器学习方法是可学习的？为什么会有过拟合？拿什么来衡量机器学习模型的复杂度？深度学习与VC维的关系？

---

在讲VC维之前，我们不妨来说说VC维的历史。而说起VC维的历史，又不得不提起神经网络，一方面是因为神经网络与VC维的发明过程是交织在一起的，另一方面是由于神经网络乏善可陈的泛化控制方法，深度学习在理论基础上一直被怀疑，甚至神经网络和VC维的代表SVM还一起争风吃醋过好多年。

---

1943年，模拟神经网络由麦卡洛可（McCulloch）和皮茨（Pitts)提出，他们分析了理想化的人工神经元网络，并且指出了它们进行简单逻辑运算的机制。

---

1957年，康奈尔大学的实验心理学家弗兰克·罗森布拉特(Rosenblatt)在一台IBM–704计算机上模拟实现了一种他发明的叫作“感知机”（Perceptron）的神经网络模型。神经网络与支持向量机都源自于感知机（Perceptron）。

---

1971年，V. Vapnik and A. Chervonenkis在论文“On the uniform convergence of relative frequencies of events to their probabilities”中提出VC维的概念。

---

1974年，沃波斯（Werbos）的博士论文证明了在神经网络多加一层，并且利用“后向传播”（Back-propagation）学习方法，可以解决XOR问题。那时正是神经网络研究的低谷，文章不合时宜。

---

1982年，在加州理工担任生物物理教授的霍普菲尔德，提出了一种新的神经网络，可以解决一大类模式识别问题，还可以给出一类组合优化问题的近似解。这种神经网络模型后被称为霍普菲尔德网络。

---

1993年，Corinna Cortes和Vapnik等人提出了支持向量机(support vector machine)。神经网络是多层的非线性模型，支持向量机利用核技巧把非线性问题转换成线性问题。

---

2006年，Hinton提出神经网络的Deep Learning算法。Deep Learning假设神经网络是多层的，首先用Restricted Boltzmann Machine（非监督学习）学习网络的结构，然后再通过Back Propagation（监督学习）学习网络的权值。

---

现在，deep learning的应用越来越广泛，甚至已经有超越SVM的趋势。一方面以Hinton，Lecun为首的深度学习派坚信其有效实用性，另一方面Vapnik等统计机器学习理论专家又坚持着理论阵地，怀疑deep learning的泛化界。

---

