# Longest Increasing Subsequence

- tags: [DP_Sequence]

## Question

- leetcode: [Longest Increasing Subsequence | LeetCode OJ](https://leetcode.com/problems/longest-increasing-subsequence/)
- lintcode: [(76) Longest Increasing Subsequence](http://www.lintcode.com/en/problem/longest-increasing-subsequence/)
- [Dynamic Programming | Set 3 (Longest Increasing Subsequence) - GeeksforGeeks](http://www.geeksforgeeks.org/dynamic-programming-set-3-longest-increasing-subsequence/)

### Problem Statement

Given an unsorted array of integers, find the length of longest increasing
subsequence.

For example,

Given `[10, 9, 2, 5, 3, 7, 101, 18]`,

The longest increasing subsequence is `[2, 3, 7, 101]`, therefore the length
is `4`. Note that there may be more than one LIS combination, it is only
necessary for you to return the length.

Your algorithm should run in $$O(n^2)$$ complexity.

#### Follow up:

Could you improve it to $$O(n \log n)$$ time complexity?

#### Credits:

Special thanks to [@pbrother](https://leetcode.com/discuss/user/pbrother) for
adding this problem and creating all test cases.

## 题解1 - 双重 for 循环

由题意知这种题应该是单序列动态规划题，结合四要素，可定义`f[i]`为前`i`个数字中的 LIC 数目，那么问题来了，接下来的状态转移方程如何写？似乎写不出来... 再仔细看看 LIS 的定义，状态转移的关键一环应该为数字本身而不是最后返回的结果(数目)，那么理所当然的，我们应定义`f[i]`为前`i`个数字中以第`i`个数字结尾的 LIS 长度，相应的状态转移方程为`f[i] = {1 + max{f[j]} where j < i, nums[j] < nums[i]}`, 该转移方程的含义为在所有满足以上条件的 j 中将最大的`f[j]` 赋予`f[i]`, 如果上式不满足，则`f[i] = 1`. 具体实现时不能直接使用`f[i] = 1 + max(f[j])`, 应为若`if f[i] < 1 + f[j], f[i] = 1 + f[j]`. 最后返回 `max(f[])`. 需要注意的是 LIS 的含义，序列中是否可以包含相等的值。如果包含，则改为 `nums[j] < nums[i]`.

### Python

```python
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0

        lis = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and lis[i] < 1 + lis[j]:
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
                if (nums[j] < nums[i] && (lis[i] < lis[j] + 1)) {
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
                if (nums[j] < nums[i] && (lis[i] < lis[j] + 1)) {
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

使用了与 nums 等长的空间，空间复杂度 $$O(n)$$. 两重 for 循环时间复杂度为 $$O(n^2)$$, 遍历求得最大值，时间复杂度为 $$O(n)$$, 故总的时间复杂度为 $$O(n^2)$$.

## 题解2 - 巧用 `lower_bound`

谢谢 @mckelvin 补充！在题解1中我们每次更新 LIS 的值时均遍历了之前的值，那么这里面是否存在重复判断从而可以优化时间复杂度的方法呢？由 LIS 的定义可知，最终构成 LIS 的数列一定是一个递增有序数列，求 LIS 即在构造 LIS 递增数列，最终输出该数列长度即可。这种场景使用 `lower_bound` 十分合适，即首先将数组第一个元素置于`lis` 第一个元素，随后如果元素比 `lis` 中的最后一个元素还要大，则将该元素加入至 `lis` 末尾，反之则将其放入指定的位置。这里有个小小的问题就是最终构成的 `lis` 并不一定是题目要求的 `lis`, 只是在长度上和题目要求的结果一致。[Binary Search - lower/upper bound](../basics_algorithm/binary_search.html) 中对 `lower_bound` 的实现做了详述。

### C++

```c++
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        if (nums.empty()) return 0;

        vector<int> lis;
        for (int i = 0; i < nums.size(); ++i) {
            vector<int>::iterator it = lower_bound(lis.begin(), lis.end(), nums[i]);
            if (it == lis.end()) {
                lis.push_back(nums[i]);
            } else {
                *it = nums[i];
            }
        }

        return lis.size();
    }
};
```

### 源码分析

需要注意的是 `lower_bound` 的使用，需要找 `nums[index] >= target, min(index)`.

### 复杂度分析

最坏空间复杂度为和 `nums` 等长，$$O(n)$$. for 循环加上二分查找最坏情况下时间复杂度为 $$O(n \log n)$$

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
