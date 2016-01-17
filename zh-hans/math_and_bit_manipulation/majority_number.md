# Majority Number

## Question

- leetcode: [Majority Element | LeetCode OJ](https://leetcode.com/problems/majority-element/)
- lintcode: [(46) Majority Number](http://www.lintcode.com/en/problem/majority-number/)

```
Given an array of integers, the majority number is
the number that occurs more than half of the size of the array. Find it.

Example
Given [1, 1, 1, 1, 2, 2, 2], return 1

Challenge
O(n) time and O(1) extra space
```

## 题解

找出现次数超过一半的数，使用哈希表统计不同数字出现的次数，超过二分之一即返回当前数字。这种方法非常简单且容易实现，但会占据过多空间，注意到题中明确表明要找的数会超过二分之一，这里的隐含条件不是那么容易应用。既然某个数超过二分之一，那么用这个数和其他数进行 PK，不同的计数器都减一**（核心在于两两抵消）**，相同的则加1，最后返回计数器大于0的即可。综上，我们需要一辅助数据结构如`pair<int, int>`.

### C++
```c++
int majorityNumber(vector<int> nums) {
    if (nums.empty()) return -1;
    
    int k = -1, count = 0;
    for (auto n : nums) {
        if (!count) k = n;
        if (k == n) count++;
        else count--;
    }
    return k;
}
```

### Java

```java
public class Solution {
    /**
     * @param nums: a list of integers
     * @return: find a  majority number
     */
    public int majorityNumber(ArrayList<Integer> nums) {
        if (nums == null || nums.isEmpty()) return -1;

        // pair<key, count>
        int key = -1, count = 0;
        for (int num : nums) {
            // re-initialize
            if (count == 0) {
                key = num;
                count = 1;
                continue;
            }
            // increment/decrement count
            if (key == num) {
                count++;
            } else {
                count--;
            }
        }

        return key;
    }
}
```

### 源码分析

初始化`count = 0`, 遍历数组时需要先判断`count == 0`以重新初始化。

### 复杂度分析

时间复杂度 $$O(n)$$, 空间复杂度 $$O(1)$$.
