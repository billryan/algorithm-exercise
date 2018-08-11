---
difficulty: Medium
tags:
- Priority Queue
- Heap
- Data Stream
title: Top k Largest Numbers II
---

# Top k Largest Numbers II

## Problem

### Metadata

- tags: Priority Queue, Heap, Data Stream
- difficulty: Medium
- source(lintcode): <https://www.lintcode.com/problem/top-k-largest-numbers-ii/>

### Description

Implement a data structure, provide two interfaces:

1. `add(number)`. Add a new number in the data structure.
2. `topk()`. Return the top *k* largest numbers in this data structure. *k* is given when we create the data structure.

#### Example

```
s = new Solution(3);
>> create a new data structure.
s.add(3)
s.add(10)
s.topk()
>> return [10, 3]
s.add(1000)
s.add(-99)
s.topk()
>> return [1000, 10, 3]
s.add(4)
s.topk()
>> return [1000, 10, 4]
s.add(100)
s.topk()
>> return [1000, 100, 10]
```

## 题解

此题只用堆的话在最后的排序输出会比较难受，最后用 List 的排序也可以。

### Java

```java
public class Solution {
    private int k = -1;
    private Queue<Integer> heap = null;
    /*
    * @param k: An integer
    */public Solution(int k) {
        // do intialization if necessary
        this.k = k;
        heap = new PriorityQueue<Integer>(k);
    }

    /*
     * @param num: Number to be added
     * @return: nothing
     */
    public void add(int num) {
        // write your code here
        if (heap.size() < k) {
            heap.offer(num);
        } else if (heap.peek() < num) {
            heap.poll();
            heap.offer(num);
        }
    }

    /*
     * @return: Top k element
     */
    public List<Integer> topk() {
        // write your code here
        List<Integer> result = new ArrayList<>(k);
        Iterator<Integer> it = heap.iterator();
        while(it.hasNext()) {
            result.add(it.next());
        }
        result.sort(Collections.reverseOrder());
        return result;
    }
}
```

### 源码分析

略

### 复杂度分析

略