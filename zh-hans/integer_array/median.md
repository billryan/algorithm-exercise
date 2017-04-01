# Median

Tags: LintCode Copyright, Quick Sort, Array, Easy

## Question

- lintcode: [Median](http://www.lintcode.com/en/problem/median/)

### Problem Statement

Given a unsorted array with integers, find the median of it.

A median is the middle number of the array after it is sorted.

If there are even numbers in the array, return the `N/2`-th number after
sorted.

#### Example

Given `[4, 5, 1, 2, 3]`, return `3`.

Given `[7, 9, 4, 5]`, return `5`.

#### Challenge

$$O(n)$$ time.

## 题解

寻找未排序数组的中位数，简单粗暴的方法是先排序后输出中位数索引处的数，但是基于比较的排序算法的时间复杂度为 $$O(n \log n)$$, 不符合题目要求。线性时间复杂度的排序算法常见有计数排序、桶排序和基数排序，这三种排序方法的空间复杂度均较高，且依赖于输入数据特征（数据分布在有限的区间内），用在这里并不是比较好的解法。

由于这里仅需要找出中位数，即找出数组中前半个长度的较大的数，不需要进行完整的排序，说到这你是不是想到了快速排序了呢？快排的核心思想就是以基准为界将原数组划分为左小右大两个部分，用在这十分合适。快排的实现见 [Quick Sort](../basics_sorting/quick_sort.html), 由于调用一次快排后基准元素的最终位置是知道的，故递归的终止条件即为当基准元素的位置(索引)满足中位数的条件时(左半部分长度为原数组长度一半，无论奇偶均是如此)即返回最终结果。在数组长度确定后，我们可以直接套用 [K 大数](./kth_largest_element.html)的模板来解，即 K 为 (length + 1) / 2.

### Python

```python
class Solution:
    """
    @param nums: A list of integers.
    @return: An integer denotes the middle number of the array.
    """
    def median(self, nums):
        if not nums:
            return -1
        return self.kth(nums, 0, len(nums) - 1, (1 + len(nums)) / 2)

    def kth(self, nums, left, right, k):
        # if left >= right: return nums[right]

        m = left
        for i in xrange(left + 1, right + 1):
            if nums[i] < nums[left]:
                m += 1
                nums[m], nums[i] = nums[i], nums[m]

        # swap between m and l after partition, important!
        nums[m], nums[left] = nums[left], nums[m]

        if m + 1 == k:
            return nums[m]
        elif m + 1 > k:
            return self.kth(nums, left, m - 1, k)
        else:
            return self.kth(nums, m + 1, right, k)
```

### C++

```c++
class Solution {
public:
    /**
     * @param nums: A list of integers.
     * @return: An integer denotes the middle number of the array.
     */
    int median(vector<int> &nums) {
        if (nums.empty()) return 0;

        int len = nums.size();
        return kth(nums, 0, len - 1, (len + 1) / 2);
    }

private:
    int kth(vector<int> &nums, int left, int right, int k) {
        // if (left >= right) return nums[right];

        int m = left; // index m to track pivot
        for (int i = left + 1; i <= right; ++i) {
            if (nums[i] < nums[left]) {
                ++m;
                std::swap(nums[i], nums[m]);
            }
        }

        // swap with the pivot
        std::swap(nums[left], nums[m]);

        if (m + 1 == k) {
            return nums[m];
        } else if (m + 1 > k) {
            return kth(nums, left, m - 1, k);
        } else {
            return kth(nums, m + 1, right, k);
        }
    }
};
```

### Java

```java
public class Solution {
    /**
     * @param nums: A list of integers.
     * @return: An integer denotes the middle number of the array.
     */
    public int median(int[] nums) {
        if (nums == null || nums.length == 0) return -1;
        
        return kth(nums, 0, nums.length - 1, (nums.length + 1) / 2);
    }

    private int kth(int[] nums, int left, int right, int k) {
        // if (left >= right) return nums[right];

        int m = left;
        for (int i = left + 1; i <= right; i++) {
            if (nums[i] < nums[left]) {
                m++;
                swap(nums, i, m);
            }
        }
        // put pivot in the mid position
        swap(nums, left, m);

        if (k == m + 1) {
            return nums[m];
        } else if (k > m + 1) {
            return kth(nums, m + 1, right, k);
        } else {
            return kth(nums, left, m - 1, k);
        }
    }

    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
```

### 源码分析

以题目中给出的样例进行分析，k 传入的值可为`(len(nums) + 1) / 2`, 由于在 kth 入口处 left >= right 之前已经找到解，无需判断。

### 复杂度分析

和快排类似，这里也有最好情况与最坏情况，平均情况下，索引`m`每次都处于中央位置，即每次递归后需要遍历的数组元素个数减半，故总的时间复杂度为 $$O(n (1 + 1/2 + 1/4 + ...)) = O(2n)$$, 最坏情况下为平方。使用了临时变量，空间复杂度为 $$O(1)$$, 满足题目要求。
