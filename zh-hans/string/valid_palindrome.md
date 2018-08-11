# Valid Palindrome

Tags: Two Pointers, String, Easy

## Question

- leetcode: [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
- lintcode: [Valid Palindrome](http://www.lintcode.com/en/problem/valid-palindrome/)

### Problem Statement

Given a string, determine if it is a palindrome, considering only alphanumeric
characters and ignoring cases.

For example,  
`"A man, a plan, a canal: Panama"` is a palindrome.  
`"race a car"` is _not_ a palindrome.

**Note:**  

Have you consider that the string might be empty? This is a good question to
ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

## 题解

字符串的回文判断问题，由于字符串可随机访问，故逐个比较首尾字符是否相等最为便利，即常见的『两根指针』技法。此题忽略大小写，并只考虑字母和数字字符。链表的回文判断总结见 [Check if a singly linked list is palindrome](http://algorithm.yuanbin.me/zh-hans/linked_list/check_if_a_singly_linked_list_is_palindrome.html).

### Python

```python
class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        if not s:
            return True

        l, r = 0, len(s) - 1

        while l < r:
            # find left alphanumeric character
            if not s[l].isalnum():
                l += 1
                continue
            # find right alphanumeric character
            if not s[r].isalnum():
                r -= 1
                continue
            # case insensitive compare
            if s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        #
        return True
```

### C++

```c++
class Solution {
public:
    /**
     * @param s A string
     * @return Whether the string is a valid palindrome
     */
    bool isPalindrome(string& s) {
        if (s.empty()) return true;

        int l = 0, r = s.size() - 1;
        while (l < r) {
            // find left alphanumeric character
            if (!isalnum(s[l])) {
                ++l;
                continue;
            }
            // find right alphanumeric character
            if (!isalnum(s[r])) {
                --r;
                continue;
            }
            // case insensitive compare
            if (tolower(s[l]) == tolower(s[r])) {
                ++l;
                --r;
            } else {
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
    public boolean isPalindrome(String s) {
        if (s == null || s.trim().isEmpty()) {
            return true;
        }
        
        int l = 0, r = s.length() - 1;
        while (l < r) {
            if(!Character.isLetterOrDigit(s.charAt(l))) {
                l++;
                continue;
            }
            if(!Character.isLetterOrDigit(s.charAt(r))) {
                r--;
                continue;
            }
            if (Character.toLowerCase(s.charAt(l)) == Character.toLowerCase(s.charAt(r))) {
                l++;
                r--;
            } else {
                return false;
            }
        }

        return true;
    }
}
```

### 源码分析

两步走：

1. 找到最左边和最右边的第一个合法字符(字母或者字符)
2. 一致转换为小写进行比较

字符的判断尽量使用语言提供的 API, while 循环内部使用 if 而不是 while 可将 `l < r` 的逻辑移至一处。

### 复杂度分析

两根指针遍历一次，时间复杂度 $$O(n)$$, 空间复杂度 $$O(1)$$.
