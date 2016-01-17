# Merge Sorted Array

## Question

- leetcode: [Merge Sorted Array | LeetCode OJ](https://leetcode.com/problems/merge-sorted-array/)
- lintcode: [(6) Merge Sorted Array](http://www.lintcode.com/en/problem/merge-sorted-array/)

```
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Example
A = [1, 2, 3, empty, empty], B = [4, 5]

After merge, A will be filled as [1, 2, 3, 4, 5]

Note
You may assume that A has enough space (size that is greater or equal to m + n)
to hold additional elements from B.
The number of elements initialized in A and B are m and n respectively.
```

## 题解

因为本题有 in-place 的限制，故必须从数组末尾的两个元素开始比较；否则就会产生挪动，一旦挪动就会是 $$O(n^2)$$ 的。
自尾部向首部逐个比较两个数组内的元素，取较大的置于数组 A 中。由于 A 的容量较 B 大，故最后 `m == 0` 或者 `n == 0` 时仅需处理 B 中的元素，因为 A 中的元素已经在 A 中，无需处理。

### Python

```python
class Solution:
    """
    @param A: sorted integer array A which has m elements,
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return: void
    """
    def mergeSortedArray(self, A, m, B, n):
        if B is None:
            return A

        index = m + n - 1
        while m > 0 and n > 0:
            if A[m - 1] > B[n - 1]:
                A[index] = A[m - 1]
                m -= 1
            else:
                A[index] = B[n - 1]
                n -= 1
            index -= 1

        # B has elements left
        while n > 0:
            A[index] = B[n - 1]
            n -= 1
            index -= 1
```

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
        int index = m + n - 1;
        while (m > 0 && n > 0) {
            if (A[m - 1] > B[n - 1]) {
                A[index] = A[m - 1];
                --m;
            } else {
                A[index] = B[n - 1];
                --n;
            }
            --index;
        }

        // B has elements left
        while (n > 0) {
            A[index] = B[n - 1];
            --n;
            --index;
        }
    }
};
```

### Java

```java
class Solution {
    /**
     * @param A: sorted integer array A which has m elements,
     *           but size of A is m+n
     * @param B: sorted integer array B which has n elements
     * @return: void
     */
    public void mergeSortedArray(int[] A, int m, int[] B, int n) {
        if (A == null || B == null) return;

        int index = m + n - 1;
        while (m > 0 && n > 0) {
            if (A[m - 1] > B[n - 1]) {
                A[index] = A[m - 1];
                m--;
            } else {
                A[index] = B[n - 1];
                n--;
            }
            index--;
        }

        // B has elements left
        while (n > 0) {
            A[index] = B[n - 1];
            n--;
            index--;
        }
    }
}
```

### 源码分析

第一个 while 只能用条件与。

### 复杂度分析

最坏情况下需要遍历两个数组中所有元素，时间复杂度为 $$O(n)$$. 空间复杂度 $$O(1)$$.

