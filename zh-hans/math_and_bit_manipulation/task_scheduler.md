---
difficulty: Medium
tags:
- Queue
- Greedy
- Facebook
- Array
title: Task Scheduler
---

# Task Scheduler

## Problem

### Metadata

- tags: Queue, Greedy, Facebook, Array
- difficulty: Medium
- source(leetcode): <https://leetcode.com/problems/task-scheduler/>
- source(lintcode): <https://www.lintcode.com/problem/task-scheduler/>

### Description

Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval `n` that means between two `same tasks`, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the `least` number of intervals the CPU will take to finish all the given tasks.

#### Notice

1. The number of tasks is in the range `[1, 10000]`.
2. The integer n is in the range `[0, 100]`.

#### Example

Given tasks = `['A','A','A','B','B','B']`, n = `2`, return `8`.
```
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B.
```

## 题解 - 填充空闲时隙

TODO 分情况讨论

1. 出现频率最高的字符有多个
2. 以频率最高的字符为分界点，空闲时隙数不够所有字符放满
3. 空闲时隙数足够所有字符放下

### Java

```java
class Solution {
    public int leastInterval(char[] tasks, int n) {
        if (tasks == null) return -1;

        int[] map = new int[26];
        for (char c : tasks) {
            map[c - 'A']++;
        }
        Arrays.sort(map);

        int maxFreq = map[25];
        int idleSlots = n * (maxFreq - 1);
        for (int i = 24; i >= 0; i--) {
            if (map[i] == 0) {
                break;
            } else if (map[i] == maxFreq) {
                idleSlots -= maxFreq - 1;
            } else {
                idleSlots -= map[i];
            }
        }

        return idleSlots > 0 ? idleSlots + tasks.length : tasks.length;
    }
}
```

### 源码分析

此题的技巧性较强，由于出现的字符数仅为 A-Z 这26个字符，而且我们需要先进行排序，这种特殊情形的排序往往不能使用通用排序方法，我们使用数组映射再进行排序。

### 复杂度分析

空间复杂度 $$O(26)$$ ==> $$O(1)$$, 时间复杂度最坏情况下遍历26个元素，故为 $$O(1)$$.

## Reference

[Task Scheduler - Approach #3 Calculating Idle slots](https://leetcode.com/problems/task-scheduler/solution/)