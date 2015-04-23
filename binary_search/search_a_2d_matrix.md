# Search a 2D Matrix

## Source

- lintcode: [(28) Search a 2D Matrix](http://www.lintcode.com/en/problem/search-a-2d-matrix/)

```
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:

    * Integers in each row are sorted from left to right.

    * The first integer of each row is greater than the last integer of the previous row.

Example
Consider the following matrix:

[

    [1, 3, 5, 7],

    [10, 11, 16, 20],

    [23, 30, 34, 50]

]

Given target = 3, return true.

Challenge
O(log(n) + log(m)) time
```

### 题解 - 一次二分搜索 V.S. 两次二分搜索

**一次二分搜索**

由于矩阵按升序排列，因此可将二维矩阵转换为一维问题。对原始的二分搜索进行适当改变即可(求行和列)。时间复杂度为 $$O(log(mn))=O(log(m)+log(n))$$

**两次二分搜索**

先按行再按列进行搜索，即两次二分搜索。时间复杂度相同。

以一次二分搜素的方法为例。

#### Java

```java
/**
 * 本代码由九章算法编辑提供。没有版权欢迎转发。
 * http://www.jiuzhang.com/solutions/search-a-2d-matrix
 */
// Binary Search Once
public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        if (matrix == null || matrix.length == 0) {
            return false;
        }
        if (matrix[0] == null || matrix[0].length == 0) {
            return false;
        }

        int row = matrix.length, column = matrix[0].length;
        int start = 0, end = row * column - 1;
        int mid, number;

        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            number = matrix[mid / column][mid % column];
            if (number == target) {
                return true;
            } else if (number < target) {
                start = mid;
            } else {
                end = mid;
            }
        }

        if (matrix[start / column][start % column] == target) {
            return true;
        } else if (matrix[end / column][end % column] == target) {
            return true;
        }

        return false;
    }
}
```

#### 源码分析

仍然可以使用经典的二分搜索模板，注意下标的赋值即可。

1. 首先对输入做异常处理，不仅要考虑到matrix为空串，还要考虑到matrix[0]也为空串。
2. 如果搜索结束时target与start或者end的值均不等时，则必在矩阵的值范围之外，避免了特殊情况的考虑。

第一次A掉这个题用的是分行分列两次搜索，好蠢...

## Search a 2D Matrix II

## Source

- lintcode: [(38) Search a 2D Matrix II](http://lintcode.com/en/problem/search-a-2d-matrix-ii/)

```
Write an efficient algorithm that searches for a value in an m x n matrix, return the occurrence of it.

This matrix has the following properties:

    * Integers in each row are sorted from left to right.

    * Integers in each column are sorted from up to bottom.

    * No duplicate integers in each row or column.

Example
Consider the following matrix:

[

    [1, 3, 5, 7],

    [2, 4, 7, 8],

    [3, 5, 9, 10]

]

Given target = 3, return 2.

Challenge
O(m+n) time and O(1) extra space
```

### 题解 - 自右上而左下

1. 复杂度要求——O(m+n) time and O(1) extra space，同时输入只满足自顶向下和自左向右的升序，行与行之间不再有递增关系，与上题有较大区别。时间复杂度为线性要求，因此可从元素排列特点出发，从一端走向另一端无论如何都需要m+n步，因此可分析对角线元素。
2. 首先分析如果从左上角开始搜索，由于元素升序为自左向右和自上而下，因此如果target大于当前搜索元素时还有两个方向需要搜索，不太合适。
3. 如果从右上角开始搜索，由于左边的元素一定不大于当前元素，而下面的元素一定不小于当前元素，因此每次比较时均可排除一列或者一行元素（大于当前元素则排除当前行，小于当前元素则排除当前列，由矩阵特点可知），可达到题目要求的复杂度。

**在遇到之前没有遇到过的复杂题目时，可先使用简单的数据进行测试去帮助发现规律。**

#### C++

```c++
class Solution {
public:
    /**
     * @param matrix: A list of lists of integers
     * @param target: An integer you want to search in matrix
     * @return: An integer indicate the total occurrence of target in the given matrix
     */
    int searchMatrix(vector<vector<int> > &matrix, int target) {
        if (matrix.empty() || matrix[0].empty()) {
            return 0;
        }

        const int ROW = matrix.size();
        const int COL = matrix[0].size();

        int row = 0, col = COL - 1;
        int occur = 0;
        while (row < ROW && col >= 0) {
            if (target == matrix[row][col]) {
                ++occur;
                --col;
            } else if (target < matrix[row][col]){
                --col;
            } else {
                ++row;
            }
        }

        return occur;
    }
};
```

#### Java

```java
public class Solution {
    /**
     * @param matrix: A list of lists of integers
     * @param: A number you want to search in the matrix
     * @return: An integer indicate the occurrence of target in the given matrix
     */
    public int searchMatrix(int[][] matrix, int target) {
        int occurence = 0;

        if (matrix == null || matrix.length == 0) {
            return occurence;
        }
        if (matrix[0] == null || matrix[0].length == 0) {
            return occurence;
        }

        int row = matrix.length - 1;
        int column = matrix[0].length - 1;
        int index_row = 0, index_column = column;
        int number;

        if (target < matrix[0][0] || target > matrix[row][column]) {
            return occurence;
        }

        while (index_row < row + 1 && index_column + 1 > 0) {
            number = matrix[index_row][index_column];
            if (target == number) {
                occurence++;
                index_column--;
            } else if (target < number) {
                index_column--;
            } else if (target > number) {
                index_row++;
            }
        }

        return occurence;
    }
}
```

#### 源码分析

1. 首先对输入做异常处理，不仅要考虑到matrix为空串，还要考虑到matrix[0]也为空串。
2. 注意循环终止条件。
3. 在找出`target`后应继续向左搜索其他可能相等的元素，下方比当前元素大，故排除此列。

## Reference

[Searching a 2D Sorted Matrix Part II | LeetCode](http://articles.leetcode.com/2010/10/searching-2d-sorted-matrix-part-ii.html)
