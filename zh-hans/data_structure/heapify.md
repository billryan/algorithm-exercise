# Heapify

## Question

- lintcode: [(130) Heapify](http://www.lintcode.com/en/problem/heapify/)

```
Given an integer array, heapify it into a min-heap array.

For a heap array A, A[0] is the root of heap, and for each A[i],
A[i * 2 + 1] is the left child of A[i] and A[i * 2 + 2] is the right child of A[i].

Example
Given [3,2,1,4,5], return [1,2,3,4,5] or any legal heap array.

Challenge
O(n) time complexity

Clarification
What is heap?

Heap is a data structure, which usually have three methods: push, pop and top.
where "push" add a new element the heap,
"pop" delete the minimum/maximum element in the heap,
"top" return the minimum/maximum element.

What is heapify?
Convert an unordered integer array into a heap array.
If it is min-heap, for each element A[i],
we will get A[i * 2 + 1] >= A[i] and A[i * 2 + 2] >= A[i].

What if there is a lot of solutions?
Return any of them.
```

## 题解

参考前文提到的 [Heap Sort](http://algorithm.yuanbin.me/zh-hans/basics_sorting/heap_sort.html) 可知此题要实现的只是小根堆的堆化过程，并不要求堆排。

### C++

```c++
class Solution {
public:
    /**
     * @param A: Given an integer array
     * @return: void
     */
    void heapify(vector<int> &A) {
        // build min heap
        for (int i = A.size() / 2; i >= 0; --i) {
            min_heap(A, i);
        }
    }

private:
    void min_heap(vector<int> &nums, int k) {
        int len = nums.size();
        while (k < len) {
            int min_index = k;
            // left leaf node search
            if (k * 2 + 1 < len && nums[k * 2 + 1] < nums[min_index]) {
                min_index = k * 2 + 1;
            }
            // right leaf node search
            if (k * 2 + 2 < len && nums[k * 2 + 2] < nums[min_index]) {
                min_index = k * 2 + 2;
            }
            if (k == min_index) {
                break;
            }
            // swap with the minimal
            int temp = nums[k];
            nums[k] = nums[min_index];
            nums[min_index] = temp;
            // not only current index
            k = min_index;
        }
    }
};
```

### 源码分析

堆排的简化版，最后一步`k = min_index`不能忘，因为增删节点时需要重新建堆，这样才能保证到第一个节点时数组已经是二叉堆。

### 复杂度分析

由于采用的是自底向上的建堆方式，时间复杂度为 $$(N)$$, 证明待补充...

## Reference

- [Heap Sort](http://algorithm.yuanbin.me/zh-hans/basics_sorting/heap_sort.html)
- [Heapify 参考程序 Java/C++/Python](http://www.jiuzhang.com/solutions/heapify/)
