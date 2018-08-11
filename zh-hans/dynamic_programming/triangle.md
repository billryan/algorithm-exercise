# Triangle - Find the minimum path sum from top to bottom

## Question

- leetcode: [Triangle | LeetCode OJ](https://leetcode.com/problems/triangle/)
- lintcode: [(109) Triangle](http://www.lintcode.com/en/problem/triangle/)

```
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

Note
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

Example
For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
```

## 题解

题中要求最短路径和，每次只能访问下行的相邻元素，将triangle视为二维坐标。此题方法较多，下面分小节详述。

### Method 1 - Traverse without hashmap

首先考虑最容易想到的方法——递归遍历，逐个累加所有自上而下的路径长度，最后返回这些不同的路径长度的最小值。由于每个点往下都有2条路径，使用此方法的时间复杂度约为 $$O(2^n)$$, 显然是不可接受的解，不过我们还是先看看其实现思路。

### C++ Traverse without hashmap

```c++
class Solution {
public:
    /**
     * @param triangle: a list of lists of integers.
     * @return: An integer, minimum path sum.
     */
    int minimumTotal(vector<vector<int> > &triangle) {
        if (triangle.empty()) {
            return -1;
        }

        int result = INT_MAX;
        dfs(0, 0, 0, triangle, result);

        return result;
    }

private:
    void dfs(int x, int y, int sum, vector<vector<int> > &triangle, int &result) {
        const int n = triangle.size();
        if (x == n) {
            if (sum < result) {
                result = sum;
            }
            return;
        }

        dfs(x + 1, y, (sum + triangle[x][y]), triangle, result);
        dfs(x + 1, y + 1, (sum + triangle[x][y]), triangle, result);
    }
};
```

### 源码分析

`dfs()`的循环终止条件为`x == n`，而不是`x == n - 1`，主要是方便在递归时sum均可使用`sum + triangle[x][y]`，而不必根据不同的y和y+1改变，代码实现相对优雅一些。理解方式则变为从第x行走到第x+1行时的最短路径和，也就是说在此之前并不将第x行的元素值计算在内。

这种遍历的方法时间复杂度如此之高的主要原因是因为在n较大时递归计算了之前已经得到的结果，而这些结果计算一次后即不再变化，可再次利用。因此我们可以使用hashmap记忆已经计算得到的结果从而对其进行优化。

### Method 2 - Divide and Conquer without hashmap

既然可以使用递归遍历，当然也可以使用「分治」的方法来解。「分治」与之前的遍历区别在于「分治」需要返回每次「分治」后的计算结果，下面看代码实现。

### C++ Divide and Conquer without hashmap

```c++
class Solution {
public:
    /**
     * @param triangle: a list of lists of integers.
     * @return: An integer, minimum path sum.
     */
    int minimumTotal(vector<vector<int> > &triangle) {
        if (triangle.empty()) {
            return -1;
        }

        int result = dfs(0, 0, triangle);

        return result;
    }

private:
    int dfs(int x, int y, vector<vector<int> > &triangle) {
        const int n = triangle.size();
        if (x == n) {
            return 0;
        }

        return min(dfs(x + 1, y, triangle), dfs(x + 1, y + 1, triangle))  + triangle[x][y];
    }
};
```

使用「分治」的方法代码相对简洁一点，接下来我们使用hashmap保存triangle中不同坐标的点计算得到的路径和。

### Method 3 - Divide and Conquer with hashmap

新建一份大小和triangle一样大小的hashmap，并对每个元素赋以`INT_MIN`以做标记区分。

### C++ Divide and Conquer with hashmap

```c++
class Solution {
public:
    /**
     * @param triangle: a list of lists of integers.
     * @return: An integer, minimum path sum.
     */
    int minimumTotal(vector<vector<int> > &triangle) {
        if (triangle.empty()) {
            return -1;
        }

        vector<vector<int> > hashmap(triangle);
        for (int i = 0; i != hashmap.size(); ++i) {
            for (int j = 0; j != hashmap[i].size(); ++j) {
                hashmap[i][j] = INT_MIN;
            }
        }
        int result = dfs(0, 0, triangle, hashmap);

        return result;
    }

private:
    int dfs(int x, int y, vector<vector<int> > &triangle, vector<vector<int> > &hashmap) {
        const int n = triangle.size();
        if (x == n) {
            return 0;
        }

        // INT_MIN means no value yet
        if (hashmap[x][y] != INT_MIN) {
            return hashmap[x][y];
        }
        int x1y = dfs(x + 1, y, triangle, hashmap);
        int x1y1 = dfs(x + 1, y + 1, triangle, hashmap);
        hashmap[x][y] =  min(x1y, x1y1) + triangle[x][y];

        return hashmap[x][y];
    }
};
```

由于已经计算出的最短路径值不再重复计算，计算复杂度由之前的 $$O(2^n)$$，变为 $$O(n^2)$$, 每个坐标的元素仅计算一次，故共计算的次数为 $$1+2+...+n \approx O(n^2)$$.

### Method 4 - Dynamic Programming

从主章节中对动态规划的简介我们可以知道使用动态规划的难点和核心在于**状态的定义及转化方程的建立**。那么问题来了，到底如何去找适合这个问题的状态及转化方程呢？

我们仔细分析题中可能的状态和转化关系，发现从`triangle`中坐标为 $$triangle[x][y]$$ 的元素出发，其路径只可能为 $$triangle[x][y]->triangle[x+1][y]$$ 或者 $$triangle[x][y]->triangle[x+1][y+1]$$. 以点 $$(x,y)$$ 作为参考，那么可能的状态 $$f(x,y)$$ 就可以是：

1. 从 $$(x,y)$$ 出发走到最后一行的最短路径和
2. 从 $$(0,0)$$ 走到 $$(x,y)$$的最短路径和

如果选择1作为状态，则相应的状态转移方程为：
$$f_1(x,y) = min\{f_1(x+1, y), f_1(x+1, y+1)\} + triangle[x][y]$$

如果选择2作为状态，则相应的状态转移方程为：
$$f_2(x,y) = min\{f_2(x-1, y), f_2(x-1, y-1)\} + triangle[x][y]$$

两个状态所对应的初始状态分别为 $$f_1(n-1, y), 0 \leq y \leq n-1$$ 和 $$f_2(0,0)$$. 在代码中应注意考虑边界条件。下面分别就这种不同的状态进行动态规划。

### C++ From Bottom to Top

```c++
class Solution {
public:
    /**
     * @param triangle: a list of lists of integers.
     * @return: An integer, minimum path sum.
     */
    int minimumTotal(vector<vector<int> > &triangle) {
        if (triangle.empty()) {
            return -1;
        }

        vector<vector<int> > hashmap(triangle);

        // get the total row number of triangle
        const int N = triangle.size();
        for (int i = 0; i != N; ++i) {
            hashmap[N-1][i] = triangle[N-1][i];
        }

        for (int i = N - 2; i >= 0; --i) {
            for (int j = 0; j < i + 1; ++j) {
                hashmap[i][j] = min(hashmap[i + 1][j], hashmap[i + 1][j + 1]) + triangle[i][j];
            }
        }

        return hashmap[0][0];
    }
};
```

### 源码分析

1. 异常处理
2. 使用hashmap保存结果
3. 初始化`hashmap[N-1][i]`, 由于是自底向上，故初始化时保存最后一行元素
4. 使用自底向上的方式处理循环
5. 最后返回结果hashmap[0][0]

从空间利用角度考虑也可直接使用triangle替代hashmap，但是此举会改变triangle的值，不推荐。

### C++ From Top to Bottom

```c++
class Solution {
public:
    /**
     * @param triangle: a list of lists of integers.
     * @return: An integer, minimum path sum.
     */
    int minimumTotal(vector<vector<int> > &triangle) {
        if (triangle.empty()) {
            return -1;
        }

        vector<vector<int> > hashmap(triangle);

        // get the total row number of triangle
        const int N = triangle.size();
        //hashmap[0][0] = triangle[0][0];
        for (int i = 1; i != N; ++i) {
            for (int j = 0; j <= i; ++j) {
                if (j == 0) {
                    hashmap[i][j] = hashmap[i - 1][j];
                }
                if (j == i) {
                    hashmap[i][j] = hashmap[i - 1][j - 1];
                }
                if ((j > 0) && (j < i)) {
                    hashmap[i][j] = min(hashmap[i - 1][j], hashmap[i - 1][j - 1]);
                }
                hashmap[i][j] += triangle[i][j];
            }
        }

        int result = INT_MAX;
        for (int i = 0; i != N; ++i) {
            result = min(result, hashmap[N - 1][i]);
        }
        return result;
    }
};
```

#### 源码解析

自顶向下的实现略微有点复杂，在寻路时需要考虑最左边和最右边的边界，还需要在最后返回结果时比较最小值。

### Java From Top to Bottom

```java
public class Solution {
    /**
     * @param triangle: a list of lists of integers.
     * @return: An integer, minimum path sum.
     */
    public int minimumTotal(int[][] triangle) {
        // write your code here
        if (triangle == null || triangle.length == 0) return 0;
        int[] last = new int[triangle.length];
        int[] current = new int[triangle.length];
        last[0] = triangle[0][0];
        current[0] = last[0];
        for (int i = 1; i < triangle.length; i++) {
            for (int j = 0; j < i + 1; j++) {
                int sum = Integer.MAX_VALUE;
                if (j != 0) {
                    sum = triangle[i][j] + last[j - 1];
                }
                if (j != i) {
                    sum = Math.min(sum, triangle[i][j] + last[j]);
                }
                current[j] = sum;
            }
            for (int k = 0; k < i + 1; k++) last[k] = current[k];
        }
        int min = Integer.MAX_VALUE;
        for (int n : current) {
            min = Math.min(n, min);
        }
        return min;
    }
}
```

#### 源码解析

思路基本和上个解法一样，但是在数组last中保留上一层的最短和的，因此不用hashmap，空间复杂度是O(n)
