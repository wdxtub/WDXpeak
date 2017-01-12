# Nth Prime

出处

Compute the nth prime

## Solution

在数学理论中，存在埃拉托斯特尼筛法(sieve of Eratosthenes)，用来解决素数判定问题。如果面试中碰到这个问题，面试官绝对不是希望获得那样的解答，因为这里考察的是编程技能，而不是高深的数学知识。

第n个素数仍然是一个特解问题，我们需要考虑DP。事实上，素数的定义隐含了一个递推关系，即如果n是素数，那么n不能被1 ~ n-1的所有素数整除(事实上，可以优化为1~sqrt(n))，即当前节点与之前的所有节点有关:

+ Prime(n) = G ( Prime(n-1), Prime(n-2), Prime(n-3) … Prime(1));
+ Prime(1) = 2
+ G( )表示不能整除的关系。

## Complexity

对于每个数字需要检查前面所有的素数，所以时间复杂度是 O(n^2 )，空间复杂度为 O(n)

## Code

```java
int NthPrime(int n){
	ArrayList<Intger> primes = new ArrayList<Integer>();
	primes.add(2);
	int number = 3;
	while (primes.size() < n){
		boolean isPrime = true;
		for (int i = 0; i < primes.size(); i++){
			if (number % primes.get(i) == 0){
				isPrime = false;
			}
		}
		if (isPrime){
			primes.add(number);
		}		
		number += 2;
	}
	return primes.get(n-1);
}

```


