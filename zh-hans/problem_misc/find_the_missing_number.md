# Find the Missing Number

## Question

- lintcode: [(196) Find the Missing Number](http://www.lintcode.com/en/problem/find-the-missing-number/)
- [Find the Missing Number - GeeksforGeeks](http://www.geeksforgeeks.org/find-the-missing-number/)

### Problem Statement

Given an array contains _N_ numbers of 0 .. _N_, find which number doesn't exist in the array.

#### Example

Given _N_ = `3` and the array `[0, 1, 3]`, return `2`.

#### Challenge

Do it in-place with $$O(1)$$ extra memory and $$O(n)$$ time.

## 题解1 - 位运算

和找单数的题类似，这里我们不妨试试位运算中异或的思路。最开始自己想到的是利用相邻项异或结果看是否会有惊喜，然而发现 `a^(a+1) != a^a + a^1` 之后眼泪掉下来... 如果按照找单数的做法，首先对数组所有元素异或，得到数`x1`, 现在的问题是如何利用`x1`得到缺失的数，由于找单数中其他数都是成对出现的，故最后的结果即是单数，这里每个数都是单数，怎么办呢？我们现在再来分析下如果没有缺失数的话会是怎样呢？假设所有元素异或得到数`x2`, 数`x1`和`x2`有什么差异呢？假设缺失的数是`x0`，那么容易知道`x2 = x1 ^ x0`, 相当于现在已知`x1`和`x2`，要求`x0`. 根据 [Bit Manipulation](http://algorithm.yuanbin.me/zh-hans/basics_misc/bit_manipulation.html) 中总结的交换律，`x0 = x1 ^ x2`.

位运算的题往往比较灵活，需要好好利用常用等式变换。

### Java

```java
public class Solution {
    /**
     * @param nums: an array of integers
     * @return: an integer
     */
    public int findMissing(int[] nums) {
        if (nums == null || nums.length == 0) return -1;

        // get xor from 0 to N excluding missing number
        int x1 = 0;
        for (int i : nums) {
            x1 ^= i;
        }

        // get xor from 0 to N
        int x2 = 0;
        for (int i = 0; i <= nums.length; i++) {
            x2 ^= i;
        }

        // missing = x1 ^ x2;
        return x1 ^ x2;
    }
}
```

### 源码分析

略

### 复杂度分析

遍历原数组和 N+1大小的数组，时间复杂度 $$O(n)$$, 空间复杂度 $$O(1)$$.

## 题解2 - 桶排序

非常简单直观的想法——排序后检查缺失元素，但是此题中要求时间复杂度为 $$O(n)$$, 因此如果一定要用排序来做，那一定是使用非比较排序如桶排序或者计数排序。题中另一提示则是要求只使用 $$O(1)$$ 的额外空间，那么这就是在提示我们应该使用原地交换。根据题意，元素应无重复，可考虑使用桶排，索引和值一一对应即可。第一重 for 循环遍历原数组，内循环使用 while, 调整索引处对应的值，直至相等或者索引越界为止，for 循环结束时桶排结束。最后再遍历一次数组找出缺失元素。

初次接触这种题还是比较难想到使用桶排这种思想的，尤其是利用索引和值一一对应这一特性找出缺失元素，另外此题在实际实现时不容易做到 bug-free, while 循环处容易出现死循环。

### Java

```java
public class Solution {
    /**
     * @param nums: an array of integers
     * @return: an integer
     */
    public int findMissing(int[] nums) {
        if (nums == null || nums.length == 0) return -1;

        bucketSort(nums);
        // find missing number
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != i) {
                return i;
            }
        }

        return nums.length;
    }

    private void bucketSort(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            while (nums[i] != i) {
		        // ignore nums[i] == nums.length
                if (nums[i] == nums.length) {
                    break;
                }
                int nextNum = nums[nums[i]];
                nums[nums[i]] = nums[i];
		        nums[i] = nextNum;
            }
        }
    }
}
```

### 源码分析

难点一在于正确实现桶排，难点二在于数组元素中最大值 N 如何处理。N 有三种可能：

1. N 不在原数组中，故最后应该返回 N
2. N 在原数组中，但不在数组中的最后一个元素
3. N 在原数组中且在数组最后一个元素

其中情况1在遍历桶排后的数组时无返回，最后返回 N.

其中2和3在 while 循环处均会遇到 break 跳出，即当前这个索引所对应的值要么最后还是 N，要么就是和索引相同的值。如果最后还是 N, 也就意味着原数组中缺失的是其他值，如果最后被覆盖掉，那么桶排后的数组不会出现 N, 且缺失的一定是 N 之前的数。

综上，这里的实现无论 N 出现在哪个索引都能正确返回缺失值。实现上还是比较巧妙的，所以说在没做过这类题时要在短时间内 bug-free 比较难，当然也可能是我比较菜...

另外一个难点在于如何保证或者证明 while 一定不会出现死循环，可以这么理解，如果 while 条件不成立且未出现`nums.length`这个元素，那么就一定会使得一个元素正确入桶，又因为没有重复元素出现，故一定不会出现死循环。

### 复杂度分析

桶排时间复杂度 $$O(n)$$, 空间复杂度 $$O(1)$$. 遍历原数组找缺失数时间复杂度 $$O(n)$$. 故总的时间复杂度为 $$O(n)$$, 空间复杂度 $$O(1)$$.
