# First Position of Target

## Question

- lintcode: [First Position of Target](http://www.lintcode.com/en/problem/first-position-of-target)

### Problem Statement

For a given sorted array (ascending order) and a `target` number, find the
first index of this number in `O(log n)` time complexity.

If the target number does not exist in the array, return `-1`.

#### Example

If the array is `[1, 2, 3, 3, 4, 5, 10]`, for given target `3`, return `2`.

#### Challenge

If the count of numbers is bigger than $$2^{32}$$, can your code work properly?

## 题解

对于已排序升序(升序)数组，使用二分查找可满足复杂度要求，注意数组中可能有重复值，所以需要使用类似`lower_bound`中提到的方法。

### Java

```java
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

        int start = -1, end = nums.length;
        int mid;
        while (start + 1 < end) {
            // avoid overflow when (end + start)
            mid = start + (end - start) / 2;
            if (nums[mid] < target) {
                start = mid;
            } else {
                end = mid;
            }
        }

        if (end == nums.length || nums[end] != target) {
            return -1;
        } else {
            return end;
        }
    }
}

```

### 源码分析

1. 首先对输入做异常处理，数组为空或者长度为0。
2. 初始化 `start, end, mid`三个变量，这里`start`初始化为`-1`主要是考虑到`end`为`1`。注意mid的求值方法，可以防止两个整型值相加时溢出。
3. **使用迭代而不是递归**进行二分查找，因为工程中递归写法存在潜在溢出的可能。
4. while终止条件应为`start + 1 < end`而不是`start <= end`，`start == end`时可能出现死循环。**即循环终止条件是相邻或相交元素时退出。**由于这里初始化时`start < end`，所以一定是`start + 1 == end`时退出循环。
5. 迭代终止时有两种情况，一种是在原数组中找到了，这种情况下一定是`end`, 因为`start`的更新只在`nums[mid] < target`.
6. 最后判断`end`和`target`的关系，先排除`end`为数组长度这种会引起越界的情况，然后再判断和目标值是否相等。

### 复杂度分析

时间复杂度 $$O(\log n)$$, 空间复杂度 $$(1)$$.
对于题中的 follow up, Java 中数组不允许使用 long 型，如果使用 long 型，那么数组大小可大 17GB 之巨！！几乎没法用。

## Reference

- 《挑战程序设计竞赛》3.1节
