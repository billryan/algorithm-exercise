# Matrix Zigzag Traversal

## Question

- lintcode: [(185) Matrix Zigzag Traversal](http://www.lintcode.com/en/problem/matrix-zigzag-traversal/)

```
Given a matrix of m x n elements (m rows, n columns),
return all elements of the matrix in ZigZag-order.

Example
Given a matrix:

[
  [1, 2,  3,  4],
  [5, 6,  7,  8],
  [9,10, 11, 12]
]
return [1, 2, 5, 9, 6, 3, 4, 7, 10, 11, 8, 12]
```

## 题解

按之字形遍历矩阵，纯粹找下标规律。以题中所给范例为例，设`(x, y)`为矩阵坐标，按之字形遍历有如下规律：

```
(0, 0)
(0, 1), (1, 0)
(2, 0), (1, 1), (0, 2)
(0, 3), (1, 2), (2, 1)
(2, 2), (1, 3)
(2, 3)
```

可以发现其中每一行的坐标之和为常数，坐标和为奇数时 x 递增，为偶数时 x 递减。

### Java - valid matrix index second

```java
public class Solution {
    /**
     * @param matrix: a matrix of integers
     * @return: an array of integers
     */
    public int[] printZMatrix(int[][] matrix) {
        if (matrix == null || matrix.length == 0) return null;

        int m = matrix.length - 1, n = matrix[0].length - 1;
        int[] result = new int[(m + 1) * (n + 1)];
        int index = 0;
        for (int i = 0; i <= m + n; i++) {
            if (i % 2 == 0) {
                for (int x = i; x >= 0; x--) {
                    // valid matrix index
                    if ((x <= m) && (i - x <= n)) {
                        result[index] = matrix[x][i - x];
                        index++;
                    }
                }
            } else {
                for (int x = 0; x <= i; x++) {
                    if ((x <= m) && (i - x <= n)) {
                        result[index] = matrix[x][i - x];
                        index++;
                    }
                }
            }
        }

        return result;
    }
}
```

### Java - valid matrix index first

```java
public class Solution {
    /**
     * @param matrix: a matrix of integers
     * @return: an array of integers
     */
    public int[] printZMatrix(int[][] matrix) {
        if (matrix == null || matrix.length == 0) return null;

        int m = matrix.length - 1, n = matrix[0].length - 1;
        int[] result = new int[(m + 1) * (n + 1)];
        int index = 0;
        for (int i = 0; i <= m + n; i++) {
            int upperBoundx = Math.min(i, m); // x <= m
            int lowerBoundx = Math.max(0, i - n); // lower bound i - x(y) <= n
            int upperBoundy = Math.min(i, n); // y <= n
            int lowerBoundy = Math.max(0, i - m); // i - y(x) <= m
            if (i % 2 == 0) {
                // column increment
                for (int y = lowerBoundy; y <= upperBoundy; y++) {
                    result[index] = matrix[i - y][y];
                    index++;
                }
            } else {
                // row increment
                for (int x = lowerBoundx; x <= upperBoundx; x++) {
                    result[index] = matrix[x][i - x];
                    index++;
                }
            }
        }

        return result;
    }
}
```

### 源码分析

矩阵行列和分奇偶讨论，奇数时行递增，偶数时列递增，一种是先循环再判断索引是否合法，另一种是先取的索引边界。

### 复杂度分析

后判断索引是否合法的实现遍历次数为 $$1 + 2 + ... + (m + n) = O((m+n)^2)$$, 首先确定上下界的每个元素遍历一次，时间复杂度 $$O(m \cdot n)$$. 空间复杂度都是 $$O(1)$$.

## Reference

- [LintCode/matrix-zigzag-traversal.cpp at master · kamyu104/LintCode](https://github.com/kamyu104/LintCode/blob/master/C++/matrix-zigzag-traversal.cpp)
