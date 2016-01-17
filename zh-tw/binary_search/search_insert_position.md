# Search Insert Position

## Question

- lintcode: [(60) Search Insert Position](http://www.lintcode.com/en/problem/search-insert-position/)

```
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
```

## 題解

應該把二分法的問題拆解為`find the first/last position of...`的問題。由最原始的二分搜尋可找到不小於目標整數的最小下標。返回此下標即可。

### Java

```java
public class Solution {
    /**
     * param A : an integer sorted array
     * param target :  an integer to be inserted
     * return : an integer
     */
    public int searchInsert(int[] A, int target) {
        if (A == null) {
            return -1;
        }
        if (A.length == 0) {
            return 0;
        }

        int start = 0, end = A.length - 1;
        int mid;

        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (A[mid] == target) {
                return mid; // no duplicates, if not `end = target;`
            } else if (A[mid] < target) {
                start = mid;
            } else {
                end = mid;
            }
        }

        if (A[start] >= target) {
            return start;
        } else if (A[end] >= target) {
            return end; // in most cases
        } else {
            return end + 1; // A[end] < target;
        }
    }
}
```

### 源碼分析

要注意例子中的第三個, [1,3,5,6], 7 → 4，即找不到要找的數字的情況，此時應返回數組長度，即代碼中最後一個else的賦值語句`return end + 1;`

### C++
```c++
class Solution {
    /** 
     * param A : an integer sorted array
     * param target :  an integer to be inserted
     * return : an integer
     */
public:
    int searchInsert(vector<int> &A, int target) {
        int N = A.size();
        if (N == 0) return 0;
        if (A[N-1] < target) return N;
        int lo = 0, hi = N;
        while (lo < hi) {
            int mi = lo + (hi - lo)/2;
            if (A[mi] < target)
                lo = mi + 1;
            else
                hi = mi;
        }
        return lo;
    }
};

```

### 源碼分析
與lintcode - (14) Binary Search類似，在C++的解法裡我們也使用了[lo, hi)的表示方法，而題意是找出不小於`target`的最小位置，因此每次二分搜尋的循環裡如果發現`A[m]`已經小於`target`，就應該將下界`lo`往右推，其他狀況則將上界`hi`向左移動，然而必須注意的是如果`target`比陣列中所有元素都大，必須返回`ho`位置，然而此上下界的表示方法是不可能返回`ho`的，所以還有另外加一個判斷式，如果`target`已經大於陣列中最後一個元素，就直接返回其位置。
