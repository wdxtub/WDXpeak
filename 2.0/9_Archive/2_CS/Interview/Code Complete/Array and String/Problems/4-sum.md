# 4 Sum

出处

Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.

    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)

## Solution

Similar to 3Sum, 2Sum. 但是又很多细节需要注意

## Complexity

## Code 

```java
public class Solution {
    public List<List<Integer>> fourSum(int[] num, int target) {
        int N = num.length;
        List<List<Integer>> res = new ArrayList<List<Integer>>();
        if (N < 4) return res;
        Arrays.sort(num);
        for (int i = 0; i < N; ++i)
        {
            if (i > 0 && num[i] == num[i-1]) continue; // avoid duplicates
            for (int j = i+1; j < N; ++j)
            {
                if (j > i+1 && num[j] == num[j-1]) continue; // avoid duplicates
                int twosum = target - num[i] - num[j];
                int l = j + 1, r = N - 1;
                while (l < r)
                {
                    int sum = num[l] + num[r];
                    if (sum == twosum) {
                    ArrayList<Integer> tmp = new ArrayList<Integer>();
                    tmp.add(num[i]); tmp.add(num[j]); tmp.add(num[l]); tmp.add(num[r]);
                    res.add(tmp);
                        while (l < r && num[l+1] == num[l]) l++; // avoid duplicates
                        while (l < r && num[r-1] == num[r]) r--; // avoid duplicates
                        l++; r--;
                    }
                    else if (sum < twosum) l++;
                    else r--;
                }
            }
        }
        return res;
    }
}
```


