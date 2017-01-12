# H-Index

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.

Hint:

1. An easy approach is to sort the array first.
2. What are the possible values of h-index?
3. A faster approach is to use extra space.

## Solution

可以按照如下方法确定某人的H指数：1、将其发表的所有SCI论文按被引次数从高到低排序；2、从前往后查找排序后的列表，直到某篇论文的序号大于该论文被引次数。所得序号减一即为H指数。

方法一：

O(nlogn)时间，O(1)空间。现将数组排序。然后从大到小遍历，一边计数一边比较计数与当前的引用数，直到计数大于引用数。

```java
public class Solution {
    public int hIndex(int[] citations) {
        int len = citations.length;
        Arrays.sort(citations);
        int result = 0;
        for (int i = citations.length - 1; i >= 0; i--) {
            if (result >= citations[i]) {
                return result;
            }
            result++;
        }
         
        return result;
    }
}
```


方法二；

O(n)时间，O(n)空间。
使用一个额外的数组，其下标为引用数，置为为具有该引用数的文章数量。注意，根据定义，H-index的上限不可能超过文章总数n。因此我们只需要额外开一个长度为n的数组即可。然后对新数组按引用数从大到小遍历，一边计数一边比较计数与当前的引用数，直到计数大于引用数。

```java
public class Solution {
    public int hIndex(int[] citations) {
        int len = citations.length;
        if(citations == null || len == 0) return 0;
        int[] counts = new int[len + 1];
        for(int c : citations){
            if(c > len) counts[len]++;
            else counts[c]++;
        }
        if(counts[len] >= len) return len;
        for(int i = len - 1; i >= 0; i--){
            counts[i] += counts[i + 1];
            if(counts[i] >= i) return i;
        }
        return 0;
    }
}
```

