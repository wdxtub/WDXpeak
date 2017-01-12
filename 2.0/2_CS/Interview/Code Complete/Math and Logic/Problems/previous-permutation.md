# Previous Permuation

给定一个整数数组来表示排列，找出其上一个排列。

样例

    给出排列[1,3,2,3]，其上一个排列是[1,2,3,3]
    给出排列[1,2,3,4]，其上一个排列是[4,3,2,1]

注意

    排列中可能包含重复的整数

## Solution

这里找上一个排列，仍然使用字典序算法，大致步骤如下：

1. 从后往前寻找索引满足 a[k] > a[k + 1], 如果此条件不满足，则说明已遍历到最后一个。
2. 从后往前遍历，找到第一个比a[k]小的数a[l], 即a[k] > a[l].
3. 交换a[k]与a[l].
4. 反转k + 1 ~ n之间的元素。

为何不从前往后呢？因为只有从后往前才能保证得到的是相邻的排列，可以举个实际例子自行分析。

## Code

```java
public class Solution {
    /**
     * @param nums: A list of integers
     * @return: A list of integers that's previous permuation
     */
    public ArrayList<Integer> previousPermuation(ArrayList<Integer> nums) {
        if (nums == null || nums.size() <= 1) {
            return nums;
        }
        // step1: find nums[i] > nums[i + 1]
        int i = 0;
        for (i = nums.size() - 2; i >= 0; i--) {
            if (nums.get(i) > nums.get(i + 1)) {
                break;
            } else if (i == 0) {
                // reverse nums if reach minimum
                reverse(nums, 0, nums.size() - 1);
                return nums;
            }
        }
        // step2: find nums[i] > nums[j]
        int j = 0;
        for (j = nums.size() - 1; j > i; j--) {
            if (nums.get(i) > nums.get(j)) {
                break;
            }
        }
        // step3: swap betwenn nums[i] and nums[j]
        Collections.swap(nums, i, j);
        // step4: reverse between [i + 1, n - 1]
        reverse(nums, i + 1, nums.size() - 1);

        return nums;
    }

    private void reverse(List<Integer> nums, int start, int end) {
        for (int i = start, j = end; i < j; i++, j--) {
            Collections.swap(nums, i, j);
        }
    }
}
```

