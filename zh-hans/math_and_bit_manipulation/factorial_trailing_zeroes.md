# Factorial Trailing Zeroes

## Question

- leetcode: [Factorial Trailing Zeroes | LeetCode OJ](https://leetcode.com/problems/factorial-trailing-zeroes/)
- lintcode: [(2) Trailing Zeros](http://www.lintcode.com/en/problem/trailing-zeros/)

```
Write an algorithm which computes the number of trailing zeros in n factorial.

Example
11! = 39916800, so the out should be 2

Challenge
O(log N) time
```

## 题解1 - Iterative

找阶乘数中末尾的连零数量，容易想到的是找相乘能为10的整数倍的数，如 $$2 \times 5$$, $$1 \times 10$$ 等，遥想当初做阿里笔试题时遇到过类似的题，当时想着算算5和10的个数就好了，可万万没想到啊，25可以变为两个5相乘！真是蠢死了... 根据数论里面的知识，任何正整数都可以表示为它的质因数的乘积[^wikipedia]。所以比较准确的思路应该是计算质因数5和2的个数，取小的即可。质因数2的个数显然要大于5的个数，故只需要计算给定阶乘数中质因数中5的个数即可。原题的问题即转化为求阶乘数中质因数5的个数，首先可以试着分析下100以内的数，再试试100以上的数，聪明的你一定想到了可以使用求余求模等方法 :)

### Python

```python
class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        if n < 0:
            return -1

        count = 0
        while n > 0:
            n /= 5
            count += n

        return count
```

### C++

```c++
class Solution {
public:
    int trailingZeroes(int n) {
        if (n < 0) {
            return -1;
        }

        int count = 0;
        for (; n > 0; n /= 5) {
            count += (n / 5);
        }

        return count;
    }
};
```

### Java

```java
public class Solution {
    public int trailingZeroes(int n) {
        if (n < 0) {
            return -1;
        }

        int count = 0;
        for (; n > 0; n /= 5) {
            count += (n / 5);
        }

        return count;
    }
}
```

### 源码分析

1. 异常处理，小于0的数返回-1.
2. 先计算5的正整数幂都有哪些，不断使用 n / 5 即可知质因数5的个数。
3. 在循环时使用 `n /= 5` 而不是 `i *= 5`, 可有效防止溢出。

> **Warning** lintcode 和 leetcode 上的方法名不一样，在两个 OJ 上分别提交的时候稍微注意下。

### 复杂度分析

关键在于`n /= 5`执行的次数，时间复杂度 $$\log_5 n$$，使用了`count`作为返回值，空间复杂度 $$O(1)$$.

## 题解2 - Recursive

可以使用迭代处理的程序往往用递归，而且往往更为优雅。递归的终止条件为`n <= 0`.

### Python

```python
class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        if n == 0:
            return 0
        elif n < 0:
            return -1
        else:
            return n / 5 + self.trailingZeroes(n / 5)
```

### C++

```c++
class Solution {
public:
    int trailingZeroes(int n) {
        if (n == 0) {
            return 0;
        } else if (n < 0) {
            return -1;
        } else {
            return n / 5 + trailingZeroes(n / 5);
        }
    }
};
```

### Java

```java
public class Solution {
    public int trailingZeroes(int n) {
        if (n == 0) {
            return 0;
        } else if (n < 0) {
            return -1;
        } else {
            return n / 5 + trailingZeroes(n / 5);
        }
    }
}
```

### 源码分析

这里将负数输入视为异常，返回-1而不是0. 注意使用递归时务必注意收敛和终止条件的返回值。这里递归层数最多不超过 $$\log_5 n$$, 因此效率还是比较高的。

### 复杂度分析

递归层数最大为 $$\log_5 n$$, 返回值均在栈上，可以认为没有使用辅助的堆空间。

## Reference

- [^wikipedia]: [Prime factor - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Prime_factor)
- [Count trailing zeroes in factorial of a number - GeeksforGeeks](http://www.geeksforgeeks.org/count-trailing-zeroes-factorial-number/)
