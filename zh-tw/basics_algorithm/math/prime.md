# Prime

質數：恰好有兩個因數的整數，一個是1，另一個則是它自己，比如整數3和5就是質數。質數的基本算法有**素性測試、埃氏篩法和整數分解。**

## 質數測試

如果`d`是`n`的因數，則易知 $$n = d \cdot \frac{n}{d}$$, 因此 `n/d`也是`n`的因數，且這兩個因數中的較小者 $$\min(d, n/d) <= \sqrt{n}$$. 因此我們只需要對前 $$\sqrt{n}$$ 個數進行處理。

## 埃氏篩法 Sieve of Eratosthenes

質數測試針對的是單個整數，如果需要枚舉整數`n`以內的質數就需要埃氏篩法了。核心思想是枚舉從小到大的質數並將質數的整數倍依次從原整數數組中刪除，餘下的即爲全部質數。

## 區間篩法

求區間`[a, b)`內有多少質數？

埃氏篩法得到的是`[1, n)`內的質數，求區間質數時不太容易直接求解，我們採取以退爲進的思路先用埃氏篩法求得`[1, b)`內的質數，然後截取爲`[a, b)`即可。

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
