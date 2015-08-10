# Distinct Subsequences

## Source

- leetcode: [Distinct Subsequences | LeetCode OJ](https://leetcode.com/problems/distinct-subsequences/)
- lintcode: [(118) Distinct Subsequences](http://www.lintcode.com/en/problem/distinct-subsequences/)

```
Given a string S and a string T, count the number of distinct subsequences of T in S.
A subsequence of a string is a new string
which is formed from the original string by deleting some (can be none) of the characters
without disturbing the relative positions of the remaining characters.
(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example
Given S = "rabbbit", T = "rabbit", return 3.
Challenge
Do it in O(n2) time and O(n) memory.

O(n2) memory is also acceptable if you do not know how to optimize memory.
```

## 题解1

首先分清 subsequence 和 substring 两者的区别，subsequence 可以是不连续的子串。题意要求 S 中子序列 T 的个数。如果不考虑程序实现，我们能想到的办法是逐个比较 S 和 T 的首字符，相等的字符删掉，不等时则删除 S 中的首字符，继续比较后续字符直至 T 中字符串被删完。这种简单的思路有这么几个问题，题目问的是子序列的个数，而不是是否存在，故在字符不等时不能轻易删除掉 S 中的字符。那么如何才能得知子序列的个数呢？

要想得知不同子序列的个数，那么我们就不能在 S 和 T 中首字符不等时简单移除 S 中的首字符了，取而代之的方法应该是先将 S 复制一份，再用移除 S 中首字符后的新字符串和 T 进行比较，这点和深搜中的剪枝函数的处理有点类似。

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

1. 对 null 异常处理
2. S 字符串长度若小于 T 字符串长度，T 必然不是 S 的子序列，返回0
3. T 字符串长度为0，证明 T 是 S 的子序列，返回1

由于进入 for 循环的前提是 `T.length() >= 1`, 故当 T 的长度为1时，Java 中对 T 取子串`T.substring(1)`时产生的是空串`""`而并不抛出索引越界的异常。

### 复杂度分析

最好情况下，S 中没有和 T 相同的字符，时间复杂度为 $$O(n)$$; 最坏情况下，S 中的字符和 T 中字符完全相同，此时可以画出递归调用栈，发现和深搜非常类似，数学关系为 $$f(n) = \sum _{i = 1} ^{n - 1} f(i)$$, 这是指数级别的复杂度。

## Reference

- [LeetCode: Distinct Subsequences（不同子序列的个数） - 亦忘却_亦纪念](http://blog.csdn.net/abcbc/article/details/8978146)
