# Merge Intervals

## Question

- leetcode: [Merge Intervals | LeetCode OJ](https://leetcode.com/problems/merge-intervals/)
- lintcode: [(156) Merge Intervals](http://www.lintcode.com/en/problem/merge-intervals/)

### Problem Statement

Given a collection of intervals, merge all overlapping intervals.

#### Example

Given intervals => merged intervals:

```
[                     [
  [1, 3],               [1, 6],
  [2, 6],      =>       [8, 10],
  [8, 10],              [15, 18]
  [15, 18]            ]
]
```

#### Challenge

O(n log n) time and O(1) extra space.

## 题解1 - 排序后

初次接触这道题可能会先对 interval 排序，随后考虑相邻两个 interval 的 end 和 start 是否交叉，若交叉则合并之。

### Java

```java
/**
 * Definition of Interval:
 * public class Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 */

class Solution {
    /**
     * @param intervals: Sorted interval list.
     * @return: A new sorted interval list.
     */
    public List<Interval> merge(List<Interval> intervals) {
        if (intervals == null || intervals.isEmpty()) return intervals;

        List<Interval> result = new ArrayList<Interval>();
        // sort with Comparator
        Collections.sort(intervals, new IntervalComparator());
        Interval prev = intervals.get(0);
        for (Interval interval : intervals) {
            if (prev.end < interval.start) {
                result.add(prev);
                prev = interval;
            } else {
                prev.start = Math.min(prev.start, interval.start);
                prev.end = Math.max(prev.end, interval.end);
            }
        }
        result.add(prev);

        return result;
    }

    private class IntervalComparator implements Comparator<Interval> {
        public int compare(Interval a, Interval b) {
            return a.start - b.start;
        }
    }

}
```

### 源码分析

这里因为需要比较 interval 的 start, 所以需要自己实现 Comparator 接口并覆盖 compare 方法。这里取 prev 为前一个 interval。最后不要忘记加上 prev.

### 复杂度分析

排序 $$O(n \log n)$$, 遍历 $$O(n)$$, 所以总的时间复杂度为 $$O(n \log n)$$. 空间复杂度 $$O(1)$$.

## 题解2 - 插入排序

除了首先对 intervals 排序外，还可以使用类似插入排序的方法，插入的方法在题 [Insert Interval ](http://algorithm.yuanbin.me/zh-hans/problem_misc/insert_interval.html) 中已详述。这里将 result 作为 intervals 传进去即可，新插入的 interval 为 intervals 遍历得到的结果。

### Java

```java
/**
 * Definition of Interval:
 * public class Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 */

class Solution {
    /**
     * @param intervals: Sorted interval list.
     * @return: A new sorted interval list.
     */
    public List<Interval> merge(List<Interval> intervals) {
        if (intervals == null || intervals.isEmpty()) return intervals;

        List<Interval> result = new ArrayList<Interval>();
        for (Interval interval : intervals) {
            result = insert(result, interval);
        }

        return result;
    }

    private List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        List<Interval> result = new ArrayList<Interval>();
        int insertPos = 0;
        for (Interval interval : intervals) {
            if (newInterval.end < interval.start) {
                result.add(interval);
            } else if (newInterval.start > interval.end) {
                result.add(interval);
                insertPos++;
            } else {
                newInterval.start = Math.min(newInterval.start, interval.start);
                newInterval.end = Math.max(newInterval.end, interval.end);
            }
        }
        result.add(insertPos, newInterval);

        return result;
    }
}
```

### 源码分析

关键在 insert 的理解，`result = insert(result, interval);`作为迭代生成新的 result.

### 复杂度分析

每次添加新的 interval 都是线性时间复杂度，故总的时间复杂度为 $$O(1 + 2 + ... + n) = O(n^2)$$. 空间复杂度为 $$O(n)$$.

## Reference

- [Merge Intervals 参考程序 Java/C++/Python](http://www.jiuzhang.com/solutions/merge-intervals/)
- Soulmachine 的 leetcode 题解
