# Permutations

## Source

- leetcode: [Permutations | LeetCode OJ](https://leetcode.com/problems/permutations/)
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

## 题解1 - Recursion(using subsets template)

排列常见的有数字全排列，字符串排列等。

使用之前 [Subsets](http://algorithm.yuanbin.me/exhaustive_search/subsets.html) 的模板，但是在取结果时只能取`list.size() == nums.size()`的解，且在添加list元素的时候需要注意除重以满足全排列的要求。此题假设前提为输入数据中无重复元素。

### Python

```python
class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        alist = []
        result = [];
        if not nums:
            return result

        self.helper(nums, alist, result)

        return result

    def helper(self, nums, alist, ret):
        if len(alist) == len(nums):
            # new object
            ret.append([] + alist)
            return

        for i, item in enumerate(nums):
            if item not in alist:
                alist.append(item)
                self.helper(nums, alist, ret)
                alist.pop()

```

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

### Java

```java
class Solution {
    /**
     * @param nums: A list of integers.
     * @return: A list of permutations.
     */
    public ArrayList<ArrayList<Integer>> permute(ArrayList<Integer> nums) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        ArrayList<Integer> list = new ArrayList<Integer>();

        if (nums == null || nums.isEmpty()) return result;

        helper(nums, list, result);

        return result;
    }

    private void helper(ArrayList<Integer> nums, ArrayList<Integer> list,
                        ArrayList<ArrayList<Integer>> ret
                        ) {

        if (list.size() == nums.size()) {
            ret.add(new ArrayList<Integer>(list));
            return;
        }

        for (int i = 0; i < nums.size(); i++) {
            if (list.contains(nums.get(i))) continue;

            list.add(nums.get(i));
            helper(nums, list, ret);
            list.remove(list.size() - 1);
        }
    }
}
```

### 源码分析

在除重时使用了标准库`find`(不可使用时间复杂度更低的`binary_search`，因为`list`中元素不一定有序)，时间复杂度为 $$O(N)$$, 也可使用`hashmap`记录`nums`中每个元素是否被添加到`list`中，这样一来空间复杂度为 $$O(N)$$, 查找的时间复杂度为 $$O(1)$$.

在`list.size() == nums.size()`时，已经找到需要的解，及时`return`避免后面不必要的`for`循环调用开销。

使用回溯法解题的**关键在于如何确定正确解及排除不符条件的解(剪枝)**。

### 复杂度分析

以状态数来分析，最终全排列个数应为 $$n!$$, 每个节点被遍历的次数为 $$(n-1)!$$, 故节点共被遍历的状态数为 $$O(n!)$$, 此为时间复杂度的下界，因为这里只算了合法条件下的遍历状态数。若不对 list 中是否包含 nums[i] 进行检查，则总的状态数应为 $$n^n$$ 种。

由于最终的排列结果中每个列表的长度都为 n, 各列表的相同元素并不共享，故时间复杂度的下界为 $$O(n \cdot n!)$$, 上界为 $$n \cdot n^n$$. 实测`helper`中 for 循环的遍历次数在 $$O(2n \cdot n!)$$ 以下，注意这里的时间复杂度并不考虑查找列表里是否包含重复元素。

## 题解2 - Recursion

与题解1基于 subsets 的模板不同，这里我们直接从全排列的数学定义本身出发，要求给定数组的全排列，可将其模拟为某个袋子里有编号为1到 n 的球，将其放入 n 个不同的盒子怎么放？基本思路就是从袋子里逐个拿球放入盒子，直到袋子里的球拿完为止，拿完时即为一种放法。

### Python

```python
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        if nums is None:
            return [[]]
        elif len(nums) <= 1:
            return [nums]

        result = []
        for i, item in enumerate(nums):
            for p in self.permute(nums[:i] + nums[i + 1:]):
                result.append(p + [item])

        return result
```

### C++

```c++
class Solution {
public:
    /**
     * @param nums: A list of integers.
     * @return: A list of permutations.
     */
    vector<vector<int> > permute(vector<int>& nums) {
        vector<vector<int> > result;

        if (nums.size() == 1) {
            result.push_back(nums);
            return result;
        }

        for (int i = 0; i < nums.size(); ++i) {
            vector<int> nums_new = nums;
            nums_new.erase(nums_new.begin() + i);

            vector<vector<int> > res_tmp = permute(nums_new);
            for (int j = 0; j < res_tmp.size(); ++j) {
                vector<int> temp = res_tmp[j];
                temp.push_back(nums[i]);
                result.push_back(temp);
            }
        }

        return result;
    }
};
```

### Java

```java
public class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> numsList = new ArrayList<Integer>();

        if (nums == null) {
            return result;
        } else {
            // convert int[] to List<Integer>
            for (int item : nums) numsList.add(item);
        }

        if (nums.length <= 1) {
            result.add(numsList);
            return result;
        }

        for (int i = 0; i < nums.length; i++) {
            int[] numsNew = new int[nums.length - 1];
            System.arraycopy(nums, 0, numsNew, 0, i);
            System.arraycopy(nums, i + 1, numsNew, i, nums.length - i - 1);

            List<List<Integer>> resTemp = permute(numsNew);
            for (List<Integer> temp : resTemp) {
                temp.add(nums[i]);
                result.add(temp);
            }
        }

        return result;
    }
}
```

### 源码分析

Python 中使用`len()`时需要防止`None`, 递归终止条件为数组中仅剩一个元素或者为空，否则遍历`nums`数组，取出第`i`个元素并将其加入至最终结果。`nums[:i] + nums[i + 1:]`即为去掉第`i`个元素后的新列表。

Java 中 ArrayList 和 List 的类型转换需要特别注意。

### 复杂度分析

由于取的结果都是最终结果，无需去重判断，故时间复杂度为 $$O(n!)$$, 但是由于`nums[:i] + nums[i + 1:]`会产生新的列表，实际运行会比第一种方法慢不少。

## 题解3 - Iteration

递归版的程序比较简单，咱们来个迭代的实现。

**TBD**

## Reference

- [Programming Interview Questions 11: All Permutations of String | Arden DertatArden Dertat](http://www.ardendertat.com/2011/10/28/programming-interview-questions-11-all-permutations-of-string/)
- [algorithm - complexity of recursive string permutation function - Stack Overflow](http://stackoverflow.com/questions/5363619/complexity-of-recursive-string-permutation-function)
- [[leetcode]Permutations @ Python - 南郭子綦 - 博客园](http://www.cnblogs.com/zuoyuan/p/3758816.html)
- [[leetcode] permutations的讨论 - tuantuanls的专栏 - 博客频道 - CSDN.NET](http://blog.csdn.net/tuantuanls/article/details/8717262)
- [非递归排列算法（Permutation Generation）](http://arieshout.me/2012/04/non-recursive-permutation-generation.html)
- [闲谈permutations | HelloYou](http://helloyou2012.me/?p=133)
- [9.7. itertools — Functions creating iterators for efficient looping — Python 2.7.10 documentation](https://docs.python.org/2/library/itertools.html#itertools.permutations)
