# Binary Search - 二分搜索

二分搜索是一种在有序数组中寻找目标值的经典方法，也就是说使用前提是『有序数组』。非常简单的题中『有序』特征非常明显，但更多时候可能需要我们自己去构造『有序数组』。下面我们从最基本的二分搜索开始逐步深入。

## 模板一 - 从有序数组中寻找目标值插入索引

以 lintcode 上一道测试题 [search insert position](http://algorithm.yuanbin.me/zh-cn/binary_search/search_insert_position.html) 为例，题目要求寻找目标值在升序数组中插入的索引。我们先直接看代码。

### Java

```java
public class Solution {
    /**
     * param A : an integer sorted array
     * param target :  an integer to be inserted
     * return : an integer
     */
    public int searchInsert(int[] A, int target) {
        if (A == null || A.length == 0) {
            return -1;
        }

        int start = -1, end = A.length;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (A[mid] == target) {
                return mid; // no duplicates
            } else if (A[mid] < target) {
                start = mid;
            } else {
                end = mid;
            }
        }

	return start + 1;
    }
}
```

### 源码分析

以上二分搜索的模板有两个非常优雅的实现：

1. `while` 循环中 `start + 1 < end`, 而不是等号，因为取等号可能会引起死循环。初始化`start < end` 时，最后循环退出时一定有`start + 1 == end`.
2. `start` 和 `end` 的初始化，初始化为数组的两端以外，这种初始化方式比起`0` 和`nums.length - 1` 有不少优点，详述如下。

插入位置可以分三种典型情况：

1. 目标值在数组范围之内，最后返回值一定是`start + 1`
2. 目标值比数组最小值还小，此时`start` 一直为`-1`, 故最后返回`start + 1` 也没错，也可以将`-1` 理解为数组前一个更小的值
3. 目标值大于等于数组最后一个值，由于循环退出条件为`start + 1 == end`, 那么循环退出时一定有`start = A.length - 1`, 应该返回`start + 1`

综上所述，返回`start + 1`是非常优雅的实现。其实以上三种情况都可以统一为一种方式来理解，即索引`-1` 对应于数组前方一个非常小的数，索引`end` 即对应数组后方一个非常大的数，那么要插入的数就一定在`start` 和`end` 之间了。

**有时复杂的边界条件处理可以通过『补项』这种优雅的方式巧妙处理。**

## Reference

- 《挑战程序设计竞赛》
