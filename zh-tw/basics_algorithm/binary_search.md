# Binary Search - 二分搜索

二分搜索是一種在有序陣列中尋找目標值的經典方法，也就是說使用前提是『有序陣列』。非常簡單的題中『有序』特徵非常明顯，但更多時候可能需要我們自己去構造『有序陣列』。下面我們從最基本的二分搜索開始逐步深入。

## 模板一 - lower/upper bound

定義 lower bound 爲在給定升序陣列中大於等於目標值的最小索引，upper bound 則爲小於等於目標值的最大索引，下面給出程式碼和測試用例。

### Java

```java
import java.util.*;

public class Main {
    public static void main(String[] args) {
        int[] nums = new int[]{1,2,2,3,4,6,6,6,13,18};
        System.out.println(lowerBound(nums, 6)); // 5
        System.out.println(upperBound(nums, 6)); // 7
        System.out.println(lowerBound(nums, 7)); // 8
        System.out.println(upperBound(nums, 7)); // 7
    }

    /*
    * nums[index] >= target, min(index)
    */
    public static int lowerBound(int[] nums, int target) {
        if (nums == null || nums.length == 0) return -1;
        int lb = -1, ub = nums.length;
        while (lb + 1 < ub) {
            int mid = lb + (ub - lb) / 2;
            if (nums[mid] < target) {
                lb = mid;
            } else {
                ub = mid;
            }
        }

        return lb + 1;
    }

    /*
    * nums[index] <= target, max(index)
    */
    public static int upperBound(int[] nums, int target) {
        if (nums == null || nums.length == 0) return -1;
        int lb = -1, ub = nums.length;
        while (lb + 1 < ub) {
            int mid = lb + (ub - lb) / 2;
            if (nums[mid] > target) {
                ub = mid;
            } else {
                lb = mid;
            }
        }

        return ub - 1;
    }
}
```

### 源碼分析

以`lowerBound`的實現爲例，以上二分搜索的模板有幾個非常優雅的實現：

1. `while` 循環中 `lb + 1 < ub`, 而不是等號，因爲取等號可能會引起死循環。初始化`lb < ub` 時，最後循環退出時一定有`lb + 1 == ub`.
2. `mid = lb + (ub - lb) / 2`, 可有效防止兩數相加後溢出。
3. `lb` 和 `ub` 的初始化，初始化爲陣列的兩端以外，這種初始化方式比起`0` 和`nums.length - 1` 有不少優點，詳述如下。

如果遇到有問插入索引的位置時，可以分三種典型情況：

1. 目標值在陣列範圍之內，最後返回值一定是`lb + 1`
2. 目標值比陣列最小值還小，此時`lb` 一直爲`-1`, 故最後返回`lb + 1` 也沒錯，也可以將`-1` 理解爲陣列前一個更小的值
3. 目標值大於等於陣列最後一個值，由於循環退出條件爲`lb + 1 == ub`, 那麼循環退出時一定有`lb = A.length - 1`, 應該返回`lb + 1`

綜上所述，返回`lb + 1`是非常優雅的實現。其實以上三種情況都可以統一爲一種方式來理解，即索引`-1` 對應於陣列前方一個非常小的數，索引`ub` 即對應陣列後方一個非常大的數，那麼要插入的數就一定在`lb` 和`ub` 之間了。

**有時複雜的邊界條件處理可以通過『補項』這種優雅的方式巧妙處理。**

關於lb 和 ub 的初始化，由於`mid = lb + (ub - lb) / 2`, 且有`lb + 1 < ub`，故 mid 還是有可能爲`ub - 1`或者`lb + 1`的，在需要訪問`mid + 1`或者`mid - 1`處索引的元素時可能會越界。這時候就需要將初始化方式改爲`lb = 0, ub = A.length - 1` 了，最後再加一個關於`lb, ub` 處索引元素的判斷即可。如 [Search for a Range](http://algorithm.yuanbin.me/zh-hans/binary_search/search_for_a_range.html) 和 [Find Peak Element](http://algorithm.yuanbin.me/zh-hans/binary_search/find_peak_element.html). 尤其是 Find Peak Element 中 lb 和 ub 的初始值如果初始化爲-1和陣列長度會帶來一些麻煩。

## 模板二 - 最優解

除了在有序陣列中尋找目標值這種非常直接的二分搜索外，我們還可以利用二分搜索求最優解（最大值/最小值），通常這種題中只是隱含了『有序陣列』，需要我們自己構造。

用數學語言來描述就是『求滿足某條件 $$C(x)$$ 的最小/大的 $$x$$』，以求最小值爲例，對於任意滿足條件的 $$x$$, 如果所有的 $$x \leq x^\prime \leq UB$$ 對於 $$C(x^\prime)$$ 都爲真（其中 `UB` 可能爲無窮大，也可能爲滿足條件的最大的解，如果不滿足此條件就不能保證二分搜索的正確性），那麼我們就能使用二分搜索進行求解，其中初始化時下界`lb` 初始化爲不滿足條件的值`LB`, 上界初始化爲滿足條件的上界`UB`. 隨後在`while` 循環內部每次取中，滿足條件就取`ub = mid`, 否則`lb = mid`, 那麼最後`ub` 就是要求的最小值。求最大值時類似，只不過處理的是`lb`.

以 [POJ No.1064](http://poj.org/problem?id=1064) 爲例。

### Problem Statement

有 $$N$$ 條繩子，它們的長度分別爲 $$L_i$$. 如果從它們中切割出 $$K$$ 條長度相同的繩子的話，這 $$K$$ 條繩子每條最長能有多長？答案保留到小數點後兩位。

#### 輸入

```
N = 4, L = {8.02, 7.43, 4.57, 5.39}, K = 11
```

#### 輸出

2.00

### 題解

這道題看似是一個最優化問題，我們來嘗試下使用模板二的思想求解，**令 $$C(x)$$ 爲『可以得到 $$K$$ 條長度爲 $$x$$ 的繩子』。**根據題意，我們可以將上述條件進一步細化爲：
$$
C(x) = \sum_i(floor(L_i / x)) \geq K
$$

我們現在來分析下可行解的上下界。由於答案保留小數點後兩位，顯然繩子長度一定大於0，大於0的小數點後保留兩位的最小值爲`0.01`, 顯然如果問題最後有解，`0.01` 一定是可行解中最小的，且這個解可以分割出的繩子條數是最多的。一般在 OJ 上不同變量都是會給出範圍限制，那麼我們將上界初始化爲`最大範圍 + 0.01`, 它一定在可行解之外（也可以遍歷一遍陣列取陣列最大值，但其實二分後複雜度相差不大）。使用二分搜索後最後返回`lb` 即可。

### Java

```java
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        double[] nums = new double[n];
        for (int i = 0; i < n; i++) {
            nums[i] = in.nextDouble();
        }
        System.out.printf("%.2f\n", Math.floor(solve(nums, k) * 100) / 100);
    }

    public static double solve(double[] nums, int K) {
        double lb = 0.00, ub = 10e5 + 0.01;
        // while (lb + 0.001 < ub) {
	for (int i = 0; i < 100; i++) {
            double mid = lb + (ub - lb) / 2;
            if (C(nums, mid, K)) {
                lb = mid;
            } else {
                ub = mid;
            }
        }
        return lb;
    }

    public static boolean C(double[] nums, double seg, int k) {
        int count = 0;
        for (double num : nums) {
            count += Math.floor(num / seg);
        }
        return count >= k;
    }
}
```

### 源碼分析

方法`C` 只做一件事，給定陣列`nums`, 判斷是否能切割出`K` 條長度均爲`seg` 的繩子。`while` 循環中使用`lb + 0.001 < ub`, 不能使用`0.01`, 因爲計算`mid` 時有均值的計算，對於`double` 型數值否則會有較大誤差。

## 模板三 - 二分搜索的 `while` 結束條件判定

對於整型我們通常使用`lb + 1 < ub`, 但對於`double`型數據來說會有些精度上的丟失，使得結束條件不是那麼好確定。像上題中採用的方法是題目中使用的精度除10。但有時候這種精度可能還是不夠，如果結束條件`lb + EPS < ub`中使用的 EPS 過小時 double 型數據精度有可能不夠從而導致死循環的產生！這時候我們將`while`循環體替換爲`for (int i = 0; i < 100; i++)`, 100 次循環後可以達到 $$10^{-30}$$ 精度範圍，一般都沒問題。

## 模板四 － （九章算法）模版

這個模版跟第一個模版類似， 但是相對更容易上手。這個模版的核心是， `將binary search 問題轉化成：尋找第一個或者最後一個，該target元素出現的位置的問題`，`Find the any/first/last position of target in nums`. 詳解請見下面的例題。這個模版有四個要素。

1. start + 1 < end
    表示， 當指針指到兩個元素，相鄰或者相交的時候， 循環停止。 這樣的話在最終分情況討論的時候，只用考慮`1～2`個元素。
2. start + (end - start) / 2
    寫C++ 和 Java的同學要考慮到int overflow的問題， 所以需要考慮邊界情況。 寫Python的同學就不用考慮了， 因爲python這個語言本身已經非常努力的保證了number不會overflow。
3. A[mid] ==, >, <
    在循環中， 分三種情況討論邊界。 要注意， 在移動`start`和`end`的時候， 只要單純的把指針指向`mid`的位置， 不要`+1`或者`-1`。 因爲只移動邊界到`mid`的位置， 不會誤刪除target。在工程中，儘量在程序最後的時候統一寫`return`, 這樣可以增強可讀性。
4. A[start], A[end]? target
    在循環結束時，因爲只有1～2個元素需要討論，所以結果非常容易解釋清楚。 只存在的2種情況爲， 1. `start + 1 == end` 邊界指向相鄰的兩個元素， 這時只需要分情況討論`start`和`end`與target的關係，就可以得出結果。 2. `start == end` 邊界指向同一元素， 其實這個情況還是可以按照1的方法，分成`start``end`討論，只不過討論結果一樣而已。

### Python
```python
class Solution:
    def binary_search(self, array, target):
        if not array:
            return -1

        start, end = 0, len(array) - 1
        while start + 1 < end:
            mid = (start + end) / 2
            if array[mid] == target:
                start = mid
            elif array[mid] < target:
                start = mid
            else:
                end = mid

        if array[start] == target:
            return start
        if array[end] == target:
            return end
        return -1
```

### Java
```java
class Solution {
    public int binarySearch(int[] array, int target) {
        if (array == null || array.length == 0) {
            return -1;
        }

        int start = 0, end = array.length - 1;
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (array[mid] == target) {
                start = mid;
            } else if (array[mid] < target) {
                start = mid;
            } else {
                end = mid;
            }
        }
        if (array[start] == target) {
            return start;
        }
        if (array[end] == target) {
            return end;
        }
        return -1;
    }
}
```

### Problem Statement
[Search for a Range](http://www.lintcode.com/zh-hans/problem/search-for-a-range/)

#### 樣例
給出[5, 7, 7, 8, 8, 10]和目標值target=8,

返回[3, 4]

### Python
```python
class Solution:
    def search_range(self, array, target):
        ret = [-1, -1]
        if not array:
            return ret
        # search first position of target
        st, ed = 0, len(array) - 1
        while st + 1 < ed:
            mid = (st + ed) / 2
            if array[mid] == target:
                ed = mid
            elif array[mid] < target:
                st = mid
            else:
                ed = mid
        if array[st] == target:
            ret[0] = st
        elif array[ed] == target:
            ret[0] = ed

        # search last position of target
        st, ed = 0, len(array) - 1
        while st + 1 < ed:
            mid = (st + ed) / 2
            if array[mid] == target:
                st = mid
            elif array[mid] < target:
                st = mid
            else:
                ed = mid
        if array[ed] == target:
            ret[1] = ed
        elif array[st] == target:
            ret[1] = st

        return ret
```
### 源碼分析
search range的問題可以理解爲， 尋找第一次target出現的位置和最後一次target出現的位置。 當尋找第一次target出現位置的循環中， `array[mid] == target`表示， target可以出現在mid或者mid更前的位置， 所以將ed移動到mid。當循環跳出時， st的位置在ed之前，所以先判斷在st位置上是否是target， 再判斷ed位置。當尋找最後一次target出現位置的循環中，`array[mid] == target`表示， target可以出現在mid或者mid之後的位置， 所以將st移動到mid。 當循環結束時，ed的位置比st的位置更靠後， 所以先判斷ed的位置是否爲target， 再判斷st位置。 最後返回ret。

## Reference

- 《挑戰程序設計競賽》
