# Two Strings Are Anagrams

Tags: String, Cracking The Coding Interview, Easy

## Question

- leetcode: [Valid Anagram](https://leetcode.com/problems/valid-anagram/)
- lintcode: [Two Strings Are Anagrams](http://www.lintcode.com/en/problem/two-strings-are-anagrams/)

### Problem Statement

Write a method `anagram(s,t)` to decide if two strings are anagrams or not.

**Clarification**

What is **Anagram**?  
\- Two strings are anagram if they can be the same after change the order of
characters.

**Example**

Given s = `"abcd"`, t = `"dcab"`, return `true`.  
Given s = `"ab"`, t = `"ab"`, return `true`.  
Given s = `"ab"`, t = `"ac"`, return `false`.

**Challenge** ****

O(n) time, O(1) extra space

## 题解1 - hashmap 统计字频

判断两个字符串是否互为变位词，若区分大小写，考虑空白字符时，直接来理解可以认为两个字符串的拥有各不同字符的数量相同。对于比较字符数量的问题常用的方法为遍历两个字符串，统计其中各字符出现的频次，若不等则返回`false`. 有很多简单字符串类面试题都是此题的变形题。

### Python

``` python
class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        return collections.Counter(s) == collections.Counter(t)
```

### C++

```c++
class Solution {
public:
    /**
     * @param s: The first string
     * @param b: The second string
     * @return true or false
     */
    bool anagram(string s, string t) {
        if (s.empty() || t.empty()) {
            return false;
        }
        if (s.size() != t.size()) {
            return false;
        }

        int letterCount[256] = {0};

        for (int i = 0; i != s.size(); ++i) {
            ++letterCount[s[i]];
            --letterCount[t[i]];
        }
        for (int i = 0; i != t.size(); ++i) {
            if (letterCount[t[i]] != 0) {
                return false;
            }
        }

        return true;
    }
};
```

### Java

```java
public class Solution {
    /**
     * @param s: The first string
     * @param b: The second string
     * @return true or false
     */
    public boolean anagram(String s, String t) {
        if (s == null || t == null) return false;
        if (s.length() != t.length()) return false;

        final int CHAR_NUM = 256;
        int[] letterCount = new int[CHAR_NUM];

        for (int i = 0; i != s.length(); i++) {
            letterCount[s.charAt(i)]++;
            letterCount[t.charAt(i)]--;
        }
        for (int i = 0; i != CHAR_NUM; i++) {
            if (letterCount[i] != 0) return false;
        }

        return true;
    }
};
```

### 源码分析

1. 两个字符串长度不等时必不可能为变位词(需要注意题目条件灵活处理)。
2. 初始化含有256个字符的计数器数组。
3. 对字符串 s 自增，字符串 t 递减，再次遍历判断`letterCount`数组的值，小于0时返回`false`.

在字符串长度较长(大于所有可能的字符数)时，还可对第二个`for`循环做进一步优化，即`t.size() > 256`时，使用256替代`t.size()`直接比较字符计数, 使用`i`替代`t[i]`.

### 复杂度分析

两次遍历字符串，时间复杂度最坏情况下为 $$O(n)$$, 使用了额外的数组，空间复杂度 $$O(1)$$.

## 题解2 - 排序字符串

另一直接的解法是对字符串先排序，若排序后的字符串内容相同，则其互为变位词。

### Python

```python
class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        return sorted(s) == sorted(t)
```

### C++

```c++
class Solution {
public:
    /**
     * @param s: The first string
     * @param b: The second string
     * @return true or false
     */
    bool anagram(string s, string t) {
        if (s.empty() || t.empty()) {
            return false;
        }
        if (s.size() != t.size()) {
            return false;
        }

        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        if (s == t) {
            return true;
        } else {
            return false;
        }
    }
};
```

### Java

```java
public class Solution {
    /**
     * @param s: The first string
     * @param b: The second string
     * @return true or false
     */
    public boolean anagram(String s, String t) {
        if (s == null || t == null) return false;
        if (s.length() != t.length()) return false;

        char[] sChars = s.toCharArray();
        char[] tChars = t.toCharArray();
        Arrays.sort(sChars);
        Arrays.sort(tChars);

        for (int i = 0; i != s.length(); i++) {
            if (sChars[i] != tChars[i]) return false;
        }

        return true;
    }
};
```

### 源码分析

对字符串 s 和 t 分别排序，而后比较是否含相同内容。对字符串排序时可以采用先统计字频再组装成排序后的字符串，效率更高一点。

### 复杂度分析

C++的 STL 中 sort 的时间复杂度介于 $$O(n)$$ 和 $$O(n^2)$$之间，判断`s == t`时间复杂度最坏为 $$O(n)$$. 可以看出此方法的时间复杂度相比题解1还是比较高的。Java 中字符串默认不可变，故空间复杂度为 $$O(n)$$.

## Reference

- *CC150 Chapter 9.1* 中文版 p109
