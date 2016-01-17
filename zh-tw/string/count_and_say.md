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

## 題解

題目大意是找第 n 個數(字符串表示)，規則則是對於連續字符串，表示為重複次數+數本身。純粹是implementation的題目，小心處理實現細節就可以。

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

### C++
```c++
class Solution {
public:
    string countAndSay(int n) {
        string s = "1";
        if(n <= 1) return s;
        stringstream ss;
        while(n-- > 1){
            int count = 1;
            for(int j = 0; j < s.size(); j++){
                if(j < s.size()-1 and s[j] == s[j+1]){
                    count++;
                }
                else{
                    ss << count << s[j];
                    count = 1;
                }
            }
            s = ss.str();
            ss.str("");
        }
        return s;
    }
};
```

### 源碼分析

字符串是動態生成的，故使用 StringBuilder 更為合適。注意s 初始化為"1", 第一重 for循環中注意循環的次數為 n-1.

### 複雜度分析

略

## Reference

- [[leetcode]Count and Say - 喵星人與汪星人](http://huntfor.iteye.com/blog/2059877)
