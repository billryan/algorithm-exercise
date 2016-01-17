# First Bad Version

## Question

- lintcode: [(74) First Bad Version](http://www.lintcode.com/en/problem/first-bad-version/)

### Problem Statement

The code base version is an integer start from 1 to n. One day, someone
committed a bad version in the code case, so it caused this version and the
following versions are all failed in the unit tests. Find the first bad
version.

You can call `isBadVersion` to help you determine which version is the first
bad one. The details interface can be found in the code's annotation part.

#### Example

Given n = `5`:



    isBadVersion(3) -> false
    isBadVersion(5) -> true
    isBadVersion(4) -> true


Here we are 100% sure that the 4th version is the first bad version.

#### Note

Please read the annotation in code area to get the correct way to call
isBadVersion in different language. For example, Java is
`VersionControl.isBadVersion(v)`

#### Challenge

You should call _isBadVersion_ as few as possible.

## 题解

基础算法中 [Binary Search](http://algorithm.yuanbin.me/zh-hans/basics_algorithm/binary_search.html) 的 lower bound. 找出满足条件的下界即可。

### Python

```python
#class VersionControl:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use VersionControl.isBadVersion(10) to check whether version 10 is a
# bad version.
class Solution:
    """
    @param n: An integers.
    @return: An integer which is the first bad version.
    """
    def findFirstBadVersion(self, n):
        lb, ub = 0, n + 1
        while lb + 1 < ub:
            mid = lb + (ub - lb) / 2
            if VersionControl.isBadVersion(mid):
                ub = mid
            else:
                lb = mid

        return lb + 1
```

### C++

```c++
/**
 * class VersionControl {
 *     public:
 *     static bool isBadVersion(int k);
 * }
 * you can use VersionControl::isBadVersion(k) to judge whether
 * the kth code version is bad or not.
*/
class Solution {
public:
    /**
     * @param n: An integers.
     * @return: An integer which is the first bad version.
     */
    int findFirstBadVersion(int n) {
        int lb = 0, ub = n + 1;
        while (lb + 1 < ub) {
            int mid = lb + (ub - lb) / 2;
            if (VersionControl::isBadVersion(mid)) {
                ub = mid;
            } else {
                lb = mid;
            }
        }

        return lb + 1;
    }
};
```

### Java

```java
/**
 * public class VersionControl {
 *     public static boolean isBadVersion(int k);
 * }
 * you can use VersionControl.isBadVersion(k) to judge whether
 * the kth code version is bad or not.
*/
class Solution {
    /**
     * @param n: An integers.
     * @return: An integer which is the first bad version.
     */
    public int findFirstBadVersion(int n) {
        int lb = 0, ub = n + 1;
        while (lb + 1 < ub) {
            int mid = lb + (ub - lb) / 2;
            if (VersionControl.isBadVersion(mid)) {
                ub = mid;
            } else {
                lb = mid;
            }
        }

        return lb + 1;
    }
}
```

### 源码分析

lower bound 的实现，这里稍微注意下lb 初始化为 0，因为 n 从1开始。ub 和 lb 分别都在什么条件下更新就好了。另外这里并未考虑 `n <= 0` 的情况。

### 复杂度分析

二分搜索，$$O(\log n)$$.
