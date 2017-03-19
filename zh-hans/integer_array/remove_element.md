# Remove Element

Tags: Array, Two Pointers, Easy

## Question

- leetcode: [Remove Element](https://leetcode.com/problems/remove-element/)
- lintcode: [Remove Element](http://www.lintcode.com/en/problem/remove-element/)

### Problem Statement

Given an array and a value, remove all instances of that value in place and
return the new length.

Do not allocate extra space for another array, you must do this in place with
constant memory.

The order of elements can be changed. It doesn't matter what you leave beyond
the new length.

**Example:**  

Given input array _nums_ = `[3,2,2,3]`, _val_ = `3`

Your function should return length = 2, with the first two elements of _nums_
being 2.

  1. Try two pointers.
  2. Did you use the property of "the order of elements can be changed"?
  3. What happens when the elements to remove are rare?


## 题解1 - 两根指针从前往后遍历

使用两根指针从前往后依次遍历，一根指针遍历数组，另一根指针则指向数组当前不含给定值的索引。遍历时索引处的值不等于给定值则递增1，否则继续遍历，直至遍历结束，返回的索引值恰好是原地替换后的数组（不含给定值）的长度。

### Python

```python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left = 0
        for num in nums:
            if num != val:
                nums[left] = num
                left += 1

        return left
```

### Go

```go
func removeElement(nums []int, val int) int {
        left := 0
        for _, num := range nums {
                if num != val {
                        nums[left] = num
                        left++
                }
        }

        return left
}
```

### Java

```java
public class Solution {
    public int removeElement(int[] nums, int val) {
        int left = 0;
        for (int num : nums) {
            if (num != val) {
                nums[left++] = num;
            }
        }
        
        return left;
    }
}
```

### 源码分析

在遍历数组时若能省略索引值则尽量省略，可使代码更为简明与减少局部变量的使用。

### 复杂度分析

遍历数组一次，最坏情况下需要赋值及 left 自增，故最好最坏情况下时间复杂度均为 $$O(n)$$, 空间复杂度为 $$O(1)$$.

## 题解2 - 给定值出现极少时的优化

从题解1的分析中我们可以发现在数组中元素不等于给定值时都会执行赋值及自增操作，如果给定值在数组中出现次数极少时这种方法效率不高，因此我们可以想办法减少赋值及自增操作。
由于题中明确暗示元素的顺序可变，且新长度后的元素不用理会。我们可以使用两根指针分别往前往后遍历，头指针用于指示当前遍历的元素位置，尾指针则用于在当前元素与欲删除值相等时替换当前元素，两根指针相遇时返回尾指针索引——即删除元素后「新数组」的长度。

### Python

```python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left, right = 0, len(nums)
        while left < right:
            if nums[left] == val:
                nums[left] = nums[right - 1]
                right -= 1
            else:
                left += 1

        return right
```

### C++

```cpp
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int right = nums.size();
        for (int i = 0; i < right; i++) {
            if (nums[i] == val) {
                nums[i] = nums[right - 1];
                right--;
                i--;
            }
        }

        return right;
    }
};
```

### Java

```java
public class Solution {
    public int removeElement(int[] nums, int val) {
        int right = nums.length;
        for (int i = 0; i < right; i++) {
            if (nums[i] == val) {
                nums[i] = nums[right - 1];
                right--;
                i--;
            }
        }

        return right;
    }
}
```

### 源码分析

遍历当前数组，`nums[i] == val` 时将数组尾部元素赋给当前遍历的元素。同时自减 i 和 right, 因为 i 在 for 循环里会自增。另外需要注意的是 right 在遍历过程中可能会变化。

### 复杂度分析

此方法只遍历一次数组，因此时间复杂度是 $$O(n)$$, 空间复杂度为 $$O(1)$$.
