# Next Permutation

## Source

- lintcode: [(52) Next Permutation](http://www.lintcode.com/en/problem/next-permutation/)

```
Given a list of integers, which denote a permutation.

Find the next permutation in ascending order.

Example
For [1,3,2,3], the next permutation is [1,3,3,2]

For [4,3,2,1], the next permutation is [1,2,3,4]

Note
The list may contains duplicate integers.
```

## 题解

找下一个升序排列，C++ STL 源码剖析一书中有提及，[Permutations](http://algorithm.yuanbin.me/zh-cn/exhaustive_search/permutations.html) 一小节中也有详细介绍，下面简要介绍一下字典序算法：

1. 从后往前寻找索引满足 `a[k] < a[k + 1]`, 如果此条件不满足，则说明已遍历到最后一个。
2. 从后往前遍历，找到第一个比`a[k]`大的数`a[l]`, 即`a[k] < a[l]`.
3. 交换`a[k]`与`a[l]`.
4. 反转`k + 1 ~ n`之间的元素。

由于这道题中规定对于`[4,3,2,1]`, 输出为`[1,2,3,4]`, 故在第一步稍加处理即可。

### Python

```python
class Solution:
    # @param num :  a list of integer
    # @return : a list of integer
    def nextPermutation(self, num):
        if num is None or len(num) <= 1:
            return num
        # step1: find nums[i] < nums[i + 1], Loop backwards
        i = 0
        for i in xrange(len(num) - 2, -1, -1):
            if num[i] < num[i + 1]:
                break
            elif i == 0:
                # reverse nums if reach maximum
                num = num[::-1]
                return num
        # step2: find nums[i] < nums[j], Loop backwards
        j = 0
        for j in xrange(len(num) - 1, i, -1):
            if num[i] < num[j]:
                break
        # step3: swap betwenn nums[i] and nums[j]
        num[i], num[j] = num[j], num[i]
        # step4: reverse between [i + 1, n - 1]
        num[i + 1:len(num)] = num[len(num) - 1:i:-1]

        return num
```

### C++

```c++
class Solution {
public:
    /**
     * @param nums: An array of integers
     * @return: An array of integers that's next permuation
     */
    vector<int> nextPermutation(vector<int> &nums) {
        if (nums.empty() || nums.size() <= 1) {
            return nums;
        }
        // step1: find nums[i] < nums[i + 1]
        int i = 0;
        for (i = nums.size() - 2; i >= 0; --i) {
            if (nums[i] < nums[i + 1]) {
                break;
            } else if (0 == i) {
                // reverse nums if reach maximum
                reverse(nums, 0, nums.size() - 1);
                return nums;
            }
        }
        // step2: find nums[i] < nums[j]
        int j = 0;
        for (j = nums.size() - 1; j > i; --j) {
            if (nums[i] < nums[j]) break;
        }
        // step3: swap betwenn nums[i] and nums[j]
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
        // step4: reverse between [i + 1, n - 1]
        reverse(nums, i + 1, nums.size() - 1);

        return nums;

    }

private:
    void reverse(vector<int>& nums, int start, int end) {
        for (int i = start, j = end; i < j; ++i, --j) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }
};
```

### Java

```java
public class Solution {
    /**
     * @param nums: an array of integers
     * @return: return nums in-place
     */
    public int[] nextPermutation(int[] nums) {
        if (nums == null || nums.length <= 1) {
            return nums;
        }
        // step1: find nums[i] < nums[i + 1]
        int i = 0;
        for (i = nums.length - 2; i >= 0; i--) {
            if (nums[i] < nums[i + 1]) {
                break;
            } else if (i == 0) {
                // reverse nums if reach maximum
                reverse(nums, 0, nums.length - 1);
                return nums;
            }
        }
        // step2: find nums[i] < nums[j]
        int j = 0;
        for (j = nums.length - 1; j > i; j--) {
            if (nums[i] < nums[j]) {
                break;
            }
        }
        // step3: swap betwenn nums[i] and nums[j]
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
        // step4: reverse between [i + 1, n - 1]
        reverse(nums, i + 1, nums.length - 1);

        return nums;
    }

    private void reverse(int[] nums, int start, int end) {
        for (int i = start, j = end; i < j; i++, j--) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }
}
```

### 源码分析

和 Permutation 一小节类似，这里只需要注意在step 1中`i == 0`时需要反转之以获得最小的序列。对于有重复元素，只要在 step1和 step2中判断元素大小时不取等号即可。

### 复杂度分析

最坏情况下，遍历两次原数组，反转一次数组，时间复杂度为 $$O(n)$$, 使用了 temp 临时变量，空间复杂度可认为是 $$O(1)$$.

## Reference

- [Permutations](http://algorithm.yuanbin.me/zh-cn/exhaustive_search/permutations.html)
