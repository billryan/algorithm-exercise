# 2 Sum

## Question

- leetcode: [Two Sum | LeetCode OJ](https://leetcode.com/problems/two-sum/)
- lintcode: [(56) 2 Sum](http://www.lintcode.com/en/problem/2-sum/)

```
Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers
such that they add up to the target, where index1 must be less than index2.
Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
```

## 題解1 - 哈希表

找兩數之和是否為`target`, 如果是找數組中一個值為`target`該多好啊！遍歷一次就知道了，我只想說，too naive... 難道要將數組中所有元素的兩兩組合都求出來與`target`比較嗎？時間複雜度顯然為 $$O(n^2)$$, 顯然不符題目要求。找一個數時直接遍歷即可，那麼可不可以將兩個數之和轉換為找一個數呢？我們先來看看兩數之和為`target`所對應的判斷條件—— $$x_i + x_j = target$$, 可進一步轉化為 $$x_i = target - x_j$$, 其中 $$i$$ 和 $$j$$ 為數組中的下標。一段神奇的數學推理就將找兩數之和轉化為了找一個數是否在數組中了！可見數學是多麼的重要...

基本思路有了，現在就來看看怎麼實現，顯然我們需要額外的空間(也就是哈希表)來保存已經處理過的 $$x_j$$, 如果不滿足等式條件，那麼我們就往後遍歷，並把之前的元素加入到哈希表中，如果`target`減去當前索引後的值在哈希表中找到了，那麼就將哈希表中相應的索引返回，大功告成！

### C++

```c++
class Solution {
public:
    /*
     * @param numbers : An array of Integer
     * @param target : target = numbers[index1] + numbers[index2]
     * @return : [index1+1, index2+1] (index1 < index2)
     */
    vector<int> twoSum(vector<int> &nums, int target) {
        vector<int> result;
        const int length = nums.size();
        if (0 == length) {
            return result;
        }

        // first value, second index
        unordered_map<int, int> hash(length);
        for (int i = 0; i != length; ++i) {
            if (hash.find(target - nums[i]) != hash.end()) {
                result.push_back(hash[target - nums[i]]);
                result.push_back(i + 1);
                return result;
            } else {
                hash[nums[i]] = i + 1;
            }
        }

        return result;
    }
};
```

### 源碼分析

1. 異常處理。
2. 使用 C++ 11 中的哈希表實現`unordered_map`映射值和索引。
3. 找到滿足條件的解就返回，找不到就加入哈希表中。注意題中要求返回索引值的含義。

### 複雜度分析

哈希表用了和數組等長的空間，空間複雜度為 $$O(n)$$, 遍歷一次數組，時間複雜度為 $$O(n)$$.

### Python

```python
class Solution:
    """
    @param numbers : An array of Integer
    @param target : target = numbers[index1] + numbers[index2]
    @return : [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        hashdict = {}
        for i, item in enumerate(numbers):
            if (target - item) in hashdict:
                return (hashdict[target - item] + 1, i + 1)
            hashdict[item] = i

        return (-1, -1)
```

### 源碼分析

Python 中的`dict`就是天然的哈希表，使用 enumerate 可以同時返回索引和值，甚為方便。按題意似乎是要返回 list, 但個人感覺返回 tuple 更為合理。最後如果未找到符合題意的索引，返回`(-1, -1)`.

## 題解2 - 排序後使用兩根指針

但凡可以用空間換時間的做法，往往也可以使用時間換空間。另外一個容易想到的思路就是先對數組排序，然後使用兩根指針分別指向首尾元素，逐步向中間靠攏，直至找到滿足條件的索引為止。

### C++

```c++
class Solution {
public:
    /*
     * @param numbers : An array of Integer
     * @param target : target = numbers[index1] + numbers[index2]
     * @return : [index1+1, index2+1] (index1 < index2)
     */
    vector<int> twoSum(vector<int> &nums, int target) {
        vector<int> result;
        const int length = nums.size();
        if (0 == length) {
            return result;
        }

        // first num, second is index
        vector<pair<int, int> > num_index(length);
        // map num value and index
        for (int i = 0; i != length; ++i) {
            num_index[i].first = nums[i];
            num_index[i].second = i + 1;
        }

        sort(num_index.begin(), num_index.end());
        int start = 0, end = length - 1;
        while (start < end) {
            if (num_index[start].first + num_index[end].first > target) {
                --end;
            } else if(num_index[start].first + num_index[end].first == target) {
                int min_index = min(num_index[start].second, num_index[end].second);
                int max_index = max(num_index[start].second, num_index[end].second);
                result.push_back(min_index);
                result.push_back(max_index);
                return result;
            } else {
                ++start;
            }
        }

        return result;
    }
};
```

### 源碼分析

1. 異常處理。
2. 使用`length`保存數組的長度，避免反複調用`nums.size()`造成性能損失。
3. 使用`pair`組合排序前的值和索引，避免排序後找不到原有索引信息。
4. 使用標準庫函數排序。
5. 兩根指針指頭尾，逐步靠攏。

### 複雜度分析

遍歷一次原數組得到`pair`類型的新數組，時間複雜度為 $$O(n)$$, 空間複雜度也為 $$O(n)$$. 標准庫中的排序方法時間複雜度近似為 $$O(n \log n)$$, 兩根指針遍歷數組時間複雜度為 $$O(n)$$.

> **Note** lintcode 上的題要求時間複雜度在 $$O(n \log n)$$ 時，空間複雜度為 $$O(1)$$, 但問題是排序後索引會亂掉，如果要保存之前的索引，空間複雜度一定是 $$O(n)$$，所以個人認為不存在較為簡潔的 $$O(1)$$ 實現。如果一定要 $$O(n)$$ 的空間複雜度，那麼只能用暴搜了，此時的時間複雜度為 $$O(n^2)$$.
