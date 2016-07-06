# [Flip Bits](http://www.lintcode.com/en/problem/flip-bits/)

## Question

- lintcode: [Flip Bits](http://www.lintcode.com/en/problem/flip-bits/)

### Problem Statement

Determine the number of bits required to flip if you want to convert integer
_n_ to integer _m_.

##### Notice

Both _n_ and _m_ are 32-bit integers.

#### Example

Given _n_ = `31` (11111), _m_ = `14` (01110), return `2`.

## 题解

比较两个数不同的比特位个数，显然容易想到可以使用异或处理两个整数，相同的位上为0，不同的位上为1，故接下来只需将异或后1的个数求出即可。容易想到的方法是移位后和1按位与得到最低位的结果，使用计数器记录这一结果，直至最后操作数为0时返回最终值。这种方法需要遍历元素的每一位，有咩有更为高效的做法呢？还记得之前做过的 [O1 Check Power of 2](http://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/o1_check_power_of_2.html) 吗？`x & (x - 1)`既然可以检查2的整数次幂，那么如何才能进一步得到所有1的个数呢？——将异或得到的数分拆为若干个2的整数次幂，计算得到有多少个2的整数次幂即可。

以上的分析过程对于正数来说是毫无问题的，但问题就在于如果出现了负数如何破？不确定的时候就来个实例测测看，以-2为例，(-2) & (-2 - 1)的计算如下所示(简单起见这里以8位为准)：

```
 11111110 <==> -2   -2 <==> 11111110
+                          &
 11111111 <==> -1   -3 <==> 11111101
=                          =
 11111101                   11111100
```

细心的你也许发现了对于负数来说，其表现也是我们需要的——`x & (x - 1)`的含义即为将二进制比特位的值为1的最低位置零。逐步迭代直至最终值为0时返回。

C/C++ 和 Java 中左溢出时会直接将高位丢弃，正好方便了我们的计算，但是在 Python 中就没这么幸运了，因为溢出时会自动转换类型，Orz... 所以使用 Python 时需要对负数专门处理，转换为求其补数中0的个数。

### Python

```python
class Solution:
    """
    @param a, b: Two integer
    return: An integer
    """
    def bitSwapRequired(self, a, b):
        count = 0
        a_xor_b = a ^ b
        neg_flag = False
        if a_xor_b < 0:
            a_xor_b = abs(a_xor_b) - 1
            neg_flag = True
        while a_xor_b > 0:
            count += 1
            a_xor_b &= (a_xor_b - 1)

        # bit_wise = 32
        if neg_flag:
            count = 32 - count
        return count
```

### C++

```c++
class Solution {
public:
    /**
     *@param a, b: Two integer
     *return: An integer
     */
    int bitSwapRequired(int a, int b) {
        int count = 0;
        int a_xor_b = a ^ b;
        while (a_xor_b != 0) {
            ++count;
            a_xor_b &= (a_xor_b - 1);
        }

        return count;
    }
};
```

### Java

```java
class Solution {
    /**
     *@param a, b: Two integer
     *return: An integer
     */
    public static int bitSwapRequired(int a, int b) {
        int count = 0;
        int a_xor_b = a ^ b;
        while (a_xor_b != 0) {
            ++count;
            a_xor_b &= (a_xor_b - 1);
        }

        return count;
    }
};
```

### 源码分析

Python 中 int 溢出时会自动变为 long 类型，故处理负数时需要求补数中0的个数，间接求得原异或得到的数中1的个数。

考虑到负数的可能，C/C++, Java 中循环终止条件为`a_xor_b != 0`，而不是`a_xor_b > 0`.

### 复杂度分析

取决于异或后数中1的个数，`O(max(ones in a ^ b))`.

关于 Python 中位运算的一些坑总结在参考链接中。

## Reference

- [BitManipulation - Python Wiki](https://wiki.python.org/moin/BitManipulation)
- [5. Expressions — Python 2.7.10rc0 documentation](https://docs.python.org/2/reference/expressions.html#shifting)
- [Python之位移操作符所带来的困惑 - 旁观者 - 博客园](http://www.cnblogs.com/zhengyun_ustc/archive/2009/10/14/shifting.html)
