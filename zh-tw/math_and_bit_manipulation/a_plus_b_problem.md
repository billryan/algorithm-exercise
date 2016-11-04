# A plus B Problem

## Question

- lintcode: [(1) A + B Problem](http://www.lintcode.com/en/problem/a-b-problem/)

```
Write a function that add two numbers A and B.
You should not use + or any arithmetic operators.


Example
Given a=1 and b=2 return 3

Note
There is no need to read data from standard input stream.
Both parameters are given in function aplusb,
you job is to calculate the sum and return it.
Challenge
Of course you can just return a + b to get accepted.
But Can you challenge not do it like that?
Clarification
Are a and b both 32-bit integers?
Yes.
Can I use bit operation?

Sure you can.
```

## 題解

不用加減法實現加法，類似數字電路中的全加器 (Full Adder)，XOR 求得部分和，OR 求得進位，最後將進位作爲加法器的輸入，典型的遞迴實現思路。

### Java

```java
class Solution {
    /*
     * param a: The first integer
     * param b: The second integer
     * return: The sum of a and b
     */
    public int aplusb(int a, int b) {
        int result = a ^ b;
        int carry = a & b;
        carry <<= 1;
        if (carry != 0) {
            result = aplusb(result, carry);
        }

        return result;
    }
}
```

### 源碼分析

遞迴步爲進位是否爲0，爲0時返回。

### 複雜度分析

取決於進位，近似爲 $$O(1)$$. 使用了部分額外變量，空間複雜度爲 $$O(1)$$.
