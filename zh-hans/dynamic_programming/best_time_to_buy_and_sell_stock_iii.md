# Best Time to Buy and Sell Stock III

## Question

- leetcode: [Best Time to Buy and Sell Stock III | LeetCode OJ](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)
- lintcode: [(151) Best Time to Buy and Sell Stock III](http://www.lintcode.com/en/problem/best-time-to-buy-and-sell-stock-iii/)

```
Say you have an array for
which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit.
You may complete at most two transactions.

Example
Given an example [4,4,6,1,1,4,2,5], return 6.

Note
You may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).
```

## 题解

与前两道允许一次或者多次交易不同，这里只允许最多两次交易，且这两次交易不能交叉。咋一看似乎无从下手，我最开始想到的是找到排在前2个的波谷波峰，计算这两个差值之和。原理上来讲应该是可行的，但是需要记录 $$O(n^2)$$ 个波谷波峰并对其排序，实现起来也比较繁琐。

除了以上这种直接分析问题的方法外，是否还可以借助分治的思想解决呢？最多允许两次不相交的交易，也就意味着这两次交易间存在某一分界线，考虑到可只交易一次，也可交易零次，故分界线的变化范围为第一天至最后一天，只需考虑分界线两边各自的最大利润，最后选出利润和最大的即可。

这种方法抽象之后则为首先将 [1,n] 拆分为 [1,i] 和 [i+1,n], 参考卖股票系列的第一题计算各自区间内的最大利润即可。[1,i] 区间的最大利润很好算，但是如何计算 [i+1,n] 区间的最大利润值呢？难道需要重复 n 次才能得到？注意到区间的右侧 n 是个不变值，我们从 [1, i] 计算最大利润是更新波谷的值，那么我们可否逆序计算最大利润呢？这时候就需要更新记录波峰的值了。逆向思维大法好！Talk is cheap, show me the code!

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

        n = len(prices)
        # get profit in the front of prices
        profit_front = [0] * n
        valley = prices[0]
        for i in xrange(1, n):
            profit_front[i] = max(profit_front[i - 1], prices[i] - valley)
            valley = min(valley, prices[i])
        # get profit in the back of prices, (i, n)
        profit_back = [0] * n
        peak = prices[-1]
        for i in xrange(n - 2, -1, -1):
            profit_back[i] = max(profit_back[i + 1], peak - prices[i])
            peak = max(peak, prices[i])
        # add the profit front and back
        profit = 0
        for i in xrange(n):
            profit = max(profit, profit_front[i] + profit_back[i])

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

        int n = prices.size();
        // get profit in the front of prices
        vector<int> profit_front = vector<int>(n, 0);
        for (int i = 1, valley = prices[0]; i < n; ++i) {
            profit_front[i] = max(profit_front[i - 1], prices[i] - valley);
            valley = min(valley, prices[i]);
        }
        // get profit in the back of prices, (i, n)
        vector<int> profit_back = vector<int>(n, 0);
        for (int i = n - 2, peak = prices[n - 1]; i >= 0; --i) {
            profit_back[i] = max(profit_back[i + 1], peak - prices[i]);
            peak = max(peak, prices[i]);
        }
        // add the profit front and back
        int profit = 0;
        for (int i = 0; i < n; ++i) {
            profit = max(profit, profit_front[i] + profit_back[i]);
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

        // get profit in the front of prices
        int[] profitFront = new int[prices.length];
        profitFront[0] = 0;
        for (int i = 1, valley = prices[0]; i < prices.length; i++) {
            profitFront[i] = Math.max(profitFront[i - 1], prices[i] - valley);
            valley = Math.min(valley, prices[i]);
        }
        // get profit in the back of prices, (i, n)
        int[] profitBack = new int[prices.length];
        profitBack[prices.length - 1] = 0;
        for (int i = prices.length - 2, peak = prices[prices.length - 1]; i >= 0; i--) {
            profitBack[i] = Math.max(profitBack[i + 1], peak - prices[i]);
            peak = Math.max(peak, prices[i]);
        }
        // add the profit front and back
        int profit = 0;
        for (int i = 0; i < prices.length; i++) {
            profit = Math.max(profit, profitFront[i] + profitBack[i]);
        }

        return profit;
    }
};
```

### 源码分析

整体分为三大部分，计算前半部分的最大利润值，然后计算后半部分的最大利润值，最后遍历得到最终的最大利润值。

### 复杂度分析

三次遍历原数组，时间复杂度为 $$O(n)$$, 利用了若干和数组等长的数组，空间复杂度也为 $$O(n)$$.

## Reference

- soulmachine 的卖股票系列
