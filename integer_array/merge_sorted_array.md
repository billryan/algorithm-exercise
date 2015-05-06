# Merge Sorted Array

## Source

- leetcode: [Merge Sorted Array | LeetCode OJ](https://leetcode.com/problems/merge-sorted-array/)
- lintcode: [(6) Merge Sorted Array](http://www.lintcode.com/en/problem/merge-sorted-array/)

```
Merge two given sorted integer array A and B into a new sorted integer array.

Example
A=[1,2,3,4]

B=[2,4,5,6]

return [1,2,2,3,4,4,5,6]

Challenge
How can you optimize your algorithm if one array is very large and the other is very small?
```

## 题解

自尾部向首部逐个比较两个数组内的元素，取较大的置于新数组尾部元素中。

### Python

```python
class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        # resize nums1 to required size
        nums1 += [0] * (n + m - len(nums1))
        index = m + n
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                index -= 1
                m -= 1
                nums1[index] = nums1[m]
            else:
                index -= 1
                n -= 1
                nums1[index] = nums2[n]

        while n > 0:
            index -= 1
            n -= 1
            nums1[index] = nums2[n]
```

### Java

```java
class Solution {
    /**
     * @param A and B: sorted integer array A and B.
     * @return: A new sorted integer array
     */
    public ArrayList<Integer> mergeSortedArray(ArrayList<Integer> A, ArrayList<Integer> B) {
        // write your code here
        int aLen = A.size();
        int bLen = B.size();
        ArrayList<Integer> res = new ArrayList<Integer>();

        int i = 0, j = 0;
        while (i < aLen || j < bLen) {
            if (i == aLen) {
                res.add(B.get(j++));
                continue;
            } else if (j == bLen) {
                res.add(A.get(i++));
                continue;
            }

            if (A.get(i) < B.get(j)) {
                res.add(A.get(i++));
            } else {
                res.add(B.get(j++));
            }
        }
        return res;
    }
}
```

### C++

```c++
class Solution {
public:
    /**
     * @param A and B: sorted integer array A and B.
     * @return: A new sorted integer array
     */
    vector<int> mergeSortedArray(vector<int> &A, vector<int> &B) {
        if (A.empty()) {
            return B;
        }
        if (B.empty()) {
            return A;
        }

        vector<int>::size_type sizeA = A.size();
        vector<int>::size_type sizeB = B.size();
        vector<int>::size_type sizeC = sizeA + sizeB;
        vector<int> C(sizeC);

        while (sizeA > 0 && sizeB > 0) {
            if (A[sizeA - 1] > B[sizeB - 1]) {
                C[--sizeC] = A[--sizeA];
            } else {
                C[--sizeC] = B[--sizeB];
            }
        }
        while (sizeA > 0) {
            C[--sizeC] = A[--sizeA];
        }
        while (sizeB > 0) {
            C[--sizeC] = B[--sizeB];
        }

        return C;
    }
};
```

### 源码分析

分三种情况遍历比较。实际上在能确定最后返回的数组时，只需要分两次遍历即可。

### 复杂度分析

最坏情况下需要遍历两个数组中所有元素，时间复杂度为 $$O(n)$$. 空间复杂度 $$O(1)$$.

#### Challenge

两个倒排列表，一个特别大，一个特别小，如何 Merge？此时应该考虑用一个二分法插入小的，即内存拷贝。

