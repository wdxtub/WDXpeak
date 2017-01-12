# cPacket

## 公司介绍

主要是给大公司的 data center 提供进一步的底层封装和技术支持，比如说 google 或者是 facebook 的 data center，他们不用直接去操心 data center，而可以直接使用 cPacket 提供的 web 界面来实时了解和监控运行状况。并且 cPacket 也会负责注入安全，部署，攻击防范等。

公司目前工程师大概 40 个，分成 4 个 team

1. Hardware/Firmware: 主要是负责硬件以及相关的底层开发 —— FPGA
2. Software: 主要是 web 界面开发 —— Python
3. Solution: 主要是在客户的 data center 那边来处理各种事务
4. QA

今天面试我的是 firmware 的 engineer。

提供午餐、零食、周五有 happy hour，上班8-11点，下班5-8点，在 Mountain View。服务运行在自己的服务器上。

接下来如果顺利是两轮电面之后 onsite。看看自己能走多远了

## Phone Screen

Mark Lewis，也是 firmware group 的小哥，问了我三个题目

1. 如何把十进制转换为二进制，分别用递归，循环和位操作来实现
2. 返回链表的倒数第 n 个节点
3. 如何设计一个文件系统

进制转换

```java
// 递归
void dTox(int n, int r){
	if (n >= r){
		dTox(n/r, r);
	}
	System.out.print(n%r);
}

// 非递归
void dTox(int n, int r){
	Stack<Integer> s = new Stack<Integer>();
	while (n > 0){
		s.push(n%r);
		n = n/r;	
	}
	
	while (!s.empty()){
		System.out.print(s.top());
		s.pop();
	}
}

// 位操作 主要指二进制
void dToX(int n, int r){
	Stack<Integer> s = new Stack<Integer>();
	while (n > 0){
		s.push(n >> i) & 1;
	}
	while (!s.empty()){
		System.out.print(s.top());
		s.pop();
	}
}



```

---

二面

```
// recursive method
// given a sorted array
// balanced
// middle of the array 
// left side [0 to mid-1] right side [mid+1 to len-1]
// stop condition: left index > right index

Node sortedArrayToBST(int[] arr){
	// input checking
  if (arr.length == 0 || arr == null) return null;
  if (arr.length == 1) {
  	Node head = new Node(arr[0]);
    return head;
  }
  
  // recursive
  return help(arr, 0, arr.length -1);
}

// return the root node of the bst from arr[left to right]
Node help(int[] arr, int left, int right){
	if ( left > right ){
  	return null;
  } 
  if (left == right) {
  	Node head = new Node(arr[left]);
    return head;
  }
  
  int mid = (left + right) / 2;
  // arr[left...mid-1, mid, mid+1...right]
  Node left = help(arr, left, mid - 1);
  Node right = help(arr, mid + 1, right);
  Node head = new Node(arr[mid]);
  head.left = left;
  head.right = right;
  return head;
}

// input : index number
// output : fibonacci number
input:		0	1	2	3	4	5	6	...
output:		1	1	2	3	5	8	13

// equation ele[i] = ele[i-1] + ele[i-2]
// use array to store the result

int N = 1000;

int computedflag = 1;
int[] resultSet = new int[N];
resultSet[0] = 1;
resultSet[1] = 1;
// init state 

int fibonacci(int n){
  if (n <= computedflag)
  	return resultSet[n];

  // n = 2 -> output = 2
  for (int i = computedflag + 1; i < n; i++){
  	resultSet[i] = resultSet[i-1] + resultSet[i-2];
  }
  computedflag = n;
  return resultSet[n];
}
```


