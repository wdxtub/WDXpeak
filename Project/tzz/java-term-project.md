# CSC212 Term Project

## 描述

Graph 与 Graph Algorithm 的可视化

## 输入

1. GUI 选择文件
2. 命令行输入文件位置
3. 读入一个指定的 data file(和第二个其实一个意思) √

读入的过程大概就是：

1. 知道文件在哪里 √
2. 按照给定的规律读出来图的信息 √
3. 存成代码能看懂的格式(数组，链表之类的) √
    + ArrayList √
    + 邻接矩阵
    + Node √
    + Edge √
4. 显示出来一些东西证明真的读入进去了(老师懒，所以展示的部分要特别留意)

具体的data file要有趣一点，稍微复杂一点，才能体现出后面的算法，最好有实际的意义，让老师觉得wow。

## 输出

保存成差不多格式即可，也可以自己加点拓展，方便显示 √

## 算法

图算法无非以下几个：

1. 深搜
2. 广搜
3. Dij 最短路径

以上这三个是老师要求的，其实还有一些，比方说 bellman-ford, floyd-warshall, johnson

甚至还可以插一些其他的算法，例如最大流(ford-fulkerson)，最小生成树(prim)，就看有木有时间了，不过做了估计老师吓cry哈哈

有一些特定的要求，比方说能够修改一个点的连通性(修改邻接矩阵)，以及指定两个点，给出最短距离

## README

这个可能比代码还重要，老师估计是不会仔细看代码的

+ 做了啥
    + 概要介绍
+ 怎么做
    + 面对不同的实现方式选择，为什么要选现在用的这个
    + 具体的思考过程
+ 点出自己的extra work，妥妥有加分

## bfs & dfs test result

Neighbors of 苏州? [广州, 南京, 上海, 杭州, 济南]
Neighbors of 广州? [苏州, 长沙, 海口, 香港, 澳门, 南宁, 台北]
Neighbors of 北京? [石家庄, 天津, 沈阳, 呼和浩特, 太原, 银川, 长春, 哈尔滨]
Neighbors of 西安? [武汉, 太原, 郑州, 银川, 兰州, 重庆, 成都]
Neighbors of 成都? [西安, 西宁, 昆明, 重庆, 拉萨, 兰州]

bfs find path between Guangzhou(广州) and Beijing(北京)!
done<-Beijing(北京)<-Shijiazhuang(石家庄)<-Jinan(济南)<-Suzhou(苏州)<-Guangzhou(广州)

bfs find path between Guangzhou(广州) and Huhehaote(呼和浩特)!
done<-Huhehaote(呼和浩特)<-Taiyuan(太原)<-Zhengzhou(郑州)<-Jinan(济南)<-Suzhou(苏州)<-Guangzhou(广州)

bfs find path between Suzhou(苏州) and Xining(西宁)!
done<-Xining(西宁)<-Chengdu(成都)<-Xian(西安)<-Zhengzhou(郑州)<-Jinan(济南)<-Suzhou(苏州)

dfs find path between Guangzhou(广州) and Beijing(北京)!
->Guangzhou(广州)->Suzhou(苏州)->Hangzhou(杭州)->Fuzhou(福州)->Nanchang(南昌)->Changsha(长沙)->Guiyang(贵阳)->Kunming(昆明)->Chengdu(成都)->Chongqing(重庆)->Wuhan(武汉)->Hefei(合肥)->Jinan(济南)->Zhengzhou(郑州)->Xian(西安)->Taiyuan(太原)->Beijing(北京)

dfs find path between Guangzhou(广州) and Huhehaote(呼和浩特)!
->Guangzhou(广州)->Suzhou(苏州)->Hangzhou(杭州)->Fuzhou(福州)->Nanchang(南昌)->Changsha(长沙)->Guiyang(贵阳)->Kunming(昆明)->Chengdu(成都)->Chongqing(重庆)->Wuhan(武汉)->Hefei(合肥)->Jinan(济南)->Zhengzhou(郑州)->Xian(西安)->Taiyuan(太原)->Beijing(北京)->Huhehaote(呼和浩特)

dfs find path between Suzhou(苏州) and Xining(西宁)!
->Suzhou(苏州)->Guangzhou(广州)->Nanning(南宁)->Guiyang(贵阳)->Kunming(昆明)->Chengdu(成都)->Chongqing(重庆)->Wuhan(武汉)->Changsha(长沙)->Nanchang(南昌)->Fuzhou(福州)->Hangzhou(杭州)->Hefei(合肥)->Jinan(济南)->Zhengzhou(郑州)->Xian(西安)->Taiyuan(太原)->Beijing(北京)->Huhehaote(呼和浩特)->Yinchuan(银川)->Lanzhou(兰州)->Xining(西宁)
