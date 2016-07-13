# Previous Permuation

## Question

- lintcode: [(51) Previous Permuation](http://www.lintcode.com/en/problem/previous-permutation/)

### Problem Statement

Given a list of integers, which denote a permutation.

Find the previous permutation in ascending order.

#### Example

For `[1,3,2,3]`, the previous permutation is `[1,2,3,3]`

For `[1,2,3,4]`, the previous permutation is `[4,3,2,1]`

#### Note

The list may contains duplicate integers.

## 题解

和前一题 [Next Permutation](http://algorithm.yuanbin.me/zh-hans/exhaustive_search/next_permutation.html) 非常类似，这里找上一个排列，仍然使用字典序算法，大致步骤如下：

1. 从后往前寻找索引满足 `a[k] > a[k + 1]`, 如果此条件不满足，则说明已遍历到最后一个。
2. 从后往前遍历，找到第一个比`a[k]`小的数`a[l]`, 即`a[k] > a[l]`.
3. 交换`a[k]`与`a[l]`.
4. 反转`k + 1 ~ n`之间的元素。

为何不从前往后呢？因为只有从后往前才能保证得到的是相邻的排列，可以举个实际例子自行分析。

### Python

```python
class Solution:
    # @param num :  a list of integer
    # @return : a list of integer
    def previousPermuation(self, num):
        if num is None or len(num) <= 1:
            return num
        # step1: find nums[i] > nums[i + 1], Loop backwards
        i = 0
        for i in xrange(len(num) - 2, -1, -1):
            if num[i] > num[i + 1]:
                break
            elif i == 0:
                # reverse nums if reach maximum
                num = num[::-1]
                return num
        # step2: find nums[i] > nums[j], Loop backwards
        j = 0
        for j in xrange(len(num) - 1, i, -1):
            if num[i] > num[j]:
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
     * @return: An array of integers that's previous permuation
     */
    vector<int> previousPermuation(vector<int> &nums) {
        if (nums.empty() || nums.size() <= 1) {
            return nums;
        }
        // step1: find nums[i] > nums[i + 1]
        int i = 0;
        for (i = nums.size() - 2; i >= 0; --i) {
            if (nums[i] > nums[i + 1]) {
                break;
            } else if (0 == i) {
                // reverse nums if reach minimum
                reverse(nums, 0, nums.size() - 1);
                return nums;
            }
        }
        // step2: find nums[i] > nums[j]
        int j = 0;
        for (j = nums.size() - 1; j > i; --j) {
            if (nums[i] > nums[j]) break;
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
     * @param nums: A list of integers
     * @return: A list of integers that's previous permuation
     */
    public ArrayList<Integer> previousPermuation(ArrayList<Integer> nums) {
        ArrayList<Integer> perm = new ArrayList<Integer>(nums);
        if (nums == null || nums.size() == 0) return perm;

        // step1: search the first num[k] > num[k+1] backward
        int k = -1;
        for (int i = perm.size() - 2; i >= 0; i--) {
            if (perm.get(i) > perm.get(i + 1)) {
                k = i;
                break;
            }
        }
        // if current rank is the smallest, reverse it to largest, return
        if (k == -1) {
            reverse(perm, 0, perm.size() - 1);
            return perm;
        }

        // step2: search the first perm[k] > perm[l] backward
        int l = perm.size() - 1;
        while (l > k && perm.get(l) >= perm.get(k)) {
            l--;
        }

        // step3: swap perm[k] with perm[l]
        Collections.swap(perm, k, l);

        // step4: reverse between k+1 and perm.length-1;
        reverse(perm, k + 1, perm.size() - 1);

        return perm;
    }

    private void reverse(List<Integer> nums, int lb, int ub) {
        for (int i = lb, j = ub; i < j; i++, j--) {
            Collections.swap(nums, i, j);
        }
    }
}
```

### 源码分析

和 Permutation 一小节类似，这里只需要注意在step 1中`i == -1`时需要反转之以获得最大的序列。对于有重复元素，只要在 step1和 step2中判断元素大小时不取等号即可。

### 复杂度分析

最坏情况下，遍历两次原数组，反转一次数组，时间复杂度为 $$O(n)$$, 使用了 temp 临时变量，空间复杂度可认为是 $$O(1)$$.
