# Wood Cut

## Source

- lintcode: [(183) Wood Cut](http://www.lintcode.com/en/problem/wood-cut/)

```
Given n pieces of wood with length L[i] (integer array).
Cut them into small pieces to guarantee you could have equal or more than k pieces with the same length.
What is the longest length you can get from the n pieces of wood?
Given L & k, return the maximum length of the small pieces.

Example
For L=[232, 124, 456], k=7, return 114.

Note
You couldn't cut wood into float length.

Challenge
O(n log Len), where Len is the longest length of the wood.
```

## 题解 - 二分搜索

这道题要直接想到二分搜素其实不容易，但是看到题中 Challenge 的提示后你大概就能想到往二分搜索上靠了。首先来分析下题意，题目意思是说给出 n 段木材`L[i]`, 将这 n 段木材切分为至少 k 段，这 k 段等长，求能从 n 段原材料中获得的最长单段木材长度。以 k=7 为例，要将 L 中的原材料分为7段，能得到的最大单段长度为114, 232/114 = 2, 124/114 = 1, 456/114 = 4, 2 + 1 + 4 = 7.

理清题意后我们就来想想如何用算法的形式表示出来，显然在计算如`2`, `1`, `4`等分片数时我们进行了取整运算，在计算机中则可以使用下式表示：
$$\sum _{i = 1} ^{n} \frac {L[i]}{l} \geq k$$

其中 $$l$$ 为单段最大长度，显然有 $$1 \leq l \leq max(L[i])$$. 单段长度最小为1，最大不可能超过给定原材料中的最大木材长度。

> **Warning** 注意求和与取整的顺序，是先求 `L[i]/l`的单个值，而不是先对`L[i]`求和。

分析到这里就和题 [Sqrt x](http://algorithm.yuanbin.me/binary_search/sqrt_x.html) 差不多一样了，要求的是 $$l$$ 的最大可能取值，同时 $$l$$ 可以看做是从有序序列`[1, max(L[i])]`的一个元素，典型的二分搜素！

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

        max_len = max(L)
        start, end = 1, max_len
        while start + 1 < end:
            mid = start + (end - start) / 2
            pieces_sum = sum([len_i / mid for len_i in L])
            if pieces_sum < k:
                end = mid
            else:
                start = mid

        # corner case
        if end == 2 and sum([len_i / 2 for len_i in L]) >= k:
            return 2

        return start
```

### 源码分析

1. 异常处理，若对 L 求和所得长度都小于 k，那么肯定无解。
2. 初始化`start`和`end`, 使用二分搜索。
3. 使用 list comprehension 求 $$\sum _{i = 1} ^{n} \frac {L[i]}{l}$$.
4. 若求得的`pieces_sum`小于 k，则说明`mid`偏大，下一次循环应缩小`mid`，对应为将当前`mid`赋给`end`.
5. 与一般的二分搜索不同，即使有`pieces_sum == k`也不应立即返回`mid`, 因为这里使用了取整运算，满足`pieces_sum == k`的值不止一个，应取其中最大的`mid`, 具体实现中可以将`pieces_sum < k`写在前面，大于等于的情况直接用`start = end`代替。
6. 排除`end == 2`之后返回`start`即可。

简单对第6条做一些说明，首先需要进行二分搜索的前提是 `sum(L) >= k`且`end`不满足`end == 1 || end == 2`, `end`为2时单独考虑即可。

### 复杂度分析

遍历求和时间复杂度为 $$O(n)$$, 二分搜索时间复杂度为 $$O(\log max(L))$$. 故总的时间复杂度为 $$O(n \log n)$$. 空间复杂度 $$O(1)$$.

## Reference

- [Wood Cut | 九章算法](http://www.jiuzhang.com/solutions/wood-cut/)
