# Fibonacci

## Question

- lintcode: [(366) Fibonacci](http://www.lintcode.com/en/problem/fibonacci/)

### Problem Statement

Find the _N_th number in Fibonacci sequence.

A Fibonacci sequence is defined as follow:

  * The first two numbers are 0 and 1.
  * The _i_ th number is the sum of _i_-1 th number and _i_-2 th number.

The first ten numbers in Fibonacci sequence is:

`0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...`

#### Example

Given `1`, return `0`

Given `2`, return `1`

Given `10`, return `34`

#### Note

The _N_th fibonacci number won't exceed the max value of signed 32-bit integer
in the test cases.

## 题解

斐波那契数列使用递归极其容易实现，其实使用非递归的方法也很容易，不断向前滚动即可。

### C++
```c++
class Solution{
public:
    /**
     * @param n: an integer
     * @return an integer f(n)
     */
    int fibonacci(int n) {
        if (n <= 0) return -1;
        if (n == 1) return 0;
        if (n == 2) return 1;
        
        int fn = 0, fn1 = 0, fn2 = 1;
        for (int i = 3; i <= n; i++) {
            fn = fn1 + fn2;
            fn1 = fn2;
            fn2 = fn;
        }
        return fn;
    }
};
```

### Java

```java
class Solution {
    /**
     * @param n: an integer
     * @return an integer f(n)
     */
    public int fibonacci(int n) {
        if (n <= 0) return -1;
        if (n == 1) return 0;
        if (n == 2) return 1;

        int fn = 0, fn1 = 1, fn2 = 0;
        for (int i = 3; i <= n; i++) {
            fn = fn1 + fn2;
            fn2 = fn1;
            fn1 = fn;
        }

        return fn;
    }
}
```

### 源码分析

1. corner cases
2. 初始化 fn, fn1, fn2, 建立地推关系。
3. 注意 fn, fn2, fn1的递推顺序。

### 复杂度分析

遍历一次，时间复杂度为 $$O(n)$$, 使用了两个额外变量，空间复杂度为 $$O(1)$$.
