# 凸优化教程

## 思考凸集和凸函数

![co1](./_resources/co1.jpg)

## 凸集

集合 C 内任意两点间的线段均在集合 C 内，则称集合 C 为凸集

![co2](./_resources/co2.jpg)

**一些例子**

![co3](./_resources/co3.jpg)

## 超平面和半空间

![co4](./_resources/co4.jpg)

## 多面体

![co5](./_resources/co5.jpg)

一个例子

![co6](./_resources/co6.jpg)

## 保持凸性的运算

![co7](./_resources/co7.jpg)

**集合交运算：半空间的交**

![co8](./_resources/co8.jpg)

**仿射变换**

![co9](./_resources/co9.jpg)

**透视变换**

![co10](./_resources/co10.jpg)

凸集的透视变换仍然是凸集

**投射函数(线性分式函数)**

![co11](./_resources/co11.jpg)

Ax+b - 仿射函数

## 分割超平面

![co12](./_resources/co12.jpg)

一个例子

![co13](./_resources/co13.jpg)

**分割超平面的构造**

![co14](./_resources/co14.jpg)

## 支撑超平面

![co15](./_resources/co15.jpg)

**思考**

![co16](./_resources/co16.jpg)

## 凸函数

![co17](./_resources/co17.jpg)

### 一阶可微

![co18](./_resources/co18.jpg)

即函数的增长(下降)速度要快于(慢于)以当前点的梯度为方向的直线。

**进一步思考**

![co19](./_resources/co19.jpg)

### 二阶可微

![co20](./_resources/co20.jpg)

**凸函数举例**

![co21](./_resources/co21.jpg)

## 上境图 epigraph

![co22](./_resources/co22.jpg)

一个函数是凸函数，当且仅当其上境图是凸集(可以根据定义证明)

进一步，一个函数是凹函数，当且仅当其亚图(hypograph)是凸集

![co23](./_resources/co23.jpg)

## Jensen 不等式

**若 f 是凸函数**

![co24](./_resources/co24.jpg)

**Jensen 不等式几乎是所有不等式的基础**

![co25](./_resources/co25.jpg)

## 保持函数凸性的算子

![co26](./_resources/co26.jpg)

### 凸函数的逐点最大值

![co27](./_resources/co27.jpg)

凸函数的逐点最大值仍然是凸函数

![co28](./_resources/co28.jpg)

## 凸优化

优化问题的基本形式

![co29](./_resources/co29.jpg)

![co30](./_resources/co30.jpg)

inf-下确界 sup-上确界

## 凸优化问题的基本形式

![co31](./_resources/co31.jpg)

要求还是比较严格的

## 对偶问题

![co32](./_resources/co32.jpg)

## Lagrange 对偶函数(dual function)

![co33](./_resources/co33.jpg)

通过 Lagrange 方法我们可以把一个一般的优化问题转换成凸优化问题

左侧为原函数，右侧为对偶函数

![co34](./_resources/co34.jpg)

左侧的虚线函数是约束条件

## 鞍点解释

![co35](./_resources/co35.jpg)

不可行即不满足约束条件 fi(x) <= 0

## 鞍点：最优点

![co36](./_resources/co36.jpg)

![co37](./_resources/co37.jpg)

## 例子：线性方程的最小二乘问题

![co38](./_resources/co38.jpg)

![co39](./_resources/co39.jpg)

先对 x 求偏导，令其为 0，得到 x 和 v 的关系，然后把用 v 来表示的 `x*` 带入 L 中，即得到 g，也就是对偶函数。

![co40](./_resources/co40.jpg)

然后再求对偶函数的极大值，g 关于 v 求导数，令其为零，求得 v，然后把 v 的表达式代入 `x*`，就得到了最优解

![co41](./_resources/co41.jpg)

## 强对偶条件

![co42](./_resources/co42.jpg)

这里 hi(x) = 0, fi(x) <= 0

为了取等号，fi(x) 和 hi(x) 都需要等于 0

![co43](./_resources/co43.jpg)

