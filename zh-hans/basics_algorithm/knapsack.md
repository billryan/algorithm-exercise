# Knapsack - 背包问题

在一次抢珠宝店的过程中，抢劫犯只能抢走以下三种珠宝，其重量和价值如下表所述。

| Item(jewellery) | Weight | Value |
| -- | -- | -- |
| 1 | 6 | 23 |
| 2 | 3 | 13 |
| 3 | 4 | 11 |

抢劫犯这次过来光顾珠宝店只带了一个最多只能承重 17 kg 的粉红色小包，于是问题来了，怎样搭配这些不同重量不同价值的珠宝才能不虚此行呢？唉，这年头抢劫也不容易啊...

用数学语言来描述这个问题就是：

背包最多只能承重 $$W$$ kg, 有 $$n$$ 种珠宝可供选择，这 $$n$$ 种珠宝的重量分别为 $$w_1,\cdots,w_n$$, 相应的价值为 $$v_1,\cdots,v_n$$. 问如何选择这些珠宝使得放进包里的珠宝价值最大化？

现实场景中，我们遇到的问题往往是重量或者珠宝数有限，对于这 n 种珠宝，只有两种情况——要么取，要么不取，这也被称为著名的 01 背包问题；而同一种珠宝如果可以取无限多次，则对应完全背包问题。

## Knapsack without repetition - 01 背包问题

我们先来处理一种珠宝最多只能带走一件这种情形下，抢劫犯该如何做才能使得背包中的珠宝价值总价最大？最为简单粗暴的方法自然是把这 n 种珠宝挨个试一遍，总共可能的组合数之和为 $$C_n^0 + \cdots + C_n^n = 2^n$$, 这种指数级别的时间复杂度显然是不能忍的，在搜索的过程中我们可以发现中间的一些子状态是可以避免重复计算的，下面我们使用动态规划的思路去进一步分析 01 背包问题。

在动态规划中，主要的问题之一就是——状态(子问题)是什么？在本题中我们可以从两个方面对原始问题进行化大为小：要么尝试更小的背包容量 $$w \leq W$$, 要么尝试更少的珠宝数目 $$j \leq n$$. 由于涉及到两个自变量，考虑到按顺序挑选珠宝这一过程更容易理解，我们不难定义状态 $$K(i, w)$$ 为挑选出前 i 件珠宝时，重量不超过 w 时的珠宝总价值的最大值。相应的状态转移方程为第 i 件珠宝要么不选，要么选，即 $$K(i,w) = \max \{K(i-1, w), K(i-1, w- w_i) + v_i\}$$. 令 `dp[i + 1][j]` 表示从前 i 种物品中选出总重量不超过 j 时珠宝总价值的最大值。那么有转移方程：

```
dp[i + 1][j] = max{dp[i][j], dp[i][j - w[i]] + v[i]}
```

时间复杂度为 $$(O(nW))$$.

这里的分析是以容量递推的，但是在容量特别大时，可以看出时间复杂度略高，这时我们可能需要以价值作为转移方程。定义状态 `dp[i + 1][j]` 为前 i 个物品中挑选出价值总和为 j 时总重量的最小值（所以对于不满足条件的索引应该用充分大的值而不是最大值替代，防止溢出）。相应的状态转移方程相思：即第 i 件珠宝选中与否，即 `dp[i + 1][j] = min{dp[i][j], dp[i][j - v[i]] + w[i]}`. 最终返回结果为 `dp[n][j] ≤ W` 中最大的 j.

## Knapsack with repetition - 物品重复可用的背包问题

相比于 01 背包问题，这类背包问题中同一物品可以被多次选择，因此称为 Knapsack with repetition, 又称 Unbounded knapsack problem(无界背包问题). 由 01 背包问题扩展后状态定义仍然可以不变，但状态变化则由原来的第 i 件珠宝选或者不选改为选不小于 0 任何整数件。

令 `dp[i + 1][j]` 表示从前 i 种物品中选出总重量不超过 j 时珠宝总价值的最大值。那么有转移方程：

```
dp[i + 1][j] = max{dp[i][j - k × w[i]] + k × v[i] | 0 ≤ k}
```

最坏情况下时间复杂度为 $$O(kW^2)$$. 我们对上式进一步变形可得：

```
dp[i + 1][j] = max{dp[i][j - k × w[i]] + k × v[i] | 0 ≤ k}
             = max{dp[i][j], max{dp[i][j - k × w[i]] + k × v[i] | 1 ≤ k}}
             = max{dp[i][j], max{dp[i][(j - w[i]) - k × w[i]] + k × v[i] | 0 ≤ k} + v[i]}
             = max{dp[i][j], dp[i + 1][j - w[i]] + v[i]}
```

**注意等式最后一行，咋看和01背包一样，实际上区别在于`dp[i + 1][]`, 01背包中为`dp[i][]`.** 此时时间复杂度简化为 $$O(nW)$$. 和 01 背包的递推关系区别在于第 i 件珠宝是否可以重复取。

## 扩展

以上我们只是求得了最终的最大获利，假如还需要输出选择了哪些项如何破？

以普通的01背包为例，如果某元素被选中，那么其必然满足`w[i] > j`且大于之前的`dp[i][j]`, 这还只是充分条件，因为有可能被后面的元素代替。保险起见，我们需要跟踪所有可能满足条件的项，然后反向计算有可能满足条件的元素，有可能最终输出不止一项。

### Java

```java
import java.util.*;

public class Backpack {
    // 01 backpack with small datasets(O(nW), W is small)
    public static int backpack(int W, int[] w, int[] v, boolean[] itemTake) {
        int N = w.length;
        int[][] dp = new int[N + 1][W + 1];
        boolean[][] matrix = new boolean[N + 1][W + 1];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j <= W; j++) {
                if (w[i] > j) {
                    // backpack cannot hold w[i]
                    dp[i + 1][j] = dp[i][j];
                } else {
                    dp[i + 1][j] = Math.max(dp[i][j], dp[i][j - w[i]] + v[i]);
                    // pick item i and get value j
                    matrix[i][j] = (dp[i][j - w[i]] + v[i] > dp[i][j]);
                }
            }
        }

        // determine which items to take
        for (int i = N - 1, j = W; i >= 0; i--) {
            if (matrix[i][j]) {
                itemTake[i] = true;
                j -= w[i];
            } else {
                itemTake[i] = false;
            }
        }

        return dp[N][W];
    }

    // 01 backpack with big datasets(O(n\sigma{v}), W is very big)
    public static int backpack2(int W, int[] w, int[] v) {
        int N = w.length;
        // sum of value array
        int V = 0;
        for (int i : v) {
            V += i;
        }
        // initialize
        int[][] dp = new int[N + 1][V + 1];
        for (int[] i : dp) {
            // should avoid overflow for dp[i][j - v[i]] + w[i]
            Arrays.fill(i, Integer.MAX_VALUE >> 1);
        }
        dp[0][0] = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j <= V; j++) {
                if (v[i] > j) {
                    // value[i] > j
                    dp[i + 1][j] = dp[i][j];
                } else {
                    // should avoid overflow for dp[i][j - v[i]] + w[i]
                    dp[i + 1][j] = Math.min(dp[i][j], dp[i][j - v[i]] + w[i]);
                }
            }
        }

        // search for the largest i dp[N][i] <= W
        for (int i = V; i >= 0; i--) {
            // if (dp[N][i] <= W) return i;
            if (dp[N][i] <= W) return i;
        }
        return 0;
    }

    // repeated backpack
    public static int backpack3(int W, int[] w, int[] v) {
        int N = w.length;
        int[][] dp = new int[N + 1][W + 1];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j <= W; j++) {
                if (w[i] > j) {
                    // backpack cannot hold w[i]
                    dp[i + 1][j] = dp[i][j];
                } else {
                    dp[i + 1][j] = Math.max(dp[i][j], dp[i + 1][j - w[i]] + v[i]);
                }
            }
        }

        return dp[N][W];
    }

    public static void main(String[] args) {
        int[] w1 = new int[]{2, 1, 3, 2};
        int[] v1 = new int[]{3, 2, 4, 2};
        int W1 = 5;
        boolean[] itemTake = new boolean[w1.length + 1];
        System.out.println("Testcase for 01 backpack.");
        int bp1 = backpack(W1, w1, v1, itemTake); // bp1 should be 7
        System.out.println("Maximum value: " + bp1);
        for (int i = 0; i < itemTake.length; i++) {
            if (itemTake[i]) {
                System.out.println("item " + i + ", weight " + w1[i] + ", value " + v1[i]);
            }
        }

        System.out.println("Testcase for 01 backpack with large W.");
        int bp2 = backpack2(W1, w1, v1); // bp2 should be 7
        System.out.println("Maximum value: " + bp2);

        int[] w3 = new int[]{3, 4, 2};
        int[] v3 = new int[]{4, 5, 3};
        int W3 = 7;
        System.out.println("Testcase for repeated backpack.");
        int bp3 = backpack3(W3, w3, v3); // bp3 should be 10
        System.out.println("Maximum value: " + bp3);
    }
}
```

## Reference

- 《挑战程序设计竞赛》第二章
- Chapter 6.4 Knapsack *Algorithm - S. Dasgupta*
- [0019算法笔记——【动态规划】0-1背包问题 - liufeng_king的专栏](http://blog.csdn.net/liufeng_king/article/details/8683136)
- [崔添翼 § 翼若垂天之云 › 《背包问题九讲》2.0 alpha1](http://cuitianyi.com/blog/%E3%80%8A%E8%83%8C%E5%8C%85%E9%97%AE%E9%A2%98%E4%B9%9D%E8%AE%B2%E3%80%8B2-0-alpha1/)
- [Knapsack.java](http://introcs.cs.princeton.edu/java/96optimization/Knapsack.java.html)
