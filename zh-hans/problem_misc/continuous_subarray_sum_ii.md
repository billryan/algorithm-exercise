# Continuous Subarray Sum II

## Question

- lintcode: [(403) Continuous Subarray Sum II](http://www.lintcode.com/en/problem/continuous-subarray-sum-ii/)
- [Maximum circular subarray sum - GeeksforGeeks](http://www.geeksforgeeks.org/maximum-contiguous-circular-sum/)

### Problem Statement

Given an integer array, find a continuous rotate subarray where the sum of
numbers is the biggest. Your code should return the index of the first number
and the index of the last number. (If their are duplicate answer, return
anyone. The answer can be rorate array or non- rorate array)

#### Example

Give `[3, 1, -100, -3, 4]`, return `[4,1]`.

## 题解

题 [Continuous Subarray Sum](http://algorithm.yuanbin.me/zh-hans/problem_misc/continuous_subarray_sum.html) 的 follow up, 这道题 AC 率极低，真是磨人的小妖精。在上题的基础上容易想到可以将`first`和`last`分四种情况讨论，然后再逆向求大于0的最大和即可，但是这种想法忽略了一种情况——旋转后的最大值可能由两段子数组和构成，而这种情况如果用上题的解法则会被忽略。

所以这道题的正确解法不是分`first`和`last`四种情况讨论，而是利用旋转数组的特性。第一种情况，无论怎么拼接原数组中的数组和都无法大于最大的单一数组和；第二种情况则相反。所以现在问题的关键则转化为怎么求第二种情况。首先可以明确一点，最终得到的数组和索引必须连续（含首尾相接）。也就是说情况二一旦出现，则我们可以将原数组中挖空一小段，现在问题来了：到底要挖掉多少元素？

**我们的目标是使得挖掉后的元素值最大。**由于分段求解不容易（被隔开），但是被挖掉的元素索引是挨着的！正难则反！由于数组的总和是一定的，那么我们只要求得被挖掉部分元素的最小值即可得两边子数组的最大值！最后判断两个最大值孰大孰小就可以了。

### Java

```java
public class Solution {
    /**
     * @param A an integer array
     * @return  A list of integers includes the index of the first number and the index of the last number
     */
    public ArrayList<Integer> continuousSubarraySumII(int[] A) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        if (A == null || A.length == 0) return result;
        // maximal subarray sum
        ArrayList<Integer> sub1 = subSum(A, 1);
        // minimal subarray sum
        ArrayList<Integer> sub2 = subSum(A, -1);
        int first = 0, last = 0;
        if (sub1.get(3) - sub2.get(2) > sub1.get(2)) {
            last = sub2.get(0) - 1;
            first = sub2.get(1) + 1;
        } else {
            first = sub1.get(0);
            last = sub1.get(1);
        }
        // corner case(all elements are negtive)
        if (last == -1 && first == A.length) {
            first = sub1.get(0);
            last = sub1.get(1);
        }

        result.add(first);
        result.add(last);
        return result;
    }

    private ArrayList<Integer> subSum(int[] A, int sign) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        // find the max/min subarray sum from [0...A.length]
        int sum = 0, minSum = 0, maxSub = Integer.MIN_VALUE;
        if (sign == -1) maxSub = Integer.MAX_VALUE;
        int first = 0, last = 0;
        int first2 = 0; // candidate for first
        for (int i = 0; i < A.length; i++) {
            if (sign * minSum > sign * sum) {
                minSum = sum;
                first2 = i;
            }
            sum += A[i];
            if (sign * (sum - minSum) > sign * maxSub) {
                maxSub = sum - minSum;
                last = i;
                // update first if valid
                if (first2 <= last) first = first2;
            }
        }
        result.add(first);
        result.add(last);
        result.add(maxSub);
        result.add(sum);
        return result;
    }
}
```

### 源码分析

由于既需要求最大子数组和，也需要求最小子数组和，我们将这一部分写成一私有方法，并加入`sign`控制符号。如果两段子数组和大于一段子数组和时，新的`first`和`last`正好相反。且在数组全为负时需要排除，直接使用单一子数组和最大的情况。

### 复杂度分析

遍历两次数组，时间复杂度 $$O(n)$$, 使用了部分额外 List, 空间复杂度 $$O(1)$$.

## Reference

- [CC150+Leetcode Continuous Subarray Sum II](http://meetqun.com/thread-9856-1-1.html)
