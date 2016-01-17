# Length of Last Word

## Question

- leetcode: [Length of Last Word | LeetCode OJ](https://leetcode.com/problems/length-of-last-word/)
- lintcode: [(422) Length of Last Word](http://www.lintcode.com/en/problem/length-of-last-word/)

```
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Have you met this question in a real interview? Yes
Example
Given s = "Hello World", return 5.

Note
A word is defined as a character sequence consists of non-space characters only.
```

## 题解 1

关键点在于确定最后一个字符串之前的空格，此外还需要考虑末尾空格这一特殊情况，故首先除掉右边的空白字符比较好。

### Java

```java
public class Solution {
    /**
     * @param s A string
     * @return the length of last word
     */
    public int lengthOfLastWord(String s) {
        if (s == null | s.isEmpty()) return 0;

        // trim right space
        int begin = 0, end = s.length();
        while (end > 0 && s.charAt(end - 1) == ' ') {
            end--;
        }
        // find the last space
        for (int i = 0; i < end; i++) {
            if (s.charAt(i) == ' ') {
                begin = i + 1;
            }
        }

        return end - begin;
    }
}
```

### 源码分析

两根指针。

### 复杂度分析

遍历一次，时间复杂度 $$O(n)$$.

## 题解 2

直接从后向前扫描

### C++

``` c++
    int lengthOfLastWord(string s) {
        if (s.size() == 0) return 0;
       
        int count = 0;
        for (int i=s.size()-1; i>=0; i--)
            if (s[i] == ' ') {
                if (count) break;
            } else count++;

        return count;
    }
```
