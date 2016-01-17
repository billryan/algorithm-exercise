# Fast Power

## Question

- lintcode: [(140) Fast Power](http://www.lintcode.com/en/problem/fast-power/)

## 题解

数学题，考察整数求模的一些特性，不知道这个特性的话此题一时半会解不出来，本题中利用的关键特性为：

```
(a * b) % p = ((a % p) * (b % p)) % p
```

即 a 与 b 的乘积模 p 的值等于 a, b 分别模 p 相乘后再模 p 的值，只能帮你到这儿了，不看以下的答案先想想知道此关系后如何解这道题。

首先不太可能先把 $$a^n$$ 具体值求出来，太大了... 所以利用以上求模公式，可以改写 $$a^n$$ 为：

$$a^n = a^{n/2} \cdot a^{n/2} = a^{n/4} \cdot a^{n/4} \cdot a^{n/4} \cdot a^{n/4} \cdot = ...$$

至此递归模型建立。

### Python

```python
class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """
    def fastPower(self, a, b, n):
        if n == 1:
            return a % b
        elif n == 0:
            # do not use `1` instead `1 % b` because `b = 1`
            return 1 % b
        elif n < 0:
            return -1

        # (a * b) % p = ((a % p) * (b % p)) % p
        product = self.fastPower(a, b, n / 2)
        product = (product * product) % b
        if n % 2 == 1:
            product = (product * a) % b

        return product
```

### C++

```c++
class Solution {
public:
    /*
     * @param a, b, n: 32bit integers
     * @return: An integer
     */
    int fastPower(int a, int b, int n) {
        if (1 == n) {
            return a % b;
        } else if (0 == n) {
            // do not use 1 instead (1 % b)! b = 1
            return 1 % b;
        } else if (0 > n) {
            return -1;
        }

        // (a * b) % p = ((a % p) * (b % p)) % p
        // use long long to prevent overflow
        long long product = fastPower(a, b, n / 2);
        product = (product * product) % b;
        if (1 == n % 2) {
            product = (product * a) % b;
        }

        // cast long long to int
        return (int) product;
    }
};
```

### Java

```java
class Solution {
    /*
     * @param a, b, n: 32bit integers
     * @return: An integer
     */
    public int fastPower(int a, int b, int n) {
        if (n == 1) {
            return a % b;
        } else if (n == 0) {
            return 1 % b;
        } else if (n < 0) {
            return -1;
        }

        // (a * b) % p = ((a % p) * (b % p)) % p
        // use long to prevent overflow
        long product = fastPower(a, b, n / 2);
        product = (product * product) % b;
        if (n % 2 == 1) {
            product = (product * a) % b;
        }

        // cast long to int
        return (int) product;
    }
};
```

### 源码分析

分三种情况讨论 n 的值，需要特别注意的是`n == 0`，虽然此时 $$a^0$$ 的值为1，但是不可直接返回1，因为`b == 1`时应该返回0，故稳妥的写法为返回`1 % b`.

递归模型中，需要注意的是要分 n 是奇数还是偶数，奇数的话需要多乘一个 a, 保存乘积值时需要使用`long`型防止溢出，最后返回时强制转换回`int`。

### 复杂度分析

使用了临时变量`product`，空间复杂度为 $$O(1)$$, 递归层数约为 $$\log n$$, 时间复杂度为 $$O(\log n)$$, 栈空间复杂度也为 $$O(\log n)$$.

## Reference

- [Lintcode: Fast Power 解题报告 - Yu's Garden - 博客园](http://www.cnblogs.com/yuzhangcmu/p/4174781.html)
- [Fast Power 参考程序 Java/C++/Python](http://www.jiuzhang.com/solutions/fast-power/)
