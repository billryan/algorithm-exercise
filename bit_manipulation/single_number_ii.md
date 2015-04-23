# Single Number II


## Source

- lintcode: [(83) Single Number II](http://www.lintcode.com/en/problem/single-number-ii/)


```
Given 3*n + 1 numbers, every numbers occurs triple times except one, find it.

Example
Given [1,1,2,3,3,3,2,2,4,1] return 4

Challenge
One-pass, constant exstra space
```

### 题解 - 逐位处理

上题 Single Number 用到了二进制中异或的运算特性，这题给出的元素数目为`3*n + 1`，因此我们很自然地想到如果有种运算能满足「三三运算」为0该有多好！对于三个相同的数来说，其相加的和必然是3的倍数，仅仅使用这一个特性还不足以将单数找出来，我们再来挖掘隐含的信息。以3为例，若使用不进位加法，三个3相加的结果为：

```
0011
0011
0011
----
0033
```
注意到其中的奥义了么？三个相同的数相加，不仅其和能被3整除，其二进制位上的每一位也能被3整除！因此我们只需要一个和`int`类型相同大小的数组记录每一位累加的结果即可。时间复杂度约为 $$O((3n+1)\cdot sizeof(int) \cdot 8)$$

#### C++ bit by bit

```c++
class Solution {
public:
	/**
	 * @param A : An integer array
	 * @return : An integer
	 */
    int singleNumberII(vector<int> &A) {
        if (A.empty()) {
            return 0;
        }

        int result = 0, bit_i_sum = 0;

        for (int i = 0; i != 8 * sizeof(int); ++i) {
            bit_i_sum = 0;
            for (int j = 0; j != A.size(); ++j) {
                // get the *i*th bit of A
                bit_i_sum += ((A[j] >> i) & 1);
            }
            // set the *i*th bit of result
            result |= ((bit_i_sum % 3) << i);
        }

        return result;
    }
};
```

#### 源码解析

1. 异常处理
2. 循环处理返回结果`result`的`int`类型的每一位，要么自增1，要么保持原值。注意`i`最大可取 $$8 \cdot sizeof(int) - 1$$, 字节数=>位数的转换
3. 对第`i`位处理完的结果模3后更新`result`的第`i`位，由于`result`初始化为0，故使用或操作即可完成

## Reference

[Single Number II - Leetcode Discuss](https://leetcode.com/discuss/857/constant-space-solution?show=2542) 中抛出了这么一道扩展题：

```
Given an array of integers, every element appears k times except for one. Find that single one which appears l times.
```

@ranmocy 给出了如下经典解：

We need a array `x[i]` with size `k` for saving the bits appears `i` times. For every input number a, generate the new counter by `x[j] = (x[j-1] & a) | (x[j] & ~a)`. Except `x[0] = (x[k] & a) | (x[0] & ~a)`.

In the equation, the first part indicates the the carries from previous one. The second part indicates the bits not carried to next one.

Then the algorithms run in `O(kn)` and the extra space `O(k)`.

#### Java

```java
public class Solution {
    public int singleNumber(int[] A, int k, int l) {
        if (A == null) return 0;
        int t;
        int[] x = new int[k];
        x[0] = ~0;
        for (int i = 0; i < A.length; i++) {
            t = x[k-1];
            for (int j = k-1; j > 0; j--) {
                x[j] = (x[j-1] & A[i]) | (x[j] & ~A[i]);
            }
            x[0] = (t & A[i]) | (x[0] & ~A[i]);
        }
        return x[l];
    }
}
```
