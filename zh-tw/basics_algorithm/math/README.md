# Math

本小節總結一些與數學（尤其是數論部分）有關的基礎，主要總結了《挑戰程序設計競賽》(原文為《プログラミングコンテストチャレンジブック》)第二章。主要包含以下內容：

1. Greatest Common Divisor(最大公因數)
2. Prime(質數基礎理論)
3. Modulus(取模運算)
4. Fast Power(快速冪運算)

## Modulus - 取模運算

有時計算結果可能會溢位，此時往往需要對結果取餘。如果有`a % m = c % m` 和 `b % m = d % m`, 那麼有以下模運算成立。

- `(a + b) % m = (c + d) % m`
- `(a - b) % m = (c - d) % m`
- `(a × b) % m = (c × d) % m`

需要注意的是沒有除法運算，另外由於最終結果可能溢位，故需要使用更大範圍的類型來保存取模之前的結果。另外若`a`是負數時往往需要改寫爲 `a % m + m`, 這樣就保證結果在`[0, m - 1]`範圍內了。

## Fast Power - 快速冪運算

快速冪運算的核心思想爲反覆平方法，將冪指數表示爲2的冪次的和，等價於二進制進行移位計算（不斷取冪的最低位），比如 $$x^{22} = x^{16}  x^4  x^2$$.

### C++

```C++
long long fastModPow(lont long x, int n, long long mod) {
    long long res = 1 % mod;
    while(n > 0) {
        //if lowest bit is 1, fast judge of even number
        if((n & 1) != 0)
            res = res * x % mod;
        x = x * x % mod;
        n >>= 1; 
    }
    return res;
}
```

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
