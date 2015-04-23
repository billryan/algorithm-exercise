# Binary Search - 二分查找

Question: [lintcode - (14) Binary Search](http://www.lintcode.com/en/problem/binary-search/)

```
Binary search is a famous question in algorithm.

For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.

If the target number does not exist in the array, return -1.

Example
If the array is [1, 2, 3, 3, 4, 5, 10], for given target 3, return 2.

Challenge
If the count of numbers is bigger than MAXINT, can your code work properly?
```

### 题解

对于已排序升序数组，使用二分查找可满足复杂度要求，注意数组中可能有重复值。

#### Java

```java
/**
 * 本代码fork自九章算法。没有版权欢迎转发。
 * http://www.jiuzhang.com//solutions/binary-search/
 */
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
            } else {
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

#### 源码分析

1. 首先对输入做异常处理，数组为空或者长度为0。
2. 初始化 `start, end, mid`三个变量，注意mid的求值方法，可以防止两个整型值相加时溢出。
3. **使用迭代而不是递归**进行二分查找，因为工程中递归写法存在潜在溢出的可能。
4. while终止条件应为`start + 1 < end`而不是`start <= end`，`start == end`时可能出现死循环。**即循环终止条件是相邻或相交元素时退出。**
5. 迭代终止时target应为start或者end中的一个——由上述循环终止条件有两个，具体谁先谁后视题目是找 first position or last position 而定。
6. 赋值语句`end = mid`有两个条件是相同的，可以选择写到一块。
7. 配合while终止条件`start + 1 < end`（相邻即退出）的赋值语句mid永远没有`+1`或者`-1`，这样不会死循环。
