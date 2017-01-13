# 3D打印

## 在哪里能够学习到3d打印技术？

专业学术类：

1. [Understanding Additive Manufacturing: Rapid Prototyping, Rapid Tooling, Rapid Manufacturing, by Andreas Gebhardt](http://www.goodreads.com/book/show/16650939-understanding-additive-manufacturing) (这本是我看的第一本3D打印书籍，讲得很浅，很广，是一本不错的入门书）
2. [Additive Manufacturing Technologies: Rapid Prototyping to Direct Digital Manufacturing, by Ian Gibson, David W. Rosen, Brent Stucker](http://www.goodreads.com/book/show/9197092-additive-manufacturing-technologies)
3. [Rapid Manufacturing: An Industrial Revolution in the Digital Age, by Neil Hopkinson](http://www.goodreads.com/book/show/1051630.Rapid_Manufacturing) (以上两本都没看过，据说是不错的大学教材）
4. [Solid Freeform Frabrication Symposium Preceedings](http://utwired.engr.utexas.edu/lff/symposium/proceedingsArchive/toc.cfm) (这里可以找到每年一次的Solid Freeform Frabrication Symposium学术会议上发表的文章。从1990年到2012年，今年的会议还未开。看前面几本入门后，再来认真研究这些文章，根据文章引用再挖掘一下。这样应该可以对3D打印学术界的发展有个比较深入的了解）

DIY发烧友类：

畅销书类（讲大方向大趋势的那种）

1. [3D Printing: The Next Technology Gold Rush, by Christopher D. Winnan](http://www.goodreads.com/book/show/17279154-3d-printing)（这是前几个月才出版的新书，我大概浏览了一下。如果想了解专业或者工业3D打印机的话，Understanding Additive Manufacturing应该会更好，讲得也比较系统化，有逻辑。而这本毕竟是畅销书类型的，比较有趣，好看，但是话有点多）
2. [Makers: The New Industrial Revolution, by Chris Anderson](http://www.goodreads.com/book/show/13414678-makers)（这大概与3D打印有关的书里头是最出名的一本了，《长尾理论》作者Chris Anderson于2012年出版的新书，有中文版：[创客 (豆瓣) ](http://book.douban.com/subject/20365163/)这本书讲的不仅仅是3D打印，而是创客运动。3D打印是创客运动中的一辆重型战车，但不是唯一一辆。我受这本书启发不少，认真读能挖掘出不少其他有趣的技术，比如数控机床、激光蚀刻机、物联网、众包等等。Chris Anderson很会鼓动人心，看这本书的时候我感到热血沸腾。不过后来冷静分析，感觉某些地方还是吹得有点过了。）
3. [Fabricated: The New World of 3D Printing by Hod Lipson ](http://www.goodreads.com/book/show/17134932-fabricated)
4. [The Homebrew Industrial Revolution by Kevin A. Carson ](http://www.goodreads.com/book/show/8709638-the-homebrew-industrial-revolution)（以上两本没有看过，不过都是蛮有名的著作）

---

3D打印让传统制造瞬间过时，规模经济的铁律从此被打破制造业和商业模式发生巨大变革，知识产权将彻底失效

3D（Three Dimensions）打印是一种通过材料逐层添加制造三维物体的变革性、数字化增材制造技术，它将信息、材料、生物、控制等技术融合渗透，将对未来制造业生产模式与人类生活方式产生重要影响。

3D打印过程如下：3D打印机在设计文件指令的导引下，先喷出固体粉末或熔融的液态材料，使其固化为一个特殊的平面薄层。第一层固化后，3D打印机打印头返回，在第一层外部形成另一薄层。第二层固化后，打印头再次返回，并在第二层外部形成另一薄层。如此往复，最终薄层累积成为三维物体。

尽管具有这些优势，3D打印制造业并不具有规模经济。像任何极端的个性特征一样，事实上，3D打印未能提供规模经济是其最大的弱点，但同时也是其最大的优势。对于一个靠大生产规模获取边际利润的企业来说，达到规模经济非常重要。然而，如果一家企业的商业模式是销售少量独特的、不断变化的或者定制的、具有高边际收益的产品，那么3D打印产品（像鸭嘴兽）代表了革命性的飞跃。

向人们介绍3D打印时，我经常会说3D打印有两大家族，第一个家族通过沉积原材料层制造物体，第二个家族通过黏合原材料制造物体。

设计文件必须可以和3D打印机的内置软件准确交流，打印机的内置软件（或固件）会告诉其机械组件如何操作。为3D打印准备一个完整的设计文件并不是一项简单的工作。

3D打印过程中经常出现的挑战是需要弥补大多数设计软件在开发时并未考虑到3D打印所带来的问题，设计文件以各种令人眼花缭乱的文件格式发送过来，各具问题和挑战。

在设计文件转换为STL格式后，STL将设计对象的数字形状“包装”在虚拟的表面之内，我们称之为“网格”，其由成千上万（有时数百万）个连锁多边形组成。表面网格上的每个连锁多边形（常用的是三角形）都携带着物体的形状信息。在设计文件转换中，全部的设计表面包括物体可以接触到空气的任何部分，不是工程师的人可能会对此感到些许困惑。例如，一个物体的表面设计既包括物体的外表面，也包括其空心处的内表面。当STL转换完成，新包装的STL文件的虚拟表面必须是防水的，这有点儿类似于给物体涂上一层防水密封剂。一个防水的STL文件的表面网格可以精确而完整地覆盖和捕捉到设计表面的曲线和内部镂空。就像在密封防水麂皮鞋上的孔洞或缝隙一样，STL文件表面网格的缝隙将会在后续过程中引起问题。

一旦STL准备就绪，连接CAD和CAM的桥梁已经基本完成。即将进行3D打印的物体在完成表面防水网格包装后，还要为其最终阶段做准备：分层制造过程。在此STL文件将完成它的最后一部分工作，打印机固件读取STL文件，将数字网格“切”为虚拟的薄层，这对应着将来3D打印的物理薄层。 STL文件每个虚拟切片都反映着最终打印物体的一个横截面。还记得沿着咖啡杯底描出轮廓吗？该轮廓就等于STL文件中的一个单独的“薄片”的轮廓，也对应着一个单独的3D打印层。轮廓跟踪完成后，打印机需要进行光栅前后扫描以填满内部轮廓，就像填满着色薄中的所有形状。
