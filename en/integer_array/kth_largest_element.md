# Kth Largest Element in an Array

Tags: Quick Sort, Divide and Conquer, Medium

## Question

- leetcode: [(215) Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- lintcode: [(5) Kth Largest Element](http://www.lintcode.com/en/problem/kth-largest-element/)

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

## Solution

Trail and error: Comparison-based sorting algorithms don't work because they incur ***O(n2)*** time complexity. Neither does Radix Sort which requires the elements to be in a certain range. In fact, Quick Sort is the answer to `kth largest` problems ([Here](http://algorithm.yuanbin.me/zh-hans/basics_sorting/quick_sort.html) are code templates of quick sort).

By quick sorting, we get the final index of a pivot. And by comparing that index with `K`, we decide which side (the greater or the smaller) of the pivot to recurse on.

### Java - Recursion

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
        int tmp = nums[i]; nums[i] = nums[j]; nums[j] = tmp;
    }
}
```

### Src Code Analysis

Two cases when the recursion ceases:
a. left bound equals right bound;
b. final index of pivot equals K.

Since 'Kth **largest**' is wanted, numbers greater than pivot are placed to the left and numbers smaller to the right, which is a little different with typical quick sort code.

### Java - Iteration

Recursive code is easier to read than to write, and it demands some experience and skill. Here is an iterative implementation.

```
class Solution {
    public int findKthLargest(int[] A, int k) {
        if (A == null || A.length == 0 || k < 0 || k > A.length) {
            return -1;
        }

        int lo = 0, hi = A.length - 1;
        while (lo <= hi) {
            int idx = partition(A, lo, hi);
            if (idx == k - 1) {
                return A[idx];
            } else if (idx < k - 1) {
                lo = idx + 1;
            } else {
                hi = idx - 1;
            }
        }

        return -1;
    }

    private int partition(int[] A, int lo, int hi) {
        int pivot = A[lo], i = lo + 1, j = hi;
        while (i <= j) {
            while (i <= j && A[i] > pivot) {
                i++;
            }
            while (i <= j && A[j] <= pivot) {
                j--;
            }
            if (i < j) {
                swap(A, i, j);
            }
        }
        swap(A, lo, j);

        return j;
    }

    private void swap(int[] A, int i, int j) {
        int tmp = A[i];
        A[i] = A[j];
        A[j] = tmp;
    }
}
```

### Src Code Analysis

The `while` loop in `findKthLargest` is very much like that in `binary search`. And `partition` method is just the same as quick sort partition.

### Complexity

Time Complexity. Worse case (when the array is sorted): ***n + n - 1 + ... + 1 = O(n^2)*** . Amortized complexity: ***n + n/2 + n/4 + ... + 1 = O(2n)=O(n)*** .

Space complexity is ***O(1)*** .
