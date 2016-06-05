# Search for a Range

## Question

- leetcode: [Search for a Range | LeetCode OJ](https://leetcode.com/problems/search-for-a-range/)
- lintcode: [(61) Search for a Range](http://www.lintcode.com/en/problem/search-for-a-range/)

### Problem Statement

Given a sorted array of _n_ integers, find the starting and ending position of
a given target value.

If the target is not found in the array, return `[-1, -1]`.

#### Example

Given `[5, 7, 7, 8, 8, 10]` and target value `8`, return `[3, 4]`.

#### Challenge

O(log _n_) time.

## 题解

### Python
first/last position 结合。
```python
class Solution:
    """
    @param A : a list of integers
    @param target : an integer to be searched
    @return : a list of length 2, [index1, index2]
    """
    def searchRange(self, A, target):
        ret = [-1, -1]
        if not A:
            return ret

        # find the first position of target
        st, ed = 0, len(A) - 1
        while st + 1 < ed:
            mid = (st + ed) / 2
            if A[mid] == target:
                ed = mid
            elif A[mid] < target:
                st = mid
            else:
                ed = mid
        if A[st] == target:
            ret[0] = st
        elif A[ed] == target:
            ret[0] = ed
        # find the last position of target
        st, ed = 0, len(A) - 1
        while st + 1 < ed:
            mid = (st + ed) / 2
            if A[mid] == target:
                st = mid
            elif A[mid] < target:
                st = mid
            else:
                ed = mid
        if A[ed] == target:
            ret[1] = ed
        elif A[st] == target:
            ret[1] = st

        return ret
```

### C++
```c++
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> result = {-1, -1};
        if (nums.empty()) return result;

        int lb = -1, ub = nums.size();
        while (lb + 1 < ub) {
            int mid = lb + (ub - lb) / 2;
            if (nums[mid] < target) lb = mid;
            else ub = mid;
        }

        if ((ub < nums.size()) && (nums[ub] == target)) result[0] = ub;
        else return result;

        ub = nums.size();
        while (lb + 1 < ub) {
            int mid = lb + (ub - lb) / 2;
            if (nums[mid] > target) ub = mid;
            else lb = mid;
        }
        result[1] = ub - 1;
        return result;
    }
};
```

### Java
lower/upper bound 的结合，做两次搜索即可。
```java
public class Solution {
    /**
     *@param A : an integer sorted array
     *@param target :  an integer to be inserted
     *return : a list of length 2, [index1, index2]
     */
    public int[] searchRange(int[] A, int target) {
        int[] result = new int[]{-1, -1};
        if (A == null || A.length == 0) return result;

        int lb = -1, ub = A.length;
        // lower bound
        while (lb + 1 < ub) {
            int mid = lb + (ub - lb) / 2;
            if (A[mid] < target) {
                lb = mid;
            } else {
                ub = mid;
            }
        }
        // whether A[lb + 1] == target, check lb + 1 first
        if ((lb + 1 < A.length) && (A[lb + 1] == target)) {
            result[0] = lb + 1;
        } else {
            result[0] = -1;
            result[1] = -1;
            // target is not in the array
            return result;
        }

        // upper bound, since ub >= lb, we do not reset lb
        ub = A.length;
        while (lb + 1 < ub) {
            int mid = lb + (ub - lb) / 2;
            if (A[mid] > target) {
                ub = mid;
            } else {
                lb = mid;
            }
        }
        // target must exist in the array
        result[1] = ub - 1;

        return result;
    }
}
```

### 源码分析

1. 首先对输入做异常处理，数组为空或者长度为0
2. 分 lower/upper bound 两次搜索，注意如果在 lower bound 阶段未找到目标值时，upper bound 也一定找不到。
3. 取`A[lb + 1]` 时一定要注意判断索引是否越界！

### 复杂度分析

两次二分搜索，时间复杂度仍为 $$O(\log n)$$.

## Reference

- [Binary Search – topcoder](https://www.topcoder.com/community/data-science/data-science-tutorials/binary-search/) - 思路更清晰的 find first 模板，find last k 可转化为 find first `k + 1` 谢谢 @mckelvin 同学推荐
