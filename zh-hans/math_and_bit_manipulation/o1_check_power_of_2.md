# O(1) Check Power of 2

## Question

- lintcode: [(142) O(1) Check Power of 2](http://www.lintcode.com/en/problem/o1-check-power-of-2/)

```
Using O(1) time to check whether an integer n is a power of 2.

Example
For n=4, return true;

For n=5, return false;

Challenge
O(1) time
```

## 题解

咋看起来挺简单的一道题目，可之前若是没有接触过神奇的位运算技巧遇到这种题就有点不知从哪入手了，咳咳，我第一次接触到这个题就是在七牛的笔试题中看到的，泪奔 :-(

简单点来考虑可以连除2求余，看最后的余数是否为1，但是这种方法无法在 $$O(1)$$ 的时间内解出，所以我们必须要想点别的办法了。2的整数幂若用二进制来表示，则其中必只有一个1，其余全是0，那么怎么才能用一个式子把这种特殊的关系表示出来了？传统的位运算如按位与、按位或和按位异或等均无法直接求解，我就不卖关子了，比较下`x - 1`和`x`的关系试试？以`x=4`为例。

```
0100 ==> 4
0011 ==> 3
```

两个数进行按位与就为0了！如果不是2的整数幂则无上述关系，反证法可证之。

### Python

```python
class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        if n < 1:
            return False
        else:
            return (n & (n - 1)) == 0
```

### C++

```c++
class Solution {
public:
    /*
     * @param n: An integer
     * @return: True or false
     */
    bool checkPowerOf2(int n) {
        if (1 > n) {
            return false;
        } else {
            return 0 == (n & (n - 1));
        }
    }
};
```

### Java

```java
class Solution {
    /*
     * @param n: An integer
     * @return: True or false
     */
    public boolean checkPowerOf2(int n) {
        if (n < 1) {
            return false;
        } else {
            return (n & (n - 1)) == 0;
        }
    }
};
```

### 源码分析

除了考虑正整数之外，其他边界条件如小于等于0的整数也应考虑在内。在比较0和`(n & (n - 1))`的值时，需要用括号括起来避免优先级结合的问题。

### 复杂度分析

$$O(1)$$.

## 扩展

关于2的整数幂还有一道有意思的题，比如 [Next Power of 2 - GeeksforGeeks](http://www.geeksforgeeks.org/next-power-of-2/)，有兴趣的可以去围观下。
