# Maximum Subarray II

## Question

- lintcode: [(42) Maximum Subarray II](http://www.lintcode.com/en/problem/maximum-subarray-ii/)

```
Given an array of integers,
find two non-overlapping subarrays which have the largest sum.

The number in each subarray should be contiguous.

Return the largest sum.

Example
For given [1, 3, -1, 2, -1, 2],
the two subarrays are [1, 3] and [2, -1, 2] or [1, 3, -1, 2] and [2],
they both have the largest sum 7.

Note
The subarray should contain at least one number

Challenge
Can you do it in time complexity O(n) ?
```

## 题解

严格来讲这道题这道题也可以不用动规来做，这里还是采用经典的动规解法。[Maximum Subarray](http://algorithm.yuanbin.me/zh-hans/dynamic_programming/maximum_subarray.html) 中要求的是数组中最大子数组和，这里是求不相重叠的两个子数组和的和最大值，做过买卖股票系列的题的话这道题就非常容易了，既然我们已经求出了单一子数组的最大和，那么我们使用隔板法将数组一分为二，分别求这两段的最大子数组和，求相加后的最大值即为最终结果。隔板前半部分的最大子数组和很容易求得，但是后半部分难道需要将索引从0开始依次计算吗？NO!!! 我们可以采用从后往前的方式进行遍历，这样时间复杂度就大大降低了。

### Java

```java
public class Solution {
    /**
     * @param nums: A list of integers
     * @return: An integer denotes the sum of max two non-overlapping subarrays
     */
    public int maxTwoSubArrays(ArrayList<Integer> nums) {
        // -1 is not proper for illegal input
        if (nums == null || nums.isEmpty()) return -1;

        int size = nums.size();
        // get max sub array forward
        int[] maxSubArrayF = new int[size];
        forwardTraversal(nums, maxSubArrayF);
        // get max sub array backward
        int[] maxSubArrayB = new int[size];
        backwardTraversal(nums, maxSubArrayB);
        // get maximum subarray by iteration
        int maxTwoSub = Integer.MIN_VALUE;
        for (int i = 0; i < size - 1; i++) {
            // non-overlapping
            maxTwoSub = Math.max(maxTwoSub, maxSubArrayF[i] + maxSubArrayB[i + 1]);
        }

        return maxTwoSub;
    }

    private void forwardTraversal(List<Integer> nums, int[] maxSubArray) {
        int sum = 0, minSum = 0, maxSub = Integer.MIN_VALUE;
        int size = nums.size();
        for (int i = 0; i < size; i++) {
            minSum = Math.min(minSum, sum);
            sum += nums.get(i);
            maxSub = Math.max(maxSub, sum - minSum);
            maxSubArray[i] = maxSub;
        }
    }

    private void backwardTraversal(List<Integer> nums, int[] maxSubArray) {
        int sum = 0, minSum = 0, maxSub = Integer.MIN_VALUE;
        int size = nums.size();
        for (int i = size - 1; i >= 0; i--) {
            minSum = Math.min(minSum, sum);
            sum += nums.get(i);
            maxSub = Math.max(maxSub, sum - minSum);
            maxSubArray[i] = maxSub;
        }
    }
}
```

### 源码分析

前向搜索和逆向搜索我们使用私有方法实现，可读性更高。注意是求非重叠子数组和，故求`maxTwoSub`时i 的范围为`0, size - 2`, 前向数组索引为 i, 后向索引为 i + 1.

### 复杂度分析

前向和后向搜索求得最大子数组和，时间复杂度 $$O(2n)=O(n)$$, 空间复杂度 $$O(n)$$. 遍历子数组和的数组求最终两个子数组和的最大值，时间复杂度 $$O(n)$$. 故总的时间复杂度为 $$O(n)$$, 空间复杂度 $$O(n)$$.
