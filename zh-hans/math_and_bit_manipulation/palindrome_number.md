---
difficulty: Easy
tags:
- Math
title: Palindrome Number
---

# Palindrome Number

## Problem

### Metadata

- tags: Math
- difficulty: Easy
- source(leetcode): <https://leetcode.com/problems/palindrome-number/>
- source(lintcode): <http://www.lintcode.com/en/problem/palindrome-number/>

### Description

Determine whether an integer is a palindrome. Do this without extra space.

click to show spoilers.

**Some hints:**

Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction
of using extra space.

You could also try reversing an integer. However, if you have solved the
problem "Reverse Integer", you know that the reversed integer might overflow.
How would you handle such case?

There is a more generic way of solving this problem.

## 题解1 - 循环处理首尾数字

题意为判断数字是否为回文，要求为不允许使用额外空间，也就是说不能使用类似数字转字符串的方法直接判断。既然不能使用和数字等长的数组空间，那不借助数组来循环判断首尾数字是否相等总是可以的。接下来的问题就转化为怎么获取数字的首尾数字，获取整数的末尾是非常容易的，对10取模即可，那如何获取整数的首部数字呢？用当前整数除以10的幂(幂的大小和整数的宽度一样)即可。确定好初始和循环终止条件即可。

### Java

```java
class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) return false;
        
        int mod = 1000000000;
        while (x / mod == 0 && (mod > 1)) {
            mod /= 10;
        }
        while (mod > 1) {
            if (x / mod != x % 10) {
                return false;
            }
            x = (x % mod) / 10;
            mod /= 100;
        }
        return true;
    }
}
```

### 源码分析

对于32位整数来说，初始化最大的除数为 1000000000, 循环找出适合当前的最大的除数，随后算出首尾的数字并对其进行比对，循环退出条件为首尾不匹配或者除数为1(比对至最后一位).

### 复杂度分析

未使用数组，空间复杂度为 $$O(1)$$. 求最大除数时时间复杂度为数字长度的对数 $$logN$$，判断整数是否回文最差情况下为 $$logN$$, 故综合仍为 $$logN$$.

## 题解2 - 逆序比对

除了解法1中对整数首尾数字进行一一比对之外，还有一种解法则是先得到逆序的数字输出(求模即可)，然后比对逆序输出构建的整数和原整数值，若相等则为回文。这里需要注意的则是在不借助多余空间的情况下构建。

### Java

```java
class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0) return false;

        int prev = 0;
        int y = x;
        while (y > 0) {
            prev = prev * 10 + y % 10;
            y /= 10;
        }
        if (prev == x) {
            return true;
        } else {
            return false;
        }
    }
}
```

### 源码分析

由于构建过程中依赖上一次获得的整数值，故初始化上一个整数为 0, 不断累积原整数对10取模后末尾的值，同时进位10.

### 复杂度分析

空间复杂度为 $$O(1)$$, 时间复杂度为 $$logN$$.
