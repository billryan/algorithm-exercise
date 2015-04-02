# Compare Strings - 字符串查找

## strstr

Question:
- [Implement strStr() | LeetCode OJ](https://leetcode.com/problems/implement-strstr/)
- [(13) 字符串查找](http://lintcode.com/zh-cn/problem/strstr/)

问题简述：

> 对于一个给定的source字符串和一个target字符串，你应该在source字符串中找出target字符串出现的第一个位置(从0开始)。

对于字符串查找问题，可使用双重for循环解决，效率更高的则为KMP算法。


九章算法的实现：
1. [Java版](http://www.ninechapter.com//solutions/implement-strstr/)

```
/**
 * 本代码由九章算法编辑提供。没有版权欢迎转发。
 * - 九章算法致力于帮助更多中国人找到好的工作，教师团队均来自硅谷和国内的一线大公司在职工程师。
 * - 现有的面试培训课程包括：九章算法班，系统设计班，BAT国内班
 * - 更多详情请见官方网站：http://www.ninechapter.com/
 */

public class Solution {
    public String strStr(String haystack, String needle) {
        if(haystack == null || needle == null) {
            return null;
        }
        int i, j;
        for(i = 0; i < haystack.length() - needle.length() + 1; i++) {
            for(j = 0; j < needle.length(); j++) {
                if(haystack.charAt(i + j) != needle.charAt(j)) {
                    break;
                }
            }
            if(j == needle.length()) {
                return haystack.substring(i);
            }
        }
        return null;
    }
}
```

## Compare Strings

Question: [(55) Compare Strings](http://www.lintcode.com/en/problem/compare-strings/)

```
Compare two strings A and B, determine whether A contains all of the characters in B.

The characters in string A and B are all Upper Case letters.

Example
For A = "ABCD", B = "ABC", return true.

For A = "ABCD" B = "AABC", return false.
```

题解：

题目意思是问B中的所有字符是否都在A中，而不是单个字符。比如B="AABC"包含两个「A」，而A="ABCD"只包含一个「A」，故返回false.

既然不是类似strstr那样的匹配，直接使用两重循环就不太合适了。题目中另外给的条件则是A和B都是全大小单词，理解题意后容易想到的方案就是先遍历A和B统计各字符出现的频次，然后比较频次大小即可。嗯，祭出万能的哈希表。

**C++**
```
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
源码解析：

使用数组`freqA`和`freqB`分别保存A和B中各字母出现的频次，随后遍历比较两数组，若A中相应的频次小于B时，返回false，否则遍历完后返回true.

最后一步比较`freqA`和`freqB`的频次时，其实是可以放到遍历B字符串的时候处理的。优化后的代码如下：

**C++**
```
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

Reference: [Lintcode: Compare Strings - neverlandly - 博客园](http://www.cnblogs.com/EdwardLiu/p/4273817.html)
