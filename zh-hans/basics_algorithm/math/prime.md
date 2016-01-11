# Prime

素数：恰好有两个约数的整数，一个是1，另一个则是它自己，比如整数3和5就是素数。素数的基本算法有**素性测试、埃氏筛法和整数分解。**

## 素性测试

如果`d`是`n`的约数，则易知 $$n = d \cdot \frac{n}{d}$$, 因此 `n/d`也是`n`的约数，且这两个约数中的较小者 $$\min(d, n/d) <= \sqrt{n}$$. 因此我们只需要对前 $$\sqrt{n}$$ 个数进行处理。

## 埃氏筛法

素性测试针对的是单个整数，如果需要枚举整数`n`以内的素数就需要埃氏筛法了。核心思想是枚举从小到大的素数并将素数的整数倍依次从原整数数组中删除，余下的即为全部素数。

## 区间筛法

求区间`[a, b)`内有多少素数？

埃氏筛法得到的是`[1, n)`内的素数，求区间素数时不太容易直接求解，我们采取以退为进的思路先用埃氏筛法求得`[1, b)`内的素数，然后截取为`[a, b)`即可。

## Implementation

### Java

```java
import java.util.*;

public class Prime {
    // test if n is prime
    public static boolean isPrime(int n) {
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) return false;
        }
        return n != 1; // 1 is not prime
    }

    // enumerate all the divisor for n
    public static List<Integer> getDivisor(int n) {
        List<Integer> result = new ArrayList<Integer>();
        for (int i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                result.add(i);
                // i * i <= n ==> i <= n / i
                if (i != n / i) result.add(n / i);
            }
        }
        Collections.sort(result);
        return result;
    }

    // 12 = 2 * 2 * 3, the number of prime factor, small to big
    public static Map<Integer, Integer> getPrimeFactor(int n) {
        Map<Integer, Integer> result = new HashMap<Integer, Integer>();
        for (int i = 2; i * i <= n; i++) {
            // if i is a factor of n, repeatedly divide it out
            while (n % i == 0) {
                if (result.containsKey(i)) {
                    result.put(i, result.get(i) + 1);
                } else {
                    result.put(i, 1);
                }
                n = n / i;
            }
        }
        // if n is not 1 at last
        if (n != 1) result.put(n, 1);
        return result;
    }

    // sieve all the prime factor less equal than n
    public static List<Integer> sieve(int n) {
        List<Integer> prime = new ArrayList<Integer>();
        // flag if i is prime
        boolean[] isPrime = new boolean[n + 1];
        Arrays.fill(isPrime, true);
        isPrime[0] = false;
        isPrime[1] = false;
        for (int i = 2; i <= n; i++) {
            if (isPrime[i]) {
                prime.add(i);
                for (int j = 2 * i; j <= n; j += i) {
                    isPrime[j] = false;
                }
            }
        }
        return prime;
    }

    // sieve between [a, b)
    public static List<Integer> sieveSegment(int a, int b) {
        List<Integer> prime = new ArrayList<Integer>();
        boolean[] isPrime = new boolean[b];
        Arrays.fill(isPrime, true);
        isPrime[0] = false;
        isPrime[1] = false;
        for (int i = 2; i < b; i++) {
            if (isPrime(i)) {
                for (int j = 2 * i; j < b; j += i) isPrime[j] = false;
                if (i >= a) prime.add(i);
            }
        }
        return prime;
    }

    public static void main(String[] args) {
        if (args.length == 1) {
            int n = Integer.parseInt(args[0]);
            if (isPrime(n)) {
                System.out.println("Integer " + n + " is prime.");
            } else {
                System.out.println("Integer " + n + " is not prime.");
            }
            System.out.println();

            List<Integer> divisor = getDivisor(n);
            System.out.print("Divisor of integer " + n + ":");
            for (int d : divisor) System.out.print(" " + d);
            System.out.println();
            System.out.println();

            Map<Integer, Integer> primeFactor = getPrimeFactor(n);
            System.out.println("Prime factor of integer " + n + ":");
            for (Map.Entry<Integer, Integer> entry : primeFactor.entrySet()) {
                System.out.println("prime: " + entry.getKey() + ", times: " + entry.getValue());
            }

            System.out.print("Sieve prime of integer " + n + ":");
            List<Integer> sievePrime = sieve(n);
            for (int i : sievePrime) System.out.print(" " + i);
            System.out.println();
        } else if (args.length == 2) {
            int a = Integer.parseInt(args[0]);
            int b = Integer.parseInt(args[1]);
            List<Integer> primeSegment = sieveSegment(a, b);
            System.out.println("Prime of integer " + a + " to " + b + ":");
            for (int i : primeSegment) System.out.print(" " + i);
            System.out.println();
        }
    }
}
```
