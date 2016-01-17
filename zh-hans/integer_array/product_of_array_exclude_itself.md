# Product of Array Exclude Itself

## Question

- lintcode: [(50) Product of Array Exclude Itself](http://www.lintcode.com/en/problem/product-of-array-exclude-itself/)
- GeeksforGeeks: [A Product Array Puzzle - GeeksforGeeks](http://www.geeksforgeeks.org/a-product-array-puzzle/)

```
Given an integers array A.

Define B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1], calculate B WITHOUT divide operation.

Example
For A=[1, 2, 3], return [6, 3, 2].
```

## 题解1 - 左右分治

根据题意，有 $$result[i] = left[i] \cdot right[i]$$, 其中 $$left[i] = \prod _{j = 0} ^{i - 1} A[j]$$, $$right[i] = \prod _{j = i + 1} ^{n - 1} A[j]$$. 即将最后的乘积分为两部分求解，首先求得左半部分的值，然后求得右半部分的值。最后将左右两半部分乘起来即为解。

### C++

```c++
class Solution {
public:
    /**
     * @param A: Given an integers array A
     * @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
     */
    vector<long long> productExcludeItself(vector<int> &nums) {
        const int nums_size = nums.size();
        vector<long long> result(nums_size, 1);
        if (nums.empty() || nums_size == 1) {
            return result;
        }

        vector<long long> left(nums_size, 1);
        vector<long long> right(nums_size, 1);
        for (int i = 1; i != nums_size; ++i) {
            left[i] = left[i - 1] * nums[i - 1];
            right[nums_size - i - 1] = right[nums_size - i] * nums[nums_size - i];
        }
        for (int i = 0; i != nums_size; ++i) {
            result[i] = left[i] * right[i];
        }

        return result;
    }
};
```

### 源码分析

一次`for`循环求出左右部分的连乘积，下标的确定可使用简单例子辅助分析。

### 复杂度分析

两次`for`循环，时间复杂度 $$O(n)$$. 使用了左右两半部分辅助空间，空间复杂度 $$O(2n)$$.

## 题解2 - 原地求积

题解1中使用了左右两个辅助数组，但是仔细瞅瞅其实可以发现完全可以在最终返回结果`result`基础上原地计算左右两半部分的积。

### C++

```c++
class Solution {
public:
    /**
     * @param A: Given an integers array A
     * @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
     */
    vector<long long> productExcludeItself(vector<int> &nums) {
        const int nums_size = nums.size();
        vector<long long> result(nums_size, 1);

        // solve the left part first
        for (int i = 1; i < nums_size; ++i) {
            result[i] = result[i - 1] * nums[i - 1];
        }

        // solve the right part
        long long temp = 1;
        for (int i = nums_size - 1; i >= 0; --i) {
            result[i] *= temp;
            temp *= nums[i];
        }

        return result;
    }
};
```

### 源码分析

计算左半部分的递推式不用改，计算右半部分的乘积时由于会有左半部分值的干扰，故使用`temp`保存连乘的值。注意`temp`需要使用`long long`, 否则会溢出。

### 复杂度分析

时间复杂度同上，空间复杂度为 $$O(1)$$.
