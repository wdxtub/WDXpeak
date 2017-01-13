# A Plus B

出处

给出两个整数a和b, 求他们的和, 但不能使用 + 等数学运算符

样例

    如果 a=1 并且 b=2，返回3

注意

    你不需要从输入流读入数据，只需要根据aplusb的两个参数a和b，计算他们的和并返回就行。

挑战

    显然你可以直接 return a + b，但是你是否可以挑战一下不这样做？

说明

    a和b都是 32位 整数么？是的
    我可以使用位运算符么？当然可以

## Solution

位运算实现整数加法本质就是用二进制进行运算。
其主要用了两个基本表达式：

+ `x^y` //执行加法，不考虑进位。
+ `(x&y)<<1` //进位操作

令 `x=x^y; y=(x&y)<<1` 进行迭代，每迭代一次进位操作右面就多一位 0，最多需要“加数二进制位长度”次迭代就没有进位了，此时`x^y`的值就是结果。

我们来做个3位数的加法：

101+011=1000 //正常加法

位运算加法：

    （1） 101 ^ 011 = 110
    (101 & 011)<<1 = 010
    （2） 110 ^ 010 = 100
    (110 & 010)<<1 = 100
    （3） 100 ^ 100 = 000
    (100 & 100)<<1 = 1000

此时进行相加操作就没有进位了，即000 ^ 1000=1000即是最后结果。

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
class Solution {
    /*
     * param a: The first integer
     * param b: The second integer
     * return: The sum of a and b
     */
    public int aplusb(int a, int b) {
        // write your code here, try to do it without arithmetic operators.
        while(b != 0){
            int carry = a & b;
            a = a ^ b;
            b = carry << 1;
        }
        return a;
    }
};

```

