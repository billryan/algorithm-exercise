# Best Time to Buy and Sell Stock II

## Question

- leetcode: [Best Time to Buy and Sell Stock II | LeetCode OJ](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)
- lintcode: [(150) Best Time to Buy and Sell Stock II](http://www.lintcode.com/en/problem/best-time-to-buy-and-sell-stock-ii/)

```
Say you have an array for
which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete as many transactions as you like
(ie, buy one and sell one share of the stock multiple times).
However, you may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).

Example
Given an example [2,1,2,0,1], return 2
```

## 题解

卖股票系列之二，允许进行多次交易，但是不允许同时进行多笔交易。直觉上我们可以找到连续的多对波谷波峰，在波谷买入，波峰卖出，稳赚不赔~ 那么这样是否比只在一个差值最大的波谷波峰处交易赚的多呢？即比上题的方案赚的多。简单的证明可先假设存在一单调上升区间，若人为改变单调区间使得区间内存在不少于一对波谷波峰，那么可以得到进行两次交易的差值之和比单次交易大，证毕。

好了，思路知道了——计算所有连续波谷波峰的差值之和。需要遍历求得所有波谷波峰的值吗？我最开始还真是这么想的，看了 soulmachine 的题解才发现原来可以把数组看成时间序列，只需要计算相邻序列的差值即可，只累加大于0的差值。

### Python

```python
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if prices is None or len(prices) <= 1:
            return 0

        profit = 0
        for i in xrange(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            if diff > 0:
                profit += diff

        return profit
```

### C++

```c++
class Solution {
public:
    /**
     * @param prices: Given an integer array
     * @return: Maximum profit
     */
    int maxProfit(vector<int> &prices) {
        if (prices.size() <= 1) return 0;

        int profit = 0;
        for (int i = 1; i < prices.size(); ++i) {
            int diff = prices[i] - prices[i - 1];
            if (diff > 0) profit += diff;
        }

        return profit;
    }
};
```

### Java

```java
class Solution {
    /**
     * @param prices: Given an integer array
     * @return: Maximum profit
     */
    public int maxProfit(int[] prices) {
        if (prices == null || prices.length <= 1) return 0;

        int profit = 0;
        for (int i = 1; i < prices.length; i++) {
            int diff = prices[i] - prices[i - 1];
            if (diff > 0) profit += diff;
        }

        return profit;
    }
};
```

### 源码分析

核心在于将多个波谷波峰的差值之和的计算转化为相邻序列的差值，故 i 从1开始算起。

### 复杂度分析

遍历一次原数组，时间复杂度为 $$O(n)$$, 用了几个额外变量，空间复杂度为 $$O(1)$$.

## Reference

- soulmachine 的卖股票系列
