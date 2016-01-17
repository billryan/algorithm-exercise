# Two Strings Are Anagrams

## Question

- CC150: [(158) Two Strings Are Anagrams](http://www.lintcode.com/en/problem/two-strings-are-anagrams/)
- leetcode: [Valid Anagram | LeetCode OJ](https://leetcode.com/problems/valid-anagram/)

```
Write a method anagram(s,t) to decide if two strings are anagrams or not.

Example
Given s="abcd", t="dcab", return true.

Challenge
O(n) time, O(1) extra space
```

## 題解1 - hashmap 統計字頻

判斷兩個字串是否互為變位詞，若區分大小寫，考慮空白字符時，直接來理解可以認為兩個字串的擁有各不同字符的數量相同。對於比較字符數量的問題常用的方法為遍歷兩個字串，統計其中各字符出現的頻次，若不等則返回`false`. 有很多簡單字串類面試題都是此題的變形題。

### C++

```c++
class Solution {
public:
    /**
     * @param s: The first string
     * @param t: The second string
     * @return true or false
     */
    bool anagram(string s, string t) {
        if (s.empty() || t.empty()) {
            return false;
        }
        if (s.size() != t.size()) {
            return false;
        }

        int letterCount[256] = {0};

        for (int i = 0; i != s.size(); ++i) {
            ++letterCount[s[i]];
            --letterCount[t[i]];
        }
        for (int i = 0; i != t.size(); ++i) {
            if (letterCount[t[i]] != 0) {
                return false;
            }
        }

        return true;
    }
};
```

### 源碼分析

1. 兩個字串長度不等時必不可能為變位詞(需要注意題目條件靈活處理)。
2. 初始化含有256個字符的計數器陣列。
3. 對字串 s 自增，字串 t 遞減，再次遍歷判斷`letterCount`陣列的值，小於0時返回`false`.

在字串長度較長(大於所有可能的字符數)時，還可對第二個`for`循環做進一步優化，即`t.size() > 256`時，使用256替代`t.size()`, 使用`i`替代`t[i]`.

### 複雜度分析

兩次遍歷字串，時間複雜度最壞情況下為 $$O(2n)$$, 使用了額外的陣列，空間複雜度 $$O(256)$$.

## 題解2 - 排序字串

另一直接的解法是對字串先排序，若排序後的字串內容相同，則其互為變位詞。題解1中使用 hashmap 的方法對於比較兩個字串是否互為變位詞十分有效，但是在比較多個字串時，使用 hashmap 的方法複雜度則較高。

### C++

```c++
class Solution {
public:
    /**
     * @param s: The first string
     * @param b: The second string
     * @return true or false
     */
    bool anagram(string s, string t) {
        if (s.empty() || t.empty()) {
            return false;
        }
        if (s.size() != t.size()) {
            return false;
        }

        sort(s.begin(), s.end());
        sort(t.begin(), t.end());

        if (s == t) {
            return true;
        } else {
            return false;
        }
    }
};
```

### 源碼分析

對字串 s 和 t 分別排序，而後比較是否含相同內容。對字串排序時可以採用先統計字頻再組裝成排序後的字串，效率更高一點。

### 複雜度分析

C++的 STL 中 sort 的時間複雜度介於 $$O(n)$$ 和 $$O(n^2)$$之間，判斷`s == t`時間複雜度最壞為 $$O(n)$$.

## Reference

- *CC150 Chapter 9.1* 中文版 p109
