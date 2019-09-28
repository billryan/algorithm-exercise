# Search in Rotated Sorted Array II

## Question

- leetcode: [Search in Rotated Sorted Array II | LeetCode OJ](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)
- lintcode: [(63) Search in Rotated Sorted Array II](http://www.lintcode.com/en/problem/search-in-rotated-sorted-array-ii/)

### Problem Statement

Follow up for "Search in Rotated Sorted Array":
What if _duplicates_ are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.

## 题解

仔细分析此题和之前一题的不同之处，前一题我们利用`A[start] < A[mid]`这一关键信息，而在此题中由于有重复元素的存在，在`A[start] == A[mid]`时无法确定有序数组，此时只能依次递增start/递减end以缩小搜索范围，时间复杂度最差变为O(n)。

### C++

```c++
class Solution {
    /**
     * param A : an integer ratated sorted array and duplicates are allowed
     * param target :  an integer to be search
     * return : a boolean
     */
public:
    bool search(vector<int> &A, int target) {
        if (A.empty()) {
            return false;
        }

        vector<int>::size_type start = 0;
        vector<int>::size_type end = A.size() - 1;
        vector<int>::size_type mid;

        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (target == A[mid]) {
                return true;
            }
            if (A[start] < A[mid]) {
                // situation 1, numbers between start and mid are sorted
                if (A[start] <= target && target < A[mid]) {
                    end = mid;
                } else {
                    start = mid;
                }
            } else if (A[start] > A[mid]) {
                // situation 2, numbers between mid and end are sorted
                if (A[mid] < target && target <= A[end]) {
                    start = mid;
                } else {
                    end = mid;
                }
            } else  {
                // increment start
                ++start;
            }
        }

        if (A[start] == target || A[end] == target) {
            return true;
        }
        return false;
    }
};
```

### Java

```java
public class Solution {
    /**
     * param A : an integer ratated sorted array and duplicates are allowed
     * param target :  an integer to be search
     * return : a boolean
     */
    public boolean search(int[] A, int target) {
        if (A == null || A.length == 0) return false;

        int lb = 0, ub = A.length - 1;
        while (lb + 1 < ub) {
            int mid = lb + (ub - lb) / 2;
            if (A[mid] == target) return true;

            if (A[mid] > A[lb]) {
                // case1: numbers between lb and mid are sorted
                if (A[lb] <= target && target <= A[mid]) {
                    ub = mid;
                } else {
                    lb = mid;
                }
            } else if (A[mid] < A[lb]) {
                // case2: numbers between mid and ub are sorted
                if (A[mid] <= target && target <= A[ub]) {
                    lb = mid;
                } else {
                    ub = mid;
                }
            } else {
                // case3: A[mid] == A[lb]
                lb++;
            }
        }

        if (target == A[lb] || target == A[ub]) {
            return true;
        }
        return false;
    }
}
```

### 源码分析

在`A[lb] == A[mid]`时递增lb序号即可。

### 复杂度分析

最差情况下 $$O(n)$$, 平均情况下 $$O(\log n)$$.
