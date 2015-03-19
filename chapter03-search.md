# Search - 搜索

## Binary Search - 二分查找

Question: [lintcode - (14) Binary Search](http://www.lintcode.com/en/problem/binary-search/)

> Binary search is a famous question in algorithm.

> For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.

> If the target number does not exist in the array, return -1.

> **Example**

> If the array is [1, 2, 3, 3, 4, 5, 10], for given target 3, return 2.

> **Challenge**

> If the count of numbers is bigger than `MAXINT`, can your code work properly?

题解：

对于已排序升序数组，使用二分查找可满足复杂度要求，注意数组中可能有重复值。

```
/**
 * 本代码fork自九章算法。没有版权欢迎转发。
 * http://www.ninechapter.com//solutions/binary-search/
 */
class Solution {
    /**
     * @param nums: The integer array.
     * @param target: Target to find.
     * @return: The first position of target. Position starts from 0.
     */
    public int binarySearch(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return -1;
        }
        
        int start = 0;
        int end = nums.length - 1;
        int mid;
        while (start + 1 < end) {
            mid = start + (end - start) / 2; // avoid overflow when (end + start)
            if (target < nums[mid]) {
                end = mid;
            } else if (target > nums[mid]) {
                start = mid;
            } else {
                end = mid;
            }
        }
        
        if (nums[start] == target) {
            return start;
        }
        if (nums[end] == target) {
            return end;
        }

        return -1;
    }
}
```

源码分析：

1. 首先对输入做异常处理，数组为空或者长度为0
2. 初始化 `start, end, mid`三个变量，注意mid的求值方法，可以防止两个整型值相加时溢出
3. **使用迭代而不是递归**进行二分查找
4. while终止条件应为`start + 1 < end`而不是`start <= end`，`start == end`时可能出现死循环
5. 迭代终止时target应为start或者end中的一个
6. 赋值语句`end = mid`有两个条件是相同的，为何不写到一起？程序执行时可能还要慢些？

## Search for a Range

Question: [(61) Search for a Range](http://www.lintcode.com/en/problem/search-for-a-range/)

题解：

由上题二分查找可找到满足条件的左边界，因此只需要再将右边界找出即可。注意到在`(target == nums[mid]`时赋值语句为`end = mid`，将其改为`start = mid`即可找到右边界，解毕。

```
/**
 * 本代码fork自九章算法。没有版权欢迎转发。
 * http://www.ninechapter.com/solutions/search-for-a-range/
 */
public class Solution {
    /** 
     *@param A : an integer sorted array
     *@param target :  an integer to be inserted
     *return : a list of length 2, [index1, index2]
     */
    public ArrayList<Integer> searchRange(ArrayList<Integer> A, int target) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        int start, end, mid;
        result.add(-1);
        result.add(-1);
        
        if (A == null || A.size() == 0) {
            return result;
        }
        
        // search for left bound
        start = 0;
        end = A.size() - 1;
        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (A.get(mid) == target) {
                end = mid; // set end = mid to find the minimum mid
            } else if (A.get(mid) > target) {
                end = mid;
            } else {
                start = mid;
            }
        }
        if (A.get(start) == target) {
            result.set(0, start);
        } else if (A.get(end) == target) {
            result.set(0, end);
        } else {
            return result;
        }
        
        // search for right bound
        start = 0;
        end = A.size() - 1;
        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (A.get(mid) == target) {
                start = mid; // set start = mid to find the maximum mid
            } else if (A.get(mid) > target) {
                end = mid;
            } else {
                start = mid;
            }
        }
        if (A.get(end) == target) {
            result.set(1, end);
        } else if (A.get(start) == target) {
            result.set(1, start);
        } else {
            return result;
        }
        
        return result;
        // write your code here
    }
}
```

源码分析：

1. 首先对输入做异常处理，数组为空或者长度为0
2. 初始化 `start, end, mid`三个变量，注意mid的求值方法，可以防止两个整型值相加时溢出
3. **使用迭代而不是递归**进行二分查找
4. while终止条件应为`start + 1 < end`而不是`start <= end`，`start == end`时可能出现死循环
5. 先求左边界，迭代终止时先判断`A.get(start) == target`，再判断`A.get(end) == target`，因为迭代终止时target必取start或end中的一个，而end又大于start，取左边界即为start.
6. 再求右边界，迭代终止时先判断`A.get(end) == target`，再判断`A.get(start) == target`

## Search Insert Position

Question: [(60) Search Insert Position](http://www.lintcode.com/en/problem/search-insert-position/)

题解：

由最原始的二分查找可找到不小于目标整数的最小下标。返回此下标即可。

```
public class Solution {
    /** 
     * param A : an integer sorted array
     * param target :  an integer to be inserted
     * return : an integer
     */
    public int searchInsert(int[] A, int target) {
        if (A == null) {
            return -1;
        }
        if (A.length == 0) {
            return 0;
        }

        int start = 0, end = A.length - 1;
        int mid;

        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (A[mid] == target) {
                return mid; // no duplicates, if not `end = target;`
            } else if (A[mid] < target) {
                start = mid;
            } else {
                end = mid;
            }
        }

        if (A[start] >= target) {
            return start;
        } else if (A[end] >= target) {
            return end; // in most cases
        } else {
            return end + 1; // A[end] < target;
        }
    }
}
```

源码分析：已在源码处注释

## Search a 2D Matrix

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