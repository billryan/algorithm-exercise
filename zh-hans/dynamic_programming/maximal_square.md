# Maximal Square

## Question

- leetcode: [Maximal Square | LeetCode OJ](https://leetcode.com/problems/maximal-square/)
- lintcode: [Maximal Square](http://www.lintcode.com/en/problem/maximal-square/)

### Problem Statement

Given a 2D binary matrix filled with 0's and 1's, find the largest square
containing all 1's and return its area.

#### Example

For example, given the following matrix:



    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0


Return `4`.

## 题解

第一次遇到这个题是在嘀嘀打车现场面试中，首先把题意理解错了，而且动态规划的状态定义错了，没搞出来... 所以说明确题意非常重要！

题意是问矩阵中子正方形（不是长方形）的最大面积。也就是说我们的思路应该是去判断正方形这一子状态以及相应的状态转移方程。正方形的可能有边长为1，2，3等等... 边长为2的可由边长为1 的转化而来，边长为3的可由边长为2的转化而来。那么问题来了，边长的转化是如何得到的？边长由1变为2容易得知，即左上、左边以及上边的值均为1，边长由2变为3这一状态转移方程不容易直接得到。直观上来讲，我们需要边长为3的小正方形内格子中的数均为1. **抽象来讲也可以认为边长为3的正方形是由若干个边长为2的正方形堆叠得到的，这就是这道题的核心状态转移方程。**

令状态`dp[i][j]`表示为从左上角(不一定是`(0,0)`)到矩阵中坐标`(i,j)`为止能构成正方形的最大边长。那么有如下状态转移方程：

```
dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1; if matrix[i][j] == 1
dp[i][j] = 0; if matrix[i][j] = 0
```

初始化直接用第一行和第一列即可。

### Java

```java
public class Solution {
    /**
     * @param matrix: a matrix of 0 and 1
     * @return: an integer
     */
    public int maxSquare(int[][] matrix) {
        int side = 0;
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return side;
        }

        final int ROW = matrix.length, COL = matrix[0].length;
        int[][] dp = new int[ROW][COL];
        for (int i = 0; i < ROW; i++) {
            dp[i][0] = matrix[i][0];
            side = 1;
        }
        for (int i = 0; i < COL; i++) {
            dp[0][i] = matrix[0][i];
            side = 1;
        }

        for (int i = 1; i < ROW; i++) {
            side = Math.max(side, matrix[i][0]);
            for (int j = 1; j < COL; j++) {
                if (matrix[i][j] == 1) {
                    dp[i][j] = 1 + minTri(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]);
                    side = Math.max(side, dp[i][j]);
                }
            }
        }

        return side * side;
    }

    private int minTri(int a, int b, int c) {
        return Math.min(a, Math.min(b, c));
    }
}
```

### 源码分析

经典的动规实现三步走。先初始化，后转移方程，最后对结果做必要的处理（边长 side 的更新）。

### 复杂度分析

使用了二维矩阵，空间复杂度 $$O(mn)$$. 遍历一次原矩阵，时间复杂度 $$O(mn)$$.

### Follow up

题目问的是子正方形，如果问的是矩形呢？

转移方程仍然可以不变，但是遍历完之后需要做进一步处理，比如如果不是正方形的话可能会出现多个相同的边长值，此时需要对相同的边长值递增(按行或者按列)，相乘后保存，最后取最大输出。

## Reference

- [Maximum size square sub-matrix with all 1s - GeeksforGeeks](http://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/)
- [maximal-square/ 参考程序 Java/C++/Python](http://www.jiuzhang.com/solutions/maximal-square/) - 空间复杂度可进一步优化(只保存最近的两行即可)
