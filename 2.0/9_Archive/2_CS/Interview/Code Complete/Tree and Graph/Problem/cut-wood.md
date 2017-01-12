# Cut Wood

有一些原木，现在想把这些木头切割成一些长度相同的小段木头，需要得到的小段的数目至少为 k。当然，我们希望得到的小段越长越好，你需要计算能够得到的小段木头的最大长度。

样例

    有3根木头[232, 124, 456], k=7, 最大长度为114.

注意

    木头长度的单位是厘米。原木的长度都是正整数，我们要求切割得到的小段木头的长度也要求是整数。无法切出要求至少 k 段的,则返回 0 即可。

挑战

    O(n log Len), Len为 n 段原木中最大的长度

## Solution

这道题要直接想到二分搜素其实不容易，但是看到题中 Challenge 的提示后你大概就能想到往二分搜索上靠了。首先来分析下题意，题目意思是说给出 n 段木材L[i], 将这 n 段木材切分为至少 k 段，这 k 段等长，求能从 n 段原材料中获得的最长单段木材长度。以 k=7 为例，要将 L 中的原材料分为7段，能得到的最大单段长度为114, 232/114 = 2, 124/114 = 1, 456/114 = 4, 2 + 1 + 4 = 7.

理清题意后我们就来想想如何用算法的形式表示出来，显然在计算如2, 1, 4等分片数时我们进行了取整运算，在计算机中则可以使用下式表示：

$\sum_{i=1}^{n}\frac{L[i]}{l} \le k$

其中 l 为单段最大长度，显然有 1 ≤ l ≤ max(L[i]). 单段长度最小为1，最大不可能超过给定原材料中的最大木材长度。

注意求和与取整的顺序，是先求 L[i]/l的单个值，而不是先对L[i]求和。

分析到这里就和题 Sqrt x 差不多一样了，要求的是 l 的最大可能取值，同时
l 可以看做是从有序序列[1, max(L[i])]的一个元素，典型的二分搜索！

## Complexity

时间复杂度 O(logn)，空间复杂度 O(1)

## Code

```java
public class Solution {
    /**
     *@param L: Given n pieces of wood with length L[i]
     *@param k: An integer
     *return: The maximum length of the small pieces.
     */
    public int woodCut(int[] L, int k) {
        if(L == null || L.length == 0) return 0;
        if(L.length == 1){
            return L[0] / (L[0] / k);
        }
        Arrays.sort(L);
        int start = 1, end = L[L.length - 1];
        int max = 0;
        while(start <= end){
            int mid = (end - start) / 2 + start;
            int count = 0;
            for(int l : L){
                count += (l / mid);
            }
            if(count < k){
                end = mid-1;
            } else{
                start = mid+1;
                max = mid;
            }
        }
        return max;
    }
}
``` 

