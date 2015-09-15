# Merge Sorted Array II

## Source

- leetcode: [Merge Sorted Array | LeetCode OJ](https://leetcode.com/problems/merge-sorted-array/)
- lintcode: [(6) Merge Sorted Array II](http://www.lintcode.com/en/problem/merge-sorted-array-ii/)

```
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Note
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are mand n respectively.

Example
A = [1, 2, 3, empty, empty] B = [4,5]

After merge, A will be filled as [1,2,3,4,5]
```

## 題解

在上題的基礎上加入了in-place的限制。將上題的新陣列視為length相對較大的陣列即可，仍然從陣列末尾合併，取出較大的元素。

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

### 源碼分析

1. 因為本題有了 in-place 的限制，則必須從陣列末尾的兩個元素開始比較；否則就會產生挪動，一旦挪動就會是 $$O(n^2)$$ 的。

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
