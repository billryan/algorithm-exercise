# Combinations

## Question

- leetcode: [Combinations | LeetCode OJ](https://leetcode.com/problems/combinations/)
- lintcode: [(152) Combinations](http://www.lintcode.com/en/problem/combinations/)

### Problem Statement

Given two integers n and k,
return all possible combinations of k numbers out of 1 ... n.

#### Example

For example,
If n = 4 and k = 2, a solution is:
`[[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]`

## 题解

套用 [Permutations](http://algorithm.yuanbin.me/zh-hans/exhaustive_search/permutations.html) 模板。

### Java

```java
public class Solution {
    public List<List<Integer>> combine(int n, int k) {
        assert(n >= 1 && n >= k && k >= 1);
        
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> list = new ArrayList<Integer>();
        dfs(n, k, 1, list, result);
        
        return result;
    }
    
    private void dfs(int n, int k, int pos, List<Integer> list,
                     List<List<Integer>> result) {
        
        if (list.size() == k) {
            result.add(new ArrayList<Integer>(list));
            return;
        }
        for (int i = pos; i <= n; i++) {
            list.add(i);
            dfs(n, k, i + 1, list, result);
            list.remove(list.size() - 1);
        }
    }
}
```

### 源码分析

注意递归`helper(n, k, i + 1, list, result);`中的`i + 1`，不是`pos + 1`。

### 复杂度分析

状态数 $$C_n^2$$, 每组解有两个元素，故时间复杂度应为 $$O(n^2)$$. list 只保留最多两个元素，空间复杂度 $$O(1)$$.
