# Longest Common Substring

Tags: String, LintCode Copyright, Medium

## Question

- lintcode: [Longest Common Substring](http://www.lintcode.com/en/problem/longest-common-substring/)

### Problem Statement

Given two strings, find the longest common substring.

Return the length of it.

#### Notice

The characters in **substring** should occur continuously in original string.
This is different with **subsequence**.

**Example**

Given A = `"ABCD"`, B = `"CBCE"`, return `2`.

**Challenge** ****

O(n x m) time and memory.

## 题解1 - 暴力枚举

求最长公共子串，注意「子串」和「子序列」的区别！简单考虑可以暴力使用两根指针索引分别指向两个字符串的当前遍历位置，若遇到相等的字符时则同时向后移动一位。

### Python

```python
class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        if not (A and B):
            return 0

        lcs = 0
        for i in range(len(A)):
            for j in range(len(B)):
                lcs_temp = 0
                while (i + lcs_temp < len(A) and
                       j + lcs_temp < len(B) and
                       A[i + lcs_temp] == B[j + lcs_temp]):
                    lcs_temp += 1
                # update lcs
                if lcs_temp > lcs:
                    lcs = lcs_temp
        return lcs
```

### C++

```cpp
class Solution {
public:    
    /**
     * @param A, B: Two string.
     * @return: the length of the longest common substring.
     */
    int longestCommonSubstring(string &A, string &B) {
        if (A.empty() || B.empty()) {
            return 0;
        }

        int lcs = 0;
        for (int i = 0; i < A.length(); ++i) {
            for (int j = 0; j < B.length(); ++j) {
                int lcs_temp = 0;
                while ((i + lcs_temp < A.length()) &&
                       (j + lcs_temp < B.length()) &&
                       (A[i + lcs_temp] == B[j + lcs_temp])) {
                    ++lcs_temp;
                }
                // update lcs
                if (lcs_temp > lcs) lcs = lcs_temp;
            }
        }

        return lcs;
    }
};
```

### Java

```java
public class Solution {
    /**
     * @param A, B: Two string.
     * @return: the length of the longest common substring.
     */
    public int longestCommonSubstring(String A, String B) {
        if ((A == null || A.isEmpty()) || 
            (B == null || B.isEmpty())) {
            return 0;
        }

        int lcs = 0;
        for (int i = 0; i < A.length(); i++) {
            for (int j = 0; j < B.length(); j++) {
                int lcs_temp = 0;
                while (i + lcs_temp < A.length() && 
                       j + lcs_temp < B.length() && 
                       A.charAt(i + lcs_temp) == B.charAt(j + lcs_temp)) {
                    lcs_temp++;
                }
                // update lcs
                if (lcs_temp > lcs) lcs = lcs_temp;
            }
        }

        return lcs;
    }
}
```

### 源码分析

1. 异常处理，空串时返回0.
2. 分别使用`i`和`j`表示当前遍历的索引处。若当前字符相同时则共同往后移动一位。
3. 没有相同字符时比较此次遍历的`lcs_temp`和`lcs`大小，更新`lcs`.
4. 返回`lcs`.

注意在`while`循环中不可直接使用`++i`或者`++j`，即两根指针依次向前移动，不能在内循环处更改，因为有可能会漏解！

### 复杂度分析

双重 for 循环，最坏时间复杂度约为 $$O(mn \cdot lcs)$$, lcs 最大可为 $$ \min{m, n} $$.

## 题解2 - 动态规划

题解1中使用了两根指针指向当前所取子串的起点，在实际比较过程中存在较多的重复计算，故可以考虑使用记忆化搜索或者动态规划对其进行优化。动态规划中状态的确定及其状态转移方程最为关键，如果直接以题目所求为状态，我们会发现其状态转移方程似乎写不出来，但退而求其次，我们不妨采用子串/子序列中常用的状态定义——『以(i,j)结尾(如 A[i-1], B[j-1])且其字符相等的子串lcs, 状态转移时只需判断两个字符串后一位字符是否相等，最后再次遍历二维状态数组即可。

### Python

```python
class Solution:
    # @param A, B: Two string.
    # @return: the length of the longest common substring.
    def longestCommonSubstring(self, A, B):
        if not (A and B):
            return 0

        n, m = len(A), len(B)
        f = [[0 for i in range(m + 1)] for j in range(n + 1)]
        for i in range(n):
            for j in range(m):
                if A[i] == B[j]:
                    f[i + 1][j + 1] = 1 + f[i][j]

        lcs = max(map(max, f))
        return lcs
```

### C++

```cpp
class Solution {
public:
    /**
     * @param A, B: Two string.
     * @return: the length of the longest common substring.
     */
    int longestCommonSubstring(string &A, string &B) {
        if (A.empty() || B.empty()) {
            return 0;
        }

        int n = A.length();
        int m = B.length();
        vector<vector<int> > f = vector<vector<int> >(n + 1, vector<int>(m + 1, 0));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (A[i] == B[j]) {
                    f[i + 1][j + 1] = 1 + f[i][j];
                }
            }
        }

        // find max lcs
        int lcs = 0;
        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                if (f[i][j] > lcs) lcs = f[i][j];
            }
        }

        return lcs;
    }
};
```

### Java

```java
public class Solution {
    /**
     * @param A, B: Two string.
     * @return: the length of the longest common substring.
     */
    public int longestCommonSubstring(String A, String B) {
        if ((A == null || A.isEmpty()) ||
            (B == null || B.isEmpty())) {
            return 0;
        }

        int n = A.length();
        int m = B.length();
        int[][] f = new int[n + 1][m + 1];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (A.charAt(i) == B.charAt(j)) {
                    f[i + 1][j + 1] = 1 + f[i][j];
                }
            }
        }

        // find max lcs
        int lcs = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                if (f[i][j] > lcs) lcs = f[i][j];
            }
        }

        return lcs;
    }
}
```

### 源码分析

1. 异常处理
2. 列出状态转移方程，关键处在于以 (i,j) 结尾的两个字符串

### 复杂度分析

两次双重 for 循环，时间复杂度约为 $$O(mn)$$, 空间复杂度为 $$O(mn)$$. 对于这个题而言，使用动态规划的思维其复杂度并未得到明显下降。

## Reference

- [Longest Common Substring | 九章算法](http://www.jiuzhang.com/solutions/longest-common-substring/)
