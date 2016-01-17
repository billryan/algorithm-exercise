# Plus One

## Question

- leetcode: [Plus One | LeetCode OJ](https://leetcode.com/problems/plus-one/)
- lintcode: [(407) Plus One](http://www.lintcode.com/en/problem/plus-one/)

### Problem Statement

Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.

#### Example

Given [1,2,3] which represents 123, return [1,2,4].

Given [9,9,9] which represents 999, return [1,0,0,0].

## 题解

又是一道两个整数按数位相加的题，自后往前累加，处理下进位即可。这道题中是加1，其实还可以扩展至加2，加3等。

### C++
```c++
class Solution {
public:
    /**
     * @param digits a number represented as an array of digits
     * @return the result
     */
    vector<int> plusOne(vector<int>& digits) {
        return plusN(digits, 1);
    }
    
    vector<int> plusN(vector<int>& digits, int n) {
        vector<int> result;
        int carry = n;
        for (int i = digits.size() - 1; i >= 0; i--) {
            result.insert(result.begin(), (digits[i] + carry) % 10);
            carry = (digits[i] + carry) / 10;
        }
        if (carry) result.insert(result.begin(), carry);
        return result;
    }
};
```

### Java

```java
public class Solution {
    /**
     * @param digits a number represented as an array of digits
     * @return the result
     */
    public int[] plusOne(int[] digits) {
        return plusDigit(digits, 1);
    }

    private int[] plusDigit(int[] digits, int digit) {
        if (digits == null || digits.length == 0) return null;

        // regard digit(0~9) as carry
        int carry = digit;
        int[] result = new int[digits.length];
        for (int i = digits.length - 1; i >= 0; i--) {
            result[i] = (digits[i] + carry) % 10;
            carry = (digits[i] + carry) / 10;
        }

        // carry == 1
        if (carry == 1) {
            int[] finalResult = new int[result.length + 1];
            finalResult[0] = 1;
            return finalResult;
        }

        return result;
    }
}
```

### 源码分析

源码中单独实现了加任何数(0~9)的私有方法，更为通用，对于末尾第一个数，可以将要加的数当做进位处理，这样就不必单独区分最后一位了，十分优雅！

### 复杂度分析

Java 中需要返回数组，而这个数组在处理之前是不知道大小的，故需要对最后一个进位单独处理。时间复杂度 $$O(n)$$, 空间复杂度在最后一位有进位时恶化为 $$O(n)$$, 当然也可以通过两次循环使得空间复杂度为 $$O(1)$$.

## Reference

- Soulmachine 的 leetcode 题解，将要加的数当做进位处理就是从这学到的。
