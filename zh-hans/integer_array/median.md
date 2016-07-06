# Median

## Question

- lintcode: [(80) Median](http://www.lintcode.com/en/problem/median/)

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

由于这里仅需要找出中位数，即找出数组中前半个长度的较大的数，不需要进行完整的排序，说到这你是不是想到了快速排序了呢？快排的核心思想就是以基准为界将原数组划分为左小右大两个部分，用在这十分合适。快排的实现见 [Quick Sort](../basics_sorting/quick_sort.html), 由于调用一次快排后基准元素的最终位置是知道的，故递归的终止条件即为当基准元素的位置(索引)满足中位数的条件时(左半部分长度为原数组长度一半)即返回最终结果。由于函数原型中左右最小索引并不总是原数组的最小最大，故需要引入相对位置(长度)也作为其中之一的参数。若左半部分长度偏大，则下一次递归排除右半部分，反之则排除左半部分。

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
        return self.helper(nums, 0, len(nums) - 1, (1 + len(nums)) / 2)

    def helper(self, nums, l, u, size):
        if l >= u:
            return nums[u]

        m = l
        for i in xrange(l + 1, u + 1):
            if nums[i] < nums[l]:
                m += 1
                nums[m], nums[i] = nums[i], nums[m]

        # swap between m and l after partition, important!
        nums[m], nums[l] = nums[l], nums[m]

        if m - l + 1 == size:
            return nums[m]
        elif m - l + 1 > size:
            return self.helper(nums, l, m - 1, size)
        else:
            return self.helper(nums, m + 1, u, size - (m - l + 1))
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
        return helper(nums, 0, len - 1, (len + 1) / 2);
    }

private:
    int helper(vector<int> &nums, int l, int u, int size) {
        // if (l >= u) return nums[u];

        int m = l; // index m to track pivot
        for (int i = l + 1; i <= u; ++i) {
            if (nums[i] < nums[l]) {
                ++m;
                int temp = nums[i];
                nums[i] = nums[m];
                nums[m] = temp;
            }
        }

        // swap with the pivot
        int temp = nums[m];
        nums[m] = nums[l];
        nums[l] = temp;

        if (m - l + 1 == size) {
            return nums[m];
        } else if (m - l + 1 > size) {
            return helper(nums, l, m - 1, size);
        } else {
            return helper(nums, m + 1, u, size - (m - l + 1));
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
        if (nums == null) return -1;

        return helper(nums, 0, nums.length - 1, (nums.length + 1) / 2);
    }

    // l: lower, u: upper, m: median
    private int helper(int[] nums, int l, int u, int size) {
        if (l >= u) return nums[u];

        int m = l;
        for (int i = l + 1; i <= u; i++) {
            if (nums[i] < nums[l]) {
                m++;
                int temp = nums[m];
                nums[m] = nums[i];
                nums[i] = temp;
            }
        }
        // swap between array[m] and array[l]
        // put pivot in the mid
        int temp = nums[m];
        nums[m] = nums[l];
        nums[l] = temp;

        if (m - l + 1 == size) {
            return nums[m];
        } else if (m - l + 1 > size) {
            return helper(nums, l, m - 1, size);
        } else {
            return helper(nums, m + 1, u, size - (m - l + 1));
        }
    }
}
```

### 源码分析

以相对距离(长度)进行理解，递归终止步的条件一直保持不变(比较左半部分的长度)。

以题目中给出的样例进行分析，`size` 传入的值可为`(len(nums) + 1) / 2`, 终止条件为`m - l + 1 == size`, 含义为基准元素到索引为`l`的元素之间(左半部分)的长度(含)与`(len(nums) + 1) / 2`相等。若`m - l + 1 > size`, 即左半部分长度偏大，此时递归终止条件并未变化，因为`l`的值在下一次递归调用时并未改变，所以仍保持为`size`; 若`m - l + 1 < size`, 左半部分长度偏小，下一次递归调用右半部分，由于此时左半部分的索引值已变化，故`size`应改为下一次在右半部分数组中的终止条件`size - (m - l + 1)`, 含义为原长度`size`减去左半部分数组的长度`m - l + 1`.

P.S. 经 @l1xiao 提醒，也可直接将 size 固定，代码上更为简洁，置于个中缘由读者可先自行分析。

```
        if (m + 1 == size) {
            return nums[m];
        } else if (m + 1 > size) {
            return helper(nums, start, m - 1, size);
        } else {
            return helper(nums, m + 1, end, size);
        }
```

### 复杂度分析

和快排类似，这里也有最好情况与最坏情况，平均情况下，索引`m`每次都处于中央位置，即每次递归后需要遍历的数组元素个数减半，故总的时间复杂度为 $$O(n (1 + 1/2 + 1/4 + ...)) = O(2n)$$, 最坏情况下为平方。使用了临时变量，空间复杂度为 $$O(1)$$, 满足题目要求。
