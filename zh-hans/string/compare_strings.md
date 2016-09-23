# Compare Strings

Tags: Basic Implementation, String, LintCode Copyright, Easy

## Question

- lintcode: [Compare Strings](http://www.lintcode.com/en/problem/compare-strings/)

### Problem Statement

Compare two strings A and B, determine whether A contains all of the
characters in B.

The characters in string A and B are all **Upper Case** letters.

#### Notice

The characters of B in A are not necessary continuous or ordered.

**Example**

For `A = "ABCD"`, `B = "ACD"`, return `true`.

For `A = "ABCD"`, `B = "AABC"`, return `false`.

## 题解

题 [Two Strings Are Anagrams](http://algorithm.yuanbin.me/zh-hans/string/two_strings_are_anagrams.html) 的变形题。题目意思是问B中的所有字符是否都在A中，而不是单个字符。比如B="AABC"包含两个「A」，而A="ABCD"只包含一个「A」，故返回false. 做题时注意题意，必要时可向面试官确认。

既然不是类似 strstr 那样的匹配，直接使用两重循环就不太合适了。题目中另外给的条件则是A和B都是全大写单词，理解题意后容易想到的方案就是先遍历 A 和 B 统计各字符出现的频次，然后比较频次大小即可。嗯，祭出万能的哈希表。

### Python

```python
class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        letters = collections.defaultdict(int)
        for a in A:
            letters[a] += 1

        for b in B:
            letters[b] -= 1
            if b not in letters or letters[b] < 0:
                return False

        return True
```

### C++

```c++
class Solution {
public:
    /**
     * @param A: A string includes Upper Case letters
     * @param B: A string includes Upper Case letter
     * @return:  if string A contains all of the characters in B return true 
     *           else return false
     */
    bool compareStrings(string A, string B) {
        if (A.size() < B.size()) return false;

        const int UPPER_NUM = 26;
        int letter_cnt[UPPER_NUM] = {0};

        for (int i = 0; i != A.size(); ++i) {
            ++letter_cnt[A[i] - 'A'];
        }
        for (int i = 0; i != B.size(); ++i) {
            --letter_cnt[B[i] - 'A'];
            if (letter_cnt[B[i] - 'A'] < 0) return false;
        }

        return true;
    }
};
```

### Java

```java
public class Solution {
    /**
     * @param A : A string includes Upper Case letters
     * @param B : A string includes Upper Case letter
     * @return :  if string A contains all of the characters in B return true else return false
     */
    public boolean compareStrings(String A, String B) {
        if (A == null || B == null) return false;
        if (A.length() < B.length()) return false;

        final int UPPER_NUM = 26;
        int[] letter_cnt = new int[UPPER_NUM];

        for (int i = 0; i < A.length(); i++) {
            letter_cnt[A.charAt(i) - 'A']++;
        }
        for (int i = 0; i < B.length(); i++) {
            letter_cnt[B.charAt(i) - 'A']--;
            if (letter_cnt[B.charAt(i) - 'A'] < 0) return false;
        }

        return true;
    }
}
```

### 源码分析

Python 的`dict`就是hash， 所以 Python 在处理需要用到 hash 的地方非常方便。collections 提供的数据结构非常实用，不过复杂度分析起来要麻烦些。

1. 异常处理，B 的长度大于 A 时必定返回`false`, 包含了空串的特殊情况。
2. 使用额外的辅助空间，统计各字符的频次。

### 复杂度分析

遍历一次 A 字符串，遍历一次 B 字符串，时间复杂度最坏 $$O(n)$$, 空间复杂度为 $$O(1)$$.
