# Search - 搜索

## Binary Search - 二分查找

Question: [lintcode - (14) Binary Search](http://www.lintcode.com/en/problem/binary-search/)

> Binary search is a famous question in algorithm.

> For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.

> If the target number does not exist in the array, return -1.

> **Example**

> If the array is [1, 2, 3, 3, 4, 5, 10], for given target 3, return 2.

> **Challenge**

> If the count of numbers is bigger than `MAXINT`, can your code work properly?

题解：

对于已排序升序数组，使用二分查找可满足复杂度要求，注意数组中可能有重复值。

```
class Solution {
    /**
     * @param nums: The integer array.
     * @param target: Target to find.
     * @return: The first position of target. Position starts from 0.
     */
    public int binarySearch(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return -1;
        }
        
        int start = 0;
        int end = nums.length - 1;
        int mid;
        while (start + 1 < end) {
            mid = start + (end - start) / 2; // avoid overflow when (end + start)
            if (target < nums[mid]) {
                end = mid;
            } else if (target > nums[mid]) {
                start = mid;
            } else if (target == nums[mid]) {
                end = mid;
            }
        }
        
        if (nums[start] == target) {
            return start;
        }
        if (nums[end] == target) {
            return end;
        }

        return -1;
    }
}
```

源码分析：

1. 首先对输入做异常处理，数组为空或者长度为0
2. 初始化 `start, end, mid`三个变量，注意mid的求值方法，可以防止两个整型值相加时溢出
3. **使用迭代而不是递归**进行二分查找

## Reference

- [[NineChap 2.1] Binary Search - Woodstock Blog](http://okckd.github.io/blog/2014/06/08/NineChap-Binary-Search/)
- [九章算法 - binary search](http://www.ninechapter.com//solutions/binary-search/)