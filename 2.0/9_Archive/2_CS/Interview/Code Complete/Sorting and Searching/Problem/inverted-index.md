# Inverted Index

出处

A library is trying to build up a smart computer-aided look up system: user may input a list of key words, and the system shall provide all books that “contain these words. How to implement such query? (A library may have millions of books)

## Solution

对于文章中单词的检索，一般采用倒排索引(Inverted index) ，其本质就是单词到文档集合的一个哈希，例如：

    apple -> doc 1, doc 2
    banana -> doc 2

对于文档集合，可以进一步利用各种集合操作，例如交集，并集等，获得对应的结果。如果题目中书本数目不大，并且出现的单词总个数不多，那么可以直接将倒排索引建立在一部机器上。在查询时，对于用户给定的每个单词，通过哈希表查找出对应的文档集合，最后对所有集合求交集，即可实现查询功能。但是，当文档／单词量巨大时，如何实现可扩展性？我们需要以一定的规律将哈希表分配到多台机器上，即完成对哈希表的拆分和分块存储。例如，machine1可以负责首字母为a的所有单词，machine2可以负责首字母为b的单词，以此类推。事实上，这个过程相当于引入另一层hash进行数据分流：建立对象与存储该对象的机器之间的映射。

## Complexity

设计题

## Code 

设计题

