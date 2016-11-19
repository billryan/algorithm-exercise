# 3 Sum

## Question

* leetcode: [3Sum \| LeetCode OJ](https://leetcode.com/problems/3sum/)
* lintcode: [\(57\) 3 Sum](http://www.lintcode.com/en/problem/3-sum/)

```
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Example
For example, given array S = {-1 0 1 2 -1 -4}, A solution set is:

(-1, 0, 1)
(-1, -1, 2)
Note
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)

The solution set must not contain duplicate triplets.
```

## 題解1 - 排序 + 哈希表 + 2 Sum

相比之前的 [2 Sum](http://algorithm.yuanbin.zh-hans/integer_array/2_sum.html), 3 Sum 又多加了一個數，按照之前 2 Sum 的分解為『1 Sum + 1 Sum』的思路，我們同樣可以將 3 Sum 分解為『1 Sum + 2 Sum』的問題，具體就是首先對原陣列排序，排序後選出第一個元素，隨後在剩下的元素中使用 2 Sum 的解法。

### Python

```python
class Solution:
    """
    @param numbersbers : Give an array numbersbers of n integer
    @return : Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        triplets = []
        length = len(numbers)
        if length < 3:
            return triplets

        numbers.sort()
        for i in xrange(length):
            target = 0 - numbers[i]
            # 2 Sum
            hashmap = {}
            for j in xrange(i + 1, length):
                item_j = numbers[j]
                if (target - item_j) in hashmap:
                    triplet = [numbers[i], target - item_j, item_j]
                    if triplet not in triplets:
                        triplets.append(triplet)
                else:
                    hashmap[item_j] = j

        return triplets
```

### 源碼分析

1. 異常處理，對長度小於3的直接返回。
2. 排序輸入陣列，有助於提高效率和返回有序列表。
3. 循環遍歷排序後陣列，先取出一個元素，隨後求得 2 Sum 中需要的目標數。
4. 由於本題中最後返回結果不能重複，在加入到最終返回值之前查重。

由於排序後的元素已經按照大小順序排列，且在2 Sum 中先遍歷的元素較小，所以無需對列表內元素再排序。

### 複雜度分析

排序時間複雜度 $$O(n \log n)$$, 兩重`for`循環，時間複雜度近似為 $$O(n^2)$$，使用哈希表\(字典\)實現，空間複雜度為 $$O(n)$$.

目前這段源碼為比較簡易的實現，leetcode 上的運行時間為500 + ms, 還有較大的優化空間，嗯，後續再進行優化。

### C++

```c++
class Solution {
public:
    vector<vector<int> > threeSum(vector<int> &num) 
    {
        vector<vector<int> > result;
        if (num.size() < 3) return result;

        int ans = 0;

        sort(num.begin(), num.end());

        for (int i = 0;i < num.size() - 2; ++i)
        {
            if (i > 0 && num[i] == num[i - 1])  
                continue;
            int j = i + 1;
            int k = num.size() - 1;

            while (j < k)
            {
                ans = num[i] + num[j] + num[k];

                if (ans == 0)
                {
                    result.push_back({num[i], num[j], num[k]});
                    ++j;
                    while (j < num.size() && num[j] == num[j - 1])
                        ++j;
                    --k;
                    while (k >= 0 && num[k] == num[k + 1])
                        --k;
                }
                else if (ans > 0) 
                    --k;
                else 
                    ++j;
            }
        }

        return result;
    }
};
```

### Java
```java
public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        // Assumptions: array is not null, array.length >= 3
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }
            int left = i + 1;
            int right = nums.length - 1;
            while (left < right) {
                int tmp = nums[left] + nums[right];
                if (tmp + nums[i] == 0) {
                    result.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;
                    while (left < right && nums[left] == nums[left - 1]) {
                        left++;
                    }
                } else if (tmp + nums[i] < 0) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        return result;
    }
}
```

### 源碼分析

同python解法不同，沒有使用hash map

```
S = {-1 0 1 2 -1 -4}
排序後：
S = {-4 -1 -1 0 1 2}
      ↑  ↑        ↑
      i  j        k
         →        ←
i每輪只走一步，j和k根據S[i]+S[j]+S[k]=ans和0的關係進行移動，且j只向後走（即S[j]只增大），k只向前走（即S[k]只減小）
如果ans>0說明S[k]過大，k向前移；如果ans<0說明S[j]過小，j向後移；ans==0即為所求。
至於如何取到所有解，看程式碼即可理解，不再贅述。
```

### 複雜度分析

外循環i走了n輪,每輪j和k一共走n-i步，所以時間複雜度為$$O(n^2)$$。
最終運行時間為52ms

## Reference

* [3Sum \| 九章算法](http://www.jiuzhang.com/solutions/3sum/)
* [A simply Python version based on 2sum - O\(n^2\) - Leetcode Discuss](https://leetcode.com/discuss/32455/a-simply-python-version-based-on-2sum-o-n-2)

