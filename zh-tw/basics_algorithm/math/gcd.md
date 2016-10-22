# Math

本小節總結一些與數學（尤其是數論部分）有關的基礎，主要總結了《挑戰程序設計競賽》第二章。

## 最大公因數(GCD, Greatest Common Divisor)

常用的方法爲輾轉相除法，也稱爲歐幾里得算法。不妨設函數`gcd(a, b)`是自然是`a`, `b`的最大公因數，不妨設`a > b`, 則有 $$a = b \times p + q$$, 那麼對於`gcd(b, q)`則是`b`和`q`的最大公因數，也就是說`gcd(b, q)`既能整除`b`, 又能整除`a`(因爲 $$a = b \times p + q$$, `p`是整數)，如此反覆最後得到`gcd(a, b) = gcd(c, 0)`, 第二個數爲0時直接返回`c`. 如果最開始`a < b`, 那麼`gcd(b, a % b) = gcd(b, a) = gcd(a, b % a)`.

關於時間複雜度的證明：可以分`a > b/2`和`a < b/2`證明，對數級別的時間複雜度，過程略。

與最大公因數相關的還有最小公倍數(LCM, Lowest Common Multiple), 它們兩者之間的關係爲 $$ lcm(a, b) \times gcd(a, b) = |ab|$$.

### Java

```java
public static long gcd(long a, long b) {
    return (b == 0) ? a : gcd(b, a % b);
}
```

### Problem

給定平面上兩個座標 P1=(x1, y1), P2=(x2,y2), 問線段 P1P2 上除 P1, P2以外還有幾個整數座標點？

#### Solution

問的是線段 P1P2, 故除 P1,P2以外的座標需在 x1,x2,y1,y2範圍之內，且不包含端點。在兩端點不重合的前提下有：

$$
\frac{y-y_1}{x-x_1}=\frac{y_2 - y_1}{x_2 - x_1}
$$
那麼若得知 $$M = gcd(x_2 - x_1, y_2 - y_1)$$, 則有 $$x - x_1$$ 必爲 $$x_2 - x_1 / M$$ 的整數倍大小，又因爲 $$ x_1 < x < x_2$$, 故最多有 $$M - 1$$個整數座標點。

## 擴展歐幾里得算法

求解整係數 $$x$$ 和 $$y$$ 滿足 $$d = gcd(a, b) = ax + by$$, 仿照歐幾里得算法，應該要尋找 $$gcd(b, a \% b) = bx^\prime + (a \% b)y^\prime$$.

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

求整數 $$x$$ 和 $$y$$ 使得 $$ax+by=1$$.

#### Solution

不妨設`gcd(a, b) = M`, 那麼有 $$M(a^\prime x+b^\prime y)=1$$ ==> $$a^\prime x+b^\prime y=1/M$$ 如果 M 大於1，由於等式左邊爲整數，故等式不成立，所以要想題中等式有解，必有`gcd(a, b) = 1`.

**擴展提：題中等式右邊爲1，假如爲2又會怎樣？**

提示：此時$$c = k \cdot gcd(a, b), x^\prime = k\cdot x ==> c\ \%\ gcd(a, b) == 0$$, c 爲等式右邊的正整數值。詳細推導見 [How to find solutions of linear Diophantine ax + by = c?](http://math.stackexchange.com/questions/20717/how-to-find-solutions-of-linear-diophantine-ax-by-c)
