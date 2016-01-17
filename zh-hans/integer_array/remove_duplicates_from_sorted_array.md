# Remove Duplicates from Sorted Array

## Question

- leetcode: [Remove Duplicates from Sorted Array | LeetCode OJ](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)
- lintcode: [(100) Remove Duplicates from Sorted Array](http://www.lintcode.com/en/problem/remove-duplicates-from-sorted-array/)

```
Given a sorted array, remove the duplicates in place
such that each element appear only once and return the new length.

Do not allocate extra space for another array,
you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].

Example
```

## 题解

使用两根指针(下标)，一个指针(下标)遍历数组，另一个指针(下标)只取不重复的数置于原数组中。

### C++

```c++
class Solution {
public:
    /**
     * @param A: a list of integers
     * @return : return an integer
     */
    int removeDuplicates(vector<int> &nums) {
        if (nums.size() <= 1) return nums.size();

        int len = nums.size();
        int newIndex = 0;
        for (int i = 1; i< len; ++i) {
            if (nums[i] != nums[newIndex]) {
                newIndex++;
                nums[newIndex] = nums[i];
            }
        }

        return newIndex + 1;
    }
};
```

### Java

```java
public class Solution {
    /**
     * @param A: a array of integers
     * @return : return an integer
     */
    public int removeDuplicates(int[] nums) {
        if (nums == null) return -1;
        if (nums.length <= 1) return nums.length;

        int newIndex = 0;
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] != nums[newIndex]) {
                newIndex++;
                nums[newIndex] = nums[i];
            }
        }

        return newIndex + 1;
    }
}
```

### 源码分析

注意最后需要返回的是索引值加1。

### 复杂度分析

遍历一次数组，时间复杂度 $$O(n)$$, 空间复杂度 $$O(1)$$.
