# Heap - 堆

一般情況下，堆通常指的是**二叉堆**，**二叉堆**是一個近似**完全二元樹**的數據結構，**即披著二元樹羊皮的陣列，**故使用陣列來實現較為便利。子結點的鍵值(key)或索引總是小於（或者大於）它的父節點，且每個節點的左右子樹又是一個**二叉堆**(大根堆(Max Heap)或者小根堆(Min Heap))。根節點最大的堆叫做最大堆或大根堆，根節點最小的堆叫做最小堆或小根堆。**常被用作實現優先隊列(Priority Queue)。**

## 特點

1. **以陣列表示，但是以完全二元樹的方式理解**。
2. 唯一能夠同時最優地利用空間和時間的方法——最壞情況下也能保證使用 $$2N \log N$$ 次比較和恒定的額外空間。
3. 在索引從0開始的陣列中：
  - 父節點 `i` 的左子節點在位置`(2*i+1)`
  - 父節點 `i` 的右子節點在位置`(2*i+2)`
  - 子節點 `i` 的父節點在位置`floor((i-1)/2)`

## 堆的基本操作

以大根堆為例，堆的常用操作如下。

1. 最大堆調整（Max_Heapify）：將堆的末端子節點作調整，使得子節點永遠小於父節點
2. 創建最大堆（Build_Max_Heap）：將堆所有數據重新排序
3. 堆排序（HeapSort）：移除位在第一個數據的根節點，並做最大堆調整的遞迴運算

其中步驟1是給步驟2和3用的。

![Heapsort-example](../../shared-files/images/Heapsort-example.gif)

## Python

```python
class MaxHeap:
    def __init__(self, array=None):
        if array:
            self.heap = self._max_heapify(array)
        else:
            self.heap = []

    def _sink(self, array, i):
        # move node down the tree
        left, right = 2 * i + 1, 2 * i + 2
        max_index = i
        if left < len(array) and array[left] > array[max_index]:
            max_index = left
        if right < len(array) and array[right] > array[max_index]:
            max_index = right
        if max_index != i:
            array[i], array[max_index] = array[max_index], array[i]
            self._sink(array, max_index)

    def _swim(self, array, i):
        # move node up the tree
        if i == 0:
            return
        father = (i - 1) / 2
        if array[father] < array[i]:
            array[father], array[i] = array[i], array[father]
            self._swim(array, father)

    def _max_heapify(self, array):
        for i in xrange(len(array) / 2, -1, -1):
            self._sink(array, i)
        return array

    def push(self, item):
        self.heap.append(item)
        self._swim(self.heap, len(self.heap) - 1)

    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        item = self.heap.pop()
        self._sink(self.heap, 0)
        return item
```
