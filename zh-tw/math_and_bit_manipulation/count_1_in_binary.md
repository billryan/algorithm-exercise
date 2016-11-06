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

## 題解

題 [O1 Check Power of 2](http://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/o1_check_power_of_2.html) 的進階版，`x & (x - 1)` 的含義爲去掉二進制數中1的最後一位，無論 x 是正數還是負數都成立。

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

### 源碼分析

累加計數器即可。

### 複雜度分析

這種算法依賴於數中1的個數，時間複雜度爲 $$O(m)$$. 空間複雜度 $$O(1)$$.

## Reference

- [Number of 1 bits | LeetCode](http://articles.leetcode.com/2010/09/number-of-1-bits.html) - 評論中有關於不同演算法性能的討論
