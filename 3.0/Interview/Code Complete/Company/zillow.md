# Zillow

> 三维空间给定N个点的坐标(x, y, z)，找到N个点其中的一个点，使得其他点到这个点的距离总和最小。

解法：将所有点的坐标值加起来，求平均数，也就是求中心点，然后找N个点中离中心点最近的点。


> string to long : 输入的string是一个64bit的数字 输出为一个long。 

1. 若是有任何情况不能完整返回精确的原始数的话 要throw exception （例如overflow）
2. 输入的string中 出现任何不是数字或者+/-的字符 要throw exception (例如空格)

> 实现三叉树的 insert() 和 delete()函数 

left node 小于当前node, middle node等于当前node, right node 大于当前node. 

写法可以参照 https://gist.github.com/dydt/870393

