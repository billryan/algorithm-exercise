# Unique Paths II

- tags: [DP_Matrix]

## Question

- lintcode: [(115) Unique Paths II](http://www.lintcode.com/en/problem/unique-paths-ii/)

```
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids.
How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.
Note
m and n will be at most 100.

Example
For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.
```

## 题解

在上题的基础上加了obstacal这么一个限制条件，那么也就意味着凡是遇到障碍点，其路径数马上变为0，需要注意的是初始化环节和上题有较大不同。首先来看看错误的初始化实现。

### C++ initialization error

```c++
class Solution {
public:
    /**
     * @param obstacleGrid: A list of lists of integers
     * @return: An integer
     */
    int uniquePathsWithObstacles(vector<vector<int> > &obstacleGrid) {
        if(obstacleGrid.empty() || obstacleGrid[0].empty()) {
            return 0;
        }

        const int M = obstacleGrid.size();
        const int N = obstacleGrid[0].size();

        vector<vector<int> > ret(M, vector<int>(N, 0));

        for (int i = 0; i != M; ++i) {
            if (0 == obstacleGrid[i][0]) {
                ret[i][0] = 1;
            }
        }
        for (int i = 0; i != N; ++i) {
            if (0 == obstacleGrid[0][i]) {
                ret[0][i] = 1;
            }
        }

        for (int i = 1; i != M; ++i) {
            for (int j = 1; j != N; ++j) {
                if (obstacleGrid[i][j]) {
                    ret[i][j] = 0;
                } else {
                    ret[i][j] = ret[i -1][j] + ret[i][j - 1];
                }
            }
        }

        return ret[M - 1][N - 1];
    }
};
```

### 源码分析

错误之处在于初始化第0行和第0列时，未考虑到若第0行/列有一个坐标出现障碍物，则当前行/列后的元素路径数均为0！

### C++

```c++
class Solution {
public:
    /**
     * @param obstacleGrid: A list of lists of integers
     * @return: An integer
     */
    int uniquePathsWithObstacles(vector<vector<int> > &obstacleGrid) {
        if(obstacleGrid.empty() || obstacleGrid[0].empty()) {
            return 0;
        }

        const int M = obstacleGrid.size();
        const int N = obstacleGrid[0].size();

        vector<vector<int> > ret(M, vector<int>(N, 0));

        for (int i = 0; i != M; ++i) {
            if (obstacleGrid[i][0]) {
                break;
            } else {
                ret[i][0] = 1;
            }
        }
        for (int i = 0; i != N; ++i) {
            if (obstacleGrid[0][i]) {
                break;
            } else {
                ret[0][i] = 1;
            }
        }

        for (int i = 1; i != M; ++i) {
            for (int j = 1; j != N; ++j) {
                if (obstacleGrid[i][j]) {
                    ret[i][j] = 0;
                } else {
                    ret[i][j] = ret[i -1][j] + ret[i][j - 1];
                }
            }
        }

        return ret[M - 1][N - 1];
    }
};
```

### 源码分析

1. 异常处理
2. 初始化二维矩阵(全0阵)，尤其注意遇到障碍物时应`break`跳出当前循环
3. 递推路径数
4. 返回`ret[M - 1][N - 1]`
