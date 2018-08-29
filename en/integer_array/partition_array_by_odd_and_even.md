# Partition Array by Odd and Even

## Question

- lintcode: [(373) Partition Array by Odd and Even](http://www.lintcode.com/en/problem/partition-array-by-odd-and-even/)
- [Segregate Even and Odd numbers - GeeksforGeeks](http://www.geeksforgeeks.org/segregate-even-and-odd-numbers/)

```
Partition an integers array into odd number first and even number second.

Example
Given [1, 2, 3, 4], return [1, 3, 2, 4]

Challenge
Do it in-place.
```

## Solution

Use **two pointers** to keep the odd before the even, and swap when necessary.

### Java

```java
public class Solution {
    /**
     * @param nums: an array of integers
     * @return: nothing
     */
    public void partitionArray(int[] nums) {
        if (nums == null) return;

        int left = 0, right = nums.length - 1;
        while (left < right) {
            // odd number
            while (left < right && nums[left] % 2 != 0) {
                left++;
            }
            // even number
            while (left < right && nums[right] % 2 == 0) {
                right--;
            }
            // swap
            if (left < right) {
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
            }
        }
    }
}
```

### C++

```c++
void partitionArray(vector<int> &nums) {
      if (nums.empty()) return;

      int i=0, j=nums.size()-1;
      while (i<j) {
          while (i<j && nums[i]%2!=0) i++;
          while (i<j && nums[j]%2==0) j--;
          if (i != j) swap(nums[i], nums[j]);
      }
  }
```

### Src Code Analysis

Be careful not to forget `left < right` in while loop condition.

### Complexity

To traverse the array, time complexity is $$O(n)$$. And maintaining two pointers means $$O(1)$$ space complexity.
