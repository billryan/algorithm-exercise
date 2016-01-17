# Longest Increasing Continuous subsequence II

## Question

- lintcode: [(398) Longest Increasing Continuous subsequence II](http://www.lintcode.com/en/problem/longest-increasing-continuous-subsequence-ii/)

### Problem Statement

Give you an integer matrix (with row size n, column size m)，find the longest increasing continuous subsequence in this matrix. (The definition of the longest increasing continuous subsequence here can start at any row or column and go up/down/right/left any direction).

#### Example

Given a matrix:
```
[
  [1 ,2 ,3 ,4 ,5],
  [16,17,24,23,6],
  [15,18,25,22,7],
  [14,19,20,21,8],
  [13,12,11,10,9]
]
```
return 25

#### Challenge

O(nm) time and memory.

## 题解

题 [Longest Increasing Continuous subsequence](http://algorithm.yuanbin.me/zh-hans/dynamic_programming/longest_increasing_continuous_subsequence.html) 的 follow up, 变成一道比较难的题了。从之前的一维 DP 变为现在的二维 DP，自增方向可从上下左右四个方向进行。需要结合 DFS 和动态规划两大重量级武器。

根据二维 DP 的通用方法，我们首先需要关注状态及状态转移方程，状态转移方程相对明显一点，即上下左右四个方向的元素值递增关系，根据此转移方程，**不难得到我们需要的状态为`dp[i][j]`——表示从坐标`(i, j)`出发所得到的最长连续递增子序列。**根据状态及转移方程我们不难得到初始化应该为1或者0，这要视具体情况而定。

这里我们可能会纠结的地方在于自增的方向，平时见到的二维 DP 自增方向都是从小到大，而这里的增长方向却不一定。**这里需要突破思维定势的地方在于我们可以不理会从哪个方向自增，只需要处理自增和边界条件即可。**根据转移方程可以知道使用递归来解决是比较好的方式，这里关键的地方就在于递归的终止条件。比较容易想到的一个递归终止条件自然是当前元素是整个矩阵中的最大元素，索引朝四个方向出发都无法自增，因此返回1. 另外可以预想到的是如果不进行记忆化存储，递归过程中自然会产生大量重复计算，根据记忆化存储的通用方法，这里可以以结果是否为0(初始化为0时)来进行区分。

### Java

```java
public class Solution {
    /**
     * @param A an integer matrix
     * @return  an integer
     */
    public int longestIncreasingContinuousSubsequenceII(int[][] A) {
        if (A == null || A.length == 0 || A[0].length == 0) return 0;

        int lics = 0;
        int[][] dp = new int[A.length][A[0].length];
        for (int row = 0; row < A.length; row++) {
            for (int col = 0; col < A[0].length; col++) {
                if (dp[row][col] == 0) {
                    lics = Math.max(lics, dfs(A, row, col, dp));
                }
            }
        }

        return lics;
    }

    private int dfs(int[][] A, int row, int col, int[][] dp) {
        if (dp[row][col] != 0) {
            return dp[row][col];
        }

        // increasing from xxx to up, down, left, right
        int up = 0, down = 0, left = 0, right = 0;
        // increasing from down to up
        if (row > 0 && A[row - 1][col] > A[row][col]) {
            up = dfs(A, row - 1, col, dp);
        }
        // increasing from up to down
        if (row + 1 < A.length && A[row + 1][col] > A[row][col]) {
            down = dfs(A, row + 1, col, dp);
        }
        // increasing from right to left
        if (col > 0 && A[row][col - 1] > A[row][col]) {
            left = dfs(A, row, col - 1, dp);
        }
        // increasing from left to right
        if (col + 1 < A[0].length && A[row][col + 1] > A[row][col]) {
            right = dfs(A, row, col + 1, dp);
        }
        // return maximum of up, down, left, right
        dp[row][col] = 1 + Math.max(Math.max(up, down), Math.max(left, right));

        return dp[row][col];
    }
}
```

### 源码分析

dfs 递归最深一层即矩阵中最大的元素处，然后逐层返回。这道题对状态`dp[i][j]`的理解很重要，否则会陷入对上下左右四个方向的迷雾中。

### 复杂度分析

由于引入了记忆化存储，时间复杂度逼近 $$O(mn)$$, 空间复杂度 $$O(mn)$$.

## Reference

- [Lintcode: Longest Increasing Continuous subsequence II | codesolutiony](https://codesolutiony.wordpress.com/2015/05/25/lintcode-longest-increasing-continuous-subsequence-ii/)
