# Generate Parentheses

出处

Given n pairs of parentheses, generate all valid combinations of parentheses. E.g. if n = 2, you should return ()(), (())

## Solution

解题分析：由于题目要求找出所有解，故属于发散性的DP，用backtracking。核心在于：对于当前节点，也哪些可用的选择。对本题而言：

+ 如果所剩的左括号大于0，那么继续添加左括号一定是一种决策；
+ 如果所剩的左括号少于右括号，那么补充右括号也一定是一种决策；

应该按照决策的选择方向进行回溯。

## Complexity

可以近似认为时间复杂度为 O(n!)，空间复杂度为 O(2^n )

## Code 

```java
void parenthesesCombination(int left, int right, String path, ArrayList<String> paths){
	if (left < 0 || right < 0) return;
	
	if (left > 0){
		String newpath = path + '(';
		parenthesesCombination(left-1, right, newpath, paths);
		
		// we use newpath so as to skip the explicit backtracing 
	}
	
	if (left < right){
		String newpath = path + ')';
		right--;
		if (right == 0){
			paths.add(newpath);
		} 
		// 上面 right 已经减过了，所以不用再减
		parenthesesCombination(left, right, newpath, paths);
		// we use newpath so as to skip the explicit backtracing 
	}
}

ArrayList<String> generateParenthesis(int n){
	ArrayList<String> res = new ArrayList<String>();
	if (n <= 0) return res;
	String path = "";
	parenthesesCombination(n, n, path, res);
}

```
  

