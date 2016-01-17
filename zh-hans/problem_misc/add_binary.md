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

## 题解

用字符串模拟二进制的加法，加法操作一般使用自后往前遍历的方法，不同位大小需要补零。

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

### 源码分析

用到的技巧主要有两点，一是两个数位数大小不一时用0补上，二是最后需要判断最高位的进位是否为1。最后需要反转字符串，因为我们是从低位往高位迭代的。虽然可以使用 insert 避免最后的 reverse 操作，但如此一来时间复杂度就从 $$O(n)$$ 变为 $$O(n^2)$$ 了。

### 复杂度分析

遍历两个字符串，时间复杂度 $$O(n)$$. reverse 操作时间复杂度 $$O(n)$$, 故总的时间复杂度 $$O(n)$$. 使用了 StringBuilder 作为临时存储对象，空间复杂度 $$O(n)$$.
