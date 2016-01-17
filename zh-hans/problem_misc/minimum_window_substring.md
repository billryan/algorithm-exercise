# Minimum Window Substring

## Question

- leetcode: [Minimum Window Substring | LeetCode OJ](https://leetcode.com/problems/minimum-window-substring/)
- lintcode: [(32) Minimum Window Substring](http://www.lintcode.com/en/problem/minimum-window-substring/)

### Problem Statement

Given a string source and a string target, find the minimum window in source
which will contain all the characters in target.

#### Example

source = "**ADOBECODEBANC**" target = "**ABC**" Minimum window is "**BANC**".

#### Note

If there is no such window in source that covers all characters in target,
return the emtpy string "".

If there are multiple such windows, you are guaranteed that there will always
be only one unique minimum window in source.

#### Challenge

Can you do it in time complexity O(n) ?

#### Clarification

Should the characters in minimum window has the same order in target?

- Not necessary.

## 题解

计算目标字符串的字符在给定字符串中出现的最小窗口。由于并不需要在给定字符串中有序出现，故只需要统计出现次数。这是典型的需要借助『哈希表』实现的题。题中字符串中的字符可以假定为 ascii 码，那么我们使用256个 ascii 码处理起来较为方便。那么接下来有两个难点，一就是在于怎么知道给定字符串中某一窗口长度已包含目标字符串中的全部字符（可能重复），二是在包含目标字符串中全部字符后如果再出现目标字符串中的其他字符串时如何处理？

其中第一个难点我们通过巧用目标字符串的长度来处理，遍历给定字符串，如果给定字符串中出现的字符次数小于目标字符串，我们就更新总的字符出现次数。第二个难题通过维护窗口起止索引（两根指针）来处理，在给定字符串中出现目标字符串中的全部字符时向前移动窗口起始处，若窗口长度小于之前的窗口长度则更新最终答案要求的窗口起始索引。

### Java

```java
public class Solution {
    /**
     * @param source: A string
     * @param target: A string
     * @return: A string denote the minimum window
     *          Return "" if there is no such a string
     */
    public String minWindow(String source, String target) {
        if (source == null || target == null) return "";
        if (source.length() < target.length()) return "";
        
        final int ASCII_COUNT = 256;
        int[] targetCount = new int[ASCII_COUNT];
        int[] sourceCount = new int[ASCII_COUNT];
        for (int i = 0; i < target.length(); i++) {
            int ch2i = (int)target.charAt(i);
            targetCount[ch2i]++;
        }
        // target string character appeared in source string
        int winStart = 0, winMinStart = 0, winMin = Integer.MAX_VALUE;
        int occurence = 0;
        for (int winEnd = 0; winEnd < source.length(); winEnd++) {
            // convert character to integer
            int ch2i = (int)source.charAt(winEnd);
            sourceCount[ch2i]++;
            // character occur in both source and target
            if (targetCount[ch2i] > 0 && targetCount[ch2i] >= sourceCount[ch2i]) {
                occurence++;
            }
            // adjust window size if all the target char occur in source
            if (occurence == target.length()) {
                // convert character to integer
                int ch2i2 = (int)source.charAt(winStart);
                while (sourceCount[ch2i2] > targetCount[ch2i2]) {
                    sourceCount[ch2i2]--;
                    winStart++;
                    ch2i2 = (int)source.charAt(winStart);
                }
                // update winMinStart
                if (winMin > winEnd - winStart + 1) {
                    winMin = winEnd - winStart + 1;
                    winMinStart = winStart;
                }
            }
        }
        
        if (winMin == Integer.MAX_VALUE) {
            return "";
        } else {
            return source.substring(winMinStart, winMinStart + winMin);
        }
    }
}
```

### 源码分析

整个程序最为核心的即为题解中所提出的两大难点，窗口移动的方法使用贪心实现，在窗口长度变小时需要记录起始索引。

### 复杂度分析

遍历给定字符串一次，外加更新窗口时可能需要遍历给定字符串一次，时间复杂度为 $$O(n)$$, 使用了几个额外变量，空间复杂度 $$O(1)$$.

## Reference

- [水中的鱼: [LeetCode] Minimum Window Substring 解题报告](http://fisherlei.blogspot.com/2012/12/leetcode-minimum-window-substring.html)
