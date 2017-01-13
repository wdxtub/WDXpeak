# Codility 准备指南

因为要准备在线测试，所以先上网收集一些题目热身一下

<!-- MarkdownTOC -->

- challenge Aluminium 2014

<!-- /MarkdownTOC -->


## challenge Aluminium 2014

数组元素范围 [-10^4,+10^4]

函数头部：

    int solution(vector<int> &A);

要求时间复杂度 O(N)，空间复杂度O(N)。

分析：这是我比较喜欢的一个题，它在传统的最大子段和上做了一些改动。之前尝试过从最大子段和方法上做修改，例如换一个元素，删一个元素等等，都挂了。后来和管神讨论，发现可以dp，dp也是很巧妙的。

设f表示以i结尾的一段连续的最大子数组外加单独一个元素的最大和。这里需要多说几句，这个定义非常重要。首先：
1. 以i结尾的连续一段可以为空，但如果非空的话，一定要以i结尾 （废话）
2. 单独存在的一个点不能为空，并且这个点不能在（1）之内 （同一个元素不能加两次嘛）

定义这个的目的是，如果我们有了这个值，那个单独的元素就是我们换入最终结果的元素。

那么f的递推式是 f = max(f[i - 1] + A, max{A[0..i]}} 前者对应以i结尾的连续一段非空的情况，这个和传统最大子段和很像…… 后面那个其实是如果连续一段为空，按照f的定义，我们只能取一个点，那么这个点显然要取A[0..i]最大的。如此，我们定义好了f。

再定义一个g,这个g是和传统最大子段和定义是一样的，g表示以i开头的最大子段和。这个不多说g = max(g[i + 1] , 0) + A, 那么我们倒着循环i的时候（i = n - 2..0)顺便能求出每个g的值，并且也能求出不交换的普通的最大子段和。也就是max{g[0..n-1]}。

那么对于交换的情况，我们考虑A和某个元素j < i做了交换，那么其实结果是g - a + f[i - 1] , 也就是说f[i - 1]里面包含了a要换入的元素。所以我们再循环一次取max就行了。

可是这种交换值对应了i和j < i的交换。 所以我们还需要把A中的元素翻转，再计算一次。


    // you can use includes, for example:
    // #include <algorithm>
    // you can write to stdout for debugging purposes, e.g.
    // cout << "this is a debug message" << endl;

    #include <algorithm>

    int help(vector<int> &a) {
        int n = a.size();
        vector<int> f,g;
        f.resize(n);
        f[0] = a[0];
        int now = a[0];
        for (int i = 1; i < n; ++i) {
            now = max(now, a[i]);
            f[i] = max(a[i] + f[i - 1], now);
        }
        g.resize(n);
        g[n - 1] = a[n - 1];
        int answer = a[n - 1];
        for (int i = n - 2; i >= 0; --i) {
            g[i] = max(g[i + 1], 0) + a[i];
            answer = max(answer, g[i]);
        }
        for (int i = 1; i < n; ++i) {
            answer = max(answer, g[i] - a[i] + f[i - 1]);
        }
        return answer;
    }

    int solution(vector<int> &A) {
        // write your code in C++11
        int answer = help(A);
        reverse(A.begin(),A.end());
        answer = max(answer,help(A));
        return answer;
    }

