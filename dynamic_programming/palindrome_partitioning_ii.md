# Palindrome Partitioning II

- category: [DP_Sequence]

## Source

- leetcode: [Palindrome Partitioning II | LeetCode OJ](https://leetcode.com/problems/palindrome-partitioning-ii/)
- lintcode: [(108) Palindrome Partitioning II](http://www.lintcode.com/en/problem/palindrome-partitioning-ii/)

```
Given a string s, cut s into some substrings such that 
every substring is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example
For example, given s = "aab",

Return 1 since the palindrome partitioning ["aa","b"] could be produced 
using 1 cut.
```

## 题解

此题为难题，费了我九牛二虎之力才bug-free :( 求最小切分数，非常明显的动规暗示，两重单序列动态规划。由问题出发可建立状态`f[i]` 表示到索引`i` 处时需要的最少切割数(即切割前 i 个字符组成的字符串)，状态转移方程为`f[i] = min{1 + f[j]}, where j < i and substring [j, i] is palindrome`, 判断区间[j, i] 是否为回文简单的方法可反转后比较，但是这样一来会导致大量重复的计算，大量数据时过不了 OJ，所以在判断字符串是否为回文时也应使用动态规划！定义状态 PaMat[i][j]  为区间 `[i,j]` 是否为回文的标志, 状态转移方程 `PaMat[i][j] = str[i] == str[j] && PaMat[i+1][j-1]`, 实际实现中需要考虑一些边界条件和初始化方式，做到 bug-free 需要点时间。

### Python

```python
class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        if not s:
            print 0

        cut = [i - 1 for i in xrange(1 + len(s))]
        PaMatrix = self.getMat(s)

        for i in xrange(1 + len(s)):
            for j in xrange(i):
                if PaMatrix[j][i - 1]:
                    cut[i] = min(cut[i], cut[j] + 1)
        return cut[-1]

    def getMat(self, s):
        PaMat = [[True for i in xrange(len(s))] for j in xrange(len(s))]
        for i in xrange(len(s), -1, -1):
            for j in xrange(i, len(s)):
                if j == i:
                    PaMat[i][j] = True
		# not necessary if init with True
                # elif j == i + 1:
                #     PaMat[i][j] = s[i] == s[j]
                else:
                    PaMat[i][j] = s[i] == s[j] and PaMat[i + 1][j - 1]
        return PaMat
```

### 源码分析

初始化 cut 长度为`1 + len(s)`, `cut[0] = -1` 便于状态转移方程实现。使用`getMat` 得到字符串区间的回文矩阵，由于cut 的长度为1+len(s), 两重 for 循环时需要注意索引的取值，这个地方非常容易错。

### 复杂度分析

最坏情况下每次 for 循环都遍历 n 次，时间复杂度近似为 $$O(n^2)$$, 使用了回文矩阵保存记忆化搜索结果，空间复杂度为 $$O(n^2)$$.

## Reference

- [Palindrome Partitioning II 参考程序 Java/C++/Python](http://www.jiuzhang.com/solutions/palindrome-partitioning-ii/)
- soulmachine 的 leetcode 题解
