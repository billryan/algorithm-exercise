# Wood Cut

## Question

- lintcode: [(183) Wood Cut](http://www.lintcode.com/en/problem/wood-cut/)

### Problem Statement

Given n pieces of wood with length `L[i]` (integer array). Cut them into small
pieces to guarantee you could have equal or more than k pieces with the same
length. What is the longest length you can get from the n pieces of wood?
Given L &amp; k, return the maximum length of the small pieces.

#### Example

For `L=[232, 124, 456]`, `k=7`, return `114`.

#### Note

You couldn't cut wood into float length.

#### Challenge

O(n log Len), where Len is the longest length of the wood.

## 题解 - 二分搜索

这道题要直接想到二分搜素其实不容易，但是看到题中 Challenge 的提示后你大概就能想到往二分搜索上靠了。首先来分析下题意，题目意思是说给出 n 段木材`L[i]`, 将这 n 段木材切分为至少 k 段，这 k 段等长，求能从 n 段原材料中获得的最长单段木材长度。以 k=7 为例，要将 L 中的原材料分为7段，能得到的最大单段长度为114, 232/114 = 2, 124/114 = 1, 456/114 = 4, 2 + 1 + 4 = 7.

理清题意后我们就来想想如何用算法的形式表示出来，显然在计算如`2`, `1`, `4`等分片数时我们进行了取整运算，在计算机中则可以使用下式表示：
$$\sum _{i = 1} ^{n} \frac {L[i]}{l} \geq k$$

其中 $$l$$ 为单段最大长度，显然有 $$1 \leq l \leq max(L[i])$$. 单段长度最小为1，最大不可能超过给定原材料中的最大木材长度。

> **Warning** 注意求和与取整的顺序，是先求 `L[i]/l`的单个值，而不是先对`L[i]`求和。

分析到这里就和题 [Sqrt x](http://algorithm.yuanbin.me/zh-hans/binary_search/sqrt_x.html) 差不多一样了，要求的是 $$l$$ 的最大可能取值，同时 $$l$$ 可以看做是从有序序列`[1, max(L[i])]`的一个元素，典型的二分搜素！

P.S. 关于二分搜索总结在 [Binary Search](http://algorithm.yuanbin.me/zh-hans/basics_algorithm/binary_search.html) 一小节，直接套用『模板二——最优化』即可。

### Python

```python
class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    return: The maximum length of the small pieces.
    """
    def woodCut(self, L, k):
        if sum(L) < k:
            return 0

        start, end = 1, max(L)
        while start + 1 < end:
            mid = (start + end) / 2
            pieces_sum = sum(len_i / mid for len_i in L)
            if pieces_sum < k:
                end = mid
            else:
                start = mid

        if sum(len_i / end for len_i in L) >= k:
            return end
        return start
```

### C++
```c++
class Solution {
public:
    /** 
     *@param L: Given n pieces of wood with length L[i]
     *@param k: An integer
     *return: The maximum length of the small pieces.
     */
    int woodCut(vector<int> L, int k) {
        // write your code here
        int lb = 0, ub = 0;
        for (auto l : L) if (l + 1 > ub) ub = l + 1;
        
        while (lb + 1 < ub) {
            int mid = lb + (ub - lb) / 2;
            if (C(L, k, mid)) lb = mid;
            else ub = mid;
        }
        return lb;
    }
    
    int C(vector<int> L, int k, int mid) {
        int sum = 0;
        for (auto l : L) {
            sum += l / mid;
        }
        return sum >= k;
    }
};
```

### Java

```java
public class Solution {
    /**
     *@param L: Given n pieces of wood with length L[i]
     *@param k: An integer
     *return: The maximum length of the small pieces.
     */
    public int woodCut(int[] L, int k) {
        if (L == null || L.length == 0) return 0;

        int lb = 0, ub = Integer.MIN_VALUE;
        // get the upper bound of L
        for (int l : L) if (l > ub) ub = l + 1;

        while (lb + 1 < ub) {
            int mid = lb + (ub - lb) / 2;
            if (C(L, k, mid)) {
                lb = mid;
            } else {
                ub = mid;
            }
        }

        return lb;
    }

    // whether it cut with length x and get more than k pieces
    private boolean C(int[] L, int k, int x) {
        int sum = 0;
        for (int l : L) {
            sum += l / x;
        }
        return sum >= k;
    }
}
```

### 源码分析

定义私有方法`C`为切分为 x 长度时能否大于等于 k 段。若满足条件则更新`lb`, 由于 lb 和 ub 的初始化技巧使得我们无需单独对最后的 lb 和 ub 单独求和判断。九章算法网站上的方法初始化为1和某最大值，还需要单独判断，虽然不会出bug, 但稍显复杂。这个时候lb, ub初始化为两端不满足条件的值的优雅之处就体现出来了。

### 复杂度分析

遍历求和时间复杂度为 $$O(n)$$, 二分搜索时间复杂度为 $$O(\log max(L))$$. 故总的时间复杂度为 $$O(n \log max(L))$$. 空间复杂度 $$O(1)$$.

## Reference

- [Binary Search](http://algorithm.yuanbin.me/zh-hans/basics_algorithm/binary_search.html)
