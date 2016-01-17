# Palindrome Partitioning II

- tags: [DP_Sequence]

## Question

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

## 题解1 - 仅对最小切割数使用动态规划

此题为难题，费了我九牛二虎之力才bug-free :( 求最小切分数，非常明显的动规暗示。由问题出发可建立状态`f[i]` 表示到索引`i` 处时需要的最少切割数(即切割前 i 个字符组成的字符串)，状态转移方程为`f[i] = min{1 + f[j]}, where j < i and substring [j, i] is palindrome`, 判断区间[j, i] 是否为回文简单的方法可反转后比较。

### Python

```python
class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        if not s:
            print 0

        cut = [i - 1 for i in xrange(1 + len(s))]

        for i in xrange(1 + len(s)):
            for j in xrange(i):
                # s[j:i] is palindrome
                if s[j:i] == s[j:i][::-1]:
                    cut[i] = min(cut[i], 1 + cut[j])
        return cut[-1]
```

### 源码分析

1. 当 s 为 None 或者列表为空时返回0
2. 初始化切割数数组
3. 子字符串的索引位置可为`[0, len(s) - 1]`, 内循环 j 比外循环 i 小，故可将 i 的最大值设为`1 + len(s)` 较为便利。
4. 回文的判断使用了`[::-1]` 对字符串进行反转
5. 最后返回数组最后一个元素

### 复杂度分析

两重循环，遍历的总次数为 $$1/2 \cdots n^2)$$, 每次回文的判断时间复杂度为 $$O(len(s))$$, 故总的时间复杂度近似为 $$O(n^3)$$. 在 s 长度较长时会 TLE.
使用了与 s 等长的辅助切割数数组，空间复杂度近似为 $$O(n)$$.

## 题解2 - 使用动态规划计算子字符串回文状态

切割数部分使用的是动态规划，优化的空间不大，仔细瞅瞅可以发现在判断字符串是否为回文的部分存在大量重叠计算，故可引入动态规划进行优化，时间复杂度可优化至到平方级别。

定义状态 PaMat[i][j]  为区间 `[i,j]` 是否为回文的标志, 对应此状态的子问题可从回文的定义出发，如果字符串首尾字符相同且在去掉字符串首尾字符后字符串仍为回文，则原字符串为回文，相应的状态转移方程 `PaMat[i][j] = s[i] == s[j] && PaMat[i+1][j-1]`, 由于状态转移方程中依赖比`i`大的结果，故实现中需要从索引大的往索引小的递推，另外还需要考虑一些边界条件和初始化方式，做到 bug-free 需要点时间。

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

### C++

```c++
class Solution {
public:
    int minCut(string s) {
        if (s.empty()) return 0;

        int len = s.size();
        vector<int> cut;
        for (int i = 0; i < 1 + len; ++i) {
            cut.push_back(i - 1);
        }
        vector<vector<bool> > mat = getMat(s);

        for (int i = 1; i < 1 + len; ++i) {
            for (int j = 0; j < i; ++j) {
                if (mat[j][i - 1]) {
                    cut[i] = min(cut[i], 1 + cut[j]);
                }
            }
        }

        return cut[len];
    }

    vector<vector<bool> > getMat(string s) {
        int len = s.size();
        vector<vector<bool> > mat = vector<vector<bool> >(len, vector<bool>(len, true));
        for (int i = len; i >= 0; --i) {
            for (int j = i; j < len; ++j) {
                if (j == i) {
                    mat[i][j] = true;
                } else if (j == i + 1) {
                    mat[i][j] = (s[i] == s[j]);
                } else {
                    mat[i][j] = ((s[i] == s[j]) && mat[i + 1][j - 1]);
                }
            }
        }

        return mat;
    }
};
```

### Java

```java
public class Solution {
    public int minCut(String s) {
        if (s == null || s.length() == 0) return 0;

        int len = s.length();
        int[] cut = new int[1 + len];
        for (int i = 0; i < 1 + len; ++i) {
            cut[i] = i - 1;
        }
        boolean[][] mat = paMat(s);

        for (int i = 1; i < 1 + len; i++) {
            for (int j = 0; j < i; j++) {
                if (mat[j][i - 1]) {
                    cut[i] = Math.min(cut[i], 1 + cut[j]);
                }
            }
        }

        return cut[len];
    }

    private boolean[][] paMat(String s) {
        int len = s.length();
        boolean[][] mat = new boolean[len][len];

        for (int i = len - 1; i >= 0; i--) {
            for (int j = i; j < len; j++) {
                if (j == i) {
                    mat[i][j] = true;
                } else if (j == i + 1) {
                    mat[i][j] = (s.charAt(i) == s.charAt(j));
                } else {
                    mat[i][j] = (s.charAt(i) == s.charAt(j)) && mat[i + 1][j - 1];
                }
            }
        }

        return mat;
    }
}
```

### 源码分析

初始化 cut 长度为`1 + len(s)`, `cut[0] = -1` 便于状态转移方程实现。在执行`mat[i][j] == ... mat[i + 1][j - 1]`时前提是`j - 1 > i + 1`, 所以才需要分情况赋值。使用`getMat` 得到字符串区间的回文矩阵，由于cut 的长度为1+len(s), 两重 for 循环时需要注意索引的取值，这个地方非常容易错。

### 复杂度分析

最坏情况下每次 for 循环都遍历 n 次，时间复杂度近似为 $$O(n^2)$$, 使用了二维回文矩阵保存记忆化搜索结果，空间复杂度为 $$O(n^2)$$.

## Reference

- [Palindrome Partitioning II 参考程序 Java/C++/Python](http://www.jiuzhang.com/solutions/palindrome-partitioning-ii/)
- soulmachine 的 leetcode 题解
