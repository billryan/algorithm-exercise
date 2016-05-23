# Math

本小节总结一些与数学（尤其是数论部分）有关的基础，主要总结了《挑战程序设计竞赛》第二章。主要包含以下内容：

1. Greatest Common Divisor(最大公约数)
2. Prime(素数基础理论)
3. Modulus(求模运算)
4. Fast Power(快速幂运算)

## Modulus - 求模运算

有时计算结果可能会溢出，此时往往需要对结果取余。如果有`a % m = c % m` 和 `b % m = d % m`, 那么有以下模运算成立。

- `(a + b) % m = (c + d) % m`
- `(a - b) % m = (c - d) % m`
- `(a × b) % m = (c × d) % m`

需要注意的是没有除法运算，另外由于最终结果可能溢出，故需要使用更大范围的类型来保存求模之前的结果。另外若`a`是负数时往往需要改写为 `a % m + m`, 这样就保证结果在`[0, m - 1]`范围内了。

## Fast Power - 快速幂运算

快速幂运算的核心思想为反复平方法，将幂指数表示为2的幂次的和，等价于二进制进行移位计算（不断取幂的最低位），比如 $$x^{22} = x^{16}  x^4  x^2$$.

### Java

```java
import java.util.*;

public class FastPow {
    public static long fastModPow(long x, long n, long mod) {
        long res = 1 % mod;
        while (n > 0) {
            // if lowest bit is 1
            if ((n & 1) != 0) res = res * x % mod;
            x = x * x % mod;
            n >>= 1;
        }
        return res;
    }

    public static void main(String[] args) {
        if (args.length != 2 && args.length != 3) return;

        long x = Long.parseLong(args[0]);
        long n = Long.parseLong(args[1]);
        long mod = Long.MAX_VALUE;
        if (args.length == 3) {
            mod = Long.parseLong(args[2]);
        }
        System.out.println(fastModPow(x, n, mod));
    }
}
```
