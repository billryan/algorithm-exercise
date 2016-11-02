# Climbing Stairs

## Question

- lintcode: [(111) Climbing Stairs](http://www.lintcode.com/en/problem/climbing-stairs/)

```
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Example
Given an example n=3 , 1+1+1=2+1=1+2=3

return 3
```

## 題解

題目問的是到達頂端的方法數，我們採用序列類問題的通用分析方法，可以得到如下四要素：

1. State: f[i] 爬到第i級的方法數
2. Function: f[i]=f[i-1]+f[i-2]
3. Initialization: f[0]=1,f[1]=1
4. Answer: f[n]

尤其注意狀態轉移方程的寫法，f[i]只可能由兩個中間狀態轉化而來，一個是f[i-1]，由f[i-1]到f[i]其方法總數並未增加；另一個是f[i-2]，由f[i-2]到f[i]隔了兩個臺階，因此有1+1和2兩個方法，因此容易寫成 f[i]=f[i-1]+f[i-2]+1，但仔細分析後能發現，由f[i-2]到f[i]的中間狀態f[i-1]已經被利用過一次，故f[i]=f[i-1]+f[i-2]. 使用動規思想解題時需要分清『重疊子狀態』, 如果有重複的需要去掉。

### C++

```c++
class Solution {
public:
    /**
     * @param n: An integer
     * @return: An integer
     */
    int climbStairs(int n) {
        if (n < 1) {
            return 0;
        }

        vector<int> ret(n + 1, 1);

        for (int i = 2; i != n + 1; ++i) {
            ret[i] = ret[i - 1] + ret[i - 2];
        }

        return ret[n];
    }
};
```

1. 異常處理
2. 初始化n+1個元素，初始值均爲1。之所以用n+1個元素是下標分析起來更方便
3. 狀態轉移方程
4. 返回ret[n]

初始化ret[0]也爲1，可以認爲到第0級也是一種方法。

以上答案的空間複雜度爲 $$O(n)$$，仔細觀察後可以發現在狀態轉移方程中，我們可以使用三個變數來替代長度爲n+1的數組。具體程式碼可參考 [climbing-stairs | 九章算法 ](http://www.jiuzhang.com/solutions/climbing-stairs/)

### Python
```python
class Solution:
    def climbStairs(n):
        if n < 1:
            return 0

        l = r = 1
        for _ in xrange(n - 1):
            l, r = r, r + l
        return r
```

### C++

```c++
class Solution {
public:
    /**
     * @param n: An integer
     * @return: An integer
     */
    int climbStairs(int n) {
        if (n < 1) {
            return 0;
        }

        int ret0 = 1, ret1 = 1, ret2 = 1;

        for (int i = 2; i != n + 1; ++i) {
            ret0 = ret1 + ret2;
            ret2 = ret1;
            ret1 = ret0;
        }

        return ret0;
    }
};
```
