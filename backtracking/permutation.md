# Permutation - 排列

排列常见的有数字全排列，字符串排列等。

## Permutations - 全排列

Question: [(15) Permutations](http://www.lintcode.com/en/problem/permutations/)

```
Given a list of numbers, return all possible permutations.

Example
For nums [1,2,3], the permutaions are:

[

    [1,2,3],

    [1,3,2],

    [2,1,3],

    [2,3,1],

    [3,1,2],

    [3,2,1]

]

Challenge
Do it without recursion
```

题解：

使用之前subsets的模板，但是在取结果时只能取`list.size() == nums.size()`的解，且在添加list元素的时候需要注意除重。

**C++**
```
class Solution {
public:
    /**
     * @param nums: A list of integers.
     * @return: A list of permutations.
     */
    vector<vector<int> > permute(vector<int> nums) {
        vector<vector<int> > result;
    	if (nums.empty()) {
    	    return result;
    	}

    	vector<int> list;
    	backTrack(result, list, nums);

    	return result;
    }

private:
    void backTrack(vector<vector<int> > &result, vector<int> &list, \
                   vector<int> &nums) {
        if (list.size() == nums.size()) {
            result.push_back(list);
            return;
        }

        for (int i = 0; i != nums.size(); ++i) {
            if (find(list.begin(), list.end(), nums[i]) != list.end()) {
                continue;
            }
            list.push_back(nums[i]);
            backTrack(result, list, nums);
            list.pop_back();
        }
    }
};
```

源码分析：

在除重时使用了标准库`find`，使用回溯法解题的关键在于如何确定正确解及排除不符条件的解(剪枝)。
