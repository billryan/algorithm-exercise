# Sliding Window Maximum

## Question

- leetcode: [Sliding Window Maximum | LeetCode OJ](https://leetcode.com/problems/sliding-window-maximum/)
- lintcode: [(362) Sliding Window Maximum](http://www.lintcode.com/en/problem/sliding-window-maximum/)

```
Given an array of n integer with duplicate number, and a moving window(size k),
move the window at each iteration from the start of the array,
find the maximum number inside the window at each moving.

Example
For array [1, 2, 7, 7, 8], moving window size k = 3. return [7, 7, 8]

At first the window is at the start of the array like this

[|1, 2, 7| ,7, 8] , return the maximum 7;

then the window move one step forward.

[1, |2, 7 ,7|, 8], return the maximum 7;

then the window move one step forward again.

[1, 2, |7, 7, 8|], return the maximum 8;

Challenge
o(n) time and O(k) memory
```

## 题解

$$O(nk)$$ 的时间复杂度的方法很容易想到，不停地从当前窗口中取最大就好了。但其实可以发现下一个窗口的最大值与当前窗口的最大值其实是有一定关系的，但这个关系不是简单的将前一个窗口的最大值传递给下一个窗口，**因为数组中每一个元素都是有其作用范围的，超过窗口长度后就失效了！**所以现在思路就稍微清晰一些了，将前一个窗口的最大值传递给下一个窗口时需要判断当前遍历的元素下标和前一个窗口的最大元素下标之差是否已经超过一个窗口长度。

问题来了，思路基本定型，现在就是选用合适的数据结构了。根据上面的思路，这种数据结构应该能在 $$O(1)$$ 的时间内返回最大值，且存储的元素最大可以不超过窗口长度。常规一点的可以采用队列，但是此题中使用普通队列似乎还是很难实现，因为要在 $$O(1)$$ 的时间内返回最大值。符合这个要求的数据结构必须能支持从两端对队列元素进行维护，其中一种实现方法为队首维护最大值，队尾用于插入新元素。双端队列无疑了，有关双端队列的科普见 [双端队列](https://zh.wikipedia.org/wiki/%E5%8F%8C%E7%AB%AF%E9%98%9F%E5%88%97)。可以自己试着以一个实际例子来帮助理解。

### Java

```java
public class Solution {
    /**
     * @param nums: A list of integers.
     * @return: The maximum number inside the window at each moving.
     */
    public ArrayList<Integer> maxSlidingWindow(int[] nums, int k) {
        ArrayList<Integer> winMax = new ArrayList<Integer>();
        if (nums == null || nums.length == 0 || k <= 0) return winMax;

        int len = nums.length;
        Deque<Integer> deque = new ArrayDeque<Integer>();
        for (int i = 0; i < len; i++) {
            // remove the smaller in the rear of queue
            while ((!deque.isEmpty()) && (nums[i] > deque.peekLast())) {
                deque.pollLast();
            }
            // push element in the rear of queue
            deque.offer(nums[i]);
            // remove invalid max
            if (i + 1 > k && deque.peekFirst() == nums[i - k]) {
                deque.pollFirst();
            }
            // add max in current window
            if (i + 1 >= k) {
                winMax.add(deque.peekFirst());
            }
        }

        return winMax;
    }
}
```

### 源码分析

1. 移除队尾元素时首先判断是否为空，因为在移除过程中可能会将队列元素清空。
2. 在移除队尾元素时`nums[i] > deque.peekLast()`不可取等于号，因为这样会将相等的元素全部移除，这样会在窗口中部分元素相等时错误地移除本该添加到最终结果的元素。
3. 移除失效元素和添加元素到最终结果时需要注意下标`i`和`k`的关系，建议举例确定。

### 复杂度分析

时间复杂度 $$O(n)$$, 空间复杂度 $$O(k)$$. 空间复杂度可能不是那么直观，可以这么理解，双端队列中的元素最多只能存活 k 次，因为只有最大元素的存活时间最久，而最大元素在超过窗口长度时即被移除，故空间复杂度为 $$O(k)$$.

## Reference

- 《剑指 Offer》
- [sliding-window-maximum 参考程序 Java/C++/Python](http://www.jiuzhang.com/solutions/sliding-window-maximum/)
- [Maximum of all subarrays of size k (Added a O(n) method) - GeeksforGeeks](http://www.geeksforgeeks.org/maximum-of-all-subarrays-of-size-k/)
