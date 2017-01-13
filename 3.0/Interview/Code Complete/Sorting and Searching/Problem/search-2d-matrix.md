# Search 2D matrix

出处

Check if an element is in a M x N matrix, each row and column of which is sorted.

## Solution

首先我们可以构造一个矩阵：

    1    5    10   20
    2    6    11   30
    7    9    12   40
    8    15   31   41

如果要在上述矩阵中找到9，应该如何计算？最简单的方法显然是遍历每行每列，这样的时间复杂度是O(n^2 )，而且完全没有利用到矩阵已经部分有序的特性。

进一步观察矩阵，任何元素都将矩阵划分为4个部分：

     I  | II
    III | IV

根据矩阵的特性，同行同列中元素的大小关系已知，并且I区的所有数据都比当前元素小，IV区的所有数据都比当前元素大。II，III两区数据与当前元素没有明确的相对大小关系。因此，我们的每次操作必须保证没有II区或III区，即从右上角或者左下角开始搜索。不妨假设从右上角(20)开始搜索：

1. 比较20与9，左移
2. 比较10与9，左移
3. 比较5与9，下移
4. 比较6与9，下移
5. 找到9

不难发现，每次当前元素大于待搜索元素，我们左移，否则下移。

对于有序容器的搜索，能不能用二分查找？对于本例，我们不能使用二分查找及其变种。原因是：二分查找的关键在于，当前元素将容器分为两个部分，并且通过比较当前元素和待搜索元素的大小，我们能够确定两者的相对位置关系，进而缩小搜索范围。但是对于本例，当前元素和待搜索元素大小关系并不能确定两者相对位置。

## Complexity

假设矩阵有M行N列，则我们至多下移M次，左移N次，即算法复杂度O(M+N)。

## Code 

```java
boolean isInMatrix(int[][] matrix, int target){
	int row = matrix.length;
	int column = matrix[0].length;
	int r = 0;
	int c = column - 1;
	while (r < row && c >= 0){
		if (matrix[r][c] == target){
			return true;
		}
		if (matrix[r][c] > target){
			c--;
		} else {
			r++;
		}
	}
	return false;
}
```

