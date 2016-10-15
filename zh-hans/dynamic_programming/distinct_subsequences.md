# Distinct Subsequences

Tags: Dynamic Programming, String, Hard

## Question

- leetcode: [Distinct Subsequences](https://leetcode.com/problems/distinct-subsequences/)
- lintcode: [Distinct Subsequences](http://www.lintcode.com/en/problem/distinct-subsequences/)

### Problem Statement

Given a string **S** and a string **T**, count the number of distinct
subsequences of **T** in **S**.

A subsequence of a string is a new string which is formed from the original
string by deleting some (can be none) of the characters without disturbing the
relative positions of the remaining characters. (ie, `"ACE"` is a subsequence
of `"ABCDE"` while `"AEC"` is not).

Here is an example:  
**S** = `"rabbbit"`, **T** = `"rabbit"`

Return `3`.

## 题解1

首先分清 subsequence 和 substring 两者的区别，subsequence 可以是不连续的子串。题意要求 S 中子序列 T 的个数。如果不考虑程序实现，我们能想到的办法是逐个比较 S 和 T 的首字符，相等的字符删掉，不等时则删除 S 中的首字符，继续比较后续字符直至 T 中字符串被删完。这种简单的思路有这么几个问题，题目问的是子序列的个数，而不是是否存在，故在字符不等时不能轻易删除掉 S 中的字符。那么如何才能得知子序列的个数呢？

要想得知不同子序列的个数，那么我们就不能在 S 和 T 中首字符不等时简单移除 S 中的首字符了，取而代之的方法应该是先将 S 复制一份，再用移除 S 中首字符后的新字符串和 T 进行比较，这点和深搜中的剪枝函数的处理有点类似。

### Python

```python
class Solution:
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, S, T):
        if S is None or T is None:
            return 0
        if len(S) < len(T):
            return 0
        if len(T) == 0:
            return 1

        num = 0
        for i, Si in enumerate(S):
            if Si == T[0]:
                num += self.numDistinct(S[i + 1:], T[1:])

        return num
```

### C++

```c++
class Solution {
public:
    /**
     * @param S, T: Two string.
     * @return: Count the number of distinct subsequences
     */
    int numDistinct(string &S, string &T) {
        if (S.size() < T.size()) return 0;
        if (T.empty()) return 1;

        int num = 0;
        for (int i = 0; i < S.size(); ++i) {
            if (S[i] == T[0]) {
                string Si = S.substr(i + 1);
                string t = T.substr(1);
                num += numDistinct(Si, t);
            }
        }

        return num;
    }
};
```

### Java

```java
public class Solution {
    /**
     * @param S, T: Two string.
     * @return: Count the number of distinct subsequences
     */
    public int numDistinct(String S, String T) {
        if (S == null || T == null) return 0;
        if (S.length() < T.length()) return 0;
        if (T.length() == 0) return 1;

        int num = 0;
        for (int i = 0; i < S.length(); i++) {
            if (S.charAt(i) == T.charAt(0)) {
                // T.length() >= 1, T.substring(1) will not throw index error
                num += numDistinct(S.substring(i + 1), T.substring(1));
            }
        }

        return num;
    }
}
```

### 源码分析

1. 对 null 异常处理(C++ 中对 string 赋NULL 是错的，函数内部无法 handle 这种情况)
2. S 字符串长度若小于 T 字符串长度，T 必然不是 S 的子序列，返回0
3. T 字符串长度为0，证明 T 是 S 的子序列，返回1

由于进入 for 循环的前提是 `T.length() >= 1`, 故当 T 的长度为1时，Java 中对 T 取子串`T.substring(1)`时产生的是空串`""`而并不抛出索引越界的异常。

### 复杂度分析

最好情况下，S 中没有和 T 相同的字符，时间复杂度为 $$O(n)$$; 最坏情况下，S 中的字符和 T 中字符完全相同，此时可以画出递归调用栈，发现和深搜非常类似，数学关系为 $$f(n) = \sum _{i = 1} ^{n - 1} f(i)$$, 这比 Fibonacci 的复杂度还要高很多。

## 题解2 - Dynamic Programming

从题解1 的复杂度分析中我们能发现由于存在较多的重叠子状态(相同子串被比较多次), 因此可以想到使用动态规划优化。但是动规的三大要素如何建立？由于本题为两个字符串之间的关系，故可以尝试使用双序列(DP_Two_Sequence)动规的思路求解。

定义`f[i][j]`为 S[0:i] 中子序列为 T[0:j] 的个数，接下来寻找状态转移关系，状态转移应从 f[i-1][j], f[i-1][j-1], f[i][j-1] 中寻找，接着寻找突破口——S[i] 和 T[j] 的关系。

1. `S[i] == T[j]`: 两个字符串的最后一个字符相等，我们可以选择 S[i] 和 T[j] 配对，那么此时有 f[i][j] = f[i-1][j-1]; 若不使 S[i] 和 T[j] 配对，而是选择 S[0:i-1] 中的某个字符和 T[j] 配对，那么 f[i][j] = f[i-1][j]. 综合以上两种选择，可得知在`S[i] == T[j]`时有 f[i][j] = f[i-1][j-1] + f[i-1][j]
2. `S[i] != T[j]`: 最后一个字符不等时，S[i] 不可能和 T[j] 配对，故 f[i][j] = f[i-1][j]

为便于处理第一个字符相等的状态(便于累加)，初始化f[i][0]为1, 其余为0. 这里对于 S 或 T 为空串时返回0，返回1 也能说得过去。

### Python

```python
class Solution:
    # @param S, T: Two string.
    # @return: Count the number of distinct subsequences
    def numDistinct(self, S, T):
        if S is None or T is None:
            return 0
        if len(S) < len(T):
            return 0
        if len(T) == 0:
            return 1

        f = [[0 for i in xrange(len(T) + 1)] for j in xrange(len(S) + 1)]
        for i, Si in enumerate(S):
            f[i][0] = 1
            for j, Tj in enumerate(T):
                if Si == Tj:
                    f[i + 1][j + 1] = f[i][j + 1] + f[i][j]
                else:
                    f[i + 1][j + 1] = f[i][j + 1]

        return f[len(S)][len(T)]
```

### C++

```c++
class Solution {
public:
    /**
     * @param S, T: Two string.
     * @return: Count the number of distinct subsequences
     */
    int numDistinct(string &S, string &T) {
        if (S.size() < T.size()) return 0;
        if (T.empty()) return 1;

        vector<vector<int> > f(S.size() + 1, vector<int>(T.size() + 1, 0));
        for (int i = 0; i < S.size(); ++i) {
            f[i][0] = 1;
            for (int j = 0; j < T.size(); ++j) {
                if (S[i] == T[j]) {
                    f[i + 1][j + 1] = f[i][j + 1] + f[i][j];
                } else {
                    f[i + 1][j + 1] = f[i][j + 1];
                }
            }
        }

        return f[S.size()][T.size()];
    }
};
```

### Java

```java
public class Solution {
    /**
     * @param S, T: Two string.
     * @return: Count the number of distinct subsequences
     */
    public int numDistinct(String S, String T) {
        if (S == null || T == null) return 0;
        if (S.length() < T.length()) return 0;
        if (T.length() == 0) return 1;

        int[][] f = new int[S.length() + 1][T.length() + 1];
        for (int i = 0; i < S.length(); i++) {
            f[i][0] = 1;
            for (int j = 0; j < T.length(); j++) {
                if (S.charAt(i) == T.charAt(j)) {
                    f[i + 1][j + 1] = f[i][j + 1] + f[i][j];
                } else {
                    f[i + 1][j + 1] = f[i][j + 1];
                }
            }
        }

        return f[S.length()][T.length()];
    }
}
```

### 源码分析

异常处理部分和题解1 相同，初始化时维度均多一个元素便于处理。

### 复杂度分析

由于免去了重叠子状态的计算，双重 for 循环，时间复杂度为 $$O(n^2)$$, 使用了二维矩阵保存状态，空间复杂度为 $$O(n^2)$$. 空间复杂度可以通过滚动数组的方式优化，详见 [Dynamic Programming - 动态规划](http://algorithm.yuanbin.me/zh-hans/dynamic_programming/index.html).

空间复杂度优化之后的代码如下：

#### Java

```java
public class Solution {
    /**
     * @param S, T: Two string.
     * @return: Count the number of distinct subsequences
     */
    public int numDistinct(String S, String T) {
        if (S == null || T == null) return 0;
        if (S.length() < T.length()) return 0;
        if (T.length() == 0) return 1;
        
        int[] f = new int[T.length() + 1];
        f[0] = 1;
        for (int i = 0; i < S.length(); i++) {
            for (int j = T.length() - 1; j >= 0; j--) {
                if (S.charAt(i) == T.charAt(j)) {
                        f[j + 1] += f[j];
                }
            }
        }
        
        return f[T.length()];
    }
}
```

## Reference

- [LeetCode: Distinct Subsequences（不同子序列的个数） - 亦忘却_亦纪念](http://blog.csdn.net/abcbc/article/details/8978146)
- soulmachine leetcode-cpp 中 Distinct Subsequences 部分
- [Distinct Subsequences | Training dragons the hard way](http://traceformula.blogspot.com/2015/08/distinct-subsequences.html)
