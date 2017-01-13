# N Queen

出处

## Solution

本题是经典的八皇后问题。由于需要找到所有解，属于发散性问题。对于每一行，我们枚举可以将当前的皇后放在哪一列，所有目前为止可行的列都可以作为选择进行DP，即每次选择方向时都经过充分剪枝，使得每一步都朝着胜利条件前进。这样，最后得到的解“一定是需要的解。

## Complexity

回溯总共n步，每次供选择的方向为n。经过剪枝之后，可以认为复杂度小于n!。

## Code

```java
boolean checkValid(int row, int col, int[] rowCol){
	for (int r = row - 1; r >=0; r--){
		if (rowCol[r] == col) return false;
		if (abs[r - row) == abs(rowCol[r] - col) return false;
	}
	return true;
}

void placeQ(int row, int[] rowCol, ArrayList<ArrayList<Integer> res){
	if (row == GRID_SIZE){
		// winning
		ArrayList<Integer> sol = new ArrayList<Integer>();
		for (int i = 0; i < GRID_SIZE; i++){
			sol.add(rowCol[i]);
		}
		res.add(sol);
		return;
	}
	
	int col = 0;
	for (col = 0; col < GRIDSIZE; col++){
		if (checkValid(row, col, rowCol)){
			rowCol[row] = col;
			placeQ(row+1, rowCol, res);
			// because we rewrite rowCol[row] everytime, 
        // so backtracking is inferred here
		}
	}
}
```

