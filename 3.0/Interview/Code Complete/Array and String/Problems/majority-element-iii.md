# Majority Element III

给定一个整型数组，找到主元素，它在数组中的出现次数严格大于数组元素个数的1/k。

样例

    给出数组 [3,1,2,3,2,3,3,4,4,4] ，和 k = 3，返回 3

注意

    数组中只有唯一的主元素

挑战

    要求时间复杂度为O(n)，空间复杂度为O(k)

## Solution

Keep k-1 pointers and counters. Use HashMap to store numbers and counters, every delete operation will cost k-1, however, the max times of deletion is n/(k-1) because deletion only happens when there are (k-1) numbers in the map. So the overall complexity is still O(n).

## Code

```java
public class Solution {
    /**
     * @param nums: A list of integers
     * @param k: As described
     * @return: The majority number
     */
    public int majorityNumber(ArrayList<Integer> nums, int k) {
        int len = nums.size();
        if (len < k) {
            return -1;
        }
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int x : nums) {
            if (map.size() < k && !map.containsKey(x)) {
                map.put(x, 1);
            } else if (map.containsKey(x)) {
                map.put(x, map.get(x) + 1);
            } else {
                Map<Integer, Integer> tmp = new HashMap<Integer, Integer>();
                for (int key : map.keySet()) {
                    if (map.get(key) > 1) {
                        tmp.put(key, map.get(key)-1);
                    }
                }
                map = tmp;
            }
        }
        int result = 0;
        int count = 0;
        for (int key : map.keySet()) {
            if (map.get(key) > count) {
                result = key;
                count = map.get(key);
            }
        }
        return result;
    }
}


```

