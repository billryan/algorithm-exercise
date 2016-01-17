# Longest Palindromic Substring

- tags: [palindrome]

## Question

- leetcode: [Longest Palindromic Substring | LeetCode OJ](https://leetcode.com/problems/longest-palindromic-substring/)
- lintcode: [(200) Longest Palindromic Substring](http://www.lintcode.com/en/problem/longest-palindromic-substring/)

```
Given a string S, find the longest palindromic substring in S.
You may assume that the maximum length of S is 1000,
and there exists one unique longest palindromic substring.

Example
Given the string = "abcdzdcab", return "cdzdc".
Challenge
O(n2) time is acceptable. Can you do it in O(n) time.
```

## 題解1 - 窮舉搜索(brute force)

最簡單的方案，窮舉所有可能的子串，判斷子串是否為回文，使用一變數記錄最大回文長度，若新的回文超過之前的最大回文長度則更新標記變數並記錄當前回文的起止索引，最後返回最長回文子串。

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
    /**
     * @param s input string
     * @return the longest palindromic substring
     */
    public String longestPalindrome(String s) {
        String result = new String();
        if (s == null || s.isEmpty()) return result;

        int n = s.length();
        int longest = 0, left = 0, right = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j <= n; j++) {
                String substr = s.substring(i, j);
                if (isPalindrome(substr) && substr.length() > longest) {
                    longest = substr.length();
                    left = i;
                    right = j;
                }
            }
        }

        result = s.substring(left, right);
        return result;
    }

    private boolean isPalindrome(String s) {
        if (s == null || s.isEmpty()) return false;

        int n = s.length();
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) != s.charAt(n - i - 1)) return false;
        }

        return true;
    }
}
```

### 源碼分析

使用`left`, `right`作為子串的起止索引，用於最後構造返回結果，避免中間構造字串以減少開銷。

### 複雜度分析

窮舉所有的子串，$$O(C_n^2) = O(n^2)$$, 每次判斷字符串是否為回文，複雜度為 $$O(n)$$, 故總的時間複雜度為 $$O(n^3)$$. 故大數據集下可能 TLE. 使用了`substr`作為臨時子串，空間複雜度為 $$O(n)$$.

## 題解2 - 動態規劃(dynamic programming)

要改善效率，可以觀察哪邊有重複而冗餘的計算，例如已知"bab"為回文的情況下，若前後各加一個相同的字元，"cbabc"，當然也是回文。
因此可以使用動態規劃，將先前的結果儲存起來，假設字串`s`的長度為`n`，我們創建一個$$(n\times n)$$的bool值矩陣`P`，`P[i, j], i<= j`表示由$$[s_i, ..., s_j]$$構成的子串是否為回文。就可以得到一個與子結構關係<br>
`
P[i, j] = P[i+1, j-1] AND s[i] == s[j]
`

而基本狀態為<br>
`
P[i, i] = true
`
<br>與<br>
`
P[i, i+1] = (s[i] == s[i+1])
`

因此可以整理成程式碼如下
```c++
string longestPalindrome(string s) {
    int n = s.length();
    int maxBegin = 0;
    int maxLen = 1;
    bool table[1000][1000] = {false};

    for (int i = 0; i < n; i++) {
        table[i][i] = true;
    }

    for (int i = 0; i < n-1; i++) {
            if (s[i] == s[i+1]) {
            table[i][i+1] = true;
            maxBegin = i;
            maxLen = 2;
        }
    }
    for (int len = 3; len <= n; len++) {
        for (int i = 0; i < n-len+1; i++) {
            int j = i+len-1;
            if (s[i] == s[j] && table[i+1][j-1]) {
                table[i][j] = true;
                maxBegin = i;
                maxLen = len;
            }
        }
    }
    return s.substr(maxBegin, maxLen);
}
```

###複雜度分析

仍然是兩層迴圈，但每次迴圈內部只有常數次操作，因此時間複雜度是$$O(n^2)$$，另外空間複雜度是$$O(n^2)$$

## 題解 3 - Manacher's Algorithm

## Reference

- [Longest Palindromic Substring Part I | LeetCode](http://articles.leetcode.com/2011/11/longest-palindromic-substring-part-i.html)
- [Longest Palindromic Substring Part II | LeetCode](http://articles.leetcode.com/2011/11/longest-palindromic-substring-part-ii.html)
