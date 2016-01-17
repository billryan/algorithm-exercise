# Search a 2D Matrix

## Question

- leetcode: [Search a 2D Matrix | LeetCode OJ](https://leetcode.com/problems/search-a-2d-matrix/)
- lintcode: [(28) Search a 2D Matrix](http://www.lintcode.com/en/problem/search-a-2d-matrix/)

### Problem Statement

Write an efficient algorithm that searches for a value in an _m_ x _n_ matrix.

This matrix has the following properties:

  * Integers in each row are sorted from left to right.
  * The first integer of each row is greater than the last integer of the previous row.

#### Example

Consider the following matrix:



    [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]


Given `target = 3`, return `true`.

#### Challenge

O(log(n) + log(m)) time

## 题解 - 一次二分搜索 V.S. 两次二分搜索

- **一次二分搜索** - 由于矩阵按升序排列，因此可将二维矩阵转换为一维问题。对原始的二分搜索进行适当改变即可(求行和列)。时间复杂度为 $$O(log(mn))=O(log(m)+log(n))$$
- **两次二分搜索** - 先按行再按列进行搜索，即两次二分搜索。时间复杂度相同。


## 一次二分搜索

### Python

```python
class Solution:
    def search_matrix(self, matrix, target):
        # Find the first position of target
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        st, ed = 0, m * n - 1

        while st + 1 < ed:
            mid = (st + ed) / 2
            if matrix[mid / n][mid % n] == target:
                return True
            elif matrix[mid / n][mid % n] < target:
                st = mid
            else:
                ed = mid
        return matrix[st / n][st % n] == target or \
                matrix[ed / n][ed % n] == target
```

### C++
```c++
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) return false;

        int ROW = matrix.size(), COL = matrix[0].size();
        int lb = -1, ub = ROW * COL;
        while (lb + 1 < ub) {
            int mid = lb + (ub - lb) / 2;
            if (matrix[mid / COL][mid % COL] < target) {
                lb = mid;
            } else {
                if (matrix[mid / COL][mid % COL] == target) return true;
                ub = mid;
            }
        }
        return false;
    }
};
```

### Java
lower bound 二分模板。
```java
public class Solution {
    /**
     * @param matrix, a list of lists of integers
     * @param target, an integer
     * @return a boolean, indicate whether matrix contains target
     */
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0 || matrix[0] == null) {
            return false;
        }

        int ROW = matrix.length, COL = matrix[0].length;
        int lb = -1, ub = ROW * COL;
        while (lb + 1 < ub) {
            int mid = lb + (ub - lb) / 2;
            if (matrix[mid / COL][mid % COL] < target) {
                lb = mid;
            } else {
                if (matrix[mid / COL][mid % COL] == target) {
                    return true;
                }
                ub = mid;
            }
        }

        return false;
    }
}
```

### 源码分析

仍然可以使用经典的二分搜索模板(lower bound)，注意下标的赋值即可。

1. 首先对输入做异常处理，不仅要考虑到matrix为null，还要考虑到matrix[0]的长度也为0。
2. 由于 lb 的变化处一定小于 target, 故在 else 中判断。

### 复杂度分析

二分搜索，$$O(\log mn)$$.


## 两次二分法

### Python
```python
class Solution:
    def search_matrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False

        # first pos >= target
        st, ed = 0, len(matrix) - 1
        while st + 1 < ed:
            mid = (st + ed) / 2
            if matrix[mid][-1] == target:
                st = mid
            elif matrix[mid][-1] < target:
                st = mid
            else:
                ed = mid
        if matrix[st][-1] >= target:
            row = matrix[st]
        elif matrix[ed][-1] >= target:
            row = matrix[ed]
        else:
            return False

        # binary search in row
        st, ed = 0, len(row) - 1
        while st + 1 < ed:
            mid = (st + ed) / 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                st = mid
            else:
                ed = mid
        return row[st] == target or row[ed] == target
```

### 源码分析

1. 先找到`first position`的行， 这一行的最后一个元素大于等于target
2. 再在这一行中找target

#### 复杂度分析
二分搜索， $$O(\log m + \log n)$$
