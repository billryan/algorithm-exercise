# Find Minimum in Rotated Sorted Array II

## Question

- leetcode: [Find Minimum in Rotated Sorted Array II | LeetCode OJ](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)
- lintcode: [(160) Find Minimum in Rotated Sorted Array II](http://www.lintcode.com/en/problem/find-minimum-in-rotated-sorted-array-ii/)

### Problem Statement

Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

The array may contain duplicates.

#### Example

Given [4,4,5,6,7,0,1,2] return 0

## 题解

由于此题输入可能有重复元素，因此在`num[mid] == num[end]`时无法使用二分的方法缩小start或者end的取值范围。此时只能使用递增start/递减end逐步缩小范围。

### C++

```c++
class Solution {
public:
    /**
     * @param num: a rotated sorted array
     * @return: the minimum number in the array
     */
    int findMin(vector<int> &num) {
        if (num.empty()) {
            return -1;
        }

        vector<int>::size_type start = 0;
        vector<int>::size_type end = num.size() - 1;
        vector<int>::size_type mid;
        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (num[mid] > num[end]) {
                start = mid;
            } else if (num[mid] < num[end]) {
                end = mid;
            } else {
                --end;
            }
        }

        if (num[start] < num[end]) {
            return num[start];
        } else {
            return num[end];
        }
    }
};
```

### Java

```java
public class Solution {
    /**
     * @param num: a rotated sorted array
     * @return: the minimum number in the array
     */
    public int findMin(int[] num) {
        if (num == null || num.length == 0) return Integer.MIN_VALUE;

        int lb = 0, ub = num.length - 1;
        // case1: num[0] < num[num.length - 1]
        // if (num[lb] < num[ub]) return num[lb];

        // case2: num[0] > num[num.length - 1] or num[0] < num[num.length - 1]
        while (lb + 1 < ub) {
            int mid = lb + (ub - lb) / 2;
            if (num[mid] < num[ub]) {
                ub = mid;
            } else if (num[mid] > num[ub]){
                lb = mid;
            } else {
                ub--;
            }
        }

        return Math.min(num[lb], num[ub]);
    }
}
```

### 源码分析

注意`num[mid] > num[ub]`时应递减 ub 或者递增 lb.

### 复杂度分析

最坏情况下 $$O(n)$$, 平均情况下 $$O(\log n)$$.
