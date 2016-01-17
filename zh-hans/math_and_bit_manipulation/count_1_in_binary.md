# Count 1 in Binary

## Question

- lintcode: [(365) Count 1 in Binary](http://www.lintcode.com/en/problem/count-1-in-binary/)

```
Count how many 1 in binary representation of a 32-bit integer.

Example
Given 32, return 1

Given 5, return 2

Given 1023, return 9

Challenge
If the integer is n bits with m 1 bits. Can you do it in O(m) time?
```

## 题解

题 [O1 Check Power of 2](http://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/o1_check_power_of_2.html) 的进阶版，`x & (x - 1)` 的含义为去掉二进制数中1的最后一位，无论 x 是正数还是负数都成立。

### C++
``` c++
class Solution {
public:
    /**
     * @param num: an integer
     * @return: an integer, the number of ones in num
     */
    int countOnes(int num) {
        int count=0;
        while (num) {
            num &= num-1;
            count++;
        }
        return count;
    }
};
```

### Java

```java
public class Solution {
    /**
     * @param num: an integer
     * @return: an integer, the number of ones in num
     */
    public int countOnes(int num) {
        int count = 0;
        while (num != 0) {
            num = num & (num - 1);
            count++;
        }

        return count;
    }
}
```

### 源码分析

累加计数器即可。

### 复杂度分析

这种算法依赖于数中1的个数，时间复杂度为 $$O(m)$$. 空间复杂度 $$O(1)$$.

## Reference

- [Number of 1 bits | LeetCode](http://articles.leetcode.com/2010/09/number-of-1-bits.html) - 评论中有关于不同算法性能的讨论
