# Unique Subsets

## Question

- leetcode: [Subsets II | LeetCode OJ](https://leetcode.com/problems/subsets-ii/)
- lintcode: [(18) Unique Subsets](http://www.lintcode.com/en/problem/subsets-ii/)

### Problem Statement

Given a list of numbers that may has duplicate numbers, return all possible subsets.

#### Example

If **_S_** = `[1,2,2]`, a solution is:

    
    
    [
      [2],
      [1],
      [1,2,2],
      [2,2],
      [1,2],
      []
    ]

#### Note

Each element in a subset must be in **non-descending **order.
The ordering between two subsets is free.
The solution set must not contain duplicate subsets.

## 题解

此题在上一题的基础上加了有重复元素的情况，因此需要对回溯函数进行一定的剪枝，对于排列组合的模板程序，剪枝通常可以从两个地方出发，一是在返回结果`result.add`之前进行剪枝，另一个则是在`list.add`处剪枝，具体使用哪一种需要视情况而定，哪种简单就选谁。

由于此题所给数组不一定有序，故首先需要排序。有重复元素对最终结果的影响在于重复元素最多只能出现`n`次(重复个数为n时)。具体分析过程如下(此分析过程改编自 [九章算法](http://www.jiuzhang.com))。

以 $$[1, 2_1, 2_2]$$ 为例，若不考虑重复，组合有 $$[], [1], [1, 2_1], [1, 2_1, 2_2], [1, 2_2], [2_1], [2_1, 2_2], [2_2]$$. 其中重复的有 $$[1, 2_2], [2_2]$$. 从中我们可以看出只能从重复元素的第一个持续往下添加到列表中，而不能取第二个或之后的重复元素。参考上一题Subsets的模板，能代表「重复元素的第一个」即为 for 循环中的`pos`变量，`i == pos`时，`i`处所代表的变量即为某一层遍历中得「第一个元素」，因此去重时只需判断`i != pos && s[i] == s[i - 1]`(不是 i + 1, 可能索引越界，而i 不等于 pos 已经能保证 i >= 1).

### C++

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

### Java

```java
class Solution {
    /**
     * @param S: A set of numbers.
     * @return: A list of lists. All valid subsets.
     */
    public ArrayList<ArrayList<Integer>> subsetsWithDup(ArrayList<Integer> S) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
        if (S == null) return result;
        // 
        Collections.sort(S);
        List<Integer> list = new ArrayList<Integer>();
        dfs(S, 0, list, result);
        return result;
    }
    
    private void dfs(ArrayList<Integer> S, int pos, List<Integer> list, 
                     ArrayList<ArrayList<Integer>> result) {
        
        result.add(new ArrayList<Integer>(list));
        for (int i = pos; i < S.size(); i++) {
            // exlude duplicate
            if (i != pos && S.get(i) == S.get(i - 1)) {
                continue;
            }
            list.add(S.get(i));
            dfs(S, i + 1, list, result);
            list.remove(list.size() - 1);
        }
    }
}
```

### 源码分析

相比前一道题多了去重的判断。

### 复杂度分析

和前一道题差不多，最坏情况下时间复杂度为 $$2^n$$. 空间复杂度为 $$O(n)$$.

## Reference

- [Subsets II | 九章算法](http://www.jiuzhang.com/solutions/subsets-ii/)
