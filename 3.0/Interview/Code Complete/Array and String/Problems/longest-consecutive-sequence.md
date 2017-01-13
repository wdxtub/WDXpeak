# Longest Consecutive Sequence

出处

最长连续序列

Get the length of the longest consecutive elements sequence in an array. For example, given [31, 6, 32, 1, 3, 2],the longest consecutive elements sequence is [1, 2, 3]. Return its length: 3.

## Solution

如何判断当前节点i是否属于一个序列？如果array[i] – 1存在在数组中，那么array[i]就可以作为后继加入序列。类似地，如果array[i] + 1存在在数组中，那么array[i]就可以作为前驱加入序列。我们发现处理当前节点需要依赖于之前的部分结果：判断array[i] – 1，array[i] + 1是否存在于数组中。如何保存之前的处理结果？可以使用哈希表。很显然，键对应于数值。但对于这个问题，value并不是那么明显，需要进一步分析。

一般而言，键用于快速判断哈希表中有没有我们需要的元素，值提供我们需要的结果。在这题中，我们期望于获得怎样的部分解呢？我们需要知道现在已经构成的序列是怎样的。由于序列是一系列连续整数，所以只要序列的最小值以及最大值，就能唯一确定序列。“而所谓的“作为后继加入序列”，“作为前驱加入序列”，无非就是更新最大最小值。所以哈希表的值可以是一个记录最大／最小值的结构，用以描述当前节点参与构成的最长序列。

## Complexity

根据上述算法，我们只要扫描一遍整个数组就能获得结果，时间复杂度O(n)，附加空间O(n)。

## Code

```java
class Bound{
	int high;
	int low;
	public Bound(int h, int l){
		high = h;
		low = l;
	}
}

int lcs(int[] arr){
	HashMap<Integer, Bound> range = new HashMap<Integer, Bound>();
	int maxLen = 0;
	for (int i = 0; i < arr.length; i++){
		if (!range.containsKey(arr[i]){
			int local = arr[i];
			int high = local;
			int low = local;
			
			if (range.containsKey(local-1){
				low = range.get(local-1).low;
			}
			
			if (range.containsKey(local+1){
				high = range.get(local+1).high;
			}
			
			if (high - low + 1 > maxLen){
				maxLen = high - low + 1;
			}
			
			range.put(local, new Bound(high, low)):
		} else {
			continue;
		}
	}
	return maxLen;
}

```


