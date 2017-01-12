# Gas Station

出处

Suppose you are traveling along a circular route. On that route, we have N gas stations for you, where the amount of gas at station i is gas[i]. Suppose the size of the gas tank on your car is unlimited. To travel from station i to its next neighbor will cost you cost[i] of gas. Initially, your car has an empty tank, but you can begin your travel at any of the gas stations. Please return the smallest starting gas station's index if you can travel around the circuit once, otherwise return -1.

在一条环路上有 N 个加油站，其中第 i 个加油站有汽油gas[i]，并且从第 i 个加油站前往第 i+1个加油站需要消耗汽油cost[i]。

你有一辆油箱容量无限大的汽车，现在要从某一个加油站出发绕环路一周，一开始油箱为空。

求可环绕环路一周时出发的加油站的编号，若不存在环绕一周的方案，则返回-1。

样例

    现在有4个加油站，汽油量gas[i]=[1, 1, 3, 1]，环路旅行时消耗的汽油量cost[i]=[2, 2, 1, 1]。则出发的加油站的编号为2。

注意

    数据保证答案唯一。

挑战

    O(n)时间和O(1)额外空间

## Solution

这是一个比较难理解的问题，但其本质上还是选择一个序列，只不过这个序列是环形的。事实上，可以考虑对问题进行如下操作：对于第i个加油站，它能够给车子提供的净动力为array[i] = gas[i] – cost[i]。问题转化为，找到一个起始位置index，将array依此向左shift，即index->0(index对应新的数组下标0)，index+1->1…，使得对于任意0 <= i < n，满足序列和subSum(0, i)大于0。

首先，考虑什么情况下有解。经过上述转换，很明显有解的情况对应于sum(array)大于等于0。

那么，剩下的问题是在有解的情况下，如何选择一个正确的起始点。类似与一般序列问题，考虑将当前节点作为序列的末节点。如果从记录的开始节点(index)起，到当前节点的过程中，一旦出现subSum小于0，那么从开始节点到当前节点的所有节点都不能作为开始节点，因为在过程中一定会出现subSum小于0的情况，否则累计的结果不会为负。那么，开始点至少是index+1。另一方面，可以证明，如果从记录的开始点出发可以走到第n个加油站，即subSum(index, n)大于0，那么该开始点一定能走完全程。

---

1. 从i开始，j是当前station的指针，sum += gas[j] – cost[j] （从j站加了油，再算上从i开始走到j剩的油，走到j+1站还能剩下多少油）
2. 如果sum < 0，说明从i开始是不行的。那能不能从i..j中间的某个位置开始呢？既然i出发到i+1是可行的， 又i~j是不可行的， 从而发现i+1~ j是不可行的。
3. 以此类推i+2~j， i+3~j，i+4~j 。。。。等等都是不可行的
4. 所以一旦sum<0，index就赋成j + 1，sum归零。
5. 最后total表示能不能走一圈。

以上做法，其实是贪心的思想：

也就是说brute force的解是 ： 一个一个来考虑， 每一个绕一圈， 但是 实际上 我们发现 i - j不可行 直接index就跳到j+1， 这样周而复始，很快就是绕一圈 就得到解了。

## Complexity

时间复杂度 O(n)，空间复杂度 O(n)，可以优化至 O(1)

## Code 

O(1)

```java
public class Solution {
    /**
     * @param gas: an array of integers
     * @param cost: an array of integers
     * @return: an integer
     */
    public int canCompleteCircuit(int[] gas, int[] cost) {
        if (gas == null || cost == null || gas.length == 0 || cost.length == 0) {
            // Bug 0: should not return false;
            return -1;
        }

        int total = 0;
        int sum = 0;

        int startIndex = 0;

        int len = gas.length;
        for (int i = 0; i < len; i++) {
            int dif = gas[i] - cost[i];
            sum += dif;

            if (sum < 0) {
                // Means that from 0 to this gas station, none of them can be the solution.
                startIndex = i + 1; // Begin from the next station.
                sum = 0; // reset the sum.
            }

            total += dif;
        }

        if (total < 0) {
            return -1;
        }

        return startIndex;
    }
}
```

O(n)

```java
int canCompleteCircuit(int[] gas, int[] cost){
	int len = gas.length;
	if (len != cost.length || len == 0) return -1;
	
	int[] arr = new int[len];
	int sum = 0;
	for (int i = 0; i < len; i++){
		arr[i] = gas[i] - cost[i];
		sum += arr[i];
	}
	
	if (sum < 0){
		return -1;
	}
	
	sum = 0;
	int index = 0;
	for (int i = 0; i < len; i++){
		sum += arr[i];
		if (sum < 0){
			sum = 0;
			index = i + 1;
		}
	}
	return index;
}

```


