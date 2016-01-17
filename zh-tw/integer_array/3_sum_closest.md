# 3 Sum Closest

## Question

- leetcode: [3Sum Closest | LeetCode OJ](https://leetcode.com/problems/3sum-closest/)
- lintcode: [(59) 3 Sum Closest](http://www.lintcode.com/en/problem/3-sum-closest/)

```
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. 
Return the sum of the three integers. You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
```
## 題解1 - 排序 + 2 Sum + 兩根指標 + 優化過濾

和 3 Sum 的思路接近，首先對原陣列排序，隨後將3 Sum 的題拆解為『1 Sum + 2 Sum』的題，對於 Closest 的題使用兩根指標而不是哈希表的方法較為方便。對於有序陣列來說，在查找 Cloest 的值時其實是有較大的優化空間的。

### Python

```python
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        result = 2**31 - 1
        length = len(numbers)
        if length < 3:
            return result

        numbers.sort()
        larger_count = 0
        for i, item_i in enumerate(numbers):
            start = i + 1
            end = length - 1
            # optimization 1 - filter the smallest sum greater then target
            if start < end:
                sum3_smallest = numbers[start] + numbers[start + 1] + item_i
                if sum3_smallest > target:
                    larger_count += 1
                    if larger_count > 1:
                        return result

            while (start < end):
                sum3 = numbers[start] + numbers[end] + item_i
                if abs(sum3 - target) < abs(result - target):
                    result = sum3

                # optimization 2 - filter the sum3 closest to target
                sum_flag = 0
                if sum3 > target:
                    end -= 1
                    if sum_flag == -1:
                        break
                    sum_flag = 1
                elif sum3 < target:
                    start += 1
                    if sum_flag == 1:
                        break
                    sum_flag = -1
                else:
                    return result

        return result
```

### 源碼分析

1. leetcode 上不能自己導入`sys`包，保險起見就初始化了`result`為還算較大的數，作為異常的返回值。
2. 對陣列進行排序。
3. 依次遍歷排序後的陣列，取出一個元素`item_i`後即轉化為『2 Sum Cloest』問題。『2 Sum Cloest』的起始元素索引為`i + 1`，之前的元素不能參與其中。
4. 優化一——由於已經對原陣列排序，故遍歷原陣列時比較最小的三個元素和`target`值，若第二次大於`target`果斷就此罷休，後面的值肯定越來越大。
5. 兩根指標求『2 Sum Cloest』，比較`sum3`和`result`與`target`的差值的絕對值，更新`result`為較小的絕對值。
6. 再度對『2 Sum Cloest』進行優化，仍然利用有序陣列的特點，若處於『一大一小』的臨界值時就可以馬上退出了，後面的元素與`target`之差的絕對值只會越來越大。

### 複雜度分析

對原陣列排序，平均時間複雜度為 $$O(n \log n)$$, 兩重`for`循環，由於有兩處優化，故最壞的時間複雜度才是 $$O(n^2)$$, 使用了`result`作為臨時值保存最接近`target`的值，兩處優化各使用了一個輔助變量，空間複雜度 $$O(1)$$.

### C++

```c++
class Solution {
public:
    int threeSumClosest(vector<int> &num, int target) 
    {
        if (num.size() <= 3) return accumulate(num.begin(), num.end(), 0);
        sort (num.begin(), num.end());

        int result = 0, n = num.size(), temp;
        result = num[0] + num[1] + num[2];
        for (int i = 0; i < n - 2; ++i)
        {
            int j = i + 1, k = n - 1;
            while (j < k)
            {
                temp = num[i] + num[j] + num[k];
                
                if (abs(target - result) > abs(target - temp))
                    result = temp;
                if (result == target)
                    return result;
                ( temp > target ) ? --k : ++j;
            }
        }
        return result;
    }
};
```
### 源碼分析

和前面3Sum解法相似，同理使用i,j,k三個指標進行循環。<br>
區別在於3sum中的target為0，這裡新增一個變數用於比較哪組數據與target更為相近，並讓相對應的指標調整使之更近。

### 複雜度分析

時間複雜度同理為$$O(n^2)$$
運行時間 16ms

## Reference

- [3Sum Closest | 九章算法](http://www.jiuzhang.com/solutions/3sum-closest/)
