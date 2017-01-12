# Sqrt(x)

出处

Implement sqrt(x), which returns the square root of value x.

## Solution

解题分析：首先我们需要明确开根号的性质：

1. 负数无效
2. 若x为0，则返回0
3. 若x属于(0,1)，则sqrt(x)属于(x,1)
4. 若x为1，则返回1
5. 若x大于1，则sqrt(x)属于(1,x)

此外，若x > y，则sqrt(x) > sqrt(y)。情况1，2，4可以作为特例，而对于通常情况(情况3，情况5)，我们发现如下两个特性：

1. 解落在已知区间
2. 存在相对大小关系

进一步地，我们可以将sqrt(x)的所有“候选数”看成是分布在有限区间上的有序数列，对于每个元素，我们通过平方操作比较与待搜索数x的相对大小关系。很明显，这就是二分查找的思想。

## Complexity

由于我们利用了二分查找的思想，故复杂度为O(log(x/precision))

## Code

```java
double mySqrtHelper(double x, double lowBound, double highBound) {
    double precision = 0.00001;
    double sqrt = lowBound / 2 + highBound / 2;
    if (Math.abs(sqrt * sqrt - x) <  precision) {
        return sqrt;
    } else if (sqrt * sqrt - x > 0) {
        return mySqrtHelper(x, lowBound, sqrt);
    } else {
        return mySqrtHelper(x, sqrt, highBound);
    }
}

double mySqrt(double x) {
    if (x < 0)
        return ERROR;
    if (x == 0) {
        return 0;
    }

    if (x == 1) {
        return 1;
    }

    if (x < 1) {
        return mySqrtHelper(x, x, 1);
    } else {
        return mySqrtHelper(x, 1, x);
    }
}
```

