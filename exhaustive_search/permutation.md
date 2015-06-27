# Permutations

## Source

- lintcode: [(15) Permutations](http://www.lintcode.com/en/problem/permutations/)

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

## 题解

排列常见的有数字全排列，字符串排列等。

使用之前subsets的模板，但是在取结果时只能取`list.size() == nums.size()`的解，且在添加list元素的时候需要注意除重。

### C++

```c++
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
            // remove the element belongs to list
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

### 源码分析

在除重时使用了标准库`find`(不可使用时间复杂度更低的`binary_search`，因为`list`中元素不一定有序)，时间复杂度为 $$O(N)$$, 也可使用`hashmap`记录`nums`中每个元素是否被添加到`list`中，这样一来空间复杂度为 $$O(N)$$, 查找的时间复杂度为 $$O(1)$$.

在`list.size() == nums.size()`时，已经找到需要的解，及时`return`避免后面不必要的`for`循环调用开销。

使用回溯法解题的**关键在于如何确定正确解及排除不符条件的解(剪枝)**。

