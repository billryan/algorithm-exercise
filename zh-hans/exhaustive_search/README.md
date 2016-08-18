# Exhaustive Search - 穷竭搜索

穷竭搜索又称暴力搜索，指代将所有可能性列出来，然后再在其中寻找满足题目条件的解。常用求解方法和工具有：

1. 递归函数
2. 栈
3. 队列
4. 深度优先搜索(DFS, Depth-First Search)，又常称为回溯法
5. 广度优先搜索(BFS, Breadth-First Search)

1, 2, 3 往往在深搜或者广搜中体现。

## DFS

DFS 通常从某个状态开始，根据特定的规则转移状态，直至无法转移(节点为空)，然后回退到之前一步状态，继续按照指定规则转移状态，直至遍历完所有状态。

回溯法包含了多类问题，模板类似。

排列组合模板->搜索问题(是否要排序，哪些情况要跳过)

使用回溯法的一般步骤：

1. 确定所给问题的解空间：首先应明确定义问题的解空间，解空间中至少包含问题的一个解。
2. 确定结点的扩展搜索规则
3. 以深度优先方式搜索解空间，并在搜索过程中用剪枝函数避免无效搜索。

### BFS

BFS 从某个状态开始，搜索**所有可以到达的状态**，转移顺序为『初始状态->只需一次转移就可到达的所有状态->只需两次转移就可到达的所有状态->...』，所以对于同一个状态，BFS 只搜索一次，故时间复杂度为 $$O(states \times transfer\_methods)$$. BFS 通常配合队列一起使用，搜索时先将状态加入到队列中，然后从队列顶端不断取出状态，再把从该状态可转移到的状态中尚未访问过的部分加入队列，知道队列为空或已找到解。因此 BFS 适合用于『由近及远』的搜索，比较适合用于求解最短路径、最少操作之类的问题。

## Reference

- 《挑战程序设计竞赛》Chaper 2.1 p26 最基础的“穷竭搜索”
- [Steven Skiena: Lecture15 - Backtracking](http://7xojrx.com1.z0.glb.clouddn.com/docs/algorithm-exercise/docs/lecture15-backtracking.pdf)
- [全面解析回溯法：算法框架与问题求解 - 五岳 - 博客园](http://www.cnblogs.com/wuyuegb2312/p/3273337.html)
- [五大常用算法之四：回溯法 - 红脸书生 - 博客园](http://www.cnblogs.com/steven_oyj/archive/2010/05/22/1741376.html)
- [演算法筆記 - Backtracking](http://www.csie.ntnu.edu.tw/~u91029/Backtracking.html)
