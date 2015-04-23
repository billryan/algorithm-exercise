# Search in Rotated Sorted Array

对于旋转数组的分析可使用画图的方法，如下图所示，升序数组经旋转后可能为如下两种形式。

![Rotated Array](../images/rotated_array.png)

## Source

- lintcode: [(62) Search in Rotated Sorted Array](http://www.lintcode.com/en/problem/search-in-rotated-sorted-array/)

```
Suppose a sorted array is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
Example
For [4, 5, 1, 2, 3] and target=1, return 2

For [4, 5,1, 2, 3] and target=0, return -1
```

### 题解

对于有序数组，使用二分搜索比较方便。分析题中的数组特点，旋转后初看是乱序数组，但仔细一看其实里面是存在两段有序数组的。因此该题可转化为如何找出旋转数组中的局部有序数组，并使用二分搜索解之。结合实际数组在纸上分析较为方便。

#### C++

```c++
/**
 * 本代码fork自
 * http://www.jiuzhang.com/solutions/search-in-rotated-sorted-array/
 */
class Solution {
    /**
     * param A : an integer ratated sorted array
     * param target :  an integer to be searched
     * return : an integer
     */
public:
    int search(vector<int> &A, int target) {
        if (A.empty()) {
            return -1;
        }

        vector<int>::size_type start = 0;
        vector<int>::size_type end = A.size() - 1;
        vector<int>::size_type mid;

        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (target == A[mid]) {
                return mid;
            }
            if (A[start] < A[mid]) {
                // situation 1, numbers between start and mid are sorted
                if (A[start] <= target && target < A[mid]) {
                    end = mid;
                } else {
                    start = mid;
                }
            } else {
                // situation 2, numbers between mid and end are sorted
                if (A[mid] < target && target <= A[end]) {
                    start = mid;
                } else {
                    end = mid;
                }
            }
        }

        if (A[start] == target) {
            return start;
        }
        if (A[end] == target) {
            return end;
        }
        return -1;
    }
};
```

#### 源码分析

1. 若`target == A[mid]`，索引找到，直接返回
2. 寻找局部有序数组，分析`A[mid]`和两段有序的数组特点，由于旋转后前面有序数组最小值都比后面有序数组最大值大。故若`A[start] < A[mid]`成立，则start与mid间的元素必有序（要么是前一段有序数组，要么是后一段有序数组，还有可能是未旋转数组）。
3. 接着在有序数组`A[start]~A[mid]`间进行二分搜索，但能在`A[start]~A[mid]`间搜索的前提是`A[start] <= target <= A[mid]`。
4. 接着在有序数组`A[mid]~A[end]`间进行二分搜索，注意前提条件。
5. 搜索完毕时索引若不是mid或者未满足while循环条件，则测试A[start]或者A[end]是否满足条件。
6. 最后若未找到满足条件的索引，则返回-1.

## Search in Rotated Sorted Array II

## Source

- lintcode: [(63) 搜索旋转排序数组 II](http://www.lintcode.com/zh-cn/problem/search-in-rotated-sorted-array-ii/)

```
跟进“搜索旋转排序数组”，假如有重复元素又将如何？

是否会影响运行时间复杂度？

如何影响？

为何会影响？

写出一个函数判断给定的目标值是否出现在数组中。

样例
给出[3,4,4,5,7,0,1,2]和target=4，返回 true
```

### 题解

仔细分析此题和之前一题的不同之处，前一题我们利用`A[start] < A[mid]`这一关键信息，而在此题中由于有重复元素的存在，在`A[start] == A[mid]`时无法确定有序数组，此时只能依次递增start/递减end以缩小搜索范围，时间复杂度最差变为O(n)。

#### C++

```c++
class Solution {
    /**
     * param A : an integer ratated sorted array and duplicates are allowed
     * param target :  an integer to be search
     * return : a boolean
     */
public:
    bool search(vector<int> &A, int target) {
        if (A.empty()) {
            return false;
        }

        vector<int>::size_type start = 0;
        vector<int>::size_type end = A.size() - 1;
        vector<int>::size_type mid;

        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (target == A[mid]) {
                return true;
            }
            if (A[start] < A[mid]) {
                // situation 1, numbers between start and mid are sorted
                if (A[start] <= target && target < A[mid]) {
                    end = mid;
                } else {
                    start = mid;
                }
            } else if (A[start] > A[mid]) {
                // situation 2, numbers between mid and end are sorted
                if (A[mid] < target && target <= A[end]) {
                    start = mid;
                } else {
                    end = mid;
                }
            } else  {
                // increment start
                ++start;
            }
        }

        if (A[start] == target || A[end] == target) {
            return true;
        }
        return false;
    }
};
```

#### 源码分析

在`A[start] == A[mid]`时递增start序号即可。
