# Longest Increasing Subsequence

- tags: [DP_Sequence]

## Question

- lintcode: [(76) Longest Increasing Subsequence](http://www.lintcode.com/en/problem/longest-increasing-subsequence/)
- [Dynamic Programming | Set 3 (Longest Increasing Subsequence) - GeeksforGeeks](http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/)

### Problem Statement

Given a sequence of integers, find the longest increasing subsequence (LIS).

You code should return the length of the LIS.

#### Example

For [5, 4, 1, 2, 3], the LIS is [1, 2, 3], return 3

For [4, 2, 4, 5, 3, 7], the LIS is [4, 4, 5, 7], return 4

#### Challenge

Time complexity O(n^2) or O(nlogn)

#### Clarification

What's the definition of longest increasing subsequence?

* The longest increasing subsequence problem is to find a subsequence of a given sequence in which the subsequence's elements are in sorted order, lowest to highest, and in which the subsequence is as long as possible. This subsequence is not necessarily contiguous, or unique. 
* https://en.wikipedia.org/wiki/Longest_common_subsequence_problem


## 题解

由题意知这种题应该是单序列动态规划题，结合四要素，可定义`f[i]`为前`i`个数字中的 LIC 数目，那么问题来了，接下来的状态转移方程如何写？似乎写不出来... 再仔细看看 LIS 的定义，状态转移的关键一环应该为数字本身而不是最后返回的结果(数目)，那么理所当然的，我们应定义`f[i]`为前`i`个数字中以第`i`个数字结尾的 LIS 长度，相应的状态转移方程为`f[i] = {1 + max{f[j]} where j < i, nums[j] < nums[i]}`, 该转移方程的含义为在所有满足以上条件的 j 中将最大的`f[j]` 赋予`f[i]`, 如果上式不满足，则`f[i] = 1`. 具体实现时不能直接使用`f[i] = 1 + max(f[j])`, 应为若`if f[i] < 1 + f[j], f[i] = 1 + f[j]`. 最后返回 `max(f[])`.

### Python

```python
class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        if not nums:
            return 0

        lis = [1] * len(nums)
        for i in xrange(1, len(nums)):
            for j in xrange(i):
                if nums[j] <= nums[i] and lis[i] < 1 + lis[j]:
                    lis[i] = 1 + lis[j]
        return max(lis)
```

### C++

```c++
class Solution {
public:
    /**
     * @param nums: The integer array
     * @return: The length of LIS (longest increasing subsequence)
     */
    int longestIncreasingSubsequence(vector<int> nums) {
        if (nums.empty()) return 0;

        int len = nums.size();
        vector<int> lis(len, 1);

        for (int i = 1; i < len; ++i) {
            for (int j = 0; j < i; ++j) {
                if (nums[j] <= nums[i] && (lis[i] < lis[j] + 1)) {
                    lis[i] = 1 + lis[j];
                }
            }
        }

        return *max_element(lis.begin(), lis.end());
    }
};
```

### Java

```java
public class Solution {
    /**
     * @param nums: The integer array
     * @return: The length of LIS (longest increasing subsequence)
     */
    public int longestIncreasingSubsequence(int[] nums) {
        if (nums == null || nums.length == 0) return 0;

        int[] lis = new int[nums.length];
        Arrays.fill(lis, 1);

        for (int i = 1; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] <= nums[i] && (lis[i] < lis[j] + 1)) {
                    lis[i] = lis[j] + 1;
                }
            }
        }

        // get the max lis
        int max_lis = 0;
        for (int i = 0; i < lis.length; i++) {
            if (lis[i] > max_lis) {
                max_lis = lis[i];
            }
        }

        return max_lis;
    }
}
```

### 源码分析

1. 初始化数组，初始值为1
2. 根据状态转移方程递推求得`lis[i]`
3. 遍历`lis` 数组求得最大值

### 复杂度分析

使用了与 nums 等长的空间，空间复杂度 $$O(n)$$. 两重 for 循环，最坏情况下 $$O(n^2)$$, 遍历求得最大值，时间复杂度为 $$O(n)$$, 故总的时间复杂度为 $$O(n^2)$$.

# Follow up

上述问题均只输出最大值，现在需要输出 LIS 中的每一个原始元素值。

## 题解1 - LIS

由于以上递归推导式只能返回最大值，如果现在需要返回 LIS 中的每个元素，直观来讲，构成 LIS 数组中的值对应的原数组值即为我们想要的结果。我们不妨从后往前考虑，依次移除 lis[i] 数组中的值(减一)和索引，遇到和 lis[i]的值相等的 LIS 时即加入到最终返回结果。

### Java

```java
import java.util.*;

public class Solution {
    /**
     * @param nums: The integer array
     * @return: LIS array
     */
    public int[] longestIncreasingSubsequence(int[] nums) {
        if (nums == null || nums.length == 0) return null;

        int[] lis = new int[nums.length];
        Arrays.fill(lis, 1);

        for (int i = 1; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[j] <= nums[i] && (lis[i] < lis[j] + 1)) {
                    lis[i] = lis[j] + 1;
                }
            }
        }

        // get the max lis
        int max_lis = 0, index = 0;
        for (int i = 0; i < lis.length; i++) {
            if (lis[i] > max_lis) {
                max_lis = lis[i];
                index = i;
            }
        }

        // get result
        int[] result = new int[max_lis];
        for (int i = index; i >= 0; i--) {
            if (lis[i] == max_lis) {
                result[max_lis - 1] = nums[i];
                max_lis--;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        int[] nums = new int[]{5, 4, 1, 2, 3};
        Solution sol = new Solution();
        int[] result = sol.longestIncreasingSubsequence(nums);
        for (int i : result) {
            System.out.println(i);
        }
    }
}
```

关于`// get result` 那一节中为何`max_lis` 自减一定是会得到最终想要的结果？假如有和其一样的lis如何破？根据 DP 中状态的定义可知正好为其逆过程，只不过答案不唯一，反向输出的答案输出的是最靠右的结果。
