+ 3月2日截止，这之前做各种各样的测试
+ 100% sure what your project is about
+ 仔细研读那三篇论文（了解术语和上下文）
+ meeting once a week
+ Da: Preprocessing, rendering, segmentation
+ Yuan: PCA
+ 主要用 Matlab来写
+ 要做一个 app 用来获取数据
+ why is it useful, biomedical
+ early detection diagnosing ADD before 1-2 years
+ universal tool to capture videos.
+ ask questions and record people’s reaction
+ facial cues
+ AU6 + AU12, 不同表情是不同 AU 的组合，Action Unit
+ 若干 database, Facegen modeller
+ 精确 segmentation 以找到追踪点，用 nearest neighbor 来决定不同帧之间的相关性

![](_resources/jan_20_meeting.jpg)

+ how to track the points
+ global movement, not the shape(Elliptic Fourier Descriptor)
+ come up with a new product
+ face expression analysis
+ PCA （非监督）
+ LDA（监督） 这两个都可以用于机器学习
+ 看看其他用于学习的算法

具体的流程

移动设备的一个 APP 拍摄一段视频->针对某个表情，选出10帧subsample->对这10帧进行预处理，找出五官边缘->对于这五官边缘来进行处理计算，找到兴趣点->resample这些兴趣点（逐帧数量不同）为同一数量->进行具体的计算分析

目前状况

现在有两个程序可以运行，其中一个基本满足条件，另一个是PCA LDA 相关，也可以看看，去了解
