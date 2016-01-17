# Sqrt x

## Question

- leetcode: [Sqrt(x) | LeetCode OJ](https://leetcode.com/problems/sqrtx/)
- lintcode: [(141) Sqrt(x)](http://www.lintcode.com/en/problem/sqrtx/)

## 題解 - 二分搜索

由於只需要求整數部分，故對於任意正整數 $$x$$, 設其整數部分為 $$k$$, 顯然有 $$1 \leq k \leq x$$, 求解 $$k$$ 的值也就轉化為了在有序陣列中查找滿足某種約束條件的元素，顯然二分搜索是解決此類問題的良方。

### Python

```python
class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if x < 0:
            return -1
        elif x == 0:
            return 0

        start, end = 1, x
        while start + 1 < end:
            mid = start + (end - start) / 2
            if mid**2 == x:
                return mid
            elif mid**2 > x:
                end = mid
            else:
                start = mid

        return start
```

### 源碼分析

1. 異常檢測，先處理小於等於0的值。
2. 使用二分搜索的經典模板，注意不能使用`start < end`, 否則在給定值1時產生死循環。
3. 最後返回平方根的整數部分`start`.

二分搜索過程很好理解，關鍵是最後的返回結果還需不需要判斷？比如是取 start, end, 還是 mid? 我們首先來分析下二分搜索的循環條件，由`while`循環條件`start + 1 < end`可知，`start`和`end`只可能有兩種關系，一個是`end == 1 || end ==2`這一特殊情況，返回值均為1，另一個就是循環終止時`start`恰好在`end`前一個元素。設值 x 的整數部分為 k, 那麼在執行二分搜索的過程中 $$ start \leq k \leq end$$ 關系一直存在，也就是說在沒有找到 $$mid^2 == x$$ 時，循環退出時有 $$start < k < end$$, 取整的話顯然就是`start`了。


### C++
```c++
class Solution{
public:
    int mySqrt(int x) {
        if(x <= 1) return x;
        int lo = 2, hi = x;
        while(lo < hi){
            int m = lo + (hi - lo)/2;
            int q = x/m;
            if(q == m and x % m == 0)
                return m;
            else if(q < m)
                hi = m;
            else
                lo = m + 1;
        }
        
        return lo - 1;
    }
};
```

### 源碼分析
此題依然可以被翻譯成"找不大於target的$$x^2$$"，而所有待選的自然數當然是有序數列，因此同樣可以用二分搜索的思維解題，然而此題不會出現重複元素，因此可以增加一個相等就返回的條件，另外這邊我們同樣使用[lo, hi)的標示法來處理邊界條件，可以參照[Search for a range]，就不再贅述。另外特別注意，判斷找到的條件不是用`m * m == x`而是`x / m == m`，這是因為`x * x`可能會超出`INT_MAX`而溢位，因此用除法可以解決這個問題，再輔以餘數判斷是否整除以及下一步的走法。

### 複雜度分析

經典的二分搜索，時間複雜度為 $$O(\log n)$$, 使用了`start`, `end`, `mid`變量，空間複雜度為 $$O(1)$$.

除了使用二分法求平方根近似解之外，還可使用牛頓迭代法進一步提高運算效率，欲知後事如何，請猛戳 [求平方根sqrt()函數的底層算法效率問題 -- 簡明現代魔法](http://www.nowamagic.net/algorithm/algorithm_EfficacyOfFunctionSqrt.php)，不得不感歎演算法的魔力！
