# 2 Sum

出处 LeetCode 1

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where `index1` must be less than `index2`. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

    Input: numbers={2, 7, 11, 15}, target=9
    Output: index1=1, index2=2

## Solution

当处理当前节点需要依赖于之前的部分结果时，可以考虑使用哈希表记录之前的处理结果。其本质类似于动态编程(Dynamic Programming)，利用哈希表以O(1)的时间复杂度利用之前的结果。

对于数组中的某个下标i，如何判断它是否属于符合条件的两个数字之一？最直观的方法是再次扫描数组，判断target – array[i]是否存在在数组中。这样做的时间复杂度是O(n^2 )，效率不高的原因是没有保存之前的处理结果，每次都在做重复的工作。尽管效率不高，但是通过最直观的方法，我们发现处理当前节点需要依赖于之前的部分结果。如何保存之前的处理结果？可以使用哈希表。既然我们需要回答target – array[i]是否存在在数组中”，那不妨把值作为键，通过询问哈希表是否含有所需要的键来得到我们需要的回答。最终，根据题目，我们需要返回下标，那么把下标作为哈希表的值也是非常自然了。

## Complexity 

我们可以先对数组中的每个元素进行上述哈希处理，然后再从头至尾扫描数组，判断对应的另一个数是否存在在数组中，时间复杂度O(n + n)。事实上，我们可以利用动态编程的思想，仅仅利用已经处理的部分解：哈希表只存储前驱节点的信息。对于当前节点，判断前驱中是否含有对应值。当处理完当前节点，把当前节点加入哈希表，作为已经处理的部分解。这样，时间复杂度可以进一步减少为O(n)。

## Code

```java
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int len = nums.length;
        for (int i = 0; i < len; i++){
            if (map.get(target - nums[i]) != null){
                return new int[]{map.get(target - nums[i]), i+1};
            } 
            map.put(nums[i], i+1);
        }
        return null;
    }
}
```

