# Compare Strings - 字符串查找

## strstr

## Source

- lintcode: [lintcode - (13) strstr](http://www.lintcode.com/zh-cn/problem/strstr/)

```
strstr (a.k.a find sub string), is a useful function in string operation. You task is to implement this function.

For a given source string and a target string, you should output the "first" index(from 0) of target string in source string.

If target is not exist in source, just return -1.

Example
If source="source" and target="target", return -1.

If source="abcdabcdefg" and target="bcd", return 1.

Challenge
O(n) time.

Clarification
Do I need to implement KMP Algorithm in an interview?

    - Not necessary. When this problem occurs in an interview, the interviewer just want to test your basic implementation ability.
```

## 题解

对于字符串查找问题，可使用双重for循环解决，效率更高的则为KMP算法。

### Java

```java
/**
 * http://www.jiuzhang.com//solutions/implement-strstr
 */
class Solution {
    /**
     * Returns a index to the first occurrence of target in source,
     * or -1  if target is not part of source.
     * @param source string to be scanned.
     * @param target string containing the sequence of characters to match.
     */
    public int strStr(String source, String target) {
        if (source == null || target == null) {
            return -1;
        }
        
        int i, j;
        for (i = 0; i < source.length() - target.length() + 1; i++) {
            for (j = 0; j < target.length(); j++) {
                if (source.charAt(i + j) != target.charAt(j)) {
                    break;
                } //if
            } //for j
            if (j == target.length()) {
                return i;
            }
        } //for i

        // did not find the target
        return -1;
    }
}
```

### 源码分析

1. 边界检查：`source`和`target`有可能是空串。
2. 边界检查之下标溢出：注意变量`i`的循环判断条件，如果是单纯的`i < source.length()`则在后面的`source.charAt(i + j)`时有可能溢出。
2. 代码风格：（1）运算符`==`两边应加空格；（2）变量名不要起`s1``s2`这类，要有意义，如`target``source`；（3）即使if语句中只有一句话也要加大括号，即`{return -1;}`；（4）Java 代码的大括号一般在同一行右边，C++ 代码的大括号一般另起一行；（5）`int i, j;`声明前有一行空格，是好的代码风格。
3. 不要在for的条件中声明`i`,`j`，容易在循环外再使用时造成编译错误，错误代码示例：

### Another Similar Question

```java
/**
 * http://www.jiuzhang.com//solutions/implement-strstr
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

#### 源码解析

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
