# Next Permutation

## Question

- leetcode: [Next Permutation | LeetCode OJ](https://leetcode.com/problems/next-permutation/)
- lintcode: [(52) Next Permutation](http://www.lintcode.com/en/problem/next-permutation/)

### Problem Statement

Given a list of integers, which denote a permutation.

Find the next permutation in ascending order.

#### Example

For `[1,3,2,3]`, the next permutation is `[1,3,3,2]`

For `[4,3,2,1]`, the next permutation is `[1,2,3,4]`

#### Note

The list may contains duplicate integers.


## 題解

找下一個升序排列，C++ STL 源碼剖析一書中有提及，[Permutations](http://algorithm.yuanbin.me/zh-hans/exhaustive_search/permutations.html) 一小節中也有詳細介紹，下面簡要介紹一下字典序算法：

1. 從後往前尋找索引滿足 `a[k] < a[k + 1]`, 如果此條件不滿足，則說明已遍歷到最後一個。
2. 從後往前遍歷，找到第一個比`a[k]`大的數`a[l]`, 即`a[k] < a[l]`.
3. 交換`a[k]`與`a[l]`.
4. 反轉`k + 1 ~ n`之間的元素。

由於這道題中規定對於`[4,3,2,1]`, 輸出爲`[1,2,3,4]`, 故在第一步稍加處理即可。

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
     * @return: return nothing (void), do not return anything, modify nums in-place instead
     */
    public void nextPermutation(int[] nums) {
        if (nums == null || nums.length == 0) return;

        // step1: search the first nums[k] < nums[k+1] backward
        int k = -1;
        for (int i = nums.length - 2; i >= 0; i--) {
            if (nums[i] < nums[i + 1]) {
                k = i;
                break;
            }
        }
        // if current rank is the largest, reverse it to smallest, return
        if (k == -1) {
            reverse(nums, 0, nums.length - 1);
            return;
        }

        // step2: search the first nums[k] < nums[l] backward
        int l = nums.length - 1;
        while (l > k && nums[l] <= nums[k]) l--;

        // step3: swap nums[k] with nums[l]
        int temp = nums[k];
        nums[k] = nums[l];
        nums[l] = temp;

        // step4: reverse between k+1 and nums.length-1;
        reverse(nums, k + 1, nums.length - 1);
    }

    private void reverse(int[] nums, int lb, int ub) {
        for (int i = lb, j = ub; i < j; i++, j--) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }
}
```

### 源碼分析

和 Permutation 一小節類似，這裏只需要注意在step 1中`i == -1`時需要反轉之以獲得最小的序列。對於有重復元素，只要在 step1和 step2中判斷元素大小時不取等號即可。Lintcode 上給的註釋要求（其實是 Leetcode 上的要求）和實際給出的輸出不一樣。

### 複雜度分析

最壞情況下，遍歷兩次原陣列，反轉一次陣列，時間複雜度爲 $$O(n)$$, 使用了 temp 臨時變量，空間複雜度可認爲是 $$O(1)$$.
