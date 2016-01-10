# Queue - 隊列

Queue 是一個 FIFO（First-in First-out, 先進先出）的資料結構，併發(concurrent)中經常使用，可以安全地將對象從一個任務傳給另一個任務。

## 程式碼實現

### Python

Queue 和 Stack 在 Python 中都是用 `list` ,`[]` 實現的。 在python 中list是一個dynamic array, 可以通過`append`在list的尾部添加元素， 通過`pop()`在list的尾部彈出元素實現`Stack`的`FILO`， 如果是`pop(0)`則彈出頭部的元素實現`Queue`的`FIFO`。
```python
queue = []  # same as list()
size = len(queue)
queue.append(1)
queue.append(2)
queue.pop(0) # return 1
queue[0] # return 2 examine the first element
```

#### Methods
| \ | methods |
| -- | -- |
| Insert | queue.append(e) |
| Remove | queue.pop(0) |
| Examine | queue[0] |

### Java

Queue 在 Java 中是 Interface, 一種實現是 LinkedList, LinkedList 向上轉型為 Queue, Queue 通常不能存儲 `null` 元素，否則與 `poll()` 等方法的返回值混淆。

```java
Queue<Integer> q = new LinkedList<Integer>();
int qLen = q.size(); // get queue length
```

#### Methods

| 0:0 | Throws exception | Returns special value |
| -- | -- | -- |
| Insert | add(e) | offer(e) |
| Remove | remove() | poll() |
| Examine | element() | peek() |

優先考慮右側方法，右側元素不存在時返回 `null`. 判斷非空時使用`isEmpty()`方法，繼承自 Collection.

## Priority Queue - 優先隊列

應用程式常常需要處理帶有優先級的業務，優先級最高的業務首先得到服務。因此優先隊列這種資料結構應運而生。優先隊列中的每個元素都有各自的優先級，優先級最高的元素最先得到服務；優先級相同的元素按照其在優先隊列中的順序得到服務。

優先隊列可以使用陣列或鏈表實現，從時間和空間覆雜度來說，往往用二叉堆(Binary heap)來實現。

### Python

Python 中提供`heapq`的lib來實現 priority queue. 提供`push`和`pop`兩個基本操作和`heapify`初始化操作.

| \ | methods | time complexity |
| -- | -- | -- |
| enqueue | heapq.push(queue, e) | $$O(\log n)$$ |
| dequeue | heapq.pop(queue) | $$O(\log n)$$ |
| init | heapq.heapify(queue) | $$O(n\log n)$$ |
| peek | queue[0]| $$O(1)$$ |


### Java

Java 中提供`PriorityQueue`類，該類是 Interface Queue 的另外一種實現，和`LinkedList`的區別主要在於排序行為而不是性能，基於 priority heap 實現，非`synchronized`，故多執行緒(Multi-thread)下應使用`PriorityBlockingQueue`. 預設為自然序（小根堆），需要其他排序方式可自行實現`Comparator`接口，選用合適的構造器初始化。使用叠代器遍歷時不保證有序，有序訪問時需要使用`Arrays.sort(pq.toArray())`.

不同方法的時間覆雜度：

- enqueuing and dequeuing: `offer`, `poll`, `remove()` and `add` - $$O(\log n)$$
- Object: `remove(Object)` and `contains(Object)` - $$O(n)$$
- retrieval: `peek`, `element`, and `size` - $$O(1)$$.

## Deque - 雙端隊列

雙端隊列（deque，全名double-ended queue）可以讓你在任何一端添加或者移除元素，因此它是一種具有隊列和堆疊性質的資料結構。

### Python

Python 的`list`就可以執行類似於`deque`的操作， 但是效率會過於慢。 為了提升數據的處理效率， 一些高效的資料結構放在了`collections`中。 在`collections` 中提供了`deque`的類， 如果需要多次對`list`執行頭尾元素的操作， 請使用`deque`。

```python
dq = collections.deque();
```

#### Methods

| \ | methods | time complexity |
| -- | -- | -- |
| enqueue left | dq.appendleft(e) | $$O(1)$$ |
| enqueue right | dq.append(e) | $$O(1)$$ |
| dequeue left | dq.popleft() | $$O(1)$$ |
| dequeue right | dq.pop() | $$O(1)$$ |
| peek left | dq[0] | $$O(1)$$ |
| peek right | dq[-1] | $$O(1)$$ |

### Java

Java 在1.6之後提供了 Deque 介面，既可使用`ArrayDeque`（陣列）來實現，也可以使用`LinkedList`（鏈表）來實現。前者是一個數組外加首尾索引，後者是雙向鏈表。

```java
Deque<Integer> deque = new ArrayDeque<Integer>();
```

#### Methods

<table>
  <tr>
    <td></td>
    <td colspan="2">First Element (Head)</td>
    <td colspan="2">Last Element (Tail)</td>
  </tr>
  <tr>
    <td></td>
    <td>Throws exception</td>
    <td>Special value</td>
    <td>Throws exception</td>
    <td>Special value</td>
  </tr>
  <tr>
    <td>Insert</td>
    <td>`addFirst(e)`</td>
    <td>`offerFirst(e)`</td>
    <td>`addLast(e)`</td>
    <td>`offerLast(e)`</td>
  </tr>
  <tr>
    <td>Remove</td>
    <td>`removeFirst()`</td>
    <td>`pollFirst()`</td>
    <td>`removeLast()`</td>
    <td>`pollLast()`</td>
  </tr>
  <tr>
    <td>Examine</td>
    <td>`getFirst()`</td>
    <td>`peekFirst()`</td>
    <td>`getLast()`</td>
    <td>`peekLast()`</td>
  </tr>
</table>

其中`offerLast`和 Queue 中的`offer`功能相同，都是從尾部插入。

## Reference

- [優先隊列 - 維基百科，自由的百科全書](http://zh.wikipedia.org/zh/%E5%84%AA%E5%85%88%E4%BD%87%E5%88%97)
- [雙端隊列 - 維基百科，自由的百科全書](https://zh.wikipedia.org/wiki/%E5%8F%8C%E7%AB%AF%E9%98%9F%E5%88%97)
