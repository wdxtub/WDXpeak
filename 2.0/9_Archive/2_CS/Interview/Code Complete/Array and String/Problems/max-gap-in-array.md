# 最大间隔问题

> 给定数组 a，求下标对 i, j 满足 a[i] <= a[j]，并且 j - i 最大

分析

+ 假设目前最优解是 d，对于 j，至少要检查 i = j - d - 1 才可能最优
+ 记录前缀最小值 p[x] = min{p[0..x]}
+ 倒着循环 j，对于每个 j 看一下 p[j-d-1] 是否 <= a[j]，用 p 引导，这里指的是通过 p 可以知道在这个 i 之前还有没有比 a[j] 更小的
+ 如果前面都比 a[j] 大，则这个 j 得不到更优的解

时间 O(n) 因为内层循环的值(best)始终在增大，一共循环了 n 次。

```
int run(vector<int> &a){
    int n = a.size();
    vector<int> p(n);
    for (int i = 0; i < n; i++){
        p[i] = ((i == 0) || (a[i] < p[i - 1])) ? a[i] : p[i - 1];
    }
    int best = 0;
    for (int j = n - 1; j > best; j--){
        while ((j > best) && (a[j] >= p[j - best - 1])){
            ++ best;
        }
    }
    return best;
}
```

