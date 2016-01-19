# Binary Search - 二分搜索

二分搜索是一种在有序数组中寻找目标值的经典方法，也就是说使用前提是『有序数组』。非常简单的题中『有序』特征非常明显，但更多时候可能需要我们自己去构造『有序数组』。下面我们从最基本的二分搜索开始逐步深入。

## 模板一 - lower/upper bound

定义 lower bound 为在给定升序数组中大于等于目标值的最小索引，upper bound 则为小于等于目标值的最大索引，下面上代码和测试用例。

### Java

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        int[] nums = new int[]{1,2,2,3,4,6,6,6,13,18};
        System.out.println(lowerBound(nums, 6)); // 5
        System.out.println(upperBound(nums, 6)); // 7
        System.out.println(lowerBound(nums, 7)); // 8
        System.out.println(upperBound(nums, 7)); // 7
    }

    /*
    * nums[index] >= target, min(index)
    */
    public static int lowerBound(int[] nums, int target) {
        if (nums == null || nums.length == 0) return -1;
        int lb = -1, ub = nums.length;
        while (lb + 1 < ub) {
            int mid = lb + (ub - lb) / 2;
            if (nums[mid] < target) {
                lb = mid;
            } else {
                ub = mid;
            }
        }

        return lb + 1;
    }

    /*
    * nums[index] <= target, max(index)
    */
    public static int upperBound(int[] nums, int target) {
        if (nums == null || nums.length == 0) return -1;
        int lb = -1, ub = nums.length;
        while (lb + 1 < ub) {
            int mid = lb + (ub - lb) / 2;
            if (nums[mid] > target) {
                ub = mid;
            } else {
                lb = mid;
            }
        }

        return ub - 1;
    }
}
```

### 源码分析

以`lowerBound`的实现为例，以上二分搜索的模板有几个非常优雅的实现：

1. `while` 循环中 `lb + 1 < ub`, 而不是等号，因为取等号可能会引起死循环。初始化`lb < ub` 时，最后循环退出时一定有`lb + 1 == ub`.
2. `mid = lb + (ub - lb) / 2`, 可有效防止两数相加后溢出。
3. `lb` 和 `ub` 的初始化，初始化为数组的两端以外，这种初始化方式比起`0` 和`nums.length - 1` 有不少优点，详述如下。

如果遇到有问插入索引的位置时，可以分三种典型情况：

1. 目标值在数组范围之内，最后返回值一定是`lb + 1`
2. 目标值比数组最小值还小，此时`lb` 一直为`-1`, 故最后返回`lb + 1` 也没错，也可以将`-1` 理解为数组前一个更小的值
3. 目标值大于等于数组最后一个值，由于循环退出条件为`lb + 1 == ub`, 那么循环退出时一定有`lb = A.length - 1`, 应该返回`lb + 1`

综上所述，返回`lb + 1`是非常优雅的实现。其实以上三种情况都可以统一为一种方式来理解，即索引`-1` 对应于数组前方一个非常小的数，索引`ub` 即对应数组后方一个非常大的数，那么要插入的数就一定在`lb` 和`ub` 之间了。

**有时复杂的边界条件处理可以通过『补项』这种优雅的方式巧妙处理。**

关于lb 和 ub 的初始化，由于`mid = lb + (ub - lb) / 2`, 且有`lb + 1 < ub`，故 mid 还是有可能为`ub - 1`或者`lb + 1`的，在需要访问`mid + 1`或者`mid - 1`处索引的元素时可能会越界。这时候就需要将初始化方式改为`lb = 0, ub = A.length - 1` 了，最后再加一个关于`lb, ub` 处索引元素的判断即可。如 [Search for a Range](http://algorithm.yuanbin.me/zh-hans/binary_search/search_for_a_range.html) 和 [Find Peak Element](http://algorithm.yuanbin.me/zh-hans/binary_search/find_peak_element.html). 尤其是 Find Peak Element 中 lb 和 ub 的初始值如果初始化为-1和数组长度会带来一些麻烦。

## 模板二 - 最优解

除了在有序数组中寻找目标值这种非常直接的二分搜索外，我们还可以利用二分搜索求最优解（最大值/最小值），通常这种题中只是隐含了『有序数组』，需要我们自己构造。

用数学语言来描述就是『求满足某条件 $$C(x)$$ 的最小/大的 $$x$$』，以求最小值为例，对于任意满足条件的 $$x$$, 如果所有的 $$x \leq x^\prime \leq UB$$ 对于 $$C(x^\prime)$$ 都为真（其中 `UB` 可能为无穷大，也可能为满足条件的最大的解，如果不满足此条件就不能保证二分搜索的正确性），那么我们就能使用二分搜索进行求解，其中初始化时下界`lb` 初始化为不满足条件的值`LB`, 上界初始化为满足条件的上界`UB`. 随后在`while` 循环内部每次取中，满足条件就取`ub = mid`, 否则`lb = mid`, 那么最后`ub` 就是要求的最小值。求最大值时类似，只不过处理的是`lb`.

以 [POJ No.1064](http://poj.org/problem?id=1064) 为例。

### Problem Statement

有 $$N$$ 条绳子，它们的长度分别为 $$L_i$$. 如果从它们中切割出 $$K$$ 条长度相同的绳子的话，这 $$K$$ 条绳子每条最长能有多长？答案保留到小数点后两位。

#### 输入

```
N = 4, L = {8.02, 7.43, 4.57, 5.39}, K = 11
```

#### 输出

2.00

### 题解

这道题看似是一个最优化问题，我们来尝试下使用模板二的思想求解，**令 $$C(x)$$ 为『可以得到 $$K$$ 条长度为 $$x$$ 的绳子』。**根据题意，我们可以将上述条件进一步细化为：
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
        double lb = 0.00, ub = 10e5 + 0.01;
        // while (lb + 0.001 < ub) {
	for (int i = 0; i < 100; i++) {
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

对于整型我们通常使用`lb + 1 < ub`, 但对于`double`型数据来说会有些精度上的丢失，使得结束条件不是那么好确定。像上题中采用的方法是题目中使用的精度除10。但有时候这种精度可能还是不够，如果结束条件`lb + EPS < ub`中使用的 EPS 过小时 double 型数据精度有可能不够从而导致死循环的产生！这时候我们将`while`循环体替换为`for (int i = 0; i < 100; i++)`, 100 次循环后可以达到 $$10^{-30}$$ 精度范围，一般都没问题。

## 模板四 － （九章算法）模版

这个模版跟第一个模版类似， 但是相对更容易上手。这个模版的核心是， `将binary search 问题转化成：寻找第一个或者最后一个，该target元素出现的位置的问题`，`Find the any/first/last position of target in nums`. 详解请见下面的例题。这个模版有四个要素。

1. start + 1 < end
    表示， 当指针指到两个元素，相邻或者相交的时候， 循环停止。 这样的话在最终分情况讨论的时候，只用考虑`1～2`个元素。
2. start + (end - start) / 2
    写C++ 和 Java的同学要考虑到int overflow的问题， 所以需要考虑边界情况。 写Python的同学就不用考虑了， 因为python这个语言本身已经非常努力的保证了number不会overflow。
3. A[mid] ==, >, <
    在循环中， 分三种情况讨论边界。 要注意， 在移动`start`和`end`的时候， 只要单纯的把指针指向`mid`的位置， 不要`+1`或者`-1`。 因为只移动边界到`mid`的位置， 不会误删除target。在工程中，尽量在程序最后的时候统一写`return`, 这样可以增强可读性。
4. A[start], A[end]? target
    在循环结束时，因为只有1～2个元素需要讨论，所以结果非常容易解释清楚。 只存在的2种情况为， 1. `start + 1 == end` 边界指向相邻的两个元素， 这时只需要分情况讨论`start`和`end`与target的关系，就可以得出结果。 2. `start == end` 边界指向同一元素， 其实这个情况还是可以按照1的方法，分成`start``end`讨论，只不过讨论结果一样而已。

### Python
```python
class Solution:
    def binary_search(self, array, target):
        if not array:
            return -1

        start, end = 0, len(array) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if array[mid] == target:
                start = mid
            elif array[mid] < target:
                start = mid
            else:
                end = mid

        if array[start] == target:
            return start
        if array[end] == target:
            return end
        return -1
```

### Java
```java
class Solution {
    public int binarySearch(int[] array, int target) {
        if (array == null || array.length == 0) {
            return -1;
        }

        int start = 0, end = array.length - 1;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (array[mid] == target) {
                start = mid;
            } else if (array[mid] < target) {
                start = mid;
            } else {
                end = mid;
            }
        }
        if (array[start] == target) {
            return start;
        }
        if (array[end] == target) {
            return end;
        }
        return -1;
    }
}
```

### Problem Statement
[Search for a Range](http://www.lintcode.com/zh-hans/problem/search-for-a-range/)

#### 样例
给出[5, 7, 7, 8, 8, 10]和目标值target=8,

返回[3, 4]

### Python
```python
class Solution:
    def search_range(self, array, target):
        ret = [-1, -1]
        if not array:
            return ret
        # search first position of target
        st, ed = 0, len(array) - 1
        while st + 1 < ed:
            mid = (st + ed) / 2
            if array[mid] == target:
                ed = mid
            elif array[mid] < target:
                st = mid
            else:
                ed = mid
        if array[st] == target:
            ret[0] = st
        elif array[ed] == target:
            ret[0] = ed

        # search last position of target
        st, ed = 0, len(array) - 1
        while st + 1 < ed:
            mid = (st + ed) / 2
            if array[mid] == target:
                st = mid
            elif array[mid] < target:
                st = mid
            else:
                ed = mid
        if array[ed] == target:
            ret[1] = ed
        elif array[st] == target:
            ret[1] = st

        return ret
```
### 源码分析
search range的问题可以理解为， 寻找第一次target出现的位置和最后一次target出现的位置。 当寻找第一次target出现位置的循环中， `array[mid] == target`表示， target可以出现在mid或者mid更前的位置， 所以将ed移动到mid。当循环跳出时， st的位置在ed之前，所以先判断在st位置上是否是target， 再判断ed位置。当寻找最后一次target出现位置的循环中，`array[mid] == target`表示， target可以出现在mid或者mid之后的位置， 所以将st移动到mid。 当循环结束时，ed的位置比st的位置更靠后， 所以先判断ed的位置是否为target， 再判断st位置。 最后返回ret。

## Reference

- 《挑战程序设计竞赛》
