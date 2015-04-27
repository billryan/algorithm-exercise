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

题目意思是问B中的所有字符是否都在A中，而不是单个字符。比如B="AABC"包含两个「A」，而A="ABCD"只包含一个「A」，故返回false.

既然不是类似strstr那样的匹配，直接使用两重循环就不太合适了。题目中另外给的条件则是A和B都是全大小单词，理解题意后容易想到的方案就是先遍历A和B统计各字符出现的频次，然后比较频次大小即可。嗯，祭出万能的哈希表。

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
        if (B.empty()) {
            return true;
        }
        if (A.empty()) {
            return false;
        }

        const int AlphabetNum = 26;
        int freqA[AlphabetNum] = {0};
        int freqB[AlphabetNum] = {0};
        string::size_type ixA, ixB;
        for (ixA = 0; ixA != A.size(); ++ixA) {
            ++freqA[A[ixA] - 'A'];
        }
        for (ixB = 0; ixB != B.size(); ++ixB) {
            ++freqB[B[ixB] - 'A'];
        }
        for (int i = 0; i != AlphabetNum; ++i) {
            if (freqA[i] - freqB[i] < 0) {
                return false;
            }
        }

        return true;
    }
};
```

### 源码解析

使用数组`freqA`和`freqB`分别保存A和B中各字母出现的频次，随后遍历比较两数组，若A中相应的频次小于B时，返回false，否则遍历完后返回true.

最后一步比较`freqA`和`freqB`的频次时，其实是可以放到遍历B字符串的时候处理的。优化后的代码如下：

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
        if (B.empty()) {
            return true;
        }
        if (A.empty()) {
            return false;
        }

        const int AlphabetNum = 26;
        int freqA[AlphabetNum] = {0};
        int freqB[AlphabetNum] = {0};
        string::size_type ixA, ixB;
        for (ixA = 0; ixA != A.size(); ++ixA) {
            ++freqA[A[ixA] - 'A'];
        }
        for (ixB = 0; ixB != B.size(); ++ixB) {
            ++freqB[B[ixB] - 'A'];
            if (freqA[B[ixB] - 'A'] - freqB[B[ixB] - 'A'] < 0) {
                return false;
            }
        }

        return true;
    }
};
```

## Reference

- [Lintcode: Compare Strings - neverlandly - 博客园](http://www.cnblogs.com/EdwardLiu/p/4273817.html)
