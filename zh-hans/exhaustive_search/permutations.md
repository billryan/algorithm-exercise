# Permutations

## Question

- leetcode: [Permutations | LeetCode OJ](https://leetcode.com/problems/permutations/)
- lintcode: [(15) Permutations](http://www.lintcode.com/en/problem/permutations/)

### Problem Statement

Given a list of numbers, return all possible permutations.

#### Example

For nums = `[1,2,3]`, the permutations are:



    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]


#### Challenge

Do it without recursion.



## 题解1 - Recursion(using subsets template)

排列常见的有数字全排列，字符串排列等。

使用之前 [Subsets](http://algorithm.yuanbin.me/zh-hans/exhaustive_search/subsets.html) 的模板，但是在取结果时只能取`list.size() == nums.size()`的解，且在添加list元素的时候需要注意除重以满足全排列的要求。此题假设前提为输入数据中无重复元素。

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
public class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if (nums == null || nums.length == 0) return result;

        List<Integer> list = new ArrayList<Integer>();
        dfs(nums, list, result);

        return result;
    }

    private void dfs(int[] nums, List<Integer> list, List<List<Integer>> result) {
        if (list.size() == nums.length) {
            result.add(new ArrayList<Integer>(list));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (list.contains(nums[i])) continue;
            list.add(nums[i]);
            dfs(nums, list, result);
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

class Solution2:
    # 类似 subset的模版
    def permute(self, nums):
        if not nums:
            return []
        res = []
        self.helper(sorted(nums), res, [])
        return res

    def helper(self, nums, res, tmp):
        if not nums:
            res.append(tmp[:])
            return
        for i, num in enumerate(nums, 1):
            self.helper(nums[:i] + nums[i + 1:], res, tmp + [num])
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

递归版的程序比较简单，咱们来个迭代的实现。非递归版的实现也有好几种，这里基于 C++ STL 中`next_permutation`的字典序实现方法。参考 Wikipedia 上的字典序算法，大致步骤如下：

1. 从后往前寻找索引满足 `a[k] < a[k + 1]`, 如果此条件不满足，则说明已遍历到最后一个。
2. 从后往前遍历，找到第一个比`a[k]`大的数`a[l]`, 即`a[k] < a[l]`.
3. 交换`a[k]`与`a[l]`.
4. 反转`k + 1 ~ n`之间的元素。

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

        # sort nums first
        nums.sort()

        result = []
        while True:
            result.append([] + nums)
            # step1: find nums[i] < nums[i + 1], Loop backwards
            i = 0
            for i in xrange(len(nums) - 2, -1, -1):
                if nums[i] < nums[i + 1]:
                    break
                elif i == 0:
                    return result
            # step2: find nums[i] < nums[j], Loop backwards
            j = 0
            for j in xrange(len(nums) - 1, i, -1):
                if nums[i] < nums[j]:
                    break
            # step3: swap betwenn nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]
            # step4: reverse between [i + 1, n - 1]
            nums[i + 1:len(nums)] = nums[len(nums) - 1:i:-1]

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
    	if (nums.empty() || nums.size() <= 1) {
    	    result.push_back(nums);
    	    return result;
    	}

        // sort nums first
        sort(nums.begin(), nums.end());
        for (;;) {
            result.push_back(nums);

            // step1: find nums[i] < nums[i + 1]
            int i = 0;
            for (i = nums.size() - 2; i >= 0; --i) {
                if (nums[i] < nums[i + 1]) {
                    break;
                } else if (0 == i) {
                    return result;
                }
            }

            // step2: find nums[i] < nums[j]
            int j = 0;
            for (j = nums.size() - 1; j > i; --j) {
                if (nums[i] < nums[j]) break;
            }

            // step3: swap betwenn nums[i] and nums[j]
            int temp = nums[j];
            nums[j] = nums[i];
            nums[i] = temp;

            // step4: reverse between [i + 1, n - 1]
            reverse(nums, i + 1, nums.size() - 1);
        }
    	return result;
    }

private:
    void reverse(vector<int>& nums, int start, int end) {
        for (int i = start, j = end; i < j; ++i, --j) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }
};
```

### Java - Array

```java
class Solution {
    /**
     * @param nums: A list of integers.
     * @return: A list of permutations.
     */
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if (nums == null || nums.length == 0) return result;

        // deep copy(do not change nums)
        int[] perm = Arrays.copyOf(nums, nums.length);
        // sort first!!!
        Arrays.sort(perm);

        while (true) {
            // step0: add perm into result
            List<Integer> tempList = new ArrayList<Integer>();
            for (int i : perm) tempList.add(i);
            result.add(tempList);

            // step1: search the first perm[k] < perm[k+1] backward
            int k = -1;
            for (int i = perm.length - 2; i >= 0; i--) {
                if (perm[i] < perm[i + 1]) {
                    k = i;
                    break;
                }
            }
            // if current rank is the largest, exit while loop
            if (k == -1) break;

            // step2: search the first perm[k] < perm[l] backward
            int l = perm.length - 1;
            while (l > k && perm[l] <= perm[k]) l--;

            // step3: swap perm[k] with perm[l]
            int temp = perm[k];
            perm[k] = perm[l];
            perm[l] = temp;

            // step4: reverse between k+1 and perm.length-1;
            reverse(perm, k + 1, perm.length - 1);
        }

        return result;
    }

    private void reverse(int[] nums, int lb, int ub) {
        for (int i = lb, j = ub; i < j; i++, j--) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }
}
```

### Java - List

```java
class Solution {
    /**
     * @param nums: A list of integers.
     * @return: A list of permutations.
     */
    public ArrayList<ArrayList<Integer>> permute(ArrayList<Integer> nums) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        if (nums == null || nums.size() == 0) return result;

        // deep copy(do not change nums)
        List<Integer> perm = new ArrayList<Integer>(nums);
        // sort first!!!
        Collections.sort(perm);

        while (true) {
            // step0: add perm into result
            result.add(new ArrayList<Integer>(perm));

            // step1: search the first num[k] < num[k+1] backward
            int k = -1;
            for (int i = perm.size() - 2; i >= 0; i--) {
                if (perm.get(i) < perm.get(i + 1)) {
                    k = i;
                    break;
                }
            }
            // if current rank is the largest, exit while loop
            if (k == -1) break;

            // step2: search the first perm[k] < perm[l] backward
            int l = perm.size() - 1;
            while (l > k && perm.get(l) <= perm.get(k)) l--;

            // step3: swap perm[k] with perm[l]
            Collections.swap(perm, k, l);

            // step4: reverse between k+1 and perm.size()-1;
            reverse(perm, k + 1, perm.size() - 1);
        }

        return result;
    }

    private void reverse(List<Integer> nums, int lb, int ub) {
        for (int i = lb, j = ub; i < j; i++, j--) {
            Collections.swap(nums, i, j);
        }
    }
}
```

### 源码分析

注意好字典序算法的步骤即可，对于 Java 来说其实可以首先将数组转化为 List, 相应的方法多一些。吐槽下 Lintcode 上的接口设计，总是见到一长串的`ArrayList`, 个人觉得采用 Leetcode 上的`List`更灵活（代码更短，哈哈），不知道 Lintcode 那样的接口设计有什么其他考虑吗？

### 复杂度分析

除了将 $$n!$$ 个元素添加至最终结果外，首先对元素排序，时间复杂度近似为 $$O(n \log n)$$, 反转操作近似为 $$O(n)$$, 故总的时间复杂度为 $$O(n!)$$. 除了保存结果的`result`外，其他空间可忽略不计，所以此题用生成器来实现较为高效，扩展题可见底下的 Python itertools 中的实现，从 n 个元素中选出 m 个进行全排列。

## Reference

- [Permutation Generation](http://7xojrx.com1.z0.glb.clouddn.com/docs/algorithm-exercise/docs/permutation_generation.pdf) - Robert Sedgewick 的大作，总结了诸多 Permutation 的产生方法。
- [Next lexicographical permutation algorithm](http://www.nayuki.io/page/next-lexicographical-permutation-algorithm) - 此题非递归方法更为详细的解释。
- [Permutation - Wikipedia, the free encyclopedia](https://en.wikipedia.org/wiki/Permutation#Generation_in_lexicographic_order) - 字典序实现。
- [Programming Interview Questions 11: All Permutations of String | Arden DertatArden Dertat](http://www.ardendertat.com/2011/10/28/programming-interview-questions-11-all-permutations-of-string/)
- [algorithm - complexity of recursive string permutation function - Stack Overflow](http://stackoverflow.com/questions/5363619/complexity-of-recursive-string-permutation-function)
- [[leetcode]Permutations @ Python - 南郭子綦 - 博客园](http://www.cnblogs.com/zuoyuan/p/3758816.html)
- [[leetcode] permutations的讨论 - tuantuanls的专栏 - 博客频道 - CSDN.NET](http://blog.csdn.net/tuantuanls/article/details/8717262)
- [非递归排列算法（Permutation Generation）](http://arieshout.me/2012/04/non-recursive-permutation-generation.html)
- [闲谈permutations | HelloYou](http://helloyou2012.me/?p=133)
- [9.7. itertools — Functions creating iterators for efficient looping — Python 2.7.10 documentation](https://docs.python.org/2/library/itertools.html#itertools.permutations)
