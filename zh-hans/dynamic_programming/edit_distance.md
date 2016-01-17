# Edit Distance

- tags: [DP_Two_Sequence]

## Question

- leetcode: [Edit Distance | LeetCode OJ](https://leetcode.com/problems/edit-distance/)
- lintcode: [(119) Edit Distance](http://www.lintcode.com/en/problem/edit-distance/)

```
Given two words word1 and word2, find the minimum number of steps required 
to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example
Given word1 = "mart" and word2 = "karma", return 3.
```

## 题解1 - 双序列动态规划

两个字符串比较，求最值，直接看似乎并不能直接找出解决方案，这时往往需要使用动态规划的思想寻找递推关系。使用双序列动态规划的通用做法，不妨定义`f[i][j]`为字符串1的前`i`个字符和字符串2的前`j`个字符的编辑距离，那么接下来寻找其递推关系。增删操作互为逆操作，即增或者删产生的步数都是一样的。故初始化时容易知道`f[0][j] = j, f[i][0] = i`, 接下来探讨`f[i][j]` 和`f[i - 1][j - 1]`的关系，和 LCS 问题类似，我们分两种情况讨论，即`word1[i] == word2[j]` 与否，第一种相等的情况有：

1. `i == j`, 且有`word1[i] == word2[j]`, 则由`f[i - 1][j - 1] -> f[i][j]` 不增加任何操作，有`f[i][j] = f[i - 1][j - 1]`.
2. `i != j`, 由于字符数不等，肯定需要增/删一个字符，但是增删 word1 还是 word2 是不知道的，故可取其中编辑距离的较小值，即`f[i][j] = 1 + min{f[i - 1][j], f[i][j - 1]}`.

第二种不等的情况有：

1. `i == j`, 有`f[i][j] = 1 + f[i - 1][j - 1]`.
2. `i != j`, 由于字符数不等，肯定需要增/删一个字符，但是增删 word1 还是 word2 是不知道的，故可取其中编辑距离的较小值，即`f[i][j] = 1 + min{f[i - 1][j], f[i][j - 1]}`.

最后返回`f[len(word1)][len(word2)]`

### Python

```python
class Solution: 
    # @param word1 & word2: Two string.
    # @return: The minimum number of steps.
    def minDistance(self, word1, word2):
        len1, len2 = 0, 0
        if word1:
            len1 = len(word1)
        if word2:
            len2 = len(word2)
        if not word1 or not word2:
            return max(len1, len2)
        
        f = [[i + j for i in xrange(1 + len2)] for j in xrange(1 + len1)]
        
        for i in xrange(1, 1 + len1):
            for j in xrange(1, 1 + len2):
                if word1[i - 1] == word2[j - 1]:
                    f[i][j] = min(f[i - 1][j - 1], 1 + f[i - 1][j], 1 + f[i][j - 1])
                else:
                    f[i][j] = 1 + min(f[i - 1][j - 1], f[i - 1][j], f[i][j - 1])
        return f[len1][len2]
```
### C++

```c++
class Solution {
public:
    /**
     * @param word1 & word2: Two string.
     * @return: The minimum number of steps.
     */
    int fistance(string word1, string word2) {
        if (word1.empty() || word2.empty()) {
            return max(word1.size(), word2.size());
        }

        int len1 = word1.size();
        int len2 = word2.size();
        vector<vector<int> > f = \
            vector<vector<int> >(1 + len1, vector<int>(1 + len2, 0));
        for (int i = 0; i <= len1; ++i) {
            f[i][0] = i;
        }
        for (int i = 0; i <= len2; ++i) {
            f[0][i] = i;
        }

        for (int i = 1; i <= len1; ++i) {
            for (int j = 1; j <= len2; ++j) {
                if (word1[i - 1] == word2[j - 1]) {
                    f[i][j] = min(f[i - 1][j - 1], 1 + f[i - 1][j]);
                    f[i][j] = min(f[i][j], 1 + f[i][j - 1]);
                } else {
                    f[i][j] = min(f[i - 1][j - 1], f[i - 1][j]);
                    f[i][j] = 1 + min(f[i][j], f[i][j - 1]);
                }
            }
        }

        return f[len1][len2];
    }
};
```

### Java

```java
public class Solution {
    public int minDistance(String word1, String word2) {
        int len1 = 0, len2 = 0;
        if (word1 != null && word2 != null) {
            len1 = word1.length();
            len2 = word2.length();
        }
        if (word1 == null || word2 == null) {
            return Math.max(len1, len2);
        }
        
        int[][] f = new int[1 + len1][1 + len2];
        for (int i = 0; i <= len1; i++) {
            f[i][0] = i;
        }
        for (int i = 0; i <= len2; i++) {
            f[0][i] = i;
        }
        
        for (int i = 1; i <= len1; i++) {
            for (int j = 1; j <= len2; j++) {
                if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
                    f[i][j] = Math.min(f[i - 1][j - 1], 1 + f[i - 1][j]);
                    f[i][j] = Math.min(f[i][j], 1 + f[i][j - 1]);
                } else {
                    f[i][j] = Math.min(f[i - 1][j - 1], f[i - 1][j]);
                    f[i][j] = 1 + Math.min(f[i][j], f[i][j - 1]);
                }
            }
        }
        
        return f[len1][len2];
    }
}
```

### 源码解析

1. 边界处理
2. 初始化二维矩阵(Python 中初始化时 list 中 len2 在前，len1 在后)
3. i, j 从1开始计数，比较 word1 和 word2 时注意下标
4. 返回`f[len1][len2]`

### 复杂度分析

两重 for 循环，时间复杂度为 $$O(len1 \cdot len2)$$. 使用二维矩阵，空间复杂度为 $$O(len1 \cdot len2)$$.
