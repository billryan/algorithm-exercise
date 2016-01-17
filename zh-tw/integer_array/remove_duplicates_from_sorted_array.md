# Remove Duplicates from Sorted Array

## Question

- lintcode: [(100) Remove Duplicates from Sorted Array](http://www.lintcode.com/en/problem/remove-duplicates-from-sorted-array/)

```
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].

Example
```

## 題解

使用雙指標(下標)，一個指標(下標)遍歷vector數組，另一個指標(下標)只取不重複的數置於原vector中。

```c++
class Solution {
public:
    /**
     * @param A: a list of integers
     * @return : return an integer
     */
    int removeDuplicates(vector<int> &nums) {
        if (nums.empty()) {
            return 0;
        }

        int size = 0;
        for (vector<int>::size_type i = 0; i != nums.size(); ++i) {
            if (nums[i] != nums[size]) {
                nums[++size] = nums[i];
            }
        }
        return ++size;
    }
};
```

### 源碼分析

注意最後需要返回的是`++size`或者`size + 1`

