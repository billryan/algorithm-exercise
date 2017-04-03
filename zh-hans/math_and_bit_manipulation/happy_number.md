# Happy Number

Tags: Hash Table, Math, Easy

## Question

- leetcode: [Happy Number](https://leetcode.com/problems/happy-number/)
- lintcode: [Happy Number](http://www.lintcode.com/en/problem/happy-number/)

### Problem Statement

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any
positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay), or it
loops endlessly in a cycle which does not include 1. Those numbers for which
this process ends in 1 are happy numbers.

**Example: ** 19 is a happy number

  * $$1^2 + 9^2 = 82$$
  * $$8^2 + 2^2 = 68$$
  * $$6^2 + 8^2 = 100$$
  * $$1^2 + 0^2 + 0^2 = 1$$

**Credits:**  
Special thanks to [@mithmatt](https://leetcode.com/discuss/user/mithmatt) and
[@ts](https://leetcode.com/discuss/user/ts) for adding this problem and
creating all test cases.

## 题解

根据指定运算规则判断输入整数是否为『happy number』，容易推断得知最终要么能求得1，要么为环形队列不断循环。
第一种情况容易判断，第二种情况即判断得到的数是否为环形队列，也就是说是否重复出现，这种场景使用哈希表轻易解决。

### Java

```java
public class Solution {
    public boolean isHappy(int n) {
        if (n < 0) return false;

        Set<Integer> set = new HashSet<Integer>();
        set.add(n);
        while (n != 1) {
            n = digitsSquareSum(n);
            if (n == 1) {
                return true;
            } else if (set.contains(n)) {
                return false;
            } else {
                set.add(n);
            }
        }

        return true;
    }

    private int digitsSquareSum(int n) {
        int sum = 0;
        for (; n > 0; n /= 10) {
            sum += (n % 10) * (n % 10);
        }
        return sum;
    }
}
```

### 源码分析

辅助方法计算数字平方和。

### 复杂度分析

有限迭代次数一定终止，时间和空间复杂度均为 $$O(1)$$.