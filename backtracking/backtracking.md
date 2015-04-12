# Backtracking - 回溯法

回溯法包含了多类问题，模板类似。

排列组合模板->搜索问题(是否要排序，哪些情况要跳过)

使用回溯法的一般步骤：

1. 确定所给问题的解空间：首先应明确定义问题的解空间，解空间中至少包含问题的一个解。
2. 确定结点的扩展搜索规则
3. 以深度优先方式搜索解空间，并在搜索过程中用剪枝函数避免无效搜索。

## Reference

- [Steven Skiena: Lecture15 - Backtracking](../docs/lecture15-backtracking.pdf)
- [全面解析回溯法：算法框架与问题求解 - 五岳 - 博客园](http://www.cnblogs.com/wuyuegb2312/p/3273337.html)
- [五大常用算法之四：回溯法 - 红脸书生 - 博客园](http://www.cnblogs.com/steven_oyj/archive/2010/05/22/1741376.html)
- [演算法筆記 - Backtracking](http://www.csie.ntnu.edu.tw/~u91029/Backtracking.html)
