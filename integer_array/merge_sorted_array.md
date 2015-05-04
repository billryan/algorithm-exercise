# Merge Sorted Array

## Source

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

逐个比较两个数组内的元素，取较大的置于新数组尾部元素中。

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

分三种情况遍历比较。

#### Challenge

两个倒排列表，一个特别大，一个特别小，如何 Merge？此时应该考虑用一个二分法插入小的，即内存拷贝。

