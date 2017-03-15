# Reverse Words in a String

Tags: String, Medium

## Question

- leetcode: [Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)
- lintcode: [Reverse Words in a String](http://www.lintcode.com/en/problem/reverse-words-in-a-string/)

### Problem Statement

Given an input string, reverse the string word by word.

For example,  
Given s = "`the sky is blue`",  
return "`blue is sky the`".

**Update (2015-02-12):**  
For C programmers: Try to solve it _in-place_ in _O_(1) space.

**Clarification:**

  * What constitutes a word?  
A sequence of non-space characters constitutes a word.

  * Could the input string contain leading or trailing spaces?  
Yes. However, your reversed string should not contain leading or trailing
spaces.

  * How about multiple spaces between two words?  
Reduce them to a single space in the reversed string.

## 题解

1. 由第一个提问可知：题中只有空格字符和非空格字符之分，因此空格字符应为其一关键突破口。
2. 由第二个提问可知：输入的前导空格或者尾随空格在反转后应去掉。
3. 由第三个提问可知：两个单词间的多个空格字符应合并为一个或删除掉。

首先找到各个单词(以空格隔开)，根据题目要求，单词应从后往前依次放入。split 后从后往前加入空格返回即可。如果不使用 split 的话正向取出比较麻烦，因此可尝试采用逆向思维——先将输入字符串数组中的单词从后往前逆序取出，取出单词后即翻转并append至新字符串数组。在append之前加入空格即可，即两次翻转法。

### Python

```python
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(reversed(s.strip().split()))
```

### C++

```c++
class Solution {
public:
    /**
     * @param s : A string
     * @return : A string
     */
    string reverseWords(string s) {
        if (s.empty()) {
            return s;
        }

        string s_ret, s_temp;
        string::size_type ix = s.size();
        while (ix != 0) {
            s_temp.clear();
            while (!isspace(s[--ix])) {
                s_temp.push_back(s[ix]);
                if (ix == 0) {
                    break;
                }
            }
            if (!s_temp.empty()) {
                if (!s_ret.empty()) {
                    s_ret.push_back(' ');
                }
                std::reverse(s_temp.begin(), s_temp.end());
                s_ret.append(s_temp);
            }
        }

        return s_ret;
    }
};
```

### Java

```java
public class Solution {
    public String reverseWords(String s) {
        if (s == null || s.trim().isEmpty()) {
            return "";
        }

        String[] words = s.split(" ");
        StringBuilder sb = new StringBuilder();
        for (int i = words.length - 1; i >= 0; i--) {
            if (!words[i].isEmpty()) {
                sb.append(words[i]).append(" ");
            }
        }

        return sb.substring(0, sb.length() - 1);
    }
}
```

### 源码分析

1. 首先处理异常，s 为空或者空白字符串时直接返回空。
2. 如果首先排除掉空白字符串则后面不需要为长度为0单独考虑。
3. Java 中使用 StringBuilder 效率更高。

空间复杂度为 O(1) 的解法？

1. 处理异常及特殊情况
2. 处理多个空格及首尾空格
3. 记住单词的头尾指针，翻转之
4. 整体翻转
