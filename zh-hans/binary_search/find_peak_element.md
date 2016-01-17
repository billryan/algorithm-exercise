# Find Peak Element

## Question

- leetcode: [Find Peak Element | LeetCode OJ](https://leetcode.com/problems/find-peak-element/)
- lintcode: [(75) Find Peak Element](http://www.lintcode.com/en/problem/find-peak-element/)

### Problem Statement

A peak element is an element that is greater than its neighbors.

Given an input array where `num[i] ≠ num[i+1]`, find a peak element and return
its index.

The array may contain multiple peaks, in that case return the index to any one
of the peaks is fine.

You may imagine that `num[-1] = num[n] = -∞`.

For example, in array `[1, 2, 3, 1]`, 3 is a peak element and your function
should return the index number 2.

#### Note:

Your solution should be in logarithmic complexity.

#### Credits:


Special thanks to [@ts](https://oj.leetcode.com/discuss/user/ts) for adding
this problem and creating all test cases.

## 题解1

由时间复杂度的暗示可知应使用二分搜索。首先分析若使用传统的二分搜索，若`A[mid] > A[mid - 1] && A[mid] < A[mid + 1]`，则找到一个peak为A[mid]；若`A[mid - 1] > A[mid]`，则A[mid]左侧必定存在一个peak，可用反证法证明：若左侧不存在peak，则A[mid]左侧元素必满足`A[0] > A[1] > ... > A[mid -1] > A[mid]`，与已知`A[0] < A[1]`矛盾，证毕。同理可得若`A[mid + 1] > A[mid]`，则A[mid]右侧必定存在一个peak。如此迭代即可得解。
由于题中假设端点外侧的值均为负无穷大，即`num[-1] < num[0] && num[n-1] > num[n]`, 那么问题来了，这样一来就不能确定峰值一定存在了，因为给定数组为单调序列的话就咩有峰值了，但是实际情况是——题中有负无穷的假设，也就是说在单调序列的情况下，峰值为数组首部或者尾部元素，谁大就是谁了。

备注：如果本题是找 first/last peak，就不能用二分法了。

### Python

```python
class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        if not A:
            return -1

        l, r = 0, len(A) - 1
        while l + 1 < r:
            mid = l + (r - l) / 2
            if A[mid] < A[mid - 1]:
                r = mid
            elif A[mid] < A[mid + 1]:
                l = mid
            else:
                return mid
        mid = l if A[l] > A[r] else r
        return mid
```

### C++

```c++
class Solution {
public:
    /**
     * @param A: An integers array.
     * @return: return any of peek positions.
     */
    int findPeak(vector<int> A) {
        if (A.size() == 0) return -1;

        int l = 0, r = A.size() - 1;
        while (l + 1 < r) {
            int mid = l + (r - l) / 2;
            if (A[mid] < A[mid - 1]) {
                r = mid;
            } else if (A[mid] < A[mid + 1]) {
                l = mid;
            } else {
                return mid;
            }
        }

        int mid = A[l] > A[r] ? l : r;
        return mid;
    }
};
```

### Java

```java
class Solution {
    /**
     * @param A: An integers array.
     * @return: return any of peek positions.
     */
    public int findPeak(int[] A) {
        if (A == null || A.length == 0) return -1;

        int lb = 0, ub = A.length - 1;
        while (lb + 1 < ub) {
            int mid = lb + (ub - lb) / 2;
            if (A[mid] < A[mid + 1]) {
                lb = mid;
            } else if (A[mid] < A[mid - 1]){
                ub = mid;
            } else {
                // find a peak
                return mid;
            }
        }

        // return a larger number
        return A[lb] > A[ub] ? lb : ub;
    }
}
```

### 源码分析

典型的二分法模板应用，需要注意的是需要考虑单调序列的特殊情况。当然也可使用紧凑一点的实现如改写循环条件为`l < r`，这样就不用考虑单调序列了，见实现2.

### 复杂度分析

二分法，时间复杂度 $$O(\log n)$$.

#### Java - compact implementation[^leetcode_discussion]

```java
public class Solution {
    public int findPeakElement(int[] nums) {
        if (nums == null || nums.length == 0) {
            return -1;
        }

        int start = 0, end = nums.length - 1, mid = end / 2;
        while (start < end) {
            if (nums[mid] < nums[mid + 1]) {
                // 1 peak at least in the right side
                start = mid + 1;
            } else {
                // 1 peak at least in the left side
                end = mid;
            }
            mid = start + (end - start) / 2;
        }

        return start;
    }
}
```

C++ 的代码可参考 Java 或者 @xuewei4d 的实现。

> **Warning** leetcode 和 lintcode 上给的方法名不一样，leetcode 上的为`findPeakElement`而 lintcode 上为`findPeak`，弄混的话会编译错误。

## Reference

- [^leetcode_discussion]: [Java - Binary-Search Solution - Leetcode Discuss](https://leetcode.com/discuss/23840/java-binary-search-solution)
