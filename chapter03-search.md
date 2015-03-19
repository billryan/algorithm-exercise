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

源码分析：

1. 首先对输入做异常处理，数组为空或者长度为0
2. 初始化 `start, end, mid`三个变量，注意mid的求值方法，可以防止两个整型值相加时溢出
3. **使用迭代而不是递归**进行二分查找
4. while终止条件应为`start + 1 < end`而不是`start <= end`，`start == end`时可能出现死循环
5. 迭代终止时target应为start或者end中的一个
6. 赋值语句`end = mid`有两个条件是相同的，为何不写到一起？程序执行时可能还要慢些？

## Search for a Range

Question: [lintcode - (14) Binary Search](http://www.lintcode.com/en/problem/binary-search/)

题解：

由上题二分查找可找到满足条件的左边界，因此只需要再将右边界找出即可。注意到在`(target == nums[mid]`时赋值语句为`end = mid`，将其改为`start = mid`即可找到右边界，解毕。

```
public class Solution {
    /** 
     *@param A : an integer sorted array
     *@param target :  an integer to be inserted
     *return : a list of length 2, [index1, index2]
     */
    public ArrayList<Integer> searchRange(ArrayList<Integer> A, int target) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        int start, end, mid;
        result.add(-1);
        result.add(-1);
        
        if (A == null || A.size() == 0) {
            return result;
        }
        
        // search for left bound
        start = 0;
        end = A.size() - 1;
        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (A.get(mid) == target) {
                end = mid; // set end = mid to find the minimum mid
            } else if (A.get(mid) > target) {
                end = mid;
            } else {
                start = mid;
            }
        }
        if (A.get(start) == target) {
            result.set(0, start);
        } else if (A.get(end) == target) {
            result.set(0, end);
        } else {
            return result;
        }
        
        // search for right bound
        start = 0;
        end = A.size() - 1;
        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (A.get(mid) == target) {
                start = mid; // set start = mid to find the maximum mid
            } else if (A.get(mid) > target) {
                end = mid;
            } else {
                start = mid;
            }
        }
        if (A.get(end) == target) {
            result.set(1, end);
        } else if (A.get(start) == target) {
            result.set(1, start);
        } else {
            return result;
        }
        
        return result;
        // write your code here
    }
}
```

源码分析：

1. 首先对输入做异常处理，数组为空或者长度为0
2. 初始化 `start, end, mid`三个变量，注意mid的求值方法，可以防止两个整型值相加时溢出
3. **使用迭代而不是递归**进行二分查找
4. while终止条件应为`start + 1 < end`而不是`start <= end`，`start == end`时可能出现死循环
5. 先求左边界，迭代终止时先判断`A.get(start) == target`，再判断`A.get(end) == target`，因为迭代终止时target必取start或end中的一个，而end又大于start，取左边界即为start.
6. 再求右边界，迭代终止时先判断`A.get(end) == target`，再判断`A.get(start) == target`

## Search Insert Position

Question: [(60) Search Insert Position](http://www.lintcode.com/en/problem/search-insert-position/)

题解：

由最原始的二分查找可找到不小于目标整数的最小下标。返回此下标即可。

```
public class Solution {
    /** 
     * param A : an integer sorted array
     * param target :  an integer to be inserted
     * return : an integer
     */
    public int searchInsert(int[] A, int target) {
        if (A == null) {
            return -1;
        }
        if (A.length == 0) {
            return 0;
        }

        int start = 0, end = A.length - 1;
        int mid;

        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (A[mid] == target) {
                return mid; // no duplicates, if not `end = target;`
            } else if (A[mid] < target) {
                start = mid;
            } else {
                end = mid;
            }
        }

        if (A[start] >= target) {
            return start;
        } else if (A[end] >= target) {
            return end; // in most cases
        } else {
            return end + 1; // A[end] < target;
        }
    }
}
```

源码分析：已在源码处注释

## Reference

- [[NineChap 2.1] Binary Search - Woodstock Blog](http://okckd.github.io/blog/2014/06/08/NineChap-Binary-Search/)
- [九章算法 - binary search](http://www.ninechapter.com//solutions/binary-search/)