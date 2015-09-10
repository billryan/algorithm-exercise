# Bucket Sort

桶排序和合併排序有那麼點點類似，也使用了合併的思想。大致步驟如下：

1. 設置一個定量的數組當作空桶。
2. Divide - 從待排序數組中取出元素，將元素按照一定的規則塞進對應的桶子去。
3. 對每個非空桶進行排序，通常可在塞元素入桶時進行插入排序。
4. Conquer - 從非空桶把元素再放回原來的數組中。

## Reference

- [Bucket Sort Visualization](http://www.cs.usfca.edu/~galles/visualization/BucketSort.html) - 動態示例。
- [桶排序 - 維基百科，自由的百科全書](http://zh.wikipedia.org/wiki/%E6%A1%B6%E6%8E%92%E5%BA%8F)
