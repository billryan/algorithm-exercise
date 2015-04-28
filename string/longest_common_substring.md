# Longest Common Substring

## Source

- lintcode: [(79) Longest Common Substring](http://www.lintcode.com/en/problem/longest-common-substring/)

```
Given two strings, find the longest common substring.
Return the length of it.

Example
Given A="ABCD", B="CBCE", return 2.
Note
The characters in substring should occur continuously in original string.
This is different with subsequence.
```

## 题解

求最长公共子串，注意「子串」和「子序列」的区别！简单考虑可以使用两根指针索引分别指向两个字符串的当前遍历位置，若遇到相等的字符时则同时向后移动一位。

### C++

```c++
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

        int lcs = 0, lcs_temp = 0;
        for (int i = 0; i < A.size(); ++i) {
            for (int j = 0; j < B.size(); ++j) {
                lcs_temp = 0;
                while ((i + lcs_temp < A.size()) &&\
                       (j + lcs_temp < B.size()) &&\
                       (A[i + lcs_temp] == B[j + lcs_temp]))
                {
                    ++lcs_temp;
                }

                // update lcs
                if (lcs_temp > lcs) {
                    lcs = lcs_temp;
                }
            }
        }

        return lcs;
    }
};
```

### 源码分析

1. 异常处理，空串时返回0.
2. 分别使用`i`和`j`表示当前遍历的索引处。若当前字符相同时则共同往后移动一位。
3. 没有相同字符时比较此次遍历的`lcs_temp`和`lcs`大小，更新`lcs`.
4. 返回`lcs`.

注意在`while`循环中不可直接使用`++i`或者`++j`，因为有可能会漏解！

### 复杂度分析

双重 for 循环，最坏时间复杂度约为 $$O(mn \cdot lcs)$$.

## Reference

- [Longest Common Substring | 九章算法](http://www.jiuzhang.com/solutions/longest-common-substring/)
