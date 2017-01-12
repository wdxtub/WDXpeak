# Hanoi Tower with Stack

出处

Solve the Hanoi Tower problem without recursion

## Solution

在面试中，比较普遍的一个技巧是从最基本的情况出发，根据题意推倒整个计算流程。这样做的好处是：1) 确保自己正确地理解了题目 2) 从简单的情况出发，找找解题思路。该方法特别适用于递归，动态编程等题目类型。在这里就可以尝试一下：

1) 假设有1个盘子

直接把盘子从left移动到right，需要1步完成。

2) 假设有2个盘子

+ 将盘子1从left移动到middle
+ 将盘子2从left移动到right
+ 将盘子1从middle移动到right

可以发现，这里我们解了一个子问题：把n-1个盘子移动到middle，然后把第n个盘子移动到left，最后把n-1个盘子从middle移动到left。这里限于篇幅不列举三个盘子的情况，但强烈建议你根据上面子问题的描述方式重现三个盘子的情况。

根据上述分析，汉诺塔(Hanoi Tower)的游戏过程是一个自上而下结构：从顶层(移动n个盘子)出发，逐渐向下(移动n-1个盘子)扩散。实际计算时，我们先解决子问题(移动n-1个盘子到middle)，再利用子问题的结果解决当前问题(移动最后一个盘子到right，移动n-1个盘子到right)。

如果用栈作为辅助结构消除递归，由于子问题是“从A柱通过B柱移动n个盘子到C柱”，所以我们可以构造含有source、midpoint、destination及盘子个数信息的object，并把它加入栈中。每次弹出时，需要解决当前问题，即把“从A柱通过C柱移动n-1个盘子到B柱”，然后“从A移动1个盘子到C”，最后“从B柱通过A柱移动n-1个盘子到C柱”。注意栈的LIFO特性，我们需要的出栈顺序如上所述，实际入栈顺序与之相反。

## Complexity

可以用数学归纳法证明复杂度为O(2^n - 1)：

1) 1个盘子的时候需要2^1 – 1步

2) 根据1)，我们知道移动n-1 个盘子需要`2^(n - 1) - 1`步。而移动n个盘子需要做：把n-1个盘子移动到middle，然后把第n个盘子移动到left“。即`2 * (2^(n - 1) - 1) + 1 = 2^n – 1`。

3) 由数学归纳法可知，对于任意n，完成Hanoi Tower需要2^n – 1步。

## Code

```java
enum Tower { Zero, Left, Mid, Right };

class HanoiObj {
    public Tower src, tmp, dest;
    public int num, index;
    public HanoiObj(Tower s, Tower t, Tower d, int n) : src(s), tmp(t), dest(d), num(n) {
        if (n == 1) {
            index = 1;
        }
    }
    public HanoiObj(Tower s, Tower d, int i) : src(s), dest(d), index(i) {
        num = 1; tmp = Zero;
    }
}

void move(Tower src, Tower dest, int index) {
	System.out.println("Move Disk #" + index + " from Tower " + src + " to Tower " + dest);
}

void TOH(int N) {
    Stack<HanoiObj> Hstack;
    Tower s, t, d;
    int n;
    Hstack.push(new HanoiObj(Left, Mid, Right, N));
    while (!Hstack.empty()) {
        HanoiObj tmpObj = Hstack.top();
        Hstack.pop();
        s = tmpObj.src;
        t = tmpObj.tmp;
        d = tmpObj.dest;
        n = tmpObj.num;
        if (n < 1) {
            continue;
        }
        if (n == 1) {
            move(s, d, tmpObj.index);
        } else {
				// because Stack is LIFO, the push sequence is symmetric to the way we expect it to pop
            Hstack.push(new HanoiObj(t, s, d, n - 1));
            Hstack.push(new HanoiObj(s, d, n)); // basically, equivalent to calling move function
            Hstack.push(new HanoiObj(s, d, t, n - 1));
        }
    }
}
```

