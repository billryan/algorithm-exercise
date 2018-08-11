---
difficulty: Medium
tags:
- Binary Search
- LinkedIn
- Array
- Facebook
- Sorted Array
- Uber
- Microsoft
- Bloomberg
title: Search in Rotated Sorted Array
---

# Search in Rotated Sorted Array

## Problem

### Metadata

- tags: Binary Search, LinkedIn, Array, Facebook, Sorted Array, Uber, Microsoft, Bloomberg
- difficulty: Medium
- source(leetcode): <https://leetcode.com/problems/search-in-rotated-sorted-array/>
- source(lintcode): <https://www.lintcode.com/problem/search-in-rotated-sorted-array/>

### Description

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., `0 1 2 4 5 6 7` might become `4 5 6 7 0 1 2`).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

#### Example

For `[4, 5, 1, 2, 3]` and `target=1`, return `2`.

For `[4, 5, 1, 2, 3]` and `target=0`, return `-1`.

#### Challenge

O(logN) time

## 题解1 - 找到有序数组

对于旋转数组的分析可使用画图的方法，如下图所示，升序数组经旋转后可能为如下两种形式。

![Rotated Array](../../shared-files/images/rotated_array.png)

对于有序数组，使用二分搜索比较方便。分析题中的数组特点，旋转后初看是乱序数组，但仔细一看其实里面是存在两段有序数组的。刚开始做这道题时可能会去比较`target`和`A[mid]`, 但分析起来异常复杂。**该题较为巧妙的地方在于如何找出旋转数组中的局部有序数组，并使用二分搜索解之。**结合实际数组在纸上分析较为方便。

### C++

```c++
/**
 * 本代码fork自
 * http://www.jiuzhang.com/solutions/search-in-rotated-sorted-array/
 */
class Solution {
    /**
     * param A : an integer ratated sorted array
     * param target :  an integer to be searched
     * return : an integer
     */
public:
    int search(vector<int> &A, int target) {
        if (A.empty()) {
            return -1;
        }

        vector<int>::size_type start = 0;
        vector<int>::size_type end = A.size() - 1;
        vector<int>::size_type mid;

        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (target == A[mid]) {
                return mid;
            }
            if (A[start] < A[mid]) {
                // situation 1, numbers between start and mid are sorted
                if (A[start] <= target && target < A[mid]) {
                    end = mid;
                } else {
                    start = mid;
                }
            } else {
                // situation 2, numbers between mid and end are sorted
                if (A[mid] < target && target <= A[end]) {
                    start = mid;
                } else {
                    end = mid;
                }
            }
        }

        if (A[start] == target) {
            return start;
        }
        if (A[end] == target) {
            return end;
        }
        return -1;
    }
};
```

### Java

```java
public class Solution {
    /**
     *@param A : an integer rotated sorted array
     *@param target :  an integer to be searched
     *return : an integer
     */
    public int search(int[] A, int target) {
        if (A == null || A.length == 0) return -1;

        int lb = 0, ub = A.length - 1;
        while (lb + 1 < ub) {
            int mid = lb + (ub - lb) / 2;
            if (A[mid] == target) return mid;

            if (A[mid] > A[lb]) {
                // case1: numbers between lb and mid are sorted
                if (A[lb] <= target && target <= A[mid]) {
                    ub = mid;
                } else {
                    lb = mid;
                }
            } else {
                // case2: numbers between mid and ub are sorted
                if (A[mid] <= target && target <= A[ub]) {
                    lb = mid;
                } else {
                    ub = mid;
                }
            }
        }

        if (A[lb] == target) {
            return lb;
        } else if (A[ub] == target) {
            return ub;
        }
        return -1;
    }
}
```

### 源码分析

1. 若`target == A[mid]`，索引找到，直接返回
2. 寻找局部有序数组，分析`A[mid]`和两段有序的数组特点，由于旋转后前面有序数组最小值都比后面有序数组最大值大。故若`A[start] < A[mid]`成立，则start与mid间的元素必有序（要么是前一段有序数组，要么是后一段有序数组，还有可能是未旋转数组）。
3. 接着在有序数组`A[start]~A[mid]`间进行二分搜索，但能在`A[start]~A[mid]`间搜索的前提是`A[start] <= target <= A[mid]`。
4. 接着在有序数组`A[mid]~A[end]`间进行二分搜索，注意前提条件。
5. 搜索完毕时索引若不是mid或者未满足while循环条件，则测试A[start]或者A[end]是否满足条件。
6. 最后若未找到满足条件的索引，则返回-1.

### 复杂度分析

分两段二分，时间复杂度仍近似为 $$O(\log n)$$.

## 题解2 - 应用两次二分

应用两次二分搜索：第一次是找到分段点，第二次是对分段点两边的有序数组（之一）进行搜索。后者非常简单，关键是第一步怎么找分段点。

乍一看，有序数组经过旋转就不再有序、也不单调了，好像用不了二分。其实不然，分段点左边的元素全都 ≥A[0]、右边元素全都 <A[0], 这就是一个单调性质，借助这个性质就能二分地找到段点。

注：如果觉得上述“二分性质”不够显著，可以引入一个辅助数组 `A'` 来理解, 令 `A'[i] = A[i] < A[0] ? true : false`. 比如示例中 `A = [4, 5, 6, 7, 0, 1, 2]` 对应的 `A'` 就是 `[false, false, false, false, true, true, true]`. 显然 `A'` 是单调序列，只不过元素取值仅 true 和 false 两种。

### Java

```java
public class Solution {
    /**
     *@param A : an integer rotated sorted array
     *@param target :  an integer to be searched
     *return : an integer
     */
    public int search(int[] A, int target) {
        if (A == null || A.length == 0) {
            return -1;
        }

        int p = findBreakPoint(A);
        if (target >= A[0]) {
            // search in [lo, segPoint]
            return binSearch(A, target, 0, p);
        } else {
            // search in [segPoint, hi]
            return binSearch(A, target, p, A.length - 1);
        }
    }

    private int findBreakPoint(int[] A) {
        // A[index] < A[0], min[index]
        int index;

        int lo = 0, hi = A.length - 1, segValue = A[0];
        while (lo + 1 < hi) {
            int md = lo + (hi - lo)/2;
            if (A[md] > segValue) {
                lo = md;
            } else {
                hi = md;
            }
        }
        index = A[lo] < segValue ? lo : hi;

        return index;
    }

    private int binSearch(int[] A, int target, int lo, int hi) {
        while (lo + 1 < hi) {
            int md = lo + (hi - lo) / 2;
            if (A[md] == target) {
                lo = md;
            } else if (A[md] < target) {
                lo = md;
            } else {
                hi = md;
            }
        }

        if (A[lo] == target) {
            return lo;
        }
        if (A[hi] == target) {
            return hi;
        }
        return -1;
    }
}
```

### 复杂度分析

第一次二分找段点时间复杂度为 ***O(log n)*** , 第二次在局部有序数组上二分时间复杂度不超过 ***O(log n)*** , 总起来还是近似 ***O(log n)*** .
