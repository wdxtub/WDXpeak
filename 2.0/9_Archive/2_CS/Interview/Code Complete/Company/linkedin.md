# Linkedin

> search similar people的API

大致说一下前端，后端，不用太细

> 给一排房子，用RGB三种颜色染色，相邻不能染成同色，每个房子染对应颜色会有对应的weight（W[N][3]），求最大的weight和

follow up，N种颜色

> nested array，etc [[1,2], 2, [[3], [4]]]，input是nested array的iterator，实现next element的iterator

版上高频 


> design，tiny url 

高频


> 比较长  

    /**
     * Find threevalues that can be the lengths of the sides of a triangle.
     * Three segmentsof lengths A, B, C can form a triangle if and only if:
     *
     *      A + B > C
     *      B + C > A
     *      A + C > B
     *
     * e.g.
     *  6, 4, 5 can form a triangle
     * 10, 2, 7 can't
     *
     * @paramsegmentLengths the lengths of segments that might form a triangle.
     * @return threevalues that can be the lengths of the sides of a triangle,
     *         or an empty array if there are no suchvalues in segmentLengths.
     * sample input:segmentLengths = [10, 5, 7, 4, 3]
     */
     
第一反应brute force 因为没见过 同时手极快的google了 然后google到了这个（没权限发链接 大家自行google geeksforgeeks/find-number-of-triangles-possible）

但是面试官不要求count 有多少个triangle 只要return 一组 就行了 此题的重点是要sort 好像背后还有什么数学原因

我当时就扫了遍帖子 说要sort 然后后面写了个iteration match 第一组符合的pair


> Find the size of longest palindrome subset of an array

高频

注意是subset而不是subarray。不能改变order。所以[1, 2, 2, 0, 1]的longest palindrome subset是[1, 2, 2, 1]，应该返回4。

> 检查两个bst是否identical

TODO


> Deepest comman ancestor (with parent nodes).

LinkedIn这题都快问烂了...我说了用hashmap的方法，他说你能不能不用额外空间，我想了一下又说了那个把两个节点调到一个高度的做法。

对就是每个node除了left和right还有个parent

Class Node {
       Node left;
       Node right;
       Node parent;
}
root节点parent是null. 没有parent的做法的确是递归，但是有parent指针的话递归就划不来了。举个例子：

        ____3___
       /        \
      5          1
    /    \     /    \
    6     2   0      8
         / \
        7   4

要找4 和 8的lca，把4先设成到2，因为2 和 8 深度一样。然后2 和 8 一起沿着parent往上，碰到的第一个一样的节点就是第一个祖先了。

> 实现一个Max Stack， 支持peekMax() 和popMax().

很自然地用两个栈去做，但是这样popMax的时候很费时间。然后我又加了一个stack存的是max value的index, 把stack全变成ArrayList, 然后就开始纠结pop了。。。结果corner case太多没写完。。。不过他也说这题要简单clean是比较难



> linked list找intersection~本来窃以为不要太简单~没想到他居然无数个follow-up

分情况讨论：

+ 两个没有环，不想交
+ 两个没有环，相交
+ 两个有环，不想交
+ 两个有环，相交

在第三种情况纠结了很久，然后决定上slow, fast pointer找到两个环的起点，然后固定一个起点，另外一个环走一圈看有没有重复
之后又扯淡了很久~

> 就是面经里的那道nestedInteger, 只不过我的题目是个变形. 当时要求多加一层就是求得是ReverseDepthSum. 也就是层数越深，所获得的weight value越低.

举例就是 `{{1,1},2,{1,1}}` the function should return 8 (four 1's at weight 1, one 2 at depth 2)

Given the list {1,{4,{6}}} the function should return 17 (one 1 at weight 3, one 4 at depth 2, and one 6 at depth 1).先得走通一遍得到层数，然后对应上乘出来才可以得到结果.

> 面经里的Add Interval那题

其实L家如果准备很充分还是很有帮助的. 跟原题一样，不过后来又继续followup如何remove Interval.

> 给定一个中心点，然后找到K个nearest points.　

这个当时我复习电面的时候看过下，
但是后来就一直没管了，就记得用priority_queue来做就好了，结果被问到了minHeap和maxHeap,在这两个概念上纠结了很久，

