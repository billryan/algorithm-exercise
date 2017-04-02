# Single Number

Tags: Hash Table, Bit Manipulation, Easy

## Question

- leetcode: [Single Number](https://leetcode.com/problems/single-number/)
- lintcode: [Single Number](http://www.lintcode.com/en/problem/single-number/)

### Problem Statement

Given an array of integers, every element appears _twice_ except for one. Find
that single one.

**Note:**  
Your algorithm should have a linear runtime complexity. Could you implement it
without using extra memory?

## 题解

「找单数」系列题，技巧性较强，需要灵活运用位运算的特性。根据题意，共有`2*n + 1`个数，且有且仅有一个数落单，要找出相应的「单数」。鉴于有空间复杂度的要求，不可能使用另外一个数组来保存每个数出现的次数，考虑到异或运算的特性，根据`x ^ x = 0`和`x ^ 0 = x`可将给定数组的所有数依次异或，最后保留的即为结果。

### C++

```c++
class Solution {
public:
	/**
	 * @param A: Array of integers.
	 * return: The single number.
	 */
    int singleNumber(vector<int> &A) {
        if (A.empty()) {
            return -1;
        }
        int result = 0;

        for (vector<int>::iterator iter = A.begin(); iter != A.end(); ++iter) {
            result = result ^ *iter;
        }

        return result;
    }
};
```

### Java

```java
public class Solution {
    public int singleNumber(int[] nums) {
        if (nums == null || nums.length == 0) return -1;

        int result = 0;
        for (int num : nums) {
            result ^= num;
        }

        return result;
    }
}
```

### 源码分析

1. 异常处理(OJ上对于空vector的期望结果为0，但个人认为-1更为合理)
2. 初始化返回结果`result`为0，因为`x ^ 0 = x`
