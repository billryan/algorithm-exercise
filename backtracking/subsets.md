# Subsets - 子集

子集类问题类似Combination。

Question: [(17) Subsets](http://www.lintcode.com/en/problem/subsets/)

```
Given a set of distinct integers, return all possible subsets.

Note
Elements in a subset must be in non-descending order.

The solution set must not contain duplicate subsets.

Example
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```

#### 题解

1. 首先对数组按升序排序
2. 回溯法递归


**Java**
```java
class Solution {
    /**
     * @param S: A set of numbers.
     * @return: A list of lists. All valid subsets.
     */
    public ArrayList<ArrayList<Integer>> subsets(ArrayList<Integer> S) {

        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        if (S == null || S.size() == 0) {
            return result;
        }

        ArrayList<Integer> list = new ArrayList<Integer>();
        Collections.sort(S);
        backTrack(result, list, S, 0);
        return result;
    }

    private void backTrack(ArrayList<ArrayList<Integer>> result,
        ArrayList<Integer> list, ArrayList<Integer> num, int pos) {
        result.add(new ArrayList<Integer>(list));

        for (int i = pos; i < num.size(); i++) {
            list.add(num.get(i));
            backTrack(result, list, num, i + 1);
            list.remove(list.size() - 1);
        }
    }
}
```

**Notice: backTrack(result, list, num, i + 1);中的『i + 1』不可误写为『pos + 1』，第一次写subsets的时候在这坑了很久... :(**

回溯法可用图示和函数运行的堆栈图来理解，强烈建议**使用图形和递归的思想**分析，以数组`[1, 2, 3]`进行分析。下图所示为`list`及`result`动态变化的过程，箭头向下表示`list.add`及`result.add`操作，箭头向下表示`list.remove`操作。

![Subsets运行递归调用图](../figure/subsets.jpg)

如果你不相信以上的图形化分析，还可以自己在纸上分析代码的调用关系，下面以数组`[1,2]`为例分析回溯法的调用栈。

1. 首先由主函数 `subsets` 进入，初始化 `result` 为[]，接着进行异常处理，随后初始化 `list` 为[]，递归调用`backTrack()`, `num = [1, 2]`。
2. `result = [], list = [], pos = 0`. 调用`result.add()`加入[], `result = [[]]`。进入`for`循环，`num.size() = 2`。
    - `i = 0`,
        1. `list.add(num[0]) -> list = [1]`, 递归调用`backTrack()`前, `result = [[]], list = [1], pos = 1`
        2. 递归调用`backTrack([[]], [1], [1, 2]，1)`
            - `reslut.add[[1]] -> result = [[], [1]]`
            - `i = 1`, for(i = 1 < 2)
                1. `list.add(num[1]) -> list = [1, 2]`
                2. 递归调用`backTrack([[], [1]], [1, 2], [1, 2]，2)`
                    - `reslut.add[[1, 2]] -> result = [[], [1], [1, 2]]`
                    - `i = 2` 退出for循环，退出此次调用
                3. `list.remove(2 - 1) -> list = [1]`
                4. `i++ -> i = 2`
            - `i = 2`, 退出for循环，退出此次调用
        3. `list.remove() -> list = []`
        4. `i++ -> i = 1`，进入下一次循环
    - `i = 1`, for(i = 1 < 2)
        1. `list.add(num[1]) -> list = [2]`
        2. 递归调用`backTrack([[], [1], [1, 2]], [2], [1, 2]，2)`
            - `reslut.add[[2]] -> result = [[], [1], [1, 2], [2]]`
            - `i = 2` 退出for循环，退出此次调用
        3. `list.remove(1 - 1) -> list = []`
        4. `i++ -> i = 2`
    - `i = 2`, 退出for循环，退出此次调用
3. 返回结果`result`

**C++**
```c++
class Solution {
public:
    /**
     * @param S: A set of numbers.
     * @return: A list of lists. All valid subsets.
     */
    vector<vector<int> > subsets(vector<int> &nums) {
        vector<vector<int> > result;
    	if (nums.empty()) {
    	    return result;
    	}

    	vector<int> list;
    	backTrack(result, list, nums, 0);

    	return result;
    }

private:
    void backTrack(vector<vector<int> > &result, vector<int> &list, \
                   vector<int> &nums, int pos) {
        result.push_back(list);

        for (int i = pos; i != nums.size(); ++i) {
            list.push_back(nums[i]);
            backTrack(result, list, nums, i + 1);
            list.pop_back();
        }
    }
};
```

## Unique Subsets

Question: [(18) Unique Subsets](http://www.lintcode.com/en/problem/unique-subsets/)
```
Given a list of numbers that may has duplicate numbers, return all possible subsets

Note
Each element in a subset must be in non-descending order.

The ordering between two subsets is free.

The solution set must not contain duplicate subsets.

Example
If S = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
```

#### 题解

此题在上一题的基础上加了有重复元素的情况，因此需要对回溯函数进行一定的剪枝，对于排列组合的模板程序，剪枝通常可以从两个地方出发，一是在返回结果`result.add`之前进行剪枝，另一个则是在`list.add`处剪枝，具体使用哪一种需要视情况而定，哪种简单就选谁。

由于此题所给数组不一定有序，故首先需要排序。有重复元素对最终结果的影响在于重复元素最多只能出现`n`次(重复个数为n时)。具体分析过程如下(此分析过程改编自 [九章算法](http://www.jiuzhang.com))。

以 $$[1, 2_1, 2_2]$$ 为例，若不考虑重复，组合有 $$[], [1], [1, 2_1], [1, 2_1, 2_2], [1, 2_2], [2_1], [2_1, 2_2], [2_2]$$. 其中重复的有 $$[1, 2_2], [2_2]$$. 从中我们可以看出只能从重复元素的第一个持续往下添加到列表中，而不能取第二个或之后的重复元素。参考上一题Subsets的模板，能代表「重复元素的第一个」即为 for 循环中的`pos`变量，`i == pos`时，`i`处所代表的变量即为某一层遍历中得「第一个元素」，因此去重时只需判断`i != pos && s[i] == s[i - 1]`.

**C++**
```c++
class Solution {
public:
    /**
     * @param S: A set of numbers.
     * @return: A list of lists. All valid subsets.
     */
    vector<vector<int> > subsetsWithDup(const vector<int> &S) {
        vector<vector<int> > result;
        if (S.empty()) {
            return result;
        }

        vector<int> list;
        vector<int> source(S);
        sort(source.begin(), source.end());
        backtrack(result, list, source, 0);

        return result;
    }

private:
    void backtrack(vector<vector<int> > &ret, vector<int> &list,
              vector<int> &s, int pos) {

        ret.push_back(list);

        for (int i = pos; i != s.size(); ++i) {
            if (i != pos && s[i] == s[i - 1]) {
                continue;
            }
            list.push_back(s[i]);
            backtrack(ret, list, s, i + 1);
            list.pop_back();
        }
    }
};
```

## Reference - 参考

- [[NineChap 1.2] Permutation - Woodstock Blog](http://okckd.github.io/blog/2014/06/12/NineChap-Permutation/)
- [九章算法 - subsets模板](http://www.jiuzhang.com/solutions/subsets/)
- [LeetCode: Subsets 解题报告 - Yu's Garden - 博客园](http://www.cnblogs.com/yuzhangcmu/p/4211815.html)
- [九章算法 | Subsets II](http://www.jiuzhang.com/solutions/subsets-ii/)
