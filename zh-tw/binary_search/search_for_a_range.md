# Search for a Range

## Question

- lintcode: [(61) Search for a Range](http://www.lintcode.com/en/problem/search-for-a-range/)

```
Given a sorted array of integers, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
```

## 題解

Search for a range 的題目可以拆解為找 first & last position 的題目，即要做兩次二分。由上題二分查找可找到滿足條件的左邊界，因此只需要再將右邊界找出即可。注意到在`(target == nums[mid]`時賦值語句為`end = mid`，將其改為`start = mid`即可找到右邊界，解畢。

### Java

```java
/**
 * 本代碼fork自九章算法。沒有版權歡迎轉發。
 * http://www.jiuzhang.com/solutions/search-for-a-range/
 */
public class Solution {
    /**
     *@param A : an integer sorted array
     *@param target :  an integer to be inserted
     *return : a list of length 2, [index1, index2]
     */
    public ArrayList<Integer> searchRange(ArrayList<Integer> A, int target) {
        ArrayList<Integer> result = new ArrayList<Integer>();
        int start, end, mid;
        result.add(-1);
        result.add(-1);

        if (A == null || A.size() == 0) {
            return result;
        }

        // search for left bound
        start = 0;
        end = A.size() - 1;
        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (A.get(mid) == target) {
                end = mid; // set end = mid to find the minimum mid
            } else if (A.get(mid) > target) {
                end = mid;
            } else {
                start = mid;
            }
        }
        if (A.get(start) == target) {
            result.set(0, start);
        } else if (A.get(end) == target) {
            result.set(0, end);
        } else {
            return result;
        }

        // search for right bound
        start = 0;
        end = A.size() - 1;
        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (A.get(mid) == target) {
                start = mid; // set start = mid to find the maximum mid
            } else if (A.get(mid) > target) {
                end = mid;
            } else {
                start = mid;
            }
        }
        if (A.get(end) == target) {
            result.set(1, end);
        } else if (A.get(start) == target) {
            result.set(1, start);
        } else {
            return result;
        }

        return result;
        // write your code here
    }
}
```

### 源碼分析

1. 首先對輸入做異常處理，數組為空或者長度為0
2. 初始化 `start, end, mid`三個變量，注意mid的求值方法，可以防止兩個整型值相加時溢出
3. **使用迭代而不是遞歸**進行二分查找
4. while終止條件應為`start + 1 < end`而不是`start <= end`，`start == end`時可能出現死循環
5. 先求左邊界，迭代終止時先判斷`A.get(start) == target`，再判斷`A.get(end) == target`，因為迭代終止時target必取start或end中的一個，而end又大於start，取左邊界即為start.
6. 再求右邊界，迭代終止時先判斷`A.get(end) == target`，再判斷`A.get(start) == target`
7. 兩次二分查找除了終止條件不同，中間邏輯也不同，即當`A.get(mid) == target`如果是左邊界（first postion），中間邏輯是`end = mid`；若是右邊界（last position），中間邏輯是`start = mid`
8. 兩次二分查找中間勿忘記重置 `start, end` 的變量值。

### C++

```
class Solution {
    /** 
     *@param A : an integer sorted array
     *@param target :  an integer to be inserted
     *return : a list of length 2, [index1, index2]
     */
public:
    vector<int> searchRange(vector<int> &A, int target) {
        // good, fail are the result
        // When found, returns good, otherwise returns fail
        int N = A.size();
        vector<int> fail = {-1, -1};
        if(N == 0) 
            return fail;
        vector<int> good;
        
        // search for starting position
        int lo = 0, hi = N;
        while(lo < hi){
            int m = lo + (hi- lo)/2;
            if(A[m] < target)
                lo = m + 1;
            else
                hi = m;
        }
        
        if(A[lo] != target) 
            return fail;
            
        good.push_back(lo);
        
        // search for ending position
        lo = 0; hi = N;
        while(lo < hi){
            int m = lo + (hi - lo)/2;
            if(target < A[m])
                hi = m;
            else
                lo = m + 1;
        }
        good.push_back(lo - 1);
        
        return good;
    }
};
```

### 源碼分析

與前面題目類似，此題是將兩個子題組合起來，前半為找出"不小於target的最左元素"，後半是"不大於target的最右元素"，同樣的，使用開閉區間[lo, hi)仍然可以簡潔的處理各種邊界條件，僅須注意在解第二個子題"不大於target的最右元素"時，由於每次`lo`更新時都至少加1，最後會落在我們要求的位置的下一個，因此記得減1回來，若直覺難以理解，可以使用一個例子在紙上推一次每個步驟就可以體會。