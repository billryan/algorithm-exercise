# Merge Sorted Array II

## Source

- lintcode: [(64) Merge Sorted Array II](http://www.lintcode.com/en/problem/merge-sorted-array-ii/)

```
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are mand n respectively.

Example
A = [1, 2, 3, empty, empty] B = [4,5]

After merge, A will be filled as [1,2,3,4,5]
```

## 题解

在上题的基础上加入了in-place的限制。将上题的新数组视为length相对较大的数组即可，仍然从数组末尾进行归并，取出较大的元素。

### Java

```java
class Solution {
    /**
     * @param A: sorted integer array A which has m elements,
     *           but size of A is m+n
     * @param B: sorted integer array B which has n elements
     * @return: void
     */
    public void mergeSortedArray(int A[], int m, int B[], int n) {
        int index = n + m;

        while (m > 0 && n > 0) {
            if (A[m - 1] > B[n - 1]) {
                A[--index] = A[--m];
            } else {
                A[--index] = B[--n];
            }
        }
        while (n > 0) {
            A[--index] = B[--n];
        }
        while (m > 0) {
            A[--index] = A[--m];
        }
    }
};
```

### 源码分析

1. 因为本题有了 in-place 的限制，则必须从数组末尾的两个元素开始比较；否则就会产生挪动，一旦挪动就会是 $$O(n^2)$$ 的。

### C++

```c++
class Solution {
public:
    /**
     * @param A: sorted integer array A which has m elements,
     *           but size of A is m+n
     * @param B: sorted integer array B which has n elements
     * @return: void
     */
    void mergeSortedArray(int A[], int m, int B[], int n) {
        int index = n + m;

        while (m > 0 && n > 0) {
            if (A[m - 1] > B[n - 1]) {
                A[--index] = A[--m];
            } else {
                A[--index] = B[--n];
            }
        }
        while (n > 0) {
            A[--index] = B[--n];
        }
        while (m > 0) {
            A[--index] = A[--m];
        }
    }
};
```
