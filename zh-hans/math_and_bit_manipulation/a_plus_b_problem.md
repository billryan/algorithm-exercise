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

## 题解

不用加减法实现加法，类似数字电路中的全加器，异或求得部分和，相与求得进位，最后将进位作为加法器的输入，典型的递归实现思路。

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

### 源码分析

递归步为进位是否为0，为0时返回。

### 复杂度分析

取决于进位，近似为 $$O(1)$$. 使用了部分额外变量，空间复杂度为 $$O(1)$$.
