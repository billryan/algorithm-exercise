# Find Peak Element

## Source

- lintcode: [(75) Find Peak Element](http://www.lintcode.com/en/problem/find-peak-element/)

```
There is an integer array which has the following features:

    * The numbers in adjacent positions are different.

    * A[0] < A[1] && A[A.length - 2] > A[A.length - 1].

We define a position P is a peek if A[P] > A[P-1] && A[P] > A[P+1].

Find a peak element in this array. Return the index of the peak.

Note
The array may contains multiple peeks, find any of them.

Example
[1, 2, 1, 3, 4, 5, 7, 6]

return index 1 (which is number 2)  or 6 (which is number 7)

Challenge
Time complexity O(logN)
```

## 题解

由时间复杂度的暗示可知应使用二分搜索。首先分析若使用传统的二分搜索，若`A[mid - 1] < A[mid] < A[mid + 1]`，则找到一个peak为A[mid]；若`A[mid - 1] > A[mid]`，则A[mid]左侧必定存在一个peak，可用反证法证明：若左侧不存在peak，则A[mid]左侧元素必满足`A[0] > A[1] > ... > A[mid -1] > A[mid]`，与已知`A[0] < A[1]`矛盾，证毕。同理可得若`A[mid + 1] > A[mid]`，则A[mid]右侧必定存在一个peak。如此迭代即可得解。

备注：如果本题是找 first/last peak，就不能用二分法了。

### C++

```c++
class Solution {
public:
    /**
     * @param A: An integers array.
     * @return: return any of peek positions.
     */
    int findPeak(vector<int> A) {
        if (A.empty()) {
            return -1;
        }

        vector<int>::size_type start = 0;
        vector<int>::size_type end = A.size() - 1;
        vector<int>::size_type mid;

        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (A[mid] < A[mid - 1]) {
                end = mid;
            } else if (A[mid] < A[mid + 1]) {
                start = mid;
            } else {
                return mid;
            }
        }
    }
};
```
