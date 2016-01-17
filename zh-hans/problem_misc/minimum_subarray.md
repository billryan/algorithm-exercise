# Minimum Subarray

## Question

- lintcode: [(44) Minimum Subarray](http://www.lintcode.com/en/problem/minimum-subarray/)

```
Given an array of integers, find the subarray with smallest sum.

Return the sum of the subarray.

Example
For [1, -1, -2, 1], return -3

Note
The subarray should contain at least one integer.
```

## 题解

题 [Maximum Subarray](http://algorithm.yuanbin.me/zh-hans/dynamic_programming/maximum_subarray.html) 的变形，使用区间和容易理解和实现。

### Java

```java
public class Solution {
    /**
     * @param nums: a list of integers
     * @return: A integer indicate the sum of minimum subarray
     */
    public int minSubArray(ArrayList<Integer> nums) {
        if (nums == null || nums.isEmpty()) return -1;

        int sum = 0, maxSum = 0, minSub = Integer.MAX_VALUE;
        for (int num : nums) {
            maxSum = Math.max(maxSum, sum);
            sum += num;
            minSub = Math.min(minSub, sum - maxSum);
        }

        return minSub;
    }
}
```

### 源码分析

略

### 复杂度分析

略
