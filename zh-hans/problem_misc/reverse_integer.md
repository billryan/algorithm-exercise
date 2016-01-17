# Reverse Integer

## Question

- leetcode: [Reverse Integer | LeetCode OJ](https://leetcode.com/problems/reverse-integer/)
- lintcode: [(413) Reverse Integer](http://www.lintcode.com/en/problem/reverse-integer/)

### Problem Statement

Reverse digits of an integer. Returns 0 when the reversed integer overflows (signed 32-bit integer).

#### Example

Given x = 123, return 321

Given x = -123, return -321

## 题解

初看这道题觉得先将其转换为字符串然后转置以下就好了，但是仔细一想这种方法存在两种缺陷，一是负号需要单独处理，而是转置后开头的0也需要处理。另一种方法是将原数字逐个弹出，然后再将弹出的数字组装为新数字，咋看以为需要用到栈，实际上却是队列... 所以根本不需要辅助数据结构。关于正负号的处理，我最开始是单独处理的，后来看其他答案时才发现根本就不用分正负考虑。因为`-1 / 10 = 0`.

### Java

```java
public class Solution {
    /**
     * @param n the integer to be reversed
     * @return the reversed integer
     */
    public int reverseInteger(int n) {
        long result = 0;
        while (n != 0) {
            result = n % 10 + 10 * result;
            n /= 10;
        }

        if (result < Integer.MIN_VALUE || result > Integer.MAX_VALUE) {
            return 0;
        }
        return (int)result;
    }
}
```

### 源码分析

注意 lintcode 和 leetcode 的方法名不一样。使用 long 型保存中间结果，最后判断是否溢出。

## Reference

- [LeetCode-Sol-Res/ReverseInt.java at master · FreeTymeKiyan/LeetCode-Sol-Res](https://github.com/FreeTymeKiyan/LeetCode-Sol-Res/blob/master/Easy/ReverseInt.java)
