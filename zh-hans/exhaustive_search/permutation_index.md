# Permutation Index

## Question

- lintcode: [(197) Permutation Index](http://www.lintcode.com/en/problem/permutation-index/)

### Problem Statement

Given a permutation which contains no repeated number, find its index in all
the permutations of these numbers, which are ordered in lexicographical order.
The index begins at 1.

#### Example

Given [1,2,4], return 1.

## 题解

做过 next permutation 系列题的话自然能想到不断迭代直至最后一个，最后返回计数器的值即可。这种方法理论上自然是可行的，但是最坏情况下时间复杂度为 $$O(n!)$$, 显然是不能接受的。由于这道题只是列出某给定 permutation 的相对顺序(index), 故我们可从 permutation 的特点出发进行分析。

以序列`1, 2, 4`为例，其不同的排列共有 `3!=6` 种，以排列`[2, 4, 1]`为例，若将1置于排列的第一位，后面的排列则有 `2!=2` 种。将2置于排列的第一位，由于`[2, 4, 1]`的第二位4在1, 2, 4中为第3大数，故第二位可置1或者2，那么相应的排列共有 `2 * 1! = 2`种，最后一位1为最小的数，故比其小的排列为0。综上，可参考我们常用的十进制和二进制的转换，对于`[2, 4, 1]`, 可总结出其排列的`index`为`2! * (2 - 1) + 1! * (3 - 1) + 0! * (1 - 1) + 1`.

以上分析看似正确无误，实则有个关键的漏洞，在排定第一个数2后，第二位数只可为1或者4，而无法为2, **故在计算最终的 index 时需要动态计算某个数的相对大小。**按照从低位到高位进行计算，我们可通过两重循环得出到某个索引处值的相对大小。

### Python

```python
class Solution:
    # @param {int[]} A an integer array
    # @return {long} a long integer
    def permutationIndex(self, A):
        if A is None or len(A) == 0:
            return 0

        index = 1
        factor = 1
        for i in xrange(len(A) - 1, -1, -1):
            rank = 0
            for j in xrange(i + 1, len(A)):
                if A[i] > A[j]:
                    rank += 1

            index += rank * factor
            factor *= (len(A) - i)

        return index
```

### C++

```c++
class Solution {
public:
    /**
     * @param A an integer array
     * @return a long integer
     */
    long long permutationIndex(vector<int>& A) {
        if (A.empty()) return 0;

        long long index = 1;
        long long factor = 1;
        for (int i = A.size() - 1; i >= 0; --i) {
            int rank = 0;
            for (int j = i + 1; j < A.size(); ++j) {
                if (A[i] > A[j]) ++rank;
            }
            index += rank * factor;
            factor *= (A.size() - i);
        }

        return index;
    }
};
```

### Java

```java
public class Solution {
    /**
     * @param A an integer array
     * @return a long integer
     */
    public long permutationIndex(int[] A) {
        if (A == null || A.length == 0) return 0L;

        long index = 1, fact = 1;
        for (int i = A.length - 1; i >= 0; i--) {
            // get rank in every iteration
            int rank = 0;
            for (int j = i + 1; j < A.length; j++) {
                if (A[i] > A[j]) rank++;
            }

            index += rank * fact;
            fact *= (A.length - i);
        }

        return index;
    }
}
```

### 源码分析

注意 index 和 factor 的初始值，rank 的值每次计算时都需要重新置零，index 先自增，factorial 后自乘求阶乘。

### 复杂度分析

双重 for 循环，时间复杂度为 $$O(n^2)$$. 使用了部分额外空间，空间复杂度 $$O(1)$$.

## Reference

- [Permutation Index](http://www.geekviewpoint.com/java/numbers/permutation_index)
