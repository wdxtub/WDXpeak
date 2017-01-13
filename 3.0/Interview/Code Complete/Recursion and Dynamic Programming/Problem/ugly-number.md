# Ugly Number

出处

设计一个算法，找出只含素因子3，5，7 的第 k 大的数。

符合条件的数如：3，5，7，9，15......

样例

    如果k=4， 返回 9

挑战

    要求时间复杂度为O(nlogn)或者O(n)
    
## Solution

DP method O(k)

假设数组ugly[N]中存放不断产生的丑数，初始只有一个丑数ugly[0]=1，由此出发，下一个丑数由因子2,3,5竞争产生，得到`ugly[0]*2`, `ugly[0]*3`, `ugly[0]*5`， 显然最小的那个数是新的丑数，所以第2个丑数为ugly[1]=2，开始新一轮的竞争，由于上一轮竞争中，因子2获胜，这时因子2应该乘以ugly[1]才显得公平，得到`ugly[1]*2`,`ugly[0]*3`,`ugly[0]*5`， 因子3获胜，ugly[2]=3，同理，下次竞争时因子3应该乘以ugly[1]，即：`ugly[1]*2`, `ugly[1]*3` `ugly[0]*5`, 因子5获胜，得到ugly[3]=5，重复这个过程，直到第n个丑数产生。总之：每次竞争中有一个（也可能是两个）因子胜出，下一次竞争中胜出的因子就应该加大惩罚！

注意这里不可以使用if/else 循环，因为有可能多于一个指针的结果是相等的：例如p3->5, p5->3, 他们的结果相等，这是两个指针都要+1

indexFor3 指的是上次乘完 3 之后需要加的惩罚。

## Complexity

时间复杂度 O(n)，空间复杂度 O(n)

## Code

```java
class Solution {
    /**
     * @param k: The number k.
     * @return: The kth prime number as description.
     */
    public long kthPrimeNumber(int k) {
        long[] uglyNumbers = new long[k + 1];
        int indexFor3 = 0, indexFor5 = 0, indexFor7 = 0; //multiplier index
        uglyNumbers[0] = 1;
        for (int i = 1; i <= k; i++) {
            uglyNumbers[i] = Math.min(Math.min(3 * uglyNumbers[indexFor3], 5 * uglyNumbers[indexFor5]), 7 * uglyNumbers[indexFor7]);
            if (uglyNumbers[i] == 3 * uglyNumbers[indexFor3]) {
                indexFor3++;
            }
            if (uglyNumbers[i] == 5 * uglyNumbers[indexFor5]) {
                indexFor5++;
            }
            if (uglyNumbers[i] == 7 * uglyNumbers[indexFor7]) {
                indexFor7++;
            }
        }
        return uglyNumbers[k];
    }
};
```


