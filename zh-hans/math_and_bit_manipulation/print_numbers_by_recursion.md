# Print Numbers by Recursion

## Question

- lintcode: [(371) Print Numbers by Recursion](http://www.lintcode.com/en/problem/print-numbers-by-recursion/)

```
Print numbers from 1 to the largest number with N digits by recursion.

Example
Given N = 1, return [1,2,3,4,5,6,7,8,9].

Given N = 2, return [1,2,3,4,5,6,7,8,9,10,11,12,...,99].

Note
It's pretty easy to do recursion like:

recursion(i) {
    if i > largest number:
        return
    results.add(i)
    recursion(i + 1)
}
however this cost a lot of recursion memory as the recursion depth maybe very large.
Can you do it in another way to recursive with at most N depth?

Challenge
Do it in recursion, not for-loop.
```

## 题解

从小至大打印 N 位的数列，正如题目中所提供的 `recursion(i)`, 解法简单粗暴，但问题在于 N 稍微大一点时栈就溢出了，因为递归深度太深了。能联想到的方法大概有两种，一种是用排列组合的思想去解释，把0~9当成十个不同的数(字符串表示)，塞到 N 个坑位中，这个用 DFS 来解应该是可行的；另一个则是使用数学方法，依次递归递推，比如 N=2 可由 N=1递归而来，具体方法则是乘10进位加法。题中明确要求递归深度最大不超过 N, 故 DFS 方法比较危险。

### Java

```java
public class Solution {
    /**
     * @param n: An integer.
     * return : An array storing 1 to the largest number with n digits.
     */
    public List<Integer> numbersByRecursion(int n) {
        List<Integer> result = new ArrayList<Integer>();
        if (n <= 0) {
            return result;
        }
        helper(n, result);
        return result;
    }

    private void helper(int n, List<Integer> ret) {
        if (n == 0) return;
        helper(n - 1, ret);
        // current base such as 10, 20, 30...
        int base = (int)Math.pow(10, n - 1);
        // get List size before for loop
        int size = ret.size();
        for (int i = 1; i < 10; i++) {
            // add 10, 100, 1000...
            ret.add(i * base);
            for (int j = 0; j < size; j++) {
                // add 11, 12, 13...
                ret.add(ret.get(j) + base * i);
            }
        }
    }
}
```

### 源码分析

递归步的截止条件`n == 0`, 由于需要根据之前 N-1 位的数字递推，`base` 每次递归一层都需要乘10，`size`需要在`for`循环之前就确定。

### 复杂度分析

添加 $$10^n$$ 个元素，时间复杂度 $$O(10^n)$$, 空间复杂度 $$O(1)$$.

## Reference

- [Lintcode: Print Numbers by Recursion | codesolutiony](https://codesolutiony.wordpress.com/2015/05/21/lintcode-print-numbers-by-recursion/)
