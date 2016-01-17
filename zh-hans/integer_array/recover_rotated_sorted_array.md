# Recover Rotated Sorted Array

## Question

- lintcode: [(39) Recover Rotated Sorted Array](http://lintcode.com/en/problem/recover-rotated-sorted-array/)

```
Given a rotated sorted array, recover it to sorted array in-place.

Example
[4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]

Challenge
In-place, O(1) extra space and O(n) time.

Clarification
What is rotated array:

    - For example, the orginal array is [1,2,3,4], The rotated array of it can be [1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]
```

首先可以想到逐步移位，但是这种方法显然太浪费时间，不可取。下面介绍利器『三步翻转法』，以`[4, 5, 1, 2, 3]`为例。

1. 首先找到分割点`5`和`1`
2. 翻转前半部分`4, 5`为`5, 4`，后半部分`1, 2, 3`翻转为`3, 2, 1`。整个数组目前变为`[5, 4, 3, 2, 1]`
3. 最后整体翻转即可得`[1, 2, 3, 4, 5]`

由以上3个步骤可知其核心为『翻转』的in-place实现。使用两个指针，一个指头，一个指尾，使用for循环移位交换即可。

### Java

```java
public class Solution {
    /**
     * @param nums: The rotated sorted array
     * @return: The recovered sorted array
     */
    public void recoverRotatedSortedArray(ArrayList<Integer> nums) {
        if (nums == null || nums.size() <= 1) {
            return;
        }

        int pos = 1;
        while (pos < nums.size()) { // find the break point
            if (nums.get(pos - 1) > nums.get(pos)) {
                break;
            }
            pos++;
        }
        myRotate(nums, 0, pos - 1);
        myRotate(nums, pos, nums.size() - 1);
        myRotate(nums, 0, nums.size() - 1);
    }

    private void myRotate(ArrayList<Integer> nums, int left, int right) { // in-place rotate
        while (left < right) {
            int temp = nums.get(left);
            nums.set(left, nums.get(right));
            nums.set(right, temp);
            left++;
            right--;
        }
    }
}
```

### C++

```c++
/**
 * forked from
 * http://www.jiuzhang.com/solutions/recover-rotated-sorted-array/
 */
class Solution {
private:
    void reverse(vector<int> &nums, vector<int>::size_type start, vector<int>::size_type end) {
        for (vector<int>::size_type i = start, j = end; i < j; ++i, --j) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }

public:
    void recoverRotatedSortedArray(vector<int> &nums) {
        for (vector<int>::size_type index = 0; index != nums.size() - 1; ++index) {
            if (nums[index] > nums[index + 1]) {
                reverse(nums, 0, index);
                reverse(nums, index + 1, nums.size() - 1);
                reverse(nums, 0, nums.size() - 1);

                return;
            }
        }
    }
};
```

### 源码分析

首先找到分割点，随后分三步调用翻转函数。简单起见可将`vector<int>::size_type`替换为`int`
