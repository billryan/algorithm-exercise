# Find Peak Element

## Question

- leetcode: [Find Peak Element | LeetCode OJ](https://leetcode.com/problems/find-peak-element/)
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

## 題解1 - lintcode

由時間複雜度的暗示可知應使用二分搜索。首先分析若使用傳統的二分搜索，若`A[mid] > A[mid - 1] && A[mid] < A[mid + 1]`，則找到一個peak為A[mid]；若`A[mid - 1] > A[mid]`，則A[mid]左側必定存在一個peak，可用反證法證明：若左側不存在peak，則A[mid]左側元素必滿足`A[0] > A[1] > ... > A[mid -1] > A[mid]`，與已知`A[0] < A[1]`矛盾，證畢。同理可得若`A[mid + 1] > A[mid]`，則A[mid]右側必定存在一個peak。如此迭代即可得解。

備注：如果本題是找 first/last peak，就不能用二分法了。

### Python

```python
class Solution:
    #@param A: An integers list.
    #@return: return any of peek positions.
    def findPeak(self, A):
        if not A:
            return -1

        l, r = 0, len(A) - 1
        while l + 1 < r:
            mid = l + (r - l) / 2
            if A[mid] < A[mid - 1]:
                r = mid
            elif A[mid] < A[mid + 1]:
                l = mid
            else:
                return mid
        mid = l if A[l] > A[r] else r
        return mid
```

### C++

```c++
class Solution {
public:
    /**
     * @param A: An integers array.
     * @return: return any of peek positions.
     */
    int findPeak(vector<int> A) {
        if (A.size() == 0) return -1;

        int l = 0, r = A.size() - 1;
        while (l + 1 < r) {
            int mid = l + (r - l) / 2;
            if (A[mid] < A[mid - 1]) {
                r = mid;
            } else if (A[mid] < A[mid + 1]) {
                l = mid;
            } else {
                return mid;
            }
        }

        int mid = A[l] > A[r] ? l : r;
        return mid;
    }
};
```

### Java

```java
class Solution {
    /**
     * @param A: An integers array.
     * @return: return any of peek positions.
     */
    public int findPeak(int[] A) {
        if (A == null || A.length == 0) return -1;

        int l = 0, r = A.length - 1;
        while (l + 1 < r) {
            int mid = l + (r - l) / 2;
            if (A[mid] < A[mid - 1]) {
                r = mid;
            } else if (A[mid] < A[mid + 1]) {
                l = mid;
            } else {
                return mid;
            }
        }

        int mid = A[l] > A[r] ? l : r;
        return mid;
    }
}
```

## 題解2 - leetcode

leetcode 上的題和 lintcode 上有細微的變化，題目如下：

```
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1],
find a peak element and return its index.

The array may contain multiple peaks,
in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and
your function should return the index number 2.

click to show spoilers.

Note:
Your solution should be in logarithmic complexity.
```

如果一開始做的是 leetcode 上的版本而不是 lintcode 上的話，這道題難度要大一些。有了以上的分析基礎再來刷 leetcode 上的這道題就是小 case 了，注意題中的關鍵提示`num[-1] = num[n] = -∞`, 雖然不像 lintcode 上那麼直接，但是稍微變通下也能想到。即`num[-1] < num[0] && num[n-1] > num[n]`, 那麼問題來了，這樣一來就不能確定峰值一定存在了，因為給定數組為單調序列的話就咩有峰值了，但是實際情況是——題中有負無窮的假設，也就是說在單調序列的情況下，峰值為數組首部或者尾部元素，誰大就是誰了。

### C++

```C++
class Solution {
public:
    int findPeakElement(vector<int>& arr) {
        int N = arr.size();
    	int lo = 0, hi = N;
	    while(lo < hi) {
		    int mi = lo + (hi - lo)/2;
    		if( (mi == 0 || arr[mi-1] <= arr[mi] ) && (mi == N-1 || arr[mi] >= arr[mi+1]) ) 
	    		return mi;
		    else if((mi == 0 || arr[mi-1] <= arr[mi] ))
			    lo = mi + 1;
    		else
	    		hi = mi;
	    }
	    return -1;
    }
};
```

### Java

```java
public class Solution {
    public int findPeakElement(int[] nums) {
        if (nums == null || nums.length == 0) return -1;

        int l = 0, r = nums.length - 1;
        while (l + 1 < r) {
            mid = l + (r - l) / 2;
            if (nums[mid] < nums[mid - 1]) {
                // 1 peak at least in the left side
                r = mid;
            } else if (nums[mid] < nums[mid + 1]) {
                // 1 peak at least in the right side
                l = mid;
            } else {
                return mid;
            }
        }

        mid = nums[l] > nums[r] ? l : r;
        return mid;
    }
}
```

### 源碼分析

典型的二分法模板應用，需要注意的是需要考慮單調序列的特殊情況。當然也可使用緊湊一點的實現如改寫循環條件為`l < r`，這樣就不用考慮單調序列了，見實現2.

### 複雜度分析

二分法，時間複雜度 $$O(\log n)$$.

### Java - compact implementation[^leetcode_discussion]

```java
public class Solution {
    public int findPeakElement(int[] nums) {
        if (nums == null || nums.length == 0) {
            return -1;
        }

        int start = 0, end = nums.length - 1, mid = end / 2;
        while (start < end) {
            if (nums[mid] < nums[mid + 1]) {
                // 1 peak at least in the right side
                start = mid + 1;
            } else {
                // 1 peak at least in the left side
                end = mid;
            }
            mid = start + (end - start) / 2;
        }

        return start;
    }
}
```

C++ 的代碼可參考 Java 或者 @xuewei4d 的實現。

> **Warning** leetcode 和 lintcode 上給的方法名不一樣，leetcode 上的為`findPeakElement`而 lintcode 上為`findPeak`，弄混的話會編譯錯誤。

## Reference

- [^leetcode_discussion]: [Java - Binary-Search Solution - Leetcode Discuss](https://leetcode.com/discuss/23840/java-binary-search-solution)
