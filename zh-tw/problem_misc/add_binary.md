# Add Binary

## Question

- leetcode: [Add Binary | LeetCode OJ](https://leetcode.com/problems/add-binary/)
- lintcode: [(408) Add Binary](http://www.lintcode.com/en/problem/add-binary/)

```
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".
```

## 題解

用字串模擬二進制的加法，加法操作一般使用自後往前遍歷的方法，不同位大小需要補零。

### Java

```java
public class Solution {
    /**
     * @param a a number
     * @param b a number
     * @return the result
     */
    public String addBinary(String a, String b) {
        if (a == null || a.length() == 0) return b;
        if (b == null || b.length() == 0) return a;

        StringBuilder sb = new StringBuilder();
        int aLen = a.length(), bLen = b.length();

        int carry = 0;
        for (int ia = aLen - 1, ib = bLen - 1; ia >= 0 || ib >= 0; ia--, ib--) {
            // replace with 0 if processed
            int aNum = (ia < 0) ? 0 : a.charAt(ia) - '0';
            int bNum = (ib < 0) ? 0 : b.charAt(ib) - '0';

            int num = (aNum + bNum + carry) % 2;
            carry = (aNum + bNum + carry) / 2;
            sb.append(num);
        }
        if (carry == 1) sb.append(1);

        // important!
        sb.reverse();
        String result = sb.toString();
        return result;
    }
}
```

### 源碼分析

用到的技巧主要有兩點，一是兩個數位數大小不一時用0補上，二是最後需要判斷最高位的進位是否為1。最後需要反轉字符串，因為我們是從低位往高位迭代的。雖然可以使用 insert 避免最後的 reverse 操作，但如此一來時間複雜度就從 $$O(n)$$ 變為 $$O(n^2)$$ 了。

### C++
``` c++
class Solution {
public:
    // helper functions
    char XOR(char x, char y) {
        return x == y ? '0' : '1';
    }
    char CARRY(char x, char y){
        return (x == '1' and y == '1') ? '1' : '0';
    }
    string addBinary(string a, string b) {
        if(a.size() < b.size())
            swap(a,b);
            
        int i = a.size()-1;
        int j = b.size()-1;
        char carry ='0';
        
        while(0 <= i) {
            char tmp = a[i];
            a[i] = XOR(tmp, carry);
            carry = CARRY(tmp, carry);
            if(0 <= j) {
                tmp = a[i];
                a[i] = XOR(tmp, b[j]);
                carry = XOR(carry, CARRY(tmp, b[j]));
            }
            i--; j--;
        }
    
        if(carry == '1')
            a = "1" + a;
        return a;
    }
};
```

###源碼分析
C++的解法採用了直接操作char的作法，模擬硬體半加器(half adder)的行為，先確保a的長度不小於b的長度後，下標從尾到頭逐位相加，小心處理進位即可。

### 複雜度分析

Java解法遍歷兩個字串，時間複雜度 $$O(n)$$. reverse 操作時間複雜度 $$O(n)$$, 故總的時間複雜度 $$O(n)$$. 使用了 StringBuilder 作為臨時存儲對象，空間複雜度 $$O(n)$$.

C++解法時間複雜度也是$$O(n)$$，計算過程中使用的臨時變數，額外空間複雜度是$$O(1)$$，實際整體空間複雜度則取決於最後我們要將答案擴張一位時，函數的實現方法，最差可能達到$$O(n)$$。
