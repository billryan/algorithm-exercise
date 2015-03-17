# 字符串


## 字符串查找

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
