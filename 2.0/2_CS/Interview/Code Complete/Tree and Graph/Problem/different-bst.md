# Different BST

给出 n，问由 1...n 为节点组成的不同的二叉查找树有多少种？

样例

    给出n = 3，有5种不同形态的二叉查找树：
    1           3    3       2      1
     \         /    /       / \      \
      3      2     1       1   3      2
     /      /       \                  \
    2     1          2                  3

## 题解

The case for 3 elements example

    Count[3] = Count[0]*Count[2]  (1 as root)
               + Count[1]*Count[1]  (2 as root)
               + Count[2]*Count[0]  (3 as root)

Therefore, we can get the equation:

    count[n] = sum(count[0..k]*count[k+1...n]) 0 <= k < n-1

## Complexity

时间复杂度 O(n^2 )，空间复杂度 O(n)

## Code

```java
public class Solution {
    /**
     * @paramn n: An integer
     * @return: An integer
     */
    public int numTrees(int n) {
        int[] count = new int[n+2];
        count[0] = 1;
        count[1] = 1;

        for(int i=2;  i<= n; i++){
            for(int j=0; j<i; j++){
                count[i] += count[j] * count[i - j - 1];
            }
        }
        return count[n];
    }
}

```

