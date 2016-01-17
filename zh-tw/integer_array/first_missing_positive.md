# First Missing Positive

## Question

- leetcode: [First Missing Positive | LeetCode OJ](https://leetcode.com/problems/first-missing-positive/)
- lintcode: [(189) First Missing Positive](http://www.lintcode.com/en/problem/first-missing-positive/)

```
Given an unsorted integer array, find the first missing positive integer.

Example
Given [1,2,0] return 3, and [3,4,-1,1] return 2.

Challenge
Your algorithm should run in O(n) time and uses constant space.
```

## 題解

容易想到的方案是先排序，然後遍歷求得缺的最小整數。排序算法中常用的基於比較的方法時間複雜度的理論下界為 $$O(n \log n)$$, 不符題目要求。常見的能達到線性時間複雜度的排序算法有 [基數排序](http://zh.wikipedia.org/wiki/%E5%9F%BA%E6%95%B0%E6%8E%92%E5%BA%8F)，[計數排序](http://algorithm.yuanbin.zh-hans/basics_sorting/counting_sort.html) 和 [桶排序](http://algorithm.yuanbin.zh-hans/basics_sorting/bucket_sort.html)。

基數排序顯然不太適合這道題，計數排序對元素落在一定區間且重複值較多的情況十分有效，且需要額外的 $$O(n)$$ 空間，對這道題不太合適。最後就只剩下桶排序了，桶排序通常需要按照一定規則將值放入桶中，一般需要額外的 $$O(n)$$ 空間，乍看之下似乎不太適合在這道題中使用，但是若能設定一定的規則原地交換原數組的值呢？這道題的難點就在於這種規則的設定。

設想我們對給定數組使用桶排序的思想排序，第一個桶放1，第二個桶放2，如果找不到相應的數，則相應的桶的值不變(可能為負值，也可能為其他值)。

那麼怎麼才能做到原地排序呢？即若 $$A[i] = x$$, 則將 x 放到它該去的地方 - $$A[x - 1] = x$$, 同時將原來 $$A[x - 1]$$ 地方的值交換給 $$A[i]$$.

排好序後遍歷桶，如果不滿足 $$f[i] = i + 1$$, 那麼警察叔叔就是它了！如果都滿足條件怎麼辦？那就返回給定數組大小再加1唄。

### C++

```c++
class Solution {
public:
    /**
     * @param A: a vector of integers
     * @return: an integer
     */
    int firstMissingPositive(vector<int> A) {
        const int size = A.size();

        for (int i = 0; i < size; ++i) {
            while (0 < A[i]  && A[i] <= size &&
                  (A[i] != i + 1) && (A[i] != A[A[i] - 1])) {
                int temp = A[A[i] - 1];
                A[A[i] - 1] = A[i];
                A[i] = temp;
            }
        }

        for (int i = 0; i < size; ++i) {
            if (A[i] != i + 1) {
                return i + 1;
            }
        }

        return size + 1;
    }
};
```

### 源碼分析

核心程式為那幾行交換，但是要正確處理各種邊界條件則要下一番功夫了，要能正常的交換，需滿足以下幾個條件：

1. `A[i]` 為正數，負數和零都無法在桶中找到生存空間...
2. `A[i] \leq size` 當前索引處的值不能比原陣列容量大，大了的話也沒用啊，一定不是缺的第一個正數。
3. `A[i] != i + 1`, 都滿足條件了就不用交換了。
4. `A[i] != A[A[i] - 1]`, 避免欲交換的值和自身相同，否則有重複值時會產生死循環。

如果滿足以上四個條件就可以愉快地交換彼此了，使用`while`循環處理，此時`i`並不自增，直到將所有滿足條件的索引處理完。

注意交換的寫法，若寫成

```c
int temp = A[i];
A[i] = A[A[i] - 1];
A[A[i] - 1] = temp;
```

這又是滿滿的 bug :( 因為在第三行中`A[i]`已不再是之前的值，第二行賦值時已經改變，故源碼中的寫法比較安全。

最後遍歷桶排序後的數組，若在數組大小範圍內找到不滿足條件的解，直接返回，否則就意味著原數組給的元素都是從1開始的連續正整數，返回數組大小加1即可。

### 複雜度分析

「桶排序」需要遍歷一次原數組，考慮到`while`循環也需要一定次數的遍歷，故時間複雜度至少為 $$O(n)$$. 最後求索引值最多遍歷一次排序後數組，時間複雜度最高為 $$O(n)$$, 用到了`temp`作為中間交換，空間複雜度為 $$O(1)$$.

## Reference

- [Find First Missing Positive | N00tc0d3r](http://n00tc0d3r.blogspot.com/2013/03/find-first-missing-positive.html)
- [LeetCode: First Missing Positive 解題報告 - Yu's Garden - 博客園](http://www.cnblogs.com/yuzhangcmu/p/4200096.html)
- [First Missing Positive | 九章算法](http://www.jiuzhang.com/solutions/first-missing-positive/)
