# Backpack

## Question

- lintcode: [(92) Backpack](http://www.lintcode.com/en/problem/backpack/)

### Problem Statement

Given _n_ items with size $$A_i$$, an integer _m_ denotes the size of a backpack.
How full you can fill this backpack?

#### Example

If we have `4` items with size `[2, 3, 5, 7]`, the backpack size is 11, we can
select `[2, 3, 5]`, so that the max size we can fill this backpack is `10`. If
the backpack size is `12`. we can select `[2, 3, 7]` so that we can fulfill
the backpack.

You function should return the max size we can fill in the given backpack.

#### Note

You can not divide any item into small pieces.

#### Challenge

O(n x m) time and O(m) memory.

O(n x m) memory is also acceptable if you do not know how to optimize memory.

## 題解1

本題是典型的01揹包問題，每種類型的物品最多只能選擇一件。參考前文 [Knapsack](http://algorithm.yuanbin.me/zh-hans/basics_algorithm/knapsack.html) 中總結的解法，這個題中可以將揹包的 size 理解爲傳統揹包中的重量；題目問的是能達到的最大 size, 故可將每個揹包的 size 類比爲傳統揹包中的價值。

考慮到數組索引從0開始，故定義狀態`bp[i + 1][j]`爲前 `i` 個物品中選出重量不超過`j`時總價值的最大值。狀態轉移方程則爲分`A[i] > j` 與否兩種情況考慮。初始化均爲0，相當於沒有放任何物品。

### Java

```java
public class Solution {
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A: Given n items with size A[i]
     * @return: The maximum size
     */
    public int backPack(int m, int[] A) {
        if (A == null || A.length == 0) return 0;

        final int M = m;
        final int N = A.length;
        int[][] bp = new int[N + 1][M + 1];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j <= M; j++) {
                if (A[i] > j) {
                    bp[i + 1][j] = bp[i][j];
                } else {
                    bp[i + 1][j] = Math.max(bp[i][j], bp[i][j - A[i]] + A[i]);
                }
            }
        }

        return bp[N][M];
    }
}
```

### 源碼分析

注意索引及初始化的值，尤其是 N 和 M 的區別，內循環處可等於 M。

### 複雜度分析

兩重 for 循環，時間複雜度爲 $$O(m \times n)$$, 二維矩陣的空間複雜度爲 $$O(m \times n)$$, 一維矩陣的空間複雜度爲 $$O(m)$$.

## 題解2

接下來看看 [九章算法](http://www.jiuzhang.com/solutions/backpack/) 的題解，**這種解法感覺不是很直觀，推薦使用題解1的解法。**

1. 狀態: result[i][S] 表示前i個物品，取出一些物品能否組成體積和爲S的揹包
2. 狀態轉移方程: $$f[i][S] = f[i-1][S-A[i]] ~or~ f[i-1][S]$$ (A[i]爲第i個物品的大小)
    - 欲從前i個物品中取出一些組成體積和爲S的揹包，可從兩個狀態轉換得到。
        1. $$f[i-1][S-A[i]]$$: **放入第i個物品**，前 $$i-1$$ 個物品能否取出一些體積和爲 $$S-A[i]$$ 的揹包。
        2. $$f[i-1][S]$$: **不放入第i個物品**，前 $$i-1$$ 個物品能否取出一些組成體積和爲S的揹包。
3. 狀態初始化: $$f[1 \cdots n][0]=true; ~f[0][1 \cdots m]=false$$. 前1~n個物品組成體積和爲0的揹包始終爲真，其他情況爲假。
4. 返回結果: 尋找使 $$f[n][S]$$ 值爲true的最大S ($$1 \leq S \leq m$$)

### C++ - 2D vector

```c++
class Solution {
public:
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A: Given n items with size A[i]
     * @return: The maximum size
     */
    int backPack(int m, vector<int> A) {
        if (A.empty() || m < 1) {
            return 0;
        }

        const int N = A.size() + 1;
        const int M = m + 1;
        vector<vector<bool> > result;
        result.resize(N);
        for (vector<int>::size_type i = 0; i != N; ++i) {
            result[i].resize(M);
            std::fill(result[i].begin(), result[i].end(), false);
        }

        result[0][0] = true;
        for (int i = 1; i != N; ++i) {
            for (int j = 0; j != M; ++j) {
                if (j < A[i - 1]) {
                    result[i][j] = result[i - 1][j];
                } else {
                    result[i][j] = result[i - 1][j] || result[i - 1][j - A[i - 1]];
                }
            }
        }

        // return the largest i if true
        for (int i = M; i > 0; --i) {
            if (result[N - 1][i - 1]) {
                return (i - 1);
            }
        }
        return 0;
    }
};
```

### 源碼分析

1. 異常處理
2. 初始化結果矩陣，注意這裏需要使用`resize`而不是`reserve`，否則可能會出現段錯誤
3. 實現狀態轉移邏輯，一定要分`j < A[i - 1]`與否來討論
4. 返回結果，只需要比較`result[N - 1][i - 1]`的結果，返回true的最大值

狀態轉移邏輯中代碼可以進一步簡化，即：

```
        for (int i = 1; i != N; ++i) {
            for (int j = 0; j != M; ++j) {
                result[i][j] = result[i - 1][j];
                if (j >= A[i - 1] && result[i - 1][j - A[i - 1]]) {
                    result[i][j] = true;
                }
            }
        }
```

考慮揹包問題的核心——狀態轉移方程，如何優化此轉移方程？原始方案中用到了二維矩陣來保存result，注意到result的第i行僅依賴於第i-1行的結果，那麼能否用一維數組來代替這種隱含的關係呢？我們**在內循環j處遞減即可**。如此即可避免`result[i][S]`的值由本輪`result[i][S-A[i]]`遞推得到。

### C++ - 1D vector

```c++
class Solution {
public:
    /**
     * @param m: An integer m denotes the size of a backpack
     * @param A: Given n items with size A[i]
     * @return: The maximum size
     */
    int backPack(int m, vector<int> A) {
        if (A.empty() || m < 1) {
            return 0;
        }

        const int N = A.size();
        vector<bool> result;
        result.resize(m + 1);
        std::fill(result.begin(), result.end(), false);

        result[0] = true;
        for (int i = 0; i != N; ++i) {
            for (int j = m; j >= 0; --j) {
                if (j >= A[i] && result[j - A[i]]) {
                    result[j] = true;
                }
            }
        }

        // return the largest i if true
        for (int i = m; i > 0; --i) {
            if (result[i]) {
                return i;
            }
        }
        return 0;
    }
};
```

### 複雜度分析

兩重 for 循環，時間複雜度均爲 $$O(m \times n)$$, 二維矩陣的空間複雜度爲 $$O(m \times n)$$, 一維矩陣的空間複雜度爲 $$O(m)$$.

## Reference

- 《挑戰程序設計競賽》第二章
- [Lintcode: Backpack - neverlandly - 博客園](http://www.cnblogs.com/EdwardLiu/p/4269149.html)
- [九章算法 | 揹包問題](http://www.jiuzhang.com/problem/58/)
- [崔添翼 § 翼若垂天之雲 › 《揹包問題九講》2.0 alpha1](http://cuitianyi.com/blog/%E3%80%8A%E8%83%8C%E5%8C%85%E9%97%AE%E9%A2%98%E4%B9%9D%E8%AE%B2%E3%80%8B2-0-alpha1/)
