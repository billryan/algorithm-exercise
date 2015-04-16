# Heap Sort - 堆排序

特点：唯一能够同时最优地利用空间和时间的方法——最坏情况下也能保证使用2NlogN次比较和恒定的额外空间。

在空间比较小(嵌入式设备和手机)时特别有用，但是因为现代系统往往有较多的缓存，堆排序无法有效利用缓存，数组元素很少和相邻的其他元素比较，故缓存未命中的概率远大于其他在相邻元素间比较的算法。

但是在海量数据的排序下又重新发挥了重要作用，因为它在插入操作和删除最大元素的混合动态场景中能保证对数级别的运行时间。TopM

## Reference

- [堆排序 - 维基百科，自由的百科全书](http://zh.wikipedia.org/wiki/%E5%A0%86%E6%8E%92%E5%BA%8F)
- [Priority Queues](http://algs4.cs.princeton.edu/24pq/) - Robert Sedgewick 的大作，详解了关于堆的操作。
- [经典排序算法总结与实现 | Jark's Blog](http://wuchong.me/blog/2014/02/09/algorithm-sort-summary/) - 堆排序讲的很好。
