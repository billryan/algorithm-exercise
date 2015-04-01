# Search a 2D Matrix

Question: [(28) Search a 2D Matrix](http://www.lintcode.com/en/problem/search-a-2d-matrix/)

题解：

1. 由于矩阵按升序排列，因此可将二维矩阵转换为一维问题。对原始的二分搜索进行适当改变即可(求行和列)。时间复杂度为O(log(mn))=O(log(m)+log(n))
2. 先按行再按列进行搜索，即两次二分搜索。时间复杂度相同。

以思路1为例。

```
/**
 * 本代码由九章算法编辑提供。没有版权欢迎转发。
 * http://www.ninechapter.com/solutions/search-a-2d-matrix
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

源码分析：

1. 首先对输入做异常处理，不仅要考虑到matrix为空串，还要考虑到matrix[0]也为空串。
2. 如果搜索结束时target与start或者end的值均不等时，则必在矩阵的值范围之外，避免了特殊情况的考虑。

第一次A掉这个题用的是分行分列两次搜索，好蠢...

## Search a 2D Matrix II

Question: [(38) Search a 2D Matrix II](http://lintcode.com/en/problem/search-a-2d-matrix-ii/)

题解：

1. 复杂度要求——O(m+n) time and O(1) extra space，同时输入只满足自顶向下和自左向右的升序，行与行之间不再有递增关系，与上题有较大区别。时间复杂度为线性要求，因此可从元素排列特点出发，从一端走向另一端无论如何都需要m+n步，因此可分析对角线元素。
2. 首先分析如果从左上角开始搜索，由于元素升序为自左向右和自上而下，因此如果target大于当前搜索元素时还有两个方向需要搜索，不太合适。
3. 如果从右上角开始搜索，由于左边的元素一定不大于当前元素，而下面的元素一定不小于当前元素，因此每次比较时均可排除一列或者一行元素（大于当前元素则排除当前行，小于当前元素则排除当前列，由矩阵特点可知），可达到题目要求的复杂度。

```
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

源码分析：

1. 首先对输入做异常处理，不仅要考虑到matrix为空串，还要考虑到matrix[0]也为空串。
2. 注意循环终止条件。
3. 在找出target后应继续搜索其他元素。

### Reference

[Searching a 2D Sorted Matrix Part II | LeetCode](http://articles.leetcode.com/2010/10/searching-2d-sorted-matrix-part-ii.html)
