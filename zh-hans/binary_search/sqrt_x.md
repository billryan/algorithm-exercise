# Sqrt(x)

Tags: Binary Search, Math, Medium

## Question

- leetcode: [Sqrt(x)](https://leetcode.com/problems/sqrtx/)
- lintcode: [Sqrt(x)](http://www.lintcode.com/en/problem/sqrtx/)

### Problem Statement

Implement `int sqrt(int x)`.

Compute and return the square root of _x_.

## 题解 - 二分搜索

由于只需要求整数部分，故对于任意正整数 $$x$$, 设其整数部分为 $$k$$, 显然有 $$1 \leq k \leq x$$, 求解 $$k$$ 的值也就转化为了在有序数组中查找满足某种约束条件的元素，显然二分搜索是解决此类问题的良方。

### Python

```python
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return -1
        elif x == 0:
            return 0

        lb, ub = 1, x
        while lb + 1 < ub:
            mid = (lb + ub) / 2
            if mid**2 == x:
                return mid
            elif mid**2 < x:
                lb = mid
            else:
                ub = mid

        return lb
```

### C++

```cpp
class Solution {
public:
    int mySqrt(int x) {
        if (x < 0) return -1;
        if (x == 0) return 0;

        int lb = 1, ub = x;
        long long mid = 0;
        while (lb + 1 < ub) {
            mid = lb + (ub - lb) / 2;
            if (mid * mid == x) {
                return mid;
            } else if (mid * mid < x) {
                lb = mid;
            } else {
                ub = mid;
            }
        }

        return lb;
    }
};
```

### Java

```java
public class Solution {
    public int mySqrt(int x) {
        if (x < 0) return -1;
        if (x == 0) return 0;

        int lb = 1, ub = x;
        long mid = 0;
        while (lb + 1 < ub) {
            mid = lb + (ub - lb) / 2;
            if (mid * mid == x) {
                return (int)mid;
            } else if (mid * mid < x) {
                lb = (int)mid;
            } else {
                ub = (int)mid;
            }
        }

        return (int)lb;
    }
}
```

### 源码分析

1. 异常检测，先处理小于等于0的值。
2. 使用二分搜索的经典模板，注意不能使用`lb < ub`, 否则在给定值1时产生死循环。
3. 最后返回平方根的整数部分`lb`.
4. C++ 代码 `mid` 需要定义为`long long`，否则计算平方时会溢出，定义 mid 放在循环体外部有助于提升效率。

二分搜索过程很好理解，关键是最后的返回结果还需不需要判断？比如是取 lb, ub, 还是 mid? 我们首先来分析下二分搜索的循环条件，由`while`循环条件`lb + 1 < ub`可知，`lb` 和 `ub` 只可能有两种关系，一个是`ub == 1 || ub ==2`这一特殊情况，返回值均为1，另一个就是循环终止时`lb`恰好在`ub`前一个元素。设值 x 的整数部分为 k, 那么在执行二分搜索的过程中 $$lb \leq k \leq ub$$ 关系一直存在，也就是说在没有找到 $$mid^2 == x$$ 时，循环退出时有 $$lb < k < ub$$, 取整的话显然就是`lb`了。

### 复杂度分析

经典的二分搜索，时间复杂度为 $$O(\log n)$$, 使用了`lb`, `ub`, `mid`变量，空间复杂度为 $$O(1)$$.

除了使用二分法求平方根近似解之外，还可使用牛顿迭代法进一步提高运算效率，欲知后事如何，请猛戳 [求平方根sqrt()函数的底层算法效率问题 -- 简明现代魔法](http://www.nowamagic.net/algorithm/algorithm_EfficacyOfFunctionSqrt.php)，不得不感叹算法的魔力！
