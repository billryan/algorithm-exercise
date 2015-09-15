# Merge Sorted Array

## Source

- lintcode: [(64) Merge Sorted Array](http://www.lintcode.com/en/problem/merge-sorted-array/)

```
Merge two given sorted integer array A and B into a new sorted integer array.

Example
A=[1,2,3,4]

B=[2,4,5,6]

return [1,2,2,3,4,4,5,6]

Challenge
How can you optimize your algorithm if one array is very large and the other is very small?
```

## 題解

自尾部向首部逐個比較兩個陣列內的元素，取較大的置於新陣列尾部元素中。

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

### 源碼分析

分三種情況遍歷比較。實際上在能確定最後返回的陣列時，只需要分兩次遍歷即可。

### 複雜度分析

最壞情況下需要遍歷兩個陣列中所有元素，時間複雜度為 $$O(n)$$. 空間複雜度 $$O(1)$$.


#### Challenge

兩個倒排列表，一個特別大，一個特別小，如何 Merge？此時應該考慮用一個二分法插入小的，即內存拷貝。

