# Best Time to Buy and Sell Stock

## Question

- leetcode: [Best Time to Buy and Sell Stock | LeetCode OJ](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- lintcode: [(149) Best Time to Buy and Sell Stock](http://www.lintcode.com/en/problem/best-time-to-buy-and-sell-stock/)

```
Say you have an array for
which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction
(ie, buy one and sell one share of the stock),
design an algorithm to find the maximum profit.

Example
Given an example [3,2,3,1,2], return 1
```

## 题解

最多只允许进行一次交易，显然我们只需要把波谷和波峰分别找出来就好了。但是这样的话问题又来了，有多个波峰和波谷时怎么办？——找出差值最大的一对波谷和波峰。故需要引入一个索引用于记录当前的波谷，结果即为当前索引值减去波谷的值。

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
        cur_price_min = 2**31 - 1
        for price in prices:
            profit = max(profit, price - cur_price_min)
            cur_price_min = min(cur_price_min, price)

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
        int cur_price_min = INT_MAX;
        for (int i = 0; i < prices.size(); ++i) {
            profit = max(profit, prices[i] - cur_price_min);
            cur_price_min = min(cur_price_min, prices[i]);
        }

        return profit;
    }
};
```

### Java

```java
public class Solution {
    /**
     * @param prices: Given an integer array
     * @return: Maximum profit
     */
    public int maxProfit(int[] prices) {
        if (prices == null || prices.length <= 1) return 0;

        int profit = 0;
        int curPriceMin = Integer.MAX_VALUE;
    	for (int price : prices) {
            profit = Math.max(profit, price - curPriceMin);
            curPriceMin = Math.min(curPriceMin, price);
    	}

        return profit;
    }
}
```

### 源码分析

善用`max`和`min`函数，减少`if`的使用。

### 复杂度分析

遍历一次 prices 数组，时间复杂度为 $$O(n)$$, 使用了几个额外变量，空间复杂度为 $$O(1)$$.

## Reference

- soulmachine 的卖股票系列
