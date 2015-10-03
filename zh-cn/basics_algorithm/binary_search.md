# Binary Search - 二分搜索

二分搜索是一种在有序数组中寻找目标值的经典方法，也就是说使用前提是『有序数组』。非常简单的题中『有序』特征非常明显，但更多时候可能需要我们自己去构造『有序数组』。下面我们从最基本的二分搜索开始逐步深入。

## 模板一 - 从有序数组中寻找目标值

以 lintcode 上一道测试题 [search insert position](http://algorithm.yuanbin.me/zh-cn/binary_search/search_insert_position.html) 为例，题目要求寻找目标值在升序数组中插入的索引。我们先直接看代码。

### Java

```java
public class Solution {
    /**
     * param A : an integer sorted array
     * param target :  an integer to be inserted
     * return : an integer
     */
    public int searchInsert(int[] A, int target) {
        if (A == null || A.length == 0) {
            return -1;
        }
        // lower bound, upper bound
        int lb = -1, ub = A.length;
        while (lb + 1 < ub) {
            int mid = lb + (ub - lb) / 2;
            if (A[mid] == target) {
                return mid; // no duplicates
            } else if (A[mid] < target) {
                lb = mid;
            } else {
                ub = mid;
            }
        }

	    return lb + 1;
    }
}
```

### 源码分析

以上二分搜索的模板有两个非常优雅的实现：

1. `while` 循环中 `start + 1 < end`, 而不是等号，因为取等号可能会引起死循环。初始化`start < end` 时，最后循环退出时一定有`start + 1 == end`.
2. `start` 和 `end` 的初始化，初始化为数组的两端以外，这种初始化方式比起`0` 和`nums.length - 1` 有不少优点，详述如下。

插入位置可以分三种典型情况：

1. 目标值在数组范围之内，最后返回值一定是`start + 1`
2. 目标值比数组最小值还小，此时`start` 一直为`-1`, 故最后返回`start + 1` 也没错，也可以将`-1` 理解为数组前一个更小的值
3. 目标值大于等于数组最后一个值，由于循环退出条件为`start + 1 == end`, 那么循环退出时一定有`start = A.length - 1`, 应该返回`start + 1`

综上所述，返回`start + 1`是非常优雅的实现。其实以上三种情况都可以统一为一种方式来理解，即索引`-1` 对应于数组前方一个非常小的数，索引`end` 即对应数组后方一个非常大的数，那么要插入的数就一定在`start` 和`end` 之间了。

**有时复杂的边界条件处理可以通过『补项』这种优雅的方式巧妙处理。**

使用这个模板可以直接解决的问题有如 lower/upper bound, 有序数组中寻找目标值等。

## 模板二 - 最优解

除了在有序数组中寻找目标值这种非常直接的二分搜索外，我们还可以利用二分搜索求最优解（最大值/最小值），通常这种题中只是隐含了『有序数组』，需要我们自己构造。

用数学语言来描述就是『求满足某条件 $$C(x)$$ 的最小/大的 $$x$$』，以求最小值为例，对于任意满足条件的 $$x$$, 如果所有的 $$x \leq x^\prime \leq UB$$ 对于 $$C(x^\prime)$$ 都为真（其中 `UB` 可能为无穷大，也可能为满足条件的最大的解，如果不满足此条件就不能保证二分搜索的正确性），那么我们就能使用二分搜索进行求解，其中初始化时下界`lb` 初始化为不满足条件的值`LB`, 上界初始化为满足条件的上界`UB`. 随后在`while` 循环内部每次取中，满足条件就取`ub = mid`, 否则`lb = mid`, 那么最后`ub` 就是要求的最小值。求最大值时类似，只不过处理的是`lb`.

以 POJ No.1064 为例。

### Problem

有 $$N$$ 条绳子，它们的长度分别为 $$L_i$$. 如果从它们中切割出 $$K$$ 条长度相同的绳子的话，这 $$K$$ 条绳子每条最长能有多长？答案保留到小数点后两位。

#### 输入

```
N = 4, L = {8.02, 7.43, 4.57, 5.39}, K = 11
```

#### 输出

2.00

### 题解

这道题看似是一个最优化问题，我们来尝试下使用模板二的思想求解，**令 $$C(x)$$ 为『可以得到 $$K$$ 条长度为 $$x$$ 的绳子』。根据题意，我们可以将上述条件进一步细化为：
$$
C(x) = \sum_i(floor(L_i / x)) \geq K
$$

我们现在来分析下可行解的上下界。由于答案保留小数点后两位，显然绳子长度一定大于0，大于0的小数点后保留两位的最小值为`0.01`, 显然如果问题最后有解，`0.01` 一定是可行解中最小的，且这个解可以分割出的绳子条数是最多的。一般在 OJ 上不同变量都是会给出范围限制，那么我们将上界初始化为`最大范围 + 0.01`, 它一定在可行解之外（也可以遍历一遍数组取数组最大值，但其实二分后复杂度相差不大）。使用二分搜索后最后返回`lb` 即可。

### Java

```java
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        double[] nums = new double[n];
        for (int i = 0; i < n; i++) {
            nums[i] = in.nextDouble();
        }
        System.out.printf("%.2f\n", Math.floor(solve(nums, k) * 100) / 100);
    }

    public static double solve(double[] nums, int K) {
        double lb = 0.01, ub = 10e5 + 0.01;
        while (lb + 0.001 < ub) {
            double mid = lb + (ub - lb) / 2;
            if (C(nums, mid, K)) {
                lb = mid;
            } else {
                ub = mid;
            }
        }
        return lb;
    }

    public static boolean C(double[] nums, double seg, int k) {
        int count = 0;
        for (double num : nums) {
            count += Math.floor(num / seg);
        }
        return count >= k;
    }
}
```

### 源码分析

方法`C` 只做一件事，给定数组`nums`, 判断是否能切割出`K` 条长度均为`seg` 的绳子。`while` 循环中使用`lb + 0.001 < ub`, 不能使用`0.01`, 因为计算`mid` 时有均值的计算，对于`double` 型数值否则会有较大误差。

## 模板三 - 二分搜索的 `while` 结束条件判定

> **Note** 对于整型我们通常使用`lb + 1 < ub`, 但对于`double`型数据来说会有些精度上的丢失，使得结束条件不是那么好确定。像上题中采用的方法是题目中使用的精度除10。但有时候这种精度可能还是不够，如果结束条件`lb + EPS < ub`中使用的 EPS 过小时 double 型数据精度有可能不够从而导致死循环的产生！这时候我们将`while`循环体替换为`for (int i = 0; i < 100; i++)`, 100 次循环后可以达到 $$10^{-30}$$ 精度范围，一般都没问题。

## Reference

- 《挑战程序设计竞赛》
