# Longest Increasing Continuous subsequence

## Source

- lintcode: [(397) Longest Increasing Continuous subsequence](http://www.lintcode.com/en/problem/longest-increasing-continuous-subsequence/)

### Problem

Give you an integer array (index from 0 to n-1, where n is the size of this array)，find the longest increasing continuous subsequence in this array. (The definition of the longest increasing continuous subsequence here can be from right to left or from left to right)

#### Example

For `[5, 4, 2, 1, 3]`, the LICS is `[5, 4, 2, 1]`, return 4.

For `[5, 1, 2, 3, 4]`, the LICS is `[1, 2, 3, 4]`, return 4.

#### Note

O(n) time and O(1) extra space.

## 题解

题目只要返回最大长度，注意此题中的连续递增指的是双向的，即可递增也可递减。简单点考虑可分两种情况，一种递增，另一种递减，跟踪最大递增长度，最后返回即可。也可以在一个 for 循环中搞定，只不过需要增加一布尔变量判断之前是递增还是递减。本题的动态规划不太明显，当然你也可以使用传统的动态规划辅助分析。

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

## Reference

- [Lintcode: Longest Increasing Continuous subsequence | codesolutiony](https://codesolutiony.wordpress.com/2015/05/25/lintcode-longest-increasing-continuous-subsequence/)
