# All Subsets

出处

Given a collection of integers that might contain duplicates, return all possible subsets.

## Solution

如果不存在重复，那么对于当前节点，分为选取当前元素和不选取当前元素两条路径；

当存在重复时，那么对于当前节点，也可以分为选取当前元素和不选取当前元素。但是，如果没有选择当前元素，那么也一定不能选择后驱节点中与当前元素重复的任何元素，否则会产生完全重复的路径；

至于如果选取了当前元素，那么之后这个支线内部的重复问题，支线自然会解决，不需要关心。原因在于，子问题和原问题相互独立，子问题不需要关心如何来到当前节点。这样既保证了对于set{1,2,2}，subset{1, 2}只被选择一次，也保证了{1,2,2}会被选择在内。

## Complexity

时间复杂度 O(2^n ),空间复杂度 O(n^2 )

## Code 

```java
ArrayList<ArrayList<Integer>> getSubset(int[] arr){
	ArrayLIst<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
	ArrayList<Integer> path = new ArrayList<Integer>();
	Array.sort(arr);
	subsetWithDup(0, arr, path, result);
	return result;
}

void subsetWithDup(int index, int[] arr, ArrayList<Integer> path, ArrayList<ArrayList<Integer>> result){
	if (index == arr.length) return;
	for (int i = index; i < arr.length; i++){
		if (i != index && arr[i] == arr[i-1]) 
			continue;
		path.add(arr[i]);
		result.add(new ArrayList<Integer>(path));
		subsetWithDup(index + 1, arr, path, result);
		path.remove(path.size()-1);
	}
}
```
---

一些其他解法，无重复

```java
public class Solution {
    public List<List<Integer>> subsets(int[] S) {
        return subsets_2(S);
    }
    
    public List<List<Integer>> subsets_1(int[] S) {
        Arrays.sort(S);
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        List<Integer> path = new ArrayList<Integer>();
        subsetsRe(S, 0, path, res);
        return res;
    }
    void subsetsRe(int[] S, int start, List<Integer> path, List<List<Integer>> res) {
        List<Integer> sub = new ArrayList<Integer>(path);
        res.add(sub);
        for (int i = start; i < S.length; ++i) {
            path.add(S[i]);
            subsetsRe(S, i + 1, path, res);
            path.remove(path.size() - 1);
        }
    }
    
    public List<List<Integer>> subsets_2(int[] S) {
        Arrays.sort(S);
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        res.add(new ArrayList<Integer>());
        for (int i = 0; i < S.length; ++i) {
            int sz = res.size();
            for (int j = 0; j < sz; ++j) {
                List<Integer> path = new ArrayList<Integer>(res.get(j));
                path.add(S[i]);
                res.add(path);
            }
        }
        return res;
    }
}
```

---

其他解法：有重复

```java
public class Solution {
    public List<List<Integer>> subsetsWithDup(int[] S) {
        Arrays.sort(S);
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        res.add(new ArrayList<Integer>());
        int presz = 0;
        for (int i = 0; i < S.length; ++i) {
            int sz = res.size();
            for (int j = 0; j < sz; ++j) {
                if (i == 0 || S[i] != S[i-1] || j >= presz) {
                    List<Integer> path = new ArrayList<Integer>(res.get(j));
                    path.add(S[i]);
                    res.add(path);
                }
            }
            presz = sz;
        }
        return res;
    }
}
```


