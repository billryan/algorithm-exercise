# Continuous Subarray Sum

## Question

- lintcode: [(402) Continuous Subarray Sum](http://www.lintcode.com/en/problem/continuous-subarray-sum/)

### Problem Statement

Given an integer array, find a continuous subarray where the sum of numbers is
the biggest. Your code should return the index of the first number and the
index of the last number. (If their are duplicate answer, return anyone)

#### Example

Give `[-3, 1, 3, -3, 4]`, return `[1,4]`.

## 题解

和题 [Maximum Subarray](http://algorithm.yuanbin.me/zh-hans/dynamic_programming/maximum_subarray.html) 几乎一模一样，只是返回值要求不一样。由于需要返回区间索引值，那么显然需要额外变量记录区间起止处。若使用题解2中提到的`sum - minSum`的区间和更新方式，索引终止处容易得知是`sum - minSum > maxSub`时的`i`, 问题是索引起始处如何确定。容易得知索引起始处如果更新，必然在`minSum > sum`时，但问题在于满足此条件的可能不止一处，所以我们需要先记录这个索引值并在`sum - minSum > maxSub`时判定索引终止值是否大于索引起始值，不小于则更新。

此题难以一次 bug-free, 需要小心更新索引值。

### Java

```java
public class Solution {
    /**
     * @param A an integer array
     * @return  A list of integers includes the index of the first number and the index of the last number
     */
    public ArrayList<Integer> continuousSubarraySum(int[] A) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        if (A == null || A.length == 0) return result;

        int sum = 0, minSum = 0, maxSub = Integer.MIN_VALUE;
        int first = 0, last = 0;
        int first2 = 0; // candidate for first
        for (int i = 0; i < A.length; i++) {
            if (minSum > sum) {
                minSum = sum;
                first2 = i;
            }
            sum += A[i];
            if (sum - minSum > maxSub) {
                maxSub = sum - minSum;
                last = i;
                // update first if valid
                if (first2 <= last) first = first2;
            }
        }

        result.add(first);
        result.add(last);
        return result;
    }
}
```

### 源码分析

除了最后要求的`first`和`last`, 我们还需要引入`first2`作为`first`可能的候选变量值。

### 复杂度分析

略
