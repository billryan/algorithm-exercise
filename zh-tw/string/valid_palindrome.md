# Valid Palindrome

- tags: [palindrome]

## Question

- leetcode: [Valid Palindrome | LeetCode OJ](https://leetcode.com/problems/valid-palindrome/)
- lintcode: [(415) Valid Palindrome](http://www.lintcode.com/en/problem/valid-palindrome/)

```
Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.

Example
"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.
Note
Have you consider that the string might be empty?
This is a good question to ask during an interview.
For the purpose of this problem,
we define empty string as valid palindrome.

Challenge
O(n) time without extra memory.
```

## 題解

字符串的回文判斷問題，由於字符串可隨機訪問，故逐個比較首尾字符是否相等最為便利，即常見的『兩根指針』技法。此題忽略大小寫，並只考慮字母和數字字符。鏈表的回文判斷總結見 [Check if a singly linked list is palindrome](http://algorithm.yuanbin.zh-hans/linked_list/check_if_a_singly_linked_list_is_palindrome.html).

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
    /**
     * @param s A string
     * @return Whether the string is a valid palindrome
     */
    public boolean isPalindrome(String s) {
        if (s == null || s.isEmpty()) return true;

        int l = 0, r = s.length() - 1;
        while (l < r) {
            // find left alphanumeric character
            if (!Character.isLetterOrDigit(s.charAt(l))) {
                l++;
                continue;
            }
            // find right alphanumeric character
            if (!Character.isLetterOrDigit(s.charAt(r))) {
                r--;
                continue;
            }
            // case insensitive compare
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

### 源碼分析

兩步走：

1. 找到最左邊和最右邊的第一個合法字元(字母或者字元)
2. 一致轉換為小寫進行比較

字元的判斷盡量使用語言提供的 API

### 複雜度分析

兩根指標遍歷一次，時間複雜度 $$O(n)$$, 空間複雜度 $$O(1)$$.
