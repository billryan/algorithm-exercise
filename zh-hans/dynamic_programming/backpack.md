# Backpack

## Question

- lintcode: [(92) Backpack](http://www.lintcode.com/en/problem/backpack/)

### Problem Statement

Given _n_ items with size $$A_i$$, an integer _m_ denotes the size of a backpack.
How full you can fill this backpack?

#### Example

If we have `4` items with size `[2, 3, 5, 7]`, the backpack size is 11, we can
select `[2, 3, 5]`, so that the max size we can fill this backpack is `10`. If
the backpack size is `12`. we can select `[2, 3, 7]` so that we can fulfill
the backpack.

You function should return the max size we can fill in the given backpack.

#### Note

You can not divide any item into small pieces.

#### Challenge

O(n x m) time and O(m) memory.

O(n x m) memory is also acceptable if you do not know how to optimize memory.

## 题解1

本题是典型的01背包问题，每种类型的物品最多只能选择一件。参考前文 [Knapsack](http://algorithm.yuanbin.me/zh-hans/basics_algorithm/knapsack.html) 中总结的解法，这个题中可以将背包的 size 理解为传统背包中的重量；题目问的是能达到的最大 size, 故可将每个背包的 size 类比为传统背包中的价值。

考虑到数组索引从0开始，故定义状态`bp[i + 1][j]`为前 `i` 个物品中选出重量不超过`j`时总价值的最大值。状态转移方程则为分`A[i] > j` 与否两种情况考虑。初始化均为0，相当于没有放任何物品。

### Java

```java
public class Solution {
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A: Given n items with size A[i]
     * @return: The maximum size
     */
    public int backPack(int m, int[] A) {
        if (A == null || A.length == 0) return 0;

        final int M = m;
        final int N = A.length;
        int[][] bp = new int[N + 1][M + 1];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j <= M; j++) {
                if (A[i] > j) {
                    bp[i + 1][j] = bp[i][j];
                } else {
                    bp[i + 1][j] = Math.max(bp[i][j], bp[i][j - A[i]] + A[i]);
                }
            }
        }

        return bp[N][M];
    }
}
```

### 源码分析

注意索引及初始化的值，尤其是 N 和 M 的区别，内循环处可等于 M。

### 复杂度分析

两重 for 循环，时间复杂度为 $$O(m \times n)$$, 二维矩阵的空间复杂度为 $$O(m \times n)$$, 一维矩阵的空间复杂度为 $$O(m)$$.

## 题解2

接下来看看 [九章算法](http://www.jiuzhang.com/solutions/backpack/) 的题解，**这种解法感觉不是很直观，推荐使用题解1的解法。**

1. 状态: result[i][S] 表示前i个物品，取出一些物品能否组成体积和为S的背包
2. 状态转移方程: $$f[i][S] = f[i-1][S-A[i]] ~or~ f[i-1][S]$$ (A[i]为第i个物品的大小)
    - 欲从前i个物品中取出一些组成体积和为S的背包，可从两个状态转换得到。
        1. $$f[i-1][S-A[i]]$$: **放入第i个物品**，前 $$i-1$$ 个物品能否取出一些体积和为 $$S-A[i]$$ 的背包。
        2. $$f[i-1][S]$$: **不放入第i个物品**，前 $$i-1$$ 个物品能否取出一些组成体积和为S的背包。
3. 状态初始化: $$f[1 \cdots n][0]=true; ~f[0][1 \cdots m]=false$$. 前1~n个物品组成体积和为0的背包始终为真，其他情况为假。
4. 返回结果: 寻找使 $$f[n][S]$$ 值为true的最大S ($$1 \leq S \leq m$$)

### C++ - 2D vector

```c++
class Solution {
public:
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A: Given n items with size A[i]
     * @return: The maximum size
     */
    int backPack(int m, vector<int> A) {
        if (A.empty() || m < 1) {
            return 0;
        }

        const int N = A.size() + 1;
        const int M = m + 1;
        vector<vector<bool> > result;
        result.resize(N);
        for (vector<int>::size_type i = 0; i != N; ++i) {
            result[i].resize(M);
            std::fill(result[i].begin(), result[i].end(), false);
        }

        result[0][0] = true;
        for (int i = 1; i != N; ++i) {
            for (int j = 0; j != M; ++j) {
                if (j < A[i - 1]) {
                    result[i][j] = result[i - 1][j];
                } else {
                    result[i][j] = result[i - 1][j] || result[i - 1][j - A[i - 1]];
                }
            }
        }

        // return the largest i if true
        for (int i = M; i > 0; --i) {
            if (result[N - 1][i - 1]) {
                return (i - 1);
            }
        }
        return 0;
    }
};
```

### 源码分析

1. 异常处理
2. 初始化结果矩阵，注意这里需要使用`resize`而不是`reserve`，否则可能会出现段错误
3. 实现状态转移逻辑，一定要分`j < A[i - 1]`与否来讨论
4. 返回结果，只需要比较`result[N - 1][i - 1]`的结果，返回true的最大值

状态转移逻辑中代码可以进一步简化，即：

```
        for (int i = 1; i != N; ++i) {
            for (int j = 0; j != M; ++j) {
                result[i][j] = result[i - 1][j];
                if (j >= A[i - 1] && result[i - 1][j - A[i - 1]]) {
                    result[i][j] = true;
                }
            }
        }
```

考虑背包问题的核心——状态转移方程，如何优化此转移方程？原始方案中用到了二维矩阵来保存result，注意到result的第i行仅依赖于第i-1行的结果，那么能否用一维数组来代替这种隐含的关系呢？我们**在内循环j处递减即可**。如此即可避免`result[i][S]`的值由本轮`result[i][S-A[i]]`递推得到。

### C++ - 1D vector

```c++
class Solution {
public:
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A: Given n items with size A[i]
     * @return: The maximum size
     */
    int backPack(int m, vector<int> A) {
        if (A.empty() || m < 1) {
            return 0;
        }

        const int N = A.size();
        vector<bool> result;
        result.resize(m + 1);
        std::fill(result.begin(), result.end(), false);

        result[0] = true;
        for (int i = 0; i != N; ++i) {
            for (int j = m; j >= 0; --j) {
                if (j >= A[i] && result[j - A[i]]) {
                    result[j] = true;
                }
            }
        }

        // return the largest i if true
        for (int i = m; i > 0; --i) {
            if (result[i]) {
                return i;
            }
        }
        return 0;
    }
};
```

### 复杂度分析

两重 for 循环，时间复杂度均为 $$O(m \times n)$$, 二维矩阵的空间复杂度为 $$O(m \times n)$$, 一维矩阵的空间复杂度为 $$O(m)$$.

## Reference

- 《挑战程序设计竞赛》第二章
- [Lintcode: Backpack - neverlandly - 博客园](http://www.cnblogs.com/EdwardLiu/p/4269149.html)
- [九章算法 | 背包问题](http://www.jiuzhang.com/problem/58/)
- [崔添翼 § 翼若垂天之云 › 《背包问题九讲》2.0 alpha1](http://cuitianyi.com/blog/%E3%80%8A%E8%83%8C%E5%8C%85%E9%97%AE%E9%A2%98%E4%B9%9D%E8%AE%B2%E3%80%8B2-0-alpha1/)
