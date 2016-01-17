# Longest Increasing Continuous subsequence

## Question

- lintcode: [(397) Longest Increasing Continuous subsequence](http://www.lintcode.com/en/problem/longest-increasing-continuous-subsequence/)

### Problem Statement

Give you an integer array (index from 0 to n-1, where n is the size of this array)，find the longest increasing continuous subsequence in this array. (The definition of the longest increasing continuous subsequence here can be from right to left or from left to right)

#### Example

For `[5, 4, 2, 1, 3]`, the LICS is `[5, 4, 2, 1]`, return 4.

For `[5, 1, 2, 3, 4]`, the LICS is `[1, 2, 3, 4]`, return 4.

#### Note

O(n) time and O(1) extra space.

## 题解1

题目只要返回最大长度，注意此题中的连续递增指的是双向的，即可递增也可递减。简单点考虑可分两种情况，一种递增，另一种递减，跟踪最大递增长度，最后返回即可。也可以在一个 for 循环中搞定，只不过需要增加一布尔变量判断之前是递增还是递减。

### Java - two for loop

```java
public class Solution {
    /**
     * @param A an array of Integer
     * @return  an integer
     */
    public int longestIncreasingContinuousSubsequence(int[] A) {
        if (A == null || A.length == 0) return 0;

        int lics = 1, licsMax = 1, prev = A[0];
        // ascending order
        for (int a : A) {
            lics = (prev < a) ? lics + 1 : 1;
            licsMax = Math.max(licsMax, lics);
            prev = a;
        }
        // reset
        lics = 1;
        prev = A[0];
        // descending order
        for (int a : A) {
            lics = (prev > a) ? lics + 1 : 1;
            licsMax = Math.max(licsMax, lics);
            prev = a;
        }

        return licsMax;
    }
}
```

### Java - one for loop

```java
public class Solution {
    /**
     * @param A an array of Integer
     * @return  an integer
     */
    public int longestIncreasingContinuousSubsequence(int[] A) {
        if (A == null || A.length == 0) return 0;

        int start = 0, licsMax = 1;
        boolean ascending = false;
        for (int i = 1; i < A.length; i++) {
            // ascending order
            if (A[i - 1] < A[i]) {
                if (!ascending) {
                    ascending = true;
                    start = i - 1;
                }
            } else if (A[i - 1] > A[i]) {
            // descending order
                if (ascending) {
                    ascending = false;
                    start = i - 1;
                }
            } else {
                start = i - 1;
            }
            licsMax = Math.max(licsMax, i - start + 1);
        }

        return licsMax;
    }
}
```

### 源码分析

使用两个 for 循环时容易在第二次循环忘记重置。使用一个 for 循环时使用下标来计数较为方便。

### 复杂度分析

时间复杂度 $$O(n)$$, 空间复杂度 $$O(1)$$.

## 题解2 - 动态规划

除了题解1 中分两种情况讨论外，我们还可以使用动态规划求解。状态转移方程容易得到——要么向右增长，要么向左增长。相应的状态`dp[i]`即为从索引 i 出发所能得到的最长连续递增子序列。这样就避免了分两个循环处理了，这种思想对此题的 follow up 有特别大的帮助。

### Java

```java
public class Solution {
    /**
     * @param A an array of Integer
     * @return  an integer
     */
    public int longestIncreasingContinuousSubsequence(int[] A) {
        if (A == null || A.length == 0) return 0;

        int lics = 0;
        int[] dp = new int[A.length];
        for (int i = 0; i < A.length; i++) {
            if (dp[i] == 0) {
                lics = Math.max(lics, dfs(A, i, dp));
            }
        }

        return lics;
    }

    private int dfs(int[] A, int i, int[] dp) {
        if (dp[i] != 0) return dp[i];

        // increasing from xxx to left, right
        int left = 0, right = 0;
        // increasing from right to left
        if (i > 0 && A[i - 1] > A[i]) left = dfs(A, i - 1, dp);
        // increasing from left to right
        if (i + 1 < A.length && A[i + 1] > A[i]) right = dfs(A, i + 1, dp);

        dp[i] = 1 + Math.max(left, right);
        return dp[i];
    }
}
```

### 源码分析

dfs 中使用记忆化存储避免重复递归，分左右两个方向递增，最后取较大值。这种方法对于数组长度较长时栈会溢出。

### 复杂度分析

时间复杂度 $$O(n)$$, 空间复杂度 $$(n)$$.

## Reference

- [Lintcode: Longest Increasing Continuous subsequence | codesolutiony](https://codesolutiony.wordpress.com/2015/05/25/lintcode-longest-increasing-continuous-subsequence/)
