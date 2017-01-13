# Check Duplicate III

出处

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.

## Solution

维持一个长度为k的window, 每次检查新的值是否与原来窗口中的所有值的差值有小于等于t的. 如果用两个for循环会超时O(nk). 使用treeset( backed by binary search tree) 的subSet函数,可以快速搜索. 复杂度为 O(n logk)

## Complexity

复杂度为 O(n logk)

## Code

```java
public class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if(k<1 || t<0 || nums==null || nums.length<2) return false;  
          
        SortedSet<Long> set = new TreeSet<Long>();  
          
        for(int j=0; j<nums.length; j++) {  
            SortedSet<Long> subSet =  set.subSet((long)nums[j]-t, (long)nums[j]+t+1);  
            if(!subSet.isEmpty()) return true;  
              
            if(j>=k) {  
                set.remove((long)nums[j-k]);  
            }  
            set.add((long)nums[j]);  
        }  
        return false;  
    }
}
```

