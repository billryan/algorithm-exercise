# Subsets - 子集

## Question

- leetcode: [Subsets | LeetCode OJ](https://leetcode.com/problems/subsets/)
- lintcode: [(17) Subsets](http://www.lintcode.com/en/problem/subsets/)

```
Given a set of distinct integers, return all possible subsets.

Note
Elements in a subset must be in non-descending order.

The solution set must not contain duplicate subsets.

Example
If S = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
```

## 題解

子集類問題類似Combination，以輸入陣列`[1, 2, 3]`分析，根據題意，最終返回結果中子集類的元素應該按照升序排列，故首先需要對原陣列進行排序。題目的第二點要求是子集不能重複，至此原題即轉化為數學中的組合問題。我們首先嘗試使用 DFS 進行求解，大致步驟如下：

1. `[1] -> [1, 2] -> [1, 2, 3]`
2. `[2] -> [2, 3]`
3. `[3]`

將上述過程轉化為程式碼即為對陣列遍歷，每一輪都保存之前的結果並將其依次加入到最終返回結果中。

### Python

```python
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        if nums is None:
            return []
        
        result = []
        nums.sort()
        self.dfs(nums, 0, [], result)
        return result
    
    def dfs(self, nums, pos, list_temp, ret):
        # append new object with []
        ret.append([] + list_temp)
        
        for i in xrange(pos, len(nums)):
            list_temp.append(nums[i])
            self.dfs(nums, i + 1, list_temp, ret)
            list_temp.pop()
```

### C++

```c++
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int> > result;
        if (nums.empty()) return result;
        
        sort(nums.begin(), nums.end());
        vector<int> list;
        dfs(nums, 0, list, result);
        
        return result;
    }

private:
    void dfs(vector<int>& nums, int pos, vector<int> &list,
             vector<vector<int> > &ret) {
        
        ret.push_back(list);
        
        for (int i = pos; i < nums.size(); ++i) {
            list.push_back(nums[i]);
            dfs(nums, i + 1, list, ret);
            list.pop_back();
        }
    }
};
```

### Java

```java
public class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        List<Integer> list = new ArrayList<Integer>();
        if (nums == null || nums.length == 0) {
            return result;
        }
        
        Arrays.sort(nums);
        dfs(nums, 0, list, result);
        
        return result;
    }
    
    private void dfs(int[] nums, int pos, List<Integer> list,
                     List<List<Integer>> ret) {

        // add temp result first
        ret.add(new ArrayList<Integer>(list));
        
        for (int i = pos; i < nums.length; i++) {
            list.add(nums[i]);
            dfs(nums, i + 1, list, ret);
            list.remove(list.size() - 1);
        }
    }
}
```

### 源碼分析

Java 和 Python 的程式碼中在將臨時list 添加到最終結果時新生成了物件，(Python 使用`[] + `), 否則最終返回結果將隨著`list` 的變化而變化。

**Notice: backTrack(num, i + 1, list, ret);中的『i + 1』不可誤寫為『pos + 1』，因為`pos`用於每次大的循環，`i`用於內循環，第一次寫subsets的時候在這坑了很久... :(**

回溯法可用圖示和函數運行的堆棧圖來理解，強烈建議**使用圖形和遞迴的思想**分析，以陣列`[1, 2, 3]`進行分析。下圖所示為`list`及`result`動態變化的過程，箭頭向下表示`list.add`及`result.add`操作，箭頭向上表示`list.remove`操作。

![Subsets運行遞迴調用圖](../../shared-files/images/subsets.jpg)

### 複雜度分析

對原有陣列排序，時間複雜度近似為 $$O(n \log n)$$. 狀態數為所有可能的組合數 $$O(2^n)$$, 生成每個狀態所需的時間複雜度近似為 $$O(1)$$, 如`[1] -> [1, 2]`, 故總的時間複雜度近似為 $$O(2^n)$$.

使用了臨時空間`list`保存中間結果，`list` 最大長度為陣列長度，故空間複雜度近似為 $$O(n)$$.

## Reference

- [[NineChap 1.2] Permutation - Woodstock Blog](http://okckd.github.io/blog/2014/06/12/NineChap-Permutation/)
- [九章算法 - subsets模板](http://www.jiuzhang.com/solutions/subsets/)
- [LeetCode: Subsets 解題報告 - Yu's Garden - 博客園](http://www.cnblogs.com/yuzhangcmu/p/4211815.html)
