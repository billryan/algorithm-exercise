# Triangle - Find the minimum path sum from top to bottom

## Question

- lintcode: [(109) Triangle](http://www.lintcode.com/en/problem/triangle/)

```
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

Note
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

Example
For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
```

## 題解

題中要求最短路徑和，每次只能訪問下行的相鄰元素，將triangle視爲二維座標。此題方法較多，下面分小節詳述。

### Method 1 - Traverse without hashmap

首先考慮最容易想到的方法——遞歸遍歷，逐個累加所有自上而下的路徑長度，最後返回這些不同的路徑長度的最小值。由於每個點往下都有2條路徑，使用此方法的時間複雜度約爲 $$O(2^n)$$, 顯然是不可接受的解，不過我們還是先看看其實現思路。

### C++ Traverse without hashmap

```c++
class Solution {
public:
    /**
     * @param triangle: a list of lists of integers.
     * @return: An integer, minimum path sum.
     */
    int minimumTotal(vector<vector<int> > &triangle) {
        if (triangle.empty()) {
            return -1;
        }

        int result = INT_MAX;
        dfs(0, 0, 0, triangle, result);

        return result;
    }

private:
    void dfs(int x, int y, int sum, vector<vector<int> > &triangle, int &result) {
        const int n = triangle.size();
        if (x == n) {
            if (sum < result) {
                result = sum;
            }
            return;
        }

        dfs(x + 1, y, (sum + triangle[x][y]), triangle, result);
        dfs(x + 1, y + 1, (sum + triangle[x][y]), triangle, result);
    }
};
```

### 源碼分析

`dfs()`的循環終止條件爲`x == n`，而不是`x == n - 1`，主要是方便在遞歸時sum均可使用`sum + triangle[x][y]`，而不必根據不同的y和y+1改變，代碼實現相對優雅一些。理解方式則變爲從第x行走到第x+1行時的最短路徑和，也就是說在此之前並不將第x行的元素值計算在內。

這種遍歷的方法時間複雜度如此之高的主要原因是因爲在n較大時遞歸計算了之前已經得到的結果，而這些結果計算一次後即不再變化，可再次利用。因此我們可以使用hashmap記憶已經計算得到的結果從而對其進行優化。

### Method 2 - Divide and Conquer without hashmap

既然可以使用遞歸遍歷，當然也可以使用「分治」的方法來解。「分治」與之前的遍歷區別在於「分治」需要返回每次「分治」後的計算結果，下面看代碼實現。

### C++ Divide and Conquer without hashmap

```c++
class Solution {
public:
    /**
     * @param triangle: a list of lists of integers.
     * @return: An integer, minimum path sum.
     */
    int minimumTotal(vector<vector<int> > &triangle) {
        if (triangle.empty()) {
            return -1;
        }

        int result = dfs(0, 0, triangle);

        return result;
    }

private:
    int dfs(int x, int y, vector<vector<int> > &triangle) {
        const int n = triangle.size();
        if (x == n) {
            return 0;
        }

        return min(dfs(x + 1, y, triangle), dfs(x + 1, y + 1, triangle))  + triangle[x][y];
    }
};
```

使用「分治」的方法代碼相對簡潔一點，接下來我們使用hashmap保存triangle中不同座標的點計算得到的路徑和。

### Method 3 - Divide and Conquer with hashmap

新建一份大小和triangle一樣大小的hashmap，並對每個元素賦以`INT_MIN`以做標記區分。

### C++ Divide and Conquer with hashmap

```c++
class Solution {
public:
    /**
     * @param triangle: a list of lists of integers.
     * @return: An integer, minimum path sum.
     */
    int minimumTotal(vector<vector<int> > &triangle) {
        if (triangle.empty()) {
            return -1;
        }

        vector<vector<int> > hashmap(triangle);
        for (int i = 0; i != hashmap.size(); ++i) {
            for (int j = 0; j != hashmap[i].size(); ++j) {
                hashmap[i][j] = INT_MIN;
            }
        }
        int result = dfs(0, 0, triangle, hashmap);

        return result;
    }

private:
    int dfs(int x, int y, vector<vector<int> > &triangle, vector<vector<int> > &hashmap) {
        const int n = triangle.size();
        if (x == n) {
            return 0;
        }

        // INT_MIN means no value yet
        if (hashmap[x][y] != INT_MIN) {
            return hashmap[x][y];
        }
        int x1y = dfs(x + 1, y, triangle, hashmap);
        int x1y1 = dfs(x + 1, y + 1, triangle, hashmap);
        hashmap[x][y] =  min(x1y, x1y1) + triangle[x][y];

        return hashmap[x][y];
    }
};
```

由於已經計算出的最短路徑值不再重複計算，計算複雜度由之前的 $$O(2^n)$$，變爲 $$O(n^2)$$, 每個座標的元素僅計算一次，故共計算的次數爲 $$1+2+...+n \approx O(n^2)$$.

### Method 4 - Dynamic Programming

從主章節中對動態規劃的簡介我們可以知道使用動態規劃的難點和核心在於**狀態的定義及轉化方程的建立**。那麼問題來了，到底如何去找適合這個問題的狀態及轉化方程呢？

我們仔細分析題中可能的狀態和轉化關係，發現從`triangle`中座標爲 $$triangle[x][y]$$ 的元素出發，其路徑只可能爲 $$triangle[x][y]->triangle[x+1][y]$$ 或者 $$triangle[x][y]->triangle[x+1][y+1]$$. 以點 $$(x,y)$$ 作爲參考，那麼可能的狀態 $$f(x,y)$$ 就可以是：

1. 從 $$(x,y)$$ 出發走到最後一行的最短路徑和
2. 從 $$(0,0)$$ 走到 $$(x,y)$$的最短路徑和

如果選擇1作爲狀態，則相應的狀態轉移方程爲：
$$f_1(x,y) = min\{f_1(x+1, y), f_1(x+1, y+1)\} + triangle[x][y]$$

如果選擇2作爲狀態，則相應的狀態轉移方程爲：
$$f_2(x,y) = min\{f_2(x-1, y), f_2(x-1, y-1)\} + triangle[x][y]$$

兩個狀態所對應的初始狀態分別爲 $$f_1(n-1, y), 0 \leq y \leq n-1$$ 和 $$f_2(0,0)$$. 在代碼中應注意考慮邊界條件。下面分別就這種不同的狀態進行動態規劃。

### C++ From Bottom to Top

```c++
class Solution {
public:
    /**
     * @param triangle: a list of lists of integers.
     * @return: An integer, minimum path sum.
     */
    int minimumTotal(vector<vector<int> > &triangle) {
        if (triangle.empty()) {
            return -1;
        }

        vector<vector<int> > hashmap(triangle);

        // get the total row number of triangle
        const int N = triangle.size();
        for (int i = 0; i != N; ++i) {
            hashmap[N-1][i] = triangle[N-1][i];
        }

        for (int i = N - 2; i >= 0; --i) {
            for (int j = 0; j < i + 1; ++j) {
                hashmap[i][j] = min(hashmap[i + 1][j], hashmap[i + 1][j + 1]) + triangle[i][j];
            }
        }

        return hashmap[0][0];
    }
};
```

### 源碼分析

1. 異常處理
2. 使用hashmap保存結果
3. 初始化`hashmap[N-1][i]`, 由於是自底向上，故初始化時保存最後一行元素
4. 使用自底向上的方式處理循環
5. 最後返回結果hashmap[0][0]

從空間利用角度考慮也可直接使用triangle替代hashmap，但是此舉會改變triangle的值，不推薦。

### C++ From Top to Bottom

```c++
class Solution {
public:
    /**
     * @param triangle: a list of lists of integers.
     * @return: An integer, minimum path sum.
     */
    int minimumTotal(vector<vector<int> > &triangle) {
        if (triangle.empty()) {
            return -1;
        }

        vector<vector<int> > hashmap(triangle);

        // get the total row number of triangle
        const int N = triangle.size();
        //hashmap[0][0] = triangle[0][0];
        for (int i = 1; i != N; ++i) {
            for (int j = 0; j <= i; ++j) {
                if (j == 0) {
                    hashmap[i][j] = hashmap[i - 1][j];
                }
                if (j == i) {
                    hashmap[i][j] = hashmap[i - 1][j - 1];
                }
                if ((j > 0) && (j < i)) {
                    hashmap[i][j] = min(hashmap[i - 1][j], hashmap[i - 1][j - 1]);
                }
                hashmap[i][j] += triangle[i][j];
            }
        }

        int result = INT_MAX;
        for (int i = 0; i != N; ++i) {
            result = min(result, hashmap[N - 1][i]);
        }
        return result;
    }
};
```

#### 源碼解析

自頂向下的實現略微有點複雜，在尋路時需要考慮最左邊和最右邊的邊界，還需要在最後返回結果時比較最小值。

### Java From Top to Bottom

```java
public class Solution {
    /**
     * @param triangle: a list of lists of integers.
     * @return: An integer, minimum path sum.
     */
    public int minimumTotal(int[][] triangle) {
        // write your code here
        if (triangle == null || triangle.length == 0) return 0;
        int[] last = new int[triangle.length];
        int[] current = new int[triangle.length];
        last[0] = triangle[0][0];
        current[0] = last[0];
        for (int i = 1; i < triangle.length; i++) {
            for (int j = 0; j < i + 1; j++) {
                int sum = Integer.MAX_VALUE;
                if (j != 0) {
                    sum = triangle[i][j] + last[j - 1];
                }
                if (j != i) {
                    sum = Math.min(sum, triangle[i][j] + last[j]);
                }
                current[j] = sum;
            }
            for (int k = 0; k < i + 1; k++) last[k] = current[k];
        }
        int min = Integer.MAX_VALUE;
        for (int n : current) {
            min = Math.min(n, min);
        }
        return min;
    }
}
```

#### 源碼解析

思路基本和上個解法一樣，但是在數組last中保留上一層的最短和的，因此不用hashmap，空間複雜度是O(n)
