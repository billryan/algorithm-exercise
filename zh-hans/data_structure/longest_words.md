# Longest Words

## Question

- lintcode: [(133) Longest Words](http://www.lintcode.com/en/problem/longest-words/)

```
Given a dictionary, find all of the longest words in the dictionary.

Example
Given

{
  "dog",
  "google",
  "facebook",
  "internationalization",
  "blabla"
}
the longest words are(is) ["internationalization"].

Given

{
  "like",
  "love",
  "hate",
  "yes"
}
the longest words are ["like", "love", "hate"].

Challenge
It's easy to solve it in two passes, can you do it in one pass?
```

## 题解

简单题，容易想到的是首先遍历以便，找到最长的字符串，第二次遍历时取最长的放到最终结果中。但是如果只能进行一次遍历呢？一次遍历意味着需要维护当前遍历的最长字符串，这必然有比较与更新删除操作，这种情况下使用双端队列最为合适，这道题稍微特殊一点，不必从尾端插入，只需在遍历时若发现比数组中最长的元素还长时删除整个列表。

### Java

```java
class Solution {
    /**
     * @param dictionary: an array of strings
     * @return: an arraylist of strings
     */
    ArrayList<String> longestWords(String[] dictionary) {
        ArrayList<String> result = new ArrayList<String>();
        if (dictionary == null || dictionary.length == 0) return result;

        for (String str : dictionary) {
            // combine empty and shorter length
            if (result.isEmpty() || str.length() > result.get(0).length()) {
                result.clear();
                result.add(str);
            } else if (str.length() == result.get(0).length()) {
                result.add(str);
            }
        }

        return result;
    }
}
```

### 源码分析

熟悉变长数组的常用操作。

### 复杂度分析

时间复杂度 $$O(n)$$, 最坏情况下需要保存 n - 1个字符串，空间复杂度 $$O(n)$$.

## Reference

- [Lintcode: Longest Words | codesolutiony](https://codesolutiony.wordpress.com/2015/06/07/lintcode-longest-words/)
