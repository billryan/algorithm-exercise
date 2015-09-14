# Kth Largest Element

## Source

- leetcode: [Kth Largest Element in an Array | LeetCode OJ](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- lintcode: [(5) Kth Largest Element](http://www.lintcode.com/en/problem/kth-largest-element/)

```
Find K-th largest element in an array.

Example
In array [9,3,2,4,8], the 3rd largest element is 4.

In array [1,2,3,4,5], the 1st largest element is 5,
2nd largest element is 4, 3rd largest element is 3 and etc.

Note
You can swap elements in the array

Challenge
O(n) time, O(1) extra memory.
```

## 题解

找第 K 大数，基于比较的排序的方法时间复杂度为 $$O(n)$$, 数组元素无区间限定，故无法使用线性排序。由于只是需要找第 K 大数，这种类型的题通常需要使用快排的思想解决。[Quick Sort](http://algorithm.yuanbin.me/zh-cn/basics_sorting/quick_sort.html) 总结了一些经典模板。这里比较基准值最后的位置的索引值和 K 的大小关系即可递归求解。

### Java

```java
class Solution {
    //param k : description of k
    //param numbers : array of numbers
    //return: description of return
    public int kthLargestElement(int k, ArrayList<Integer> numbers) {
        if (numbers == null || numbers.isEmpty()) return -1;

        int result = qSort(numbers, 0, numbers.size() - 1, k);
        return result;
    }

    private int qSort(ArrayList<Integer> nums, int l, int u, int k) {
        // l should not greater than u
        if (l >= u) return nums.get(u);

        // index m of nums
        int m = l;
        for (int i = l + 1; i <= u; i++) {
            if (nums.get(i) > nums.get(l)) {
                m++;
                Collections.swap(nums, m, i);
            }
        }
        Collections.swap(nums, m, l);

        if (m + 1 == k) {
            return nums.get(m);
        } else if (m + 1 > k) {
            return qSort(nums, l, m - 1, k);
        } else {
            return qSort(nums, m + 1, u, k);
        }
    }
}
```

### 源码分析

递归的终止条件有两个，一个是左边界的值等于右边界(实际中其实不会有 l > u), 另一个则是索引值 `m + 1 == k`.

### 复杂度分析

最坏情况下需要遍历 $$ n + n - 1 + ... + 1 = O(n^2)$$, 平均情况下 $$n + n/2 + n/4 + ... + 1 = O(2n)=O(n)$$. 故平均情况时间复杂度为 $$O(n)$$. 交换数组的值时使用了额外空间，空间复杂度 $$O(1)$$.
