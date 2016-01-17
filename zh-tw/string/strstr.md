# strStr

## Question

- leetcode: [Implement strStr() | LeetCode OJ](https://leetcode.com/problems/implement-strstr/)
- lintcode: [lintcode - (13) strstr](http://www.lintcode.en/problem/strstr/)

```
strstr (a.k.a find sub string), is a useful function in string operation.
You task is to implement this function.

For a given source string and a target string,
you should output the "first" index(from 0) of target string in source string.

If target is not exist in source, just return -1.

Example
If source="source" and target="target", return -1.

If source="abcdabcdefg" and target="bcd", return 1.

Challenge
O(n) time.

Clarification
Do I need to implement KMP Algorithm in an interview?

    - Not necessary. When this problem occurs in an interview,
    the interviewer just want to test your basic implementation ability.
```

## 題解

對於字串查找問題，可使用雙重for迴圈解決，效率更高的則為KMP算法。

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

### 源碼分析

1. 邊界檢查：`source`和`target`有可能是空串。
2. 邊界檢查之下標溢出：注意變量`i`的循環判斷條件，如果是單純的`i < source.length()`則在後面的`source.charAt(i + j)`時有可能溢出。
2. 代碼風格：（1）運算符`==`兩邊應加空格；（2）變量名不要起`s1``s2`這類，要有意義，如`target``source`；（3）即使if語句中只有一句話也要加大括號，即`{return -1;}`；（4）Java 代碼的大括號一般在同一行右邊，C++ 代碼的大括號一般另起一行；（5）`int i, j;`聲明前有一行空格，是好的代碼風格。
3. 不要在for的條件中聲明`i`,`j`，容易在循環外再使用時造成編譯錯誤，錯誤代碼示例：

## Another Similar Question

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
