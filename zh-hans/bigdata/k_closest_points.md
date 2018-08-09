---
difficulty: Medium
tags:
- Heap
- Amazon
- LinkedIn
title: K Closest Points
---

# K Closest Points

## Problem

### Metadata

- tags: Heap, Amazon, LinkedIn
- difficulty: Medium
- source(lintcode): <https://www.lintcode.com/problem/k-closest-points/>

### Description

Given some `points` and a point `origin` in two dimensional space, find `k` points out of the some points which are nearest to `origin`.
Return these points sorted by distance, if they are same with distance, sorted by x-axis, otherwise sorted by y-axis.

#### Example

Given points = `[[4,6],[4,7],[4,4],[2,5],[1,1]]`, origin = `[0, 0]`, k = `3`
return `[[1,1],[2,5],[4,4]]`

## 题解

和普通的字符串及数目比较，此题为距离的比较。

### Java

```java
/**
 * Definition for a point.
 * class Point {
 *     int x;
 *     int y;
 *     Point() { x = 0; y = 0; }
 *     Point(int a, int b) { x = a; y = b; }
 * }
 */

public class Solution {
    /**
     * @param points: a list of points
     * @param origin: a point
     * @param k: An integer
     * @return: the k closest points
     */
    public Point[] kClosest(Point[] points, Point origin, int k) {
        // write your code here
        Queue<Point> heap = new PriorityQueue<Point>(new DistanceComparator(origin));
        for (Point point : points) {
            if (heap.size() < k) {
                heap.offer(point);
            } else {
                Point peek = heap.peek();
                if (distance(peek, origin) <= distance(point, origin)) {
                    continue;
                } else {
                    heap.poll();
                    heap.offer(point);
                }
            }
        }

        int minK = Math.min(k, heap.size());
        Point[] kClosestPoints = new Point[minK];
        for (int i = 1; i <= minK; i++) {
            kClosestPoints[minK - i] = heap.poll();
        }

        return kClosestPoints;
    }

    public int distance(Point p, Point origin) {
        return (p.x - origin.x) * (p.x - origin.x) + 
               (p.y - origin.y) * (p.y - origin.y);
    }

    class DistanceComparator implements Comparator<Point> {
        private Point origin = null;
        public DistanceComparator(Point origin) {
            this.origin = origin;
        }

        public int compare(Point p1, Point p2) {
            int d1 = distance(p1, origin);
            int d2 = distance(p2, origin);
            if (d1 != d2) {
                return d2 - d1;
            } else {
                if (p1.x != p2.x) {
                    return p2.x - p1.x;
                } else {
                    return p2.y - p1.y;
                }
            }
        }
    }
}
```

### 源码分析

注意 Comparator 的用法和大小根堆的选择即可。

### 复杂度分析

堆的删除插入操作，最大为 K, 故时间复杂度为 $$O(n \log k)$$, 空间复杂度为 $$O(K)$$.