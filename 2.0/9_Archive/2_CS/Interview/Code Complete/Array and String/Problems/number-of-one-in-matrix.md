# 二进制矩阵中 1 的个数

> 给定 n*n 的 01 方阵，每一行都是降序的(即先连续的一段 1，再连续的一段 0)，求 1 最多的那行中 1 的个数

分析

+ 算法 1：输出每一行的 1。O(n^2)
+ 算法 2：二分除每一行 0 和 1 的分界线。O(nlogn)
+ 算法 3：如果某个位置是 1，则向右，是 0 则向下(只有找到比本行更多的 1 才有意义)

时间 O(n)

```
int run(vector<vector<char>> &a){
    int n = a.size();
    int best = 0;
    for (int i = 0; (best < n) && (i < n); i++){
        while ((best < n) && (a[i][best] == '1')){
            best++;
        }
    }
    return best;
}
```

