# Count and Say

## Question

- leetcode: [Count and Say | LeetCode OJ](https://leetcode.com/problems/count-and-say/)
- lintcode: [(420) Count and Say](http://www.lintcode.com/en/problem/count-and-say/)

```
The count-and-say sequence is the sequence of integers beginning as follows:

1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.

11 is read off as "two 1s" or 21.

21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the nth sequence.

Example
Given n = 5, return "111221".

Note
The sequence of integers will be represented as a string.
```

## 题解

题目大意是找第 n 个数(字符串表示)，规则则是对于连续字符串，表示为重复次数+数本身。

### C++
```c++
string countAndSay(int n) {
    if (n == 0) return "";
    string res = "1";
    while (--n) {
        string cur = "";
        for (int i = 0; i < res.size(); i++) {
            int count = 1;
             while ((i + 1 < res.size()) && (res[i] == res[i + 1])){
                count++;   
                i++;
            }
            cur += to_string(count) + res[i];
        }
        res = cur;
    }
    return res;
}
```

### Java

```java
public class Solution {
    /**
     * @param n the nth
     * @return the nth sequence
     */
    public String countAndSay(int n) {
        if (n <= 0) return null;

        String s = "1";
        for (int i = 1; i < n; i++) {
            int count = 1;
            StringBuilder sb = new StringBuilder();
            int sLen = s.length();
            for (int j = 0; j < sLen; j++) {
                if (j < sLen - 1 && s.charAt(j) == s.charAt(j + 1)) {
                    count++;
                } else {
                    sb.append(count + "" + s.charAt(j));
                    // reset
                    count = 1;
                }
            }
            s = sb.toString();
        }

        return s;
    }
}
```

### 源码分析

字符串是动态生成的，故使用 StringBuilder 更为合适。注意s 初始化为"1", 第一重 for循环中注意循环的次数为 n-1.

### 复杂度分析

略

### 题解2 - 递归
### C++
``` c++
class Solution {
public:
    string countAndSay(int n) {
        if (n == 1) return "1";             // base case
        string res, tmp = countAndSay(n - 1);  // recursion
        char c = tmp[0];
        int count = 1;
        for (int i = 1; i < tmp.size(); i++)
            if (tmp[i] == c)
                count++;
            else {
                res += to_string(count);
                res.push_back(c);
                c = tmp[i];
                count = 1;
            }
        res += to_string(count);
        res.push_back(c);
        return res;
    }
};
```

## Reference

- [[leetcode]Count and Say - 喵星人与汪星人](http://huntfor.iteye.com/blog/2059877)
