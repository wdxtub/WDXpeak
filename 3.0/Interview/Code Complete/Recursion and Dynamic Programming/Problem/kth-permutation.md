# Kth Permuation

给定 n 和 k，求123..n组成的排列中的第 k 个排列。

样例

    对于 n = 3, 所有的排列如下：
    123
    132
    213
    231
    312
    321
    如果 k = 4, 第4个排列为，231.

注意

    1 ≤ n ≤ 9

## Solution

基本的想法是，对于第k个排列，{a1, a2, a3, ..., an}, a1 是多少呢？

因为{a2, a3, ..., an} 一共有 (n-1)!种，a1在num中的index相当于 k / (n-1)!。换句话解释，就是一共有n个block，每个block大小是(n-1)!这么大，现在要求的就是在哪个block。

同理，求a2的时候，a1（在哪个block）已经求出来了，update k = k % (n-1)!, block的大小变成了(n-2)!, 这又是一个子问题了。

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
class Solution {
    /**
      * @param n: n
      * @param k: the kth permutation
      * @return: return the k-th permutation
      */
    public String getPermutation(int n, int k) {
        int[] num = new int[n];
        int perNumCount = 1;

        for(int i = 0; i < n; i++) {
            num[i] = i+1;
            perNumCount *= i + 1;
        }
        k--;
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < n; i++) {
            perNumCount = perNumCount / (n - i);
            int choosed = k / perNumCount;
            sb.append(String.valueOf(num[choosed]));
            for(int j = choosed; j < n - i - 1; j++) {
                num[j] = num[j+1]; 
            }
            k = k % perNumCount;
        }
        return sb.toString();
    }
}
```

