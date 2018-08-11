---
difficulty: Medium
tags:
- Priority Queue
- Heap
title: Top k Largest Numbers
---

# Top k Largest Numbers

## Problem

### Metadata

- tags: Priority Queue, Heap
- difficulty: Medium
- source(lintcode): <https://www.lintcode.com/problem/top-k-largest-numbers/>

### Description

Given an integer array, find the top *k* largest numbers in it.

#### Example

Given `[3,10,1000,-99,4,100]` and *k* = `3`.
Return `[1000, 100, 10]`.

## 题解

简单题，使用堆即可。

### Java

```java
public class Solution {
    /**
     * @param nums: an integer array
     * @param k: An integer
     * @return: the top k largest numbers in array
     */
    public int[] topk(int[] nums, int k) {
        if (nums == null || nums.length <= 1) return nums;

        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(nums.length, Collections.reverseOrder());
        for (int num : nums) {
            pq.offer(num);
        }

        int[] maxK = new int[k];
        for (int i = 0; i < k; i++) {
            maxK[i] = pq.poll();
        }

        return maxK;
    }
}
```

### 源码分析

略

### 复杂度分析

略