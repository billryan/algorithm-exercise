# Longest Common Subsequence

- tags: [DP_Two_Sequence]

## Question

- lintcode: [(77) Longest Common Subsequence](http://www.lintcode.com/en/problem/longest-common-subsequence/)

```
Given two strings, find the longest common subsequence (LCS).

Your code should return the length of LCS.

Have you met this question in a real interview? Yes
Example
For "ABCD" and "EDCA", the LCS is "A" (or "D", "C"), return 1.

For "ABCD" and "EACB", the LCS is "AC", return 2.

Clarification
What's the definition of Longest Common Subsequence?

https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
http://baike.baidu.com/view/2020307.htm
```

## 题解

求最长公共子序列的数目，注意这里的子序列可以不是连续序列，务必问清楚题意。求『最长』类的题目往往与动态规划有点关系，这里是两个字符串，故应为双序列动态规划。

这道题的状态很容易找，不妨先试试以`f[i][j]`表示字符串 A 的前 `i` 位和字符串 B 的前 `j` 位的最长公共子序列数目，那么接下来试试寻找其状态转移方程。从实际例子`ABCD`和`EDCA`出发，首先初始化`f`的长度为字符串长度加1，那么有`f[0][0] = 0`, `f[0][*] = 0`, `f[*][0] = 0`, 最后应该返回`f[lenA][lenB]`. 即 f 中索引与字符串索引对应(字符串索引从1开始算起)，那么在A 的第一个字符与 B 的第一个字符相等时，`f[1][1] = 1 + f[0][0]`, 否则`f[1][1] = max(f[0][1], f[1][0])`。

推而广之，也就意味着若`A[i] == B[j]`, 则分别去掉这两个字符后，原 LCS 数目减一，那为什么一定是1而不是0或者2呢？因为不管公共子序列是以哪个字符结尾，在`A[i] == B[j]`时 LCS 最多只能增加1. 而在`A[i] != B[j]`时，由于`A[i]` 或者 `B[j]` 不可能同时出现在最终的 LCS 中，故这个问题可进一步缩小，`f[i][j] = max(f[i - 1][j], f[i][j - 1])`. 需要注意的是这种状态转移方程只依赖最终的 LCS 数目，而不依赖于公共子序列到底是以第几个索引结束。

### Python

```python
class Solution:
    """
    @param A, B: Two strings.
    @return: The length of longest common subsequence of A and B.
    """
    def longestCommonSubsequence(self, A, B):
        if not A or not B:
            return 0

        lenA, lenB = len(A), len(B)
        lcs = [[0 for i in xrange(1 + lenA)] for j in xrange(1 + lenB)]

        for i in xrange(1, 1 + lenA):
            for j in xrange(1, 1 + lenB):
                if A[i - 1] == B[j - 1]:
                    lcs[i][j] = 1 + lcs[i - 1][j - 1]
                else:
                    lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1])
        return lcs[lenA][lenB]
```

### C++

```c++
class Solution {
public:
    /**
     * @param A, B: Two strings.
     * @return: The length of longest common subsequence of A and B.
     */
    int longestCommonSubsequence(string A, string B) {
        if (A.empty()) return 0;
        if (B.empty()) return 0;

        int lenA = A.size();
        int lenB = B.size();
        vector<vector<int> > lcs = \
            vector<vector<int> >(1 + lenA, vector<int>(1 + lenB));

        for (int i = 1; i < 1 + lenA; i++) {
            for (int j = 1; j < 1 + lenB; j++) {
                if (A[i - 1] == B[j - 1]) {
                    lcs[i][j] = 1 + lcs[i - 1][j - 1];
                } else {
                    lcs[i][j] = max(lcs[i - 1][j], lcs[i][j - 1]);
                }
            }
        }

        return lcs[lenA][lenB];
    }
};
```

### Java

```java
 public class Solution {
    /**
     * @param A, B: Two strings.
     * @return: The length of longest common subsequence of A and B.
     */
    public int longestCommonSubsequence(String A, String B) {
        if (A == null || A.length() == 0) return 0;
        if (B == null || B.length() == 0) return 0;

        int lenA = A.length();
        int lenB = B.length();
        int[][] lcs = new int[1 + lenA][1 + lenB];

        for (int i = 1; i < 1 + lenA; i++) {
            for (int j = 1; j < 1 + lenB; j++) {
                if (A.charAt(i - 1) == B.charAt(j - 1)) {
                    lcs[i][j] = 1 + lcs[i - 1][j - 1];
                } else {
                    lcs[i][j] = Math.max(lcs[i - 1][j], lcs[i][j - 1]);
                }
            }
        }

        return lcs[lenA][lenB];
    }
}
```

### 源码分析

注意 Python 中的多维数组初始化方式，不可简单使用`[[0] * len(A)] * len(B)]`, 具体原因是因为 Python 中的对象引用方式 [^Stackoverflow]。

### 复杂度分析

两重for 循环，时间复杂度为 $$O(lenA \times lenB)$$, 使用了二维数组，空间复杂度也为 $$O(lenA \times lenB)$$. 

## Reference

- [^Stackoverflow]: [Python multi-dimensional array initialization without a loop - Stack Overflow](http://stackoverflow.com/questions/3662475/python-multi-dimensional-array-initialization-without-a-loop)
