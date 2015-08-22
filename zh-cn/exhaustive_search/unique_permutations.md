# Unique Permutations

## Source

- lintcode: [(16) Unique Permutations](http://www.lintcode.com/en/problem/unique-permutations/)

```
Given a list of numbers with duplicate number in it. Find all unique permutations.

Example
For numbers [1,2,2] the unique permutations are:

[

    [1,2,2],

    [2,1,2],

    [2,2,1]

]

Challenge
Do it without recursion.
```

## 题解

在上题的基础上进行剪枝，剪枝的过程和 [Subsets | Algorithm](http://algorithm.yuanbin.me/zh-cn/backtracking/subsets.html) 中的 Unique Subsets 一题极为相似。为了便于分析，我们可以先分析简单的例子，以 $$[1, 2_1, 2_2]$$ 为例。按照上题 Permutations 的解法，我们可以得到如下全排列。

1. $$[1, 2_1, 2_2]$$
2. $$[1, 2_2, 2_1]$$
3. $$[2_1, 1, 2_2]$$
4. $$[2_1, 2_2, 1]$$
5. $$[2_2, 1, 2_1]$$
6. $$[2_2, 2_1, 1]$$

从以上结果我们注意到`1`和`2`重复，`5`和`3`重复，`6`和`4`重复，从重复的解我们可以发现其共同特征均是第二个 $$2_2$$ 在前，而第一个 $$2_1$$ 在后，因此我们的**剪枝方法为：对于有相同的元素来说，我们只取不重复的一次。**嗯，这样说还是有点模糊，下面以 $$[1, 2_1, 2_2]$$ 和 $$[1, 2_2, 2_1]$$ 进行说明。

首先可以确定 $$[1, 2_1, 2_2]$$ 是我们要的一个解，此时`list`为  $$[1, 2_1, 2_2]$$, 经过两次`list.pop_back()`之后，`list`为 $$[1]$$, 如果不进行剪枝，那么接下来要加入`list`的将为 $$2_2$$, 那么我们剪枝要做的就是避免将 $$2_2$$ 加入到`list`中，如何才能做到这一点呢？我们仍然从上述例子出发进行分析，在第一次加入 $$2_2$$ 时，相对应的`visited[1]`为`true`(对应 $$2_1$$)，而在第二次加入 $$2_2$$ 时，相对应的`visited[1]`为`false`，因为在`list`为 $$[1, 2_1]$$ 时，执行`list.pop_back()`后即置为`false`。

一句话总结即为：在遇到当前元素和前一个元素相等时，如果前一个元素`visited[i - 1] == false`,  那么我们就跳过当前元素并进入下一次循环，这就是剪枝的关键所在。另一点需要特别注意的是这种剪枝的方法能使用的前提是提供的`nums`是有序数组，否则无效。

### C++

```c++
class Solution {
public:
    /**
     * @param nums: A list of integers.
     * @return: A list of unique permutations.
     */
    vector<vector<int> > permuteUnique(vector<int> &nums) {
        vector<vector<int> > ret;
        if (nums.empty()) {
            return ret;
        }

        // important! sort before call `backTrack`
        sort(nums.begin(), nums.end());
        vector<bool> visited(nums.size(), false);
        vector<int> list;
        backTrack(ret, list, visited, nums);

        return ret;
    }

private:
    void backTrack(vector<vector<int> > &result, vector<int> &list, \
                   vector<bool> &visited, vector<int> &nums) {
        if (list.size() == nums.size()) {
            result.push_back(list);
            // avoid unnecessary call for `for loop`, but not essential
            return;
        }

        for (int i = 0; i != nums.size(); ++i) {
            if (visited[i] || (i != 0 && nums[i] == nums[i - 1] \
                && !visited[i - 1])) {
                continue;
            }
            visited[i] = true;
            list.push_back(nums[i]);
            backTrack(result, list, visited, nums);
            list.pop_back();
            visited[i] = false;
        }
    }
};
```

### 源码分析

Unique Subsets 和 Unique Permutations 的源码模板非常经典！建议仔细研读并体会其中奥义。

后记：在理解 Unique Subsets 和 Unique Permutations 的模板我花了差不多一整天时间才基本理解透彻，建议在想不清楚某些问题时先分析简单的问题，在纸上一步一步分析直至理解完全。

## Reference

- [Permutation II | 九章算法](http://www.jiuzhang.com/solutions/permutations-ii/)
