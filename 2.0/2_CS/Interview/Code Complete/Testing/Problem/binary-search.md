# Binary Search

出处

How do you test your implementation for `int binary_search(vector<int> array, int value)`, which returns index of the value in array or -1 if not found?

## Solution 

本题属于“测试现实世界的一个函数”

(1) Normal cases

对于函数或软件的测试，通常采用脚本测试的方法。特别地， 对于比较常见的函数功能，例如本题的binary search，可以尝试寻找开源的函数与自己的实现进行比较。或者实现一个简单的线性搜索，比较查询结果是否一致。有了验证结果的方法，则可以编写脚本生成随机数据，同时运行需要测试的函数以及对照函数，比较运行结果是否相同。正常测试情况包括从数组中找出某个数据，以及测试数组中不存在该数据的情况。

(2) Extreme cases

极端情况包括输入数组为空，或输入数组很大的情况。

(3) Invalid case

需要考虑数组中含有重复元素是否是有效的情况。二叉搜索在这样的情况下返回的元素下标不一定是该元素第一次出现的下标。

