# Majority Element II

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.

## Solution

观察可知，数组中至多可能会有2个出现次数超过 ⌊ n/3 ⌋ 的众数

记变量n1, n2为候选众数； c1, c2为它们对应的出现次数

遍历数组，记当前数字为num

若num与n1或n2相同，则将其对应的出现次数加1

否则，若c1或c2为0，则将其置为1，对应的候选众数置为num

否则，将c1与c2分别减1

最后，再统计一次候选众数在数组中出现的次数，若满足要求，则返回之。

## Complexity

时间复杂度 O(n)，空间复杂度 O(1)

## Code

```java
public class Solution {
    public List<Integer> majorityElement(int[] nums) {
        List<Integer> res = new ArrayList<>();
        if(nums==null || nums.length==0) return res;
        if(nums.length==1) {
            res.add(nums[0]);
            return res;
        }
        
        int m1 = nums[0];
        int m2 = 0;
        
        int c1 = 1;
        int c2 = 0;
        
        for(int i=1; i<nums.length; i++) {
            int x = nums[i];
            if(x==m1) ++c1;
            else if(x==m2) ++c2;
            else if(c1==0) {
                m1 = x;
                c1 = 1;
            } else if(c2==0) {
                m2 = x;
                c2 = 1;
            } else {
                --c1; --c2;
            }
        }
        c1 = 0; c2 = 0;
        for(int i=0; i<nums.length; i++) {
            if(m1 == nums[i]) ++c1;
            else if(m2 == nums[i]) ++c2;
        }
        if(c1>nums.length/3) res.add(m1);
        if(c2>nums.length/3) res.add(m2);
        return res;
    }
}
```

