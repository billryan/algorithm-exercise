# Combination Sum II

## Question

- leetcode: [Combination Sum II | LeetCode OJ](https://leetcode.com/problems/combination-sum-ii/)
- lintcode: [(153) Combination Sum II](http://www.lintcode.com/en/problem/combination-sum-ii/)

```
Given a collection of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.
Each number in C may only be used once in the combination.

Have you met this question in a real interview? Yes
Example
For example, given candidate set 10,1,6,7,2,1,5 and target 8,

A solution set is:

[1,7]

[1,2,5]

[2,6]

[1,1,6]

Note
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order.
(ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
```

## 题解

和 [Unique Subsets](http://algorithm.yuanbin.me/zh-hans/exhaustive_search/unique_subsets.html) 非常类似。在 [Combination Sum](http://algorithm.yuanbin.me/zh-hans/exhaustive_search/combination_sum.html) 的基础上改改就好了。

### Java

```java
public class Solution {
    /**
     * @param num: Given the candidate numbers
     * @param target: Given the target number
     * @return: All the combinations that sum to target
     */
    public List<List<Integer>> combinationSum2(int[] num, int target) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> list = new ArrayList<Integer>();
        if (num == null) return result;

        Arrays.sort(num);
        helper(num, 0, target, list, result);

        return result;
    }

    private void helper(int[] nums, int pos, int gap,
                        List<Integer> list, List<List<Integer>> result) {

        if (gap == 0) {
            result.add(new ArrayList<Integer>(list));
            return;
        }

        for (int i = pos; i < nums.length; i++) {
            // ensure only the first same num is chosen, remove duplicate list
            if (i != pos && nums[i] == nums[i - 1]) {
                continue;
            }
            // cut invalid num
            if (gap < nums[i]) {
                return;
            }
            list.add(nums[i]);
            // i + 1 ==> only be used once
            helper(nums, i + 1, gap - nums[i], list, result);
            list.remove(list.size() - 1);
        }
    }
}
```

### 源码分析

这里去重的方法继承了 Unique Subsets 中的做法，当然也可以新建一变量 `prev`，由于这里每个数最多只能使用一次，故递归时索引变量传`i + 1`.

### 复杂度分析

时间复杂度 $$O(n)$$, 空间复杂度 $$O(n)$$.
