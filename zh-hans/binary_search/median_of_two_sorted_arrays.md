# Median of two Sorted Arrays

## Question

- leetcode: [Median of Two Sorted Arrays | LeetCode OJ](https://leetcode.com/problems/median-of-two-sorted-arrays/)
- lintcode: [(65) Median of two Sorted Arrays](http://www.lintcode.com/en/problem/median-of-two-sorted-arrays/)

### Problem Statement

There are two sorted arrays *A* and *B* of size *m* and *n* respectively. Find the **median** of the two sorted arrays.

#### Example

Given `A=[1,2,3,4,5,6]` and `B=[2,3,4,5]`, the median is `3.5`.

Given `A=[1,2,3]` and `B=[4,5]`, the median is `3`.

#### Challenge

The overall run time complexity should be O(log (m+n)).

## 题解1 - 归并排序

何谓"Median"? 由题目意思可得即为两个数组中一半数据比它大，另一半数据比它小的那个数。详见 [中位数 - 维基百科，自由的百科全书](http://zh.wikipedia.org/wiki/%E4%B8%AD%E4%BD%8D%E6%95%B8)。简单粗暴的方法就是使用归并排序的思想，挨个比较两个数组的值，取小的，最后分奇偶长度返回平均值或者中位值。

### Java1 - merge sort with equal length

```java
class Solution {
    /**
     * @param A: An integer array.
     * @param B: An integer array.
     * @return: a double whose format is *.5 or *.0
     */
    public double findMedianSortedArrays(int[] A, int[] B) {
        if ((A == null || A.length == 0) && (B == null || B.length == 0)) {
            return -1.0;
        }
        int lenA = (A == null) ? 0 : A.length;
        int lenB = (B == null) ? 0 : B.length;
        int len = lenA + lenB;

        /* merge sort */
        int indexA = 0, indexB = 0, indexC = 0;
        int[] C = new int[len];
        // case1: both A and B have elements
        while (indexA < lenA && indexB < lenB) {
            if (A[indexA] < B[indexB]) {
                C[indexC++] = A[indexA++];
            } else {
                C[indexC++] = B[indexB++];
            }
        }
        // case2: only A has elements
        while (indexA < lenA) {
            C[indexC++] = A[indexA++];
        }
        // case3: only B has elements
        while (indexB < lenB) {
            C[indexC++] = B[indexB++];
        }

        // return median for even and odd cases
        int indexM1 = (len - 1) / 2, indexM2 = len / 2;
        if (len % 2 == 0) {
            return (C[indexM1] + C[indexM2]) / 2.0;
        } else {
            return C[indexM2];
        }
    }
}
```

### Java2 - space optimization

```java
class Solution {
    /**
     * @param A: An integer array.
     * @param B: An integer array.
     * @return: a double whose format is *.5 or *.0
     */
    public double findMedianSortedArrays(int[] A, int[] B) {
        if ((A == null || A.length == 0) && (B == null || B.length == 0)) {
            return -1.0;
        }
        int lenA = (A == null) ? 0 : A.length;
        int lenB = (B == null) ? 0 : B.length;
        int len = lenA + lenB;
        int indexM1 = (len - 1) / 2, indexM2 = len / 2;
        int m1 = 0, m2 = 0;

        /* merge sort */
        int indexA = 0, indexB = 0, indexC = 0;
        // case1: both A and B have elements
        while (indexA < lenA && indexB < lenB) {
            if (indexC > indexM2) {
                break;
            }
            if (indexC == indexM1) {
                m1 = Math.min(A[indexA], B[indexB]);
            }
            if (indexC == indexM2) {
                m2 = Math.min(A[indexA], B[indexB]);
            }
            if (A[indexA] < B[indexB]) {
                indexA++;
            } else {
                indexB++;
            }
            indexC++;
        }
        // case2: only A has elements
        while (indexA < lenA) {
            if (indexC > indexM2) {
                break;
            }
            if (indexC == indexM1) {
                m1 = A[indexA];
            }
            if (indexC == indexM2) {
                m2 = A[indexA];
            }
            indexA++;
            indexC++;
        }
        // case3: only B has elements
        while (indexB < lenB) {
            if (indexC > indexM2) {
                break;
            }
            if (indexC == indexM1) {
                m1 = B[indexB];
            }
            if (indexC == indexM2) {
                m2 = B[indexB];
            }
            indexB++;
            indexC++;
        }

        // return median for even and odd cases
        if (len % 2 == 0) {
            return (m1 + m2) / 2.0;
        } else {
            return m2;
        }
    }
}
```

### 源码分析

使用归并排序的思想做这道题不难，但是边界条件的处理比较闹心，使用归并排序带辅助空间的做法实现起来比较简单，代码也短。如果不使用额外空间并做一定优化的话需要多个 if 语句进行判断，需要注意的是多个 if 之间不能使用 else ，因为`indexM1`和`indexM2`有可能相等。

### 复杂度分析

时间复杂度 $$O(m + n)$$, 空间复杂度为 $$(m + n)$$(使用额外数组), 或者 $$O(1)$$(不使用额外数组).

## 题解2 - 二分搜索

题中已有信息两个数组均为有序，找中位数的关键在于找到第一半大的数，显然可以使用二分搜索优化。本题是找中位数，其实可以泛化为一般的找第 k 大数，这个辅助方法的实现非常有意义！在两个数组中找第k大数->找中位数即为找第k大数的一个特殊情况——第(A.length + B.length) / 2 大数。因此首先需要解决找第k大数的问题。这个联想确实有点牵强...

由于是找第k大数(从1开始)，使用二分法则需要比较A[k/2 - 1]和B[k/2 - 1]，并思考这两个元素和第k大元素的关系。
1. A[k/2 - 1] <= B[k/2 - 1] => A和B合并后的第k大数中必包含A[0]~A[k/2  -1]，可使用归并的思想去理解。
2. 若k/2 - 1超出A的长度，则必取B[0]~B[k/2 - 1]

### C++

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

### Java

```java
class Solution {
    /**
     * @param A: An integer array.
     * @param B: An integer array.
     * @return: a double whose format is *.5 or *.0
     */
    public double findMedianSortedArrays(int[] A, int[] B) {
        if ((A == null || A.length == 0) && (B == null || B.length == 0)) {
            return -1.0;
        }
        int lenA = (A == null) ? 0 : A.length;
        int lenB = (B == null) ? 0 : B.length;
        int len = lenA + lenB;

        // return median for even and odd cases
        if (len % 2 == 0) {
            return (findKth(A, 0, B, 0, len/2) + findKth(A, 0, B, 0, len/2 + 1)) / 2.0;
        } else {
            return findKth(A, 0, B, 0, len/2 + 1);
        }
    }

    private int findKth(int[] A, int indexA, int[] B, int indexB, int k) {

        int lenA = (A == null) ? 0 : A.length;
        if (indexA > lenA - 1) {
            return B[indexB + k - 1];
        }
        int lenB = (B == null) ? 0 : B.length;
        if (indexB > lenB - 1) {
            return A[indexA + k - 1];
        }

        // avoid infilite loop if k == 1
        if (k == 1) return Math.min(A[indexA], B[indexB]);

        int keyA = Integer.MAX_VALUE, keyB = Integer.MAX_VALUE;
        if (indexA + k/2 - 1 < lenA) keyA = A[indexA + k/2 - 1];
        if (indexB + k/2 - 1 < lenB) keyB = B[indexB + k/2 - 1];

        if (keyA > keyB) {
            return findKth(A, indexA, B, indexB + k/2, k - k/2);
        } else {
            return findKth(A, indexA + k/2, B, indexB, k - k/2);
        }
    }
}
```

### 源码分析

本题用非递归的方法非常麻烦，递归的方法减少了很多边界的判断。此题的边界条件较多，不容易直接从代码看清思路。首先分析找k大的辅助程序。以 Java 的代码为例。

1. 首先在主程序中排除 A, B 均为空的情况。
2. 排除 A 或者 B 中有一个为空或者长度为0的情况。如果`A_start > A.size() - 1`，意味着A中无数提供，故仅能从B中取，所以只能是B从`B_start`开始的第k个数。下面的B...分析方法类似。
3. k为1时，无需再递归调用，直接返回较小值。如果 k 为1不返回将导致后面的无限循环。
4. 以A为例，取出自`A_start`开始的第`k / 2`个数，若下标`A_start + k / 2 - 1 < A.size()`，则可取此下标对应的元素，否则置为int的最大值，便于后面进行比较，免去了诸多边界条件的判断。
4. 比较`A_key > B_key`，取小的折半递归调用findKth。

接下来分析`findMedianSortedArrays`：

1. 首先考虑异常情况，A, B都为空。
2. A+B 的长度为偶数时返回len / 2和 len / 2 + 1的均值，为奇数时则返回len / 2 + 1

### 复杂度分析

找中位数，K 为数组长度和的一半，故总的时间复杂度为 $$O(\log (m+n))$$.

## Reference

- [九章算法 | Median of Two Sorted Arrays](http://www.jiuzhang.com/solutions/median-of-two-sorted-arrays/)
- [LeetCode: Median of Two Sorted Arrays 解题报告 - Yu's Garden - 博客园](http://www.cnblogs.com/yuzhangcmu/p/4138184.html)
