# Interleaving String

## Question

- leetcode: [Interleaving String | LeetCode OJ](https://leetcode.com/problems/interleaving-string/)
- lintcode: [(29) Interleaving String](http://www.lintcode.com/en/problem/interleaving-string/)

```
Given three strings: s1, s2, s3,
determine whether s3 is formed by the interleaving of s1 and s2.

Example
For s1 = "aabcc", s2 = "dbbca"

When s3 = "aadbbcbcac", return true.
When s3 = "aadbbbaccc", return false.
Challenge
O(n2) time or better
```

## 题解1 - bug

题目意思是 s3 是否由 s1 和 s2 交叉构成，不允许跳着从 s1 和 s2 挑选字符。那么直觉上可以对三个字符串设置三个索引，首先从 s3 中依次取字符，然后进入内循环，依次从 s1 和 s2 中取首字符，若能匹配上则进入下一次循环，否则立即返回 false. 我们先看代码，再分析 bug 之处。

### Java

```java
public class Solution {
    /**
     * Determine whether s3 is formed by interleaving of s1 and s2.
     * @param s1, s2, s3: As description.
     * @return: true or false.
     */
    public boolean isInterleave(String s1, String s2, String s3) {
        int len1 = (s1 == null) ? 0 : s1.length();
        int len2 = (s2 == null) ? 0 : s2.length();
        int len3 = (s3 == null) ? 0 : s3.length();

        if (len3 != len1 + len2) return false;

        int i1 = 0, i2 = 0;
        for (int i3 = 0; i3 < len3; i3++) {
            boolean result = false;
            if (i1 < len1 && s1.charAt(i1) == s3.charAt(i3)) {
                i1++;
                result = true;
                continue;
            }
            if (i2 < len2 && s2.charAt(i2) == s3.charAt(i3)) {
                i2++;
                result = true;
                continue;
            }

            // return instantly if both s1 and s2 can not pair with s3
            if (!result) return false;
        }

        return true;
    }
}
```

### 源码分析

异常处理部分：首先求得 s1, s2, s3 的字符串长度，随后用索引 i1, i2, i3 巧妙地避开了繁琐的 null 检测。这段代码能过前面的一部分数据，但在 lintcode 的第15个 test 跪了。不想马上看以下分析的可以自己先 debug 下。

我们可以注意到以上代码还有一种情况并未考虑到，那就是当 s1[i1] 和 s2[i2] 均和 s3[i3] 相等时，我们可以拿 s1 或者 s2 去匹配，那么问题来了，由于不允许跳着取，那么可能出现在取了 s1 中的字符后，接下来的 s1 和 s2 首字符都无法和 s3 匹配到，因此原本应该返回 true 而现在返回 false. 建议将以上代码贴到 OJ 上看看测试用例。

以上 bug 可以通过加入对 `(s1[i1] == s3[i3]) && (s2[i2] == s3[i3])` 这一特殊情形考虑，即分两种情况递归调用 isInterleave, 只不过 s1, s2, s3 为新生成的字符串。

### 复杂度分析

遍历一次 s3, 时间复杂度为 $$O(n)$$, 空间复杂度 $$O(1)$$.

## 题解2

在 `(s1[i1] == s3[i3]) && (s2[i2] == s3[i3])` 时分两种情况考虑，即让 s1[i1] 和 s3[i3] 配对或者 s2[i2] 和 s3[i3] 配对，那么嵌套调用时新生成的字符串则分别为 `s1[1+i1:], s2[i2], s3[1+i3:]` 和 `s1[i1:], s2[1+i2], s3[1+i3:]`. 嵌套调用结束后立即返回最终结果，因为递归调用时整个结果已经知晓，不立即返回则有可能会产生错误结果，递归调用并未影响到调用处的 i1 和 i2.

### Python

```python
class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        len1 = 0 if s1 is None else len(s1)
        len2 = 0 if s2 is None else len(s2)
        len3 = 0 if s3 is None else len(s3)

        if len3 != len1 + len2:
            return False

        i1, i2 = 0, 0
        for i3 in xrange(len(s3)):
            result = False
            if (i1 < len1 and s1[i1] == s3[i3]) and \
               (i1 < len1 and s1[i1] == s3[i3]):
                # s1[1+i1:], s2[i2:], s3[1+i3:]
                case1 = self.isInterleave(s1[1 + i1:], s2[i2:], s3[1 + i3:])
                # s1[i1:], s2[1+i2:], s3[1+i3:]
                case2 = self.isInterleave(s1[i1:], s2[1 + i2:], s3[1 + i3:])
                return case1 or case2

            if i1 < len1 and s1[i1] == s3[i3]:
                i1 += 1
                result = True
                continue

            if i2 < len2 and s2[i2] == s3[i3]:
                i2 += 1
                result = True
                continue

            # return instantly if both s1 and s2 can not pair with s3
            if not result:
                return False

        return True
```

### C++

```c++
class Solution {
public:
    /**
     * Determine whether s3 is formed by interleaving of s1 and s2.
     * @param s1, s2, s3: As description.
     * @return: true of false.
     */
    bool isInterleave(string s1, string s2, string s3) {
        int len1 = s1.size();
        int len2 = s2.size();
        int len3 = s3.size();

        if (len3 != len1 + len2) return false;

        int i1 = 0, i2 = 0;
        for (int i3 = 0; i3 < len3; ++i3) {
            bool result = false;
            if (i1 < len1 && s1[i1] == s3[i3] &&
                i2 < len2 && s2[i2] == s3[i3]) {
                // s1[1+i1:], s2[i2:], s3[1+i3:]
                bool case1 = isInterleave(s1.substr(1 + i1), s2.substr(i2), s3.substr(1 + i3));
                // s1[i1:], s2[1+i2:], s3[1+i3:]
                bool case2 = isInterleave(s1.substr(i1), s2.substr(1 + i2), s3.substr(1 + i3));
                // return instantly
                return case1 || case2;
	        }

            if (i1 < len1 && s1[i1] == s3[i3]) {
                i1++;
                result = true;
                continue;
            }

            if (i2 < len2 && s2[i2] == s3[i3]) {
                i2++;
                result = true;
                continue;
            }

            // return instantly if both s1 and s2 can not pair with s3
            if (!result) return false;
        }

        return true;
    }
};
```

### Java

```java
public class Solution {
    /**
     * Determine whether s3 is formed by interleaving of s1 and s2.
     * @param s1, s2, s3: As description.
     * @return: true or false.
     */
    public boolean isInterleave(String s1, String s2, String s3) {
        int len1 = (s1 == null) ? 0 : s1.length();
        int len2 = (s2 == null) ? 0 : s2.length();
        int len3 = (s3 == null) ? 0 : s3.length();

        if (len3 != len1 + len2) return false;

        int i1 = 0, i2 = 0;
        for (int i3 = 0; i3 < len3; i3++) {
            boolean result = false;
            if (i1 < len1 && s1.charAt(i1) == s3.charAt(i3) &&
                i2 < len2 && s2.charAt(i2) == s3.charAt(i3)) {
                // s1[1+i1:], s2[i2:], s3[1+i3:]
                boolean case1 = isInterleave(s1.substring(1 + i1), s2.substring(i2), s3.substring(1 + i3));
                // s1[i1:], s2[1+i2:], s3[1+i3:]
                boolean case2 = isInterleave(s1.substring(i1), s2.substring(1 + i2), s3.substring(1 + i3));
                // return instantly
                return case1 || case2;
	        }

            if (i1 < len1 && s1.charAt(i1) == s3.charAt(i3)) {
                i1++;
                result = true;
                continue;
            }

            if (i2 < len2 && s2.charAt(i2) == s3.charAt(i3)) {
                i2++;
                result = true;
                continue;
            }

            // return instantly if both s1 and s2 can not pair with s3
            if (!result) return false;
        }

        return true;
    }
}
```

## 题解3 - 动态规划

看过题解1 和 题解2 的思路后动规的状态和状态方程应该就不难推出了。按照经典的序列规划，不妨假设状态 f[i1][i2][i3] 为 s1的前i1个字符和 s2的前 i2个字符是否能交叉构成 s3的前 i3个字符，那么根据 s1[i1], s2[i2], s3[i3]的匹配情况可以分为8种情况讨论。咋一看这似乎十分麻烦，但实际上我们注意到其实还有一个隐含条件：`len3 == len1 + len2`, 故状态转移方程得到大幅简化。

新的状态可定义为 f[i1][i2], 含义为s1的前`i1`个字符和 s2的前 `i2`个字符是否能交叉构成 s3的前 `i1 + i2` 个字符。根据 `s1[i1] == s3[i3]` 和 `s2[i2] == s3[i3]` 的匹配情况可建立状态转移方程为：

```
f[i1][i2] = (s1[i1 - 1] == s3[i1 + i2 - 1] && f[i1 - 1][i2]) ||
            (s2[i2 - 1] == s3[i1 + i2 - 1] && f[i1][i2 - 1])
```

这道题的初始化有点 trick, 考虑到空串的可能，需要单独初始化 `f[*][0]` 和 `f[0][*]`.

### Python

```python
class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix.
    """
    def isInterleave(self, s1, s2, s3):
        len1 = 0 if s1 is None else len(s1)
        len2 = 0 if s2 is None else len(s2)
        len3 = 0 if s3 is None else len(s3)

        if len3 != len1 + len2:
            return False

        f = [[True] * (1 + len2) for i in xrange (1 + len1)]
        # s1[i1 - 1] == s3[i1 + i2 - 1] && f[i1 - 1][i2]
        for i in xrange(1, 1 + len1):
            f[i][0] = s1[i - 1] == s3[i - 1] and f[i - 1][0]
        # s2[i2 - 1] == s3[i1 + i2 - 1] && f[i1][i2 - 1]
        for i in xrange(1, 1 + len2):
            f[0][i] = s2[i - 1] == s3[i - 1] and f[0][i - 1]
        # i1 >= 1, i2 >= 1
        for i1 in xrange(1, 1 + len1):
            for i2 in xrange(1, 1 + len2):
                case1 = s1[i1 - 1] == s3[i1 + i2 - 1] and f[i1 - 1][i2]
                case2 = s2[i2 - 1] == s3[i1 + i2 - 1] and f[i1][i2 - 1]
                f[i1][i2] = case1 or case2

        return f[len1][len2]
```

### C++

```c++
class Solution {
public:
    /**
     * Determine whether s3 is formed by interleaving of s1 and s2.
     * @param s1, s2, s3: As description.
     * @return: true of false.
     */
    bool isInterleave(string s1, string s2, string s3) {
        int len1 = s1.size();
        int len2 = s2.size();
        int len3 = s3.size();

        if (len3 != len1 + len2) return false;

        vector<vector<bool> > f(1 + len1, vector<bool>(1 + len2, true));
        // s1[i1 - 1] == s3[i1 + i2 - 1] && f[i1 - 1][i2]
        for (int i = 1; i <= len1; ++i) {
            f[i][0] = s1[i - 1] == s3[i - 1] && f[i - 1][0];
        }
        // s2[i2 - 1] == s3[i1 + i2 - 1] && f[i1][i2 - 1]
        for (int i = 1; i <= len2; ++i) {
            f[0][i] = s2[i - 1] == s3[i - 1] && f[0][i - 1];
        }
        // i1 >= 1, i2 >= 1
        for (int i1 = 1; i1 <= len1; ++i1) {
            for (int i2 = 1; i2 <= len2; ++i2) {
                bool case1 = s1[i1 - 1] == s3[i1 + i2 - 1] && f[i1 - 1][i2];
                bool case2 = s2[i2 - 1] == s3[i1 + i2 - 1] && f[i1][i2 - 1];
                f[i1][i2] = case1 || case2;
            }
        }

        return f[len1][len2];
    }
};
```

### Java

```java
public class Solution {
    /**
     * Determine whether s3 is formed by interleaving of s1 and s2.
     * @param s1, s2, s3: As description.
     * @return: true or false.
     */
    public boolean isInterleave(String s1, String s2, String s3) {
        int len1 = (s1 == null) ? 0 : s1.length();
        int len2 = (s2 == null) ? 0 : s2.length();
        int len3 = (s3 == null) ? 0 : s3.length();

        if (len3 != len1 + len2) return false;

        boolean [][] f = new boolean[1 + len1][1 + len2];
        f[0][0] = true;
        // s1[i1 - 1] == s3[i1 + i2 - 1] && f[i1 - 1][i2]
        for (int i = 1; i <= len1; i++) {
            f[i][0] = s1.charAt(i - 1) == s3.charAt(i - 1) && f[i - 1][0];
        }
        // s2[i2 - 1] == s3[i1 + i2 - 1] && f[i1][i2 - 1]
        for (int i = 1; i <= len2; i++) {
            f[0][i] = s2.charAt(i - 1) == s3.charAt(i - 1) && f[0][i - 1];
        }
        // i1 >= 1, i2 >= 1
        for (int i1 = 1; i1 <= len1; i1++) {
            for (int i2 = 1; i2 <= len2; i2++) {
                boolean case1 = s1.charAt(i1 - 1) == s3.charAt(i1 + i2 - 1) && f[i1 - 1][i2];
                boolean case2 = s2.charAt(i2 - 1) == s3.charAt(i1 + i2 - 1) && f[i1][i2 - 1];
                f[i1][i2] = case1 || case2;
            }
        }

        return f[len1][len2];
    }
}
```

### 源码分析

为后面递推方便，初始化时数组长度多加1，for 循环时需要注意边界(取到等号)。

### 复杂度分析

双重 for 循环，时间复杂度为 $$O(n^2)$$, 使用了二维矩阵，空间复杂度 $$O(n^2)$$. 其中空间复杂度可以优化。

## Reference

- soulmachine 的 Interleaving String 部分
- [Interleaving String 参考程序 Java/C++/Python](http://www.jiuzhang.com/solutions/interleaving-string/)
