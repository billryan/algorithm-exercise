# Heap - 堆

一般情况下，堆通常指的是**二叉堆**，**二叉堆**是一个近似**完全二叉树**的数据结构，但由于对二叉树平衡及插入/删除操作较为麻烦，二叉堆实际上使用数组来实现。即物理结构为数组，逻辑结构为完全二叉树。子结点的键值或索引总是小于（或者大于）它的父节点，且每个节点的左右子树又是一个**二叉堆**(大根堆或者小根堆)。根节点最大的堆叫做最大堆或大根堆，根节点最小的堆叫做最小堆或小根堆。**常被用作实现优先队列。**

## 特点

1. **以数组表示，但是以完全二叉树的方式理解**。
2. 唯一能够同时最优地利用空间和时间的方法——最坏情况下也能保证使用 $$2N \log N$$ 次比较和恒定的额外空间。
3. 在索引从0开始的数组中：
  - 父节点 `i` 的左子节点在位置`(2*i+1)`
  - 父节点 `i` 的右子节点在位置`(2*i+2)`
  - 子节点 `i` 的父节点在位置`floor((i-1)/2)`

## 堆的基本操作

以大根堆为例，堆的常用操作如下。

1. 最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
2. 创建最大堆：将堆所有数据重新排序
3. 堆排序：移除位于第一个数据的根节点，并做最大堆调整的递归运算

其中步骤1是给步骤2和3用的。

![Heapsort-example](../../shared-files/images/Heapsort-example.gif)

## 堆实现

使用迭代实现也较为简单，注意索引值初始化和置位即可，尤其是记住最后一个索引的值 last，Java 的实现中 `poll()` 操作同时带有排序功能。

### Python

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
        # should compare two chidren then determine which one to swap with
        flag = array[left] > array[right] 
        if left < len(array) and array[left] > array[max_index] and flag:
            max_index = left
        if right < len(array) and array[right] > array[max_index] and not flag:
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

### Java

```java
import java.util.*;

/**
 * Created by billryan on 29/7/2018.
 */
public class MaxHeap {
    private final int MAX_N = 10;
    private final int[] heap = new int[MAX_N];
    private int last = 0;

    public int getLast() {
        return last;
    }

    public void push(int x) {
        int i = last++;
        while (i > 0) {
            int p = (i - 1) / 2;
            if (heap[p] >= x) {
                break;
            }
            heap[i] = heap[p];
            i = p;
        }
        heap[i] = x;
    }

    public int pop() {
        int result = heap[0];
        int x = heap[--last];
        heap[last] = result;

        int i = 0;
        while (2 * i + 1 < last) {
            int left = 2 * i + 1, right = 2 * i + 2, swap = left;
            if (right < last && heap[left] < heap[right]) {
                swap = right;
            }
            if (heap[swap] <= x) {
                break;
            }

            heap[i] = heap[swap];
            i = swap;
        }
        heap[i] = x;

        return result;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("maxHeap: [");
        for (int i = 0; i < last - 1; i++) {
            sb.append(String.format("%d, ", heap[i]));
        }
        if (last > 0) {
            sb.append(heap[last - 1]);
        }
        sb.append("]");
        return sb.toString();
    }

    public static void main(String[] args) {
        MaxHeap maxHeap = new MaxHeap();

        int[] array = new int[]{6, 5, 3, 1, 8, 7, 2, 4, 10, 9};
        for (int i : array) {
            maxHeap.push(i);
            System.out.println(maxHeap);
        }

        for (int i = maxHeap.getLast() - 1; i >= 0; i--) {
            System.out.println("pop max heap value: " + maxHeap.pop());
            System.out.println(maxHeap);
        }

        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(10, Collections.reverseOrder());
        for (int i : array) {
            pq.offer(i);
            System.out.println(pq);
        }

        // Top K problem
        int k = 5;
        for (int i = 0; i < k; i++) {
            Integer topk = pq.poll();
            if (topk != null) {
                System.out.println("top " + (i + 1) + ": " + topk);
            } else {
                System.out.println("poll null value!!!");
            }
        }
    }
}
```

## C++
```c++
#ifndef HEAP_H
#define HEAP_H

#include <algorithm>
#include <functional>
#include <stdexcept>
#include <unordered_map>
#include <utility>
#include <vector>
template <typename T, typename TComparator = std::equal_to<T>,
          typename PComparator = std::less<double>,
          typename Hasher = std::hash<T> >
class Heap {
public:
/// Constructs an m-ary heap. M should be >= 2
Heap(int m = 2, const PComparator &c = PComparator(),
     const Hasher &hash = Hasher(), const TComparator &tcomp = TComparator());

/// Destructor as needed
~Heap();

/// Adds an item with the provided priority
void push(double pri, const T &item);

/// returns the element at the top of the heap
///  max (if max-heap) or min (if min-heap)
T const &top() const;

/// Removes the top element
void pop();

/// returns true if the heap is empty
bool empty() const;

/// decreaseKey reduces the current priority of
/// item to newpri, moving it up in the heap
/// as appropriate.
void decreaseKey(double newpri, const T &item);

private:
/// Add whatever helper functions you need below
void trickleUp(int loc);
void trickleDown(int loc);

// These should be all the data members you need.
std::vector<std::pair<double, T> > store_;
int m_;   // degree
PComparator c_;
std::unordered_map<T, size_t, Hasher, TComparator> keyToLocation_;
};

// Complete
template <typename T, typename TComparator, typename PComparator,
          typename Hasher>
Heap<T, TComparator, PComparator, Hasher>::Heap(int m, const PComparator &c,
                                                const Hasher &hash,
                                                const TComparator &tcomp)
        : store_(), m_(m), c_(c), keyToLocation_(100, hash, tcomp) {
}

// Complete
template <typename T, typename TComparator, typename PComparator,
          typename Hasher>
Heap<T, TComparator, PComparator, Hasher>::~Heap() {
}

template <typename T, typename TComparator, typename PComparator,
          typename Hasher>
void Heap<T, TComparator, PComparator, Hasher>::push(double priority,
                                                     const T &item) {
        // You complete.
        std::pair<double, T> temp(priority, item);
        store_.push_back(temp);
        keyToLocation_[item] = store_.size();
        // insert(std::make_pair(item, store_.size()));
        trickleUp(store_.size()-1);
}

template <typename T, typename TComparator, typename PComparator,
          typename Hasher>
void Heap<T, TComparator, PComparator, Hasher>::trickleUp(int loc) {
        int parent = (loc-1)/m_;
        while(parent >= 0 && c_(store_[loc].first, store_[parent].first)) {
                //swap loc with parent
                std::pair<double, T> temp = store_[loc];
                store_[loc] = store_[parent];
                store_[parent] = temp;
                double to_swap  = keyToLocation_[store_[loc].second];
                keyToLocation_[store_[loc].second] = keyToLocation_[store_[parent].second];
                keyToLocation_[store_[parent].second] = to_swap;
                loc = parent;
                parent = (loc-1)/m_;
        }
}


template <typename T, typename TComparator, typename PComparator,
          typename Hasher>
void Heap<T, TComparator, PComparator, Hasher>::decreaseKey(double priority,
                                                            const T &item) {
        std::pair<double, T> temp = store_[keyToLocation_[item]];
        temp.first = priority;
        trickleUp(keyToLocation_[item]);
}

template <typename T, typename TComparator, typename PComparator,
          typename Hasher>
T const &Heap<T, TComparator, PComparator, Hasher>::top() const {
        // Here we use exceptions to handle the case of trying
        // to access the top element of an empty heap
        if (empty()) {
                throw std::logic_error("can't top an empty heap");
        }
        return store_[0].second;
}

/// Removes the top element
template <typename T, typename TComparator, typename PComparator,
          typename Hasher>
void Heap<T, TComparator, PComparator, Hasher>::pop() {
        if (empty()) {
                throw std::logic_error("can't pop an empty heap");
        }
        store_[0] = store_[store_.size()-1];
        keyToLocation_.erase(store_[0].second);
        store_.pop_back();
        if(empty()) return;
        trickleDown(0);
}
template <typename T, typename TComparator, typename PComparator,
          typename Hasher>
void Heap<T, TComparator, PComparator, Hasher>::trickleDown(int loc) {
        if (loc*m_+1 > store_.size()-1) return;
        int smallerChild = m_*loc+1; // start w/ left
        for (size_t i = 1; i < m_; i++) {
                if (m_*loc+i < store_.size()) {//if the right exist
                        int rChild = m_*loc+i+1;
                        if(c_(store_[rChild].first, store_[smallerChild].first)) {
                                smallerChild = rChild;
                        }
                }
        }
        if(c_(store_[smallerChild].first, store_[loc].first)) {
                //swap smallerChild and loc
                std::pair<double, T> temp = store_[loc];
                store_[loc] = store_[smallerChild];
                store_[smallerChild] = temp;
                double to_swap = keyToLocation_[store_[loc].second];
                keyToLocation_[store_[loc].second] = keyToLocation_[store_[smallerChild].second];
                keyToLocation_[store_[smallerChild].second] = to_swap;
                trickleDown(smallerChild);
        }
}


/// returns true if the heap is empty
template <typename T, typename TComparator, typename PComparator,
          typename Hasher>
bool Heap<T, TComparator, PComparator, Hasher>::empty() const {
        return store_.empty();
}

#endif
```
