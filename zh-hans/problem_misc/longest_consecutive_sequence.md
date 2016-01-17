# Longest Consecutive Sequence

## Question

- leetcode: [Longest Consecutive Sequence | LeetCode OJ](https://leetcode.com/problems/longest-consecutive-sequence/)
- lintcode: [(124) Longest Consecutive Sequence](http://www.lintcode.com/en/problem/longest-consecutive-sequence/)


### Problem Statement

Given an unsorted array of integers, find the length of the longest
consecutive elements sequence.

#### Example

Given `[100, 4, 200, 1, 3, 2]`,
The longest consecutive elements sequence is `[1, 2, 3, 4]`. Return its
length: `4`.

#### Clarification

Your algorithm should run in O(_n_) complexity.


## 题解

首先看题要求，时间复杂度为 $$O(n)$$, 如果排序，基于比较的实现为 $$n \log n$$, 基数排序需要数据有特征。故排序无法达到复杂度要求。接下来可以联想空间换时间的做法，其中以哈希表为代表。这个题要求返回最长连续序列，不要求有序，非常符合哈希表的用法。**由于给定一个数其连续的数要么比它小1，要么大1，那么我们只需往左往右搜索知道在数组中找不到数为止。**结合哈希表查找为 $$O(1)$$ 的特性即可满足要求。

### Java

```java
public class Solution {
    /**
     * @param nums: A list of integers
     * @return an integer
     */
    public int longestConsecutive(int[] num) {
        if (num == null || num.length == 0) return 0;

        // add number to hashset
        Set<Integer> hashset = new HashSet<Integer>();
        for (int n : num) {
            hashset.add(n);
        }

        int lcs = 0;
        for (int n : num) {
            int i = n, count = 1;
            hashset.remove(n);
            // i--
            while (hashset.contains(--i)) {
                count++;
                hashset.remove(i);
            }
            // i++
            i = n;
            while (hashset.contains(++i)) {
                count++;
                hashset.remove(i);
            }
            // update lcs
            lcs = Math.max(lcs, count);
        }

        return lcs;
    }
}
```

### 源码分析

首先使用 HashSet 建哈希表，然后遍历数组，依次往左往右搜相邻数，搜到了就从 Set 中删除。末尾更新最大值。

### 复杂度分析

时间复杂度和空间复杂度均为 $$O(n)$$.
