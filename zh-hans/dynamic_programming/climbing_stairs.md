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

## 题解

题目问的是到达顶端的方法数，我们采用序列类问题的通用分析方法，可以得到如下四要素：

1. State: f[i] 爬到第i级的方法数
2. Function: f[i]=f[i-1]+f[i-2]
3. Initialization: f[0]=1,f[1]=1
4. Answer: f[n]

尤其注意状态转移方程的写法，f[i]只可能由两个中间状态转化而来，一个是f[i-1]，由f[i-1]到f[i]其方法总数并未增加；另一个是f[i-2]，由f[i-2]到f[i]隔了两个台阶，因此有1+1和2两个方法，因此容易写成 f[i]=f[i-1]+f[i-2]+1，但仔细分析后能发现，由f[i-2]到f[i]的中间状态f[i-1]已经被利用过一次，故f[i]=f[i-1]+f[i-2]. 使用动规思想解题时需要分清『重叠子状态』, 如果有重复的需要去重。

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

1. 异常处理
2. 初始化n+1个元素，初始值均为1。之所以用n+1个元素是下标分析起来更方便
3. 状态转移方程
4. 返回ret[n]

初始化ret[0]也为1，可以认为到第0级也是一种方法。

以上答案的空间复杂度为 $$O(n)$$，仔细观察后可以发现在状态转移方程中，我们可以使用三个变量来替代长度为n+1的数组。具体代码可参考 [climbing-stairs | 九章算法 ](http://www.jiuzhang.com/solutions/climbing-stairs/)

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
