# Kth Largest Element in an Array

Tags: Heap, Divide and Conquer, Medium

## Question

- leetcode: [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- lintcode: [Kth Largest Element](http://www.lintcode.com/en/problem/kth-largest-element/)

### Problem Statement

Find the **k**th largest element in an unsorted array. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

For example,  
Given `[3,2,1,5,6,4]` and k = 2, return 5.

**Note: **  
You may assume k is always valid, 1 ≤ k ≤ array's length.

**Credits:**  

Special thanks to [@mithmatt](https://leetcode.com/discuss/user/mithmatt) for
adding this problem and creating all test cases.

## 题解

找第 K 大数，基于比较的排序的方法时间复杂度为 $$O(n)$$, 数组元素无区间限定，故无法使用线性排序。由于只是需要找第 K 大数，这种类型的题通常需要使用快排的思想解决。[Quick Sort](http://algorithm.yuanbin.me/zh-hans/basics_sorting/quick_sort.html) 总结了一些经典模板。这里比较基准值最后的位置的索引值和 K 的大小关系即可递归求解。

### Java

```java
public class Solution {
    public int findKthLargest(int[] nums, int k) {
        if (nums == null || nums.length == 0) {
            return Integer.MIN_VALUE;
        }

        int kthLargest = qSort(nums, 0, nums.length - 1, k);
        return kthLargest;
    }

    private int qSort(int[] nums, int left, int right, int k) {
        if (left >= right) {
            return nums[right];
        }

        int m = left;
        for (int i = left + 1; i <= right; i++) {
            if (nums[i] > nums[left]) {
                m++;
                swap(nums, m, i);
            }
        }
        swap(nums, m, left);

        if (k == m + 1) {
            return nums[m];
        } else if (k > m + 1) {
            return qSort(nums, m + 1, right, k);
        } else {
            return qSort(nums, left, m - 1, k);
        }
    }

    private void swap(int[] nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
```

### 源码分析

递归的终止条件有两个，一个是左边界的值等于右边界(实际中其实不会有 l > u), 另一个则是索引值 `m + 1 == k`.
这里找的是第 K 大数，故为降序排列，for 循环中使用`nums[i] > nums[left]` 而不是小于号。

### 复杂度分析

最坏情况下需要遍历 $$ n + n - 1 + ... + 1 = O(n^2)$$, 平均情况下 $$n + n/2 + n/4 + ... + 1 = O(2n)=O(n)$$. 故平均情况时间复杂度为 $$O(n)$$. 交换数组的值时使用了额外空间，空间复杂度 $$O(1)$$.
