# Product of Array Except Self

出处

Given an array of integers, write a function to replace each element with the product of all elements other than that element.

## Solution

当前节点的解，既和左边的元素有关，又与右边的元素有关，两者相互独立，可以用双向DP。左遍历DP计算积累到目前为止的乘积，右遍历DP计算从目前开始到最后的乘积。

## Complexity

两次遍历，时间复杂度 O(n)，空间复杂度 O(n)，空间可以优化至 O(1)

## Code  

```java
public class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] result = new int[nums.length];
 
        int[] t1 = new int[nums.length];
        int[] t2 = new int[nums.length];
     
        t1[0]=1;
        t2[nums.length-1]=1;
     
        //scan from left to right
        for(int i=0; i<nums.length-1; i++){
            t1[i+1] = nums[i] * t1[i];
        }
     
        //scan from right to left
        for(int i=nums.length-1; i>0; i--){
            t2[i-1] = t2[i] * nums[i];
        }
     
        //multiply
        for(int i=0; i<nums.length; i++){
            result[i] = t1[i] * t2[i];
        }
     
        return result;
    }
    
    public int[] productExceptSelf_2(int[] nums) {
        int[] result = new int[nums.length];
        result[result.length-1] = 1;
     
        for(int i=nums.length-2; i>=0; i--) {
            result[i] = result[i+1] * nums[i+1];
        }
     
        int left = 1;
        for(int i=0; i<nums.length; i++) {
            result[i] *= left;
            left *= nums[i];
        }
     
        return result;
    }
}
```


