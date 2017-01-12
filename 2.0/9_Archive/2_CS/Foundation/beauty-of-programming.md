# 编程之美

<!-- MarkdownTOC -->

- 控制 CPU 占用率曲线
- 求二进制数中 1 的个数

<!-- /MarkdownTOC -->


## 控制 CPU 占用率曲线

1. CPU 占用率为 50%，一条直线
2. 占用率为一条直线，具体多少由程序指定
3. CPU 占用率是一个正弦曲线

所谓精通 Windows 并不是那么简单

## 求二进制数中 1 的个数

位操作

```cpp
int Count(int v){
    int num = 0;
    while(v){
        num += v & 0x01;
        v >>= 1;
    }
    return num;
}
```

复杂度只与 1 相关

```cpp
int Count(int v){
    int num = 0;
    while(v){
        v &= (v-1);
        num++;
    }
    return num;
}

## 多少位不同

给两个整数，问他们的二进制表示中有多少位是不同的

## 阶乘后面 0 的个数

判断质因数分解中有多少个 5 即可。

```cpp
ret = 0;
for (int i = 1; i <= N; i++){
    j = i;
    while (j % 5 == 0){
        ret++;
        j /= 5;
    }
}
```

## N! 的二进制表示中最低位 1 的位置

这个问题实际上等同于求 N! 含有质因数 2 的个数。答案等于质因数个数加一。

```cpp
int lowestOne(int N){
    int ret = 0;
    while(N){
        N >>= 1;
        Ret += N;
    }
}
```

大概看了一下后面的题目，基本上已经都被 leetcode 一网打尽，所以这里就跳过了。
