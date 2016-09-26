# Implement strStr

Tags: Two Pointers, String, Easy

## Question

- leetcode: [Implement strStr()](https://leetcode.com/problems/implement-strstr/)
- lintcode: [strstr](http://www.lintcode.com/en/problem/strstr/)

### Problem Statement

Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.

## 题解

对于字符串查找问题，可使用双重 for 循环解决，效率更高的则为 KMP 算法。双重 for 循环的使用较有讲究，因为这里需要考虑目标字符串比源字符串短的可能。对目标字符串的循环肯定是必要的，所以可以优化的地方就在于如何访问源字符串了。简单直观的解法是利用源字符串的长度作为 for 循环的截止索引，这种方法需要处理源字符串中剩余长度不足以匹配目标字符串的情况，而更为高效的方案则为仅遍历源字符串中有可能和目标字符串匹配的部分索引。

### Python

```python
class Solution:
    def strStr(self, source, target):
        if source is None or target is None:
            return -1

        for i in range(len(source) - len(target) + 1):
            for j in range(len(target)):
                if source[i + j] != target[j]:
                    break
            else:  # no break
                return i
        return -1
```

### C

```c
int strStr(char* haystack, char* needle) {
    if (haystack == NULL || needle == NULL) return -1;

    const int len_h = strlen(haystack);
    const int len_n = strlen(needle);
    for (int i = 0; i < len_h - len_n + 1; i++) {
        int j = 0;
        for (; j < len_n; j++) {
            if (haystack[i+j] != needle[j]) {
                break;
            }
        }
        if (j == len_n) return i;
    }

    return -1;
}
```

### C++
```c++
class Solution {
public:
    int strStr(string haystack, string needle) {
        if (haystack.empty() && needle.empty()) return 0;
        if (haystack.empty()) return -1;
        if (haystack.size() < needle.size()) return -1;

        for (string::size_type i = 0; i < haystack.size() - needle.size() + 1; i++) {
            string::size_type j = 0;
            for (; j < needle.size(); j++) {
                if (haystack[i + j] != needle[j]) break;
            }
            if (j == needle.size()) return i;
        }
        
        return -1;
    }
};
```

### Java

```java
public class Solution {
    public int strStr(String haystack, String needle) {
        if (haystack == null && needle == null) return 0;
        if (haystack == null) return -1;
        if (needle == null) return 0;
        
        for (int i = 0; i < haystack.length() - needle.length() + 1; i++) {
            int j = 0;
            for (; j < needle.length(); j++) {
                if (haystack.charAt(i+j) != needle.charAt(j)) break;
            }
            if (j == needle.length()) return i;
        }

        return -1;
    }
}
```

### 源码分析

1. 边界检查：`haystack(source)`和`needle(target)`有可能是空串。
2. 边界检查之下标溢出：注意变量`i`的循环判断条件，如果用的是`i < source.length()`则在后面的`source.charAt(i + j)`时有可能溢出。
3. 代码风格：
    - 运算符`==`两边应加空格
    - 变量名不要起`s1``s2`这类，要有意义，如`target``source`
    - Java 代码的大括号一般在同一行右边，C++ 代码的大括号一般另起一行
    - int i, j;`声明前有一行空格，是好的代码风格
3. 是否在for的条件中声明`i`,`j`，这个视情况而定，如果需要在循环外再使用时，则须在外部初始化，否则没有这个必要。

需要注意的是有些题目要求并不是返回索引，而是返回字符串，此时还需要调用相应语言的`substring`方法。Python3 中用`range`替换了`xrange`，Python2 中使用`xrange`效率略高一些。
另外需要注意的是 Python 代码中的`else`接的是`for` 而不是`if`, 其含义为`no break`, 属于比较 Pythonic 的用法，有兴趣的可以参考 [4. More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) 的 4.4 节和 [if statement - Why does python use 'else' after for and while loops?](http://stackoverflow.com/questions/9979970/why-does-python-use-else-after-for-and-while-loops)

### 复杂度分析

双重 for 循环，时间复杂度最坏情况下为 $$O((n-m)*m)$$.
