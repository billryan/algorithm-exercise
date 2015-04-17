# Remove Duplicates from Sorted Array

Question: [(100) Remove Duplicates from Sorted Array](http://www.lintcode.com/en/problem/remove-duplicates-from-sorted-array/)

```
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array A = [1,1,2],

Your function should return length = 2, and A is now [1,2].

Example
```

### 题解

使用双指针(下标)，一个指针(下标)遍历vector数组，另一个指针(下标)只取不重复的数置于原vector中。

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

#### 源码分析

注意最后需要返回的是`++size`或者`size + 1`

## Remove Duplicates from Sorted Array II

Question: [(101) Remove Duplicates from Sorted Array II](http://www.lintcode.com/en/problem/remove-duplicates-from-sorted-array-ii/)

```
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array A = [1,1,1,2,2,3],

Your function should return length = 5, and A is now [1,1,2,2,3].
Example
```

### 题解

在上题基础上加了限制条件元素最多可重复出现两次。因此可以在原题的基础上添加一变量跟踪元素重复出现的次数，小于指定值时执行赋值操作。但是需要注意的是重复出现次数`occurence`的初始值(从1开始，而不是0)和reset的时机。

#### C++

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

#### 源码分析

1. 在数组元素小于3(即为2)时可直接返回vector数组大小。
2. 初始化`occurence`的值为1，而不是0. 理解起来也方便些。
3. 初始化下标值`i`从1开始
    - `nums[size] != nums[i]`时递增`size`并赋值，同时重置`occurence`的值为1
    - `(nums[size] == nums[i])`时，首先判断`occurence`的值是否小于2，小于2则先递增`size`，随后将`nums[i]`的值赋给`nums[size]`。这里由于小标`i`从1开始，免去了对`i`为0的特殊情况考虑。
4. 最后返回`size + 1`，即为`++size`
