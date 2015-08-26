# Basics Sorting - 基礎排序演算法

# 演算法複習——排序

<!-- 時間限制為1s時，大O為10000000時勉強可行，100,000,000時很懸。 -->

## 演算法分析

1. 時間複雜度-執行時間(比較和交換次數)
2. 空間複雜度-所消耗的額外記憶體空間
    - 使用小堆疊、隊列或表
    - 使用鏈表或指針、數組索引來代表數據
    - 排序數據的副本

在OJ上做題時，一些經驗法則(rule of thumb)以及封底估算(back-of-the-envelop calculation)可以幫助選擇適合的演算法，一個簡單的經驗法則是

    10^9 operations per second
舉例來說，如果今天遇到一個題目，時間限制是1s，但僅有$$10^3$$筆輸入數據，此時即使使用$$O(n^2)$$的演算法也沒問題，但若有$$10^5$$筆輸入，則$$O(n^2)$$的演算法則非常可能超時，在實作前就要先思考是不是有$$O(n\log n)$$或更快的演算法。

對具有重鍵的數據(同一組數按不同鍵多次排序)進行排序時，需要考慮排序方法的穩定性，在非穩定性排序演算法中需要穩定性時可考慮加入小索引。

穩定性：如果排序後文件中擁有相同鍵的項的相對位置不變，這種排序方式是穩定的。

常見的排序演算法根據是否需要比較可以分為如下幾類：

- Comparison Sorting
    1. Bubble Sort
    2. Selection Sort
    3. Insertion Sort
    4. Shell Sort
    5. Merge Sort
    6. Quck Sort
    7. Heap Sort
- Bucket Sort
- Counting Sort
- Radix Sort

從穩定性角度考慮可分為如下兩類：
- 穩定
- 非穩定

## Reference

- [Sorting algorithm - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Sorting_algorithm) - 各類排序演算法的「平均、最好、最壞時間複雜度」總結。
- [Big-O cheatsheet](http://bigocheatsheet.com/) - 更清晰的總結
- [經典排序演算法總結與實現 | Jark's Blog](http://wuchong.me/blog/2014/02/09/algorithm-sort-summary/) - 基於 Python 的較為清晰的總結。
- [【面經】矽谷前沿Startup面試經驗-排序演算法總結及快速排序演算法代碼_九章演算法](http://blog.sina.com.cn/s/blog_eb52001d0102v1k8.html) - 總結了一些常用常問的排序演算法。
- [雷克雅維克大學的程式競賽課程](http://algo.is/)
第一講的slide中提供了演算法分析的經驗法則
