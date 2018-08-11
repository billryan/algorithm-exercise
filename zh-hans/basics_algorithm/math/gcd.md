# Math

本小节总结一些与数学（尤其是数论部分）有关的基础，主要总结了《挑战程序设计竞赛》第二章。

## 最大公约数(GCD, Greatest Common Divisor)

常用的方法为辗转相除法，也称为欧几里得算法。不妨设函数`gcd(a, b)`是自然数`a`, `b`的最大公约数，不妨设`a > b`, 则有 $$a = b \times p + q$$, 那么对于`gcd(b, q)`则是`b`和`q`的最大公约数，也就是说`gcd(b, q)`既能整除`b`, 又能整除`a`(因为 $$a = b \times p + q$$, `p`是整数)，如此反复最后得到`gcd(a, b) = gcd(c, 0)`, 第二个数为0时直接返回`c`. 如果最开始`a < b`, 那么`gcd(b, a % b) = gcd(b, a) = gcd(a, b % a)`.

关于时间复杂度的证明：可以分`a > b/2`和`a < b/2`证明，对数级别的时间复杂度，过程略。

与最大公约数相关的还有最小公倍数(LCM, Lowest Common Multiple), 它们两者之间的关系为 $$ lcm(a, b) \times gcd(a, b) = |ab|$$.

### Java

```java
public static long gcd(long a, long b) {
    return (b == 0) ? a : gcd(b, a % b);
}
```

### Problem

给定平面上两个坐标 P1=(x1, y1), P2=(x2,y2), 问线段 P1P2 上除 P1, P2以外还有几个整数坐标点？

#### Solution

问的是线段 P1P2, 故除 P1,P2以外的坐标需在 x1,x2,y1,y2范围之内，且不包含端点。在两端点不重合的前提下有：

$$
\frac{y-y_1}{x-x_1}=\frac{y_2 - y_1}{x_2 - x_1}
$$
那么若得知 $$M = gcd(x_2 - x_1, y_2 - y_1)$$, 则有 $$x - x_1$$ 必为 $$x_2 - x_1 / M$$ 的整数倍大小，又因为 $$ x_1 < x < x_2$$, 故最多有 $$M - 1$$个整数坐标点。

## 扩展欧几里得算法

求解整系数 $$x$$ 和 $$y$$ 满足 $$d = gcd(a, b) = ax + by$$, 仿照欧几里得算法，应该要寻找 $$gcd(b, a \% b) = bx^\prime + (a \% b)y^\prime$$.

### Java

```java
public class Solution {
    public static int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    public static int[] gcdExt(int a, int b) {
        if (b == 0) {
            return new int[] {a, 1, 0};
        } else {
            int[] vals = gcdExt(b, a % b);
            int d = vals[0];
            int x = vals[2];
            int y = vals[1];
            y -= (a / b) * x;
            return new int[] {d, x, y};
        }
    }

    public static void main(String[] args) {
        int a = 4, b = 11;
        int[] result = gcdExt(a, b);
        System.out.printf("d = %d, x = %d, y = %d.\n", result[0], result[1], result[2]);
    }
}
```

### Problem

求整数 $$x$$ 和 $$y$$ 使得 $$ax+by=1$$.

#### Solution

不妨设`gcd(a, b) = M`, 那么有 $$M(a^\prime x+b^\prime y)=1$$ ==> $$a^\prime x+b^\prime y=1/M$$ 如果 M 大于1，由于等式左边为整数，故等式不成立，所以要想题中等式有解，必有`gcd(a, b) = 1`.

**扩展提：题中等式右边为1，假如为2又会怎样？**

提示：此时$$c = k \cdot gcd(a, b), x^\prime = k\cdot x ==> c\ \%\ gcd(a, b) == 0$$, c 为等式右边的正整数值。详细推导见 [How to find solutions of linear Diophantine ax + by = c?](http://math.stackexchange.com/questions/20717/how-to-find-solutions-of-linear-diophantine-ax-by-c)
