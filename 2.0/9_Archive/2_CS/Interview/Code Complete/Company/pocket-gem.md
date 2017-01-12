# PocketGem

> 题目如下，给一个科技树

          a     e
        /   \  /
       b    c
        \   /
          d

写一个function print出需要研究的科技

example： 
    
    If c is completed, 
        then techpath(d) => [a, b, d]

难点有两个：

1. how to check cycle?
2. how to print the path in right order?

