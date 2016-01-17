# Combination Sum

## Question

- leetcode: [Combination Sum | LeetCode OJ](https://leetcode.com/problems/combination-sum/)
- lintcode: [(135) Combination Sum](http://www.lintcode.com/en/problem/combination-sum/)

```
Given a set of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.
The same repeated number may be chosen from C unlimited number of times.

For example, given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]

Have you met this question in a real interview? Yes
Example
given candidate set 2,3,6,7 and target 7,
A solution set is:
[7]
[2, 2, 3]

Note
- All numbers (including target) will be positive integers.
- Elements in a combination (a1, a2, … , ak) must be in non-descending order.
(ie, a1 ≤ a2 ≤ … ≤ ak).
- The solution set must not contain duplicate combinations.
```

## 题解

和 [Permutations](http://algorithm.yuanbin.me/zh-hans/exhaustive_search/permutations.html) 十分类似，区别在于剪枝函数不同。这里允许一个元素被多次使用，故递归时传入的索引值不自增，而是由 for 循环改变。

### Java

```java
public class Solution {
    /**
     * @param candidates: A list of integers
     * @param target:An integer
     * @return: A list of lists of integers
     */
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> list = new ArrayList<Integer>();
        if (candidates == null) return result;

        Arrays.sort(candidates);
        helper(candidates, 0, target, list, result);

        return result;
    }

    private void helper(int[] candidates, int pos, int gap,
                        List<Integer> list, List<List<Integer>> result) {

        if (gap == 0) {
            // add new object for result
            result.add(new ArrayList<Integer>(list));
            return;
        }

        for (int i = pos; i < candidates.length; i++) {
            // cut invalid candidate
            if (gap < candidates[i]) {
                return;
            }
            list.add(candidates[i]);
            helper(candidates, i, gap - candidates[i], list, result);
            list.remove(list.size() - 1);
        }
    }
}
```

### 源码分析

对数组首先进行排序是必须的，递归函数中本应该传入 target 作为入口参数，这里借用了 Soulmachine 的实现，使用 gap 更容易理解。注意在将临时 list 添加至 result 中时需要 new 一个新的对象。

### 复杂度分析

按状态数进行分析，时间复杂度 $$O(n!)$$, 使用了list 保存中间结果，空间复杂度 $$O(n)$$.

## Reference

- Soulmachine 的 leetcode 题解
