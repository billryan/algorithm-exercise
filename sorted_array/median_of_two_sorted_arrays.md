# Median of two Sorted Arrays

Question: [(65) Median of two Sorted Arrays](http://www.lintcode.com/en/problem/median-of-two-sorted-arrays/)

```
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example
For A = [1,2,3,4,5,6] B = [2,3,4,5], the median is 3.5

For A = [1,2,3] B = [4,5], the median is 3



Challenge
Time Complexity O(logn)
```

### 题解

何谓"Median"? 由题目意思可得即为两个数组中一半数据比它大，另一半数据比它小的那个数。详见 [中位数 - 维基百科，自由的百科全书](http://zh.wikipedia.org/wiki/%E4%B8%AD%E4%BD%8D%E6%95%B8)，题中已有信息两个数组均为有序，题目要求时间复杂度为O(log)，因此应该往二分法上想。

在两个数组中找第k大数->找中位数即为找第k大数的一个特殊情况——第(A.length + B.length) / 2 大数。因此首先需要解决找第k大数的问题。这个联想确实有点牵强...

使用归并的思想逐个比较找出中位数的复杂度为O(n)，显然不符要求，接下来考虑使用二分法。由于是找第k大数，使用二分法则比较A[k/2 - 1]和B[k/2 - 1]，并思考这两个元素和第k大元素的关系。
1. A[k/2 - 1] <= B[k/2 - 1] => A和B合并后的第k大数中必包含A[0]~A[k/2  -1]，可使用归并的思想去理解。
2. 若k/2 - 1超出A的长度，则必取B[0]~B[k/2 - 1]

#### C++

```c++
class Solution {
public:
    /**
     * @param A: An integer array.
     * @param B: An integer array.
     * @return: a double whose format is *.5 or *.0
     */
    double findMedianSortedArrays(vector<int> A, vector<int> B) {
        if (A.empty() && B.empty()) {
            return 0;
        }

        vector<int> NonEmpty;
        if (A.empty()) {
            NonEmpty = B;
        }
        if (B.empty()) {
            NonEmpty = A;
        }
        if (!NonEmpty.empty()) {
            vector<int>::size_type len_vec = NonEmpty.size();
            return len_vec % 2 == 0 ?
                    (NonEmpty[len_vec / 2 - 1] + NonEmpty[len_vec / 2]) / 2.0 :
                    NonEmpty[len_vec / 2];
        }

        vector<int>::size_type len = A.size() + B.size();
        if (len % 2 == 0) {
            return ((findKth(A, 0, B, 0, len / 2) + findKth(A, 0, B, 0, len / 2 + 1)) / 2.0);
        } else {
            return findKth(A, 0, B, 0, len / 2 + 1);
        }
        // write your code here
    }

private:
    int findKth(vector<int> &A, vector<int>::size_type A_start, vector<int> &B, vector<int>::size_type B_start, int k) {
        if (A_start > A.size() - 1) {
            // all of the element of A are smaller than the kTh number
            return B[B_start + k - 1];
        }
        if (B_start > B.size() - 1) {
            // all of the element of B are smaller than the kTh number
            return A[A_start + k - 1];
        }

        if (k == 1) {
            return A[A_start] < B[B_start] ? A[A_start] : B[B_start];
        }

        int A_key = A_start + k / 2 - 1 < A.size() ?
                    A[A_start + k / 2 - 1] : INT_MAX;
        int B_key = B_start + k / 2 - 1 < B.size() ?
                    B[B_start + k / 2 - 1] : INT_MAX;

        if (A_key > B_key) {
            return findKth(A, A_start, B, B_start + k / 2, k - k / 2);
        } else {
            return findKth(A, A_start + k / 2, B, B_start, k - k / 2);
        }
    }
};
```

#### 源码分析

此题的边界条件较多，不容易直接从代码看清思路。首先分析找k大的辅助程序。

1. 如果`A_start > A.size() - 1`，意味着A中无数提供，故仅能从B中取，所以只能是B从`B_start`开始的第k个数。下面的B...分析方法类似。
2. k为1时，无需再递归调用，直接返回较小值。
3. 以A为例，取出自`A_start`开始的第`k / 2`个数，若下标`A_start + k / 2 - 1 < A.size()`，则可取此下标对应的元素，否则置为int的最大值，便于后面进行比较，免去了诸多边界条件的判断。
4. 比较`A_key > B_key`，取小的折半递归调用findKth。

接下来分析`findMedianSortedArrays`：

1. 首先考虑异常情况，A, B都为空，A/B其中一个为空。
2. A+B 的长度为偶数时返回len / 2和 len / 2 + 1的均值，为奇数时则返回len / 2 + 1

## reference

- [九章算法 | Median of Two Sorted Arrays](http://www.jiuzhang.com/solutions/median-of-two-sorted-arrays/)
- [LeetCode: Median of Two Sorted Arrays 解题报告 - Yu's Garden - 博客园](http://www.cnblogs.com/yuzhangcmu/p/4138184.html)
