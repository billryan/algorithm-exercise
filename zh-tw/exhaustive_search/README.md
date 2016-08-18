# Exhaustive Search - 窮竭搜索

窮竭搜索又稱暴力搜索，指代將所有可能性列出來，然後再在其中尋找滿足題目條件的解。常用求解方法和工具有：

1. 遞歸函數
2. 棧
3. 隊列
4. 深度優先搜索(DFS, Depth-First Search)，又常稱為回溯法
5. 廣度優先搜索(BFS, Breadth-First Search)

1, 2, 3 往往在深搜或者廣搜中體現。

## DFS

DFS 通常從某個狀態開始，根據特定的規則轉移狀態，直至無法轉移(節點為空)，然後回退到之前一步狀態，繼續按照指定規則轉移狀態，直至遍曆完所有狀態。

回溯法包含了多類問題，模板類似。

排列組合模板->搜索問題(是否要排序，哪些情況要跳過)

使用回溯法的一般步驟：

1. 確定所給問題的解空間：首先應明確定義問題的解空間，解空間中至少包含問題的一個解。
2. 確定結點的擴展搜索規則
3. 以深度優先方式搜索解空間，並在搜索過程中用剪枝函數避免無效搜索。

### BFS

BFS 從某個狀態開始，搜索**所有可以到達的狀態**，轉移順序為『初始狀態->只需一次轉移就可到達的所有狀態->只需兩次轉移就可到達的所有狀態->...』，所以對於同一個狀態，BFS 只搜索一次，故時間複雜度為 $$O(states \times transfer\_methods)$$. BFS 通常配合隊列一起使用，搜索時先將狀態加入到隊列中，然後從隊列頂端不斷取出狀態，再把從該狀態可轉移到的狀態中尚未訪問過的部分加入隊列，知道隊列為空或已找到解。因此 BFS 適合用於『由近及遠』的搜索，比較適合用於求解最短路徑、最少操作之類的問題。

## Reference

- 《挑戰程序設計競賽》Chaper 2.1 p26 最基礎的「窮竭搜索」
- [Steven Skiena: Lecture15 - Backtracking](http://7xojrx.com1.z0.glb.clouddn.com/docs/algorithm-exercise/docs/lecture15-backtracking.pdf)
- [全面解析回溯法：算法框架與問題求解 - 五嶽 - 博客園](http://www.cnblogs.com/wuyuegb2312/p/3273337.html)
- [五大常用算法之四：回溯法 - 紅臉書生 - 博客園](http://www.cnblogs.com/steven_oyj/archive/2010/05/22/1741376.html)
- [演算法筆記 - Backtracking](http://www.csie.ntnu.edu.tw/~u91029/Backtracking.html)
