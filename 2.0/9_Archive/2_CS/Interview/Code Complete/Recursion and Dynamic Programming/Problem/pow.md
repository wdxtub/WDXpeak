# Pow(x, n)

出处

Implement pow(x, n)

## Solution

由于pow(x, n)相当于n个x相乘，左半边乘积与右半边相互独立且类似，所以可以用D&C策略进行二分。注意，二分之后需要处理n大于0，等于0，小于0等情况。

## Complexity

时间复杂度 O(n), 空间复杂度 O(logn)

## Code 

```java
double pow(double x, int n) {      
    if (n == 0)
        return 1.0;
    if (x == 0)
        return 0.0;
    double half = pow(x,n/2);
    if(n%2 == 0)
        return half*half;
    else if(n > 0)
        return half*half*x;
    else
        return half*half/x;
}
```


