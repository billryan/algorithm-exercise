# Remove Duplicates from Sorted Array II

## Question

- lintcode: [(101) Remove Duplicates from Sorted Array II](http://www.lintcode.com/en/problem/remove-duplicates-from-sorted-array-ii/)

```
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
Example
```

## 題解

在上題基礎上加了限制條件元素最多可重複出現兩次。因此可以在原題的基礎上添加一變量跟蹤元素重複出現的次數，小於指定值時執行賦值操作。但是需要注意的是重複出現次數`occurence`的初始值(從1開始，而不是0)和reset的時機。

### C++

```c++
class Solution {
public:
    /**
     * @param A: a list of integers
     * @return : return an integer
     */
    int removeDuplicates(vector<int> &nums) {
        if (nums.size() < 3) {
            return nums.size();
        }

        int size = 0;
        int occurence = 1;
        for (vector<int>::size_type i = 1; i != nums.size(); ++i) {
            if (nums[size] != nums[i]) {
                nums[++size] = nums[i];
                occurence = 1;
            } else if (nums[size] == nums[i]) {
                if (occurence++ < 2) {
                    nums[++size] = nums[i];
                }
            }
        }

        return ++size;
    }
};
```

### 源碼分析

1. 在數組元素小於3(即為2)時可直接返回vector數組大小。
2. 初始化`occurence`的值為1，而不是0. 理解起來也方便些。
3. 初始化下標值`i`從1開始
    - `nums[size] != nums[i]`時遞增`size`並賦值，同時重置`occurence`的值為1
    - `(nums[size] == nums[i])`時，首先判斷`occurence`的值是否小於2，小於2則先遞增`size`，隨後將`nums[i]`的值賦給`nums[size]`。這裡由於小標`i`從1開始，免去了對`i`為0的特殊情況考慮。
4. 最後返回`size + 1`，即為`++size`
