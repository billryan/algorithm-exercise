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

## 题解

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

## Reference

- [Longest Common Substring | 九章算法](http://www.jiuzhang.com/solutions/longest-common-substring/)
