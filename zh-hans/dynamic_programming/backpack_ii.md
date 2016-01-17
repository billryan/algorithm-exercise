# Backpack II

## Question

- lintcode: [(125) Backpack II](http://www.lintcode.com/en/problem/backpack-ii/)

### Problem Statement

Given _n_ items with size $$Ai$$ and value Vi, and a backpack with size _m_.
What's the maximum value can you put into the backpack?

#### Example

Given 4 items with size `[2, 3, 5, 7]` and value `[1, 5, 2, 4]`, and a
backpack with size `10`. The maximum value is `9`.

#### Note

You cannot divide item into small pieces and the total size of items you
choose should smaller or equal to m.

#### Challenge

O(n x m) memory is acceptable, can you do it in O(m) memory?

## 题解

首先定义状态 $$K(i,w)$$ 为前 $$i$$ 个物品放入size为 $$w$$ 的背包中所获得的最大价值，则相应的状态转移方程为：
$$K(i,w) = \max \{K(i-1, w), K(i-1, w - w_i) + v_i\}$$

详细分析过程见 [Knapsack](http://algorithm.yuanbin.me/zh-hans/basics_algorithm/knapsack.html)

### C++ - 2D vector for result

```c++
class Solution {
public:
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A & V: Given n items with size A[i] and value V[i]
     * @return: The maximum value
     */
    int backPackII(int m, vector<int> A, vector<int> V) {
        if (A.empty() || V.empty() || m < 1) {
            return 0;
        }
        const int N = A.size() + 1;
        const int M = m + 1;
        vector<vector<int> > result;
        result.resize(N);
        for (vector<int>::size_type i = 0; i != N; ++i) {
            result[i].resize(M);
            std::fill(result[i].begin(), result[i].end(), 0);
        }

        for (vector<int>::size_type i = 1; i != N; ++i) {
            for (int j = 0; j != M; ++j) {
                if (j < A[i - 1]) {
                    result[i][j] = result[i - 1][j];
                } else {
                    int temp = result[i - 1][j - A[i - 1]] + V[i - 1];
                    result[i][j] = max(temp, result[i - 1][j]);
                }
            }
        }

        return result[N - 1][M - 1];
    }
};
```

### Java

```java
public class Solution {
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A & V: Given n items with size A[i] and value V[i]
     * @return: The maximum value
     */
    public int backPackII(int m, int[] A, int V[]) {
        if (A == null || V == null || A.length == 0 || V.length == 0) return 0;
        
        final int N = A.length;
        final int M = m;
        int[][] bp = new int[N + 1][M + 1];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j <= M; j++) {
                if (A[i] > j) {
                    bp[i + 1][j] = bp[i][j];
                } else {
                    bp[i + 1][j] = Math.max(bp[i][j], bp[i][j - A[i]] + V[i]);
                }
            }
        }
        
        return bp[N][M];
    }
}
```

### 源码分析

1. 使用二维矩阵保存结果result
2. 返回result矩阵的右下角元素——背包size限制为m时的最大价值

按照第一题backpack的思路，这里可以使用一维数组进行空间复杂度优化。优化方法为逆序求`result[j]`，优化后的代码如下：

### C++ 1D vector for result

```c++
class Solution {
public:
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A & V: Given n items with size A[i] and value V[i]
     * @return: The maximum value
     */
    int backPackII(int m, vector<int> A, vector<int> V) {
        if (A.empty() || V.empty() || m < 1) {
            return 0;
        }

        const int M = m + 1;
        vector<int> result;
        result.resize(M);
        std::fill(result.begin(), result.end(), 0);

        for (vector<int>::size_type i = 0; i != A.size(); ++i) {
            for (int j = m; j >= 0; --j) {
                if (j < A[i]) {
                    // result[j] = result[j];
                } else {
                    int temp = result[j - A[i]] + V[i];
                    result[j] = max(temp, result[j]);
                }
            }
        }

        return result[M - 1];
    }
};
```

## Reference

- [Lintcode: Backpack II - neverlandly - 博客园](http://www.cnblogs.com/EdwardLiu/p/4272300.html)
- [九章算法 | 背包问题](http://www.jiuzhang.com/problem/58/)
