# Compare Strings

## Source

- lintcode: [(55) Compare Strings](http://www.lintcode.com/en/problem/compare-strings/)

```
Compare two strings A and B, determine whether A contains all of the characters in B.

The characters in string A and B are all Upper Case letters.

Example
For A = "ABCD", B = "ABC", return true.

For A = "ABCD" B = "AABC", return false.
```

## 题解

题 [Two Strings Are Anagrams | Data Structure and Algorithm](http://algorithm.yuanbin.me/zh-hans/string/two_strings_are_anagrams.html) 的变形题。题目意思是问B中的所有字符是否都在A中，而不是单个字符。比如B="AABC"包含两个「A」，而A="ABCD"只包含一个「A」，故返回false. 做题时注意题意，必要时可向面试官确认。

既然不是类似 strstr 那样的匹配，直接使用两重循环就不太合适了。题目中另外给的条件则是A和B都是全大写单词，理解题意后容易想到的方案就是先遍历 A 和 B 统计各字符出现的频次，然后比较频次大小即可。嗯，祭出万能的哈希表。

### Python

Python 的`dict`就是hash， 所以python 在处理需要用到hash的地方非常方便。

```python
import collections
class Solution:
    def compare_strings(self, A, B):
        # return a dict with default value set to 0
        letters = collections.defaultdict(int)
        for a in A:
            letters[a] += 1

        for b in B:
            if b not in letters:
                return False
            elif letters[b] <= 0:
                return False
            else:
                letters[b] -= 1
        return True
```
### 源码解析

1. 异常处理，B 的长度大于 A 时必定返回`false`, 包含了空串的特殊情况。
2. 使用额外的辅助空间，统计各字符的频次。

### 复杂度分析

遍历一次 A 字符串，遍历一次 B 字符串，时间复杂度最坏 $$O(2n)$$, 空间复杂度为 $$O(26)$$.


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
        if (A.size() < B.size()) {
            return false;
        }

        const int AlphabetNum = 26;
        int letterCount[AlphabetNum] = {0};
        for (int i = 0; i != A.size(); ++i) {
            ++letterCount[A[i] - 'A'];
        }
        for (int i = 0; i != B.size(); ++i) {
            --letterCount[B[i] - 'A'];
            if (letterCount[B[i] - 'A'] < 0) {
                return false;
            }
        }

        return true;
    }
};
```

### 源码解析

1. 异常处理，B 的长度大于 A 时必定返回`false`, 包含了空串的特殊情况。
2. 使用额外的辅助空间，统计各字符的频次。

### 复杂度分析

遍历一次 A 字符串，遍历一次 B 字符串，时间复杂度最坏 $$O(2n)$$, 空间复杂度为 $$O(26)$$.
