# Majority Number II

## Question

- leetcode: [Majority Element II | LeetCode OJ](https://leetcode.com/problems/majority-element-ii/)
- lintcode: [(47) Majority Number II](http://www.lintcode.com/en/problem/majority-number-ii/)

```
Given an array of integers,
the majority number is the number that occurs more than 1/3 of the size of the array.

Find it.

Example
Given [1, 2, 1, 2, 1, 3, 3], return 1.

Note
There is only one majority number in the array.

Challenge
O(n) time and O(1) extra space.
```

## 题解

题 [Majority Number](http://algorithm.yuanbin.me/zh-hans/math_and_bit_manipulation/majority_number.html) 的升级版，之前那道题是『两两抵消』，这道题自然则需要『三三抵消』，不过『三三抵消』需要注意不少细节，比如两个不同数的添加顺序和添加条件。

### C++
```c++
class Solution {
public:
    /**
     * @param nums: A list of integers
     * @return: The majority number occurs more than 1/3.
     */
    int majorityNumber(vector<int> nums) {
        if (nums.empty()) return -1;
        
        int k1 = 0, k2 = 0, c1 = 0, c2 = 0;
        for (auto n : nums) {
            if (!c1 || k1 == n) {
                k1 = n;
                c1++;
            } else if (!c2 || k2 == n) {
                k2 = n;
                c2++;
            } else {
                c1--;
                c2--;
            }
        }
        
        c1 = 0; 
        c2 = 0;
        for (auto n : nums) {
            if (n == k1) c1++;
            if (n == k2) c2++;
        }
        return c1 > c2 ? k1 : k2;
    }
};
```

### Java

```java
public class Solution {
    /**
     * @param nums: A list of integers
     * @return: The majority number that occurs more than 1/3
     */
    public int majorityNumber(ArrayList<Integer> nums) {
        if (nums == null || nums.isEmpty()) return -1;

        // pair
        int key1 = -1, key2 = -1;
        int count1 = 0, count2 = 0;
        for (int num : nums) {
            if (count1 == 0) {
                key1 = num;
                count1 = 1;
                continue;
            } else if (count2 == 0 && key1 != num) {
                key2 = num;
                count2 = 1;
                continue;
            }
            if (key1 == num) {
                count1++;
            } else if (key2 == num) {
                count2++;
            } else {
                count1--;
                count2--;
            }
        }

        count1 = 0;
        count2 = 0;
        for (int num : nums) {
            if (key1 == num) {
                count1++;
            } else if (key2 == num) {
                count2++;
            }
        }
        return count1 > count2 ? key1 : key2;
    }
}
```

### 源码分析

首先处理`count == 0`的情况，这里需要注意的是`count2 == 0 && key1 = num`, 不重不漏。最后再次遍历原数组也必不可少，因为由于添加顺序的区别，count1 和 count2的大小只具有相对意义，还需要最后再次比较其真实计数器值。

### 复杂度分析

时间复杂度 $$O(n)$$, 空间复杂度 $$O(2 \times 2) = O(1)$$.

## Reference

- [Majority Number II 参考程序 Java/C++/Python](http://www.jiuzhang.com/solutions/majority-number-ii/)
