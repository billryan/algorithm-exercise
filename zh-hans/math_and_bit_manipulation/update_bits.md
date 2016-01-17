# Update Bits

## Question

- CTCI: [(179) Update Bits](http://www.lintcode.com/en/problem/update-bits/)

```
Given two 32-bit numbers, N and M, and two bit positions, i and j.
Write a method to set all bits between i and j in N equal to M
(e g , M becomes a substring of N located at i and starting at j)

Example
Given N=(10000000000)2, M=(10101)2, i=2, j=6

return N=(10001010100)2

Note
In the function, the numbers N and M will given in decimal,
you should also return a decimal number.

Challenge
Minimum number of operations?

Clarification
You can assume that the bits j through i have enough space to fit all of M.
That is, if M=10011，
you can assume that there are at least 5 bits between j and i.
You would not, for example, have j=3 and i=2,
because M could not fully fit between bit 3 and bit 2.
```

## 题解

Cracking The Coding Interview 上的题，题意简单来讲就是使用 M 代替 N 中的第`i`位到第`j`位。很显然，我们需要借用掩码操作。大致步骤如下：

1. 得到第`i`位到第`j`位的比特位为0，而其他位均为1的掩码`mask`。
2. 使用`mask`与 N 进行按位与，清零 N 的第`i`位到第`j`位。
3. 对 M 右移`i`位，将 M 放到 N 中指定的位置。
4. 返回 N | M 按位或的结果。

获得掩码`mask`的过程可参考 CTCI 书中的方法，先获得掩码(1111...000...111)的左边部分，然后获得掩码的右半部分，最后左右按位或即为最终结果。

### C++ <i class="fa fa-bug"></i>

```c++
class Solution {
public:
    /**
     *@param n, m: Two integer
     *@param i, j: Two bit positions
     *return: An integer
     */
    int updateBits(int n, int m, int i, int j) {
        int ones = ~0;
        int left = ones << (j + 1);
        int right = ((1 << i) - 1);
        int mask = left | right;

        return (n & mask) | (m << i);
    }
};
```

### 源码分析

在给定测试数据`[-521,0,31,31]`时出现了 WA, 也就意味着目前这段程序是存在 bug 的，此时`m = 0, i = 31, j = 31`，仔细瞅瞅到底是哪几行代码有问题？本地调试后发现问题出在`left`那一行，`left`移位后仍然为`ones`, 这是为什么呢？在`j`为31时`j + 1`为32，也就是说此时对`left`位移的操作已经超出了此时`int`的最大位宽！

### C++

```c++
class Solution {
public:
    /**
     *@param n, m: Two integer
     *@param i, j: Two bit positions
     *return: An integer
     */
    int updateBits(int n, int m, int i, int j) {
        int ones = ~0;
        int mask = 0;
        if (j < 31) {
            int left = ones << (j + 1);
            int right = ((1 << i) - 1);
            mask = left | right;
        } else {
            mask = (1 << i) - 1;
        }

        return (n & mask) | (m << i);
    }
};
```

### 源码分析

使用`~0`获得全1比特位，在`j == 31`时做特殊处理，即不必求`left`。求掩码的右侧1时使用了`(1 << i) - 1`, 题中有保证第`i`位到第`j`位足以容纳 M, 故不必做溢出处理。

### 复杂度分析

时间复杂度和空间复杂度均为 $$O(1)$$.

### C++

```c++
class Solution {
public:
    /**
     *@param n, m: Two integer
     *@param i, j: Two bit positions
     *return: An integer
     */
    int updateBits(int n, int m, int i, int j) {
        // get the bit width of input integer
        int bitwidth = 8 * sizeof(n);
        int ones = ~0;
        // use unsigned for logical shift
        unsigned int mask = ones << (bitwidth - (j - i + 1));
        mask = mask >> (bitwidth - 1 - j);

        return (n & (~mask)) | (m << i);
    }
};
```

### 源码分析

之前的实现需要使用`if`判断，但实际上还有更好的做法，即先获得`mask`的反码，最后取反即可。但这种方法需要提防有符号数，因为 C/C++ 中对有符号数的移位操作为算术移位，也就是说对负数右移时会在前面补零。解决办法可以使用无符号数定义`mask`.

按题意 int 的位数为32，但考虑到通用性，可以使用`sizeof`获得其真实位宽。

### 复杂度分析

时间复杂度和空间复杂度均为 $$O(1)$$.

## Reference

- [c++ - logical shift right on signed data - Stack Overflow](http://stackoverflow.com/questions/13221369/logical-shift-right-on-signed-data)
- [Update Bits | 九章算法](http://www.jiuzhang.com/solutions/update-bits/)
- *CTCI 5th Chapter 9.5 中文版* p163
