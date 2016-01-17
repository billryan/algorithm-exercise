# Remove Duplicates from Sorted Array II

## Question

- leetcode: [Remove Duplicates from Sorted Array II | LeetCode OJ](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)
- lintcode: [(101) Remove Duplicates from Sorted Array II](http://www.lintcode.com/en/problem/remove-duplicates-from-sorted-array-ii/)

```
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
Example
```

## 题解

在上题基础上加了限制条件元素最多可重复出现两次。~~因此可以在原题的基础上添加一变量跟踪元素重复出现的次数，小于指定值时执行赋值操作。但是需要注意的是重复出现次数`occurence`的初始值(从1开始，而不是0)和reset的时机。~~这种方法比较复杂，谢谢 @meishenme 提供的简洁方法，核心思想仍然是两根指针，只不过此时新索引自增的条件是当前遍历的数组值和『新索引』或者『新索引-1』两者之一不同。

### C++

```c++
class Solution {
public:
    /**
     * @param A: a list of integers
     * @return : return an integer
     */
    int removeDuplicates(vector<int> &nums) {
        if (nums.size() <= 2) return nums.size();

        int len = nums.size();
        int newIndex = 1;
        for (int i = 2; i < len; ++i) {
            if (nums[i] != nums[newIndex] || nums[i] != nums[newIndex - 1]) {
                ++newIndex;
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
        if (nums.length <= 2) return nums.length;

        int newIndex = 1;
        for (int i = 2; i < nums.length; i++) {
            if (nums[i] != nums[newIndex] || nums[i] != nums[newIndex - 1]) {
                newIndex++;
                nums[newIndex] = nums[i];
            }
        }

        return newIndex + 1;
    }
}
```

### 源码分析

遍历数组时 i 从2开始，newIndex 初始化为1便于分析。

### 复杂度分析

时间复杂度 $$O(n)$$, 空间复杂度 $$O(1)$$.
