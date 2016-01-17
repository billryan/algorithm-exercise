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

## 題解

又是一道兩個整數按數位相加的題，自後往前累加，處理下進位即可。這道題中是加1，其實還可以擴展至加2，加3等。

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
### C++
```C
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int carry = 1;
        for(int i = digits.size() - 1; i >= 0; i--){
            digits[i] += carry;
            carry = digits[i] / 10;
            digits[i] %= 10;
        }
        
        if(carry == 1){
            digits.insert(digits.begin(), 1);
        }
        return digits;
    }
};
```

### 源碼分析

源碼中單獨實現了加任何數(0~9)的私有方法，更為通用，對於末尾第一個數，可以將要加的數當做進位處理，這樣就不必單獨區分最後一位了，十分優雅！

### 複雜度分析

Java 中需要返回數組，而這個數組在處理之前是不知道大小的，故需要對最後一個進位單獨處理。時間複雜度 $$O(n)$$, 空間複雜度在最後一位有進位時惡化為 $$O(n)$$, 當然也可以通過兩次循環使得空間複雜度為 $$O(1)$$.

## Reference

- Soulmachine 的 leetcode 題解，將要加的數當做進位處理就是從這學到的。
