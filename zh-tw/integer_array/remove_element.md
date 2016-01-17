# Remove Element

## Question

- leetcode: [Remove Element | LeetCode OJ](https://leetcode.com/problems/remove-element/)
- lintcode: [(172) Remove Element](http://www.lintcode.com/en/problem/remove-element/)

```
Given an array and a value, remove all occurrences of that value in place and return the new length.

The order of elements can be changed, and the elements after the new length don't matter.

Example
Given an array [0,4,4,0,0,2,4,4], value=4

return 4 and front four elements of the array is [0,0,0,2]
```

## 題解1 - 使用容器

入門題，返回刪除指定元素後的陣列長度，使用容器操作非常簡單。以 lintcode 上給出的參數為例，遍歷容器內元素，若元素值與給定刪除值相等，刪除當前元素並往後繼續遍歷。
C++的vector已經支援了刪除操作，因此可以直接拿來使用。
### C++

```c++
class Solution {
public:
    /**
     *@param A: A list of integers
     *@param elem: An integer
     *@return: The new length after remove
     */
    int removeElement(vector<int> &A, int elem) {
        for (vector<int>::iterator iter = A.begin(); iter < A.end(); ++iter) {
            if (*iter == elem) {
                iter = A.erase(iter);
                --iter;
            }
        }

        return A.size();
    }
};

```

### 源碼分析

注意在遍歷容器內元素和指定欲刪除值相等時，需要先自減`--iter`, 因為`for`循環會對`iter`自增，`A.erase()`刪除當前元素值並返回指向下一個元素的指針，一增一減正好平衡。如果改用`while`循環，則需注意訪問陣列時是否越界。

### 複雜度分析

<!--- 沒啥好分析的，遍歷一次陣列 $$O(n)$$. -->
由於vector每次erase的複雜度是$$O(n)$$，我們遍歷整個向量，最壞情況下，每個元素都與要刪除的目標元素相等，每次都要刪除元素的複雜度高達$$O(n^2)$$
觀察此方法會如此低效的原因，是因為我們一次只刪除一個元素，導致很多沒必要的元素交換移動，如果能夠將要刪除的元素集中處理，則可以大幅增加效率，見題解2。

### 題解2 - 兩根指針

由於題中明確暗示元素的順序可變，且新長度後的元素不用理會。我們可以使用兩根指針分別往前往後遍歷，頭指針用於指示當前遍歷的元素位置，尾指針則用於在當前元素與欲刪除值相等時替換當前元素，兩根指針相遇時返回尾指針索引——即刪除元素後「新陣列」的長度。

### C++

```c++
class Solution {
public:
    int removeElement(int A[], int n, int elem) {
        for (int i = 0; i < n; ++i) {
            if (A[i] == elem) {
                A[i] = A[n - 1];
                --i;
                --n;
            }
        }

        return n;
    }
};
```

### 源碼分析

遍歷當前陣列，`A[i] == elem`時將陣列「尾部(以 n 為長度時的尾部)」元素賦給當前遍歷的元素。同時自減`i`和`n`，原因見題解1的分析。需要注意的是`n`在遍歷過程中可能會變化。

### 複雜度分析

此方法只遍歷一次陣列，且每個循環的操作至多也不過僅是常數次，因此時間複雜度是$$O(n)$$。

## Reference

- [Remove Element | 九章算法](http://www.jiuzhang.com/solutions/remove-element/)
