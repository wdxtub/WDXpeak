# Subarray Sum to K

Given an nonnegative integer array, find a subarray where the sum of numbers is k.

Your code should return the index of the first number and the index of the last number.

Example

    Given [1, 4, 20, 3, 10, 5], sum k = 33, return [2, 4].


## Solution

核心约束条件变成 f(i1) - f(i2) = k

```cpp
vector<int> subarraySum(vector<int> nums, int k){
    vector<int> result;
    // curr_sum for the first item, index for the second item
    // unordered_map<int, int> hash;
    map<int, int> hash;
    hash[0] = 0;

    int curr_sum = 0;
    for (int i = 0; i != nums.size(); ++i) {
        curr_sum += nums[i];
        if (hash.find(curr_sum - k) != hash.end()) {
            result.push_back(hash[curr_sum - k]);
            result.push_back(i);
            return result;
        } else {
            hash[curr_sum] = i + 1;
        }
    }

    return result;
}

```

与上一题的变化之处有两个地方，第一个是判断是否存在哈希表中时需要使用`hash.find(curr_sum - k)`, 最终返回结果使用`result.push_back(hash[curr_sum - k]);`而不是`result.push_back(hash[curr_sum]);`

### 利用单调函数特性的方法

f(i)为单调不减函数，题中要寻找 f(i2) - f(i1) = k 则必有 f(i2) >= k，类似于两个指针的方法来进行遍历

```cpp
vector<int> subarraySum2(vector<int> nums, int k){
    vector<int> result;

    int left_index = 0;
    int curr_sum = 0;
    for (int i = 0; i != nums.size(); ++i) {
        curr_sum += nums[i];
        if (curr_sum == k) {
            result.push_back(left_index);
            result.push_back(i);
            return result;
        }

        while (curr_sum > k) {
            curr_sum -= nums[left_index];
            ++left_index;
        }
    }

    return result;
}

```
使用for循环累加`curr_sum`, 在`curr_sum > k`时再使用`while`递减`curr_sum`, 同时递增左边索引`left_index`.

