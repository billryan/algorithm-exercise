# Permutation Sequence

## Question

- leetcode: [Permutation Sequence | LeetCode OJ](https://leetcode.com/problems/permutation-sequence/)
- lintcode: [(388) Permutation Sequence](http://www.lintcode.com/en/problem/permutation-sequence/)

### Problem Statement

Given _n_ and _k_, return the _k_-th permutation sequence.

#### Example

For `n = 3`, all permutations are listed as follows:



    "123"
    "132"
    "213"
    "231"
    "312"
    "321"


If `k = 4`, the fourth permutation is `"231"`

#### Note

_n_ will be between 1 and 9 inclusive.

#### Challenge

O(n*k) in time complexity is easy, can you do it in O(n^2) or less?


## 题解

和题 [Permutation Index](http://algorithm.yuanbin.me/zh-hans/exhaustive_search/permutation_index.html) 正好相反，这里给定第几个排列的相对排名，输出排列值。和不同进制之间的转化类似，这里的『进制』为`1!, 2!...`, 以n=3, k=4为例，我们从高位到低位转化，直觉应该是用 `k/(n-1)!`, 但以 n=3,k=5 和 n=3,k=6 代入计算后发现边界处理起来不太方便，故我们可以尝试将 k 减1进行运算，后面的基准也随之变化。第一个数可以通过`(k-1)/(n-1)!`进行计算，那么第二个数呢？联想不同进制数之间的转化，我们可以通过求模运算求得下一个数的`k-1`, 那么下一个数可通过`(k2 - 1)/(n-2)!`求得，这里不理解的可以通过进制转换类比进行理解。和减掉相应的阶乘值是等价的。

### Python

```python
class Solution:
    """
    @param n: n
    @param k: the k-th permutation
    @return: a string, the k-th permutation
    """
    def getPermutation(self, n, k):
        # generate factorial list
        factorial = [1]
        for i in xrange(1, n + 1):
            factorial.append(factorial[-1] * i)

        nums = range(1, n + 1)
        perm = []
        for i in xrange(n):
            rank = (k - 1) / factorial[n - i - 1]
            k = (k - 1) % factorial[n - i - 1] + 1
            # append and remove nums[rank]
            perm.append(nums[rank])
            nums.remove(nums[rank])
        # combine digits
        return "".join([str(digit) for digit in perm])
```

### C++

```c++
class Solution {
public:
    /**
      * @param n: n
      * @param k: the kth permutation
      * @return: return the k-th permutation
      */
    string getPermutation(int n, int k) {
        // generate factorial list
        vector<int> factorial = vector<int>(n + 1, 1);
        for (int i = 1; i < n + 1; ++i) {
            factorial[i] = factorial[i - 1] * i;
        }
        // generate digits ranging from 1 to n
        vector<int> nums;
        for (int i = 1; i < n + 1; ++i) {
            nums.push_back(i);
        }

        vector<int> perm;
        for (int i = 0; i < n; ++i) {
            int rank = (k - 1) / factorial[n - i - 1];
            k = (k - 1) % factorial[n - i - 1] + 1;
            // append and remove nums[rank]
            perm.push_back(nums[rank]);
            nums.erase(std::remove(nums.begin(), nums.end(), nums[rank]), nums.end());
        }
        // transform a vector<int> to a string
        std::stringstream result;
        std::copy(perm.begin(), perm.end(), std::ostream_iterator<int>(result, ""));

        return result.str();
    }
};
```

### Java

```java
class Solution {
    /**
      * @param n: n
      * @param k: the kth permutation
      * @return: return the k-th permutation
      */
    public String getPermutation(int n, int k) {
        if (n <= 0 && k <= 0) return "";

        int fact = 1;
        // generate nums 1 to n
        List<Integer> nums = new ArrayList<Integer>();
        for (int i = 1; i <= n; i++) {
            fact *= i;
            nums.add(i);
        }

        // get the permutation digit
        StringBuilder sb = new StringBuilder();
        for (int i = n; i >= 1; i--) {
            fact /= i;
            // take care of rank and k
            int rank = (k - 1) / fact;
            k = (k - 1) % fact + 1;
            // ajust the mapping of rank to num
            sb.append(nums.get(rank));
            nums.remove(rank);
        }

        return sb.toString();
    }
}
```

### 源码分析

源码结构分为三步走，

1. 建阶乘数组
2. 生成排列数字数组
3. 从高位到低位计算排列数值

### 复杂度分析

几个 for 循环，时间复杂度为 $$O(n)$$, 用了与 n 等长的一些数组，空间复杂度为 $$O(n)$$.

## Reference

- [Permutation Sequence 解题报告](http://blog.sina.com.cn/s/blog_eb52001d0102v1ss.html)
- [Permutation Sequence 参考程序 Java/C++/Python](http://www.jiuzhang.com/solutions/permutation-sequence/)
- [c++ - How to transform a vector<int> into a string? - Stack Overflow](http://stackoverflow.com/questions/2518979/how-to-transform-a-vectorint-into-a-string)
