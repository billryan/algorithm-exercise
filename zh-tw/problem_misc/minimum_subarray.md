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

## 題解

題目 [Maximum Subarray](http://algorithm.yuanbin.me/zh-hans/dynamic_programming/maximum_subarray.html) 的變形，使用區間和容易理解和實現。

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

### 源碼分析

略

### 複雜度分析

略
