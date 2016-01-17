# Binary Search - 二分搜尋

## Question

- lintcode: [lintcode - (14) Binary Search](http://www.lintcode.com/en/problem/binary-search/)

```
Binary search is a famous question in algorithm.

For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time complexity.

If the target number does not exist in the array, return -1.

Example
If the array is [1, 2, 3, 3, 4, 5, 10], for given target 3, return 2.

Challenge
If the count of numbers is bigger than MAXINT, can your code work properly?
```

## 題解

對於已排序升序陣列，使用二分搜尋可滿足複雜度要求，注意陣列中可能有重複值。

### Java

```java
/**
 * 本代碼fork自九章算法。沒有版權歡迎轉發。
 * http://www.jiuzhang.com//solutions/binary-search/
 */
class Solution {
    /**
     * @param nums: The integer array.
     * @param target: Target to find.
     * @return: The first position of target. Position starts from 0.
     */
    public int binarySearch(int[] nums, int target) {
        if (nums == null || nums.length == 0) {
            return -1;
        }

        int start = 0;
        int end = nums.length - 1;
        int mid;
        while (start + 1 < end) {
            mid = start + (end - start) / 2; // avoid overflow when (end + start)
            if (target < nums[mid]) {
                end = mid;
            } else if (target > nums[mid]) {
                start = mid;
            } else {
                end = mid;
            }
        }

        if (nums[start] == target) {
            return start;
        }
        if (nums[end] == target) {
            return end;
        }

        return -1;
    }
}
```

### 源碼分析

1. 首先對輸入做異常處理，陣列為空或者長度為0。
2. 初始化 `start, end, mid`三個變量，注意mid的求值方法，可以防止兩個整型值相加時溢出。
3. **使用迭代而不是遞迴**進行二分搜尋，因為工程中遞迴寫法存在潛在溢出的可能。
4. while終止條件應為`start + 1 < end`而不是`start <= end`，`start == end`時可能出現死循環。**即循環終止條件是相鄰或相交元素時退出。**
5. 迭代終止時target應為start或者end中的一個——由上述循環終止條件有兩個，具體誰先誰後視題目是找 first position or last position 而定。
6. 賦值語句`end = mid`有兩個條件是相同的，可以選擇寫到一塊。
7. 配合while終止條件`start + 1 < end`（相鄰即退出）的賦值語句mid永遠沒有`+1`或者`-1`，這樣不會死循環。

### C++

```c++
class Solution {
public:
    /**
     * @param nums: The integer array.
     * @param target: Target number to find.
     * @return: The first position of target. Position starts from 0. 
     */
    int binarySearch(vector<int> &nums, int target) {
        if( nums.size() == 0 ) return -1;
    
        int lo = 0, hi = nums.size();
        while(lo < hi){
            int mi = lo + (hi - lo)/2;
            if(nums[mi] < target)
                lo = mi + 1;
            else
                hi = mi;
        }
        
        if(nums[lo] == target) return lo;
        return -1;
    }
};

```
### 源碼分析

遇到需要處理陣列範圍的問題，由於C/C++語言本身的特性，統一使用開閉區間表示index範圍將有許多好處，[lo, hi)表示包含lo但不包含hi的區間。比方說，如果要遍歷這個區間，迴圈的條件可以寫為`for(i = lo; i < hi; i++)`這類常用的方式，如果要求此段區間長度可用`int length = hi - lo;`，另外在很多邊界條件的判斷上也會比較簡潔。實際上在STL裡的iterator也是使用了用類似的概念，一個容器的end()表示的是一個已經超出指定範圍的iterator。以此題來說，可以看出C++的實現方法確實比較簡潔。

1. 終止條件簡單設定為`lo < hi`，事實上觀察調整`lo`與`hi`範圍的過程，終止的時候一定是`lo == hi`。
2. 觀察`lo`的更新條件，是當`nums[mi]`比目標值小時將`lo`更新為`mi + 1`，也就是說，`lo`可以保證下界一定會不斷排除比`target`小的值，其餘狀況每次循環`hi`則減少範圍，因此等到循環終止之後，`lo`就會指到**不小於`target`的最小元素**，我們再將這個元素與`target`比較，就知道是否有找到，沒有的話就返回-1