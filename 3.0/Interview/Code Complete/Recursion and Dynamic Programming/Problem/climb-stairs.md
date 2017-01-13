# Climb Stairs

出处

Suppose we have a ladder which has n steps. Each time you can either climb 1 or 2 steps. Please write a function to calculate how many distinct ways that can you climb to the top?

## Solution

本问题描述了一个数量问题，属于前述的强收敛(聚合)性问题，可以用DP。DP的核心在于递推关系：当前节点的值可以由前驱走一步到达，或者前前驱走两步到达，即CountOfWays(n) = CountOfWays(n–1) + CountOfWays(n-2)；由于当前节点只与紧邻的两个节点决定，所以只需要2个临时变量来表示前驱节点的解即可，而不用DP table，因为更老的解我们不需要关心。在实现时，往往边界条件直接用if…then return value的形式，成为递归的出口。

## Complexity

遍历一次，时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
int numberWays(int n){
	if (n < 0) return 0;
	if (n < 3) return n;
	int one = 1;
	int two = 2;
	int cur = 0;
	for (int i = 3; i <= n; i++){
		cur = one + two;
		one = two;
		two = cur;
	}
	return cur;
}
```


