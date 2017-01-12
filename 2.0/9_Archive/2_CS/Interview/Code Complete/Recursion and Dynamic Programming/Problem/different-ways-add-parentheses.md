# Different Ways to Add Parentheses

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.


Example 1

Input: "2-1-1".

    ((2-1)-1) = 0
    (2-(1-1)) = 2
    
Output: [0, 2]


Example 2

Input: `2*3-4*5`

    (2*(3-(4*5))) = -34
    ((2*3)-(4*5)) = -14
    ((2*(3-4))*5) = -10
    (2*((3-4)*5)) = -10
    (((2*3)-4)*5) = 10
    
Output: [-34, -14, -10, -10, 10]

## Solution

each time we encounter an operator, split the input string into two parts, one left to the operator and the other right to it. For example, when we reach -, we split the string into `2*3` and `4*5`. Then we recursively (yeah, this is the biggest simplification) compute all possible values of the left and right parts and operate on all the possible pairs of them. The idea will become much more obvious if you read the following code.

## Complexity

时间复杂度 O(n^2 )，空间复杂度 O(n)
## Code

```cpp
class Solution {
public:
    vector<int> diffWaysToCompute(string input) {
        vector<int> outputs;
        int n = input.length();
        for (int i = 0; i < n; i++) {
            if (input[i] == '+' || input[i] == '-' || input[i] == '*') {
                string left = input.substr(0, i);
                string right = input.substr(i + 1, n - i - 1);
                vector<int> lval = diffWaysToCompute(left);
                vector<int> rval = diffWaysToCompute(right);
                for (int l : lval) {
                    for (int r : rval) {
                        switch (input[i]) {
                            case '+':
                                outputs.push_back(l + r);
                                break;
                            case '-':
                                outputs.push_back(l - r);
                                break;
                            default:
                                outputs.push_back(l * r);
                        }
                    }
                }
            }
        }
        if (outputs.empty())
            outputs.push_back(stoi(input));
        return outputs;
    }
};
```

