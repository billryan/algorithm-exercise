# Insert Interval

## Question

- leetcode: [Insert Interval | LeetCode OJ](https://leetcode.com/problems/insert-interval/)
- lintcode: [(30) Insert Interval](http://www.lintcode.com/en/problem/insert-interval/)

```
Given a non-overlapping interval list which is sorted by start point.
Insert a new interval into it,
make sure the list is still in order and non-overlapping
(merge intervals if necessary).

Example
Insert [2, 5] into [[1,2], [5,9]], we get [[1,9]].

Insert [3, 4] into [[1,2], [5,9]], we get [[1,2], [3,4], [5,9]].
```

## 题解

这道题看似简单，但其实实现起来不那么容易，因为若按照常规思路，需要分很多种情况考虑，如半边相等的情况。以返回新数组为例，首先，遍历原数组肯定是必须的，以`[N]`代表`newInterval`, `[I]`代表当前遍历到的`interval`, 那么有以下几种情况：

1. `[N], [I]` <==> `newInterval.end < interval.start`, 由于 intervals 中的间隔数组已经为升序排列，那么遍历到的下一个间隔的左边元素必然也大于新间隔的右边元素。
2. `[NI]` <==> `newInterval.end == interval.start`，这种情况下需要进行合并操作。
3. `[IN]` <==> `newInterval.start == interval.end`, 这种情况下也需要进行合并。
4. `[I], [N]` <==> `newInterval.start > interval.end`, 这意味着`newInterval`有可能在此处插入，也有可能在其后面的间隔插入。故遍历时需要在这种情况下做一些标记以确定最终插入位置。

由于间隔都是互不重叠的，故其关系只可能为以上四种中的某几个。1和4两种情况很好处理，关键在于2和3的处理。由于2和3这种情况都将生成新的间隔，且这种情况一旦发生，**原来的`newInterval`即被新的合并间隔取代，这是一个非常关键的突破口。**

### Java

```java
/**
 * Definition of Interval:
 * public classs Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this.start = start;
 *         this.end = end;
 *     }
 */

class Solution {
    /**
     * Insert newInterval into intervals.
     * @param intervals: Sorted interval list.
     * @param newInterval: A new interval.
     * @return: A new sorted interval list.
     */
    public ArrayList<Interval> insert(ArrayList<Interval> intervals, Interval newInterval) {
        ArrayList<Interval> result = new ArrayList<Interval>();
        if (intervals == null || intervals.isEmpty()) {
            if (newInterval != null) {
                result.add(newInterval);
            }
            return result;
        }

        int insertPos = 0;
        for (Interval interval : intervals) {
            if (newInterval.end < interval.start) {
                // case 1: [new], [old]
                result.add(interval);
            } else if (interval.end < newInterval.start) {
                // case 2: [old], [new]
                result.add(interval);
                insertPos++;
            } else {
                // case 3, 4: [old, new] or [new, old]
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

源码的精华在case 3 和 case 4的处理，case 2用于确定最终新间隔的插入位置。

之所以不在 case 1立即返回，有两点考虑：一是代码的复杂性(需要用到 addAll 添加数组部分元素)；二是case2, case3, case 4有可能正好遍历到数组的最后一个元素，如果在 case 1就返回的话还需要单独做一判断。

### 复杂度分析

遍历一次，时间复杂度 $$O(n)$$. 不考虑作为结果返回占用的空间 result, 空间复杂度 $$O(1)$$.

## Reference

- [Insert Interval 参考程序 Java/C++/Python](http://www.jiuzhang.com/solutions/insert-interval/)
