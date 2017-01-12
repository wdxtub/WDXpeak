# All Permutation 

出处

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

## Solution

选择后驱元素中的一个与当前节点交换，然后再将后面的节点作为子问题考虑。由于有重复元素，而重复元素对当前节点的影响是相同的，因此应该去重：把相同元素的替换作为同一个回溯方向/选择来处理，一旦发现是已经处理过的相同元素，则直接跳过。

或者使用 DFS 进行回溯

或者利用插入法：

P(a1) = a1

P(a1a2) = a1a2, a2a1

P(a1a2a3) = a1a2a3, a1a3a2, a2a1a3, a2a3a1, a3a1a2, a3a2a1

从第二步到第三步，恩可以看作是，对第二步中的两个结果，分别把 a3 插入到的每个结果中可能的各个位置，于是我们可以根据这个规律写出代码

## Complexity

时间复杂度 O(n^2 )，空间复杂度 O(n^2 )

## Code 

插入法

```java
public static ArrayList<String> getPermutations(String str){
    if (str == null){
        return null;
    }

    ArrayList<String> permutations = new ArrayList<String>();
    if (str.length() == 0){
        permutations.add("");
        return permutations;
    }

    char first = str.charAt(0);
    String rest = str.substring(1);
    ArrayList<String> words = getPermutations(rest);
    for (String word : words){
        for (int j = 0; j <= word.length(); j++){
            permutations.add(word.substring(0,j) + first + word.substring(j));
        }
    }
    return permutations;
}
```

---

交换法

```java
void helper(int index, ArrayList<Integer> path, ArrayList<ArrayList<Integer>> result){
	if (index > path.size()) return;
	
	if (index == path.size())
		result.add(new ArrayList<Integer>(path);
	
	HashSet<Integer> used = new HashSet<Integer>();
	for (int i = index; i < path.size(); i++){
		// handle duplicate
		if (used.contains(path.get(i));
			continue;
			
		// make choice
		swap(path, index, i);
		helper(index+1, path, result);
		// backtracing
		swap(path, index, i);
		used.put(path.get(i));
	}
}

ArrayList<ArrayList<Integer>> allPermutation(ArrayList<Integer> num){
	ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
	helper(0, num, result);
	return result;
}
```

---

回溯

```java
public class Solution {
    public List<List<Integer>> permute(int[] num) {
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        List<Integer> path = new ArrayList<Integer>();
        boolean[] free = new boolean[num.length];
        Arrays.fill(free, true);
        permuteRe(num, res, path,free);
        return res;
    }
    
    void permuteRe(int[] num, List<List<Integer>> res, List<Integer> path, boolean[] free) {
        if(path.size() == num.length) {
            ArrayList<Integer> tmp = new ArrayList<Integer>(path);
            res.add(tmp);
            return;
        }
        for (int i = 0; i < num.length; ++i) {
            if (free[i] == true) {
                free[i] = false;
                path.add(num[i]);
                permuteRe(num, res, path, free);
                path.remove(path.size() - 1);
                free[i] = true;
            }
        }
    }
}
```


