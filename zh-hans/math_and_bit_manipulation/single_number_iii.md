# Single Number III

## Question

- lintcode: [(84) Single Number III](http://www.lintcode.com/en/problem/single-number-iii/)

```
Given 2*n + 2 numbers, every numbers occurs twice except two, find them.

Example
Given [1,2,2,3,4,4,5,3] return 1 and 5

Challenge
O(n) time, O(1) extra space.
```

## 题解

题 [Single Number](http://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/single_number.html) 的 follow up, 不妨设最后两个只出现一次的数分别为 `x1, x2`. 那么遍历数组时根据两两异或的方法可得最后的结果为 `x1 ^ x2`, 如果我们要分别求得 `x1` 和 `x2`, 我们可以根据 `x1 ^ x2 ^ x1 = x2` 求得 `x2`, 同理可得 `x_1`. 那么问题来了，如何得到`x1`和`x2`呢？看起来似乎是个死循环。大多数人一般也就能想到这一步(比如我...)。

这道题的巧妙之处在于利用`x1 ^ x2`的结果对原数组进行了分组，进而将`x1`和`x2`分开了。具体方法则是利用了`x1 ^ x2`不为0的特性，如果`x1 ^ x2`不为0，那么`x1 ^ x2`的结果必然存在某一二进制位不为0（即为1），我们不妨将最低位的1提取出来，由于在这一二进制位上`x1`和`x2`必然相异，即`x1`, `x2`中相应位一个为0，另一个为1，所以我们可以利用这个最低位的1将`x1`和`x2`分开。又由于除了`x1`和`x2`之外其他数都是成对出现，故与最低位的1异或时一定会抵消，十分之精妙！

### Java

```java
public class Solution {
    /**
     * @param A : An integer array
     * @return : Two integers
     */
    public List<Integer> singleNumberIII(int[] A) {
        ArrayList<Integer> nums = new ArrayList<Integer>();
        if (A == null || A.length == 0) return nums;

        int x1xorx2 = 0;
        for (int i : A) {
            x1xorx2 ^= i;
        }

        // get the last 1 bit of x1xorx2, e.g. 1010 ==> 0010
        int last1Bit = x1xorx2 - (x1xorx2 & (x1xorx2 - 1));
        int single1 = 0, single2 = 0;
        for (int i : A) {
            if ((last1Bit & i) == 0) {
                single1 ^= i;
            } else {
                single2 ^= i;
            }
        }

        nums.add(single1);
        nums.add(single2);
        return nums;
    }
}
```

### 源码分析

求一个数二进制位1的最低位方法为 `x1xorx2 - (x1xorx2 & (x1xorx2 - 1))`, 其他位运算的总结可参考 [Bit Manipulation](http://algorithm.yuanbin.me/zh-hans/basics_misc/bit_manipulation.html)。利用`last1Bit`可将数组的数分为两组，一组是相应位为0，另一组是相应位为1.

### 复杂度分析

两次遍历数组，时间复杂度 $$O(n)$$, 使用了部分额外空间，空间复杂度 $$O(1)$$.

## Reference

- [Single Number III 参考程序 Java/C++/Python](http://www.jiuzhang.com/solutions/single-number-iii/)
