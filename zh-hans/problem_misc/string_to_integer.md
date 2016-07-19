# String to Integer

## Question

- leetcode: [String to Integer (atoi) | LeetCode OJ](https://leetcode.com/problems/string-to-integer-atoi/)
- lintcode: [(54) String to Integer(atoi)](http://www.lintcode.com/en/problem/string-to-integer-ii/)

```
Implement function atoi to convert a string to an integer.

If no valid conversion could be performed, a zero value is returned.

If the correct value is out of the range of representable values,
INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

Example
"10" => 10

"-1" => -1

"123123123123123" => 2147483647

"1.0" => 1
```

## 题解

经典的字符串转整数题，边界条件比较多，比如是否需要考虑小数点，空白及非法字符的处理，正负号的处理，科学计数法等。最先处理的是空白字符，然后是正负号，接下来只要出现非法字符(包含正负号，小数点等，无需对这两类单独处理)即退出，否则按照正负号的整数进位加法处理。

### Java

```java
public class Solution {
    /**
     * @param str: A string
     * @return An integer
     */
    public int atoi(String str) {
        if (str == null || str.length() == 0) return 0;

        // trim left and right spaces
        String strTrim = str.trim();
        int len = strTrim.length();
        // sign symbol for positive and negative
        int sign = 1;
        // index for iteration
        int i = 0;
        if (strTrim.charAt(i) == '+') {
            i++;
        } else if (strTrim.charAt(i) == '-') {
            sign = -1;
            i++;
        }

        // store the result as long to avoid overflow
        long result = 0;
        while (i < len) {
            if (strTrim.charAt(i) < '0' || strTrim.charAt(i) > '9') {
                break;
            }
            result = 10 * result + sign * (strTrim.charAt(i) - '0');
            // overflow
            if (result > Integer.MAX_VALUE) {
                return Integer.MAX_VALUE;
            } else if (result < Integer.MIN_VALUE) {
                return Integer.MIN_VALUE;
            }
            i++;
        }

        return (int)result;
    }
}
```

### 源码分析

符号位使用整型表示，便于后期相乘相加。在 while 循环中需要注意判断是否已经溢出，如果放在 while 循环外面则有可能超过 long 型范围。

### 复杂度分析

略

## Reference

- [String to Integer (atoi) 参考程序 Java/C++/Python](http://www.jiuzhang.com/solutions/string-to-integer-atoi/)
