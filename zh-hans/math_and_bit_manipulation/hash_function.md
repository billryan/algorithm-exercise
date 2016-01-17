# Hash Function

## Question

- lintcode: [(128) Hash Function](http://www.lintcode.com/en/problem/hash-function/)

### Problem Statement

In data structure Hash, hash function is used to convert a string(or any other
type) into an integer smaller than hash size and bigger or equal to zero. The
objective of designing a hash function is to "hash" the key as unreasonable as
possible. A good hash function can avoid collision as less as possible. A
widely used hash function algorithm is using a magic number 33, consider any
string as a 33 based big integer like follow:

hashcode("abcd") = (ascii(a) * $$33^3$$ \+ ascii(b) * $$33^2$$ \+ ascii(c) *33 +
ascii(d)) % HASH_SIZE

= (97* $$33^3$$ \+ 98 * $$33^2$$ \+ 99 * 33 +100) % HASH_SIZE

= 3595978 % HASH_SIZE

here HASH_SIZE is the capacity of the hash table (you can assume a hash table
is like an array with index 0 ~ HASH_SIZE-1).

Given a string as a key and the size of hash table, return the hash value of
this key.f

  

#### Example

For key="abcd" and size=100, return 78

#### Clarification

For this problem, you are not necessary to design your own hash algorithm or
consider any collision issue, you just need to implement the algorithm as
described.

## 题解1

基本实现题，大多数人看到题目的直觉是按照定义来递推不就得了嘛，但其实这里面大有玄机，因为在字符串较长时使用 long 型来计算33的幂会溢出！所以这道题的关键在于如何处理**大整数溢出**。对于整数求模，`(a * b) % m = a % m * b % m` 这个基本公式务必牢记。根据这个公式我们可以大大降低时间复杂度和规避溢出。

### Java

```java
class Solution {
    /**
     * @param key: A String you should hash
     * @param HASH_SIZE: An integer
     * @return an integer
     */
    public int hashCode(char[] key,int HASH_SIZE) {
        if (key == null || key.length == 0) return -1;

        long hashSum = 0;
        for (int i = 0; i < key.length; i++) {
            hashSum += key[i] * modPow(33, key.length - i - 1, HASH_SIZE);
            hashSum %= HASH_SIZE;
        }

        return (int)hashSum;
    }

    private long modPow(int base, int n, int mod) {
        if (n == 0) {
            return 1;
        } else if (n == 1) {
            return base % mod;
        } else if (n % 2 == 0) {
            long temp = modPow(base, n / 2, mod);
            return (temp % mod) * (temp % mod) % mod;
        } else {
            return (base % mod) * modPow(base, n - 1, mod) % mod;
        }
    }
}
```

### 源码分析

题解1属于较为直观的解法，只不过在计算33的幂时使用了私有方法`modPow`, 这个方法使用了对数级别复杂度的算法，可防止 TLE 的产生。注意两个 int 型数据在相乘时可能会溢出，故对中间结果的存储需要使用 long.

### 复杂度分析

遍历加求`modPow`，时间复杂度 $$O(n \log n)$$, 空间复杂度 $$O(1)$$. 当然也可以使用哈希表的方法将幂求模的结果保存起来，这样一来空间复杂度就是 $$O(n)$$, 不过时间复杂度为 $$O(n)$$.

## 题解2 - 巧用求模公式

从题解1中我们可以看到其时间复杂度还是比较高的，作为基本库来使用是比较低效的。我们从范例`hashcode("abc")`为例进行说明。

$$
\begin{array}{cl}
hashcode(abc) & = & (a \times 33^{2} + b \times 33 + c)\% M\\
 & = & (33(33\times a+b)+c)\% M\\
 & = & (33(33(33\times0+a)+b)+c)\% M
\end{array}
$$

再根据 $$(a \times b) \% M = (a \% M) \times (b \% M)$$

从中可以看出使用迭代的方法较容易实现。

### Java

```java
class Solution {
    /**
     * @param key: A String you should hash
     * @param HASH_SIZE: An integer
     * @return an integer
     */
    public int hashCode(char[] key,int HASH_SIZE) {
        if (key == null || key.length == 0) return -1;

        long hashSum = 0;
        for (int i = 0; i < key.length; i++) {
            hashSum = 33 * hashSum + key[i];
            hashSum %= HASH_SIZE;
        }

        return (int)hashSum;
    }
}
```

### 源码分析

精华在`hashSum = 33 * hashSum + key[i];`

### 复杂度分析

时间复杂度 $$O(n)$$, 空间复杂度 $$O(1)$$.
