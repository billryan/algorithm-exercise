# Bucket Sort

桶排序和归并排序有那么点点类似，也使用了归并的思想。大致步骤如下：

1. 设置一个定量的数组当作空桶。
2. Divide - 从待排序数组中取出元素，将元素按照一定的规则塞进对应的桶子去。
3. 对每个非空桶进行排序，通常可在塞元素入桶时进行插入排序。
4. Conquer - 从非空桶把元素再放回原来的数组中。

## Reference

- [Bucket Sort Visualization](http://www.cs.usfca.edu/~galles/visualization/BucketSort.html) - 动态演示。
- [桶排序 - 维基百科，自由的百科全书](http://zh.wikipedia.org/wiki/%E6%A1%B6%E6%8E%92%E5%BA%8F)
