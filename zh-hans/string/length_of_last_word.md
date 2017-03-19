# Length of Last Word

Tags: String, Easy

## Question

- leetcode: [Length of Last Word](https://leetcode.com/problems/length-of-last-word/)
- lintcode: [Length of Last Word](http://www.lintcode.com/en/problem/length-of-last-word/)

### Problem Statement

Given a string _s_ consists of upper/lower-case alphabets and empty space
characters `' '`, return the length of last word in the string.

If the last word does not exist, return 0.

**Note:** A word is defined as a character sequence consists of non-space characters only.

For example,  
Given _s_ = `"Hello World"`,  
return `5`.

## 题解

关键点在于确定最后一个字符串之前的空格，此外还需要考虑末尾空格这一特殊情况，容易想到的是利用一前一后两个索引记录，最后相减即可。但其实可以巧妙地直接利用非空字符串长度表示。除了通常简单粗暴的方法，我们还可以尝试使用正则表达式这一利器对字符串进行处理。

### Python

```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None: return 0

        last_word = s.split()
        return len(last_word[-1]) if last_word else 0
```

### Python

```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None: return 0

        m = re.search(r'(?P<word>\S+)\s*$', s)
        return len(m.group('word')) if m else 0
```

### Python

```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None: return 0
        cnt = 0
        for c in reversed(s):
            if c == ' ':
                if cnt > 0: break
            else:
                cnt += 1

        return cnt
```

### C++

```cpp
class Solution {
public:
    int lengthOfLastWord(string s) {
        if (s.empty()) return 0;

        int x = s.find_last_not_of(' ');
        return (x == std::string::npos) ? 0 : x - s.find_last_of(' ', x);
    }
};
```

### C++

```cpp
class Solution {
public:
    int lengthOfLastWord(string s) {
        if (s.length() == 0) return 0;

        int cnt = 0;
        for (int i = s.length() - 1; i >= 0; --i) {
            if (s[i] == ' ') {
                if (cnt > 0) break;
            } else {
                cnt++;
            }
        }

        return cnt;
    }
};
```

### Java

```java
public class Solution {
    public int lengthOfLastWord(String s) {
        if (s == null || s.isEmpty()) return 0;

        int len = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            if (s.charAt(i) == ' ') {
                if (len > 0) return len;
            } else {
                len++;
            }
        }

        return len;
    }
}
```

### 源码分析

注意检查输入参数和索引即可，当前长度信息和当前索引字符是否为空格这两种信息可以结合使用避免硬标记。

### 复杂度分析

遍历一次，时间复杂度 $$O(n)$$，不复制源字符串，空间复杂度 $$O(1)$$.