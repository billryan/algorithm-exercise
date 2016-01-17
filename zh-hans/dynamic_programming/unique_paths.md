# Unique Paths

- tags: [DP_Matrix]

## Question

- lintcode: [(114) Unique Paths](http://www.lintcode.com/en/problem/unique-paths/)

```
A robot is located at the top-left corner of a m x n grid
(marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid
(marked 'Finish' in the diagram below).

How many possible unique paths are there?

Note
m and n will be at most 100.
```

## 题解

题目要求：给定*m x n*矩阵，求左上角到右下角的路径总数，每次只能向左或者向右前进。按照动态规划中矩阵类问题的通用方法：

1. State: f[m][n] 从起点到坐标(m,n)的路径数目
2. Function: f[m][n] = f[m-1][n] + f[m][n-1] 分析终点与左边及右边节点的路径数，发现从左边或者右边到达终点的路径一定不会重合，相加即为唯一的路径总数
3. Initialization: f[i][j] = 1, 到矩阵中任一节点均至少有一条路径，其实关键之处在于给第0行和第0列初始化，免去了单独遍历第0行和第0列进行初始化
4. Answer: f[m - 1][n - 1]

### C++

```c++
class Solution {
public:
    /**
     * @param n, m: positive integer (1 <= n ,m <= 100)
     * @return an integer
     */
    int uniquePaths(int m, int n) {
        if (m < 1 || n < 1) {
            return 0;
        }

        vector<vector<int> > ret(m, vector<int>(n, 1));

        for (int i = 1; i != m; ++i) {
            for (int j = 1; j != n; ++j) {
                ret[i][j] = ret[i - 1][j] + ret[i][j - 1];
            }
        }

        return ret[m - 1][n - 1];
    }
};
```

### 源码分析

1. 异常处理，虽然题目有保证为正整数，但还是判断一下以防万一
2. 初始化二维矩阵，值均为1
3. 按照转移矩阵函数进行累加
4. 任何`ret[m - 1][n - 1]`
