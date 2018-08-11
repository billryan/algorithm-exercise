# Longest Palindromic Substring

Tags: String, Medium

## Question

- leetcode: [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)
- lintcode: [Longest Palindromic Substring](http://www.lintcode.com/en/problem/longest-palindromic-substring/)

### Problem Statement

Given a string **s**, find the longest palindromic substring in **s**. You may
assume that the maximum length of **s** is 1000.

**Example:**
    
    
    
    **Input:** "babad"
    
    **Output:** "bab"
    
    **Note:** "aba" is also a valid answer.
    

**Example:**
    

    **Input:** "cbbd"
    
    **Output:** "bb"

## 题解1 - 穷竭搜索

最简单的方案，穷举所有可能的子串，判断子串是否为回文，使用一变量记录最大回文长度，若新的回文超过之前的最大回文长度则更新标记变量并记录当前回文的起止索引，最后返回最长回文子串。

### Python

```python
class Solution:
    # @param {string} s input string
    # @return {string} the longest palindromic substring
    def longestPalindrome(self, s):
        if not s:
            return ""

        n = len(s)
        longest, left, right = 0, 0, 0
        for i in xrange(0, n):
            for j in xrange(i + 1, n + 1):
                substr = s[i:j]
                if self.isPalindrome(substr) and len(substr) > longest:
                    longest = len(substr)
                    left, right = i, j
        # construct longest substr
        result = s[left:right]
        return result

    def isPalindrome(self, s):
        if not s:
            return False
        # reverse compare
        return s == s[::-1]
```

### C++

```c++
class Solution {
public:
    /**
     * @param s input string
     * @return the longest palindromic substring
     */
    string longestPalindrome(string& s) {
        string result;
        if (s.empty()) return s;

        int n = s.size();
        int longest = 0, left = 0, right = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j <= n; ++j) {
                string substr = s.substr(i, j - i);
                if (isPalindrome(substr) && substr.size() > longest) {
                    longest = j - i;
                    left = i;
                    right = j;
                }
            }
        }

        result = s.substr(left, right - left);
        return result;
    }

private:
    bool isPalindrome(string &s) {
        int n = s.size();
        for (int i = 0; i < n; ++i) {
            if (s[i] != s[n - i - 1]) return false;
        }
        return true;
    }
};
```

### Java

```java
public class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.isEmpty()) return "";
        
        final int sLen = s.length();
        int longest = 0, left = 0;
        for (int i = 0; i < sLen; i++) {
            for (int j = i; j < sLen; j++) {
                if (j - i + 1 > longest && isPalindrome(s, i, j)) {
                    longest = j - i + 1;
                    left = i;
                }
            }
        }

        return s.substring(left, left + longest);
    }

    private boolean isPalindrome(String s, int left, int right) {
        for (int i = left, j = right; i <= j; i++, j--) {
            if (s.charAt(i) != s.charAt(j)) return false;
        }
        return true;
    }
}
```

### 源码分析

使用 left 作为子串的起止索引，longest 作为当前最长长度，用于最后构造返回结果，避免中间构造字符串以减少开销。两重循环中需要注意的是第二重循环的起止值及判断回文中的索引起止值。

### 复杂度分析

穷举所有的子串，$$O(C_n^2) = O(n^2)$$, 每次判断字符串是否为回文，复杂度为 $$O(n)$$, 故总的时间复杂度为 $$O(n^3)$$, 大数据集下可能 TLE. 仅在最后返回取子串，空间复杂度为 $$O(1)$$.
P.S. 目前仅 Java 对回文判断优化过。

## 题解2

题解1 中的思路是从子串出发判断回文串进而取最长，可以发现其中有许多重复的计算，如果我们从回文串本身出发进行求解，即从子串中间向左向右判断是否符合要求，由于回文串必定是某一子串，故只需从字符串的某一索引展开，分奇偶长度判断，时间复杂度可降为 $$O(n^2)$$.

### C++

```c++
string palindrome(string& s, int l, int r) {
	while (l>=0 && r<s.size() && s[l]==s[r]) l--, r++;
	return s.substr(l+1, r-l-1);
}

string longestPalindrome(string s) {
	if (s.empty()) return s;

	string res;
	for (int i=0; i<s.size(); i++) {
		string t;
		t = palindrome(s, i, i);
		if (t.size() > res.size()) res = t;
	   
		t = palindrome(s, i, i+1);
		if (t.size() > res.size()) res = t;   
	}
	return res;
}
```

### Java

```java
public class Solution {
    public String longestPalindrome(String s) {
        if (s == null || s.isEmpty()) return "";
        
        final int sLen = s.length();
        int longest = 0, left = 0;
        for (int i = 0; i < sLen; i++) {
            // odd
            int leftIndex = leftPalindromeIndex(s, i, i);
            int palindromeLen = 2 * (i - leftIndex) + 1;
            if (palindromeLen > longest) {
                left = leftIndex;
                longest = palindromeLen;
            }
            // even
            leftIndex = leftPalindromeIndex(s, i, i + 1);
            palindromeLen = 2 * (i - leftIndex + 1);
            if (palindromeLen > longest) {
                left = leftIndex;
                longest = palindromeLen;
            }
        }

        return s.substring(left, left + longest);
    }

    private int leftPalindromeIndex(String s, int left, int right) {
        for (; left >= 0 && right < s.length(); left--, right++) {
            if (s.charAt(left) != s.charAt(right)) break;
        }
        return left + 1;
    }
}
```

### 源码分析

假定扫描的每个字母是回文的中间位置（需要处理奇偶两种情况），从该位置向两头搜索寻找最大回文长度。

### 复杂度分析

时间复杂度降到 $$O(n^2)$$.

## 题解3

另外还有一个O（n）的解法，具体参考下面的链接
http://articles.leetcode.com/2011/11/longest-palindromic-substring-part-ii.html

## Reference

- [Longest Palindromic Substring Part I | LeetCode](http://articles.leetcode.com/2011/11/longest-palindromic-substring-part-i.html)
- [Longest Palindromic Substring Part II | LeetCode](http://articles.leetcode.com/2011/11/longest-palindromic-substring-part-ii.html)
