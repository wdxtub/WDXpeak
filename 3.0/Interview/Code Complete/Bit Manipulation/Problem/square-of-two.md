# Square of Two

出处

Explain what the following code does: ( n & (n-1) ) == 0

## Solution

之前我们看到n &= (n-1) 相当于clear最低的一位1，我们用这个方法统计一个整数的二进制表示中有多少个1。那么( n & (n-1) ) = 0意味着该整数的二进制表示中只有一个1，即它是2的次方。事实上，如果不能立刻看出结果，不妨尝试从1开始列举n的值，看看有什么规律。根据观察到的结果再来倒推表达式的含义。

## Complexity

时间复杂是 O(1)

## Code 

不需要代码，理解题

