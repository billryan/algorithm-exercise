# Longest Consecutive Sequence

Tags: Array, Union Find, Hard

## Question

- leetcode: [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)
- lintcode: [Longest Consecutive Sequence](https://www.lintcode.com/problem/longest-consecutive-sequence/)

### Problem Statement

Given an unsorted array of integers, find the length of the longest
consecutive elements sequence.

Your algorithm should run in O(_n_) complexity.

**Example:**
    
    
    
    **Input:** [100, 4, 200, 1, 3, 2]
    **Output:** 4
    **Explanation:** The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

## 题解

首先看题要求，时间复杂度为 $$O(n)$$, 如果排序，基于比较的实现为 $$n \log n$$, 基数排序需要数据有特征。故排序无法达到复杂度要求。接下来可以联想空间换时间的做法，其中以哈希表为代表。这个题要求返回最长连续序列，不要求有序，非常符合哈希表的用法。**由于给定一个数其连续的数要么比它小1，要么大1，那么我们只需往左往右搜索知道在数组中找不到数为止。**结合哈希表查找为 $$O(1)$$ 的特性即可满足要求。

### Java

```java
class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length <= 0) return 0;
        Set<Integer> sets = new HashSet<>(nums.length);
        for (int num : nums) {
            sets.add(num);
        }

        int result = 1;
        for (int num : nums) {
            int seq = 1;
            int right = num, left = num;
            // right
            while (sets.contains(++right)) {
                seq++;
                sets.remove(right);
            }
            // left
            while (sets.contains(--left)) {
                seq++;
                sets.remove(left);
            }
            sets.remove(num);
            if (seq > result) result = seq;
        }

        return result;
    }
}
```

### 源码分析

首先使用 HashSet 建哈希表，然后遍历数组，依次往左往右搜相邻数，搜到了就从 Set 中删除。末尾更新最大值。

### 复杂度分析

时间复杂度和空间复杂度均为 $$O(n)$$.
